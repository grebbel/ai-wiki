---
type: source
kind: paper
title: "AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents"
author: ["Haoyu Wang", "Christopher M. Poskitt", "Jun Sun"]
affiliations: ["Singapore Management University"]
arxiv_id: "2503.18666v3"
url: "https://arxiv.org/abs/2503.18666"
venue: "ICSE '26 — 2026 IEEE/ACM 48th International Conference on Software Engineering (April 12-18, 2026, Rio de Janeiro, Brazil)"
publisher: "ACM (ICSE proceedings); arXiv preprint v3"
date_published: 2025-07-31
date_ingested: 2026-05-17
length: "12 pages of ICSE-format main text + references; read in full"
raw: "../../raw/papers/2503.18666v3.pdf"
tags: [agent-harness, llm-agent-safety, runtime-enforcement, dsl, domain-specific-language, langchain, autogen, code-agents, embodied-agents, autonomous-vehicles, guardrails, redcode-exec, safeagentbench, fixdrive, apollo, ICSE-2026, smu, accepted-paper]
relationships:
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "AgentSpec operationalises Chatterjee's *Constraints* layer with a formal DSL. The rule / trigger / check / enforce / end syntax is the executable form of Chatterjee's destructive-verb-detection, workspace-isolation, and intent-validation middleware. AgentSpec is the wiki's first peer-reviewed paper specifically on the Constraints layer."
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Pan's NLAH ingredients include 'failure taxonomy: named failure modes that drive recovery' — AgentSpec gives this layer a formal DSL with named triggers, predicates, and enforcement actions. AgentSpec rules can be the executable artifact Pan's NLAH failure taxonomy compiles down to."
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "AgentSpec's automatic-rule-generation experiment (95.56% precision / 70.96% recall via OpenAI o1) is the empirical anchor for Osmani's ratchet pattern operationalised at runtime — LLM-generated rules from past failures, enforced deterministically."
  - type: supports
    target: responsible-ai
    via: "AgentSpec is the wiki's first peer-track academic source on LLM-agent runtime safety as a formal verification problem with declarative rule syntax + LLM-generated rules + cross-domain enforcement"
  - type: uses
    target: agent-harness
---

# Wang, Poskitt, Sun — *AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents*

A **12-page ICSE '26 paper** (also arXiv:2503.18666v3, dated 31 July 2025) by **Haoyu Wang**, **Christopher M. Poskitt**, and **Jun Sun** at **Singapore Management University**. **Accepted to ICSE '26** (the 2026 IEEE/ACM 48th International Conference on Software Engineering, 12-18 April 2026, Rio de Janeiro, Brazil) — *the wiki's first peer-reviewed primary-source academic paper* on the harness-engineering construct (the other three academic papers in this batch are arXiv preprints). Named as a wiki ingest target by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]] yesterday.

AgentSpec sits at a **different vantage** from the other three academic papers in this batch ([[2026-03-26-pan-natural-language-agent-harnesses|Pan]] / [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee]] / [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|Lou]] all study harness *performance optimisation*; AgentSpec studies harness *safety enforcement*). The wiki's existing harness construct ([[concepts/agent-harness]]) holds **Constraints** as one of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] four layers — AgentSpec provides the **first formal academic treatment of the Constraints layer with a domain-specific language**.

## TL;DR

