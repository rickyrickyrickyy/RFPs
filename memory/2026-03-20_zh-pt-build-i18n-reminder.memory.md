## zh/pt mirrors — regenerate after English edits

- **Source of truth:** English HTML at normal paths. **`zh/`** and **`pt/`** are generated; do not hand-edit as primary—re-run the builder after English changes.
- **Commands** (repo root):
  ```bash
  pip install -r tools/requirements-i18n.txt
  python tools/install_argos_models.py   # once per machine
  python tools/build_i18n.py
  ```
- **Script:** `tools/build_i18n.py` — retargets links inside `zh/`/`pt/`, keeps images on English tree, language bar per page. Translates visible text and **`data-caption`**, **`alt`**, **`title`**, **`aria-label`**, Mermaid `[labels]` via **Argos** first, then MyMemory → Google.
- **Quality:** Machine translation; fluent review for technical/legal copy and brand terms (P6, Delijuice, SKF, etc.).
