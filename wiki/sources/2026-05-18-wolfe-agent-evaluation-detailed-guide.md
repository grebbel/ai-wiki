---
type: source
kind: article
title: "Agent Evaluation: A Detailed Guide"
subtitle: "Best practices and common patterns for effectively evaluating AI agents"
author: ["Cameron R. Wolfe"]
publisher: "Deep (Learning) Focus (Substack)"
section: "Deep (Learning) Focus newsletter"
url: "https://cameronrwolfe.substack.com/"
date_published: 2026-05-18
date_ingested: 2026-05-18
length: "~56-page PDF / ~7,000 words / 13-reference bibliography"
raw: "../../raw/articles/Agent Evaluation_ A Detailed Guide.pdf"
tags: [agent-evaluation, agent-harness, agent-scaffold, evaluation-harness, llm-as-judge, tau-bench, terminal-bench, pass-at-k, pass-hat-k, swiss-cheese-evaluation, react-framework, multi-agent-systems, context-engineering, compaction, model-based-graders, code-based-graders, outcome-driven-evaluation, cameron-wolfe, deep-learning-focus, evaluation-suite]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: agent-harness
    via: "Wolfe explicitly equates *scaffold* with *harness* via the Anthropic Demystifying-Evals quote (*'An agent harness (or scaffold) is the system that enables a model to act as an agent... when we evaluate an agent, we're evaluating the harness and the model working together'*). This is the wiki's first source treating *eval suite + eval harness* as a load-bearing harness primitive, complementing the engineering-discipline framings of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] / [[2026-05-15-osmani-agent-harness-engineering|Osmani]] with the eval-discipline framing."
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "Wolfe's Terminal-Bench 2.0 + τ-bench case studies are the same empirical-benchmark cluster the Prompt Engineering YouTube source ablations on; Wolfe gives the *evaluation construction* vantage on the benchmark family the wiki has only held from the *harness-engineering* side"
  - type: supports
    target: 2024-12-19-anthropic-building-effective-agents
    via: "shares the load-bearing definition *'an agent is an LLM that autonomously uses tools in a loop'* and the workflow-vs-agent distinction; Wolfe extends the architectural taxonomy with an evaluation taxonomy (graders / trials / transcripts / outcomes)"
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "Wolfe cites Anthropic's harness write-up [1] as the primary source for the *scaffold = harness* equivalence; the wiki page is the canonical record of that Anthropic write-up"
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Karten's Continual Harness paper formalised *H = (p, G, K, M)* over the same benchmark family (Terminal-Bench, τ-bench) Wolfe uses as case studies; Wolfe's *evaluation harness* and Karten's *(p, G, K, M)* are complementary formalisations of the same construct from eval-side vs academic-side"
  - type: supports
    target: 2026-02-11-lopopolo-codex-harness-engineering
    via: "Lopopolo's OpenAI Codex case study and Wolfe's OpenAI guide reference [3] (*A practical guide to building agents*) anchor the same OpenAI-side eval / scaffold tradition; both treat *the agent system surrounding the model* as the load-bearing engineering artifact"
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Osmani's *harness engineering as discipline* and Wolfe's *agent evaluation as discipline* are the two halves of the same practitioner field guide — Osmani's *ratchet* (*every mistake becomes a rule in AGENTS.md*) is operationally what Wolfe calls *inspect, iterate, and maintain the benchmark* (step 7 of the roadmap)"
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "Husain's spreadsheet-first practitioner workflow (open-coding → axial-coding → pivot-table failure counts → LLM-as-judge calibration via TPR/TNR) is the *daily-workflow* counterpart to Wolfe's *textbook taxonomy*. Both converge on (a) human evaluation as the calibration north star, (b) LLM-as-judge as the scalability instrument that must be calibrated against humans, (c) eval as a *living artifact* that evolves with discovered failure modes. Husain gives the workflow; Wolfe gives the architecture."
  - type: supports
    target: 2026-03-20-huggingface-agentic-evaluations-workshop
    via: "the HuggingFace workshop frames the *capability-reliability gap* (Narayanan) and demonstrates GAIA-2 on the ARE simulated environment; Wolfe names GAIA / GAIA-2 in his benchmark roundup. Both treat agentic benchmarks as *living artifacts* and converge on outcome-driven evaluation, LLM-as-judge with rubrics, and the limitations of single-metric scoring."
