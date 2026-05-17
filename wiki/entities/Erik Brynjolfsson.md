---
type: entity
kind: person
aliases: ["Erik Brynjolfsson"]
tags: [stanford, nber, ai-research, digital-economy, labor-economics, productivity]
affiliation: "[[Stanford Digital Economy Lab]] / [[Stanford HAI]] / [[NBER]]"
role: "Director, Stanford Digital Economy Lab; AI Index Steering Committee member"
contact: "erikb@stanford.edu"
confidence: 0.87
last_confirmed: "2026-05-10"
accessed_at: "2026-05-10"
source_count: 4
relationships:
  - type: part-of
    target: Stanford-Digital-Economy-Lab
    via: "Director"
  - type: part-of
    target: AI-Index
    via: "Steering Committee member"
---

# Erik Brynjolfsson

**Erik Brynjolfsson** is a leading academic on the economics of digital technology and AI. Stanford University and NBER affiliated. **Director of the [[Stanford Digital Economy Lab]]**. Member of the [[AI Index]] Steering Committee at [[Stanford HAI]] (so cross-affiliated between Stanford's two major AI-research initiatives).

## Role in the wiki

Brynjolfsson recurs across multiple sources and is the author of two of the most-cited empirical findings in the wiki:

### 1. The "Equalizing Effect" customer-support study (2025 QJE / 2023 NBER WP)

[[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025)]] *"Generative AI at Work"*, **The Quarterly Journal of Economics 140 (2025): 889–942**. Working paper predecessor: NBER 31161 (2023). Field study with **5,172 customer-support agents**, **3M+ chats**, fall 2020 – early 2022, at a Fortune 500 firm using a GPT-3-based AI assistant. Key findings:

- **+15% productivity** in resolutions per hour (preferred specification with year-month + agent + agent-tenure FE: +15.2%; +23.9% with location-only FE).
- **Equalizing effect** with quality nuance: low-skill workers +30% RPH and quality up; **top performers small speed gains AND small quality DECLINE**.
- AI-exposed workers maintain higher efficiency during AI outages — durable learning, not just real-time scaffolding.
- **Treated 2-month-tenured agents perform like untreated 6-month-tenured agents** — AI accelerates the experience curve ~3×.
- Convergence in communication patterns — low-skill agents begin communicating more like high-skill agents.
- Customers more polite, less likely to escalate; reduced worker attrition driven by retention of newer workers.

Note: the wiki previously cited the working-paper version (+14.2%) via [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4. The QJE version of the paper is now the canonical primary source — slight upward revision and added **top-performer-quality-decline** nuance.

### 2. The "Canaries in the Coal Mine" employment study (2025)

[[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025)]], Stanford Digital Economy Lab working paper, Aug 26, 2025. Six facts using ADP payroll data showing:
- **Early-career workers (22–25) in AI-exposed occupations: ~13% relative decline** since late 2022.
- Older workers and less-exposed occupations stable or growing.
- Declines concentrated in **automation** uses, not **augmentation** uses.
- Adjustments visible in **employment more than wages** (wage stickiness).

This is the wiki's headline empirical evidence for AI labor displacement.

### 3. Updated job-postings signal (cited in [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs|Thompson 2026 (NYT The Daily)]])

In the 14 April 2026 episode of *The Daily*, **Clive Thompson** cites a more recent Brynjolfsson analysis of job postings showing **software-developer hires down 16%** *"in the last year or so"* — extending the *Canaries* employment-stock signal (2022 onset, age-22-25 cohort, ~20% software-developer decline by July 2025) into the *hiring-flow* layer through 2025-26. Thompson reports the number verbally without naming the paper; primary-source ingest of the underlying job-postings analysis is an open target. The cited number is structurally consistent with — and somewhat sharper than — the headline numbers from *Canaries*, suggesting the trend is continuing rather than plateauing as AI coding tools mature.

### Cross-paper synthesis

The two papers together describe the **task-level vs. occupation-level paradox** of AI's labor impact:
- *At the task level (within a job)*: AI raises productivity of low-skill / early-career workers more — equalizing.
- *At the occupation level (across firms)*: AI is reducing entry-level employment in occupations where it can substitute for labor — disequalizing.

Both can be true simultaneously. The mechanism: when AI raises individual productivity, total employment in that role depends on how elastic demand is for the role's output. See [[ai-employment-effects]] and [[automation-vs-augmentation]].

## Notable affiliations

- **Stanford University** — faculty
- **[[Stanford Digital Economy Lab]]** — director
- **[[Stanford HAI]]** — affiliated; member of [[AI Index]] Steering Committee
- **NBER** (National Bureau of Economic Research) — research associate

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "brynjolfsson")
SORT file.name ASC
```

## Open questions

- Brynjolfsson's books (*The Second Machine Age* with Andrew McAfee; *Race Against the Machine*; *Machine, Platform, Crowd*) — to be filled in as more sources reference them.
- The **Productivity J-Curve** (Brynjolfsson, Rock, Syverson) framework — relevant to the time-lag between AI investment and measurable productivity. Mentioned only obliquely in the wiki so far.
- His earlier work on **IT productivity paradox** — which his AI-productivity work builds on intellectually.
