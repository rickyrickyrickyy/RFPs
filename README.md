# RFPs

RFP drafts and project context. **Marceline** tracks this folder — deadlines, subsystems, and next steps.

## How to use with Marceline

- **In Cursor (Agents workspace):** Say **"ask Marceline"** or **"@Marceline"** to get status, priorities, and what’s due. Marceline loads memory from `Agents/personas/marceline/memory/medium_term/`.
- **In Cursor (RFP workspace):** If your workspace is the separate **~/RFPs** repo, Marceline there loads `marceline.md`, `memory/*.memory.md`, and this README for project snapshot and layout. She saves to `memory/`.
- **Save session state:** Say **"remember this for Marceline"** or **"save to Marceline's memory"** so the next session has up-to-date project context.
- **Key file:** [Overview/P6-RFP-context-summary.md](Overview/P6-RFP-context-summary.md) — single reference for P6 and RFP structure.

## Project snapshot

Short snapshot so Marceline and Cursor have current context. Update when priorities or due dates change.

**Last updated:** 2026-03-14

### Active project

- **P6 RFP** — Industrial prototype (Delijuice 870/970) subsystem RFPs.

### Key references

- **Full P6 context:** [Overview/P6-RFP-context-summary.md](Overview/P6-RFP-context-summary.md)
- **Subsystems to flush out:** Intake feeder, plunger/juice collection, drivetrain, outflow/bin, frame, CIP, controls/electronics (photos + Q&A per subsystem).
- **Done:** Frame — draft in [Frame/Frame.md](Frame/Frame.md).

### Due dates

| Item | Due |
|------|-----|
| RFP work | Friday night |
| P6 drawings (Sean/YES) | April 1st |
| JX operations (LTA) | October (pressure) |

### Where Marceline lives

- **Talk to Marceline:** “ask Marceline” or “@Marceline”.

### Hosting

**Now: GitHub Pages** — Use this until the site is ready, then move to Cloudflare.

- **GitHub Pages:** Repo → **Settings → Pages**. Source: **Deploy from a branch**. Branch: `main` (or your default), folder: **/ (root)**. Save; the site will be at `https://<owner>.github.io/<repo>/`.
- **Entry point:** **index.html** at the repo root. No build step.
- **Later (Cloudflare):** When ready, connect the same repo to Cloudflare Pages (or Workers) and point your domain there.

## Layout

| Folder / file | Purpose |
|---------------|---------|
| **README.md** | This file: project snapshot (active work, due dates, references), repo layout, how to use Marceline. |
| **marceline.md** | Marceline’s profile and behaviour in this repo. |
| **memory/** | Marceline’s session summaries and project state (`*.memory.md`). |
| **Overview/** | P6 context summary, subsystem lists, session summaries. |
| **index.html** | RFP-only entry: overview, nav (with content / to be completed). Marceline and hosting info stay in this README. |
| **Frame/** | Frame subsystem RFP draft. |
| **Enclosure-shell/** | Enclosure / shell (related to Frame). |
| **Feeder/**, **Plug-ejection/**, **Drivetrain/**, etc. | Subsystem RFP sections (each with index.html + README.md). |