---

# Wolfe — Agent Evaluation: A Detailed Guide

A **~7,000-word, 13-reference practitioner field guide** to agent evaluation by [[Cameron R. Wolfe]] (Deep Learning Ph.D.; Staff Research Scientist at [[Netflix]]; author of the *Deep (Learning) Focus* newsletter). Published **18 May 2026** on Substack. The article opens at the eval layer (single-turn benchmarks vs. agent eval), threads through the architectural prerequisites (agent fundamentals → scaffolds → context engineering), and lands on a 7-step practitioner roadmap for building agent evaluations. It is the wiki's **first source whose primary contribution is the eval-discipline framing** of the agent construct, complementing the engineering-discipline framings of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] / [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] / [[2026-05-15-osmani-agent-harness-engineering|Osmani 2026]] / [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]].

> *"An agent harness (or scaffold) is the system that enables a model to act as an agent... When we evaluate an agent, we're evaluating the harness and the model working together."* — Anthropic *Demystifying evals for AI agents*, quoted in [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]]

## TL;DR

- **The category split**: traditional LLM evaluation uses static single-turn benchmarks; **agent evaluation runs over multiple chat turns, tools, and an external environment**, demanding an *eval harness* that mirrors the *production harness* in scaffold, tools, and environment. *"The agent should ideally use the same scaffold, tools, and environment that are used in production during the evaluation process."*
- **The agentic loop and three components**: (1) underlying LLM (or reasoning model), (2) tools the agent calls, (3) instructions for the agent. *"The simplest definition of an agent is an LLM that autonomously uses tools in a loop."* The ReAct (Reasoning + Action) framework is the canonical loop variant.
- **Tool-use evaluation has four named metrics**: **invocation accuracy** (did the agent call a tool at all), **selection accuracy** (did it pick the right tool), **structural accuracy / schema validity** (did the call format work), **trajectory accuracy** (did the sequence of calls match ground truth). Outcome-oriented evaluation focuses on the final answer instead of the tool path.
- **Multi-agent systems**: two canonical patterns — **manager setup** (central orchestrator delegates) and **decentralized setup** (peers hand off via tool calls). *"We should expand to multi-agent systems only when necessary"* — bloated single-agent instructions / overlapping tools are the canonical signals.
- **Context engineering as agent-centric prompt engineering**: dynamic context (tool-driven retrieval rather than pre-loaded RAG) + **three compaction patterns** (summarization, tool-result clearing, note-taking) to fight *context rot* across long-horizon agentic loops.
- **The five evaluation components** every agent eval shares: **tasks** (individual test cases with input + success criteria) → **trials** (one execution attempt per task) → **transcript / trajectory** (full record of one trial's tool calls, reasoning, outputs) → **outcome** (final environment state) → **graders** (quality checks over transcript + outcome).
- **Three grader families**, each with named strengths and weaknesses:
  - **Human evaluation** — gold standard for quality, expensive and slow; used to *calibrate* model-based graders.
  - **Code-based graders** — string match / binary tests / static analysis / outcome verification / tool-call verification / transcript analysis. Fast, cheap, objective, reproducible, easy to debug — but brittle and lacking nuance.
  - **Model-based graders (LLM-as-Judge)** — pairwise (preference) / direct assessment (pointwise Likert) / reference-guided scoring; itemized **rubrics with dozens of criteria** improve scoring reliability. Flexible and scalable; non-deterministic and bias-prone; require calibration against human judgment.
- **The Swiss-cheese strategy**: combine automated evals (fast iteration) + production monitoring (ground truth, but reactive) + A/B testing + user feedback (thumbs up/down) + cost metrics. *"Although a single evaluation will not catch every error, the likelihood of any error reaching production decreases with more layers of complementary evaluations."*
- **Two benchmark case studies that anchor the field as of mid-2026**:
  - **τ-bench / τ²-bench / τ²-bench-verified / τ³-bench** (Sierra) — **dual-control conversational agent benchmarks** across retail / airline / telecom / banking domains, with LLM-simulated users, modular databases + APIs + policy documents + task instances. Introduces **Pass^K** (probability *all* K trials succeed) as a stricter alternative to Pass@K (at least one of K succeeds). *"Most agents perform poorly in terms of Pass^K, even for relatively modest values of K."* τ³-banking (~700-document knowledge base) is **3–4× harder** than predecessor domains.
  - **Terminal-Bench / 2.0 / 3.0** — **terminal as a realistic agentic environment**; each task = instruction + Docker image + test set + oracle solution; **Harbor harness** standardises agent execution. Terminal-Bench 2.0 has **89 tasks** crowdsourced from 229 contributions across 93 contributors, **3 hours of reviewer time per task**. Software engineering dominates task categories (29%). Best model **GPT-5.2 at 62.9%**; Kimi K2 Thinking at 35.7%. Near saturation; Terminal-Bench 3.0 in development.
- **The 7-step roadmap for building your own agent evaluation**:
  1. **Define success** — outcome goals (final state) + process goals (transcript components).
  2. **Collect a small task set** — 10–20 realistic tasks; manual vibe checks during this phase.
  3. **Create useful tasks** — unambiguous, repeatable, capturing prominent failure modes.
  4. **Provide ground truth and references** — reference solutions / known-good trajectories anchor grader correctness.
  5. **Configure graders** — start with code-based deterministic checks; escalate to model-based for subjective criteria; always calibrate against human reviewers.
  6. **Build the evaluation harness** — runs the agent in a realistic-but-controlled setup, collects transcript + outcome, starts each trial from a fresh environment.
  7. **Inspect, iterate, and maintain the benchmark** — eval suites are living artifacts. *"τ²-bench-verified shows how human validation can uncover task-quality issues and improve benchmark reliability."*

## What was actually ingested

Full 56-page PDF of the Substack post read end-to-end: introduction → Fundamentals of Agent Systems → Multi-Agent Systems → Context Engineering → Agent Scaffolds → Common Patterns in Agent Evaluation (components + grader types + Swiss Cheese) → Agent Evaluation Case Studies (τ-bench family + Terminal-Bench family + benchmark roundup) → A Roadmap for Agent Evaluation → Bibliography (13 entries). All in-text figure references, captions, code listings (LiteLLM agent loop from tau-bench; Qwen3 special-token tool-calling template), and tables (Terminal-Bench task completion times, Pass^K per-model performance) captured semantically. The article's two interleaved sidebar callouts (Wolfe's prior pieces: *Demystifying Reasoning Models* Feb 2025 + *AI Agents from First Principles* June 2025) noted as related-but-not-ingested.

