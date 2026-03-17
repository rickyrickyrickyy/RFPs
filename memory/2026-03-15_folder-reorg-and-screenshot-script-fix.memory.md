## Folder reorg + reference fixes + screenshot script fix (2026-03-15)

### Folder changes (user did the moves)
- **Overview:** Assembled images moved out of `Overview/images/assembled/` into `Overview/images/` (flat: 01.png–10.png).
- **Frame:** Folders `assembly-steps` and `exploded` moved from Overview into Frame (`Frame/assembly-steps/`, `Frame/exploded/`). Subsystem closeups also live under Frame (`Frame/subsystem-closeups/`).
- **Loads and load paths:** Became a subfolder: `Frame/Loads-and-load-paths/` containing `Loads-and-load-paths.html` and `images/` (frame gallery images).

### Reference updates (done in repo)
- **Overview/index.html:** `images/assembled/` → `images/`.
- **Frame/index.html:** Exploded → `exploded/`, assembly-steps → `assembly-steps/`, subsystem-closeups → `subsystem-closeups/`; link to Loads page → `Loads-and-load-paths/Loads-and-load-paths.html`.
- **Root index.html + README.md:** Link to Loads page → `Frame/Loads-and-load-paths/Loads-and-load-paths.html`.
- **Frame/Loads-and-load-paths/Loads-and-load-paths.html:** Back to Frame `index.html` → `../index.html`; P6 overview → `../../index.html`; sibling sections (Drivetrain, etc.) → `../../Section/`.
- **match_and_replace_screenshots.py:** Path list updated: assembled → `Overview/images`, exploded → `Frame/exploded`, assembly-steps → `Frame/assembly-steps`, subsystem-closeups → `Frame/subsystem-closeups`, Frame gallery → `Frame/Loads-and-load-paths/images`.

### Screenshot script behaviour fix
- **Problem:** Script used global greedy assignment: it sorted *all* (gallery, screenshot) pairs by distance and assigned in that order. The single best-matching screenshot could end up in the wrong slot (e.g. best match for 01.png assigned to 05.png).
- **Fix:** Per-slot assignment. For each gallery image in order, pick the best-matching *unused* screenshot for *that* gallery image. Each slot now gets the replacement that best matches that slot’s content; each screenshot still used at most once.
