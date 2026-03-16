# 2.5 Frame

**RFP section:** Primary structure. Design focus: stability, alignment, force transmission, smooth linear bearing operation, secure peeler mounting.

## Overview

The frame is the **primary structure** of the P6 machine. All other subsystems mount to it (drivetrain, plunger/juice collection, intake/peelers, outflow, CIP). It must provide a stable, repeatable base for:

- **Drivetrain** — forces carried without deflection affecting timing or bearing life.
- **Linear bearing mounts** — aligned so two drive shafts run true and the yoke travels smoothly.
- **Peelers** (loaded mount plate) — fixed position for extraction and CIP.

Repeatable alignment uses dowels and H7 drill/ream holes in the side rails. **Key interfaces:** Main frame → **drivetrain mount plate** (#9075CD: gears, housed tapered roller bearings, reducer spacer, Sumitomo reducer); main frame → **transmission mount plate** (#B341C3: transmission subsystem — yoke, two 35 mm shafts, two LMK35UU linear bearings; formerly bearing mount plate); main frame → **loaded mount plate** (#34E682: collection assembly, static side of extraction). All three plates mounted from top onto frame, then onto the two side rails. Leveling: **6111K669 M24 100 mm Swivel Leveling Mount** (McMaster), on M24 tapped endplates at bottom of legs. Enclosure/shell: see [Enclosure-shell](../Enclosure-shell/).

### Design principles

| Principle | Description |
|-----------|-------------|
| **Stability** | Resist deflection under operating loads; stiffness of weldment and plate interfaces is critical. |
| **Alignment** | Three main interfaces located/oriented so shafts, bearings, peelers align; dowels and H7 for repeatability. |
| **Force transmission** | Reaction forces carried through frame to floor without local distortion; clear load paths. |
| **Repeatability** | Plates removable/remountable without loss of alignment; H7 holes and dowels as datum. |
| **Serviceability** | Subassemblies removable for maintenance; no “fit once” reliance. |
| **Manufacturability** | Materials and assembly sequence achievable by fabrication partner (e.g. Sean/YES). |

### Overview figures

Seven CAD views in **[images/](images/)** (see [images/README.md](images/README.md) for colour key and filenames): `overview-full-frame.png`, `overview-three-interfaces.png`, `overview-isometric-alt.png`, `overview-perspective.png`, `overview-front-six-feet.png`, `overview-right-side.png`, `overview-side-three-plates.png`. Referenced in [Frame.md](Frame.md) and [index.html](index.html).

## Components

- **Main frame** (#26C16A) — 80×80×5 GB/T square tubes, #8 C-brackets, fully welded; six legs with M24 tapped endplates
- **Leveling mounts** (#FFD691) — 6111K669 M24 100 mm Swivel Leveling Mount (McMaster)
- **Loaded mount plate** (#34E682) — collection assembly; collection module and static side of extraction (juicer mashes oranges into)
- **Transmission mount plate** (#B341C3) — transmission subsystem: yoke, two 35 mm shafts, two LMK35UU linear bearings (formerly bearing mount plate)
- **Drivetrain mount plate** (#9075CD) — two gears, housed tapered roller bearings, reducer spacer, Sumitomo reducer
- **Driven bracket** — drivetrain / drive shaft mounting (as needed)

## Full draft

See **[Frame.md](Frame.md)** for feet, levelling, side rails, dowels, assembly steps, and H7 drill/ream.
