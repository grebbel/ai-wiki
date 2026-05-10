---
type: entity
kind: organization
aliases: ["McKinsey", "McKinsey & Company", "McKinsey and Company", "QuantumBlack"]
tags: [mckinsey, management-consulting, quantumblack, ai-research, tech-ai-transformation, agent-augmented-workforce, outcome-underwriting, post-controversy-governance]
confidence: 0.88
last_confirmed: "2026-05-10"
source_count: 5
relationships:
  - type: employs
    target: Eric-Lamarre
  - type: employs
    target: Kate-Smaje
  - type: employs
    target: Rob-Levin
  - type: employs
    target: Alex-Singla
  - type: employs
    target: Alexander-Sukharevsky
---

# McKinsey & Company

Global management consulting firm; runs **QuantumBlack** as its AI arm. A recurring data partner of the [[AI Index]] (the McKinsey Global AI Survey is the underlying instrument behind many AI Index adoption numbers — see methodological notes on the [[AI Index]] entity page). The wiki holds two complementary first-party McKinsey sources as of May 2026: *[[2026-05-03-rewired-second-edition-sample|Rewired 2nd ed]]* (the practitioner playbook for clients) and [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026 (HBR IdeaCast)]] (the firm-as-vendor self-narrative — McKinsey's own AI strategy, hiring overhaul, post-controversy governance, and business-model migration to outcome-underwriting).

## Appears in this wiki via

- [[2026-05-03-rewired-second-edition-sample]] — *Rewired*, McKinsey's flagship Tech & AI transformation playbook (2nd edition, Wiley 2026). Authors: [[Eric Lamarre]], [[Kate Smaje]], [[Rob Levin]] (with [[Alex Singla]] and [[Alexander Sukharevsky]] from QuantumBlack). Headline empirical claims drawn from McKinsey client work: **20% EBITDA uplift on average**, **$3 of incremental EBITDA per $1 invested**, **1–2 year breakeven**, across ~20 deep-dive AI-leader companies (drawn from a study set of ~200 companies).
- [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting]] — *How McKinsey Plans to Survive AI (and Reinvent Consulting)* (HBR IdeaCast, 9 Feb 2026). Bob Sternfels (Global Managing Partner) interviewed by Adi Ignatius (HBR editor-in-chief). The firm-as-vendor self-narrative. Surfaces the **40k humans + 20k agents = 60k workforce** datapoint (up from 3k agents 18 months prior; on track for **1:1 human-to-agent ratio in ~18 months**), the **outcome-underwriting business model** migration (~33% of revenues today; aspirationally majority by end-of-Sternfels-term), the **post-controversy compliance overhaul** ($1B invested; head of internal audit hired from Apple, head of compliance from Walmart; publicly-traded-equivalent governance standards adopted despite remaining private), and the **hiring-process overhaul** based on 20-year self-applied analytics (now indexes on resilience / team-sport-experience / aptitude-to-learn rather than perfect-marks credentials).
- [[AI Index]] — recurring analytics/research partner; the 2025 and 2026 editions explicitly disclose McKinsey instruments behind adoption data.
- [[2026-04-28-mit-sloan-ai-maturity]] — MIT CISR's Total AI Effectiveness measure draws on a McKinsey survey for adoption baselines.

## Affiliated authors in this wiki

- [[Eric Lamarre]] — Rewired 2nd ed lead author
- [[Kate Smaje]] — Rewired 2nd ed co-author
- [[Rob Levin]] — Rewired 2nd ed co-author
- [[Alex Singla]] — QuantumBlack global co-leader; Rewired contributing author
- [[Alexander Sukharevsky]] — QuantumBlack global co-leader; Rewired contributing author
- **Bob Sternfels** — Global Managing Partner since 2021. **First wiki source mention by name** in [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026]]. Per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion), do not promote on a single source — listed as Dangling. Promote on second-source mention.
- **Gil Clee** (likely; ASR-uncertain rendering "Gil Klee" in the manual transcript) — McKinsey Managing Director ~1967–1973 (Marvin Bower's successor); author of a 1959 HBR paper Sternfels names as the precursor to the matrix-organization concept. First wiki mention; defer entity promotion (single source).

## Methodological notes

- McKinsey's **annual Global AI Survey** is the underlying instrument for several AI-adoption headline numbers across the wiki (most visibly the 78%/88% organizational adoption figures in the [[AI Index]] 2025 / 2026 editions).
- **Rewired's 20% EBITDA uplift** comes from McKinsey's deep-dive case work on AI-leader companies, not from a representative sample. This is *vendor-of-deployment data*, useful but selection-effect-aware. Independent corroboration: see the [[2026-04-30-ai-index-report-2026|AI Index 2026]]'s 14–26% productivity-gain range in customer support and software development, and the [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI HBR 2026]]'s 10–25% EBITDA range.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mckinsey")
SORT file.name ASC
```
