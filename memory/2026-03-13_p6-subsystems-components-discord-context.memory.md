## P6 industrial machine — subsystems and components (from Discord session 2026-03-13)

Context from Ricky’s run-through of P6 subsystems. Use this for RFP drafting and design discussions. Dave covered the **intake feeder system** in a separate conversation; that summary is below under Intake feeder.

---

### Intake feeder system

*(Dave covered this in a prior conversation; capture here so Bob has full context.)*

- **Feeder body**
- **90° entry tube** — has CIP nozzle installed
- **External duct** — oranges from hopper into machine
- **Fruit synchronisation system** — drops oranges one at a time into juice extraction
- **Peelers**
- **Juice collection system**
- **Fruit support** — staging area to drop oranges into extraction one at a time

**RFP approach:** Go through subsystems/subassemblies one at a time; file relevant photos; ask as many questions as possible about each part and parameter to flush out the RFP.

---

### Plunger drive / juice collection system

- Juice outflow collection
- Filter
- Plunger
- Plunger drive bracket

---

### Drivetrain subsystem

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

### Outflow / bin subsystem

- Peel bin and core chutes
- Peel and core disposal augers
- Peel deflectors

---

### Frame

- **Main frame** — primary structural component
- **Driven bracket** — mounting for drivetrain / drive shafts
- **Drivetrain mount plate** — between drivetrain and linear bearing
- **Linear bearing mount plate** — two drive shafts pass through; drivetrain pushes through
- **Loaded mount plate** — static peelers mounted here

Design focus: stability, alignment, force transmission, smooth linear bearing operation, secure peeler mounting.

---

### Clean-in-place (CIP) system

- Nozzles pointed at each peeler from the bottom
- Nozzle pointing down from each 90° tube at the synchronisation system
- Pipes feeding CIP nozzles with cleaning fluid
- Third-party equipment controlling the CIP system

---

### Controls and electronics subsystem

**User control panel**

- Emergency stop
- Machine on/off switch
- Machine operation start/stop button
- Indicator lights: machine open, sensor status

**Motor control and power**

- AC contactor
- Motor starter
- Wires and management as needed
- **Motor:** WEG W22 — spec sheet to be provided later

**Safety**

- Safety switches on 3 lids — machine shuts off when any lid is open

**Position / cycle**

- Encoder or other way to detect yoke position for cycle position and controlled stop — **needs further development**

---

### General design and manufacturing

- **Material selection** for every component
- **Manufacturability** — choose manufacturing method per part
- **Fasteners** — select all; define assembly process
- **Tolerancing** — between components; agree with manufacturers how tolerances will be achieved
- **Post-processing** — selected to achieve tolerances
- **CAD:** Currently Inventor; **switching to SolidWorks**

---

### Third-party and site integration (Jiangxi)

- Compatible with **existing third-party equipment**
- **Jiangxi:** Kaiyi or another orange juicing line provider for line build and personnel training
- **Equipment context:** JBT Marel Corporation citrus processing (extractors, etc.); feed lines in China → assume interface with Chinese equipment
- **Interfaces:** Oranges feed in from their lines; peels removed using their augers; juice outflow collected to tanks and pumps

---

### Learning material (re-send via inbox)

- User will re-send textbooks (e.g. DFM handbook, Design of Machinery), P6 material, and other references through Bob's inbox and into the library so Bob can (re)learn from them. No prior study is assumed.

---

### Backlog / next steps

- Flush out each subsystem in turn with photos and Q&A for RFP.
- Yoke position/encoder specification and implementation.
