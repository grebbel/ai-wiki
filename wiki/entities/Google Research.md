---
type: entity
kind: organization
aliases: ["Google Research", "Google AI Research", "Google DeepMind Research"]
tags: [google-research, google, ai-research, foundation-models, gemini, durable-skills]
confidence: 0.80
last_confirmed: "2026-06-12"
accessed_at: "2026-06-12"
source_count: 5
---

# Google Research

The research arm of Google, focused on advancing fundamental and applied research in AI, computer science, and adjacent fields. Producer of the **Gemini** model family (cited extensively in the wiki — the 280×-cost-reduction marker comes from Gemini-1.5-Flash-8B), and a recurring data partner of the [[AI Index]] (the 2025 and 2026 AI Index editions disclose Google Research as an analytics/funding partner).

This entity page covers the research organisation; for product-line discussion (Gemini family, foundation models broadly) see [[foundation-models]].

## Appears in this wiki via

- [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting]] — **publisher (Brain team, with Princeton) of the foundational [[react-reasoning-acting|ReAct]] paper** (ICLR 2023). The wiki's earliest primary research source and the genealogical root of its [[ai-agents|agent]]/[[agent-harness|harness]] cluster. Authors [[Shunyu Yao]] (Princeton intern) and [[Yuan Cao]] (Brain team) were promoted to entities on this ingest.
- [[2022-11-08-yao-cao-react-google-research-blog]] — the **Google Research Blog** popularisation of the same ReAct work (8 Nov 2022). The accessible register paired with the rigorous paper.
- [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills]] — primary publisher of *Towards Scalable Measurement of Durable Skills* (preprint, 12 April 2026). Globerson et al. (~40 co-authors) introduce the Vantage assessment platform, Executive LLM steering protocol, and Gemini-based AI Evaluator — anchoring the wiki's [[durable-skills]] concept.
- [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer]] — Google I/O 2026 talk by **Nicole Forsgren** and **Andrew Macvean**, both leads on Google's **Developer Intelligence team**. The talk anchors the **DORA programme** (Forsgren-led) as a Google-Research-lineage empirical backbone for two load-bearing claims: (a) AI's productivity paradox at the team-level (the engineering-team correlate of [[micro-productivity-trap]]); (b) AI as **amplifier-and-mirror** — magnifying existing organisational strengths and weaknesses. Sister-vantage to the Globerson et al. paper: both Google-Research-lineage outputs map durable / non-routine engineering skills, one from psychometrics, the other from inside-Google measurement.
- Mentioned across multiple wiki sources as a major model contributor (Gemini family is referenced in [[2026-04-28-ai-index-report-2025|AI Index 2025]] §1 — Gemini-1.5-Flash-8B as the cost-reduction marker; [[2026-04-30-ai-index-report-2026|AI Index 2026]] continues to track Google's models alongside OpenAI, Anthropic, Meta, and others).

## Notable people (in this wiki)

- [[Yossi Matias]] *(dangling — co-author on the durable skills paper; promote on 2nd-source coverage)* — VP and Head of Google Research.
- **Nicole Forsgren** *(dangling — first-mention; high probability of recurrence given DORA stature and *Accelerate* authorship)* — lead, Developer Intelligence team; DORA founder.
- **Andrew Macvean** *(dangling — first-mention)* — lead, Developer Intelligence team.
- ~40 other co-authors of the Globerson et al. paper, currently listed in the source-page frontmatter but not promoted to individual entity pages (single-source coverage).

## Research programmes referenced in this wiki

- **Developer Intelligence team** — Google's in-house team studying how Google engineers work with AI. Anchor for [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean 2026]]; named on stage as "measuring the engineering system and all the pieces within that ... the end-to-end time to go from an initial seed of an idea all the way through to getting that idea out into a real user's hands."
- **DORA (DevOps Research and Assessment)** — long-running Forsgren-led programme running annual State of DevOps reports since 2013; provides the empirical backbone for productivity-paradox and amplifier-and-mirror claims cited in the I/O 2026 talk. First wiki-reference here; promote to its own entity page on second-source coverage.

## Funders / partnerships visible in this wiki

- **AI Index** — Google is listed as a supporting funder of the AI Index 2025 and 2026 editions ([[2026-04-30-ai-index-report-2026]]).
- **OpenMic, NYU, UT Austin** — academic and startup collaborators on the durable skills work.

## Notable products / models

The full model roster is tracked in [[foundation-models]]. Selected highlights:

- **Gemini family** (1.5, 2.5 Pro, 3.0) — Google Research's primary multimodal foundation model line. Cited as the substrate for the Vantage Executive LLM and AI Evaluator.
- **Veo 2** (video generation) — referenced via [[2026-04-28-ai-index-report-2025|AI Index 2025]].

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "google-research")
SORT file.name ASC
```

## Open questions

- The relationship between Google Research and Google DeepMind — separately structured units that often co-author. The Globerson et al. paper is published under "Google Research" affiliation; whether DeepMind shares authorship would clarify the institutional boundary.
- Google's broader AI Index funding/data-partner role — which surveys, which methodological choices.
- The institutional boundary between **Google Research (proper)** and the **Developer Intelligence team** that Forsgren and Macvean lead — the latter's outputs map cleanly to engineering-research even if formally attached to Developer Relations rather than the Research arm. Worth clarifying on a third source.
- **DORA's published methodology for the AI-era productivity-paradox finding.** Forsgren cited the result live; a published State of DevOps or DORA AI-specific report substantiating the individual-vs-team divergence would meaningfully strengthen the wiki's [[micro-productivity-trap]] page.
