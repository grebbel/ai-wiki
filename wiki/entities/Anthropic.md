---
type: entity
kind: organization
aliases: ["Anthropic", "Anthropic PBC"]
tags: [anthropic, ai-lab, foundation-models, claude]
since: 2021
confidence: 0.85
last_confirmed: "2026-05-09"
source_count: 5
---

# Anthropic

AI safety and research company; publisher of the [[Claude]] family of models and the [[Anthropic Economic Index]] research series. Founded 2021. Public Benefit Corporation. Partnered with [[Amazon Web Services]] (~$8B total invested as of 2024 per [[2026-04-28-werner-lebrun-octopus-organization]]).

## Research initiatives appearing in this wiki

- [[Anthropic Economic Index]] — recurring measurement of real-world Claude usage on Claude.ai (consumer) and 1P API (enterprise). Five reports through March 2026.
- Rwanda partnership with **ALX** — AI literacy + Claude Pro access program for African graduates ([[2026-04-28-anthropic-economic-index-q4-2025|fourth Economic Index report]]).
- [[Jack Clark]] — co-founder; serves on the [[AI Index]] steering committee.

## Platform / product engineering

- **Claude Platform** — Anthropic's developer-facing platform.
  - **Claude Managed Agents** — hosted service for long-horizon agent work; brain/hands/session decoupled architecture; published April 2026 ([[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Engineering blog]]).
  - **Claude Code** — agentic coding harness; described as "an excellent harness" in the Managed Agents post; its agentic architecture (splits coding work into smaller API calls labeled as distinct tasks) is the empirical signature of agent-mediated work in the [[2026-05-07-anthropic-economic-index-5-learning-curves|5th Economic Index report]]. Engineering leadership: [[Boris Cherny]] (10–15 concurrent Claude instances + CLAUDE.md as in-workflow learning capture per [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]) and *Fiona Fung* (Director of Engineering; documents the Claude Code team-norms rewrite — JIT planning, code-wins-over-whiteboard debate, manager-starts-as-IC dogfooding, "Claudify everything", "explicit permission to kill processes" — in [[2026-05-08-running-an-ai-native-engineering-org]]).
- **Cowork** — Anthropic product co-led by Fung alongside Claude Code; deferred for separate page on second-source mention.

## Models referenced in this wiki

- [[Claude Sonnet 4.5]] — predominant model in the November 2025 Economic Index sample. Referenced as exhibiting "context anxiety" (premature task wrap-up) in the Managed Agents engineering post.
- **Claude Opus 4.5** — released between the 4th and 5th Economic Index sample windows. The Managed Agents engineering post notes that the "context anxiety" seen on Sonnet 4.5 was *not present* on Opus 4.5.
- **Claude Opus 4.6** — released coincident with the 5th Economic Index sample window (Feb 2026).
- Family-level cost/speed/performance tradeoff: Haiku (fast, cheap) → Sonnet (default) → Opus (most capable, higher per-token price). The 5th Economic Index report quantifies that users select Opus differentially for higher-value tasks: **+1.48 pp Opus per +$10/hour** task value (Claude.ai); **+2.79 pp per +$10** (1P API — about twice as steep).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "anthropic")
SORT file.name ASC
```

## Open questions

- The wiki has multiple references to Claude as a measurement substrate but no primary source on Anthropic itself yet; this entity page is a stub awaiting first-party Anthropic source ingestion.
