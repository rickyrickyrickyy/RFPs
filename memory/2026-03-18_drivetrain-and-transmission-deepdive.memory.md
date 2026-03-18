## Drivetrain + Transmission deep-dive (2026-03-18)

### Drivetrain (Subsystem 2) — key decisions/unknowns captured
- **Catalog links** (use web, not repo PDFs):
  - WEG W22 IEC TEFC IE2 listing: https://www.weg.net/catalog/weg/US/en/c/MT_IEC_3PHASE_LV_TEFC_W22_IE2/list
  - Sumitomo Cyclo 6000 catalog PDF: https://us.sumitomodrive.com/sites/default/files/2025-03/cyclo_6000_reducer_catalog_v12_web-2.pdf
- **Motor**: WEG W21/W22 IE3, product **13533507**, 7.5 kW (10 hp), 50 Hz, 4-pole, 1460 rpm rated, ~49 N·m rated torque, 38 mm shaft.
- **Motor/reducer orientation**: current concept mounts **motor shaft vertical downward** and **reducer input shaft vertical downward**, coupled by **SPA V-belts**; tensioning via adjustable motor mount (stud/stacked-nut standoff concept; contractor to propose improved approach).
- **Belt/guard**: pulley/belt guard not designed; may require extra rails/brackets for guarding. Center distance unknown; belt tension radial loads into mount plate must be quantified.
- **Reducer**: Sumitomo Cyclo 6000 series; output speed target ~70 rpm.
- **Bearing unit roles**:
  - **SKF F4BRP 208-SRB-CRH** = locating capped unit under **passive gear** (axial locating).
  - **SKF F4BRP 208-SRB-CLE** = non-locating unit supporting **Cyclo output shaft side** (axial float).
  - SKF CLE link: https://www.skf.com/group/products/mounted-bearings/roller-bearing-units/flanged-units/productid-F4BRP%20208-SRB-CLE
  - SKF CRH link: https://www.skf.com/group/products/mounted-bearings/roller-bearing-units/flanged-units/productid-F4BRP%20208-SRB-CRH
- **Shaft mismatch + extensions**: mounted bearing bore does not match Cyclo shaft as-is; both reducer input and output shafts need extensions/adapters. Preferred: Sumitomo custom shaft if possible; otherwise custom machined hardened shaft (warranty/lead-time trade).
- **Gear concept**: spur gear preferred (70 rpm); preliminary target: **38 teeth**, **~308 mm pitch diameter**, **module ~8**, **20° pressure angle**, face width concept **~56 mm (TBD)**; module 6 vs 8 and helical angle remain open; gear needs face hardening/finishing plan.
- **Cam/yoke interface**: cam rollers are **SKF NUTR 25 A** (track/support roller) on ~25 mm post; intent to **stack two rollers** for increased yoke engagement area. Link: https://www.skf.com/cn/products/rolling-bearings/track-rollers/support-rollers/productid-NUTR%2025%20A
- **Lubrication**: open gear under a cover (not sealed); lubrication method and maintenance interval TBD; contractor to propose.
- **DT mount plate**: concept is a **~20 mm steel slab** (waterjet/laser + machining) mounted to back of machine on side rails, supported by rear cross-beam + forward gussets/plates. Assembly intent: drop plate → shim flat/aligned → bolt → drill/ream into rails → staggered dowel pattern (~3 per side) for repeatability; bolts on cross-members; dowels only in side rails.

### Transmission (Subsystem 3) — structure + key risks captured
- **Site structure update**: merged `Transmission/drive-shafts/` into `Transmission/yoke/` as **“Yoke and drive shafts”**; driveshaft page now points to combined page.
- **Primary risk**: **jam/asymmetric binding** (one linear bearing binds or fruit/hard object jam). Shafts twist; high moments into linear bearings and mount plate; design intent includes a high factor-of-safety “rock in juicer” survivability case.
- **Alignment requirement**: shaft/bearing placement is a key driver for extraction-to-collection peeler alignment; end-of-stroke target gap ~2–3 mm between driven and static peeler faces.
- **Maintenance**: expect seasonal teardown/reassembly (~yearly); alignment strategy must be repeatable (align → tighten → drill/ream for dowels; shim strategy).
- **Environment**: front face of transmission mount plate exposed to washdown/juice; seals/scrapers and corrosion resistance important.
- **Yoke concept**: ~660 mm wide; three primary **25 mm steel blocks** bolted between front/back yoke faces; cam rollers run between track faces (flatness/parallel spacing critical). Compression stroke higher stress than return but must survive any stop/jam. Concept to lower yoke onto cam rollers and fasten a **~5 mm top cap plate** for stiffness/retention.
- **Shafts/bearings**: two **35 mm hardened stainless shafts** (prior art: **440C**); flanged/double-sealed linear bearings (LMFCL35UU family). Shaft mounts: **SSTHSL-35** square flange mounts with 4 set screws.
- **Scraper concept**: add extraction-side shaft scraper and a formed sheet-metal “bowl” cover around linear bearing to shed juice and protect shafts.
- **Pull brackets**: yoke has L/R pull brackets engaging ~16 mm, ~1 m rods via stopper on return stroke; slot/hole acceptable (low precision).
- **Transmission mount plate concepts**: two options:
  - **Sand-cast + post-machined** (robust): 3° draft on ribs, min thickness ~8 mm, drill dimples for machining. Parting surface on back (negative-Z) face. Post-machine top/bottom mounting faces and hygiene-facing inner surfaces; machine bearing mount pads.
  - **Welded steel**: two waterjet plates into L + triangular gussets; stress relief then machine critical faces/pads. Dowel/bolt/shim scheme TBD; contractor to propose.

