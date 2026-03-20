#!/usr/bin/env python3
"""Download Argos Translate models for en->zh and en->pt (offline translation, no API limits)."""
from __future__ import annotations

import sys


def main() -> int:
    try:
        import argostranslate.package
    except ImportError:
        print("ERROR: pip install argostranslate")
        return 1

    argostranslate.package.update_package_index()
    available = argostranslate.package.get_available_packages()
    want = [("en", "zh"), ("en", "pt")]
    for fr, to in want:
        pkg = next((p for p in available if p.from_code == fr and p.to_code == to), None)
        if not pkg:
            print(f"WARN: no package for {fr}->{to}")
            continue
        print(f"Installing {pkg.from_code}->{pkg.to_code} ...")
        path = pkg.download()
        argostranslate.package.install_from_path(path)
        print(f"OK: {pkg.from_code}->{pkg.to_code}")
    print("Done. Run: python tools/build_i18n.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