## Key claims in detail

### The agent definition Wolfe uses

> *"The simplest definition of an agent is an LLM that autonomously uses tools in a loop."*

Wolfe's three-component agent: (1) underlying **LLM** (often a **reasoning model** for multi-step decomposition), (2) **tools** (APIs / CLIs / [[MCP]] servers / computer-use primitives) wrapped via tokenizer-level special tokens (Qwen3 `<tool_call>` / `<tool_response>` example given), (3) **instructions** (system prompt — *"clear as possible, clarify edge cases via explicit rules or concrete examples, specify the exact actions expected of the agent"*). The agent system runs in a *while loop* until an **exit condition** is met (final-answer structure / no tool calls / max steps / specific tool / terminal error).

Tool-use evaluation is decomposed into four named metrics (a sharp taxonomy not previously isolated in the wiki):

| Metric | What it measures |
|---|---|
| **Invocation accuracy** | Did the agent call a tool when it should (or refrain when it shouldn't)? |
| **Selection accuracy** | Did the agent call the *correct* tool from the available set? |
| **Structural accuracy / schema validity** | Is the tool-call format and argument structure valid? |
| **Trajectory accuracy** | Does the sequence of tool calls match a ground-truth trajectory? |

### Agent scaffolds and the eval-side scaffold = harness equivalence (load-bearing for the wiki)

Wolfe introduces *agent scaffold* as an alias for *agent harness*, citing the Anthropic *Demystifying Evals* article directly:

> *"An agent harness (or scaffold) is the system that enables a model to act as an agent... When we evaluate an agent, we're evaluating the harness and the model working together."* — Anthropic, quoted in [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]]

