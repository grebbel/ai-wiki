---
type: entity
kind: person
aliases: ["Pete Koomen", "Pete Kumman"]
tags: [pete-koomen, y-combinator, optimizely-co-founder, horseless-carriages-essay, yc-internal-ai-infrastructure, multiplayer-harness, skillify-resolver, ai-as-building-layer]
affiliation: "[[Y Combinator]]"
role: "General Partner, Y Combinator; co-founder of Optimizely (A/B testing platform); architect of YC's internal AI agent infrastructure"
confidence: 0.75
last_confirmed: "2026-05-28"
accessed_at: "2026-05-28"
source_count: 2
relationships:
  - type: part-of
    target: Y-Combinator
    via: "General Partner; led the YC-internal AI infrastructure project"
  - type: authored-by
    target: 2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook
    via: "guest on the Lightcone podcast — 46-minute architecture-and-organisation talk on the YC-internal AI infrastructure he built"
---

# Pete Koomen

**General Partner at [[Y Combinator]]** and the architect of YC's internal AI agent infrastructure. Previously co-founder of **Optimizely** (one of the first and most widely-adopted A/B testing platforms for apps and websites). Author of the **[[Horseless Carriages|*Horseless Carriages*]] essay** — a critique of *AI-as-feature-inside-deterministic-software* pattern (the Gmail email-writer as canonical example) which argues that AI-native software should look like *agent wrapping deterministic tools* rather than *deterministic software wrapping AI*.

At YC, Koomen led the year-long effort (started ~mid-2025) to build the firm's internal AI agent infrastructure: a shared-tool-registry (≥350 tools as of May 2026), a shared-skill-registry with the *skillify / DRY / MECE resolver* pattern, broadcast-by-default agent conversations, a self-improving dream-cycle, and a single Postgres-substrate *one database to rule them all* approach (*"BigTable for agents"*). His framing of the **multiplayer-harness gap** ([[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Lightcone podcast, 27 May 2026]]) is the wiki's first explicit *single-player → multiplayer harness-engineering progression* — naming the team / org-scale problem that the existing single-player harness sources ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Khan]], [[2026-05-15-osmani-agent-harness-engineering|Osmani]], [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]) don't address.

## Appears in this wiki via

- [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself]] — referenced as the architect of YC's internal infrastructure (Garg's 5-minute IC-vantage on the same project).
- [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook]] — guest on the Lightcone podcast (~46:30); first-person architecture-and-organisation talk on YC's internal AI infrastructure; names the **multiplayer-harness gap**, the **$100K-token-budget leapfrog** argument, the **egalitarian + trust-by-default precondition**, and the **two-sentence-pitch skill as worked example of org-scale super-intelligence compounding**.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "pete-koomen")
SORT file.name ASC
```

## Open questions

- The *Horseless Carriages* essay itself — is it worth ingesting as a separate `kind: article` source page? (It is the conceptual substrate for Koomen's *AI-as-building-layer* framing.)
- Pete Koomen's role at Optimizely before YC — is there a substantive thread connecting A/B-testing-platform design lessons to YC-internal-agent-infrastructure design? (Worth flagging as a follow-up if a second source addresses it.)
