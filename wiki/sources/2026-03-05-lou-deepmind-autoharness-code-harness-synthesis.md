---
type: source
kind: paper
title: "AutoHarness: improving LLM agents by automatically synthesizing a code harness"
author: ["Xinghua Lou", "Miguel Lázaro-Gredilla", "Antoine Dedieu", "Carter Wendelken", "Wolfgang Lehrach", "Kevin P. Murphy"]
affiliations: ["Google DeepMind"]
arxiv_id: "2603.03329v1"
url: "https://arxiv.org/abs/2603.03329"
publisher: "arXiv (cs.CL preprint)"
date_published: 2026-03-05
date_ingested: 2026-05-17
length: "7 pages of main text + 6 pages of appendix (game list, per-game rewards, legal-action rates, prompts); read in full"
raw: "../../raw/papers/2603.03329v1.pdf"
tags: [agent-harness, autoharness, harness-synthesis, code-harness, harness-as-action-filter, harness-as-action-verifier, harness-as-policy, thompson-sampling, tree-search, textarena, gemini-25-flash, illegal-moves, kaggle-gamearena, google-deepmind]
relationships:
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "Both papers search over code-based harnesses with an LLM-as-proposer. AutoHarness (March 5) predates Meta-Harness (March 30) by 25 days. AutoHarness uses Thompson-sampling tree search with Gemini-2.5-Flash as the proposer at scale; Meta-Harness uses filesystem-with-full-history with Claude Code as the proposer. Independent confirmation that 'LLM proposes harness code' is a working paradigm."
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Pan argues for natural-language harness representation; AutoHarness argues for code harness synthesis. The two operate at the opposite end of the representation-vs-search dichotomy — AutoHarness extreme is harness-as-policy (the LLM generates pure Python code that runs at inference time without any LLM calls)."
  - type: supports
    target: 2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering
    via: "primary source for the PY video's named AutoHarness reference (arXiv:2603.03329)"
  - type: contradicts
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "Lee et al. argue *raw execution traces are the key ingredient* and explicitly find that summaries hurt. AutoHarness uses 'at most 5 failed steps... fed to the Critic' as feedback — a relatively compressed feedback channel. The two papers achieve similar results via opposite design choices on feedback richness; this is a genuine open question worth tracking."
  - type: uses
    target: agent-harness
---

# Lou, Lázaro-Gredilla, Dedieu, Wendelken, Lehrach, Murphy — *AutoHarness: improving LLM agents by automatically synthesizing a code harness*

A **13-page arXiv preprint** (cs.CL, **2603.03329v1**, 5 March 2026) by **Xinghua Lou**, **Miguel Lázaro-Gredilla**, **Antoine Dedieu**, **Carter Wendelken**, **Wolfgang Lehrach**, and **Kevin P. Murphy** — all at **Google DeepMind**. Published **3 weeks before Pan et al.** (NLAH, March 26) and **25 days before Lee et al.** (Meta-Harness, March 30), making AutoHarness **the earliest of the four primary-source academic papers in this batch's harness-engineering cluster**.

AutoHarness was named as a wiki ingest target by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]] yesterday. **This is now the primary-source ingest** — completing the wiki's coverage of the four core harness-engineering papers from spring 2026.

## TL;DR

- **The thesis.** *"When used as agents, LLMs often try to perform actions that are not just suboptimal for a given state, but are strictly prohibited by the external system."* In the Kaggle GameArena chess competition, **78% of Gemini-2.5-Flash losses were attributed to illegal moves** (not strategic blunders). AutoHarness demonstrates that **Gemini-2.5-Flash can automatically synthesize the code harness that prevents such failures**, using a small number of rounds of iterative code refinement given feedback from the environment.
- **Three harness types, increasing in autonomy from the LLM:**
  - **harness-as-action-filter** — calls `propose_action()` to generate a *set* of legal moves, leverages the LLM to rank them (potentially using chain-of-thought reasoning). The LLM is in the loop at inference time.
  - **harness-as-action-verifier** — calls the LLM to generate a single action, verifies it via synthesised `is_legal_action()`, and if invalid repeats the process with an "illegal action" warning. The LLM is in the loop at inference time, but verification is offloaded to deterministic code.
  - **harness-as-policy** — *uses code to choose the action; the code could in principle call an LLM, but in our setting, the policy uses primitive Python functions and standard libraries such as numpy, so we do not need to invoke an LLM at inference time.* **The extreme case: the LLM writes the entire policy as code, and is not called at runtime.**
