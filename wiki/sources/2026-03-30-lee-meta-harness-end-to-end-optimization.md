---
type: source
kind: paper
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
author: ["Yoonho Lee", "Roshen Nair", "Qizheng Zhang", "Kangwook Lee", "Omar Khattab", "Chelsea Finn"]
affiliations: ["Stanford University", "KRAFTON", "MIT"]
project_page: "https://yoonholee.com/meta-harness/"
optimized_harness: "https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact"
arxiv_id: "2603.28052v1"
url: "https://arxiv.org/abs/2603.28052"
publisher: "arXiv (cs.AI preprint)"
date_published: 2026-03-30
date_ingested: 2026-05-17
length: "12 pages of main text + appendix; read in full"
raw: "../../raw/papers/02_Lee_Meta-Harness_arxiv-2603.28052v1.pdf"
tags: [agent-harness, harness-engineering, meta-harness, terminalbench-2, claude-opus-46, claude-haiku-45, outer-loop-optimization, harness-search, text-classification, retrieval-augmented-reasoning, agentic-coding, transferability, raw-traces, stanford-iris-lab, dspy-team]
relationships:
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Pan articulates the harness representation (NLAH); Lee searches over harness content (Meta-Harness as outer-loop optimisation). Complementary: 'what should a harness look like?' (Pan) vs 'how do we find a good one automatically?' (Lee)"
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Meta-Harness's outer-loop harness search via coding-agent proposer (Claude Code + Opus 4.6) reading full filesystem history is the offline equivalent of Karten's in-episode Refiner loop. Both make the case that 'access to raw prior experience' is the load-bearing primitive"
  - type: supports
    target: 2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering
    via: "primary source for PY's named result 'Meta-Harness (Stanford) automatically optimized harness code to reach rank 1 on TerminalBench with Haiku'. Verified: Meta-Harness achieves 37.6% on Claude Haiku 4.5, ranking #1 among Haiku agents on TerminalBench-2 leaderboard (next-best: Goose 35.5%)."
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Lee et al. authored by Omar Khattab (MIT, DSPy lead) — confirms the wiki's tracking of Meta-Harness as 'the DSPy-team paper' Osmani referenced via Viv Trivedy. Primary-source anchor for the 'small model + great harness > large model + bad harness' claim (Meta-Harness on Haiku 4.5 outranks all hand-engineered Haiku 4.5 agents; competitive with Opus 4.6 agents)."
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "Lee et al. is the primary source for the YouTube synthesis's transferability claim. Table 6: discovered Meta-Harness retrieval policy on math reasoning transfers across 5 held-out models (GPT-5.4n, GPT-5.4m, Gem-3.1FL, Gem-3F, GPT-20B) with +4.7-point average gain over no retrieval"
  - type: uses
    target: agent-harness
---

# Lee, Nair, Zhang, Lee, Khattab, Finn — *Meta-Harness: End-to-End Optimization of Model Harnesses*

A **12-page arXiv preprint** (cs.AI, **2603.28052v1**, 30 March 2026) by **Yoonho Lee** (Stanford), **Roshen Nair** (Stanford), **Qizheng Zhang** (Stanford), **Kangwook Lee** (KRAFTON), **Omar Khattab** (MIT), and **Chelsea Finn** (Stanford). **The DSPy-team paper** the wiki has been triangulating since 2026-05-04 — Khattab is the DSPy author, and Lee et al. is the paper Osmani referenced via "Viv (Trivedy)" and the Prompt Engineering YouTube synthesised second-hand. Project page: [yoonholee.com/meta-harness](https://yoonholee.com/meta-harness/); optimised TerminalBench-2 artifact: [github.com/stanford-iris-lab/meta-harness-tbench2-artifact](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact).

**Identification closed** by [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] reference [10] AND independently by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]]. **This is now the primary-source ingest.** Together with [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al. (NLAH/IHR)]] and [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al. (Continual Harness)]], Meta-Harness completes the **March-May 2026 academic-anchor triple** the wiki has been tracking.

## TL;DR

