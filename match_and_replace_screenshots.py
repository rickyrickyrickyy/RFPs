#!/usr/bin/env python3
"""
Match screenshots in screenshots/ to gallery images by perceptual hash,
then replace gallery images with the best-matching screenshot (higher quality).
Each screenshot used at most once; each gallery image gets one replacement.
"""
import os
import re
import shutil
from pathlib import Path

from PIL import Image
import imagehash

REPO = Path(__file__).resolve().parent
SCREENSHOTS_DIR = REPO / "screenshots"

# Gallery images referenced in HTML (relative to REPO): (subdir, filename)
GALLERY_IMAGES = [
    # Overview slideshows (assembled in Overview/images; exploded/assembly-steps in Frame)
    ("Overview/images", "01.png"),
    ("Overview/images", "02.png"),
    ("Overview/images", "03.png"),
    ("Overview/images", "04.png"),
    ("Overview/images", "05.png"),
    ("Overview/images", "06.png"),
    ("Overview/images", "07.png"),
    ("Overview/images", "08.png"),
    ("Overview/images", "09.png"),
    ("Overview/images", "10.png"),
    ("Frame/exploded", "01.png"),
    ("Frame/exploded", "02.png"),
    ("Frame/exploded", "03.png"),
    ("Frame/exploded", "04.png"),
    ("Frame/exploded", "05.png"),
    ("Frame/exploded", "06.png"),
    ("Frame/exploded", "07.png"),
    ("Frame/exploded", "08.png"),
    ("Frame/subsystem-closeups", "01.png"),
    ("Frame/subsystem-closeups", "02.png"),
    ("Frame/subsystem-closeups", "03.png"),
    ("Frame/subsystem-closeups", "04.png"),
    ("Frame/subsystem-closeups", "05.png"),
    ("Frame/subsystem-closeups", "06.png"),
    ("Frame/subsystem-closeups", "07.png"),
    ("Frame/assembly-steps", "01.png"),
    ("Frame/assembly-steps", "02.png"),
    ("Frame/assembly-steps", "03.png"),
    ("Frame/assembly-steps", "04.png"),
    ("Frame/assembly-steps", "05.png"),
    # Other subsystem galleries
    ("Enclosure-shell/images", "covers-1.png"),
    ("Enclosure-shell/images", "covers-2.png"),
    ("Enclosure-shell/images", "covers-3.png"),
    ("Enclosure-shell/images", "covers-4.png"),
    ("Enclosure-shell/images", "covers-5.png"),
    ("Enclosure-shell/images", "covers-6.png"),
    ("Enclosure-shell/images", "covers-7.png"),
    ("Enclosure-shell/images", "covers-8.png"),
    ("Enclosure-shell/images", "covers-9.png"),
    ("Enclosure-shell/images", "covers-10.png"),
    ("Frame/Loads-and-load-paths/images", "overview-full-frame.png"),
    ("Frame/Loads-and-load-paths/images", "overview-three-interfaces.png"),
    ("Frame/Loads-and-load-paths/images", "overview-isometric-alt.png"),
    ("Frame/Loads-and-load-paths/images", "overview-perspective.png"),
    ("Frame/Loads-and-load-paths/images", "overview-front-six-feet.png"),
    ("Frame/Loads-and-load-paths/images", "overview-right-side.png"),
    ("Frame/Loads-and-load-paths/images", "overview-side-three-plates.png"),
    ("Outflow-disposal/images", "disposal-top-isometric.png"),
    ("Outflow-disposal/images", "disposal-chute-augers.png"),
    ("Outflow-disposal/images", "disposal-chute-only.png"),
    ("Outflow-disposal/images", "disposal-right-chute-core.png"),
    ("Outflow-disposal/images", "disposal-front-chute-frame.png"),
    ("Outflow-disposal/images", "disposal-right-u-channels.png"),
    ("Outflow-disposal/images", "disposal-alt-blue-orange.png"),
    ("Outflow-disposal/images", "disposal-alt-isometric.png"),
    ("Outflow-disposal/images", "disposal-red-core-teal-channels.png"),
    ("Drivetrain/images", "drivetrain-1.png"),
    ("Drivetrain/images", "drivetrain-2.png"),
    ("Drivetrain/images", "drivetrain-3.png"),
    ("Drivetrain/images", "drivetrain-4.png"),
    ("Drivetrain/images", "drivetrain-5.png"),
    ("Drivetrain/images", "drivetrain-6.png"),
    ("Collection/images", "collection-with-deflectors-1.png"),
    ("Collection/images", "collection-with-deflectors-2.png"),
    ("Collection/images", "collection-with-deflectors-3.png"),
    ("Collection/images", "collection-with-deflectors-4.png"),
    ("Collection/images", "collection-with-deflectors-5.png"),
    ("Collection/images", "collection-with-deflectors-6.png"),
    ("Collection/images", "collection-with-deflectors-7.png"),
    ("Collection/images", "collection-with-deflectors-8.png"),
    ("Collection/images", "collection-with-deflectors-9.png"),
    ("Collection/images", "collection-with-deflectors-10.png"),
    ("Extraction-syncronisation/images", "extraction-1.png"),
    ("Extraction-syncronisation/images", "extraction-2.png"),
    ("Extraction-syncronisation/images", "extraction-3.png"),
    ("Extraction-syncronisation/images", "extraction-4.png"),
    ("Extraction-syncronisation/images", "extraction-5.png"),
    ("Extraction-syncronisation/images", "extraction-6.png"),
    ("Extraction-syncronisation/images", "extraction-7.png"),
    ("Extraction-syncronisation/images", "extraction-8.png"),
    ("Extraction-syncronisation/images", "fruit-support-1.png"),
    ("Extraction-syncronisation/images", "fruit-support-2.png"),
    ("Extraction-syncronisation/images", "fruit-support-3.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-1.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-2.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-3.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-4.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-5.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-6.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-7.png"),
    ("Feeder/feeding-subassembly/images", "feeding-sub-8.png"),
    ("Plug-ejection/images", "plug-ejection-1.png"),
    ("Plug-ejection/images", "plug-ejection-2.png"),
    ("Plug-ejection/images", "plug-ejection-3.png"),
    ("Plug-ejection/images", "plug-ejection-4.png"),
    ("Plug-ejection/images", "plug-ejection-5.png"),
    ("Plug-ejection/images", "plug-ejection-6.png"),
    ("Transmission/images", "transmission-overview.png"),
    ("Transmission/images", "transmission-side.png"),
    ("Transmission/images", "transmission-isometric.png"),
    ("Transmission/images", "transmission-side-plate.png"),
    ("Transmission/images", "transmission-right.png"),
    ("Transmission/images", "transmission-side-yoke.png"),
    ("Transmission/images", "transmission-top.png"),
]