- **The synthesis loop.** Tree search over the space of programs, guided by **Thompson sampling**. The LLM acts as a **mutation operator**, proposing refinements to the code based on feedback from execution. The search balances exploration (trying distinct logic branches) and exploitation (refining a partially working harness) to converge on a robust control loop. Heuristic value for each tree node = average legal-move accuracy. **At most 5 failed steps are sampled and fed to the Critic**, which consolidates the error types and feeds them with the original code into the Refiner to generate new (hopefully improved) code.
- **The training setup.** 10 parallel environments, rollouts of at most 1000 steps with auto environment resetting. Rollout terminated whenever an illegal move is made by the code or code execution fails. Training ends when heuristic value reaches 1.0 or times out. Uses **Gemini-2.5-Flash** for training.
- **Empirical results.**
  - **All 145 TextArena 1P and 2P games (after excluding 9 free-form text games) achieve 100% legal action success rate after synthesis.**
  - **2-player games (16 games): Gemini-2.5-Flash + AutoHarness wins 9/16 against Gemini-2.5-Pro (56.3% overall win rate)** — *the smaller model beats the larger one when wrapped in a synthesised harness*. Against vanilla Gemini-2.5-Flash, wins 12/16 (64.8%).
  - **1-player games (16 games): Gemini-2.5-Flash + AutoHarness 0.745 average reward** vs Gemini-2.5-Pro 0.707 vs Gemini-2.5-Flash 0.635 vs GPT-5.2 0.635 vs GPT-5.2-High 0.844.
  - **Harness-as-Policy (the extreme): 0.870 average reward** — *beating GPT-5.2-High (0.844)*. The LLM-as-policy is dispensed with entirely; the code policy generated by Gemini-2.5-Flash plays better than GPT-5.2-High plays directly. **Plus near-zero inference cost** (vs ~$640 for the GPT-5.2 experiments).
- **The motivating empirical anchor.** *"78% of losses by Gemini 2.5 Flash were attributed not to strategic blunders, but to multiple illegal moves."* This single statistic is the wiki's strongest in-context evidence for the *gap between model capability and deployable behaviour* claim that the entire harness-engineering literature rests on.
- **Cost-effectiveness as a first-class objective.** *"Using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective."* The cost numbers reported (~$640 for the GPT-5.2 experiments vs near-zero for Harness-as-Policy after synthesis) make the case quantitatively. **The wiki's clearest single numerical anchor for the "small model + synthesised harness" thesis.**

## What was actually ingested

Full 13-page PDF (7-page main text + 6-page appendix with game list, per-game rewards, per-game legal action rates, and full LLM-as-policy prompt). Three named harness types and all 16 evaluated 1P / 16 2P games. Methodology in full (Thompson sampling tree search, Refiner/Critic/Evaluator triple). Acknowledgements / authors / affiliations all DeepMind.

## Cross-positioning with the wiki

### Independent confirmation of LLM-proposes-harness paradigm

AutoHarness (Google DeepMind, March 5) and [[2026-03-30-lee-meta-harness-end-to-end-optimization|Meta-Harness]] (Stanford/MIT, March 30) are **independent papers, 25 days apart, both demonstrating that an LLM-proposer can synthesise harness code that outperforms hand-engineered baselines**. They make different design choices that the wiki should track:

| | AutoHarness (Lou et al.) | Meta-Harness (Lee et al.) |
|---|---|---|
| **Proposer LLM** | Gemini-2.5-Flash | Claude Code with Opus-4.6 |
| **Search algorithm** | Thompson-sampling tree search | Outer-loop search reading filesystem |
| **Feedback to proposer** | At most 5 failed steps + Critic consolidation | Full filesystem of all prior candidates' code, scores, traces |
| **Target tasks** | TextArena games (1P + 2P) | TerminalBench-2 + text classification + math reasoning |
| **Termination criterion** | Legal-move accuracy reaches 1.0 | Fixed number of iterations |
| **Inference-time LLM calls** | Zero for harness-as-policy | Per-task LLM calls inside the discovered harness |
| **Key result** | Haiku-equivalent (Flash) beats Pro / GPT-5.2-High via Harness-as-Policy | Meta-Harness #1 on Haiku 4.5 / #2 on Opus 4.6 |

### Productive contradiction: how rich does feedback to the proposer need to be?

[[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al.]] **explicitly find that summaries hurt**: Scores-only 34.6 / Scores+Summary 34.9 / Full filesystem 50.0 (text classification ablation). They argue *raw execution traces are the key ingredient*. AutoHarness uses **at most 5 failed steps + Critic consolidation** — a relatively compressed feedback channel — and still achieves strong results.

