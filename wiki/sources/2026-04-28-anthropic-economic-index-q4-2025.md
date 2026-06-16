---
type: source
kind: article
title: "Anthropic Economic Index: New building blocks for understanding AI use"
author: ["Anthropic"]
publisher: "Anthropic (Economic Research blog)"
url: "https://www.anthropic.com/research/anthropic-economic-index-new-building-blocks-for-understanding-ai-use"
parent_report: "Anthropic Economic Index, fourth report (Jan 2026)"
date_published: 2026-01-15
date_ingested: 2026-04-28
tags: [anthropic-economic-index, claude, productivity, automation, augmentation, deskilling, occupations, task-complexity, METR, economic-primitives]
length: "~14 pages (summary blog post; full report linked separately, not separately ingested)"
raw: "../../raw/articles/The Anthropic Economic Index report_ New building blocks for understanding AI use _ Anthropic.pdf"
---

# Anthropic Economic Index — New Building Blocks for Understanding AI Use

## TL;DR

The fourth report in [[Anthropic]]'s [[Anthropic Economic Index]] series. Introduces **economic primitives** — five measurements derived from privacy-preserving classification of ~1M [[Claude]].ai conversations and ~1M 1P API transcripts (sample period: November 2025, predominantly [[Claude Sonnet 4.5]]):

1. **Task complexity** — estimated human time without AI; whether multiple tasks are handled in one conversation
2. **Human and AI skill level** — years of education needed to understand prompts and responses
3. **Use case** — work / education / personal
4. **AI autonomy** — degree of delegation, from collaboration to fully directive
5. **Task success** — Claude's own assessment of completion

This page summarizes the **summary article** dated 15 Jan 2026; the full underlying report is referenced but not separately ingested.

## Key claims

### Tasks

**Speedup scales with task complexity** (Claude.ai sample):

- Tasks requiring high-school education (12 years): **~9× speedup**
- Tasks requiring a college degree (16 years): **~12× speedup**
- API speedups are larger still

**Success rate is slightly lower at higher complexity**:

- Tasks needing less than high school: **70%** Claude success
- Tasks needing a college degree: **66%** Claude success

> "Claude's impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate."

> "AI's productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the evidence that white collar professionals are more likely to use AI at work."

### Time horizons (METR comparison)

The report situates its findings against [[METR]]'s task-horizon benchmark for [[Claude Sonnet 4.5]]:

| Source | Duration at which 50% success is achieved |
|---|---|
| METR (fixed-task benchmark) | ~2 hours |
| Anthropic 1P API | ~3.5 hours |
| Anthropic Claude.ai | ~19 hours |

The Claude.ai number is much higher because of two methodological differences explicitly noted in the report:

- **Selection bias** — users bring tasks to Claude that they expect Claude to succeed on.
- **Task decomposition with feedback loops** — users break complex tasks into smaller steps, with Claude correcting course mid-conversation.

### Country-level use

- **Higher GDP-per-capita countries**: Claude is used more for *work* and *personal* use.
- **Lower GDP-per-capita countries**: more *educational coursework* use.
- The report describes this as an "adoption curve": education-heavy in low-income, diversifying toward work and personal as income rises.
- Cited as consistent with comparable Microsoft analysis.
- Anthropic's Rwanda partnership with ALX is framed as a literacy-to-general-use transition program (year-long Claude Pro grants for graduates).

### Occupations — coverage and effective coverage

**Pooled task coverage**:

- January 2025 first report: **36%** of jobs saw Claude used for ≥25% of their tasks.
- Pooled across reports through Nov 2025: **49%**.

**Effective AI coverage** (a new occupation-level metric introduced in this report):

- Defined as the share of a worker's *time-weighted duties* that Claude could *successfully* perform.
- Outliers where effective coverage *exceeds* task coverage: data entry keyers, radiologists, medical transcriptionists.
- Outliers where effective coverage is *below* task coverage: teachers, software developers.

**Task-content / education skew**:

