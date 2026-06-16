---
type: entity
kind: project
aliases: ["AI Index", "AI Index Report", "Stanford AI Index"]
tags: [ai-index, stanford-hai, ai-research, annual-report]
parent: "[[Stanford HAI]]"
since: 2017
confidence: 0.85
last_confirmed: "2026-05-28"
accessed_at: "2026-05-28"
source_count: 3
relationships:
  - type: part-of
    target: Stanford-HAI
    via: "AI Index is an independent initiative within Stanford HAI"
  - type: employs
    target: Yolanda-Gil
    via: "Steering Committee chair (2026 edition)"
  - type: employs
    target: Sha-Sajadieh
    via: "Editor-in-Chief (2026 edition)"
  - type: employs
    target: Nestor-Maslej
    via: "Research Manager and former Editor-in-Chief"
  - type: employs
    target: Erik-Brynjolfsson
    via: "Steering Committee member"
---

# AI Index

The **AI Index** is an independent initiative at [[Stanford HAI]] that produces an annual report on the state of artificial intelligence. Conceived in 2017 within the [[One Hundred Year Study on AI]] (AI100). The 2026 edition is the 9th annual.

Mission (per the report): equip policymakers, journalists, executives, researchers, and the public with **accurate, rigorously validated, globally sourced data** on AI's development, adoption, and impact.

## What it tracks

| Chapter (2026) | Mapped to wiki concept |
|---|---|
| 1. Research and Development (publications, patents, models, compute, energy) | [[foundation-models]] |
| 2. Technical Performance (benchmarks) | [[ai-benchmarks]] |
| 3. Responsible AI (incidents, transparency, governance) | [[responsible-ai]] |
| 4. Economy (adoption, investment, jobs, robots) | [[enterprise-ai-adoption]], [[ai-employment-effects]] |
| 5. Science (new standalone in 2026) | _no concept page yet_ |
| 6. Medicine (new standalone in 2026, with [[Schmidt Sciences]]) | _no concept page yet_ |
| 7. Education | _no concept page yet_ |
| 8. Policy and Governance | _no concept page yet_ |
| 9. Public Opinion | _no concept page yet_ |

In the 2025 edition, Science and Medicine were combined into a single chapter; the 2026 edition split them, adding a new ninth chapter overall.

## Editions

| Year | Edition | Status |
|---|---|---|
| 2017–2024 | 1–7 | Not yet ingested |
| 2025 | 8 | [[2026-04-28-ai-index-report-2025\|Ingested]] — adds AI hardware deep-dive, novel inference cost estimates, fresh corporate adoption of [[responsible-ai]] data, expanded science/medicine coverage |
| 2026 | 9 | [[2026-04-30-ai-index-report-2026\|Ingested]] — Medicine chapter spun off as standalone (with [[Schmidt Sciences]]); AI sovereignty as new analytical framework; new GenAI consumer-value estimates; "jagged frontier" enters the report's narrative |

(Earlier editions to be filled in as / if they're ingested.)

## Steering Committee (2026 edition)

- **Chair**: [[Yolanda Gil]] (USC, Information Sciences Institute)
- **Co-chair**: [[Raymond Perrault]] (SRI International)
- **Members**: [[Russ Altman]] (Stanford), [[Carla Brodley]] (Northeastern), [[Erik Brynjolfsson]] (Stanford), [[Jack Clark]] (Anthropic, OECD), [[Virginia Dignum]] (Umeå), [[Vipin Kumar]] (U Minnesota), [[James Landay]] (Stanford), [[Terah Lyons]] (JPMorgan Chase), [[James Manyika]] (Google, U Oxford), [[Juan Carlos Niebles]] (Stanford, Salesforce), [[Vanessa Parli]] (Stanford), [[Yoav Shoham]] (Stanford, AI21 Labs), [[Elham Tabassi]] (Brookings), [[Russell Wald]] (Stanford), [[Toby Walsh]] (UNSW Sydney), [[Dan Weld]] (U Washington)
- **Editor-in-Chief**: [[Sha Sajadieh]] (Stanford)
- **Research Manager**: [[Loredana Fattorini]] (Stanford)

### Changes from 2025 edition

- **Chair role flipped**: [[Yolanda Gil]] moved from chair-elect to chair; [[Raymond Perrault]] from chair to co-chair.
- **New EiC**: [[Sha Sajadieh]] replaces [[Nestor Maslej]] (Maslej remains an active contributor in 2026).
- **Joined**: [[Russ Altman]], [[Carla Brodley]], [[Virginia Dignum]], [[Vipin Kumar]], [[James Landay]], [[Elham Tabassi]], [[Dan Weld]].
- **Departed**: [[John Etchemendy]] (Stanford), [[Katrina Ligett]] (Hebrew University).

## Data partners (2026 edition)

[[Center for Research on Foundation Models]], CSTA, Digital Policy Alert, [[Epoch AI]], [[ECEP]] (Expanding Computing Education Pathways), GitHub, [[International Federation of Robotics]] (IFR), Kapor Foundation, [[Lightcast]], LinkedIn, [[McKinsey & Company]], RAISE Health, [[Schmidt Sciences]] *(new)*, [[Zeki]].

## Supporting funders (2026 edition)

Google, NSF, [[OpenAI]], Open Philanthropy, [[Quid]], **[[Infosys]]** *(new)*.

## Methodological notes

- The report uses external surveys (notably [[McKinsey & Company]]'s Global AI Survey for adoption data) rather than original surveys for most adoption and use-case data. When citing AI Index adoption numbers, the underlying instrument is typically McKinsey's, not a Stanford instrument.
- AI tooling acknowledgement (2026): ChatGPT and Claude used to refine and copy-edit drafts; all images generated with AI (Johanna Friedman 2026, Gemini 3.1 / Gemini 3). The 2025 edition disclosed Claude/ChatGPT for copy-editing only.
- License: CC BY-ND 4.0 (no derivatives). Public data and chart files released alongside the report on Google Drive; Global AI Vibrancy Tool covers 36 countries (up from ~30 in 2025).
- Notable-models data partner: [[Epoch AI]]. Year-over-year counts may differ as new/historic models are added retroactively.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-index")
SORT file.name ASC
```

## Open questions

- Year-over-year stability of methodology (e.g., adoption numbers depend on McKinsey instrument changes).
- The Global AI Vibrancy Tool (now 36 countries) — is it useful enough to file as its own resource page once engaged with?
- The Medicine chapter being split off in 2026 is an editorial signal; comparison of 2025-combined vs 2026-split coverage of medicine may surface new findings worth ingesting.
