## Git: `main` now includes zh/pt; English-only preserved

- **`main`** was **fast-forwarded** to match **`feature/translations-in-progress`** (commit `789d4d4` lineage): English pages at repo root + **`zh/`** + **`pt/`** + `tools/build_i18n.py`, Argos installer, requirements, README i18n section.
- **Backup branch:** **`main-english-only`** — points at the **pre-merge** `main` tip (English-only site, no `zh/`/`pt/` trees). Use it to diff, cherry-pick, or restore if needed.
- **`feature/translations-in-progress`** remains a valid branch name for future translation-only work; it should match `main` until someone diverges it again.

### What this is called

- Saving old `main`: an **archive / snapshot branch** (here: `main-english-only`).
- Making translated work canonical: **merging** (here: **fast-forward**) the feature branch **into `main`**, then **pushing** `main`. On GitHub the **default branch** is still `main`; you did not need to rename branches—only update what `main` contains.