The scaffold encompasses *the agent's interface with the environment, the prompting strategy, the tools available and their interfaces, the structure of the agent system (e.g., sub-agents), and the context management strategy.* The Terminus agent scaffold (keystroke-emitting tmux session inside a Docker sandbox) is the worked example. The **decoupling claim** Wolfe inherits from Anthropic — *poor performance may stem from deficient model capabilities, poor scaffold design, or both* — is the wiki's first explicit eval-side restatement of the *model + harness* decomposition that [[2026-05-15-osmani-agent-harness-engineering|Osmani 2026]] frames as the *category-error fix*.

### Context engineering as agent-centric prompt engineering

Wolfe quotes Anthropic [2] (*Effective context engineering for AI agents*): *"We view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes. Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference."* Three load-bearing operational moves:

- **Dynamic context vs static RAG**: agents use tool calls to *progressively disclose* relevant context, instead of pre-loading everything via RAG at the start. Tools should be designed to be *token-efficient* — read specific line ranges, preview file heads, avoid full-file loads.
- **Three compaction patterns**:
  - *Summarization* — generate a summary of a long conversation; reinitialize a fresh context window with the summary.
  - *Tool result clearing* — remove older tool-call output payloads from the agent's history.
  - *Note-taking* — write notes to an external store (e.g., markdown file) the agent can later retrieve. *"Note-taking is not just a compaction technique — the agent can maintain notes while solving a problem even without performing compaction."* (Wolfe cites *this paper* — link points to the Note-taking-agents arXiv work.)
- **Context rot as universal failure mode**: long contexts degrade recall regardless of the model's nominal context-window size. This converges with the wiki's [[agent-harness]] *Context-rot countermeasures* primitives ([[2026-05-15-osmani-agent-harness-engineering|Osmani]] names compaction + tool-call offloading + Anthropic full-context-resets in the same operational slot).

### The five evaluation components (canonical taxonomy)

Wolfe's most-portable contribution. Every agent eval shares:

1. **Tasks** — individual test cases with predefined input + output criteria.
2. **Trials** — one attempt at solving a task; multiple trials per task to handle non-determinism.
3. **Transcript / trace / trajectory** — the full record of one trial, including outputs, tool calls, reasoning steps, intermediate outputs.
4. **Outcome** — the final state of the external environment after a trial. *Distinct from outputs*: *"If we are testing the ability of an agent system to book a reservation, the desired outcome is a confirmed reservation. An agent may write 'The restaurant is booked!' without actually achieving this outcome."*
5. **Graders** — quality checks over transcript + outcome.

Plus a sixth component named separately: the **evaluation harness** that wraps all of the above and runs the agent end-to-end. *Eval harness ≠ production harness*, but ideally they share *the same scaffold, tools, and environment*.

### The three grader families and the Swiss-cheese strategy

The article's most-cited piece of practical guidance is the trade-off table among grader types. Wolfe is explicit that *"we should rely solely on model-based graders — it is better to use multiple grading techniques together."* The recommended composition:

- **Human evaluation** = north star; used to *calibrate* the others. Methods: SME review / crowdsourcing / spot-check sampling / A/B testing / inter-annotator agreement.
- **Code-based graders** = fast, cheap, deterministic. Methods: string match (exact/regex/fuzzy) / binary tests (fail-to-pass, pass-to-pass) / static analysis (lint, type, security) / outcome verification / tool-call verification / transcript analysis (turns, tokens).
- **Model-based graders** = LLM-as-Judge. Three named scoring setups: **pairwise** (judge picks the better of two responses) / **direct assessment** (1–10 Likert) / **reference-guided** (judge has a golden answer). Itemized rubrics with dozens of criteria improve reliability.

