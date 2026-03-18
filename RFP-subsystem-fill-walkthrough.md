# RFP fill walkthrough — subsystem by subpage (design assistance for contractors)

These RFPs go to **contractors to help you finish the design**, not only to quote a frozen drawing set. You already have **rough CAD for all parts**; what’s missing is honest capture of **known issues, DFM problems, optimizations you want, unknowns, and China supply-chain reality**—so contractors can propose fixes, alternates, and sourcing.

Use this with **Marceline** when you want to flush out the site **without losing focus**. Marceline runs **one stop at a time** (main page first, then each subpage), walks through the checklist below, and only advances when you say **next**, **done**, or **skip**.

**How to start (say to Marceline):**  
*“Marceline, walk me through filling **[subsystem name]** — one subpage at a time.”*

**Discipline:** One subpage per session chunk unless you explicitly ask to batch. Offer to save progress to `memory/` after each subsystem.

---

## What this RFP is asking contractors for

| You provide | You want back |
|-------------|----------------|
| Rough geometry, interfaces, function | **DFM** feedback (weld access, bend radii, stock sizes, tolerance relaxations) |
| Known pain points & WIP areas | **Proposed optimizations** (weight, cost, lead time, assembly steps) |
| Explicit **unknowns** & questions | Answers or **options** with trade-offs |
| Food / hygiene / load context | **Material & finish** choices that work in CN supply |
| Purchased-part intent (or “equivalent OK”) | **Sourcing**: local equivalents, lead times, MOQs |

If a topic is empty, say so on the page: *“No known issues yet”* or *“Contractor to flag DFM concerns.”* That still helps—they know the boundary.

---

## Content buckets (every stop — main page or subpage)

For **each** HTML page, work through these so contractors can help **design**, not just manufacture:

### A — Baseline (what exists today)

| Bucket | What to capture |
|--------|-----------------|
| **Function & context** | What it does, when in the cycle, what must not fail. |
| **Rough design status** | “CAD exists; not release for fab” or similar—sets expectation. |
| **Environment** | Food / splash / CIP / washdown / vibration / temp. |
| **Loads / motion** | Forces, cycles, speeds—even rough or “contractor to validate”. |
| **Interfaces** | Every mate: subsystem links, datums, tube sizes, electrical if any. |
| **Figures** | Which views to add under `images/`; what’s misleading vs intent. |

### B — Known issues & risks (be blunt)

| Bucket | What to capture |
|--------|-----------------|
| **Known issues** | Binding, wear, noise, leaks, alignment drift, collision, cleaning dead zones, things you’ve already seen on prototype or in CAD. |
| **WIP / unstable** | Parts you’re still changing; deflectors, hinges, sensor, etc. |
| **Failure modes** | What you’re worried about (fatigue, galling, pulp buildup, …). |

### C — DFM & manufacturing (China-relevant)

| Bucket | What to capture |
|--------|-----------------|
| **DFM concerns** | Tight tolerances, deep pockets, thin walls, weld reach, need for jigs, multi-op parts that could be simplified. |
| **Process assumptions** | Laser + bend + weld OK? Casting? Machining only? What you’re *not* set on. |
| **Stock & standards** | GB tubes, schedule pipe, local fastener preferences—or “match performance, source locally”. |
| **Assembly & service** | What must be removable, single-person install, no special tools if possible. |

### D — Optimizations you want

| Bucket | What to capture |
|--------|-----------------|
| **Cost** | Where you’d trade complexity for cheaper fabrication. |
| **Lead time / MOQ** | Parts you need to simplify for small runs or faster turns. |
| **Performance** | Stiffness, hygiene, cycle time, fruit handling—what you’d improve if cost allowed. |
| **Weight / envelope** | Constraints or “nice to shrink”. |

### E — Unknowns & questions for contractor

| Bucket | What to capture |
|--------|-----------------|
| **Open questions** | Anything you haven’t decided—list as numbered questions. |
| **Alternates welcome** | “Equivalent pulley OK”, “propose bearing arrangement”, etc. |
| **What you need decided** | e.g. dowel vs pilot holes, welded vs bolted bracket. |

### F — Supply chain (working in China)

| Bucket | What to capture |
|--------|-----------------|
| **Must-use parts** | McMaster / import-only items—flag lead time pain. |
| **Substitute OK** | “Performance-equivalent 304 sheet from local mill”. |
| **Long-lead / import** | Motors, reducers, sensors—what you’ll ship vs buy locally. |
| **Vendor assumptions** | Shenzhen / Sean-YES style fab partner; language of drawings (EN + key 中文 in BOM if needed). |

### G — Acceptance & handoff

| Bucket | What to capture |
|--------|-----------------|
| **Deliverables** | Updated STEP, 2D for fab, BOM revision, DFMEA light—whatever you expect. |
| **Acceptance** | Fit-up on machine, alignment check, trial run criteria. |

---

## Suggested page layout (so contractors find this fast)

On each subsystem / subpage HTML, under **Discussion** (or equivalent), use **h3** blocks contractors can scan:

1. **Rough design & intent** — what the CAD represents.  
2. **Known issues & risks** — bullet list; empty = “none listed; contractor to review”.  
3. **DFM & manufacturing (China)** — concerns + process questions.  
4. **Optimizations sought** — cost, lead time, performance.  
5. **Questions for contractor** — numbered.  
6. **Supply chain & alternates** — import vs local, equivalents OK.  
7. **Interfaces & tolerances** — table as today.  
8. **Expected deliverables & acceptance** — short paragraph.

Skeleton pages can grow these sections as you fill them.

---

## Stop order by subsystem