- **The headline claim** (the opening sentence of the paper): **"Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark."** This is the **load-bearing single-sentence framing** for the "harness > model" thesis the wiki has carried second-hand. Lee et al. cite this as a result from Bui (reference [47]), but their own results substantiate the magnitude empirically across three domains.
- **The thesis.** Existing text optimizers (OPRO, TextGrad, GEPA, AlphaEvolve/OpenEvolve, Feedback Descent, TTT-Discover) are **poorly matched to harness engineering** because they "compress feedback too aggressively: they are memoryless, condition only on scalar scores, or restrict feedback to short templates or summaries." Meta-Harness exposes **full history through a filesystem**, enabling **selective diagnosis of raw prior code and execution traces** rather than optimization from compressed per-candidate summaries.
- **The Meta-Harness search loop** (a single coding-agent proposer with filesystem access):
  1. **Filesystem 𝒟** stores all prior candidates' source code, scores, and execution traces (prompts, tool calls, model outputs, state updates).
  2. **Coding-agent proposer (Claude Code with Opus-4.6)** reads filesystem via `grep`/`cat`/standard terminal tools — *not* a fixed prompt-template. Reads a **median of 82 files per iteration, referencing 20+ prior candidates per step**.
  3. Each iteration the proposer queries filesystem, proposes a new harness, the harness is evaluated, and the new (code, scores, traces) get added to 𝒟.
  4. Runs evolution for fixed iterations (typically ~60 harnesses over 20 iterations) with final test-set evaluation on the Pareto frontier.
- **The full-history-vs-compressed-feedback comparison.** Methods compared at the *MTok per iteration* of context: OPRO 0.002 / TextGrad 0.015 / AlphaEvolve 0.022 / GEPA 0.008 / Feedback Descent 0.012 / TTT-Discover 0.026 / **Meta-Harness 10.0** — three orders of magnitude more context per artifact evaluation. *"A single evaluation can produce up to 10,000,000 tokens of diagnostic information."* The paper's central architectural bet is that **selective access to prior diagnostic experience matters more than aggressive compression**.
- **Empirical results across three domains** — Meta-Harness substantially outperforms all baselines in all three:

### Online text classification (USPTO + S2D + Law + 6 OOD datasets)

| Method | USPTO | S2D | Law | Avg Acc | Ctx (k tokens) |
|---|---|---|---|---|---|
| Zero-shot | 12.0 | 63.2 | 7.0 | 27.4 | 0 |
| Few-shot (all) | 15.0 | 78.3 | 29.0 | 40.8 | 12.3 |
| MCE [Ye et al.] | 14.0 | 83.0 | 23.0 | 40.0 | 28.5 |
| ACE [Zhang et al.] | 16.0 | 77.8 | 29.0 | 40.9 | 50.8 |
| **Meta-Harness** | **14.0** | **86.8** | **45.0** | **48.6** | **11.4** |

**+7.7 points over the best prior text optimizer (ACE) while using 4× fewer context tokens (11.4K vs 50.8K).** **Matches the next-best text optimizer's final accuracy after just 4 evaluations** (vs 60 for ACE). **OOD evaluation** on 9 unseen text classification datasets: Meta-Harness 73.1% vs ACE 70.2% — *the discovered harness captures generally effective strategies for text classification rather than overfitting.*

### Retrieval-augmented math reasoning (200 IMO-level problems)

Discovered Meta-Harness retrieval policy: **average +4.7 points across 5 held-out models** (GPT-5.4n, GPT-5.4m, Gem-3.1FL, Gem-3F, GPT-OSS-20B). **Transferability without retraining** — the search ran on GPT-OSS-20B as the proposer base, but the discovered retrieval harness transfers across model families. *"A single discovered harness transfers across five held-out models."*

### Agentic coding on TerminalBench-2 (89 challenging tasks)

| Model | Harness | Pass (%) |
|---|---|---|
| **Claude Opus 4.6** | Claude Code | 58.0 |
|  | Terminus 2 | 62.9 |
|  | Mux | 66.5 |
|  | Droid | 69.9 |
|  | TongAgents | 71.9 |
|  | MAYA-V2 | 72.1 |
|  | Terminus-KIRA | 74.7 |
|  | Capy | 75.3 |
|  | **Meta-Harness** | **76.4** |
|  | (ForgeCode) | (81.8 — unreproducible) |
| **Claude Haiku 4.5** | OpenHands | 13.9 |
|  | Claude Code | 27.5 |
|  | Terminus 2 | 28.3 |
|  | Mini-SWE-Agent | 29.8 |
|  | Terminus-KIRA | 33.7 |
|  | Goose | 35.5 |
|  | **Meta-Harness** | **37.6** |

**Meta-Harness ranks #2 among all Opus 4.6 agents (the only higher-scoring is ForgeCode at 81.8%, which the authors couldn't reproduce from the publicly available code base, suggesting the leaderboard score depends on components beyond the published repository).** **Meta-Harness ranks #1 among all Haiku 4.5 agents** with a +2.1 point margin over the next-best (Goose 35.5%).

