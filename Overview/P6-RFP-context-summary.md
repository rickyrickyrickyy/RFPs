# P6 — Full context summary for Cursor & RFP work

**Purpose:** Single reference for everything Bob (and you) have on P6 so you can build off it in Cursor. Discord is paused; RFPs are due soon.

**Last consolidated:** 2026-03-14 (from Bob’s memory + backlog + RFPs folder).

---

## 1. What P6 is and why it matters

- **P6** = current industrial prototype (Delijuice 870/970). Newest version; prototyping in China. Design work with Jamieson. Extractors, deflectors, screw conveyors.
- **Jiangxi (JX):** Factory with **LTA (Long Tai An)**. JX Phase 1 production plan lives in P6 context. Miniplant: 8,160 L/h, 6 extractors, turbo-filter, pasteurizer. **LTA pressure for operations by October.**
- **Drawings target:** April 1st for Sean/YES fabrication (China, Shenzhen area).
- **Machine lineage:** P3 → P4 → P5 (Brazil 2002, Sumitomo cyclo refs) → **P6** (current). 323 = commercial/countertop (separate).

---

## 2. Subsystems (full list — use for RFP sections)

Use these as RFP sections. For each: add photos, Q&A, and flush out part/parameter details.

### 2.1 Intake feeder system

*(Dave covered intake in a separate conversation; this is the consolidated list.)*

- Feeder body  
- 90° entry tube (CIP nozzle installed)  
- External duct (oranges from hopper into machine)  
- Fruit synchronisation system (drops oranges one at a time into extraction)  
- Peelers  
- Juice collection system  
- Fruit support (staging to drop oranges one at a time)  

**RFP approach:** One subsystem at a time; file photos; ask as many questions as possible per part/parameter.

---

### 2.2 Plunger drive / juice collection system

- Juice outflow collection  
- Filter  
- Plunger  
- Plunger drive bracket  

---

### 2.3 Drivetrain

- Bearings  
- Plunger drive rods  
- Yoke  
- Plunger pull bracket  
- Sumitomo reducer  
- Reducer mount  
- Two gears  
- Drive belt motor transmission  
- Protection pulley guard  

---

### 2.4 Outflow / bin subsystem

- Peel bin and core chutes  
- Peel and core disposal augers  
- Peel deflectors  

---

### 2.5 Frame

- **Main frame** — primary structure (from your RFP draft: 80×80×5 GB/T square tubes; #8 C-brackets; fully welded).  
- **Driven bracket** — drivetrain / drive shaft mounting  
- **Drivetrain mount plate** — between drivetrain and linear bearing  
- **Linear bearing mount plate** — two drive shafts through; drivetrain pushes through  
- **Loaded mount plate** — static peelers mounted here  

Design focus: stability, alignment, force transmission, smooth linear bearing operation, secure peeler mounting.  
**Existing RFP content:** `RFPs/Frame/Frame.md` (feet, levelling, side rails, dowels, assembly steps, H7 drill/ream).

---

### 2.6 Clean-in-place (CIP)

- Nozzles at each peeler (from below)  
- Nozzle down from each 90° tube at sync system  
- Pipes feeding CIP nozzles  
- Third-party equipment controlling CIP  

---

### 2.7 Controls and electronics

**User panel:** E-stop, on/off, start/stop, indicator lights (machine open, sensor status).  
**Motor:** AC contactor, motor starter, wiring; **WEG W22** motor (spec sheet to come).  
**Safety:** 3 lid safety switches — machine off when any lid open.  
**Position/cycle:** Encoder or other yoke position detection for cycle and controlled stop — **TBD / needs further development** (backlog item).

---

## 3. General design and manufacturing (RFP scope)

- **Material** for every component  
- **Manufacturing method** per part  
- **Fasteners** — full selection and assembly process  
- **Tolerancing** — between components; agree with manufacturers how to achieve  
- **Post-processing** — to achieve tolerances  
- **CAD:** Currently Inventor → **switching to SolidWorks**  

---

## 4. Third-party and site integration (Jiangxi)

- Compatible with **existing third-party equipment**  
- **Jiangxi:** Kaiyi or similar orange juicing line provider (line build + training)  
- **Equipment context:** JBT Marel–style citrus processing; feed lines in China → assume interface with Chinese equipment  
- **Interfaces:** Oranges in from their lines; peels out via their augers; juice to tanks/pumps  

---

## 5. Where things live

- **This summary:** `RFPs/Overview/P6-RFP-context-summary.md`  
- **Subsystems list (Discord):** `RFPs/Overview/2026-03-13_p6-subsystems-components-discord-context.memory.md`  
- **Frame RFP draft:** `RFPs/Frame/Frame.md`  
- **Bob’s memories (in Agents repo):**  
  - Long-term: `personas/bob-the-builder/memory/long_term/2026-03-13_p6-industrial-machine-overview.memory.md`  
  - Medium-term: `personas/bob-the-builder/memory/medium_term/2026-03-13_p6-subsystems-components-discord-context.memory.md` + session summaries  
- **Context (when present):** P6 design and JX plan under `context/delijuice/p6/` (e.g. in DelijuiceRep or your main workspace). In **Agents** repo there is no `context/`; your workspace also has **RFPs**, **DelijuiceRep**, **DemoAgents**.  
- **Library/manifest:** P6-related PDFs/Excel in `agent_files_library_manifest.txt` (e.g. P6 pilot plant SZ, P6 Controls Basic Design, P6 & 323 follow-up, P6 Design Log, P6 Competitive Analysis).

---

## 6. Backlog (Bob) — still open

- **RFP work (due Friday night)** — prioritise helping you get RFP work done.  
- **P6 RFP** — Flush out each subsystem with photos + Q&A: intake feeder, plunger/juice collection, drivetrain, outflow/bin, frame, CIP, controls/electronics; file to memory.  
- **Yoke position** — Specify encoder or other yoke position detection for cycle and controlled stop (further development).  
- **DFM + Design of Machinery** — Study textbooks from OneDrive into long-term memory; file to library/textbooks.  
- **P6 inbox material** — Recursively read P6 folder from OneDrive inbox; sort into library/P6; summarize in medium- and long-term memory.  

Dave’s backlog: *Add P6 machine description to knowledge base.*

---

## 7. Next steps for you in Cursor

1. Use this doc + `Frame/Frame.md` as the baseline for RFP structure.  
2. Add one subsection per subsystem (2.1–2.7); for each, add photos + Q&A as you flush out requirements.  
3. When yoke/encoder is decided, document in controls (2.7) and close the backlog item.  
4. If you have `context/delijuice/p6/` elsewhere, open those files when you need detail for a specific subsystem.

You’re set to work entirely from Cursor and this summary.