Paths are relative to repo root. **(skeleton)** = placeholder; **(with content)** = has copy/CAD—**still run buckets B–F** for design-assistance gaps.

### 1 — Frame

| # | Page | Path | Notes |
|---|------|------|--------|
| 1.1 | Frame (main) | `Frame/index.html` | Plates, levelling, attachment; weldment DFM. |
| 1.2 | Loads and load paths | `Frame/Loads-and-load-paths/Loads-and-load-paths.html` | Reactions, FEA TBD, contractor validation? |

### 2 — Drivetrain

| # | Page | Path |
|---|------|------|
| 2.1 | Drivetrain (main) | `Drivetrain/index.html` |
| 2.2 | Motor and reducer | `Drivetrain/motor-and-reducer/index.html` |
| 2.3 | Gears and cam bearings | `Drivetrain/gears-and-cam-bearings/index.html` |
| 2.4 | Drivetrain mount plate | `Drivetrain/drivetrain-mount-plate/index.html` |

### 3 — Transmission

| # | Page | Path |
|---|------|------|
| 3.1 | Transmission (main) | `Transmission/index.html` |
| 3.2 | Transmission mount plate | `Transmission/transmission-mount-plate/index.html` |
| 3.3 | Drive shafts | `Transmission/drive-shafts/index.html` |
| 3.4 | Yoke | `Transmission/yoke/index.html` |

### 4 — Extraction & synchronisation

| # | Page | Path |
|---|------|------|
| 4.1 | Extraction (main) | `Extraction-syncronisation/index.html` |
| 4.2 | Fruit support | `Extraction-syncronisation/fruit-support/index.html` |
| 4.3 | Peelers | `Extraction-syncronisation/peelers/index.html` |
| 4.4 | Driven bracket | `Extraction-syncronisation/driven-bracket/index.html` |

### 5 — Collection

| # | Page | Path |
|---|------|------|
| 5.1 | Collection (main) | `Collection/index.html` |
| 5.2 | Juice collection | `Collection/juice-collection/index.html` |
| 5.3 | Plungers and filter | `Collection/plungers-and-filter/index.html` |

### 6 — Fruit intake system (Feeder)

| # | Page | Path |
|---|------|------|
| 6.1 | Feeder (main) | `Feeder/index.html` |
| 6.2 | Feeding subassembly | `Feeder/feeding-subassembly/index.html` |
| 6.3 | Feeder body | `Feeder/feeder-body/index.html` |
| 6.4 | Entry tubes | `Feeder/entry-tubes/index.html` |

### 7 — Core ejection

| # | Page | Path |
|---|------|------|
| 7.1 | Core ejection (main) | `Plug-ejection/index.html` |
| 7.2 | Plunger drive bracket | `Plug-ejection/plunger-drive-bracket/index.html` |
| 7.3 | Plunger drive system (side panels) | `Plug-ejection/plunger-drive-system-in-side-panels/index.html` |

### 8 — Disposal system

| # | Page | Path |
|---|------|------|
| 8.1 | Disposal (main) | `Outflow-disposal/index.html` |
| 8.2 | Chutes and augers | `Outflow-disposal/chutes-and-augers/index.html` |
| 8.3 | Deflectors | `Outflow-disposal/deflectors/index.html` |

### 9 — Enclosure / shell

| # | Page | Path |
|---|------|------|
| 9.1 | Enclosure (main) | `Enclosure-shell/index.html` |
| 9.2 | Protective covers | `Enclosure-shell/protective-covers/index.html` |
| 9.3 | Overcentered hinges | `Enclosure-shell/overcentered-hinges/index.html` |

### 10 — Clean-in-place (CIP)

| # | Page | Path |
|---|------|------|
| 10.1 | CIP (main) | `Clean-in-place/index.html` |
| 10.2 | CIP nozzles and feed pipes | `Clean-in-place/cip-nozzles-and-feed-pipes/index.html` |
| 10.3 | Third-party CIP control | `Clean-in-place/third-party-cip-control-equipment/index.html` |

### 11 — Controls and electronics

| # | Page | Path |
|---|------|------|
| 11.1 | Controls (main) | `Controls-Electronics/index.html` |
| 11.2 | Machine control & UI | `Controls-Electronics/machine-control-definition-and-ui/index.html` |
| 11.3 | Motor power management | `Controls-Electronics/motor-power-management/index.html` |
| 11.4 | Yoke position sensor | `Controls-Electronics/yoke-position-sensor/index.html` |

### Cross-cutting

| # | Page | Path |
|---|------|------|
| X.1 | Third-party / site | `3rd-party/index.html` |
| X.2 | Project overview | `Overview/index.html` |
| X.3 | Questions for RFP | `Overview/Questions-for-RFP.html` — sync with per-page questions. |

---

## Per-stop flow (Marceline runs this in order)

For **this page only**:

1. **A — Baseline** — Function, rough design note, interfaces, figures.  
2. **B — Known issues** — What’s broken or worrying? (OK to say “none yet”.)  
3. **C — DFM / China fab** — Weld, bend, tolerance, process questions.  
4. **D — Optimizations** — Cost, lead time, performance trades you care about.  
5. **E — Questions for contractor** — Numbered list.  
6. **F — Supply chain** — Imports, local substitutes, MOQ/lead time sensitivities.  
7. **G — Deliverables & acceptance** — What “done” means for this scope.

Then: **Next action** — bullets Ricky (or the agent) will put into the HTML.

---

## After a subsystem

- Update main `index.html` badges **with content** when the page has enough **design-assistance** substance (not only pretty CAD).  
- Optional: `memory/YYYY-MM-DD_subsystem-N-rfp-fill.memory.md` — issues, questions, contractor TBDs.
