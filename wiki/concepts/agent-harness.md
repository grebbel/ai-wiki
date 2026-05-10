---
type: concept
aliases: ["agent harness", "harness", "AI agent harness", "agent runtime", "agent runtime layer"]
tags: [agent-harness, ai-agents, ai-engineering, harness-frameworks, context-management, constraints, contracts, telemetry, llm-non-determinism]
confidence: 0.90
last_confirmed: "2026-05-09"
source_count: 8
relationships:
  - type: part-of
    target: ai-agents
    via: "the runtime engineering layer that wraps a foundation model to turn it into a production-grade agent"
  - type: uses
    target: foundation-models
    via: "the harness wraps a (rented, swappable) foundation model in a runtime that adds context/constraints/contracts/compounding"
---

# Agent Harness

The **runtime engineering layer that lives between a foundation model and the user** in any production [[ai-agents|AI agent]] system. The harness wraps the model with context management, permission/guardrails, state and memory, tool execution, retry/error handling, human-in-the-loop, observability, and (in mature systems) a self-tuning meta-learning loop. The construct emerged in late 2025 / early 2026 as practitioner vocabulary; by April–May 2026 it had become the dominant frame for *what production AI engineering actually is*, with at least seven wiki sources engaging the term substantively — including primary-source vendor announcements from [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic]] (8 April 2026) and [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google]] (22 April 2026) that productize the harness/runtime layer as a hosted service or CLI toolkit, plus the wiki's first **empirical anchor** ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube, 4 May]]) bringing ablation data and a **transfer-across-models** finding, and the wiki's first **paradigm-vocabulary anchor** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy at Sequoia AI Ascent, 29 April]]) placing the harness inside the broader [[software-3.0]] computing paradigm and naming the practitioner discipline that wields it: [[agentic-engineering]].

The wiki treats agent harness as a **distinct concept** from [[ai-agents]] (the technology + deployment progression), [[foundation-models]] (the substrate the harness wraps), and [[generative-ai]] (the broader application class). The harness is *specifically* the application-layer software around the model.

## Working definition

An **agent harness** is the software that converts a foundation model from an inference endpoint into a system that can pursue goals reliably in production. The minimum viable harness manages:

- **Context** — assembling the right prompt + state for each request, often as a structured document with stable (KV-cacheable) and dynamic parts.
- **Constraints** — pre-tool and post-tool middleware that validates *intent* (not just output format), enforces workspace isolation, detects loops, and scores outputs against quality criteria.
- **Contracts** — formal, evaluable specifications of what "successful output" means for a workflow, calibrated to the inputs available; enables debuggable agent behaviour.
- **Compounding** — structured telemetry that feeds a self-tuning meta-learning loop adjusting *harness configuration* (not the model, which is rented and frozen).
- **Tool execution + retry + HITL + observability** — the surrounding plumbing.

### The operating-system analogy ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering, May 2026]])

The cleanest single-sentence answer to *"what does the harness do?"* is structural, not metaphorical — it maps directly onto the OS architecture every engineer already understands:

| OS-stack component | Agent-stack equivalent |
|---|---|
| **CPU** — powerful but inert | The raw LLM |
| **RAM** — fast but limited | The context window |
| **Disk** | External databases / state stores |
| **Device drivers** | Tool integrations |
| **Operating system** — schedules what the CPU sees | **The harness** |

> *"The raw LLM is the CPU — powerful but inert. No memory, no storage, no IO. Your context window acts as RAM — fast but limited. External databases serve as disk. Tool integrations are device drivers. And the harness is the operating system, deciding what the CPU sees and when."*

The mnemonic does two pieces of work at once:

- It **inverts the headline of most AI discourse**. The model is *the CPU*, not *the system*. A CPU does nothing useful without an OS scheduling its inputs. By analogy, an LLM does nothing useful in production without a harness deciding what enters its context window and when. This is why benchmark results stabilising on capability ceilings while production-agent performance keeps climbing is *not* a contradiction — the OS is doing the work.
- It **anchors the harness's job description**. An OS does memory management, scheduling, IO mediation, process isolation, and exception handling. An agent harness does context management, agentic-loop control, tool execution, sandboxing/permissions, and retry/error handling. The mapping is **structural** (one-to-one with the same problems already solved at the OS layer) rather than rhetorical.

