# RFPs

RFP drafts and project context. **Marceline** tracks this folder — deadlines, subsystems, and next steps.

## How to use with Marceline

- **In Cursor (Agents workspace):** Say **"ask Marceline"** or **"@Marceline"** to get status, priorities, and what’s due. Marceline loads memory from `Agents/personas/marceline/memory/medium_term/`.
- **In Cursor (RFP workspace):** If your workspace is the separate **~/RFPs** repo, Marceline there loads `marceline.md`, `memory/*.memory.md`, and this README for project snapshot and layout. She saves to `memory/`.
- **Save session state:** Say **"remember this for Marceline"** or **"save to Marceline's memory"** so the next session has up-to-date project context.
- **Key file:** [Overview/P6-RFP-context-summary.md](Overview/P6-RFP-context-summary.md) — single reference for P6 and RFP structure.

## For agents: persistent memory (any Cursor instance or local agent)

Ricky is training Marceline so she knows everything he knows. Memory is **repo-based** so it works no matter which Cursor instance or local agent is used:

- **Load when doing RFP work:** Read `marceline.md`, this README, and all `memory/*.memory.md` (oldest first) when the task involves RFP content, structure, naming, or project decisions. A Cursor rule (`.cursor/rules/load-marceline-context-for-rfp-work.mdc`) instructs this.
- **Save after significant updates:** After adding substantial content or making project decisions, offer to create a memory file. If the user agrees (or says "remember this"), create `memory/YYYY-MM-DD_short-slug.memory.md` with a concise summary. That keeps Marceline and future agents in sync.
- **No external store:** The repo is the single source of truth; no separate main prompt or cloud memory is required.

**Commands (for agents / workflows):**
- **Load memory:** Read `marceline.md`, then `README.md`, then all `memory/*.memory.md` (oldest first by filename).
- **Save memory:** Create `memory/YYYY-MM-DD_short-slug.memory.md` with a concise markdown summary (e.g. after significant RFP updates or when the user says "remember this").

## Project snapshot

Short snapshot so Marceline and Cursor have current context. Update when priorities or due dates change.

**Last updated:** 2026-03-20

### Active project

- **P6 RFP** — Industrial prototype (Delijuice 870/970) subsystem RFPs.

### Key references

- **Full P6 context:** [Overview/P6-RFP-context-summary.md](Overview/P6-RFP-context-summary.md)
- **Fill sessions (subpage by subpage):** [RFP-subsystem-fill-walkthrough.md](RFP-subsystem-fill-walkthrough.md) — design-assistance RFPs (rough CAD + issues, DFM, optimizations, questions, China sourcing); use with Marceline; skill `rfp-subsystem-fill-walkthrough`.
- **Subsystems (1–11):** Frame, Drivetrain, Transmission, Collection, Extraction & sync, **Fruit intake system** (6), **Core ejection** (7), **Disposal system** (8), Enclosure, CIP, Controls and electronics. Photos + Q&A per subsystem; naming is canonical in index and Overview (see memory for details).
- **Key pages:** [Delijuice cycle](Overview/Delijuice-cycle.html), [How subassemblies fit](Frame/#how-subassemblies-fit-together), [Loads and load paths](Frame/Loads-and-load-paths/Loads-and-load-paths.html).

### Due dates

| Item | Due |
|------|-----|
| RFP work | Friday night |
| P6 drawings / YES fabrication | 15 May |
| JX operations (LTA) | October (pressure) |

### Where Marceline lives

- **Talk to Marceline:** “ask Marceline” or “@Marceline”.

### Hosting

**Now: GitHub Pages** — Use this until the site is ready, then move to Cloudflare.

- **GitHub Pages:** Repo → **Settings → Pages**. Source: **Deploy from a branch**. Branch: `main` (or your default), folder: **/ (root)**. Save; the site will be at `https://<owner>.github.io/<repo>/`.
- **Entry point:** **index.html** at the repo root. No build step.
- **Later (Cloudflare):** When ready, connect the same repo to Cloudflare Pages (or Workers) and point your domain there.

### Site languages (paused)

- **English only** for now: `zh/` and `pt/` mirrors were removed from `main` until a proper translation workflow exists.
- Shared **mobile / layout** styles may still live in **`assets/site.css`**; any future i18n should regenerate mirrors from English sources of truth.

## Layout

| Folder / file | Purpose |
|---------------|---------|
| **README.md** | This file: project snapshot (active work, due dates, references), repo layout, how to use Marceline. |
| **marceline.md** | Marceline’s profile and behaviour in this repo. |
| **memory/** | Marceline’s session summaries and project state (`*.memory.md`). |
| **Overview/** | P6 context summary, subsystem lists, session summaries. |
| **index.html** | RFP-only entry: overview, nav (with content / to be completed). Marceline and hosting info stay in this README. |
| **assets/site.css** | Shared layout (e.g. mobile-friendly rules). |
| **tools/build_i18n.py** | Optional / future: regenerate language mirrors when i18n is re-enabled. |
| **Frame/** | Frame subsystem RFP draft. |
| **Enclosure-shell/** | Enclosure / shell (related to Frame). |
| **Feeder/**, **Plug-ejection/**, **Drivetrain/**, etc. | Subsystem RFP sections (each with index.html + README.md). |
