#!/usr/bin/env python3
"""
Process HTML: inject viewport, site.css. English-only; no language switcher.

Run from repo root: python tools/build_i18n.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_TOP = {"zh", "pt", "assets", "tools", ".git", "node_modules", ".cursor"}


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


def finish_page(content: str, relpath: str) -> str:
    c = strip_inject(content)
    c = ensure_viewport(c)
    c = inject_head(c, assets_prefix(relpath))
    return c


def main() -> int:
    files = list_english_html()
    for src in files:
        rel = rel_posix(src)
        raw = src.read_text(encoding="utf-8")
        raw = strip_inject(raw)
        raw = fix_plug_images(raw, rel)
        out = finish_page(raw, rel)
        src.write_text(out, encoding="utf-8")
    print(f"OK: {len(files)} pages (English only)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
