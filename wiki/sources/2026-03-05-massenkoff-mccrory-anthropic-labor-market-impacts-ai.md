---
type: source
kind: report
title: "Labor market impacts of AI: A new measure and early evidence"
author: ["Maxim Massenkoff", "Peter McCrory"]
publisher: "Anthropic (Anthropic Economic Index)"
url: "https://www.anthropic.com/research/labor-market-impacts"
date_published: 2026-03-05
date_ingested: 2026-06-15
length: "~17 pages (full text read; figures described from captions)"
raw: "../../raw/reports/Nowcasting_Econ-Report-v16.pdf"
tags: [anthropic, anthropic-economic-index, observed-exposure, labor-market-impacts, ai-employment-effects, onet, eloundou-exposure, automation-vs-augmentation, young-worker-hiring, unemployment, bls-projections, current-population-survey, brynjolfsson-canaries, massenkoff-mccrory, methodology]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: published-by
    target: Anthropic
    via: "Anthropic research note; part of the Anthropic Economic Index program; data on Hugging Face (Anthropic/EconomicIndex)"
  - type: part-of
    target: Anthropic-Economic-Index
    via: "introduces the labor-impact (observed-exposure) measure built on the Economic Index usage data; the analytic complement to the AEI usage reports"
  - type: supports
    target: 2026-04-28-anthropic-economic-index-q4-2025
    via: "sibling Anthropic Economic Index output — the AEI usage reports supply the real-world usage data this report weights against theoretical capability to build observed exposure"
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "independently echoes the Brynjolfsson young-worker finding (a hiring slowdown into exposed occupations for ages 22–25) using CPS job-start panels rather than ADP payroll — corroboration via a different dataset, while finding the effect 'barely statistically significant'"
---

# Labor market impacts of AI: A new measure and early evidence

The **methodological primary source** behind the "observed exposure" labor measure the wiki has been citing second-hand. Published by **[[Anthropic]]** (5 March 2026) as part of the [[Anthropic Economic Index]] program; authors **Maxim Massenkoff** (Naval Postgraduate School) and **Peter McCrory** (Anthropic). It is the study **[[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Brovich (AWS)]] described on stage** ("Anthropic from March of this year… observed vs theoretical exposure"), and the analytic backbone for several claims on [[ai-employment-effects]].

## Key findings

- **A new measure — *observed exposure*.** Combines (1) theoretical LLM capability (Eloundou et al. 2023 task β-ratings — can an LLM make the task ≥2× faster) with (2) **real-world usage** from the [[Anthropic Economic Index]], **weighting automated (rather than augmentative) and work-related uses more heavily**, aggregated from O*NET's ~800 occupations' tasks up to the occupation level. The automation/augmentation weighting is the methodological heart — it is what separates *displacement risk* from mere *exposure*.
- **AI is far from its theoretical ceiling.** Actual coverage is a fraction of what's feasible. Tasks rated fully feasible (β=1) account for **68% of observed Claude usage**; β=0 tasks just 3% — usage concentrates where capability is highest, but most theoretically-automatable work is not yet being done by AI at scale.
- **Most-exposed occupations.** Computer Programmers (**75% coverage**), Customer Service Representatives, Data Entry Keyers (67%), financial analysts. **30% of workers have *zero* coverage** (Cooks, Bartenders, Lifeguards, Dishwashers, Motorcycle Mechanics, Dressing Room Attendants) — tasks too infrequent in the data to meet threshold.
- **Exposure tracks (weakly) with lower projected growth.** Regression at the occupation level (employment-weighted): every **+10pp coverage → −0.6pp** in the BLS 2024–2034 growth projection. Slight but real validation against independently-derived analyst estimates — and notably **the Eloundou measure *alone* shows no such correlation**, evidence the usage-weighting adds signal.
- **Who the exposed are.** Top-quartile-exposure workers (measured Aug–Oct 2022, pre-ChatGPT) are **16pp more likely female, 11pp more likely white, ~2× as likely Asian, earn 47% more, and are far more educated** (graduate degrees: 4.5% of unexposed vs 17.4% of most-exposed — ~4×). This inverts the older "AI hits low-skill first" narrative.
- **No systematic unemployment effect yet.** Difference-in-differences (top-quartile vs zero-exposure, CPS) since ChatGPT: the gap change is **small and statistically indistinguishable from zero**. The framework could detect a **~1pp** differential increase; a "white-collar Great Recession" (top-quartile unemployment doubling 3%→6%) would be visible.
- **Suggestive young-worker hiring slowdown.** Using the CPS panel's job-*start* rate for ages 22–25: entry into the most-exposed occupations falls ~½pp; the post-ChatGPT estimate is a **~14% drop in the job-finding rate** vs 2022 (barely statistically significant; no such drop for >25). Echoes [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al.]]'s 6–16% employment fall for 22–25-year-olds in exposed occupations (they attribute it to slowed hiring, not separations) — here corroborated on a different dataset, with caveats (non-employed young workers may stay in school, switch jobs, or exit the labor force rather than appear unemployed).

