---
type: entity
kind: organization
aliases: ["Boston Consulting Group", "BCG", "BCG Henderson Institute"]
tags: [BCG, management-consulting, henderson-institute]
confidence: 0.82
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 4
---

# Boston Consulting Group

Premier global management consulting firm; headquarters Boston. Approximately 1% applicant acceptance rate per the [[2026-04-28-dellacqua-jagged-technological-frontier|Jagged Frontier]] paper. Operates an "up or out" promotion track tied to performance evaluations.

## Henderson Institute

BCG's research arm; provides authors on AI-and-strategy work referenced in this wiki. BCG has launched **BCG X** (the firm's tech build-and-design arm); Matthew Kropp serves as CAIO of BCG X (chief AI officer) per the [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al. HBR research feature]].

## Appears in this wiki via

- [[2026-04-28-dellacqua-jagged-technological-frontier]] — partnered with Harvard / Wharton / MIT / Warwick researchers for a 758-consultant randomized field experiment on GPT-4 use; experimental tasks designed by senior BCG MDs and validated as representative of consulting work.
- BCG senior partners [[François Candelon]], [[Saran Rajendran]], [[Lisa Krayer]] are co-authors on the Jagged Frontier paper.
- [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees]] — BCG Henderson Institute research feature in HBR; Matthew Kropp (BCG managing director / senior partner / CAIO of BCG X), Julie Bedard (BCG managing director / partner; People & Org + AI leadership teams), Megan Hsu (BCG project leader), [[Lisa Krayer]] (BCG principal), plus Boston University's Emma Wiles. RCT (N=1,261) on the *AI-as-employee framing* showing it causes 9pp accountability drop, 44% more escalation, 18% fewer errors caught, 13% higher identity uncertainty.
- [[2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces]] — BCG Henderson Institute microeconomic labor-impact report (Greg Emerson, [[Matthew Kropp]], [[Julie Bedard]], [[Lisa Krayer]], [[Megan Hsu]], et al.): the proprietary **six AI Labor Disruption Segments** (Amplified 5% / Rebalanced 14% / Divergent 12% / Substituted 12% / Enabled 23% / Limited-Exposure 34%) and the **50–55% reshaped / 10–15% eliminated** headline. Promotes [[Matthew Kropp]], [[Julie Bedard]], [[Megan Hsu]] to entities.
- **The Krayer/Kropp pair makes BCG the wiki's first management-consulting firm to anchor two RCT-grade studies on AI's organisational consequences** — first on knowledge-worker productivity (within-the-frontier vs outside), then on framing-and-governance (tool-vs-employee) — now extended by the labor-disruption-segments modeling report.
- **BCG-cited prior research (not separately ingested):** *AI brain fry* study (11% / 39% higher minor / major error frequency under excessive AI use); *AI workforce transformation* study (3.5× managerial-role-modelling at high-maturity orgs); BCG Henderson Institute *executive-vs-IC enthusiasm gap* research (76% / 31% gap).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "BCG")
SORT file.name ASC
```