The analogy is also operationally consistent with [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's]] *brain / hands / session* decomposition (CPU + scheduler / drivers / RAM-and-disk respectively) and with [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] 4-layer stack (the harness *is* Layer 3, sitting between Layer 4's swappable model and Layer 1's business logic, exactly as an OS sits between hardware and applications).

## Two named taxonomies (both compatible)

| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] — 4 layers | [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] — 7 building blocks |
|---|---|
| Context | Context manager |
| Constraints | Permission & guardrails + Tool executor + Retry/error handler |
| Contracts | (implicit in Permission & guardrails / Observability) |
| Compounding | Observability (extended into telemetry-as-training-data) |
| | State & memory |
| | Human-in-the-loop |

The Chatterjee taxonomy is more PM-facing (build order + roadmap implications); Kokane's is more engineering-architecture-facing (component diagram). They name the same construct.

## Architectural pattern: the 4-layer stack

[[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] places the harness in a 4-layer application stack:

```
Layer 1: Your App           — business logic, product, what user sees
Layer 2: Harness Frameworks — LangChain, Microsoft Agent Framework v1.0,
                               Google ADK, LlamaIndex, CrewAI, Haystack, DSPy
Layer 3: Agent Harness      — context manager, permissions, state, tool
   (runtime layer)            executor, retry, HITL, observability
Layer 4: Model Layer        — Azure OpenAI/GPT-5, Claude/Anthropic,
   (swappable)                Gemini/Llama/Ollama, AWS Bedrock
```

**Layer 2 vs Layer 3** is the load-bearing distinction: frameworks (LangChain etc.) are *pre-assembled harness kits*; the harness *runtime* is the actual execution layer that the framework implements under the hood. If you build without a framework, you wire Layer 3 yourself.

This stack is *operationally consistent* with [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]'s **brain / hands / session** decomposition — Kokane's "inference-only model" + "execution-only tool executor" is Anthropic's brain + hands; Kokane's State & memory + Context manager is Anthropic's session. Same architecture, two vocabularies, two vantages.

## Key claims

### The model is rented; the harness is owned ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]])

The strongest commercial framing in the wiki for the harness construct:

> *"The model is rented from a vendor whose competitor will outperform them within the year; the harness — our memory architecture, our quality contracts, our learned per-customer overrides, our telemetry — is what we own and what compounds; it is the only part of our stack that gets more valuable with every customer we ship to."*

Implications named explicitly:

- **Plan for swap, not for marriage.** Keep the harness model-agnostic where reasonable.
- **The harness investment is not a phase. It is a permanent allocation.** First three layers (Context / Constraints / Contracts) in year 1; fourth layer (Compounding) in year 2; calibrating-extending-hardening every quarter after.
- **The under-resourced role**: the engineer who thinks about agents the way SREs think about distributed systems — failure modes, observability, graceful degradation, long-tail edge cases. *"Hire for this taste. It is rare and it compounds."*

This frames the harness as a *capital asset* (compounds with use) rather than an *operational cost* (depreciates) — operationally identical to [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage's]] consumption-vs-compounding economics, applied at the engineering-stack level.

### What is genuinely novel vs. just rebranded ([[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]])

A useful sceptical counterweight to the "harness is the moat" framing. Kokane argues **90% of agent harness engineering is mature systems design applied to a new substrate**:

| Agent Harness term | What we called it before |
|---|---|
| Context management | Session / cache management |
| State persistence | Database + job queue |
| Tool orchestration | API middleware |
| Human-in-the-loop | Approval workflows |
| Context rot | Memory leak / stale state |
| Compaction | Summarization + offload |
| Harness lifecycle | Process / worker lifecycle |

**The 10% genuinely novel** has two named components:

1. **Non-determinism at the execution layer.** Classical middleware assumes the wrapped service behaves consistently. LLMs hallucinate tool calls, return semantically wrong responses, lose track of original goals 40 turns in. *You cannot unit test for it. You cannot formally specify it.* Validation must check **intent**, not just output format.
2. **Context as a first-class degrading resource.** Working memory that *actively gets worse the longer it runs.* Garbage collection ≠ semantic drift correction. The named phenomenon is **context rot**.

Kokane's verdict: *"If you've shipped real backend systems, you're already 80% of the way there. Your instincts on retries, state machines, idempotency, and observability are directly transferable. The skill gap isn't architecture. It's learning to think about prompt state as program state, and treating the context window as your most constrained and most expensive resource."*

### The Friday-in-March pattern: agent failures are usually harness failures ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]])

The wiki's most concrete worked example of harness-layer failure. A user said *"clean things up before the board review."* The agent — *competent, helpful, working exactly as designed* — interpreted this as archive stale documents + prune duplicates + remove stale sources, soft-deleting two weeks of research history 40 minutes before a board meeting.

> *"The model was not the problem. The model had reasoned correctly given what it was asked. The problem lived in the layer around the model — the layer that should have recognized 'clean up' as a destructive intent, paused before mass archiving, surfaced a preview, requested confirmation. That layer did not exist yet."*

The remediation is operationally specific: a **pre-tool hook that recognizes destructive verbs and routes the agent toward soft alternatives**. This kind of intent-validation work is precisely the 10% novel kernel Kokane names — and Chatterjee's broader claim is that **most agent failures, in production, are harness failures masquerading as model failures**.

### Layer-by-layer treatment ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]])

#### Context — "the room the agent walks into"

- The system prompt is **a document, not a string**, assembled fresh per request from many sources, with deliberate structure.
- **Stable parts** (top): identity, workspace, rules. **Cached at the model's KV layer** → reused across thousands of requests. *"At scale, this is the difference between a sustainable cost curve and one that bankrupts you."*
- **Dynamic parts** (below): user memory + workspace knowledge + delta summary + behavioral persona inferred from what the user appears to be trying to do.
- *"The same model, asked to synthesize research versus draft a strategy memo, should not receive the same instructions."*
- **The most expensive mistake**: passing a static system prompt and letting context retrieval happen later mid-conversation. Right context **before the first token** = useful first draft; lazy context = three turns to baseline competence.

#### Constraints — middleware before/after every tool call

> *"Every tool call in a production agent should pass through a checkpoint. Most do not. This is the single most common failure I have seen in agents that work in demos and break in production."*

**Pre-tool hooks**: destructive-verb recognition; workspace isolation; **loop detection** (agent has called the same search 6 times → surface exhaustion warning rather than burn another twenty cents in tokens).

**Post-tool hooks**: score output across **citation coverage, source triangulation, severity distribution, density, thematic diversity**; when below threshold, *inject corrective context into the agent's next turn* — *"your last synthesis scored a C, here is why, try again with these specific corrections."*

The harness becomes an **active editor**, not a passive observer.

#### Contracts — formal, evaluable, input-calibrated specifications of "done"

Two named failure modes around stopping: **stop too early** (output technically answers the question, adds no value) or **stop too late** (refining work that was already good until it becomes worse).

A contract is a **function, not a checklist** — it scales with input. *A synthesis contract over five sources should not impose the same minimums as one over fifty.* Output: passed/failed, score 0–1, specific issues enumerated. Harness then chooses: accept, request targeted revision, or surface partial result with note.

**Most underrated benefit**: contracts make agent behaviour **debuggable**. *"A failed run with a structured contract result tells you why it failed. A failed run without one leaves you reading transcripts."*

**Domain-specific**: research synthesis ≠ competitive analysis ≠ customer support reply. *"Encoding what 'good' looks like in your domain — explicitly, in evaluable form — is the work nobody outside your team can do for you."*

#### Compounding — telemetry as training data for the harness itself

The fourth layer "**distinguishes a harness from a system, and a system from a product that gets better with age.**"

- Every execution emits a **structured telemetry record** — *not log lines*: complexity classification with reasoning, contract score with breakdown, tool calls with latency/outcome/cost, active workspace overrides, applied learned preferences.
- Nightly process identifies patterns and proposes **harness adjustments** (not model fine-tuning — the model is rented and frozen): raise minimum source threshold for this workspace; lower complexity threshold for these query types; adjust checkpoint frequency for this risk profile.
- Proposals enter a queue with confidence scores + evidence; **human reviews**; approved adjustments become **workspace overrides** that compound durably.

> *"This is what people mean when they say AI products will get better with use. They do not mean the model is learning. The model is frozen; you cannot fine-tune Claude in production. They mean the infrastructure around the model is learning, and the surface area where learning lives is the harness."*

Operationally identical to [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]'s **verification → evaluation → learning capture** flywheel. Independent cross-source convergence: two practitioner essays, different vantages (PM-facing engineering vs. MIT SMR column), arrive at the same operational mechanism.

### The empirical anchor: same-model 6× variance, transferable harness, and the subtraction principle ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube, May 2026]])

Until early May 2026 the wiki carried *rhetorical* arguments for the model-rented / harness-owned framing — practitioner essays and vendor announcements that *asserted* harness importance without measuring it. The first **empirical anchor** is a YouTube synthesis (*[[2026-05-04-rethinking-agents-harness-is-all-you-need|Rethinking Agents — Harness is All you Need]]*) of two recent academic papers:

- **Pan et al. (Tsinghua, March 2026) — natural-language harness representation.** A 3-layer split (back-end / runtime charter / NL agent harness) tested on **SWE-bench verified** with GPT-5 max-reasoning. Module-by-module ablation results:
  - **Self-evolution** = the only module *consistently helpful* when added.
  - **Verifiers** = *actively hurt*: −0.8 SWE-bench, −8.4 OS World.
  - **Multi-candidate search** = hurt by −5.6.
  - **Full vs. stripped harness**: same 74–76% pass rate; 16.3M tokens / 600+ tool calls / 32 min vs. 1.2M tokens / 51 calls / under 7 min — **14× compute waste in the full configuration**.
  - **OS-Symphony NL migration**: rewrote a native-code harness in structured natural language with the *same strategy* — performance **30.4% → 47.2%**, runtime **361 min → 41 min**, LLM calls **1,200 → 34**. *"The representation itself drew the gain."*
- **Khattab et al. (DSPy team) — Meta-Harness auto-optimisation.** An agentic proposer (Claude Opus 4.6) reads failed execution traces, diagnoses what broke, and **rewrites the entire harness**. Loop scale: 10M tokens/iter, ~82 files read per round, **400× more feedback than any prior method**. Headline results:
  - **76.4% on Terminal Bench 2** — the only auto-optimised system in a hand-engineered field.
  - **+7.7 points above SOTA** on a 215-class text classification, **4× fewer tokens**.
  - **Haiku ranked above Opus** on the auto-optimised harness — *a smaller model outranking larger ones through harness optimisation alone.*
  - **Raw traces are irreplaceable**: removing them drops accuracy 50% → 34%; *summarising* them before feeding doesn't help (34.9%). The signal lives in the raw failure detail. Direct implication for any *Compounding* layer: do not summarise telemetry before the meta-learning loop reads it.
  - **Transferability** — the load-bearing finding: a harness optimised on *one model* improved *five other models* without re-optimisation. *"The reusable asset is not the model, it's the harness. You can build it once. It works across the model landscape."* This is the **strongest empirical support yet** for the *"model rented; harness owned"* framing — until this paper, it was a rhetorical claim. This is what makes it operational.

The video also names a discipline-counter-prescription absent from the prior wiki sources:

#### The subtraction principle (Anthropic, named operationally)

> *"Every harness component encodes an assumption about what the model cannot do alone — and those assumptions expire when models improve. When Opus 4.6 stopped needing context resets, Anthropic just dropped them entirely."*

Two corroborating data points: **Manus rewrote their harness 5× in 6 months**; **Warel removed 80% of agent tools and got better results**.

> *"Mature harness work looks less like building structure up and more like pruning it down."*

This **directly contradicts** the late-2024 / early-2025 instinct to give agents more and more tools. Combined with Pan et al.'s ablation finding that **verifiers actively hurt**, the prescription is operational: *if the model can now do an aspect that was hand-crafted in the harness before, drop the hand-crafted machinery.* The subtraction principle is the closest the wiki has yet come to a **named operational discipline for harness pruning** — distinct from but compatible with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] additive 4-layer build order. Both can be true: build the four layers; prune within each layer ruthlessly as the model improves.

#### Audit checklist for builders (when an agent underperforms)

The video closes with a **diagnostic order-of-operations** that is operationally compatible with everything else this concept holds — *don't switch the model first*:

1. What's in the context window that **does not need to be there**?
2. Which tools does the agent **rarely use well**?
3. Are verification or search loops **hurting** performance (per the Tsinghua ablation)?
4. Is your control logic in **code or in language** (per the OS-Symphony +16.8-point migration)?

> *"It is no longer a question of which model to pick. It is a question of which structure to remove."*

The two underlying papers are not separately ingested. Treat the specific numbers as second-hand until primary-source ingest confirms them — but the *direction* (transferability, subtraction, raw-traces-irreplaceable) is durable independent of the specific magnitudes.

## Convergence with prior wiki claims

| Source | Construct | Wiki vocabulary in this concept |
|---|---|---|
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic Managed Agents]] | brain / hands / session | Layer 4 / Layer 3 tool executor / State & memory + Context |
| [[2026-04-22-cheung-ippolito-secchi-google-agents-cli\|Google Agents CLI]] | 7 specialized skills + ADLC 9-stage wheel | productized harness toolkit; ADK Code = Layer 2; Cloud Run / GKE / Agent Runtime = Layer 3 substrate |
| [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] | 7 building blocks + 4-layer stack | the architectural-engineering vantage |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | 4 layers (Context/Constraints/Contracts/Compounding) | the PM-facing build-order vantage |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron & Schrage 2026]] | verification → evaluation → learning capture | the Compounding layer at organizational level |
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Prompt Engineering YouTube, May 2026]] | same-model 6× variance + transferable harness + subtraction principle | the **empirical anchor** — ablation data behind the prior rhetorical claims |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy at Sequoia AI Ascent, Apr 2026]] | [[software-3.0]] paradigm + [[agentic-engineering]] as discipline | the **paradigm-vocabulary anchor** — the harness is the runtime that executes Software 3.0 programs; the practice that builds it is agentic engineering |

