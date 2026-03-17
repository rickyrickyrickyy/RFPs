# Marceline — memory (RFP repo)

Marceline’s session summaries and project state live here. This folder is the **persistent memory** for the RFP repo so any Cursor instance or local agent can load the same context.

- **Loading:** When you talk to Marceline, or when any agent does RFP-relevant work, load all `*.memory.md` files **oldest first** together with `../marceline.md` and `../README.md`. Rule: `.cursor/rules/load-marceline-context-for-rfp-work.mdc`.
- **Filename pattern:** `YYYY-MM-DD_short-slug.memory.md`
- **Saving:** Say "remember this" or "save to Marceline's memory"; or after significant updates the agent can offer to create a new `.memory.md` file. Keeps Marceline trained across sessions and agents.
- **Structure for success:** Some memories are **durable references** (e.g. how to work with Ricky, memory structure, RFP naming/structure); others are **session or topic snapshots** (e.g. a specific decision or day’s context). Loading oldest-first gives chronological order; scan headings for "how to work", "naming", "structure" when you need consistency.
- **Profile:** `../marceline.md` (Marceline in this repo is standalone; the Agents repo has a full Marceline persona with soul, backlog, and workflows).