- **The ablation that closes the "raw traces are key" wiki open question.** Table 3 (online text classification): **Scores Only → 34.6 median / 41.3 best**; **Scores + Summary → 34.9 median / 38.7 best**; **Meta-Harness (full filesystem) → 50.0 median / 56.7 best**. *"Access to raw execution traces is the key ingredient for enabling harness search. Summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details."*
- **Practical implementation.** Each harness is a single-file Python program. Proposer is **Claude Code with Opus-4.6**, guided by a minimal domain-specific skill describing where to write new harnesses, how to inspect previous harnesses and execution traces, and what files it can and cannot modify. Base model is always frozen. A typical run evaluates roughly 60 harnesses over 20 iterations.

## What was actually ingested

Full 12-page PDF (sections 1-5 main text + references). All three experimental domains. All five tables. The Pareto-frontier accuracy-context tradeoff plot (Figure 3). The Meta-Harness search loop diagram (Figure 2).

## Cross-positioning with the wiki

### Closes wiki open questions

| Wiki claim (status before this ingest) | Status after |
|---|---|
| **The DSPy-team "Meta-Harness" paper** (carried second-hand since [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]]; identification closed twice already on 2026-05-17) | **Closed — primary source ingested.** Yoonho Lee (first author, Stanford IRIS Lab) + Omar Khattab (MIT, DSPy lead). |
| **Meta-Harness 76.4% on Terminal Bench 2** | **Closed — verified on Opus 4.6** as the model substrate. |
| **Transferability across 5 models** | **Closed — verified.** Math retrieval harness transfers to GPT-5.4n, GPT-5.4m, Gem-3.1FL, Gem-3F, GPT-OSS-20B with +4.7 avg gain. |
| **Raw traces > summaries** | **Closed — verified by ablation.** Scores-only 34.6 / Scores+Summary 34.9 / Full filesystem 50.0. The "+7.7 points using 4× fewer context tokens" framing the wiki has carried is now empirically anchored. |
| **"Small model + great harness > large model + bad harness"** (carried second-hand from PY video) | **Closed — verified on Haiku 4.5.** Meta-Harness on Haiku 4.5 reaches 37.6%, beating all hand-engineered Haiku 4.5 agents. **But qualified**: Meta-Harness on Haiku 4.5 (37.6%) is still well below Meta-Harness on Opus 4.6 (76.4%). The discipline raises both models' performance, not just the smaller one's. |

### Outer-loop optimisation vs in-episode refinement (vs Karten)