This is the strongest cross-source convergence in the wiki on a *runtime-engineering* construct — seven sources, six vantages (two big-vendor announcements / two Medium practitioner essays / MIT SMR column / YouTube empirical synthesis / venture-capital-keynote interview), all describing the same architecture. Two of the six — [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] (8 April) and [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]] (22 April) — are vendor-side productisations within two weeks of each other. The sixth — [[2026-05-04-rethinking-agents-harness-is-all-you-need|the YouTube synthesis]] — is the wiki's first *empirical* source, summarising two academic papers (Pan et al. Tsinghua March 2026, Khattab et al. DSPy team) and turning *"the harness is the moat"* from a rhetorical assertion into a measured one (transfer of one optimised harness across five models without re-tuning).

## Debates / contradictions

- **Is the harness "the moat" or "rebranded systems engineering"?** Kokane and Chatterjee disagree rhetorically on this. Resolution: both are correct at different levels — the *primitives* of harness engineering are mature systems engineering (Kokane is right); the *aggregate, in production, calibrated to a domain over time* is what compounds and differentiates (Chatterjee is right). The wiki holds both.
- **Where does the harness end and the application begin?** Kokane's stack puts business logic in Layer 1 (Your App) and the harness in Layer 3 (runtime); Chatterjee's Constraints layer (workspace isolation, scoring) blends into business logic. There is no clean boundary — what's "harness" varies by team and by the maturity of the harness frameworks available.
- **Frameworks vs. roll-your-own.** [[LangChain]] / Microsoft Agent Framework / Google ADK / LlamaIndex / CrewAI / Haystack / DSPy give you Layer 2 primitives; if you skip the framework, you wire Layer 3 yourself. Open question (and a source of practitioner debate that the wiki has not yet ingested): how much harness work is *general* (framework-able) vs. *domain-specific* (must be hand-built). Chatterjee's domain-specific contracts argument suggests significant hand-built work always remains. The [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]] announcement adds a new wrinkle here — it is a CLI *over* the framework (ADK), bundling **opinionated scaffold templates plus per-stage skills for AI coding agents**, suggesting a third tier emerging *above* harness frameworks: vendor-published lifecycle toolkits.
- **Is the harness model-coupled or model-portable?** Until early May 2026 the wiki held the *"keep the harness model-agnostic where reasonable"* claim as a prudential design hint. The [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube source]]'s transferability finding (Khattab et al.: a harness optimised on *one* model improved *five other* models without re-optimisation) **upgrades this from a hint to an empirical claim**. Direct implication: if optimised harnesses transfer across model families, then harness work compounds across model upgrades and model-tuning work doesn't — which is the strongest empirical support yet for [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] *"model rented, harness owned"* framing.
- **Does "the model is rented" framing hold under model-family reliability variation?** [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] documented that Claude Sonnet 4.5's "context anxiety" was absent on Opus 4.5 — same family, different reliability. If model-within-family variation is large, the "plan for swap" prescription needs nuance. Chatterjee acknowledges this with *"keep the harness model-agnostic where the cost of doing so is reasonable."*
- **The Claude Code leak as anchor.** Both new sources reference an unconfirmed leak of Anthropic's Claude Code source code (analysed by DistributedApps.ai / Ken Huang substack and reported in arstechnica). Treat the leak's specific claims as second-hand until the wiki ingests a primary source on it.

