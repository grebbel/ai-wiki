---
type: source
kind: paper
title: "The Crowdless Future? Generative AI and Creative Problem-Solving"
author: ["Léonard Boussioux", "Jacqueline N. Lane", "Miaomiao Zhang", "Vladimir Jacimovic", "Karim R. Lakhani"]
publisher: "Organization Science (INFORMS)"
journal_volume: "Vol. 35, No. 5, September–October 2024, pp. 1589–1607"
peer_reviewed: true
url: "https://doi.org/10.1287/orsc.2023.18430"
doi: "10.1287/orsc.2023.18430"
license: "CC BY 4.0"
raw: "../../raw/papers/boussioux-et-al-2024-the-crowdless-future-generative-ai-and-creative-problem-solving.pdf"
date_published: 2024-08-16
date_ingested: 2026-04-29
tags: [creative-problem-solving, crowdsourcing, generative-ai, GPT-4, prompt-engineering, novelty, circular-economy, human-AI-collaboration, lakhani, boussioux, lane, organization-science]
length: "~19 pages (read pp. 1589–1602: intro, lit, design, methods, results, discussion)"
---

# Boussioux, Lane, Zhang, Jacimovic & Lakhani — The Crowdless Future?

## TL;DR

A field study comparing **human-crowd (HC)** crowdsourcing against **human-AI (HAI) collaboration** for creative problem-solving. Setting: a 2023 challenge to generate **circular-economy business ideas**, run with [[Continuum Laboratory]] and Freelancer.com. **125 global solvers** produced 54 HC solutions; the research team prompt-engineered GPT-4 to produce 90 multi-instance HAI solutions and 90 single-instance HAI solutions. **300 evaluators** (recruited via Prolific from 1,000 screened) rated 234 randomly selected solutions across 18 blocks, producing **3,900 evaluator-solution pairs**.

**Headline finding — a trade-off:**

| Dimension | Human Crowd | Human-AI |
|---|---|---|
| **Novelty** | **Higher** (3.508 vs 3.230 multi / 3.469 single; HC 7.9 pp more likely top novelty) | Lower |
| **Strategic viability** | 3.194 | **3.236 / 3.315 (single higher, p<0.05)** |
| **Environmental value** | 3.616 | **3.763 / 3.827** |
| **Financial value** | 3.086 | **3.237 / 3.239** |
| **Overall quality** | 3.292 | **3.345 / 3.461 (single significantly higher)** |
| **Cost** | $2,555 + ~2,520 human-hours | **$27.01 + ~5.5 hours** (~94× cost reduction) |

The paper also introduces and tests two distinct **HAI search modes** (independent vs. differentiated), with the **differentiated single-instance configuration** outperforming the multi-instance independent configuration on most dimensions while preserving novelty.

## Key claims

### Two forms of human-AI search (the paper's framework)

| Mode | Mechanism | Effect |
|---|---|---|
| **Independent search** (multi-instance) | One initial prompt; multiple GPT-4 instances each generate a solution independently | Approximates parallel-path crowd search |
| **Differentiated search** (single-instance) | One initial prompt + iterative *differentiation instructions* after each output ("Make sure to tackle a different problem than the previous ones and propose a different solution") | Iteratively pushes the LLM to diversify successive responses; outperforms independent search on quality and value while preserving novelty |

The paper argues differentiated search is the more interesting HAI pattern because it converts the LLM's tendency to converge on the "mean" answer into a controllable parameter.

### Empirical results — main mixed-effects models

Models include screening criteria + evaluator covariates (gender, education, STEM major, employment, cohort, word count); 18 solution blocks, 300 evaluators, N=3,900.

**Table 3 — HAI vs HC (combined):**
- Novelty: −0.140 (p<0.001) — HAI lower
- Strategic viability: +0.088 (p=0.016)
- Environmental value: +0.160 (p<0.001)
- Financial value: +0.143 (p<0.001)
- Quality: +0.101 (p=0.002)

**Table 4 — splitting HAI into multi-instance vs single-instance:**
- HAI multi-instance: lower novelty (−0.217, p<0.001); no quality difference vs HC (0.049, p=0.165)
- HAI single-instance: not significantly less novel than HC (−0.056, p=0.156); higher strategic viability (+0.133, p<0.01); higher quality (+0.159, p<0.001)
- Single-instance vs multi-instance: significantly different across most dimensions (p<0.001 for novelty, environmental, financial; p=0.038 for strategic viability)

**Top-decile results (Tables 5–6):** HAI is 7.9 pp less likely to achieve top novelty rating. No differences across other dimensions at the top decile — meaning HC retains a novelty advantage at the *extreme* of the distribution.

### Interpretation: solution-space search behaviors

The authors argue HAI solutions concentrate in **incremental search space** proximal to existing ideas (consistent with LLM training on past data; tendency toward statistical mean). HC exhibits more **variable search behavior, both at the bottom and top extremes** of novelty — surfacing more "extreme outliers" that current AI systems tend not to produce.

