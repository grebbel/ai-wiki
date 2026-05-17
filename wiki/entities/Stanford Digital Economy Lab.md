---
type: entity
kind: project
aliases: ["Stanford Digital Economy Lab", "Digital Economy Lab"]
tags: [stanford, ai-research, digital-economy, labor-economics, working-papers]
parent: "[[Stanford University]]"
director: "[[Erik Brynjolfsson]]"
website: "https://digitaleconomy.stanford.edu"
confidence: 0.75
last_confirmed: "2026-04-28"
accessed_at: "2026-04-28"
source_count: 1
relationships:
  - type: employs
    target: Erik-Brynjolfsson
    via: "Director"
---

# Stanford Digital Economy Lab

The **Stanford Digital Economy Lab** is a research initiative at Stanford University focused on the economics of digital technology and AI — productivity, labor markets, market structure, measurement of intangible capital. Directed by [[Erik Brynjolfsson]].

**Distinct from [[Stanford HAI]] and the [[AI Index]]**, though personnel overlap: Brynjolfsson is on the AI Index Steering Committee and the Digital Economy Lab director.

## Role in the wiki

Publisher of [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025) "Canaries in the Coal Mine?"]] — the wiki's primary empirical source on AI's recent employment effects.

Likely future-recurring as a source of empirical AI-economics research. Brynjolfsson's earlier customer-support productivity study (Brynjolfsson, Li & Rock 2023, NBER 31161 → QJE 2025) also originated from this research stream; not yet ingested as its own source page (currently summarized via [[Erik Brynjolfsson]] entity page).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "stanford-digital-economy-lab")
SORT file.name ASC
```

## Open questions

- Lab's funding model and full personnel roster.
- Other published Digital Economy Lab papers worth ingesting standalone (vs. cited via Brynjolfsson entity page).
- Relationship to Stanford's broader economics department (HAI vs. Digital Economy Lab vs. econ dept — overlapping AI-economics communities).