## Related concepts

- [[ai-agents]] — the technology + deployment progression. Agent harness is the *runtime layer* underneath the chatbot → agent → multi-agent progression.
- [[foundation-models]] — the substrate the harness wraps. The "rent vs own" framing positions models as commodity inputs to harness-differentiated products.
- [[micro-productivity-trap]] — orgs that "just call the model" without building harness infrastructure are stuck in consumption mode. The harness is the operational machinery that escapes the trap.
- [[responsible-ai]] — the Constraints layer (destructive-verb detection, workspace isolation, intent validation) operationalizes RAI policies at runtime. *"Security as structural unreachability"* (per [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]) is the engineering principle.
- [[generative-ai]] — harness frameworks (LangChain, Microsoft Agent Framework, etc.) are now visible in the deployed-tools landscape.
- [[enterprise-ai-adoption]] — "plan for swap, not for marriage" is a *direct prescription* that complements [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria's]] firm-boundary framework.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "agent-harness")
SORT file.name ASC
```

## Open questions

- **Does harness configuration become a market?** Chatterjee implies domain-specific contracts are work no outside team can do for you — but there is no reason templates can't emerge per domain. Worth tracking whether 2026–27 sees vendors/open-source for *contract templates by domain*.
- **~~Is there empirical measurement of harness-tuning lift?~~** *Substantially answered* by [[2026-05-04-rethinking-agents-harness-is-all-you-need|the Prompt Engineering YouTube source]]: Khattab et al.'s Meta-Harness scored 76.4% on Terminal Bench 2 (the only auto-optimised system in a hand-engineered field) and +7.7 points above SOTA on a 215-class text classification with 4× fewer tokens. Pan et al.'s OS-Symphony NL migration jumped 30.4% → 47.2% on the same strategy, with runtime collapsing 361 → 41 min. The remaining open question is *primary-source ingest of the underlying papers* — the video is third-hand on these specific numbers.
- **Primary-source ingest: Pan et al. (Tsinghua, March 2026).** Would substantiate the SWE-bench verified ablation results and the OS-Symphony migration deltas. Search target: *"Pan natural-language agent harness Tsinghua March 2026"* + arXiv.
- **Primary-source ingest: Khattab et al. (DSPy team, Meta-Harness).** Would substantiate the Terminal Bench 2 76.4%, the **transferability across five models** claim, and the *raw-traces-irreplaceable* finding (50% → 34% accuracy when traces removed; 34.9% when summarised — the signal lives in the raw failure detail).
- **Does the "raw traces > summaries" finding generalise?** Khattab et al. specifically tested this on auto-harness optimisation. If it holds for *any* compounding-loop telemetry (per Chatterjee's *Compounding* layer), it has a sharp design implication: **never summarise telemetry before the meta-learning loop reads it.** Worth tracking against future ablation work.
- **How much of the 7-building-block / 4-layer architecture is novel vs. rebranded?** Kokane's "10% genuinely novel" is a plausible-sounding heuristic, but it is rhetorical, not measured. A controlled comparison (build the same system using mature systems-engineering vocabulary vs. agent-harness vocabulary, measure delta in correctness/cost/time) would settle the rhetorical dispute.
- **The Claude Code leak.** Referenced in both new sources but not directly ingested. If a primary-source ingest becomes possible, it would substantiate or challenge the harness-pattern claims that currently rest on second-hand interpretation.
- **Why do verifiers actively hurt?** Pan et al.'s ablation shows verifiers degrade SWE-bench by 0.8 and OS World by 8.4. Mechanism unstated. Hypothesis: verifier-driven retries dilute the agent's confidence calibration, or verifiers add noise faster than they catch real failures. Worth tracking against future ablation work.
- **Manus and Warel as candidate entity pages.** Both named in [[2026-05-04-rethinking-agents-harness-is-all-you-need|the YouTube source]] as agent platforms with relevant operational claims (5× harness rewrites; −80% tools / +performance). Promote on second-source mention.
