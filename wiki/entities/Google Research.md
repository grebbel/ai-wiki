---
type: entity
kind: organization
aliases: ["Google Research", "Google AI Research", "Google DeepMind Research"]
tags: [google-research, google, ai-research, foundation-models, gemini, durable-skills]
confidence: 0.75
last_confirmed: "2026-05-07"
accessed_at: "2026-05-07"
source_count: 2
---

# Google Research

The research arm of Google, focused on advancing fundamental and applied research in AI, computer science, and adjacent fields. Producer of the **Gemini** model family (cited extensively in the wiki — the 280×-cost-reduction marker comes from Gemini-1.5-Flash-8B), and a recurring data partner of the [[AI Index]] (the 2025 and 2026 AI Index editions disclose Google Research as an analytics/funding partner).

This entity page covers the research organisation; for product-line discussion (Gemini family, foundation models broadly) see [[foundation-models]].

## Appears in this wiki via

- [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills]] — primary publisher of *Towards Scalable Measurement of Durable Skills* (preprint, 12 April 2026). Globerson et al. (~40 co-authors) introduce the Vantage assessment platform, Executive LLM steering protocol, and Gemini-based AI Evaluator — anchoring the wiki's [[durable-skills]] concept.
- Mentioned across multiple wiki sources as a major model contributor (Gemini family is referenced in [[2026-04-28-ai-index-report-2025|AI Index 2025]] §1 — Gemini-1.5-Flash-8B as the cost-reduction marker; [[2026-04-30-ai-index-report-2026|AI Index 2026]] continues to track Google's models alongside OpenAI, Anthropic, Meta, and others).

## Notable people (in this wiki)

- [[Yossi Matias]] *(dangling — co-author on the durable skills paper; promote on 2nd-source coverage)* — VP and Head of Google Research.
- ~40 other co-authors of the Globerson et al. paper, currently listed in the source-page frontmatter but not promoted to individual entity pages (single-source coverage).

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
- A 2nd Google Research source would deepen this entity beyond the current durable-skills anchor; the AI Index editions are mentions-of-Google rather than first-party Google Research output.
