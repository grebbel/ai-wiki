---
type: entity
kind: org
aliases: ["MIT CISR", "MIT Center for Information Systems Research", "Center for Information Systems Research"]
tags: [mit-sloan, mit, ai-research, business-research, digital-transformation]
parent: "[[MIT Sloan]]"
website: "https://cisr.mit.edu"
confidence: 0.75
last_confirmed: "2026-04-28"
accessed_at: "2026-06-05"
source_count: 1
relationships:
  - type: employs
    target: Stephanie-Woerner
    via: "Director"
  - type: employs
    target: Peter-Weill
    via: "Chairman"
---

# MIT CISR

The **MIT Center for Information Systems Research** is a research center at the [[MIT Sloan]] School of Management, focused on how organizations use technology and data to compete and create value. Studies digital business models, IT investment portfolios, AI maturity, and large-enterprise transformation.

## Role in the wiki

A primary research source for **enterprise transformation in the digital economy** — methodologically distinct from McKinsey-style consulting research (which underpins much of the [[2026-04-28-ai-index-report-2025|AI Index]] adoption data). MIT CISR's lens is **stage-based maturity models** rather than per-function adoption rates.

Key methodological instruments mentioned in the wiki:

- **Future Ready Survey** (last published wave used: 2022, N=721) — large-N quantitative input.
- **Executive interviews** (e.g., 2024: 16 executives at 9 enterprises) — qualitative depth on transitions.
- Combined into **maturity scoring** (0–100% Total AI Effectiveness scale, banded into stages).

## Frameworks attributed to MIT CISR (in the wiki)

- **Four Stages of Enterprise AI Maturity** — see [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan article]] and [[enterprise-ai-adoption]].
- **Four S Framework** (Strategy / Systems / Synchronization / Stewardship) — challenges to scale Stage 2 → Stage 3.

## Notable people (mentioned in this wiki)

- [[Stephanie Woerner]] — Principal research scientist at MIT Sloan, **Director of MIT CISR**.
- [[Peter Weill]] — Senior research scientist at MIT Sloan, **Chairman of MIT CISR**.
- [[Ina Sebastian]] — Research scientist at MIT CISR (digital partnering, value creation, value capture).
- [[Evgeny Káganer]] — Research collaborator (also professor at IESE Business School).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mit-cisr")
SORT file.name ASC
```

## Open questions

- Funding model and member organizations of CISR (it's typically a member-funded research center; details to fill in as more sources reference it).
- Earlier Future Ready Survey waves (pre-2022) and how methodology has evolved.
