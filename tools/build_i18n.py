#!/usr/bin/env python3
"""
Mirror HTML into zh/ and pt/, inject mobile CSS + language switcher.
Translate all visible text (body strings + alt/title/data-caption/aria-label/placeholder)
using Google Translate (fallback: MyMemory). Requires: pip install beautifulsoup4 deep-translator lxml

Run from repo root: python tools/build_i18n.py

Note: Machine translation — have a native speaker review for production RFPs.
If Google rate-limits you, run `python tools/install_argos_models.py` once (offline Argos
models), then rebuild — Argos is used automatically when en→zh / en→pt packages are installed.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import threading
import time
from pathlib import Path

_WARN_KEYS: set[str] = set()
_CACHE_LOCK = threading.Lock()
# Serialize calls to free translation APIs (avoid parallel ZH+PT tripping rate limits)
_TRANSLATE_API_LOCK = threading.Lock()

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_TOP = {"zh", "pt", "assets", "tools", ".git", "node_modules", ".cursor"}

# Optional post-pass: fix common UI strings if MT is awkward (applied after translation)
UI_FIX_ZH: list[tuple[str, str]] = [
    ("← ", "← "),
]
UI_FIX_PT: list[tuple[str, str]] = []


def list_english_html() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT)
        if not rel.parts or rel.parts[0] in EXCLUDE_TOP:
            continue
        out.append(p)
    return sorted(out)


def rel_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def english_tail_from_any(relpath: str) -> str:
    parts = Path(relpath).parts
    if parts and parts[0] in ("zh", "pt"):
        return "/".join(parts[1:])
    return relpath


def lang_hrefs_for_page(page_relpath: str) -> tuple[str, str, str]:
    tail = english_tail_from_any(page_relpath)
    eng_file = ROOT / tail
    zh_file = ROOT / "zh" / tail
    pt_file = ROOT / "pt" / tail
    from_dir = ROOT / Path(page_relpath).parent

    def rel_to(target: Path) -> str:
        return os.path.relpath(target, from_dir).replace("\\", "/")

    return rel_to(eng_file), rel_to(zh_file), rel_to(pt_file)


def lang_bar(relpath: str, current: str) -> str:
    he, hz, hp = lang_hrefs_for_page(relpath)
    lab = "Language:" if current == "en" else ("语言：" if current == "zh" else "Idioma:")

    def link(href: str, text: str, is_cur: bool) -> str:
        cur = ' aria-current="page"' if is_cur else ""
        return f'<a href="{href}"{cur}>{text}</a>'

    return (
        '<nav class="site-lang-bar" aria-label="Language">\n'
        f'  <span class="lang-label">{lab}</span>\n'
        f"  {link(he, 'English', current == 'en')}\n"
        f'  <span aria-hidden="true">·</span>\n'
        f"  {link(hz, '中文', current == 'zh')}\n"
        f'  <span aria-hidden="true">·</span>\n'
        f"  {link(hp, 'Português', current == 'pt')}\n"
        "</nav>\n"
    )


def fix_plug_images(html: str, relpath: str) -> str:
    if "Plug-ejection" not in relpath.replace("\\", "/"):
        return html
    return html.replace('src="../../images/plug-ejection-', 'src="../images/plug-ejection-')


def strip_inject(html: str) -> str:
    html = re.sub(r'<link[^>]*assets/site\.css[^>]*>\s*', "", html)
    html = re.sub(r'<nav class="site-lang-bar"[^>]*>[\s\S]*?</nav>\s*', "", html)
    return html


def ensure_viewport(html: str) -> str:
    if 'name="viewport"' in html or "name='viewport'" in html:
        return html
    return re.sub(
        r'(<meta\s+charset="UTF-8"\s*>)',
        r'\1\n  <meta name="viewport" content="width=device-width, initial-scale=1">',
        html,
        count=1,
    )


def set_html_lang(html: str, lang: str) -> str:
    val = "zh-Hans" if lang == "zh" else ("pt" if lang == "pt" else "en")
    if re.search(r"<html\s+lang=", html):
        return re.sub(r'<html\s+lang="[^"]*"', f'<html lang="{val}"', html, count=1)
    return re.sub(r"<html(\s)", rf'<html lang="{val}"\1', html, count=1)


def assets_prefix(relpath: str) -> str:
    depth = len(Path(relpath).parent.parts)
    return ("../" * depth) if depth else ""


def inject_head(html: str, css_href: str) -> str:
    if "assets/site.css" in html:
        html = strip_inject(html)
    block = f'  <link rel="stylesheet" href="{css_href}assets/site.css">\n'
    if "</head>" in html:
        return html.replace("</head>", block + "</head>", 1)
    return html


def inject_body(html: str, bar: str) -> str:
    return re.sub(r"(<body[^>]*>)", r"\1\n" + bar, html, count=1)


def apply_ui_fix(html: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        if a != b:
            html = html.replace(a, b)
    return html


def should_relink(url: str) -> bool:
    u = url.strip()
    if not u or u.startswith("#") or u.startswith("javascript:"):
        return False
    if u.startswith("http://") or u.startswith("https://") or u.startswith("mailto:"):
        return False
    return True


def target_under_root(abs_path: Path) -> bool:
    try:
        abs_path.resolve().relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


def map_target_to_lang(abs_target: Path, lang: str) -> Path:
    try:
        rel = abs_target.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return abs_target
    parts = rel.parts
    if parts and parts[0] in ("zh", "pt", "assets", "tools"):
        return abs_target
    if lang not in ("zh", "pt"):
        return abs_target
    suf = abs_target.suffix.lower()
    if suf == ".html":
        return ROOT / lang / rel
    if abs_target.is_dir():
        return ROOT / lang / rel
    return abs_target


def retarget_attr(url: str, english_file: Path, dest_file: Path, lang: str) -> str:
    if not should_relink(url):
        return url
    from_dir = english_file.parent
    to_dir = dest_file.parent
    try:
        raw = (from_dir / url).resolve()
    except (OSError, ValueError):
        return url
    if not target_under_root(raw):
        return url
    if raw.is_dir():
        idx = raw / "index.html"
        raw = idx if idx.is_file() else raw
    mapped = map_target_to_lang(raw, lang)
    try:
        new_u = os.path.relpath(mapped, to_dir).replace("\\", "/")
    except ValueError:
        return url
    if mapped.is_dir() and url.endswith("/"):
        new_u = new_u.rstrip("/") + "/"
    return new_u


def retarget_all_links(html: str, english_relpath: str, dest_relpath: str, lang: str) -> str:
    eng = ROOT / english_relpath
    dest = ROOT / dest_relpath

    def sub(m: re.Match) -> str:
        attr, q, url = m.group(1), m.group(2), m.group(3)
        new = retarget_attr(url, eng, dest, lang)
        return f'{attr}={q}{new}{q}'

    return re.sub(r'(href|src)=(["\'])([^"\']+)\2', sub, html)


# --- Translation -------------------------------------------------------------

TRANSLATE_ATTRS = ("alt", "title", "aria-label", "placeholder", "data-caption")


def _google_target(lang: str) -> str:
    return "zh-CN" if lang == "zh" else "pt"


def _warn_short(key: str, msg: str) -> None:
    if key in _WARN_KEYS:
        return
    _WARN_KEYS.add(key)
    try:
        sys.stderr.write(f"WARN [{key}]: {msg[:200]}\n")
    except Exception:
        pass


def _try_argos_translate(text: str, lang: str) -> str | None:
    """Local offline translation — no rate limits if models installed (see tools/install_argos_models.py)."""
    try:
        import argostranslate.translate as ar

        to_code = "zh" if lang == "zh" else "pt"
        tr = ar.get_translation_from_codes("en", to_code)
        if tr is None:
            return None
        out = tr.translate(text)
        return out if out and out.strip() else None
    except Exception:
        return None


def _translate_chunk(text: str, lang: str) -> str:
    if not text.strip():
        return text
    argos_out = _try_argos_translate(text, lang)
    if argos_out is not None:
        return argos_out

    tgt_g = _google_target(lang)
    mm_tgt = "chinese simplified" if lang == "zh" else "portuguese brazil"
    last_err: str | None = None
    from deep_translator import GoogleTranslator, MyMemoryTranslator

    delay = float(os.environ.get("RFP_TRANSLATE_DELAY", "0.2"))
    google_first = os.environ.get("RFP_GOOGLE_FIRST", "0").strip() in ("1", "true", "yes")

    def try_mm() -> str | None:
        nonlocal last_err
        try:
            out = MyMemoryTranslator(source="english", target=mm_tgt).translate(text)
            if out is not None and out.strip():
                return out
        except Exception as e:
            last_err = str(e)[:200]
        return None

    def try_gg() -> str | None:
        nonlocal last_err
        try:
            out = GoogleTranslator(source="auto", target=tgt_g).translate(text)
            if out is not None and out.strip():
                return out
        except Exception as e:
            last_err = str(e)[:200]
        return None

    with _TRANSLATE_API_LOCK:
        for attempt in range(3):
            out = None
            if google_first:
                out = try_gg()
                if out:
                    time.sleep(delay)
                    return out
                time.sleep(0.8 + attempt * 0.5)
                out = try_mm()
            else:
                out = try_mm()
                if out:
                    time.sleep(delay)
                    return out
                time.sleep(0.8 + attempt * 0.5)
                out = try_gg()
            if out:
                time.sleep(delay)
                return out
            time.sleep(0.8 + attempt * 0.5)

        if last_err:
            _warn_short("translate_fail", last_err)
        return text


def translate_cached(text: str, lang: str, cache: dict[tuple[str, str], str]) -> str:
    key = (lang, text)
    with _CACHE_LOCK:
        if key in cache:
            return cache[key]
    stripped = text.strip()
    if not stripped:
        with _CACHE_LOCK:
            cache[key] = text
        return text
    # Keep common non-translatable tokens short-circuit (URLs alone, hex colours)
    if stripped.startswith("http://") or stripped.startswith("https://"):
        if " " not in stripped:
            with _CACHE_LOCK:
                cache[key] = text
            return text
    if re.fullmatch(r"#[0-9A-Fa-f]{3,8}", stripped):
        with _CACHE_LOCK:
            cache[key] = text
        return text

    max_len = 4500
    if len(text) <= max_len:
        out = _translate_chunk(text, lang)
    else:
        parts_out: list[str] = []
        buf = ""
        for line in text.split("\n"):
            if len(buf) + len(line) + 1 > max_len and buf:
                parts_out.append(_translate_chunk(buf, lang))
                buf = line
            else:
                buf = buf + "\n" + line if buf else line
        if buf.strip():
            parts_out.append(_translate_chunk(buf, lang))
        out = "\n".join(parts_out)

    if out is None:
        out = text
    with _CACHE_LOCK:
        if key not in cache:
            cache[key] = out
        return cache[key]


def translate_mermaid_labels(pre_text: str, lang: str, cache: dict) -> str:
    def repl(m: re.Match) -> str:
        inner = m.group(1)
        if not inner.strip():
            return m.group(0)
        t = translate_cached(inner, lang, cache)
        return "[" + (t if t is not None else inner) + "]"

    return re.sub(r"\[([^\]]+)\]", repl, pre_text)


def translate_html_document(html: str, lang: str, cache: dict) -> str:
    from bs4 import BeautifulSoup, Comment

    soup = BeautifulSoup(html, "lxml")

    title = soup.find("title")
    if title:
        t = title.get_text()
        if t.strip():
            title.clear()
            title.append(translate_cached(t, lang, cache))

    body = soup.find("body")
    if not body:
        out = str(soup)
        if not out.lstrip().lower().startswith("<!doctype"):
            out = "<!DOCTYPE html>\n" + out
        return out

    # Attributes on body subtree
    for tag in body.find_all(True):
        for attr in TRANSLATE_ATTRS:
            val = tag.get(attr)
            if val and isinstance(val, str) and val.strip():
                nv = translate_cached(val, lang, cache)
                if nv is not None:
                    tag[attr] = nv

    # Snapshot text nodes (avoid mutation during iteration issues)
    text_nodes: list = []
    for element in body.find_all(string=True):
        if isinstance(element, Comment):
            continue
        parent = element.parent
        if parent is None:
            continue
        if parent.name in ("script", "style", "noscript"):
            continue
        anc_pre = parent if parent.name == "pre" else parent.find_parent("pre")
        if anc_pre and anc_pre.get("class") and "mermaid" in anc_pre.get("class", []):
            continue
        if str(element).strip():
            text_nodes.append(element)

    for element in text_nodes:
        if getattr(element, "parent", None) is None:
            continue
        old = str(element)
        new = translate_cached(old, lang, cache)
        if new is None or new == "":
            new = old
        if new != old:
            element.replace_with(new)

    # Mermaid: translate [...] labels only
    for pre in body.find_all("pre", class_=lambda c: c and "mermaid" in c):
        raw = pre.get_text()
        if raw.strip():
            pre.clear()
            pre.append(translate_mermaid_labels(raw, lang, cache))

    out = str(soup)
    if not out.lstrip().lower().startswith("<!doctype"):
        out = "<!DOCTYPE html>\n" + out
    return out


def finish_page(content: str, page_relpath: str, lang: str) -> str:
    c = strip_inject(content)
    c = ensure_viewport(c)
    c = set_html_lang(c, lang)
    c = inject_head(c, assets_prefix(page_relpath))
    c = inject_body(c, lang_bar(page_relpath, lang))
    return c


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    ap = argparse.ArgumentParser(description="Build en + zh + pt HTML mirrors with MT")
    ap.add_argument("--limit", type=int, default=0, help="Process only first N pages (0 = all)")
    ap.add_argument(
        "--no-translate",
        action="store_true",
        help="Mirror zh/pt with English text only (structure + lang bar test)",
    )
    args = ap.parse_args()

    try:
        import bs4  # noqa: F401
    except ImportError:
        print("ERROR: pip install beautifulsoup4 deep-translator lxml")
        return 1

    files = list_english_html()
    if args.limit and args.limit > 0:
        files = files[: args.limit]

    cache_zh: dict = {}
    cache_pt: dict = {}
    n = len(files)
    for i, src in enumerate(files, 1):
        rel = rel_posix(src)
        raw = src.read_text(encoding="utf-8")
        raw = strip_inject(raw)
        raw = fix_plug_images(raw, rel)

        en_out = finish_page(raw, rel, "en")
        src.write_text(en_out, encoding="utf-8")

        zh_rel = f"zh/{rel}"
        pt_rel = f"pt/{rel}"
        zh_body = retarget_all_links(raw, rel, zh_rel, "zh")
        pt_body = retarget_all_links(raw, rel, pt_rel, "pt")

        print(f"[{i}/{n}] Translating ZH+PT: {rel} ...", flush=True)
        if args.no_translate:
            zh_html, pt_html = zh_body, pt_body
        else:
            zh_html = translate_html_document(zh_body, "zh", cache_zh)
            pt_html = translate_html_document(pt_body, "pt", cache_pt)

        zh_html = apply_ui_fix(zh_html, UI_FIX_ZH)
        zh_dest = ROOT / zh_rel
        zh_dest.parent.mkdir(parents=True, exist_ok=True)
        zh_dest.write_text(finish_page(zh_html, zh_rel, "zh"), encoding="utf-8")

        pt_html = apply_ui_fix(pt_html, UI_FIX_PT)
        pt_dest = ROOT / pt_rel
        pt_dest.parent.mkdir(parents=True, exist_ok=True)
        pt_dest.write_text(finish_page(pt_html, pt_rel, "pt"), encoding="utf-8")

    mode = "structure only (English in zh/pt)" if args.no_translate else "full MT"
    print(f"OK: {n} pages -> en + zh/ + pt/ ({mode}). Cache zh={len(cache_zh)} pt={len(cache_pt)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
