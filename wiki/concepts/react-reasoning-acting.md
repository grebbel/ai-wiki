---
type: concept
aliases: ["ReAct", "Reason+Act", "reason-act-observe loop", "reasoning and acting", "ReAct framework", "ReAct paradigm"]
tags: [react, reasoning-and-acting, agentic-loop, chain-of-thought, tool-use, llm-agents, interpretability, human-in-the-loop, foundational]
confidence: 0.85
last_confirmed: "2026-06-12"
accessed_at: "2026-06-12"
source_count: 3
relationships:
  - type: authored-by
    target: Shunyu-Yao
    via: "first author of the 2022 ReAct paper and its Google Research blog"
  - type: authored-by
    target: Yuan-Cao
  - type: part-of
    target: ai-agents
    via: "the reason–act–observe loop is the structural core of the modern agent definition"
quality_score: 1
---

# ReAct (Reasoning + Acting)

**ReAct** is the prompting paradigm — introduced by [[Shunyu Yao]] et al. (with senior Google Research co-author [[Yuan Cao]]) in 2022 ([[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|paper]], ICLR 2023; [[2022-11-08-yao-cao-react-google-research-blog|Google Research blog]]) — that **interleaves free-form reasoning traces with task-specific actions** in a single language-model trajectory. It is the **genealogical root of the wiki's [[ai-agents|agent]] definition**: the *"LLM that autonomously uses tools in a loop"* the wiki adopts from 2026 practitioners is exactly ReAct's **reason → act → observe → adjust** cycle, named four years earlier.

## The core mechanism

Take a standard agent–environment setup: at step `t` the agent sees observation `oₜ` and takes action `aₜ`. ReAct **augments the action space** `A` with a language space `L`, so `Â = A ∪ L`. An action `âₜ ∈ L` is a **thought** (reasoning trace) that:

- does **not** affect the external environment (produces no observation feedback), but
- updates the model's working context `cₜ₊₁ = (cₜ, âₜ)` to support future reasoning or acting.

This yields a two-way synergy:

- **Reason to act** — thoughts decompose goals, build/track/adjust plans, inject commonsense, handle exceptions.
- **Act to reason** — actions interface with external sources (a Wikipedia API, a shell, a browser) to pull in information that grounds the next thought.

Before ReAct, the two halves were studied separately: **chain-of-thought** prompting reasoned but stayed *ungrounded* (prone to hallucination and error propagation, no way to update knowledge from the world), while **act-only** LLM agents acted but couldn't *reason abstractly* about high-level goals or maintain working memory. ReAct's claim is that interleaving them beats either alone.

## Two prompting regimes

| Regime | When | Pattern |
|---|---|---|
| **Dense thoughts** | Reasoning-heavy tasks (multi-hop QA, fact verification) | Alternate thought / action / observation every step |
| **Sparse thoughts** | Decision-making with many actions (text games, web navigation) | Let the model decide *when* to insert a thought; most steps are pure actions |

The original results use a **frozen PaLM-540B** prompted with just **1–6 hand-written in-context trajectories** — no fine-tuning needed for the headline numbers. (Fine-tuning smaller PaLM-8B/62B on filtered ReAct trajectories improves further and scales better than CoT/Act baselines.)

## Why it mattered (the empirical case)

- **Knowledge-intensive reasoning.** Against a deliberately *weak* 3-action Wikipedia API (`search`, `lookup`, `finish`), ReAct cuts chain-of-thought's hallucination by grounding in retrieval. Best results combine **ReAct + CoT-SC** (internal knowledge *and* external facts): HotpotQA EM 35.1, FEVER acc 64.6.
- **Decision-making, near-zero-shot.** With **1–2** in-context examples, ReAct beats imitation/RL baselines trained on **10³–10⁵** instances: **+34%** absolute success on ALFWorld (71 vs 45 act-only vs 37 IL), **+10%** on WebShop (40 vs 30.1 vs 29.1). The controlled act-only baseline on the *same* trajectories underperforms — **sparse reasoning is what closes the gap**, not just more actions.
- **Interpretability and human correction.** Because thoughts are legible, a human can tell internal knowledge from retrieved fact and inspect *why* the agent acted. Editing a single hallucinating thought realigns the agent — the paper's "new form of human–machine collaboration." This anticipates the wiki's later [[agent-harness|harness]] argument that **human-correction and intent-validation layers** are where production reliability lives.

## ReAct as the ancestor of the agent harness

The structural lineage is direct:

- [[ai-agents]] defines an agent as *"an LLM that autonomously uses tools in a loop"* (via [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe]]/Willison) — **that loop is ReAct.**
- [[agent-harness]] is the runtime engineering of the same reason–act–observe cycle: the harness assembles model + tools + instructions into the loop ReAct first prompted by hand.
- 2026 framework tutorials operationalise it directly: the [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent|Google Cloud Tech / ADK tutorial]] *names ReAct as the definition of a modern agent* and builds a self-correcting multi-agent system (planner / writer / validation-checker / loop agents) whose retry loops are ReAct's exception-handling thoughts made into framework primitives.

What ReAct established as a **prompting trick on a frozen model** in 2022 is now the **architectural default** the wiki's whole agent corpus assumes.

## Related concepts

- [[ai-agents]] — ReAct is the loop at the centre of the agent definition.
- [[agent-harness]] — the production-engineering layer that operationalises the ReAct loop (model + tools + instructions as a runtime).
- [[foundation-models]] — ReAct's substrate; the original work prompts PaLM-540B, a frozen foundation model.
- [[agent-development-lifecycle]] — frameworks (Google ADK) that ship ReAct-style loops as building blocks.

## Debates and supersession

- **Is ReAct still "the" agent loop, or a 2022 special case?** The reason–act–observe cycle remains the load-bearing abstraction in every 2026 wiki source on agents, but modern harnesses add layers ReAct didn't theorise — context engineering, constraints/contracts middleware, telemetry-as-training ([[agent-harness]]). Open question: how much of contemporary agent reliability is *ReAct the paradigm* vs *everything the harness wraps around it*. The wiki's current position: ReAct named the loop; the harness owns the reliability.
- **Reasoning vs acting — which carries the weight?** ReAct's ablations show act-only and reason-only both underperform the interleaving, but the relative contribution is task-dependent (dense thoughts for QA, sparse for decision-making). No single source in the wiki adjudicates a general split.
- **Source independence caveat.** Two of the three citing sources (the paper and its Google Research blog) are the *same* work in different registers; only the [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent|2026 ADK tutorial]] is independent corroboration. Confidence reflects the result's foundational status and four years of downstream adoption rather than three independent replications.
