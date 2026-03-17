# RFP website audit (2026-03-17)

## What was done

- **Audit:** Ran the audit-rfp-website skill: loaded Marceline context, went through all 21 HTML pages for writing coherence, layout, and content.
- **Fixes applied during audit:** Overview/index.html — corrected "extration" → "extraction", "description.." → "description.", fixed broken table row 11 (Controls and electronics) with typos "saftety" → "safety", "managment" → "management", and missing `</td></tr>`.
- **Subsystem titles standardised:** Page titles and h1s now use canonical subsystem numbers 1–11 across the site:
  - 1. Frame, 2. Drivetrain, 3. Transmission, 4. Extraction & synchronisation, 5. Collection, 6. Fruit intake system, 7. Core ejection, 8. Disposal system, 9. Enclosure / shell, 10. Clean-in-place (CIP), 11. Controls and electronics.
  - Third-party page: removed "4." from title/h1 (it is under General & integration, not a subsystem).
  - Fruit support subassembly page: back-link text updated to "4. Extraction & synchronisation".

## Audit outcome

- Nav and links match current structure (including Frame/Loads-and-load-paths/Loads-and-load-paths.html).
- Canonical naming (Fruit intake system, Core ejection, Disposal system; core vs plug; plug cutter) is consistent.
- Back links and sectioning are in place on pages checked.
- README key-pages link already pointed to the correct Loads and load paths path.

## For future audits

- Use the same page order: index → Overview pages → subsystems 1–11 → 3rd-party.
- Subsystem numbers in titles should stay 1–11 as above.
