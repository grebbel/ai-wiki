---
type: entity
kind: organization
aliases: ["MIT SMR", "MIT Sloan Management Review", "Sloan Review", "Sloan Management Review"]
tags: [mit-smr, mit, publisher, ai-research, big-ideas-research, organizational-learning]
since: 1959
confidence: 0.88
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 6
relationships:
  - type: published-by
    target: 2026-04-28-mit-sloan-ai-maturity
  - type: published-by
    target: 2026-05-07-ransbotham-augmented-learners
  - type: published-by
    target: 2026-05-07-kiron-schrage-compound-benefits
  - type: published-by
    target: 2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care
    via: "Carla Goulart Peron (Philips Chief Medical Officer) interviewed by Sam Ransbotham on the *Me, Myself, and AI* podcast (Season 13, 31 May 2026) on AI-for-interoperability in health care — the wiki's first dedicated healthcare-AI source and the first *Me, Myself, and AI* podcast ingest under the MIT SMR `author:` value"
  - type: published-by
    target: 2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner
    via: "Multi-speaker compilation from the 2026 MIT Sloan CIO Symposium (host: EIC Abbie Lundberg); 11 leaders on human–agent collaboration"
---

# MIT Sloan Management Review

The research-and-management magazine of [[MIT Sloan School of Management]] — distinct from **MIT Technology Review** and from **MIT Technology Review Insights** (the custom-publishing arm that produced the [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] sponsored research). MIT SMR runs ongoing research initiatives under its **Big Ideas** program, including the **Artificial Intelligence and Business Strategy** track that has produced an 8-year panel of comparable global surveys on AI in business.

## Editorial / research structure

- **Magazine + digital**: peer-reviewed-style management writing for senior executives. Recurring contributors include MIT Sloan faculty and guest authors.
- **Big Ideas Initiatives**: original research on issues transforming the business environment, conducted via global surveys + structured executive interviews. The AI track has been running annually since 2017.
- **Editorial leadership**: [[David Kiron]] is editorial director, research, and program lead for Big Ideas.
- **Guest editors**: senior academic researchers anchor specific tracks; [[Sam Ransbotham]] (Boston College) is guest editor of the AI and Business Strategy initiative.

## Wiki sources published by MIT SMR

- [[2026-04-28-mit-sloan-ai-maturity]] — Kristin Burnham (writer) reporting on [[MIT CISR]] Four Stages of AI Maturity research, Oct 2025.
- [[2026-05-07-ransbotham-augmented-learners]] — Ransbotham, Kiron, Khodabandeh, Chu, Zhukov, *Learning to Manage Uncertainty, With AI* (8th annual MIT SMR × BCG study), Nov 2024.
- [[2026-05-07-kiron-schrage-compound-benefits]] — Kiron & Schrage, *How to Reap Compound Benefits From Generative AI*, Apr 2026.
- [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care]] — Peron (Philips CMO) interviewed by Ransbotham on *Me, Myself, and AI* podcast, S13, 31 May 2026. **The first podcast-format MIT SMR source in the wiki** (prior three are written-research outputs); also the wiki's first dedicated healthcare-AI source.
- [[2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner]] — *Agentic AI: What Leaders Wish They Knew Sooner*, a multi-speaker compilation from the **2026 MIT Sloan CIO Symposium** hosted by EIC **Abbie Lundberg** (11 June 2026). The wiki's **first MIT SMR field-interview/video source**; 11 leaders on human–agent collaboration, including research fellow [[Michael Schrage]] (promoted to an entity on this ingest).

## Distinguishing from sibling MIT publications

The wiki references **three** distinct MIT-affiliated publications:

| Publication | Affiliation | Editorial model | Wiki source(s) |
|---|---|---|---|
| **MIT Sloan Management Review** | MIT Sloan School of Management | Independent magazine; Big Ideas research initiatives | [[2026-04-28-mit-sloan-ai-maturity]], [[2026-05-07-ransbotham-augmented-learners]], [[2026-05-07-kiron-schrage-compound-benefits]] |
| **MIT Technology Review Insights** | MIT Technology Review's custom-publishing arm | Sponsored research (vendor-funded) | [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] |
| **MIT Sloan / Ideas Made to Matter** | MIT Sloan editorial site | News reporting | (referenced via [[2026-04-28-mit-sloan-ai-maturity]]) |

The distinction matters for source-quality assessment: MIT SMR's Big Ideas research is editorially independent (BCG is a research collaborator, not a sponsor of the publication itself), while MIT Tech Review Insights is explicitly sponsored research.

## Recurring research partners

- **[[Boston Consulting Group]]** — research collaborator on the 8-year AI-in-business panel; co-publishes the annual Big Ideas Research Reports.
- **[[BCG Henderson Institute]]** — BCG's think tank; supporting sponsor of the annual reports.
- **BCG X** — BCG's tech build / design unit (~3,000 technologists across 80+ cities); supporting sponsor.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mit-smr")
SORT file.name ASC
```
