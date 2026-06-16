---
type: source
kind: paper
title: "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence"
author: ["Erik Brynjolfsson", "Bharat Chandar", "Ruyu Chen"]
publisher: "[[Stanford Digital Economy Lab]]"
working_paper: true
url: "https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/"
raw: "../../raw/papers/Brynjolfsson et al. - Canaries in the Coal Mine Six Facts about the Recent Employment Effects of Artificial Intelligence.pdf"
date_published: 2025-08-26
date_ingested: 2026-04-28
tags: [employment, labor-market, automation, augmentation, generative-ai, brynjolfsson, stanford-digital-economy-lab, working-paper, ADP-payroll-data]
length: "20 pages read; 25+ pages total"
---

# Brynjolfsson, Chandar & Chen — Canaries in the Coal Mine?

## TL;DR

Stanford Digital Economy Lab working paper using **ADP payroll data** (the largest U.S. payroll provider, 25M+ workers, monthly Jan 2021–July 2025) to test whether GenAI is yet displacing human labor. Six empirical facts, headlined by: **early-career workers (ages 22–25) in the most AI-exposed occupations have experienced a ~13% relative decline in employment** since late 2022, while older workers in the same occupations and workers in less-exposed occupations have continued to grow. Adjustments are concentrated in **employment, not wages**, and in **automation uses, not augmentation uses**. Consistent with the hypothesis that the AI revolution is beginning to have a significant and disproportionate impact on entry-level workers in the American labor market — though authors caveat that other factors may be in play.

## Key claims

### Data and method

- **ADP payroll data** — the largest payroll firm in the U.S.; the company provides payroll for firms employing **25M+ workers**.
- Monthly individual-level records, **January 2021 through July 2025**.
- Main analysis sample: 3.5–5M workers per month, ages 18–70, full-time, with consistent firm sample (firms with employee earnings records every month from Jan 2021 onward).
- 7,000+ standardized job titles → 2010 SOC codes → AI-exposure metrics.
- Two AI-exposure measures:
  - **Eloundou et al. (2024)** GPT-4 β estimate (occupational task susceptibility to GPT-4)
  - **Anthropic Economic Index** (Handa et al. 2025) — derived from a sample of millions of conversations with Claude, with each task classified as "automative," "augmentative," or neither.

### Fact 1: Employment for young workers has declined in AI-exposed occupations

- **Software developers ages 22–25**: employment declined nearly **20%** from peak in late 2022 to July 2025.
- **Customer service agents ages 22–25**: similar pattern.
- Older workers (35–49) in the same occupations: stable or growing.
- Less-exposed occupations (e.g., **stock clerks, health aides**): no age divergence pattern. Health aides ages 22–25 actually growing *faster* than older workers.

### Fact 2: Overall employment continues to grow, but young-worker employment has stagnated since late 2022

- **22–25 year-olds in highest exposure quintiles**: -6% from late 2022 to July 2025.
- **35–49 year-olds in same**: +6% to +9%.
- 22–25 year-olds in lower exposure quintiles: +6% to +13% (no clear ordering by exposure).
- Implication: declining employment in AI-exposed jobs is driving tepid overall employment growth for 22–25 year-olds, while employment for older workers continues to grow.

### Fact 3: Entry-level employment has declined in *automation* applications of AI, not *augmentation*

This is the conceptually most important fact. Using the Anthropic Economic Index automation/augmentation classification:

- Occupations with **highest automation share**: declining employment for youngest workers.
- Occupations with **highest augmentation share**: **NO** similar pattern. Employment changes for young workers are not ordered by augmentation exposure; the fifth (most-augmentative) quintile even shows fastest employment growth.
- "Consistent with automative uses of AI substituting for labor while augmentative uses do not."

This directly maps to [[automation-vs-augmentation]] as a conceptual distinction and to the [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] 2×2: the **"no regrets zone"** is exactly the automation quadrant where AI does it all without humans in the loop.

### Fact 4: Employment declines remain after conditioning on firm-time effects

- Poisson event study regression with firm-time and firm-quintile fixed effects.
- For workers 22–25: **12 log-point decline** in relative employment for highest AI-exposure quintiles vs. lowest. Statistically significant.
- Estimates for other age groups: smaller, not statistically significant.
- Implication: trends are *not* driven by differential firm-level shocks (interest rate changes, industry-specific contractions, sectoral hiring cycles).

### Fact 5: Adjustments visible in employment more than compensation

- Little difference in annual salary trends by age or exposure quintile.
- "AI may have larger effects on employment than on wages, at least initially."
- Suggests **wage stickiness** — labor market adjusts via headcount before pay.

### Fact 6: Robust to alternative samples and explanations

