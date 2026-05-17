---
type: entity
kind: organization
aliases: ["Anthropic", "Anthropic PBC", "Claude"]
tags: [anthropic, ai-lab, foundation-models, claude, public-benefit-corporation, long-term-benefit-trust]
since: 2021
confidence: 0.92
last_confirmed: "2026-05-14"
accessed_at: "2026-05-14"
source_count: 10
---

# Anthropic

AI safety and research company; publisher of the [[Claude]] family of models and the [[Anthropic Economic Index]] research series. Founded 2021 by **Dario Amodei** and **Daniela Amodei** (with a cohort of OpenAI departures) following the Amodei team's exit from [[OpenAI]] *"two or three OpenAI crises ago"* per [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]]. **Public Benefit Corporation** with a **two-tier governance structure** (see [§Governance structure](#governance-structure) below). Partnered with [[Amazon Web Services]] (~$8B total invested as of 2024 per [[2026-04-28-werner-lebrun-octopus-organization]]).

## Governance structure

Per [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]] (who advised the Amodeis on the structure during Anthropic's founding):

> *"Anthropic has directors on its for-profit board who are appointed by and are accountable to an outside group of trustees who are AI safety experts who do not have equity in Anthropic."*

The mechanism: **Long-Term Benefit Trust (LTBT)** as the **mission guardian** entity. Two-tier:

1. **For-profit board** — the standard corporate governance layer; directors operate under PBC fiduciary obligations.
2. **Long-Term Benefit Trust** — outside trustees who (a) are AI safety experts, (b) hold *no equity* in Anthropic, and (c) **appoint and hold accountable** the for-profit board's directors.

The novel structural property: trustee accountability **flows the right direction with respect to mission-relevant decisions** — directors are accountable to the trust (not to shareholders) on the mission axis. Ries' first-hand framing of what this buys: *"Whenever you see Anthropic do the right thing, like when they refuse to release a model because they think it's too dangerous, think about how much that's costing them."*

Ries (who plays *"no important role"* but *"a very big role"* in the founding-advice phase) was approached by *"one of their investors"* and told the Amodeis *"if you don't get this right, here's what's going to happen"* — the early framing that became the LTBT. Per Ries' framework, **PBC + LTBT** is **strictly stronger** than **PBC alone** ([[OpenAI]]'s post-2025 structure) because the LTBT introduces *outside trustee accountability* that PBC-alone does not.

## Research initiatives appearing in this wiki

- [[Anthropic Economic Index]] — recurring measurement of real-world Claude usage on Claude.ai (consumer) and 1P API (enterprise). Five reports through March 2026.
- Rwanda partnership with **ALX** — AI literacy + Claude Pro access program for African graduates ([[2026-04-28-anthropic-economic-index-q4-2025|fourth Economic Index report]]).
- [[Jack Clark]] — co-founder; serves on the [[AI Index]] steering committee.

## Platform / product engineering

- **Claude Platform** — Anthropic's developer-facing platform.
  - **Claude Managed Agents** — hosted service for long-horizon agent work; brain/hands/session decoupled architecture; published April 2026 ([[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Engineering blog]]).
  - **Claude Code** — agentic coding harness; described as "an excellent harness" in the Managed Agents post; its agentic architecture (splits coding work into smaller API calls labeled as distinct tasks) is the empirical signature of agent-mediated work in the [[2026-05-07-anthropic-economic-index-5-learning-curves|5th Economic Index report]]. Engineering leadership: [[Boris Cherny]] (10–15 concurrent Claude instances + CLAUDE.md as in-workflow learning capture per [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]) and *Fiona Fung* (Director of Engineering; documents the Claude Code team-norms rewrite — JIT planning, code-wins-over-whiteboard debate, manager-starts-as-IC dogfooding, "Claudify everything", "explicit permission to kill processes" — in [[2026-05-08-running-an-ai-native-engineering-org]]).
- **Claude Cowork** — Anthropic collaborative-design product, referenced by [[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo|Spiegel 2026]] in the *designers-shipping-code* discussion (alongside the named team member *Jenny Wen*, head of design at Claude, ex-Figma director — the move from Figma director to Claude IC designer is narrated by Spiegel as a case study in the *crits-as-core-skill* dimension of post-AI design work).

## Third-party uses of the Anthropic API

- **WikiZZ / LLM WikiZZ** ([[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|Mysore 2026]]) — single-author open-source browser-only extension of Karpathy's LLM Wiki pattern that routes API requests via a Cloudflare Worker CORS proxy to **NVIDIA NIM, Anthropic, and Gemini** as user-selectable provider backends. The wiki's first **third-party-developer-tool-uses-Anthropic-API** mention in the [[concepts/llm-wiki|LLM Wiki]] cluster. Surfaced here as a one-line context note; the substantive treatment is on the source page.

## Models referenced in this wiki

- [[Claude Sonnet 4.5]] — predominant model in the November 2025 Economic Index sample. Referenced as exhibiting "context anxiety" (premature task wrap-up) in the Managed Agents engineering post.
- **Claude Opus 4.5** — released between the 4th and 5th Economic Index sample windows. The Managed Agents engineering post notes that the "context anxiety" seen on Sonnet 4.5 was *not present* on Opus 4.5.
- **Claude Opus 4.6** — released coincident with the 5th Economic Index sample window (Feb 2026).
- Family-level cost/speed/performance tradeoff: Haiku (fast, cheap) → Sonnet (default) → Opus (most capable, higher per-token price). The 5th Economic Index report quantifies that users select Opus differentially for higher-value tasks: **+1.48 pp Opus per +$10/hour** task value (Claude.ai); **+2.79 pp per +$10** (1P API — about twice as steep).

## As a flow-state organisation

Two recent sources name Anthropic specifically as a *flow-state organisation* — a place where structural pressure + lack of hierarchy strips away traditional thinking:

- [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]] frames it from the **governance** layer: PBC + LTBT make the structural mission-protection real.
- [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath 2026]] names it from the **operating-structure** layer: *"if you find one of these places — Anthropic is such a place, OpenAI is such a place, Facebook was such a place, Google was such a place, SpaceX is such a place"* — alongside no-org-chart and chronic-under-hire as deliberate organisational design.

The two framings are at different layers (governance vs operating-structure) but converge on Anthropic as **the AI-era exemplar** of the category.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "anthropic")
SORT file.name ASC
```

## Open questions

- The wiki has multiple references to Claude as a measurement substrate but no primary source on Anthropic itself yet; this entity page is a stub awaiting first-party Anthropic source ingestion.
