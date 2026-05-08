---
type: source
kind: report
title: "The Anthropic Economic Index report: Learning curves"
author: ["Maxim Massenkoff", "Eva Lyubich", "Peter McCrory", "Ruth Appel", "Ryan Heller"]
publisher: "Anthropic"
journal_volume: "Anthropic Economic Index, 5th report, 24 March 2026"
url: "https://www.anthropic.com/research/economic-index-march-2026-report"
date_published: 2026-03-24
date_ingested: 2026-05-07
tags: [anthropic-economic-index, claude, automation-vs-augmentation, ai-employment-effects, learning-curves, skill-biased-technological-change, model-selection, tenure, longitudinal]
length: "~20 pages, full ingest"
raw: "../../raw/reports/Economic-Index-5-v2 (1).pdf"
---

# Anthropic Economic Index report 5 — Learning curves (March 2026)

## TL;DR

The **5th [[Anthropic Economic Index]] report**, *Learning curves* (24 March 2026, lead authors Maxim Massenkoff, Eva Lyubich, Peter McCrory + Ruth Appel and Ryan Heller). Direct continuation of the [[2026-04-28-anthropic-economic-index-q4-2025|4th-report's]] "economic primitives" methodology with a fresh sample window (Feb 5–12, 2026), three months after the Claude Opus 4.5 release and coincident with the Claude Opus 4.6 release.

**This is enrichment, not supersession.** The 4th-report page stays canonical for its specific Nov 2025 numbers; this 5th-report page is the latest reading. Several primitives have shifted statistically significantly between the two reports — those longitudinal deltas are the report's empirical anchor.

The report has two chapters:
1. **What's changed** — diversification of Claude.ai use cases, persistence of geographic inequality, two new automation patterns on the API.
2. **Learning curves** — the load-bearing chapter. Two findings: **model selection matches task value**, and **high-tenure users have systematically higher success rates** (after controls). Discusses three explanations (learning-by-doing, cohort effects, survivorship bias) and connects to **skill-biased technological change**.

## Methodology continuity

Sample period **Feb 5–12, 2026**; 1M conversations from Claude.ai (consumer) + 1M from 1P API (developer-facing). Same privacy-preserving classification system as the 4th report. Same five interaction types (directive / feedback loop / task iteration / validation / learning) and same automation/augmentation grouping. **Methodological caveat (footnote 2 of the report):** these results use 2019 O*NET-SOC codes; previous reports used 2010 vintage. Year-over-year code drift is a real issue — adoption-share comparisons should be read with that grain.

## Chapter 1: What's changed since November 2025

### Use-case diversification on Claude.ai

Top 10 O*NET tasks went from 24% of conversations (Nov 2025) to **19%** (Feb 2026) — Claude.ai usage diversified. Coding tasks have continued to migrate from Claude.ai to the 1P API, where **Claude Code's agentic architecture splits coding work into smaller API calls** — labeled as distinct tasks. So while coding's overall share of API traffic has grown, it spreads across many task categories rather than concentrating in a few. Top 10 task share on the 1P API: 28% (Aug 2025) → 32% (Nov 2025) → **33%** (Feb 2026) — concentrating, while Claude.ai diversifies.

**Claude.ai use-case composition:**
| Category | Nov 2025 | Feb 2026 | Δ |
| --- | ---:| ---:| ---:|
| Work | 46% | 45% | -1 pp |
| Personal | 35% | **42%** | +7 pp |
| Coursework | 19% | 12% | -7 pp |

Coursework drop has two drivers per the report: (a) academic-calendar effects (winter break in countries where most students were on break — drop was 12 pp there vs 5 pp in active-school-term countries) and (b) **the sample period overlapped with Anthropic's Super Bowl ads release**, which brought first-time users skewing personal/non-coursework.

### Augmentation persists; automation increasingly concentrated on API

| Platform | Nov 2025 | Feb 2026 |
| --- | --- | --- |
| Claude.ai augmentation | 52% | **53%** (+1 pp) |
| Claude.ai automation | 45% | **44%** (-1 pp) |
| 1P API automation | (decreased sharply per Appendix Fig A.3) | |

Three of the four samples (Jan 2025 / Mar 2025 / Aug 2025 / Nov 2025 / Feb 2026) now show augmentation > automation on Claude.ai; the August 2025 sample remains the only inversion. **Appendix:** the 1P API has been the surface where automation patterns concentrate, particularly two emergent flows that **at least doubled in share** between Nov 2025 and Feb 2026:
- **Business sales & outreach automation** — sales enablement generation, B2B lead qualification research, customer data enrichment, cold-email drafting.
- **Automated trading & market ops** — monitor markets/positions, propose specific investments, inform traders of market conditions, related tasks.

### Average task value declined slightly on Claude.ai, rose on API

Volume-weighted mean wage (in Feb 2026 USD/hour) for tasks performed:
| Sample | Claude.ai | 1P API |
| --- | ---:| ---:|
| Jan 2025 | $49.30 | — |
| Aug 2025 | $48.90 | $50.50 |
| Nov 2025 | $48.30 | $50.40 |
| Feb 2026 | **$47.90** | **$50.70** |
| US avg. hourly wage (reference) | $37.30 | $37.30 |

Claude.ai task value drift is "mostly due to an increase in simple factual questions (sports outcomes, weather)" plus coding migrating to API. The API trajectory remains above the US average, indicative of the 1P API's specialized-developer concentration.

### Inequality in global usage persists

Anthropic Usage Index (AUI; usage adjusted by working-age population):
- **Within US:** convergence continued — top-5 states' share of per-person usage dropped 30% → **24%** since Aug 2025; Gini fell from 0.37 → 0.31 → **0.29**. Pace has slowed; convergence to roughly equal usage per capita extrapolated to **5–9 years** (vs 2–5 yrs in the prior report).
- **Across countries:** *concentration* — top 20 countries went from 45% → **48%** of per-capita usage; Gini rose 0.46 → **0.50**. Lower-income countries continue to fall behind.

### Primitives shifts (Nov 2025 → Feb 2026)

| Primitive | Nov 2025 | Feb 2026 | Δ | p |
| --- | ---:| ---:| ---:| ---:|
| Human education (years) | 12.21 | 11.92 | **-0.29** | <0.001 |
| AI autonomy (1–5) | 3.38 | 3.41 | +0.02 | <0.001 |
| Human time (min) | 185.53 | 183.77 | -1.76 | <0.001 |
| Human + AI time (min) | 15.35 | 14.30 | -1.05 | <0.001 |
| "Human can't do alone" (%) | 12.09 | 12.24 | +0.15 | <0.05 |

Education years dropping with simultaneous slight rise in "Human can't do alone" suggests the broader (more casual) user base is bringing simpler tasks on average, but a marginally larger fraction of tasks are still beyond what humans could do unaided. The two trends are not contradictory; they are different ends of the task-difficulty distribution.

## Chapter 2: Learning curves

### Model selection matches task value

The Claude family (Haiku, Sonnet, Opus) offers a cost/speed/performance tradeoff. **Users select Opus differentially across tasks** in a way that tracks task economic value:

| Occupation group | Opus over/under-representation (paid Claude.ai) |
| --- | ---:|
| Computer & Mathematical | **+4.4 pp** |
| Business & financial operations | +2.3 pp |
| Management | +1.9 pp |
| Life, physical, social science | +0.9 pp |
| Office and admin support | -0.6 pp |
| Sales | -1.6 pp |
| Arts, design, entertainment, sports, media | -5.7 pp |
| Educational instruction & library | **-6.5 pp** |

**Slopes** (Opus share regressed on occupation hourly wage):
- Claude.ai: **+1.48 pp Opus per +$10/hour** task value
- 1P API: **+2.79 pp per +$10** — about twice as steep

API users — running programmatic workflows — have stronger reason to switch models task-by-task. Web-app users mostly stay on the default Sonnet unless task complexity demands Opus.

### High-tenure users have systematically higher success rates

The **load-bearing finding of the report.** "High tenure" = signed up ≥6 months ago; "low tenure" = everyone else.

**Differences in transcript characteristics:**
| Metric | Low tenure | High tenure | Δ |
| --- | ---:| ---:| ---:|
| Directive collaboration mode | 38.1% | 29.4% | **-8.7 pp** |
| Feedback loop | 11.7% | 12.1% | +0.5 pp |
| Task iteration | 24.5% | 28.2% | +3.6 pp |
| Validation | 4.4% | 5.6% | +1.3 pp |
| Learning | 21.3% | 24.7% | +3.4 pp |
| Work use case | 41.6% | 48.9% | **+7.3 pp** |
| Personal use case | 44.3% | 40.3% | -4.0 pp |
| Coursework use case | 14.1% | 10.8% | -3.3 pp |
| **Task success rate** | 66.7% | **73.1%** | **+6.4 pp** |
| Top 10 tasks share | 22.2% | 20.7% | -1.6 pp |
| AI autonomy (1–5) | 3.42 | 3.40 | -0.6% |
| Human education (yr) | 11.5 | 12.3 | **+6.6%** |
| AI education (yr) | 11.7 | 12.4 | +6.0% |

High-tenure users **iterate more, delegate less, work-use more, and succeed more**. They bring higher-education-content tasks. Their conversational success rate is ~5–6 pp higher.

### The tenure-success regression — controlled

To rule out simple explanations (long-tenure users bringing easier tasks), the team regressed binary success on a high-tenure indicator with progressive controls:

| Specification | Effect on success (pp) | 95% CI |
| --- | ---:| ---|
| (1) Raw | **+5 pp** | tight |
| (2) + task fixed effects (O*NET task + request cluster) | **+3 pp** | tight |
| (3) + full controls (model, use case, country FE) | **+4 pp** | tight |

The within-task comparison (specification 2) is the most informative — it compares high- and low-tenure users *within the same narrowly-defined task* (e.g., "Perform corporate financial analysis, valuation, and modeling for specific companies"). Effect attenuates from +5 pp to +3 pp under task FE, but **persists**. With full controls (specification 3) the effect is ~4 pp.

**Discussion (the report's framing):**

> "These results suggest that high-tenure users have more success in their Claude conversations, and that this is not due to simple factors like language or the task being performed. One intriguing potential explanation is that these users have better learned to extract what they want from AI."

### Learning-by-doing vs cohort effects vs survivorship bias

The report explicitly flags three competing explanations:
1. **Learning-by-doing.** Experience yields skill at extracting value from AI. Consistent with the within-task effect persisting.
2. **Cohort effects.** Early adopters were more technical / sophisticated. Stable user characteristics, not learned skill.
3. **Survivorship bias.** Less-successful users churned; we observe only the survivors. The team can't rule this out: "people who signed up a year ago but are no longer using Claude" are absent from the data.

The full controls in specification (3) push back against (2), but cohort and survivorship bias remain partial confounds.

### The labor-market frame: skill-biased technological change

The report's most consequential framing in the discussion:

> "Economists have long noted the potential for skill-biased technological change: innovations that raise wages for high-skill workers while depressing them for others. Our analysis in this report identifies a channel through which such skill-biased transformation may already be unfolding: early adopters with high-skill tasks have more successful interactions with Claude than later, less technical adopters. These early-adopting users may simultaneously be the most exposed to AI-driven disruption and most aided by AI in these initial, augmentative waves of adoption."

This is the report's contribution to the [[ai-employment-effects]] cluster: even within an augmentative deployment regime ([[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond]]'s equalising-effect findings notwithstanding), the **adoption curve itself is unequal** — high-skill early adopters extract more value. The augmentative wave can be skill-biased even when its task-level productivity effect is equalising.

## Cross-source positioning

This 5th-report is the wiki's first **longitudinal Anthropic Economic Index data point** since the 4th-report ingest. Methodology continuity makes the Nov→Feb deltas the report's most reliable signal.

- **Reinforces [[automation-vs-augmentation]].** Augmentation lead persists on Claude.ai (52→53%); automation increasingly *concentrated on API* not absent from the platform overall. Useful for the wiki's longstanding cross-source convergence claim.
- **Updates [[ai-employment-effects]].** Tenure-success effect adds a new mechanism for skill-biased disparity — distinct from Brynjolfsson Canaries' early-career employment decline (a *displacement* mechanism) and from Brynjolfsson, Li & Raymond's customer-support equalising effect (a *productivity* mechanism). Tenure-success is an *adoption-curve* mechanism: those who learned to use the tool earliest extract more value over time.
- **Updates [[ai-deskilling]] and [[durable-skills]].** The "learning-by-doing" framing is the practitioner counterpart to durable-skills *measurement*: this report measures whether people actually do learn-by-doing in the wild (yes, with confounds). If so, AI fluency itself becomes a [[durable-skills|durable skill]] — and the [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al.]] critical-thinking rubric's "AI-Supported Exploration / Verification" sub-skills become more theoretically grounded.
- **Reinforces [[ai-agents]].** Coding tasks migrating from Claude.ai to API and splitting into many distinct task labels is the empirical signature of agent-mediated work. The report attributes this directly to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Claude Code's agentic architecture]] — connecting the Economic Index data to Anthropic's engineering design.
- **Updates [[Anthropic Economic Index]] entity.** This is the 5th report; the entity page will be updated to reflect the new sample.
- **Adds Claude Opus 4.5 / 4.6 references** to [[foundation-models]].

## Source-quality flag

- **Type:** Anthropic Economic Index report (5th in the series) — Anthropic Research publication, not a peer-reviewed journal article. Established methodology family with prior wiki ingest.
- **Empirical rigor:** large-N (1M Claude.ai conversations + 1M 1P API), longitudinal (5 sample periods now), pre-registered methodology family. Reports p-values, fixed-effect regressions, controls.
- **Confidence boost:** +0.05 per the [§Lifecycle](../../CLAUDE.md#lifecycle) "additional supporting source" rule. The "large-N empirical study" bonus already counted once via the 4th-report; not double-counted here.
- **Vendor-of-deployment caveat:** Anthropic's commercial interest in narratives showing *augmentation lead*, *learning-by-doing*, and *Opus higher-value-task selection* is real. The report is methodology-honest (acknowledges survivorship bias, cohort effects, methodological discontinuities like the O*NET vintage shift). Read with that vantage in mind.

## Limitations the report acknowledges

- **Survivorship bias** in the tenure-success analysis — un-resolvable with current data.
- **O*NET vintage shift** between reports introduces some adoption-share drift unrelated to actual usage change.
- **Sample-period contingencies** — Super Bowl ads brought first-time users; winter break suppressed coursework. Both pull the Feb 2026 numbers in specific directions.
- **Privacy thresholds** required log-level data with privacy thresholds for the controlled regressions; not all primitives available at full granularity.

## Linked entities and concepts

**Entities (this wiki):** [[Anthropic Economic Index]] (this is the 5th report; bumps `source_count`), [[Anthropic]] (publisher; bumps `source_count`), [[Jack Clark]] (named in the acknowledgements — promoted on cross-page presence: the [[Anthropic]] page lists him as co-founder and the [[AI Index]] page lists him as a Steering Committee member). **Dangling** (single-source, deferred): Maxim Massenkoff, Eva Lyubich, Peter McCrory (lead authors), Ruth Appel, Ryan Heller (authors).

**Concepts:** [[automation-vs-augmentation]] (heavy enrichment — longitudinal Nov→Feb data), [[ai-employment-effects]] (heavy — tenure-success effect; skill-biased technological change framing), [[ai-deskilling]] / [[durable-skills]] (light — learning-by-doing mechanism), [[ai-agents]] (light — Claude Code agentic architecture as empirical signature), [[generative-ai]] / [[foundation-models]] (light — Claude Opus 4.5/4.6), [[enterprise-ai-adoption]] (light — coding workflow migration to API).

**Threads/syntheses:** [[ai-maturity-measurement-comparison]] (still open) — Anthropic Economic Index methodology adds another measurement instrument to the cluster.

## Source

- **Raw PDF (~20 pages, full ingest):** [report file](../../raw/reports/Economic-Index-5-v2%20%281%29.pdf)
- **Publisher:** Anthropic
- **Date:** March 24, 2026
- **Sample period:** February 5–12, 2026 (~1M Claude.ai conversations + ~1M 1P API)
- **Lead authors:** Maxim Massenkoff, Eva Lyubich, Peter McCrory
- **Other authors:** Ruth Appel, Ryan Heller
- **Citation key:** `massenkoff2026learning`
- **Data:** [https://huggingface.co/datasets/Anthropic/EconomicIndex](https://huggingface.co/datasets/Anthropic/EconomicIndex)