- **The thesis.** LLM agents are increasingly deployed across diverse domains (software engineering, healthcare, autonomous driving) where unconstrained autonomy creates security, legal, and safety risks. Existing mitigation (model-based safeguards, early-enforcement strategies) **fall short in robustness, interpretability, and adaptability**. AgentSpec is a **lightweight domain-specific language** for specifying and enforcing runtime constraints on LLM agents, with **structured rules** combining **triggers, predicates, and enforcement mechanisms**.
- **Headline empirical claims** (the abstract's punch line).
  - **Prevents unsafe code executions in over 90% of cases** (RedCode-Exec dataset, 25 vulnerability types across 8 domains).
  - **Eliminates *all* hazardous actions in embodied agent tasks** (SafeAgentBench, 10 categories).
  - **Enforces 100% compliance by autonomous vehicles** in 5 out of 8 law-violation scenarios (FixDrive, 6 Chinese traffic laws).
  - **LLM-generated rules** (OpenAI o1 with few-shot examples): 95.56% precision, 70.96% recall for embodied-agent scenarios; identifies 87.26% of risky code; prevents law-breaking in 5/8 AV scenarios in zero-shot. **Computational overhead in milliseconds.**
- **The DSL.** Each rule has 5 parts:
  - `rule <Id>` — keyword + unique identifier
  - `trigger <Event>` — domain event (state_change, before_action, agent_finish, or domain-specific events like `PythonREPL`, `find`/`pick`/`put`/`open` for robotics, `red_light_detected` for ADS).
  - `check <Pred>` — Boolean predicate condition over current state and action.
  - `enforce <Enforce>+` — interventions: `user_inspection` (pause + prompt user), `llm_self_examine` (invoke LLM to self-evaluate), `invoke_action(Params)` (run a predefined action), or `stop` (halt execution).
  - `end` — close the rule definition.
- **Three triggering event types**, formalised:
  - **State change event** — detected when current state s_i differs from previous state s_{i-1}.
  - **Action event** — occurs prior to executing an action a_i. Predicate gets `(s_i, a_i)`.
  - **Agent finish event** — emitted when the agent reports task completion.
- **Implementation as a LangChain hook.** AgentSpec is **built on LangChain 0.13.13** (version explicit). It hooks into three decision points: **before an action is executed** (AgentAction), **after an action produces an observation** (AgentStep), **when the agent completes its task** (AgentFinish). **Framework-agnostic by design** — explicitly demonstrated as portable to **Microsoft AutoGen** (handle_function_call) and **Baidu Apollo** (autonomous vehicle motion planner). Rule parsing via ANTLR4.
- **Worked example: financial transactions.** *"Can you help me transfer $100 to Bob?"* → Agent executes `Transfer` tool call → AgentSpec `@inspect_transfer` rule triggers on `Transfer` event → predicate `!is_to_family_member` checks recipient → `enforce user_inspection` pauses agent for user confirmation. **The pattern**: *user_inspection* on potentially-risky financial / privacy / safety actions.
- **Four research questions, all empirically answered:**
  - **RQ1 (Expressiveness)** — Can AgentSpec rules mitigate risks across multiple domains? **Yes** — Code Agent (RedCode-Exec): over 90% unsafe executions detected and intercepted; **24 of 25 risky categories** the agent attempts to follow risky instructions, all intercepted by AgentSpec rules. Embodied Agent (SafeAgentBench): all 10 hazardous-action categories eliminated, safe tasks drop modestly (58.62% → 54.26%). AV (FixDrive): 100% pass on 5/8 law scenarios; 2/8 fail because LLM-generated rules failed to specify correct behavior; 1/8 partial enforcement.
  - **RQ2 (LLM-generated rules)** — Can LLMs generate effective AgentSpec rules? **Mostly yes, with overfitting concerns** — OpenAI o1 (few-shot): Code 87.26% enforcement on unseen risky scenarios; Embodied 95.56%; AV (zero-shot) 5/8. **Failure mode: over-fitting to specific examples** (e.g., the *"do not pour liquids to prevent unsafe results"* rule banned the pour action entirely, breaking the *"water a houseplant"* benign use).
  - **RQ3 (Generalisability)** — How general are AgentSpec rules? **High** — 25 rules cover 750 risky scenarios (Code), 12 rules cover 250 cases (Embodied), 6 rules cover 8 distinct scenarios (AV).
  - **RQ4 (Runtime overhead)** — Is the overhead acceptable? **Yes — millisecond-scale.** Parsing 1.42 ms; predicate evaluation 2.83 ms (code) / 1.11 ms (embodied); enforcement variable but `stop` is negligible. **Total overhead is ms vs the agent's ~25s (code) or ~9.8s (embodied) execution time** — effectively free.
- **Three failure modes for LLM-generated rules:**
  - **Overfitting** — rules from few-shot examples are too narrow (the *risky-instruction-list*-only rule misses similar patterns).
  - **Over-broad rules** — the *"pour ban"* rule above; one-size-fits-all when the underlying risk is contextual.
  - **Insufficient specification** — AV Law38 (yellow-light behavior) — LLM-generated rule failed to specify correct yellow-light action.
- **Comparison to prior work** (Section 6): contrasts with NeMo (natural-language constraints at dialogue level), llama.cpp + LangChain Expression Language (syntactic pattern-matching), and GuardAgent (LLM interpretation of safety constraints). AgentSpec's unique contribution: **semantic-level properties** (safety, access control, privacy) + **external, developer-defined enforcement model** (vs LLM-interpreted constraints) + **structured rule definitions with flexible enforcement mechanisms**.

## What was actually ingested

Full 12-page ICSE-format PDF (sections 1-8 main text + references). Three domains (Code Agent / Embodied Agent / Autonomous Vehicle) × four research questions. All 25 RedCode risk categories. Full DSL syntax + semantics + LangChain implementation pipeline. The ANTLR4-parsed rule examples.

## Cross-positioning with the wiki

### The Constraints layer formalised

[[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] **Constraints** layer named *"middleware-pattern pre-tool and post-tool hooks (destructive-verb detection; workspace isolation; loop detection; output scoring)"* but did not specify the layer's executable form. **AgentSpec gives Constraints a formal DSL.** The wiki's [[concepts/agent-harness]] page can now point to AgentSpec as the *executable specification language for the Constraints layer*.

| Chatterjee's Constraints layer mechanism | AgentSpec encoding |
|---|---|
| Destructive-verb detection | `rule @destructive_check` / `trigger PythonREPL` / `check is_destructive_cmd` / `enforce user_inspection` |
| Workspace isolation | `rule @scope_check` / `trigger before_action` / `check !is_in_workspace` / `enforce stop` |
| Loop detection | `rule @loop_check` / `trigger agent_step` / `check loop_count > threshold` / `enforce stop` |
| Output scoring | post-action `state_change` triggers with predicate `output_quality(...)` |

### Convergence with the harness-engineering safety layer (Anthropic / Karten failure-mode papers)

[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.'s]] Power Plant Route Loop case study (Appendix B.3) documents three named failure modes — **Context Horizon Limits / Schema Fragility / Feedback Blindness**. AgentSpec's `agent_finish` trigger + `llm_self_examine` enforcement is the formal mechanism that would have caught the Karten failure mode (the agent invoked a schema-mismatched tool 842 times without detecting the mismatch — a state-change-detection-without-anomaly-handling failure). **AgentSpec rules could in principle have intercepted Karten's documented failure.**

### Anthropic primary-source adjacency

[[2025-11-26-anthropic-effective-harnesses-long-running-agents|Anthropic's *Effective Harnesses for Long-Running Agents*]] (Nov 2025, also being ingested in this batch) names four common failure modes for long-running agents — *Claude declares victory too early / leaves environment in buggy state / marks features done prematurely / has to figure out how to run the app*. AgentSpec's DSL is precisely the kind of declarative-rule framework that could enforce the corrective patterns Anthropic prescribes (read progress notes; only mark features after testing; commit to git with descriptive messages). **AgentSpec + Anthropic vendor patterns = a deployable safety enforcement stack** — worth tracking whether a future Anthropic SDK incorporates DSL-style runtime constraints.

### LangChain anchor

AgentSpec's prototype is **on LangChain 0.13.13**. This makes it the wiki's first source that explicitly anchors a published academic safety system on LangChain — strengthening the [[LangChain]] entity page as the deployment substrate for safety-critical academic work. Authors explicitly note framework-agnostic design (porting to AutoGen + Apollo demonstrated).

## Named entities (this ingest)

- [[Haoyu Wang]], [[Christopher M. Poskitt]], [[Jun Sun]] — Singapore Management University. **All first mentions. Dangling.** Jun Sun is a well-known formal-methods researcher at SMU.
- [[Singapore Management University]] — first wiki source from SMU. **Dangling.**
- [[ICSE 2026]] — the 2026 IEEE/ACM 48th International Conference on Software Engineering. **First mention as a venue.**
- [[Microsoft AutoGen]] — already in wiki ecosystem.
- [[Baidu Apollo]] — autonomous-driving stack. **First mention.**
- [[RedCode-Exec]] — code agent risk benchmark (Guo et al. 2024). **First mention.**
- [[SafeAgentBench]] — embodied agent safety benchmark (Yin et al. 2024). **First mention.**
- [[FixDrive]] — autonomous-vehicle law-violation benchmark (Sun et al. 2025). **First mention.**

## Source-quality notes

- **Genre**: peer-reviewed conference paper (ICSE '26). **The first peer-reviewed paper in the wiki's harness-engineering cluster** — all prior academic sources have been arXiv preprints.
- **Empirical-anchor count**: high — 750 code-risk scenarios + 250 embodied scenarios + 8 AV scenarios + LLM-generated-rules ablation.
- **Reproducibility posture**: code released at github.com/haoyuwang99/AgentSpec (per reference [1]). Datasets cited (RedCode-Exec / SafeAgentBench / FixDrive).
- **Confidence: 0.92.** Per Lifecycle: single source +0.05 for peer-reviewed publication (vs arXiv preprint) +0.05 for honest failure-mode reporting (LLM-generated rules overfit; AV failures specified) +0.05 for explicit overhead numbers in ms = 0.92. The peer-review status pushes this above the four academic preprints in this batch.

## Open questions

- **Composability of rules.** Section 6.3 names this as a limitation — *"AgentSpec currently performs deterministic enforcement at discrete execution checkpoints... future work could be extending AgentSpec with probabilistic enforcement mechanisms that incorporate model-based foresight."* The wiki's [[concepts/agent-harness]] page already tracks Karten's CRUD-edit on harness components; whether AgentSpec rules can be composed CRUD-style by a Refiner is the obvious unification target.
- **Integration with Pan's NLAH failure taxonomy.** Pan's NLAH includes a "failure taxonomy" ingredient — AgentSpec rules could be the executable form of that taxonomy. No source has yet demonstrated this composition.
- **Cost of LLM-generated rules at scale.** 87.26% / 95.56% / 5-of-8 precision is strong, but the cost of generating rules with o1 + few-shot examples isn't reported. For deployment-scale safety enforcement (thousands of distinct risk categories), this matters.
- **Probabilistic / trajectory-based safety analysis.** AgentSpec's discrete-checkpoint enforcement is its main limitation — *"does not reason about long-term consequences of current actions"*. Future work could extend with DTMC-style trajectory analysis.