The **Swiss-cheese strategy** stacks complementary layers: automated evals (consistent baseline + regression catching) + manual transcript review + early-access programs (nuanced failures) + production monitoring + A/B testing + user feedback (rare edge cases at scale). *"The best approach is to combine all of these techniques."*

### Benchmark case study 1 — the τ-bench family (Sierra)

Wolfe's first deep case study. The τ-bench family (Yao et al. 2024 / Barres et al. 2025 / 2026) is the agent-benchmark cluster that **operationalises the eval discipline for dialogue + tool-use agents** across customer-service-shaped domains:

- **τ-bench** — retail + airline domains. Each domain: JSON databases + Python API tools + Markdown policy documents + JSON task instances + LLM-simulated user (signals end with `###STOP###`). Tasks have ground-truth database write actions + ground-truth outputs. Pass@K (probability of at least one success in K attempts) was the original metric; Pass^K (all K succeed) introduced as the *consistency* metric. *"Pass^K declines quickly as K increases."*
- **τ²-bench** — adds the **telecom** domain and a **dual-control setup** (both user and agent have tools and interact with shared environment). Atomic subtasks composed of *initialization functions + solution tools + assertions*; 114 telecom tasks created from 2,285 candidates via compositional sampling + model-in-the-loop refinement.
- **τ²-bench-verified** (Cuadron et al. 2025, SABER) — manual human verification across all τ²-bench domains uncovered **three named data-quality issues**: policy compliance violations, conflicting/incorrect data, ambiguous instructions. After fixes, top models cross 80% Avg@5.
- **τ³-bench** (Sierra 2026) — adds **τ-banking** domain with a **~700-document knowledge base**, forcing autonomous information retrieval. **3–4× harder** than predecessor domains: best model 25.5%. Terminal-based retrieval outperforms standard retrieval (BM25 / Qwen3-Emb / text-emb-large) by 2.4–3.6 pp on average.

The τ-bench code listing Wolfe inlines (the Sierra-published `solve()` loop using `litellm.completion()`) is the wiki's first concrete worked example of *the agentic-loop-as-Python-function* — directly compatible with [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]]'s *(p, G, K, M)* formalisation.

### Benchmark case study 2 — the Terminal-Bench family

Wolfe's second deep case study. Frames the **terminal as the realistic agentic environment** for frontier-capability evaluation. Each task = **instruction + Docker image + test set + oracle solution**; tasks use the **Harbor task format**; agents use the **Harbor harness** for standardised execution across different agents/environments/tools. *"Terminal-Bench is an outcome-driven framework where each agent is free to accomplish the task using a variety of approaches."*

**Terminal-Bench 2.0** — 89 carefully-curated tasks from 229 contributions across 93 contributors. Curation gated on **specificity** (instructions describe all viable end states, tests pass iff container in viable state) + **solvability** (oracle solution passes the tests) + **integrity** (task not solvable by cheating). The **7-stage audit pipeline** (4 pre-merge: contributor submission + automated CI & LLM checks + expert human review + accept/reject; 3 post-merge: Terminus model experiments + manual trajectory audit + adversarial exploit audit) takes **~3 reviewer-hours per task** — multiple hundreds of person-hours invested in review alone.

Task distribution is software-engineering-dominated (29%) but covers data science / security / scientific computing / file ops / debugging / data processing / model training / mathematics / ML / games / video processing / data querying / optimization / personal assistant. Most tasks take **<1 day for experts** (95.9%); **>1 week for junior engineers** (4.1% of tasks).

**Agent results** establish the wiki's first **scaffold-explicit leaderboard**: GPT-5.2 (Codex CLI) 62.9% → Claude Opus 4.5 (Terminus 2) 58% → Gemini 3 Pro (Terminus 2) ~57% → Kimi K2 Thinking (Terminus 2) 35.7% → GPT-OSS-20B (Mini-SWE-Agent) ~5%. *"Performance on Terminal-Bench is dependent upon the agent scaffold being used... model capabilities tend to have a larger impact on performance than the scaffold being used. However, the scaffold does meaningfully influence performance, and the analysis in [12] only considers reasonable scaffolds — findings may differ given a poorly-designed scaffold with functionality gaps."* **Closed models consistently beat open models.**

