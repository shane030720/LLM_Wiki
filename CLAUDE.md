# LLM Wiki — Schema

This file is the authoritative schema for this wiki. Every Claude Code session operating on this repository **must read this file first** and follow all conventions defined here.

---

## Philosophy

This wiki is a **persistent, compounding knowledge base** maintained by LLMs on behalf of a human curator. It is not a RAG index. Knowledge is synthesized and cross-referenced at ingest time, so every query benefits from accumulated understanding rather than raw retrieval.

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."
> — Andrej Karpathy

---

## Ownership Model

| Layer | Contents | Who writes |
|-------|----------|-----------|
| `raw/` | Original source documents — **immutable** | Human only (add, never edit) |
| `wiki/` | Synthesized markdown pages | LLM only (human never edits directly) |
| `CLAUDE.md` | This schema | Human + LLM co-evolve |
| `AGENTS.md` | Operational playbook for LLM agents | Human + LLM co-evolve |

---

## Directory Layout

```
LLM_Wiki/
├── CLAUDE.md                  ← this file (schema)
├── AGENTS.md                  ← agent operational playbook
├── raw/                       ← immutable source documents
│   └── *.pdf / *.md / *.txt
└── wiki/
    ├── index.md               ← master content catalog (auto-maintained)
    ├── log.md                 ← append-only operation log (auto-maintained)
    └── pages/
        ├── concepts/          ← what a thing IS (definitions, mechanics)
        ├── entities/          ← who/what EXISTS (tools, models, frameworks, people)
        └── syntheses/         ← cross-source analysis, comparisons, open questions
```

---

## Page Conventions

### Frontmatter (required on every page)

```markdown
---
title: <Human-readable title>
category: concept | entity | synthesis
tags: [tag1, tag2]
sources: [raw/filename.pdf, raw/other.pdf]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Section structure

**Concept pages** must have:
- `## Definition` — precise one-paragraph definition
- `## How It Works` — mechanism, internals, flow
- `## Key Properties` — bullet list of salient traits
- `## Relationships` — links to related pages with one-line context
- `## Open Questions` — unresolved ambiguities or contradictions
- `## Sources` — list of raw sources this page draws from

**Entity pages** must have:
- `## Overview` — what it is, who makes it, status
- `## Capabilities` — what it can do
- `## Limitations` — what it cannot do or does poorly
- `## Relationships` — links to concepts it implements or entities it competes with
- `## Sources`

**Synthesis pages** must have:
- `## Thesis` — the central claim being synthesized
- `## Evidence` — bullet points with source citations
- `## Counterevidence` — contradicting claims, if any
- `## Conclusion` — current best understanding
- `## Sources`

### Cross-references

Use wiki-link syntax: `[[page-slug]]`

- Slug = filename without `.md`, e.g., `[[vibe-coding]]`
- Always include a one-clause context: `[[vibe-coding]] (the paradigm this builds on)`
- Unresolved links (page not yet written) are valid — they mark knowledge gaps

### Contradiction notation

When two sources disagree, note it inline:

```markdown
> ⚠️ **Contradiction:** [Source A] claims X, while [Source B] claims Y. See [[open-questions-agent-memory]].
```

---

## Navigation Files

### `wiki/index.md`

One row per wiki page. Format:

```markdown
| Page | Category | Tags | Updated | Summary |
|------|----------|------|---------|---------|
| [[vibe-coding]] | concept | coding, LLM | 2026-05-26 | Iterative AI-assisted development where the LLM writes most code |
```

Rules:
- Updated at every Ingest and every Lint pass
- Sorted by category, then alphabetically by title within category
- Never remove rows — mark deprecated pages with ~~strikethrough~~

### `wiki/log.md`

Append-only chronological record. Format:

```markdown
## [YYYY-MM-DD] <operation> | <short description>

- **Source(s):** raw/filename.pdf
- **Pages created:** [[page-slug-1]], [[page-slug-2]]
- **Pages updated:** [[page-slug-3]]
- **Contradictions flagged:** <none | description>
- **Notes:** <any notable observations>
```

Rules:
- Never edit past entries
- One entry per Ingest, one per Lint, one per significant Query (when a new page is created)

---

## Naming Conventions

- Page filenames: `kebab-case.md`, English, descriptive
- Tags: lowercase, singular nouns where possible (`agent`, `tool`, `pattern`)
- Avoid dates in filenames — dates belong in frontmatter

---

## Schema Evolution

When this schema needs to change:
1. Propose the change in the current session with rationale
2. Human approves
3. LLM updates this file and migrates affected pages in one pass
4. Log the schema change in `wiki/log.md` with prefix `## [DATE] schema-update |`