def phash(path):
    try:
        with Image.open(path) as img:
            return imagehash.phash(img)
    except Exception as e:
        print(f"  [skip hash {path}: {e}]")
        return None


def main():
    if not SCREENSHOTS_DIR.is_dir():
        print("No screenshots/ folder found.")
        return
    screenshot_files = sorted(SCREENSHOTS_DIR.glob("*.png"))
    if not screenshot_files:
        print("No PNGs in screenshots/.")
        return

    print("Hashing gallery images...")
    gallery_hashes = []
    for subdir, fname in GALLERY_IMAGES:
        path = REPO / subdir / fname
        if not path.exists():
            print(f"  Gallery missing: {path}")
            continue
        h = phash(path)
        if h is not None:
            gallery_hashes.append((path, subdir, fname, h))

    print("Hashing screenshots...")
    screenshot_hashes = []
    for p in screenshot_files:
        h = phash(p)
        if h is not None:
            screenshot_hashes.append((p, h))

    print("Matching (each gallery slot <- best remaining screenshot for that slot)...")
    # Per-slot assignment: for each gallery image, pick the best-matching screenshot
    # that hasn't been used yet. This keeps the right screenshot in the right slot.
    assigned_screenshot = set()
    mapping = []  # (gallery_path, screenshot_path, distance)
    for g_path, g_sub, g_name, g_h in gallery_hashes:
        best_si = None
        best_d = None
        for si, (s_path, s_h) in enumerate(screenshot_hashes):
            if si in assigned_screenshot:
                continue
            d = g_h - s_h
            if best_d is None or d < best_d:
                best_d = d
                best_si = si
        if best_si is not None:
            assigned_screenshot.add(best_si)
            s_path = screenshot_hashes[best_si][0]
            mapping.append((g_path, s_path, best_d))

    print(f"Assigned {len(mapping)} gallery images.")
    for g_path, s_path, dist in mapping:
        print(f"  {g_path.relative_to(REPO)} <- {s_path.name} (dist={dist})")
        shutil.copy2(s_path, g_path)
    print("Done. Gallery images replaced with best-matching screenshots.")
    if len(mapping) < len(gallery_hashes):
        print(f"  Warning: {len(gallery_hashes) - len(mapping)} gallery images had no assignment (not enough screenshots?).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