### The 7-step roadmap (Wolfe's load-bearing original contribution)

The roadmap is the article's most-portable artifact — a step-by-step workflow for building an agent eval suite from scratch. Reads as the *eval-side* counterpart to [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *ratchet* and *AGENTS.md hygiene* rules on the engineering side:

1. **Define success** — outcome goals (final state) + process goals (transcript components). *"Many recent agent benchmarks are heavily outcome-oriented."*
2. **Collect a small task set** — 10–20 manually-curated initial tasks; expand over time as failure modes are discovered. Keep legacy tasks in a regression set.
3. **Create useful tasks** — unambiguous, repeatable, capturing prominent failure modes. *"An agent may be failing due to poor task specification rather than any gap in its capabilities."*
4. **Provide ground truth and references** — reference solutions / known-good trajectories anchor grader correctness (mirroring Terminal-Bench's oracle-solution design).
5. **Configure graders** — start simple (code-based deterministic); escalate to model-based for subjective criteria; calibrate human-vs-LLM-vs-code agreement.
6. **Build the evaluation harness** — runs agent in realistic-but-controlled setup; collects transcript + outcome; **starts each trial from a fresh environment** (no shared state). *Use production-equivalent scaffold + tools + environment whenever possible.*
7. **Inspect, iterate, and maintain the benchmark** — eval suites are *living artifacts*. *"Agent evaluations can become saturated quickly... we should treat evaluation suites as living artifacts that continually improve in difficulty, diversity, and reliability."*

### Benchmark roundup (for wiki cross-reference)

Wolfe names the wider 2026 agent-evaluation landscape:

- **GAIA / GAIA-2** — general assistant benchmarks (reasoning + browsing + tool use + multimodal).
- **AgentCompany** — knowledge-work benchmark simulating a small software company.
- **WorkArena** — enterprise software workflows sourced from ServiceNow.
- **OSWorld** — computer-use benchmark in real desktop environments. (Plus **OfficeBench**, **MobileBench**.)
- **MLE-Bench** — autonomous ML experimentation; Kaggle problems. (Plus **PostTrainBench**, **MLGym**.)
- **PaperBench** — reproducing AI research papers from arXiv.
- **SpreadsheetBench** — Excel-based agent tasks.
- **HIL-Bench** — human-in-the-loop benchmark; *can the agent decide when to ask humans for clarification*.
- **GDPval** — economically-valuable task benchmark.

This is the wiki's first source naming a wider benchmark landscape beyond τ-bench / Terminal-Bench — each named benchmark is a deferred-ingest candidate.

## Linked entities and concepts

**Authors / individuals named:**

- [[Cameron R. Wolfe]] — author. Deep Learning Ph.D.; Staff Research Scientist at Netflix; runs the *Deep (Learning) Focus* newsletter (hundreds of paid subscribers). **First mention in the wiki.** *Dangling pending second source.*
- **Shunyu Yao** — first author of the τ-bench paper (Yao et al. 2024) and ReAct paper (Yao et al. 2022). **First mention.** *Dangling.*
- **Victor Barres** — first author of τ²-bench (2025) and τ³-bench (2026). **First mention.** *Dangling.*
- **Alejandro Cuadron** — first author of SABER / τ²-bench-verified (2025). **First mention.** *Dangling.*
- **Mike A. Merrill** — first author of Terminal-Bench (Merrill et al. 2026). **First mention.** *Dangling.*

**Organisations / venues / products named:**

- [[Anthropic]] — already in the wiki ecosystem. References [1] *Demystifying evals for AI agents*, [2] *Effective context engineering for AI agents*, [4] *Effective harnesses for long-running agents*, [13] *How we built our multi-agent research system* — four distinct Anthropic engineering-blog primary sources cited.
- [[OpenAI]] — already in the wiki ecosystem. References [3] *A practical guide to building agents*, [6] *Evaluation Best Practices*.
- **Netflix** — Wolfe's employer. **First mention.** *Dangling.*
- **Substack / Deep (Learning) Focus** — newsletter venue. **First mention** for both. *Dangling.*
- **Sierra** — research org behind τ-bench / τ²-bench / τ³-bench. **First mention.** *Dangling.*
- **Terminal-Bench** — benchmark + framework. **First-class wiki mention** as the empirical anchor for [[agent-harness|agent-harness]]'s Pan-et-al-Top-30-to-Top-5 result. Wolfe expands the wiki's grasp on the construction process.
- **Kimi K2 Thinking** / **GPT-5.2** / **Claude Opus 4.5** / **Gemini 3 Pro** / **Qwen3** — models cited in benchmark results.
- **LiteLLM** — OpenAI-compatible model-API abstraction; the τ-bench code uses it. **First mention.** *Dangling.*
- **Terminus** — agent scaffold framing the Terminal-Bench front cover. **First mention.** *Dangling.*

**Bibliography references (deferred-ingest candidates for [[agent-harness]] / [[ai-agents]] / [[concepts/llm-wiki|llm-wiki]] clusters):**

- [1] Anthropic, *Demystifying evals for AI agents* (2026) — the load-bearing eval-side primary that Wolfe synthesises.
- [2] Anthropic, *Effective context engineering for AI agents* (2025).
- [4] Anthropic, *Effective harnesses for long-running agents* (2025).
- [5] Yao et al., *ReAct: Synergizing reasoning and acting in language models* (arXiv:2210.03629, 2022) — load-bearing foundational paper.
- [6] OpenAI, *Evaluation Best Practices* (2026).
- [7] Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (NeurIPS 2023).
- [8] Yao et al., *τ-bench* (arXiv:2406.12045, 2024).
- [9] Barres et al., *τ²-Bench* (arXiv:2506.07982, 2025).
- [10] Cuadron et al., *SABER* (arXiv:2512.07850, 2025).
- [11] Barres et al., *τ³-Bench* (Sierra, 2026).
- [12] Merrill et al., *Terminal-Bench* (arXiv:2601.11868, 2026).
- [13] Anthropic, *How we built our multi-agent research system* (2025).

## Cross-positioning with the wiki

- **With [[agent-harness]]** — Wolfe is the wiki's **first eval-discipline source** on the harness construct. The Anthropic *scaffold = harness* equivalence Wolfe inherits ratifies a vocabulary the wiki has held implicitly. The five-component eval taxonomy (tasks / trials / transcripts / outcomes / graders) + eval-harness construct should be folded into the agent-harness concept page's §Components or a new §Evaluation section. *"When we evaluate an agent, we're evaluating the harness and the model working together"* belongs on the concept page as a load-bearing claim about what *evaluating the harness* means.
- **With [[ai-agents]]** — Wolfe's three-component model (LLM + Tools + Instructions) and *"agent = LLM that autonomously uses tools in a loop"* definition restate [[2024-12-19-anthropic-building-effective-agents|Anthropic 2024]]'s workflows-vs-agents distinction at the eval-design altitude.
- **With [[agentic-engineering]]** — Wolfe's 7-step roadmap is the eval-discipline counterpart to [[2026-05-15-osmani-agent-harness-engineering|Osmani 2026]]'s engineering-discipline rule-set. Step 7 (*inspect, iterate, maintain*) is the eval-side ratchet.
- **With [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube 2026]]** — Wolfe's Terminal-Bench results table is the *outcome-side* anchor to that video's *ablation-side* result. The Pan-et-al *Top 30 → Top 5 by changing only the harness* claim Wolfe doesn't repeat directly but the broader Terminal-Bench-as-empirical-anchor story is consistent.
- **With [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al. 2026]]** — Karten's *(p, G, K, M)* formalisation is the academic counterpart; Wolfe's *evaluation harness* is the practitioner counterpart. Same construct, different vantages.
- **With [[concepts/llm-wiki|llm-wiki]] cluster** — Wolfe's *context engineering = agent-centric prompt engineering* + Anthropic [2] are directly compatible with [[syntheses/is-rag-dead|the is-RAG-dead synthesis]]: RAG is being retired as a term but the technique persists as a context-engineering primitive; agents use dynamic context (progressive disclosure via tools) rather than static pre-loaded RAG.
- **With [[strategic-foresight]]** — Wolfe's *benchmark saturation* observation (*Terminal-Bench 2.0 is near saturation with recent model releases*) is a concrete *adoption-speed-vs-capability-frontier* data point.
- **With [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain 2025]]** — Husain's spreadsheet-first practitioner workflow is the *daily-workflow* counterpart to Wolfe's *textbook taxonomy*. Husain anchors *human evaluation as the calibration north star* and *LLM-as-judge agreement metrics (TPR / TNR)*; Wolfe ratifies both as Step 5 of the 7-step roadmap (*Configure graders... always monitor the level of agreement between LLM judges and human experts*). The two sources together cover *how to think about eval* (Wolfe) + *how to actually do it on Monday morning* (Husain).
- **With [[2026-03-20-huggingface-agentic-evaluations-workshop|HuggingFace 2026]]** — the HuggingFace workshop's *capability-reliability gap* (Narayanan) and GAIA-2 / ARE simulated environment are the *community-eval / sim-to-real-gap* vantage. Wolfe names GAIA / GAIA-2 in his benchmark roundup but doesn't expand. The HuggingFace source supplies the depth on *why agentic benchmarks need their own reliability dimension separate from capability*; Wolfe supplies the construction process for those benchmarks.