Three failure modes flagged for HAI in creative problem-solving:
1. **Formal-rationality bias** — LLMs constrain exploration via training-data formal rules, missing context-dependent or personal perspectives.
2. **Training-data confinement** — outputs "retrospective and ultimately confined" to LLM's training corpus.
3. **Confabulation / hallucination** — *can* boost novelty by combining concepts from disparate domains, but may also produce distorted reflections of flawed data with limited practical value.

### Setting and design

- **Crowdsourcing context**: partnered with Continuum Laboratory and Freelancer.com on a circular-economy business-ideas challenge (Jan 30 – May 15, 2023). 310 submissions; 148 prize-eligible; 125 deemed eligible after off-topic filtering.
- **Prize pool**: $2,555 ($10 to each of 148 nonblank entrants + $1,000 best overall + $75 platform fee).
- **HAI prompt engineering**: one of the authors performed all prompt engineering using GPT-4 Python API, default temperature 1.0; baseline + role-playing + chain-of-thought prompting techniques layered.
- **Evaluator screening**: 1,000 screened on Prolific; 300 passed (US, ≥18, ≥2 years experience or ≥60% on circular-economy knowledge skills test).
- **Evaluation criteria**: Novelty, Strategic Viability, Environmental Value, Financial Value, Quality (Likert 1–5).
- **Compensation**: $12 base + $1 bonus for matching consensus per solution; mean payout $13–24.

### Cost / time comparison

| | HC | HAI |
|---|---|---|
| Total monetary cost | $2,555 | $27.01 |
| Human-hours | ~2,520 (incentive estimate) | ~5.5 (researcher prompt-engineering) |
| Number of ideas after filtering | 54 (HC) / 730 generated, 180 sampled (HAI) | — |
| Avg word count per solution | 204 | 231 (multi) / 265 (single) |

The cost-time gap is ~**94×** in money and **~458×** in time — a substantial structural advantage for HAI in early-stage idea generation.

## Methodology notes

- Pre-registered design; Harvard IRB approved (IRB23-0770).
- Blocked randomized evaluation: each evaluator nested in one of 18 solution blocks; each block had 13 solutions (3 HC + 5 multi-instance HAI + 5 single-instance HAI).
- Evaluators **blind** to solution source (HC vs HAI).
- Mixed-effects (hierarchical linear) models with random intercepts/slopes for both blocks and evaluators (lmerTest in R).
- HAI prompt engineering all done by *one author* — a single-prompt-engineer limitation flagged in the paper.

## Limitations / caveats (per paper)

- Single domain (circular-economy ideation); generalization to other creative tasks open.
- One LLM (GPT-4 mid-2023); methodology pre-dates more recent models.
- One prompt engineer for all HAI conditions; engineer skill varies in practice.
- HAI outputs may be retrospective (training-data confined); novelty findings are time-bounded to GPT-4's training cutoff.

## Quotes worth saving

> "Whereas HC solutions exhibit higher novelty — both on average and for highly novel outcomes — HAI solutions demonstrated superior strategic viability, financial and environmental value, and overall quality."

> "Notably, HAI solutions cocreated through *differentiated* search, where human-guided prompts instructed the large language model to sequentially generate output distinct from previous iterations, outperformed solutions generated through *independent* search."

> "By incorporating 'AI in the loop' into human-centered creative problem-solving, our study demonstrates a scalable, cost-effective approach to augment the early innovation phases."

> "We surmise that, ultimately, the novelty and value of HAI outputs will depend on how humans engage with AI to guide its solution search behaviors."

## Related in this wiki

- [[automation-vs-augmentation]] — differentiated-search vs. independent-search is a fine-grained augmentation pattern; the novelty/value trade-off is a per-dimension measurement
- [[jagged-frontier]] — the HC/HAI novelty-vs-value split is one face of jaggedness: HAI sits in proximal/incremental search space while HC explores distant/outlier space
- [[generative-ai]] — field cost/time data on GPT-4 in creative idea generation
- [[ai-employment-effects]] — implications for crowdsourcing labor markets (Freelancer.com-style platforms)
- [[2026-04-28-dellacqua-jagged-technological-frontier]] — same publication (Org Sci) and shared author ([[Karim Lakhani]]); also field-experimental GPT-4 evidence; consulting tasks rather than ideation crowdsourcing
- [[2026-04-28-anand-wu-genai-playbook]] — locates ideation in the "creative catalyst zone" of their 2×2 (low-cost-of-error / tacit knowledge); this paper provides empirical content for that zone
- [[2026-04-28-bansal-birkinshaw-systems-thinking]] — circular-economy framing as a wicked-problem domain; topical adjacency
- [[Karim Lakhani]] — author entity (existing)
- [[Léonard Boussioux]], [[Jacqueline N. Lane]], [[Miaomiao Zhang]], [[Vladimir Jacimovic]] — author entities
- [[Continuum Laboratory]] — partner organization
- [[Harvard Business School]] — affiliation (Lane, Jacimovic, Lakhani)
