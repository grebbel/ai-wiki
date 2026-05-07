---
type: concept
aliases: ["AI benchmark", "AI benchmarks", "AI evaluation", "AI evals"]
tags: [ai-benchmarks, ai-evaluation, foundation-models]
confidence: 0.85
last_confirmed: "2026-05-07"
source_count: 4
relationships:
  - type: uses
    target: foundation-models
    via: "benchmarks evaluate foundation-model capability"
---

# AI Benchmarks

Standardized tests used to compare AI models. The benchmark landscape in 2024 is shaped by **rapid saturation of older tests, an explosion of new harder tests, and a methodological shift toward agent / reasoning evaluations**. This page is an **umbrella** — individual benchmarks are listed here in a roster and get promoted to their own pages once they're discussed standalone in another source.

## Working definition

An AI benchmark is a fixed dataset + scoring function used to compare model performance under controlled conditions. Benchmarks live on a saturation cycle: introduced → models improve → benchmark saturates → harder benchmark proposed.

The 2024 wave is unusual in two ways:

1. **Speed of saturation.** AI now masters new benchmarks within ~12 months of introduction (MMMU +18.8pp, GPQA +48.9pp, SWE-bench +67.3pp in one year).
2. **Methodological shift.** Researchers are moving from static single-shot benchmarks toward **agent benchmarks** that evaluate trajectories under time budgets (RE-Bench), and toward **reasoning benchmarks** that resist pattern-matching (PlanBench, FrontierMath).

## Key claims

### 2024: rapid benchmark saturation

Major one-year benchmark gains in 2024 ([[2026-04-28-ai-index-report-2025|AI Index 2025]] §2):

- **MMMU**: +18.8 percentage points
- **GPQA**: +48.9 percentage points
- **SWE-bench**: +67.3 percentage points (4.4% → 71.7%)

### 2025: continued saturation, agent leaps, science benchmarks ([[2026-04-30-ai-index-report-2026|AI Index 2026]])

- **SWE-bench Verified**: 60% → **near 100%** in one year (the same benchmark that was at 71.7% in 2024 has effectively saturated within two years of being introduced).
- **OSWorld** (real computer tasks across operating systems): AI agents leapt from **12% → ~66%** task success in one year. Agents still fail roughly **1 in 3** attempts on structured benchmarks.
- **IMO** (International Mathematical Olympiad): **Gemini Deep Think** earned a **gold medal**.
- **Analog clock reading**: top model only **50.1%** correct — emblematic of the [[jagged-frontier]] (capability and incompetence on tasks of similar perceived difficulty).
- **ChemBench**: frontier AI models **outperform** human chemists on average; below 20% on astrophysics replication, 33% on Earth-observation questions.
- **RLBench** (robotic manipulation in software-based simulations): **89.4%** success — but robots succeed on only **12%** of household tasks in the real world.
- Frontier-lab disclosure has dropped: independent testing does not always confirm what developers report.

### New harder benchmarks (proposed because the old ones saturated)

- **Humanity's Last Exam** — academic test; top score so far: **8.80%**.
- **FrontierMath** — complex math; AI ~**2%** solve rate.
- **BigCodeBench** — coding; AI **35.5%** vs. human standard 97%.
- **PlanBench** — logical planning; AI **fails consistently** even when provably correct solutions exist.
- **RE-Bench** — agent evaluation: in 2-hour budgets AI scores **4× human experts**, but humans win **2:1 at 32 hours**.

### Vantage / Executive LLM — benchmarking *human* skills, not models ([[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]])

A **structurally different** type of benchmark: assesses humans on *durable skills* (collaboration, creativity, critical thinking) using LLMs as both **conversational teammates** and **autoraters**. Methodologically distinct from PISA 2015 (scripted simulated teammates with multiple-choice answers) and ATC21S (human-human dyads in digital environments), both of which sat at narrow points on the validity-vs-rigor tradeoff.

