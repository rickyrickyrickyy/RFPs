#!/usr/bin/env python3
"""
Mirror HTML into zh/ and pt/, inject mobile + language switcher.
Rewrites relative href/src so zh/pt pages resolve images and internal links correctly.

Run from repo root: python tools/build_i18n.py
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_TOP = {"zh", "pt", "assets", "tools", ".git", "node_modules", ".cursor"}

# Import translations (tools/ is script dir when run as python tools/build_i18n.py)
sys.path.insert(0, str(ROOT))
from tools.translations import get_ui_zh, get_ui_pt, get_content_with_hrefs_zh, get_content_with_hrefs_pt

UI_ZH = get_ui_zh()
UI_PT = get_ui_pt()
CONTENT_WITH_HREFS_ZH = get_content_with_hrefs_zh()
CONTENT_WITH_HREFS_PT = get_content_with_hrefs_pt()


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
    """
    Relative hrefs from this page's directory to the en / zh / pt copies of the same page.
    Fixes e.g. zh/index.html: Chinese must be index.html, not ../zh/index.html.
    """
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


def normalize_quotes(html: str) -> str:
    """Normalize curly/smart quotes to straight quotes so translations match."""
    return (
        html.replace("\u201c", '"')  # "
        .replace("\u201d", '"')  # "
        .replace("\u2018", "'")  # '
        .replace("\u2019", "'")  # '
    )


def strip_inject(html: str) -> str:
    html = re.sub(r'<link[^>]*assets/site\.css[^>]*>\s*', "", html)
    html = re.sub(r'<nav class="site-lang-bar"[^>]*>[\s\S]*?</nav>\s*', "", html)
    return html


def ensure_viewport(html: str) -> str:
    if "name=\"viewport\"" in html or "name='viewport'" in html:
        return html
    return re.sub(
        r"(<meta\s+charset=\"UTF-8\"\s*>)",
        r'\1\n  <meta name="viewport" content="width=device-width, initial-scale=1">',
        html,
        count=1,
    )


def set_html_lang(html: str, lang: str) -> str:
    val = "zh-Hans" if lang == "zh" else ("pt" if lang == "pt" else "en")
    if re.search(r"<html\s+lang=", html):
        return re.sub(r"<html\s+lang=\"[^\"]*\"", f'<html lang="{val}"', html, count=1)
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


def protect_url_attributes(html: str) -> tuple[str, list[str]]:
    """Replace href/src values with placeholders so translation doesn't corrupt paths."""
    urls: list[str] = []

    def repl(m: re.Match) -> str:
        attr, q, val = m.group(1), m.group(2), m.group(3)
        urls.append(val)
        return f'{attr}={q}__URL_{len(urls)-1}__{q}'

    html = re.sub(r'(href|src)=(["\'])([^"\']+)\2', repl, html)
    return html, urls


def restore_url_attributes(html: str, urls: list[str]) -> str:
    for i, url in enumerate(urls):
        html = html.replace(f'__URL_{i}__', url)
    return html


def apply_ui_dict(
    html: str,
    pairs: list[tuple[str, str]],
    content_with_hrefs: list[tuple[str, str]] | None = None,
) -> str:
    """Apply translations. Content with hrefs is applied first (before URL protection)."""
    content_en = set()
    if content_with_hrefs:
        for en, loc in content_with_hrefs:
            html = html.replace(en, loc)
            content_en.add(en)
    html, urls = protect_url_attributes(html)
    for en, loc in pairs:
        if en not in content_en:
            html = html.replace(en, loc)
    return restore_url_attributes(html, urls)


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
    """HTML pages live under zh/ or pt/; images and other assets stay in the English tree."""
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


def finish_page(
    content: str,
    bar_relpath: str,
    lang: str,
    ui_pairs: list[tuple[str, str]] | None,
    content_with_hrefs: list[tuple[str, str]] | None = None,
) -> str:
    c = strip_inject(content)
    c = ensure_viewport(c)
    c = set_html_lang(c, lang)
    c = inject_head(c, assets_prefix(bar_relpath))
    c = inject_body(c, lang_bar(bar_relpath, lang))
    if ui_pairs:
        c = apply_ui_dict(c, ui_pairs, content_with_hrefs)
    return c


def main() -> int:
    files = list_english_html()
    for src in files:
        rel = rel_posix(src)
        raw = src.read_text(encoding="utf-8")
        raw = strip_inject(raw)
        raw = fix_plug_images(raw, rel)
        raw = normalize_quotes(raw)

        en_out = finish_page(raw, rel, "en", None)
        src.write_text(en_out, encoding="utf-8")

        zh_rel = f"zh/{rel}"
        pt_rel = f"pt/{rel}"
        zh_body = retarget_all_links(raw, rel, zh_rel, "zh")
        pt_body = retarget_all_links(raw, rel, pt_rel, "pt")

        zh_dest = ROOT / zh_rel
        pt_dest = ROOT / pt_rel
        zh_dest.parent.mkdir(parents=True, exist_ok=True)
        pt_dest.parent.mkdir(parents=True, exist_ok=True)
        zh_dest.write_text(finish_page(zh_body, zh_rel, "zh", UI_ZH, CONTENT_WITH_HREFS_ZH), encoding="utf-8")
        pt_dest.write_text(finish_page(pt_body, pt_rel, "pt", UI_PT, CONTENT_WITH_HREFS_PT), encoding="utf-8")

    print(f"OK: {len(files)} pages -> en + zh/ + pt/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
