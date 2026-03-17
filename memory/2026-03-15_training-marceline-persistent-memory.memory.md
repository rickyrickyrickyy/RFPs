# Training Marceline and persistent memory

## Decision

Ricky is building the RFP while **simultaneously training Marceline** to know everything he knows. So that this works in **any Cursor instance** and when offloading to a **local agent**, we use **repo-based persistent memory**—no separate main prompt or external store.

## How it works

- **Source of truth:** This repo. Marceline’s profile (`marceline.md`), project snapshot (README), and memories (`memory/*.memory.md`) are the only state.
- **Loading:** When doing RFP work (content, structure, naming, project decisions), any agent loads `marceline.md`, README, and all `memory/*.memory.md` (oldest first). Cursor rule: `.cursor/rules/load-marceline-context-for-rfp-work.mdc`.
- **Saving:** After significant content or decisions, the agent offers to save a memory. If Ricky says yes (or “remember this”), create `memory/YYYY-MM-DD_short-slug.memory.md` with a concise summary. Any agent can create memories so Marceline stays current across instances.
- **Talk to Marceline:** When Ricky explicitly addresses Marceline, she still loads profile + README + memories and responds in persona; the same memory is used for “Marceline mode” and for general RFP work.

## Cursor rules in use

- `talk-to-marceline.mdc` — When user addresses Marceline by name: load context, respond as Marceline, offer to save.
- `remember-marceline-memory.mdc` — When user says “remember this”: create a new memory file.
- `load-marceline-context-for-rfp-work.mdc` — When RFP-relevant work happens: load context so behavior is consistent; offer to save memory after significant updates.

Result: persistent memory no matter which Cursor instance or local agent is used; the repo is the single source of truth.
