# Overview slideshows and assembly steps (2026-03-17)

## What was done

- **Overview page** (`Overview/index.html`): Added and expanded slideshows for the P6 project overview.
- **Exploded views:** Extended from 8 to 10 figures; added `images/exploded/09.png` and `10.png` (full-assembly explodes).
- **Subsystem closeups** (new section): Four slideshows with images under `Overview/images/`:
  - **Plunger driver, collection, plunger** — 3 images (`plunger-collection-plunger/`)
  - **Yoke, drivetrain, extraction synchronisation** — 3 images (`yoke-drivetrain-extraction/`)
  - **Shell and hinges to mount plates** — 4 images (`shell-hinges/`)
  - **Plunger drive system placed between mount plates** — 3 images (`plunger-drive-mount-plates/`)
- **Assembly steps** (new section): One slideshow, 4 figures showing sub-assemblies being placed onto the frame (`assembly-steps/`).
- All slideshows use the same pattern: container id, `.slideshow-track`, `.slide` with `data-caption`, caption element, prev/next buttons, counter; script calls `initSlideshow(id)` for each.

## Image layout

- `Overview/images/assembled/` — top-level assembled views
- `Overview/images/exploded/` — 01–10.png
- `Overview/images/plunger-collection-plunger/`, `yoke-drivetrain-extraction/`, `shell-hinges/`, `plunger-drive-mount-plates/`, `assembly-steps/` — one folder per closeup/sequence, numbered 01, 02, …

## For future edits

- To add another slideshow: add a section with the same HTML structure, give it a unique id (e.g. `xyz-slideshow`), and add `initSlideshow('xyz-slideshow')` in the script at the bottom of `Overview/index.html`.