## Methodological stance (worth importing into the wiki)

- **Humility about forecasting.** Past approaches over-predicted: offshorability flagged ~¼ of US jobs as vulnerable, most of which kept healthy growth; government occupational forecasts "added little predictive value beyond linear extrapolation." The paper's aim is to **establish a measure now, before effects emerge, and revisit periodically** — so future analyses separate signal from noise rather than rationalising post-hoc.
- **AI is more like the internet / China-trade than COVID.** Effects are likely gradual and confounded by the business cycle and trade policy — "most useful when the effects are ambiguous," not when they're unmistakable.
- **Unemployment chosen as the priority outcome** (over job-postings or occupation-mix shifts à la Gimbel et al.) because it most directly captures *harm*: a decline in postings for one exposed role may be offset by openings in a related one, but an unemployed worker wants a job and hasn't found one.

## What was actually ingested

The full 17-page PDF (the "Nowcasting" working version, v16, of the published note). Figures (1–7) were read from their captions and the surrounding text, not reproduced. The companion dataset (observed coverage at task and job level) is published at `huggingface.co/datasets/Anthropic/EconomicIndex`.

## Why this matters to the wiki

This is the **primary methodology** the wiki's labor-effects claims have leaned on through secondary citation (the AWS keynotes, the `observed exposure` framing on [[ai-employment-effects]]). Ingesting it: (a) gives the *no-unemployment-yet / young-hiring-slowdown* finding a citable primary; (b) supplies the **automated-vs-augmentative weighting** as a measurement principle that sharpens [[automation-vs-augmentation]] (exposure ≠ displacement risk; the weighting is the difference); (c) anchors the *"capability ≫ adoption"* gap (β=1 tasks = 68% of usage, yet most automatable work isn't automated) that complements [[2025-10-05-patwardhan-et-al-openai-gdpval|GDPval]]'s capability-as-leading-indicator framing from the *usage* side.

## Linked entities and concepts

- Publisher: [[Anthropic]]; program: [[Anthropic Economic Index]].
- **Promoted to entities this ingest** (second-source rule — both also lead-author the [[2026-05-07-anthropic-economic-index-5-learning-curves|5th AEI report]]): [[Maxim Massenkoff]] (Naval Postgraduate School), [[Peter McCrory]] (Anthropic). Named peers/discussants (Gimbel, Brynjolfsson, Acemoglu, Hampole, Autor, Gans & Goldfarb) are body citations, out of scope for promotion.
- Concepts: [[ai-employment-effects]], [[automation-vs-augmentation]].

## Relationships

- *published-by* [[Anthropic]]; *part-of* [[Anthropic Economic Index]].
- *supports* [[2026-04-28-anthropic-economic-index-q4-2025]] — the AEI usage data is this report's usage input.
- *supports* [[2026-04-28-brynjolfsson-canaries-coal-mine]] — independent corroboration of the young-worker hiring slowdown.
- Presented on stage by [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Brovich / AWS Sydney]] (the "Anthropic March study").