[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.'s]] Continual Harness operates **in-episode, reset-free**, with a Refiner editing the harness every *F* steps from the most recent trajectory window. Meta-Harness operates **across-episodes, in an offline outer loop**, with a proposer reading the *full prior history* across all candidate harnesses. The two are complementary:

| | Karten (Continual Harness) | Lee (Meta-Harness) |
|---|---|---|
| **Loop scope** | Inside a single episode | Across many evaluation runs |
| **Refinement signal** | Recent trajectory window τ_{t-F:t} | Full filesystem 𝒟 of all prior candidates |
| **Proposer/Refiner** | LLM Refiner editing CRUD on *(p, G, K, M)* | Claude Code with Opus-4.6 reading via grep/cat |
| **Resets** | Reset-free (state propagates across iterations) | Per-candidate (each harness evaluated independently) |
| **Compute budget** | K=256 steps × N iterations | ~60 harnesses × 20 iterations |
| **Verified transferability** | Bootstrap-updating > bootstrap-frozen within game | Retrieval policy transfers across 5 held-out LLMs |

### Adjacency to [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al.]]

Pan asks *"what should a harness look like?"* (representation question; argues for natural-language carriers under shared runtime). Lee asks *"how do we find a good harness automatically?"* (search question; argues for filesystem-based outer-loop with coding-agent proposer). **Both papers position the harness as a first-class scientific object that can be designed, exposed, and evaluated** — Pan from the representation side, Lee from the search side.

The two papers came out **4 days apart** (Pan 26 Mar 2026; Lee 30 Mar 2026), from independent groups (Tsinghua/HITSZ vs Stanford/KRAFTON/MIT), without citing each other directly. **This convergent independent timing is itself the strongest single signal in the wiki to date that the harness construct has crystallised as a research-frontier object.**

### Substantial agreement with [[2026-05-15-osmani-agent-harness-engineering|Osmani]] (with attribution corrections)

| Osmani's practitioner claim | Lee et al.'s empirical anchor |
|---|---|
| *"A decent model with a great harness beats a great model with a bad harness"* | Meta-Harness on Haiku 4.5 (37.6%) beats hand-engineered Haiku 4.5 agents; competitive performance with Opus 4.6 agents that use less-optimised harnesses (above Claude Code 58.0% and Terminus 2 62.9% but below Meta-Harness 76.4%) |
| *"The ratchet — every line in AGENTS.md should be traceable to a failure"* | The Meta-Harness proposer "uses execution traces to identify confounded edits, isolate likely causal changes, and shift toward safer modifications after repeated regressions" — automated ratchet via search |
| *"The gap between what today's models can do and what you see them doing is largely a harness gap"* | The 6× single-benchmark performance gap claim (opening line of paper) anchors this rhetorically; Tables 4 + 7 substantiate it empirically |

## Named entities (this ingest)

- [[Yoonho Lee]] — Stanford IRIS Lab; lead author. Prior wiki appearance: not yet. **First mention. Dangling.**
- [[Roshen Nair]] — Stanford. **First mention. Dangling.**
- [[Qizheng Zhang]] — Stanford. **First mention. Dangling.**
- [[Kangwook Lee]] — KRAFTON. **First mention. Dangling.**
- [[Omar Khattab]] — MIT (formerly Databricks / Stanford / DSPy author). **First mention with affiliation. The wiki has been carrying "Khattab et al." second-hand for two weeks; this is the primary-source identification of the named author.** Dangling pending second-source mention.
- [[Chelsea Finn]] — Stanford. **First mention. Dangling.** (Co-author of *Model-Agnostic Meta-Learning* — reference [17] in this paper.)
- [[Stanford IRIS Lab]] — Stanford lab; hosts the released TerminalBench-2 optimised harness artifact. **First mention.**
- [[KRAFTON]] — Korean gaming/AI company; provided API credit support. **First mention.**

Plus reference-list entities: [[ForgeCode]] (TerminalBench-2 leaderboard #1 on Opus 4.6 at 81.8%, but unreproducible from public code), [[Terminus-KIRA]] (74.7% on Opus 4.6 — the next-strongest reproducible TerminalBench-2 agent), [[Goose]] (next-best on Haiku 4.5).

## Source-quality notes

- **Genre**: arXiv preprint (cs.AI), pre-publication. Stanford / KRAFTON / MIT academic + industry-research affiliations.
- **Reproducibility posture**: **strong**. Project page + GitHub repo for the optimised TerminalBench-2 harness artifact released. Discussion explicitly notes that "the only higher-scoring [than Meta-Harness] Opus 4.6 agent is ForgeCode (81.8%); however, we were unable to reproduce their reported result from the publicly available code base, suggesting their leaderboard scores depend on components beyond the published repository" — honest about leaderboard reproducibility issues.
- **Empirical-anchor count**: high — three domains × multiple ablation conditions × OOD evaluation × 5-model transferability test.
- **Negative results reported**: yes — text optimizers with summary-only feedback (TTT-Discover, OpenEvolve) underperform Meta-Harness substantially; the *"summaries do not recover the missing signal, and may even hurt"* finding is empirical, not asserted.
- **Confidence: 0.88.** Per Lifecycle: single source +0.05 for academic primary-source +0.05 for honest reproducibility-issue reporting +0.05 for OOD generalisation evidence = 0.95 cap but capped at 0.88 pending peer review and independent reproduction.

## Open questions

- **The 81.8% ForgeCode result.** Lee et al. couldn't reproduce. Worth flagging on the TerminalBench-2 leaderboard discussion — the public leaderboard rank may not reflect reproducible-from-public-code performance.
- **Meta-Harness transferability *of the proposer* across coding-agent products.** Lee et al. use Claude Code (Opus-4.6) as the proposer. Whether the same approach works with Codex / Cursor / Aider as the proposer is "deferred to future work" (discussion section). Worth tracking.
- **Pan + Lee unification.** The two papers came out 4 days apart without citing each other. The natural follow-up — running Meta-Harness search inside Pan's IHR runtime over NLAH representations — is *the obvious next experiment for the field*.
- **Cost vs performance Pareto on TerminalBench-2.** Table 7 reports pass rates but not cost. The Meta-Harness search itself takes ~60 harnesses × 20 iterations on a coding-agent proposer; the *amortised cost of obtaining the discovered harness vs the per-task cost of running it* is not in the paper. Karten et al.'s cost-completion Pareto plane (Emerald) sets a high bar for this kind of analysis that future Meta-Harness work would do well to match.