- **Architecture:** a single Executive LLM drives multiple AI teammates *and steers the conversation* to elicit observable skill evidence. A separate AI Evaluator scores transcripts against psychometric rubrics. Analogous to a **computerized adaptive test (CAT)**, but for *complex social/cognitive constructs* rather than item-difficulty calibration.
- **Validation (large-N empirical):** 188 US-based participants ages 18-25, 373 conversations. **LLM-vs-human-rater agreement matches inter-human-rater agreement** (Cohen's κ ~0.45–0.64). For a downstream creativity task with 280 high-school students (180 held-out): **Pearson r = 0.88** between Gemini autorater and human expert scores.
- **Models:** Gemini 2.5 Pro (collaboration); Gemini 3 (creativity / critical thinking initial results).
- **Evidence elicitation:** at conversation level with skill-matched Executive LLM, evidence rates of **92.4% (Project Management)** and **85% (Conflict Resolution)**. Independent Agents (no steering) elicit significantly less. Telling subjects "focus on this skill" without LLM steering has *no effect* (p > 0.6) — the steering must come from the AI side.
- **Notable:** the critical-thinking rubric explicitly evaluates how well participants **use AI tools** during the assessment — fact-checking, retrieval, stress-testing arguments. AI fluency treated as a sub-component of CT in 2026, not a confounder.

This expands the wiki's benchmark roster from "fixed-task evaluations of model capability" to include **scalable evaluations of human skills using LLM scaffolding**. See [[durable-skills]] for the broader concept.

### Task horizons ([[METR]] / [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index, 4th report]])

A complement to single-shot benchmarks: **task horizons** measure the *duration* of tasks at which an AI achieves a given success rate. [[METR]] introduced this measure; the Anthropic Economic Index applies the same lens to its own data.

For [[Claude Sonnet 4.5]], the duration at which 50% success is achieved varies sharply by source:

| Source | 50% success threshold |
|---|---|
| METR (fixed-task benchmark) | ~2 hours |
| Anthropic 1P API | ~3.5 hours |
| Anthropic Claude.ai | ~19 hours |

Per the Anthropic report, the Claude.ai number is much higher because of selection bias (users bring tasks they expect Claude to succeed on) and task decomposition with feedback loops. The methodology gap is itself diagnostic — fixed-benchmark horizons and platform-observed effective horizons measure different things.

### Benchmark roster (mentioned in this wiki, awaiting standalone pages)

| Benchmark | Domain | Status as of [[2026-04-28-ai-index-report-2025|AI Index 2025]] |
|---|---|---|
| **MMLU** | Multitask language | Saturated; U.S./China gap closed to 0.3pp |
| **MMMU** | Multimodal understanding | New (2023); AI gained 18.8pp in 2024 |
| **GPQA** | Graduate-level reasoning | New (2023); AI gained 48.9pp in 2024 |
| **SWE-bench** | Real-world coding | New (2023); AI 4.4% → 71.7% in one year |
| **HumanEval** | Code completion | Saturated; near parity U.S./China |
| **MATH** | Competition math | Saturated; near parity U.S./China |
| **GSM8K** | Grade-school math | Saturated |
| **MedQA** | Clinical knowledge | OpenAI o1 = 96.0% (state-of-art); approaching saturation |
| **HELM Safety** | RAI / safety | New 2024; for [[responsible-ai]] |
| **AIR-Bench** | RAI | New 2024 |
| **FACTS** | Factuality | New 2024 |
| **SimpleQA** | Factuality | New 2024 |
| **Hughes Hallucination Evaluation Model** | Factuality | Updated 2024 |
| **HaluEval** | Factuality | Failed to gain widespread adoption |
| **TruthfulQA** | Factuality | Failed to gain widespread adoption |
| **Foundation Model Transparency Index** | Disclosure / governance | 37% → 58% Oct 2023 → May 2024 |
| **Chatbot Arena Leaderboard** | Pairwise human preference Elo | Top-2 gap 0.7%, top-10 gap 5.4% |
| **Humanity's Last Exam** | Academic generalist | New 2024; top score 8.80% |
| **FrontierMath** | Advanced math | New 2024; AI ~2% |
| **BigCodeBench** | Coding | New 2024; AI 35.5% vs. human 97% |
| **PlanBench** | Logical planning | AI consistently fails |
| **RE-Bench** | Agent / time-budget | New 2024; 4× humans @ 2hr, humans win 2:1 @ 32hr |
| **Vantage** ([[durable-skills]]) | Human skill assessment via LLM scaffolding | New 2026 (Globerson et al., Google Research); LLM autoraters match human raters; Pearson 0.88 vs experts on creativity tasks |

## Debates / contradictions

- **Are we measuring what matters or what's measurable?** Benchmarks gain complexity faster than tasks gain real-world specification. Open question whether the saturation race is sustainable, or whether the field is overdue for a different evaluation paradigm.
- **Agent benchmarks vs. static benchmarks.** RE-Bench's two-time-budget result suggests static benchmarks can mislead on real workflows. Future evaluations will likely emphasize trajectories, not single-shot scores. But agent evaluations are themselves harder to standardize — open question whether the field can converge.
- **Reasoning benchmarks.** The IMO/PlanBench split suggests current models are good at *patterns of math* but bad at *symbolic reasoning where verifiable solutions exist*. Open question for the [[generative-ai]] roadmap, and load-bearing for safety in high-stakes deployments.
- **Methodology stability.** Many of the highest-impact 2024 benchmarks (MMMU, GPQA, SWE-bench) are <2 years old. Year-over-year claims about "AI improvement" depend on stable benchmark methodology — worth flagging when sources cite trend lines without examining benchmark drift.

## Related concepts

- [[foundation-models]] — what's being benchmarked
- [[generative-ai]] — sub-domain dominant in current benchmarks
- [[responsible-ai]] — RAI benchmarks intersect here

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-benchmarks") OR contains(tags, "ai-evaluation")
SORT file.name ASC
```
