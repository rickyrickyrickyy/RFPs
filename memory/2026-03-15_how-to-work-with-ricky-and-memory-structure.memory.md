# How to work with Ricky and memory structure

## Goal

Ricky is building the RFP while **training Marceline** to hold everything he knows. Success = any Cursor instance or local agent can assist him consistently by using repo-based memory and these habits.

## Load memory (do this first when RFP-relevant)

When the task involves RFP content, structure, naming, or project decisions:

1. Read **marceline.md** (profile and training goal).
2. Read **README.md** (project snapshot, due dates, layout, "For agents" section).
3. Read all **memory/*.memory.md** in **oldest-first** order by filename (chronological context).

Use the context; no need to announce that you loaded. Rule: `.cursor/rules/load-marceline-context-for-rfp-work.mdc`.

## Save memory (keep Marceline and future agents in sync)

- **When:** After substantial content additions, renames, structural decisions, or when Ricky says "remember this" / "save to Marceline's memory".
- **Offer:** "Want me to save this to Marceline's memory?" if you just made significant changes.
- **How:** Create `memory/YYYY-MM-DD_short-slug.memory.md`. Concise markdown, `##` headings, key facts/decisions only. One topic or session per file.
- **Rules:** `remember-marceline-memory.mdc` (user says remember); `load-marceline-context-for-rfp-work.mdc` (offer after significant updates).

## Memory structure for success

- **One concern per file** when possible (e.g. naming, one session summary, one decision). Easier to scan and merge when loaded.
- **Durable references:** Use descriptive slugs for memories that should stay useful across sessions (e.g. `how-to-work-with-ricky-and-memory-structure`, `rfp-structure-naming`).
- **Chronological order:** Filenames `YYYY-MM-DD_slug` so "oldest first" gives timeline; newer memories can refer to or supersede older ones.
- **Marceline persona:** When Ricky addresses Marceline by name, respond as her (project tracking, deadlines, next steps); same memory, same repo. Rule: `talk-to-marceline.mdc`.

## Repo boundaries

- This repo = **~/RFPs**. Separate from Agents repo. Marceline here has only this profile, README, and memory/ — no backlog or other agents unless Ricky references them.
- Single source of truth: no external prompt or cloud memory. Everything that should persist lives in this repo.