- Claude-covered tasks average **14.4 years** of predicted education (≈ U.S. associate's degree).
- All tasks economy-wide (employment-weighted) average **13.2 years**.

### Aggregate productivity

- Earlier Anthropic estimate (carried over from prior reports): widespread AI adoption could add **+1.8 percentage points** to U.S. labor productivity growth per year over a decade.
- **Reliability-adjusted estimate** (factoring in task-level success rates):
  - **+1.2 pp/yr** when measured on Claude.ai
  - **+1.0 pp/yr** when measured on the 1P API (more challenging task mix)
- Even +1 pp/yr would return U.S. productivity growth to late-1990s / early-2000s rates.

### Updates on previous measures

**Task concentration is rising**:

- Top 10 work tasks on Claude.ai now account for **24%** of all conversations, up from **21%** in January 2025.
- Computer and mathematical tasks ≈ ⅓ of Claude.ai conversations and ≈ ½ of API traffic.

**Augmentation / automation split** on Claude.ai over time:

| Sample period | Augmentation | Automation |
|---|---|---|
| January 2025 | 55% | 41% |
| March 2025 | 55% | 42% |
| August 2025 | 47% | 49% |
| **November 2025** | **52%** | **45%** |

The August 2025 sample was the only one where automation led; the November 2025 sample reverses to augmentation-led.

**Geography**: top countries (US, India, Japan, UK, South Korea) still lead overall Claude.ai use, with adoption well-explained by GDP per capita. Within the US, distribution across states has become noticeably more even — the report's model implies state-level equalization within 2–5 years if the trend holds.

## Methodology notes

- **Privacy-preserving classification** — Claude itself answers a fixed set of questions about each conversation in the sample. Full methodology in chapter 2 of the underlying report (not separately ingested here).
- **Sample size** — 1M Claude.ai Free / Pro / Max conversations + 1M 1P API transcripts.
- **Sample period** — November 2025.
- **Predominant model** — [[Claude Sonnet 4.5]]. The report acknowledges the subsequent release of [[Claude Opus 4.5]] may shift future numbers.
- **Task taxonomy** — O*NET.

## Limitations / caveats (per report)

- Coverage analysis is restricted to tasks performed on Claude.ai — does not capture other LLM platforms, internal tooling, or non-LLM AI.
- The deskilling analysis is a *first-order* effect; the report explicitly does not predict labor-market dynamics will let it materialize unchecked.
- The Claude.ai task-horizon number embeds selection bias and task decomposition.
- The report is observational, not causal.

## Deskilling — task-composition shift

A specific finding: removing all Claude-covered tasks from current jobs would, as a first-order effect, **deskill jobs on average** — because Claude-covered tasks skew toward higher-education content. Most-affected professions named: technical writers, travel agents, teachers. Real-estate managers move in the opposite direction. The report frames the analysis as a useful first-order signal, not a labor-market forecast.

> "We're not necessarily predicting that this deskilling will occur: it's possible that even if AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn't account for."

See [[ai-deskilling]] for the wiki concept page.

## Quotes worth saving

> "AI's productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the evidence that white collar professionals are more likely to use AI at work."

> "Claude's impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate."

> "Our analysis shows how Claude's *effective* time horizons might look different to those found in a study with a consistent set of tasks."

> "We expect [tasks] might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable — and if this happens, it'll give us another possible indication of coming economic impacts."

## Related in this wiki

- [[Anthropic Economic Index]] — the parent measurement initiative
- [[Anthropic]] — publisher
- [[METR]] — task-horizon benchmark referenced
- [[automation-vs-augmentation]] — the augmentation / automation split is updated quarterly in this series
- [[ai-employment-effects]] — aggregate productivity, effective AI coverage, task-composition findings sit here
- [[ai-deskilling]] — task-composition shift within retained jobs
- [[generative-ai]] — economic-primitives framework adds five measurements to the wiki's measurement vocabulary
- [[ai-benchmarks]] — METR's task-horizon measure compared
- [[2026-04-28-brynjolfsson-canaries-coal-mine]] — earlier paper that uses Anthropic Economic Index automation/augmentation classification at the occupation level
- [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work]] — within-occupation customer-support productivity study; this report measures across-task productivity at the population level
- [[2026-04-28-ai-index-report-2025]] — Stanford HAI's annual measurement initiative; parallel in role