The two papers reach similar headline conclusions ("small model + synthesised harness beats larger model + hand-designed harness") via opposite design choices on feedback richness. **This is a genuine open question** worth tracking. Possible resolutions: (a) the harness-search task structure differs — AutoHarness optimises a small, well-defined policy code (TextArena games); Meta-Harness optimises a larger, multi-component context-management harness (text classification, retrieval, agentic coding); (b) the gain from raw-trace access may be domain-dependent — game-policy synthesis may not need diagnostic depth that text classification does.

### Confirms (and quantifies) the "78%-of-failures-are-harness-failures" claim

The wiki's harness-engineering cluster has been carrying *"agent failures are usually harness failures, not model failures"* as a rhetorical claim (anchored in [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] Friday-in-March anecdote). AutoHarness gives it the **first empirically-quantified anchor in a controlled benchmark**: 78% of Gemini-2.5-Flash chess losses in the Kaggle GameArena are attributed to illegal moves, not strategic errors. After AutoHarness wraps the same model, illegal-move rate drops to 0% across 145 games.

### The harness-as-policy extreme

AutoHarness's *harness-as-policy* condition is structurally similar to [[concepts/software-3.0|Software 3.0]]'s upper bound: the LLM compiles a code program that runs without any LLM in the loop at inference time. **The Harness-as-Policy result (0.870 avg reward, beating GPT-5.2-High 0.844 at near-zero inference cost) is the wiki's strongest empirical anchor for Karpathy's Software 3.0 thesis taken to its limit** — *the model is the compiler; the policy is code; the inference is free.* Worth a body link on the Software 3.0 page.

## Named entities (this ingest)

- [[Xinghua Lou]], [[Miguel Lázaro-Gredilla]], [[Antoine Dedieu]], [[Carter Wendelken]], [[Wolfgang Lehrach]], [[Kevin P. Murphy]] — Google DeepMind. **All first mentions. Dangling.** Kevin P. Murphy is the well-known author of *Probabilistic Machine Learning* textbooks. Wolfgang Lehrach is referenced in [[2026-03-30-lee-meta-harness-end-to-end-optimization|Meta-Harness's]] reference list as a co-author of *Code World Models for General Game Playing* (arXiv:2510.04542, 2025) — adjacent prior work.
- [[Google DeepMind]] — already in wiki ecosystem (via [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] affiliation).
- [[TextArena]] (Guertler et al. 2025) — game benchmark. **First mention. Dangling.**
- [[Kaggle GameArena]] — competitive benchmarking platform that motivated the work. **First mention.**

## Source-quality notes

- **Genre**: arXiv preprint (cs.CL), pre-publication. Google DeepMind affiliation.
- **Empirical-anchor count**: high — 145 games (full TextArena minus 9 free-form), 16 1P and 16 2P games evaluated for end-task performance, multiple agent comparisons including GPT-5.2-High (the strongest closed-model baseline available at writing time).
- **Reproducibility posture**: methodology described in detail; specific game implementations are cited (TextArena, Guertler et al. 2025). No explicit code release statement in the body.
- **Cost transparency**: yes — *"GPT-5.2 and GPT-5.2-High experiments cost approximately $640"* is a refreshingly honest cost disclosure rare in this literature.
- **Confidence: 0.85.** Per Lifecycle: single source +0.05 for industrial-research-lab affiliation (DeepMind) +0.05 for explicit cost reporting + 0.05 for negative-result acknowledgement (Harness-as-Policy doesn't beat GPT-5.2-High in *all* games — wins 3/16 directly, ties 8/16) = 0.85.

## Open questions

- **Multimodal extension.** Future-work section explicitly names Craftax and Terra Nova as targets. Open whether the synthesis loop transfers to image-conditioned game observations.
- **Cross-game library of reusable harnesses.** Future-work section mentions *"building up a library of reusable harnesses"* — this is the same direction Lee et al. demonstrate empirically (transferability across 5 held-out models). AutoHarness has not yet shown cross-game harness transfer.
- **The compressed-vs-full-trace feedback choice.** AutoHarness with 5-step-window feedback achieves comparable wins-against-larger-model headline as Meta-Harness with full-history feedback. Direct head-to-head ablation on the same task family would settle this.
- **Distillation back into the base LLM.** Future-work section asks *"distill the resulting domain specific experts (agents) back into the base LLM, so that the whole system becomes recursively self-improving"* — this is the same loop [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] operationalise as their model-harness co-learning loop. Convergent research directions worth tracking.