## Source-quality notes

- **Genre**: practitioner field-guide essay on Substack; long-form (~7,000 words); 13-reference bibliography; original to Wolfe; sponsored newsletter context (paid-subscriber tier mentioned but the article is free).
- **Speaker authority**: Cameron R. Wolfe is a recognised AI educator with prior pieces *Demystifying Reasoning Models* (Feb 2025) and *AI Agents from First Principles* (June 2025); Deep Learning Ph.D.; Staff Research Scientist at Netflix. Track record is strong on AI-research-translation/explainer genre, not on running primary studies.
- **Empirical grounding**: Wolfe synthesises and contextualises results from peer-track and vendor-published benchmarks; he does not run his own benchmarks. The benchmark results he cites (τ³-bench, Terminal-Bench 2.0 leaderboard) are second-hand from the cited bibliography. Treat as **synthesis-grade**, not primary-empirical.
- **Confidence: 0.75**. Per [[lifecycle|Lifecycle]] heuristic: single source, +0.05 for credentialed author + recognised publishing channel, +0.05 for high citation density (13 distinct primary references — strongest single-source bibliography in the [[agent-harness]] cluster), capped below 0.85 because the source is a synthesis essay, not a primary empirical study.

## Open questions

- **The Anthropic [1] *Demystifying evals for AI agents* article is the most-cited single primary source in Wolfe's bibliography** — and the wiki does not yet hold it directly. Deferred-ingest target; landing it would lift this source from synthesis-grade to dual-anchored (Wolfe's synthesis + Anthropic's primary).
- **τ-bench / τ²-bench / Terminal-Bench primary papers** (arXiv refs [8], [9], [10], [11], [12]) are all deferred-ingest candidates. Their landing would substantially deepen [[agent-harness]]'s empirical anchor (currently held second-hand via [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]] and [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]]).
- **The benchmark roundup section** (GAIA, AgentCompany, WorkArena, OSWorld, MLE-Bench, PaperBench, SpreadsheetBench, HIL-Bench, GDPval) is a *named-but-not-ingested* landscape. Each item is a candidate deferred-ingest if the wiki extends into specific agent-application domains.
- **The Sierra research-org cluster** (Yao + Barres + Cuadron) is an emerging agent-benchmarking group worth tracking. *Sierra* is dangling pending a second wiki source mentioning the org.