- Results hold when excluding **computer-occupation firms** (so it's not just tech-sector contraction).
- Results hold when excluding **occupations amenable to remote work / outsourcing**.
- AI exposure taxonomy did not predict employment outcomes for young workers in **earlier periods** (before late 2022), including during the COVID-19 unemployment spike — so it's not a generic "young workers struggle in downturns" effect.
- Patterns "appear most acutely starting in late 2022, around the time of rapid proliferation of generative AI tools" (footnote: ChatGPT introduced Nov 2022).
- For non-college workers, experience may serve as less of a buffer — low-college-share occupations exhibit divergent outcomes by AI exposure up to age 40.

## Theoretical mechanism (introduction)

> "AI replaces codified knowledge — the 'book-learning' that forms the core of formal education. AI may be less capable of replacing tacit knowledge, the idiosyncratic tips and tricks that accumulate with experience. As young workers supply relatively more codified knowledge than tacit knowledge, they may face greater task replacement from AI in exposed occupations, leading to greater employment reallocation."

Cites [[Daron Acemoglu|Acemoglu]] & [[David Autor|Autor]] (2011) for the canonical task-replacement framework. The codified-vs-tacit distinction echoes [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's]] explicit-vs-tacit knowledge axis in their 2×2 framework — strong cross-source convergence on the same conceptual cut.

Footnote (worth quoting): *"Ironically, one of the practical skills more likely to be learned on the job than in university computer science classes may be how to use AI software development."*

## Notable quotes

> "Since the widespread adoption of generative AI, early-career workers (ages 22-25) in the most AI-exposed occupations have experienced a 13 percent relative decline in employment even after controlling for firm-level shocks."

> "Employment declines are concentrated in occupations where AI is more likely to *automate*, rather than *augment*, human labor."

> "We caution that the facts we document may in part be influenced by factors other than generative AI, but our results are consistent with the hypothesis that generative AI has begun to affect entry-level employment."

> "AI may have larger effects on employment than on wages, at least initially."

## Cross-source comparison: contradictions and convergences

### Tension with [[2026-04-28-ai-index-report-2025|AI Index 2025]]'s "equalizing effect" framing

[[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4 cites multiple studies (Brynjolfsson 2023 customer support, Dell'Acqua 2023 consulting, Cui 2024 software, Hoffman 2024 software) showing AI's **equalizing effect**: low-skill workers gain more productivity than high-skill ones. The typical reading: "AI helps low-skill workers most → equalizing → good for entry-level."

This 2025 paper complicates that reading. Two findings can both be true:

1. **At the worker level, conditional on having the job**: AI raises productivity of low-skill / early-career workers more than high-skill / experienced ones (the equalizing effect).
2. **At the labor-market level**: AI is reducing employment for early-career workers in the most automate-able occupations (this paper's headline).

The **mechanism reconciling them**: when AI makes individual workers in a role more productive, the firm needs fewer workers in that role to deliver the same output. Whether headcount goes up or down depends on **demand elasticity** — the paper's footnote 3 makes exactly this point.

This is a **subtle but important enrichment** — the equalizing effect at task level does not imply pro-employment outcomes at occupation level. Captured in [[ai-employment-effects]].

### Strong convergence with [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]]'s 2×2

The Brynjolfsson paper's **automation vs. augmentation** distinction (Fact 3) is empirically the same cut as Anand-Wu's "no regrets zone" (low cost of errors / explicit data — AI does it all) vs. their other three quadrants (where humans remain in the loop). Two independent literatures arriving at the same conceptual distinction is strong evidence the cut is real.

### Convergence with [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]] workforce expectations

[[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]'s McKinsey survey reported 43% of orgs expecting workforce decreases. The Brynjolfsson paper provides the empirical correlate: those workforce decreases are showing up in the data, but **disproportionately at the entry level**, not uniformly across all roles.

### Cross-reference: [[Capital One]]'s Capability Era

The Brynjolfsson finding that **entry-level employment is declining specifically in automate-able occupations** is the empirical correlate of [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's]] historical pattern: "in the not-too-distant future your fiercest competition may not be your familiar peers but a new breed of solo entrepreneurs and micro-teams" — the AI-first entrant story is now visible in entry-level employment data.

## My take

This is the most consequential empirical AI paper I've ingested so far. It moves the labor-market debate from "will AI affect jobs?" to "AI is affecting jobs *now*, and here's the detailed pattern." The pattern is **stark**:

- The decline is specific to **young workers** (22–25), not all workers.
- Specific to **AI-exposed** occupations, not all occupations.
- Specific to **automation** uses, not augmentation uses.
- Visible in **employment, not wages** (wage stickiness).

The methodological strengths are unusual: ADP's data captures ~25M workers in near real-time, which is a different scale and timeliness than CPS-based academic studies that have driven prior debate. The 2010 SOC mapping + Eloundou et al. exposure metric + Anthropic Economic Index for automation/augmentation classification is methodologically sophisticated.

**The single most useful reframing for the wiki: automation vs. augmentation is not just a strategic choice (Anand-Wu) — it's a labor market reality with measurable headcount consequences (Brynjolfsson).** Concept page [[automation-vs-augmentation]] now links these two lenses.

Caveats worth carrying forward:
- ADP's firm distribution doesn't perfectly match the U.S. economy (somewhat overrepresents Northeast and manufacturing/services).
- Working paper, not yet peer-reviewed (Aug 2025).
- The "13% decline" is **relative**, not absolute — it's derived from relative employment trends across age × exposure quintiles. The absolute employment decline for 22–25 year-olds in highest-exposure occupations is ~6% from late 2022 to July 2025; the 13% number controls for firm-level shocks.
- Cannot rule out non-AI confounds entirely (the authors are explicit about this).

The "Canaries in the Coal Mine" framing is well-chosen: this isn't a definitive verdict on AI's labor effects; it's a credible early signal in the most-exposed corner of the workforce. Worth tracking as a *time series* — the authors say they intend to continue updating.

For the wiki, this paper:
- Promotes [[Erik Brynjolfsson]] from dangling wikilink to substantive entity page.
- Justifies new concept page [[ai-employment-effects]].
- Justifies new concept page [[automation-vs-augmentation]] as an analytical framework distinct from "where to use AI" and "how to deploy AI."
- Adds a third strand to [[ai-maturity-measurement-comparison]] (alongside maturity stages and readiness measures, now there's *labor-market consequences* as a measurable AI-impact dimension).

## Linked entities and concepts

**Entities (this wiki):** [[Erik Brynjolfsson]] (promoted from dangling), [[Stanford Digital Economy Lab]] (new). **Dangling:** [[Bharat Chandar]], [[Ruyu Chen]] (co-authors, deferred), [[ADP]] (data provider), [[Daron Acemoglu]], [[David Autor]] (cited theory), [[Joshua Gans]], [[Nick Bloom]], [[Daniel Rock]], [[Fei-Fei Li]], [[Sarah Bana]], [[Cody Cook]], [[Phil Trammell]] (acknowledged).

**Concepts (new):** [[ai-employment-effects]] (created by this ingest), [[automation-vs-augmentation]] (created by this ingest as a distinct conceptual framework).

**Concepts (enriched):** [[enterprise-ai-adoption]] (the "78% adoption / 1% maturity / equalizing-effect / declining-entry-level-employment" combined picture); [[responsible-ai]] (labor-market disruption as an RAI concern); [[generative-ai]] (the automation/augmentation distinction in deployment); [[ai-agents]] (agents are concentrated in the automation quadrant where employment is declining).

**Threads (enriched):** [[ai-maturity-measurement-comparison]] (adds employment effects as a third measurement dimension alongside maturity and readiness).

**Cross-source citations:** [[2026-04-28-ai-index-report-2025|AI Index 2025]] (cited explicitly for SWE-bench data and is the home of the "equalizing effect" productivity studies); [[2026-04-28-anand-wu-genai-playbook|Anand-Wu HBR]] (strong conceptual convergence on automation vs. augmentation); [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]] (workforce expectations align with this paper's empirical results).

## Source

- **Raw PDF (~25+ pp):** [paper file](../../raw/papers/Brynjolfsson%20et%20al.%20-%20Canaries%20in%20the%20Coal%20Mine%20Six%20Facts%20about%20the%20Recent%20Employment%20Effects%20of%20Artificial%20Intelligence.pdf)
- **Latest version:** https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- **Working paper, not yet peer-reviewed.** Stanford Digital Economy Lab, August 26, 2025.
- **Authors:**
  - **Erik Brynjolfsson** — Stanford University and NBER (erikb@stanford.edu)
  - **Bharat Chandar** — Stanford University (chandarb@stanford.edu)
  - **Ruyu Chen** — Stanford University (ruyuchen@stanford.edu)
- **Reading scope:** Pages 1–20 read in detail (intro, related literature, data description, Facts 1–4 with figures). Facts 5–6 captured from intro summary; conclusion and robustness sections not read in detail. Sufficient for a substantive ingest given the intro's clear summary of all six facts.

## Schema note

This source was originally placed in `raw/articles/` by the user but is an academic working paper (formal econometric methodology, references, footnotes). Moved to `raw/papers/` and tagged `working_paper: true` in frontmatter. **Future schema evolution candidate:** the source-page schema may benefit from explicit fields for `working_paper` / `peer_reviewed` / `preprint` to make the rigor level legible without reading the body.
