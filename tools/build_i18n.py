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

UI_ZH = [
    ("Recommended figures (contractor clarity)", "建议补充图示（便于承包商理解）"),
    ("Recommended figures", "建议补充图示"),
    ("with content", "有内容"),
    ("to be completed", "待完成"),
    ("skeleton", "骨架页"),
    ("What's filled in (highlights)", "已完成内容摘要"),
    ("Bill of materials (BOM)", "物料清单（BOM）"),
    ("Questions for RFP", "RFP 问题清单"),
    ("Delijuice extraction cycle", "Delijuice 压榨循环"),
    ("Project overview", "项目概览"),
    ("P6 RFP overview", "P6 RFP 总览"),
    ("← Back to P6 RFP overview", "← 返回 P6 RFP 总览"),
    ("← Back to", "← 返回"),
    ("Subpages", "子页面"),
    ("Subsystems", "子系统"),
    ("Reference", "参考"),
    ("Introduction", "简介"),
    ("Figures", "图示"),
    ("Discussion", "讨论"),
    ("Components", "部件"),
    ("Interfaces and tolerances", "接口与公差"),
    ("Colour key", "颜色说明"),
    ("Status", "状态"),
    ("Scope", "范围"),
    ("More", "更多"),
    ("Future developments", "后续开发"),
    ("Last updated:", "最后更新："),
    ("Language:", "语言："),
    ("Skip to content", "跳到正文"),
]
UI_PT = [
    ("Recommended figures (contractor clarity)", "Figuras recomendadas (clareza para o contratado)"),
    ("Recommended figures", "Figuras recomendadas"),
    ("with content", "com conteúdo"),
    ("to be completed", "a concluir"),
    ("skeleton", "esqueleto"),
    ("What's filled in (highlights)", "Destaques do que já está preenchido"),
    ("Bill of materials (BOM)", "Lista de materiais (BOM)"),
    ("Questions for RFP", "Perguntas para o RFP"),
    ("Delijuice extraction cycle", "Ciclo de extração Delijuice"),
    ("Project overview", "Visão geral do projeto"),
    ("P6 RFP overview", "Visão geral do RFP P6"),
    ("← Back to P6 RFP overview", "← Voltar à visão geral do RFP P6"),
    ("← Back to", "← Voltar a"),
    ("Subpages", "Subpáginas"),
    ("Subsystems", "Subsistemas"),
    ("Reference", "Referência"),
    ("Introduction", "Introdução"),
    ("Figures", "Figuras"),
    ("Discussion", "Discussão"),
    ("Components", "Componentes"),
    ("Interfaces and tolerances", "Interfaces e tolerâncias"),
    ("Colour key", "Legenda de cores"),
    ("Status", "Estado"),
    ("Scope", "Âmbito"),
    ("More", "Mais"),
    ("Future developments", "Desenvolvimentos futuros"),
    ("Last updated:", "Última atualização:"),
    ("Language:", "Idioma:"),
    ("Skip to content", "Ir para o conteúdo"),
]


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


def apply_ui_dict(html: str, pairs: list[tuple[str, str]]) -> str:
    for en, loc in pairs:
        html = html.replace(en, loc)
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
) -> str:
    c = strip_inject(content)
    c = ensure_viewport(c)
    c = set_html_lang(c, lang)
    c = inject_head(c, assets_prefix(bar_relpath))
    c = inject_body(c, lang_bar(bar_relpath, lang))
    if ui_pairs:
        c = apply_ui_dict(c, ui_pairs)
    return c


def main() -> int:
    files = list_english_html()
    for src in files:
        rel = rel_posix(src)
        raw = src.read_text(encoding="utf-8")
        raw = strip_inject(raw)
        raw = fix_plug_images(raw, rel)

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
        zh_dest.write_text(finish_page(zh_body, zh_rel, "zh", UI_ZH), encoding="utf-8")
        pt_dest.write_text(finish_page(pt_body, pt_rel, "pt", UI_PT), encoding="utf-8")

    print(f"OK: {len(files)} pages -> en + zh/ + pt/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
