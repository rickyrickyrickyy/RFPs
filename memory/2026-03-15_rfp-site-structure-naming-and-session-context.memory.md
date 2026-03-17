# RFP site structure, naming, and session context (2026-03-15)

## Canonical naming (use everywhere)

- **Subsystem 6:** **Fruit intake system** (folder still `Feeder/`). Not "Intake feeder system" in nav; label is "Fruit intake system".
- **Subsystem 7:** **Core ejection** (folder `Plug-ejection/`). Not "Plug ejection". Part name "plug cutter" is kept; the ejected item and subsystem label are "core".
- **Subsystem 8:** **Disposal system** (folder `Outflow-disposal/`). Not "Outflow / disposal" in nav; label is "Disposal system".

Use these in index.html, Overview, subsystem pages, Frame/How-subassemblies-fit, Delijuice cycle, BOM, Questions-for-RFP, and any new content.

## Main index (index.html) structure

- **Preamble:** Introduction (P6, JX, CAD colours, "use links below") at top; no separate "Overview" section at bottom.
- **Reference:** Project overview, Delijuice extraction cycle, Questions for RFP, BOM. No "How subassemblies fit together" in Reference (it lives under Frame).
- **Subsystems 1–11:** Frame (with How subassemblies fit, Loads and load paths, Assembly process), Drivetrain, Transmission, Collection, Extraction & sync, **Fruit intake system**, **Core ejection**, **Disposal system**, Enclosure, CIP (with sub-items), Controls and electronics (with sub-items).
- **General & integration:** General design and manufacturing (with content), Third-party.
- **Future developments:** Section at end before footer (yoke position, CIP, third-party, manufacturability, SolidWorks).

## Key pages and locations

- **Delijuice cycle:** `Overview/Delijuice-cycle.html` — four steps (fruit intake, compression, juice outflow, core expulsion); reverse stroke = intake + core expulsion, forward = compression + juice outflow. Terminology: core (not plug) in body text; "plug cutter" kept as part name.
- **How subassemblies fit together:** now merged into `Frame/index.html` (anchor `#how-subassemblies-fit-together`).
- **Loads and load paths:** `Frame/Loads-and-load-paths.html` — drivetrain, transmission, extraction, core ejection reaction loads and paths to floor.
- **Project overview:** `Overview/index.html` — top-level assemblies image (placeholder `Overview/images/top-level-assemblies.png`), What P6 is, How the machine works (link to Delijuice cycle), Subsystems list, General design/food-safety, Third-party.
- **Controls and electronics:** User control panel (E-stop, on/off, start/stop, indicators), Safety switches (3 lids), Motor control and power (AC contactor, starter, WEG W22), Yoke position sensor (TBD).
- **General design and manufacturing:** Material selection, Manufacturing method, Fastener and assembly process, Tolerancing, Post-processing, CAD Inventor→SolidWorks; cross-link to Overview for food-safety.

## Fruit support image

- Replaced schematic with user-provided image: `Extraction-syncronisation/images/fruit-support-1.png` (same path as previous fig1; image file overwritten so slideshow uses new image).

## Session summary (this conversation)

- Renames applied site-wide (Fruit intake, Core ejection, Disposal); plug→core in prose; "plug cutter" unchanged.
- Marceline persistent-memory strategy: repo-based memory, new rule to load context for RFP work and offer to save memory; README and marceline.md updated; memory files created for training and how-to-work.
- Changes pushed to main where requested; other edits committed in repo.

## Website clarity note

- The public HTML pages should not link to internal `.md` “source” files at the bottom, to avoid confusing readers. Keep sources in the repo for editing, but don’t surface them on the website unless explicitly requested.
