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

**Components (CAD):** Driven gear #FFE696, passive gear #237A3A, two cam bearings #4AB6F6 (interface with [transmission](../Transmission/) yoke), passive gear shaft #3683E6, locating roller bearing SKF_F4BRP 208-SRB-CRH_ECY 213 #7D26B5, non-locating roller bearing SKF_F4BRP 208-SRB-CLE, reducer spacer #366D20, **Sumitomo Cyclo 6000 reducer** #5EB45D, **V-belt** #572D9A (DIN 2215 17×957, 2-belt, 1000 mm long), **WEG 22 1450 rpm motor** #6A37BB, stainless steel motor mount plate spacer #D2B545, wooden motor mount plate #207E96.

**Reminders:** Add Sumitomo Cyclo 6000 reducer specs; add more WEG 22 motor specs. More drivetrain details to be added later.

**RFP content:** `RFPs/Drivetrain/` (Drivetrain.md, 12 CAD views — 10 drivetrain, 2 cam/yoke interface, colour key).

### Transmission subsystem (yoke, shafts, bearings)

**Function:** Transmits force from the **gears** (drivetrain) to the **extraction/synchronisation system**, which presses fruit against the **collection system** on the **collection system mount plate** (formerly static/loaded mount plate).

**Components:** Yoke (#2F9EBA), two 35 mm drive shafts with shaft mounts at both ends (#798C2E), two LMK35UU linear bearings (#3582E4), transmission mount plate (#B341C3) on frame.

**RFP content:** `RFPs/Transmission/` (overview, CAD views, colour key, interfaces).

---

### Collection subsystem (static peelers, juice, filter, plug)

**Components:** Collection mount plate (#27C16A), static peelers (#F36F3B), static deflectors (#CCDF3F — keep peels sliding towards static plate; two angled surfaces for stiffness and potential forming vs welding), juice collectors / Y-tubes (#FFFF50), filter tube (#287F3F), plug cutter (#4DB7F5). Mounts on frame’s loaded mount plate (collection system mount plate).

**Function:** Driven + static peelers mesh; oranges fall between; fingers interlace → peel to extraction chamber/outflow chute; plug cutter cuts centre plug; juice → filter tube slots → yellow collector → Y-branch → ribbed connection (standard rubber pipes). **Reminder:** Send 34 mm standard connector for quick connection.

**RFP content:** `RFPs/Collection/` (overview, 11 CAD views, colour key).

---

### 2.4 Outflow / disposal subsystem

**Disposal system:** **Peel chute** (red #D43C3C, folded sheet metal), **core chutes** (welded to peel chute), **two augers** (#28B399) that take peels and plugs/cores away separately. Alternative CAD colours: peel chute #2768BC, core chutes #D79132, augers #FFED9E.

**Cycle (after pressing stroke):** [Plug ejection](../Plug-ejection/) pushes plunger through filter → plug out of plug cutter → plug **falls into core chute**. Peels fall to **sides of peelers**, **avoid core chutes**, **two channels** for separate processing; augers take peels and plugs/cores away separately.

**Also:** Peel deflectors. **RFP content:** `RFPs/Outflow-disposal/` (Disposal.md, 9 CAD views, colour key).

---

### 2.2 Plug ejection (plunger / juice collection)

**Plug ejection (after pressing stroke):** System pushes **plunger** through **filter**, pushes **plug** back out of **plug cutter** → plug **falls into** [disposal](../Outflow-disposal/) **core chute**. Components: plunger, filter, plug cutter interface, plunger drive bracket, juice outflow collection. See [Collection](../Collection/) (juice to Y-section, plug cutter) and [Outflow-disposal](../Outflow-disposal/) (core chute, peel chute, augers).

**RFP content:** `RFPs/Plug-ejection/` (PlugEjection.md, README, index, **7 CAD views** in images/ — actuator bar, plungers, green housings, rods, spring).

---

### 2.5 Frame

- **Main frame** — primary structure (80×80×5 GB/T square tubes; #8 C-brackets; fully welded). Six legs with M24 tapped endplates; **6111K669 M24 100 mm Swivel Leveling Mount** (McMaster) at each leg.  
- **Loaded mount plate** — collection assembly; collection module and static side of extraction (juicer mashes oranges into).  
- **Transmission mount plate** (formerly bearing mount plate) — part of **transmission subsystem**: yoke, two 35 mm shafts, two LMK35UU linear bearings and this plate.  
- **Drivetrain mount plate** — two gears, housed tapered roller bearings (gears on top), reducer spacer, Sumitomo reducer.  
- **Driven bracket** — drivetrain / drive shaft mounting (as needed).  

All three plates mounted from top onto frame, then onto the two side rails. Design focus: stability, alignment, force transmission, smooth transmission/yoke operation, secure peeler mounting.  
**RFP content:** `RFPs/Frame/Frame.md` and `RFPs/Frame/images/` (CAD views, colour key, feet, levelling, side rails, dowels, assembly steps, H7 drill/ream).

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
