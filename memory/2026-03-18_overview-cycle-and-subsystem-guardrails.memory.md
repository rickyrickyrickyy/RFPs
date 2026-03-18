## Overview merge + updated subsystem guardrails (P6)

Merged the “daily” Delijuice extraction-cycle content into `Overview/index.html` and added an end-to-end factory product flow section + process-flow diagram (citrus intake -> P6-870 extraction -> juice tanks -> paddle finisher/holding -> tube-in-tube pasteuriser -> cooling -> filling -> refrigeration). The project intro now frames P6 as the newest generation citrus juicer (handles lemons/other citrus varieties) with target Jiangxi pilot setup in **October 2026** and line sizing around **6 extractors in series** (~**8160 L/hr** total; ~1360 L/hr per extractor).

Added/updated top-down assembly guidance in `Frame/index.html` (adjust feet, shim + locate mount plates with dowels/H7 concept, then install yoke/extraction system, plunger drive, and hinges/covers using the existing figure sequence).

Applied new contractor guardrails to key subsystems:
- **Feeder / feeding subassembly:** 90° entry tube **target inner diameter ~90 mm**; vertical CIP nozzle cut-out is included in latest CAD (photos/figures should be refreshed); added a **left/right tube placement** guardrail so oranges land on the correct fruit-support rails/landing zones.
- **Fruit support:** manufacturing method left open (forming is a candidate), but must satisfy rail geometry/slope and **cleanability** (no pockets; smooth drainage).
- **Transmission yoke:** top cap plate should span the **entire left-to-right top face**; added a **mass/balance sensitivity** note so driven/extraction mass is balanced with yoke mass to avoid persistent shaft stress.
- **Juice collectors:** specified **304 stainless** with **food-zone Ra ~0.8 µm** target; outlet interfaces should use a **standard** sanitary quick-connector mating to the downstream **ribbed rubber connection**.
- **Plungers + filter tube:** hardened steel filter tube; **replaceable hardened plug-cutter tip** attached to a **non-replaceable** hardened tube; scraper expected to be **3–4 blades** with a scraper alloy that limits tube wear; added dimensional guardrails: **plug cutter edge ~9 mm** out from central pin reference face, and **plunger tip ~15 mm** out from the plug cutter. **O-ring inside the filter tube is a risk** due to scraper wear during repeated in/out.
- **Core ejection / c-clip tuning:** C-clip position is the primary tuning lever for **how far plungers retract** during compression; contractor to define practical tuning method/range.
- **Gears:** gear design/material/heat-treat/lubrication are explicitly **not set**; contractor must propose the complete gear set design based on loading and China manufacturability (with sanitary/food-splash guardrail if wetted during washdown).
- **Motor/reducer:** added optional **torque limiter / overload protection** consideration to protect downstream components during stalls/jam events; contractor to propose a practical **lubrication + maintenance** plan.
- **CIP control integration:** added explicit **tank isolation during CIP** requirement and valve switching logic so CIP fluid is routed into the collectors/filter/plunger circuit and does **not** contaminate production juice tanks.

Remaining “undefined” items are intentionally left for contractors/ODM where noted (e.g., exact connector standard choice, final tolerances, and any sensor selection still TBD on other pages).

