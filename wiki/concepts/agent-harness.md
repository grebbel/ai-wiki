---
type: concept
aliases: ["agent harness", "harness", "AI agent harness", "agent runtime", "agent runtime layer"]
tags: [agent-harness, ai-agents, ai-engineering, harness-frameworks, context-management, constraints, contracts, telemetry, llm-non-determinism, hooks, repository-as-system-of-record]
confidence: 0.98
last_confirmed: "2026-05-17"
source_count: 31
relationships:
  - type: part-of
    target: ai-agents
    via: "the runtime engineering layer that wraps a foundation model to turn it into a production-grade agent"
  - type: uses
    target: foundation-models
    via: "the harness wraps a (rented, swappable) foundation model in a runtime that adds context/constraints/contracts/compounding"
---

# Agent Harness

The **runtime engineering layer that lives between a foundation model and the user** in any production [[ai-agents|AI agent]] system. The harness wraps the model with context management, permission/guardrails, state and memory, tool execution, retry/error handling, human-in-the-loop, observability, and (in mature systems) a self-tuning meta-learning loop. The construct emerged in late 2025 / early 2026 as practitioner vocabulary; by April–May 2026 it had become the dominant frame for *what production AI engineering actually is*, with **twenty** wiki sources engaging the term substantively — including primary-source vendor announcements from [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic]] (8 April 2026) and [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google]] (22 April 2026) that productize the harness/runtime layer as a hosted service or CLI toolkit; the wiki's first **empirical anchor** ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube, 4 May]]) bringing ablation data and a **transfer-across-models** finding; the wiki's first **paradigm-vocabulary anchor** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy at Sequoia AI Ascent, 29 April]]) placing the harness inside the broader [[software-3.0]] computing paradigm and naming the practitioner discipline that wields it: [[agentic-engineering]]; and now (10 May 2026 ingest batch) the wiki's first **vendor-side production case study** at scale ([[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex, 11 Feb 2026]] — five months, ~1M LOC, 0 manually-written lines), the wiki's first **operationalization of hooks-as-portable-primitive across harnesses** ([[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic / Towards Data Science, 8 May]]), and the wiki's second-vendor formalization of the surrounding [[agent-development-lifecycle|lifecycle]] ([[2026-05-09-chase-agent-development-lifecycle|Chase / LangChain, 9 May]]) — which incidentally sharpens the wiki's vocabulary by splitting *frameworks*, *runtimes*, and *harnesses* into three distinct Build-phase layers.

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

### Hooks as a first-class harness primitive ([[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]] + [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]])

The 10 May 2026 ingest batch makes **lifecycle hooks** explicit as a first-class harness primitive — distinct from MCP tools, distinct from middleware, distinct from observability. Two converging vantages:

- **[[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]]** demonstrates that **Claude Code, Codex, and Cursor all support the same five lifecycle events** with near-identical contracts: `SessionStart`, `UserPromptSubmit` (Cursor: `beforeSubmitPrompt`), `PreToolUse`, `PostToolUse`, `Stop`. The hook receives JSON on stdin and may emit JSON on stdout to inject context. Two of the five events are *injection points*: `SessionStart` prepends to the system prompt; `UserPromptSubmit` appends to the user prompt.
- **[[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]]** shows the same primitive in production at OpenAI: background "doc-gardening" tasks, custom linters, taste-invariant scans, and golden-principle GC are all hook-shaped — system-initiated, deterministic, lifecycle-fired.

The clean **hooks vs. MCP** distinction is operationally load-bearing:

| Property | MCP tools | Hooks |
|---|---|---|
| Initiator | Agent (LLM-decided) | System (lifecycle-event-fired) |
| Reliability | Inconsistent — model has to "remember to remember" | Deterministic — every event fires |
| Context cost | Consumes model attention | Zero context cost |
| Best for | On-demand search, store, update, delete | Passive logging, profile injection, append-only context |

> *"What you really want is passive, deterministic logging — something that captures every session event regardless of what the model is doing, without consuming any of its context or attention. This is exactly what hooks give you."* — [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]]

The architectural implication is sharp: **memory is portable across harnesses if it lives in hooks, locked-in if it lives in vendor-internal session state.** Bratanic's working demo (shared Python hook scripts + Neo4j store) shows you can switch from Cursor to Claude Code to Codex mid-project and pick up exactly where you left off. This is one tier higher than [[2026-05-04-rethinking-agents-harness-is-all-you-need|the Khattab et al. transferability finding]] (a harness optimised on one model improved five other models): a *substrate component of harness configuration* (memory) is portable across vendor harnesses, not just across models.

This convergence also has **wiki-internal** resonance: the schema layer of *this* repository (see [§Hooks](../../CLAUDE.md#hooks)) is built on the same primitive — `SessionStart` injects wiki snapshot context, `PostToolUse` lints edited pages, `Stop` re-exports the graph. Three independent vantages (Lopopolo / Bratanic / this repo) supply convergent evidence that hooks are a stable cross-vendor harness primitive.

#### The dream-phase pattern

Bratanic names a specific architectural pattern that Lopopolo's "doc-gardening" and Chatterjee's *Compounding* layer both gesture at without naming:

- **Hooks (online)** — passively log every event into a store. No model calls, no latency cost, just append.
- **Dream phase (offline)** — a batch job reads accumulated events, asks an LLM to distill them into durable Markdown memories, writes them back. Memories are organized by topic and merged rather than appended, so they stay current instead of growing forever.
- **Injection (online)** — on the next session start in any harness, profile memories are loaded into context. On each user prompt, relevant memories are searched and appended automatically.

The dream-phase pattern preserves the [[2026-05-04-rethinking-agents-harness-is-all-you-need|Khattab et al. *raw-traces-irreplaceable* finding]] (50% → 34% accuracy when traces removed; 34.9% when summarized — the signal lives in the raw failure detail) by keeping raw events in the store and only summarizing into the *injected* layer. The summary is for the *next* session's context, not for the meta-learning loop's training input.

### Refined Build-layer vocabulary ([[2026-05-09-chase-agent-development-lifecycle|Chase 2026]])

Until 9 May 2026 the wiki used [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] 4-layer stack (App / Frameworks / Harness / Model). Chase's lifecycle piece sharpens the framework/harness boundary by introducing a **third layer** between them:

| Layer | Focus | Examples |
|---|---|---|
| **Frameworks** | Pure abstractions: model calls, tools, prompts, retrieval, agent loops | LangChain, CrewAI |
| **Runtimes** | Execution-layer concerns: state, control flow, durability, persistence, human intervention | LangGraph, Temporal-based custom |
| **Harnesses** | The agent's environment: prompts, skills, MCP servers, hooks, middleware, memory, sometimes filesystem | Deep Agents, Claude Agent SDK |
| **No-code** | Configuration UI for non-engineers | LangSmith Fleet, Claude Cowork, n8n |

This refines what *agent harness* means in this concept page going forward:

- **Kokane's "harness"** is broad — Layer 3 in his 4-layer stack, conceptually everything that wraps the model. Operationally compatible with the wiki's prior usage.
- **Chase's "harness"** is narrower — specifically the *content + environment* the agent operates within (prompts, skills, MCP, hooks, middleware, memory), with frameworks (abstractions) and runtimes (execution) treated as separate adjacent layers.

Both are correct vocabularies. The wiki holds them as **scope variants**: when discussing the harness in the [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee Context/Constraints/Contracts/Compounding]] sense, Chase's narrow scope fits best (skills, prompts, hooks, memory). When discussing the harness as the *full runtime layer wrapping a model*, Kokane's broad scope fits. Both definitions converge on **the harness is what compounds with use; the model is rented**.

### The OpenAI Codex case study — what production looks like ([[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]])

Until February 2026 the wiki carried *practitioner essays* and *vendor announcements* about the harness construct, plus one *empirical anchor* (the YouTube synthesis). [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]] adds the wiki's first **first-person production case study from a foundation-model vendor** running its own engineering on its own model:

- **Five months, ~1M LOC, ~1,500 PRs, 7 engineers, 3.5 PRs / engineer / day, throughput increasing as team grew** — built with **0 lines of manually-written code.**
- **Repository as system of record**: every architectural rule, design doc, exec plan, taste invariant encoded as repo-local versioned markdown. *"From the agent's point of view, anything it can't access in-context while running effectively doesn't exist."* This is Chatterjee's Context layer made operational: *if a Slack thread aligned the team, that decision is illegible until it's encoded in the repo.*
- **AGENTS.md as table of contents, not encyclopedia**: progressive disclosure with verification status, ownership, freshness checks, and a **doc-gardening agent that opens fix-up PRs** for stale or obsolete docs. The directory tree itself *is* the natural-language harness — operationally identical to Pan et al.'s OS-Symphony NL migration ([[2026-05-04-rethinking-agents-harness-is-all-you-need|YouTube source]]).
- **Layered architecture mechanically enforced**: per-domain Types → Config → Repo → Service → Runtime → UI dependency direction; cross-cutting concerns route through a single Providers interface; custom linters (Codex-generated) enforce. *"This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it's an early prerequisite: the constraints are what allows speed without decay or architectural drift."*
- **Throughput inverts merge philosophy**: minimal blocking gates; PRs short-lived; flakes addressed with follow-up runs not blocked CI; *"In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive."*
- **Golden principles + scheduled GC**: opinionated mechanical rules (prefer shared utilities; never probe data, validate at boundaries with typed SDKs); background Codex tasks scan for deviations and open targeted refactoring PRs, mostly auto-merged. *"Technical debt is like a high-interest loan."*
- **Application legibility primitives**: Chrome DevTools Protocol wired into the agent runtime so Codex can take DOM snapshots, take screenshots, validate UI behavior; per-worktree observability stack (LogQL/PromQL/TraceQL) so prompts like *"ensure service startup completes in under 800ms"* become tractable; single Codex runs work on a single task for upwards of six hours.
- **Increasing autonomy**: end-to-end feature flow from a single prompt — validate state, reproduce bug, record video, implement fix, validate fix, record resolution, open PR, respond to feedback, detect/remediate build failures, escalate only when judgment is required, merge.

> *"Our most difficult challenges now center on designing environments, feedback loops, and control systems that help agents accomplish our goal: build and maintain complex, reliable software at scale."*

This **substantiates** the rhetorical claims of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] with a concrete operational case at vendor scale. It is also the strongest worked example yet of [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's]] *agentic engineering* discipline: humans steer, agents execute, the discipline shows up in *the scaffolding* — not the code.

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
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex, Feb 2026]] | repository-as-system-of-record + AGENTS.md table-of-contents + layered architecture + golden-principles GC | the **vendor-side production case study** — five months, 0 manually-written lines, ~1M LOC; the rhetorical claims become observed fact at vendor scale |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic / TDS, May 2026]] | hooks vs. MCP + dream-phase memory + cross-vendor hook contract | the **hooks-as-portable-primitive anchor** — same five lifecycle events across Claude Code / Codex / Cursor; memory portable across harnesses |
| [[2026-05-09-chase-agent-development-lifecycle\|Chase / LangChain, May 2026]] | Build → Test → Deploy → Monitor + Govern; frameworks / runtimes / harnesses / no-code split | the **lifecycle-vocabulary refinement** — sharpens the framework/harness boundary, names governance axes for agent scaling |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler / Thoughtworks at QCon London 2026]] | Feed-forward × feedback × CPU-vs-GPU two-axis decomposition; structural tests (ArchUnit, Spring Modulith, Dependency Cruiser) as agent feedback; enhanced lint messages as "good prompt injection"; harness templates as the next abstraction layer | the **practitioner-observer-from-consultancy vantage** — propagates Lopopolo's harness-engineering term to the broader engineering audience and adds Thoughtworks' cross-client perspective on which mechanisms actually carry load |
| [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs\|Thompson / NYT The Daily 2026]] | Manu Ebert's "10 Commandments" file — uppercase, repetitive, high-stakes emotional framing ("failure to do these tests is unacceptable and embarrassing") — as a small-startup-developer worked example of rules-file design; agent-driven Socratic-dialogue spec elicitation; distributional-semantics explanation for why stern/emotional prompts work | the **journalist-observer + first-person operator vantage** — Lopopolo showed the vendor-engineering rules-file at OpenAI scale, Böckeler named the enhanced-lint-as-good-prompt-injection pattern at consultancy clients, and Thompson surfaces what the same mechanism looks like in the hands of an individual startup developer. Confirms the rules-file pattern is now visible at *three distinct organisational scales* (vendor, consultancy clients, individual developer/startup) |
| [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers\|Jassy / Amazon CEO on HBR IdeaCast 2025]] | First-party-CEO May-2025 mention of *"agentic capabilities — take a bunch of automated actions in succession"* as a built-in feature of Bedrock; three-layer AI-stack framing (chips + model-building services / orchestration-with-features / applications) where the middle layer corresponds to the wiki's harness vocabulary | the **earliest-CEO vendor characterisation vantage** — predates Lopopolo by ~9 months, Anthropic Managed Agents by ~11 months, and Böckeler by ~12 months. Jassy named the *productised category* of agentic harness features before any of the wiki's subsequent sources made the mechanics concrete. Demonstrates the harness layer was visible to a major-vendor CEO well before the practitioner discourse named it as a discipline |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu / Y Combinator Startup School 2026]] | *Intelligence layer at the centre of the company* framing — the harness vocabulary applied at **company scale** rather than at the application-product scale; *queryable organization / legibility-to-AI* as the persistent-context substrate the company-harness reads; *closed-loop vs open-loop* control-systems vocabulary; *software factories* (Strong DM example) as the transferable architecture form of the Lopopolo pattern | the **YC-partner observer-of-startup-orgs vantage**. Extends the harness construct beyond the application/product/repo scale that all prior sources operated at, into **org-design scale**. The intelligence layer Hu describes reads *company artifacts* (Linear tickets, Slack channels, meeting recordings, sales calls) as the persistent context the company-harness's compounding loop tunes against — structurally identical to the application-harness Compounding layer but at the larger scope |
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | Four eval ingredients (task / dataset / scores / experiment); LLM-as-judge + code-based score families; offline-online-flywheel three-mode operation; score-at-the-span-level for agentic workflows; evals-as-offense reframing (Anker Goyal); evals-as-CI-check pre-merge gate | the **eval-platform vendor vantage** — operationalises Chatterjee's Contracts layer (formal evaluable specifications) and Compounding layer (telemetry-feeds-learning) with vendor-specific tooling vocabulary. Earliest wiki source on evaluation as a formalised discipline (June 2025) — predates Chase ADLC, Lopopolo, Böckeler by 9-11 months. Braintrust is the wiki's first dedicated eval-platform anchor; Notion + a healthcare-company-with-doctors-doing-human-review are named customers |
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan / Y Combinator (GStack) 2026]] | GStack — open-source toolkit of skills (Office Hours / Plan / Adversarial Review / Design Shotgun / Code Review / SLQA / Ship) wrapping Claude Code; Playwright+Chromium wrapped as a CLI (replacing Claude-in-Chrome MCP); 10-15 parallel sessions; 3-week ship-to-more-stars-than-Ruby-on-Rails; Yegge Gas Town stage 7 invoked explicitly | the **founder-CEO open-source-toolkit vantage** — first wiki source showing a major-accelerator-president (Garry Tan / YC) publicly shipping a packaged harness rather than just describing one. Operationalises Hu's *harness templates* future-prediction at startup-development scope; convergent with Böckeler's CPU-deterministic feedback-harness via the Playwright-CLI wrapper |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB / Martin 2026]] | Knowledge graphs as deterministic-grounding-substrate for LLM-based agents; KG-ETL pipeline; chunking-strategy taxonomy (recursive / structural / semantic / agentic / no-chunking); SurrealQL hybrid-query for vector + graph + full-text in single query; named vector-only-RAG failure modes (context clash / context confusion / dense neighbourhood degradation) | the **KG-as-persistent-context-substrate vantage** — extends harness vocabulary into the relational-knowledge-context layer. Maps onto Chatterjee's Context layer (assembling the right context) with deterministic-graph-traversal complementing similarity-search. Promotes [[knowledge-graphs]] to a wiki concept page |
| [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era\|Chamath / Stanford AI Club 2026]] | The *control plane for AI* construct — a symbolic layer (PRDs, requirements, "secrets in English") that sits **above** the embedding space and is *hardware-, database-, and language-independent*; downstream agents read from this control plane to produce code, traverse legacy systems, and operate on long-horizon tasks; *"go and convince business people of that — they get that"*; explicit acknowledgement of the same technical-harness challenges named elsewhere (*"how do you actually create the right eval and the right guard rails for the agents to stay on task? How do you actually create a knowledge graph that these agents can traverse so that they can stay at the level of embeddings?"*) | the **enterprise-rebuild platform vantage** — extends harness vocabulary into the **business-spec-as-control-substrate** layer. Where Hu's *intelligence layer at the centre of the company* applies harness thinking to org-design at startup scale, Chamath applies it at the **enterprise-rebuild scale**: the harness is what the Fortune-1000 legacy-modernization customer rents in order to operate on its own institutional symbolic representation. Strongest existing wiki source on the *English-as-control-plane* construct |
| [[2026-05-15-osmani-agent-harness-engineering\|Osmani / O'Reilly Radar, May 2026]] | First **cross-author synthesis essay** under the explicit name *harness engineering*; threads Viv Trivedy (originator), Dex Horthy / HumanLayer, Anthropic's engineering team, Birgitta Bockeler, Simon Willison, and Fareed Khan into a single discipline; names three load-bearing operating rules: **(a)** *"A decent model with a great harness beats a great model with a bad harness"*; **(b)** the **ratchet** — *every line in a good AGENTS.md should be traceable back to a specific thing that went wrong*; **(c)** *"The gap between what today's models can do and what you see them doing is largely a harness gap."* Operationalises **working-backward-from-behavior** as the harness-design pattern (*if you can't name the behavior a component exists to deliver, it probably shouldn't be there*); names **HaaS (harness-as-a-service)** as the shift from building on LLM APIs to building on harness APIs (Claude Agent SDK / Codex SDK / OpenAI Agents SDK); reports the **Terminal Bench Top 30 → Top 5 by changing only the harness** transfer datapoint as the load-bearing empirical anchor; observes that *top coding agents look more like each other than their underlying models do* | the **practitioner field-guide / cross-author synthesis vantage** — first wiki source that names the prior cluster *as a single discipline*. Operationalises the discipline at the working-engineer altitude (ratchet pattern, AGENTS.md hygiene, hook-as-enforcement principle, harnesses-don't-shrink-they-move ceiling-shift observation). The HaaS framing is the wiki's first naming of the **substrate-shift from completion APIs to runtime APIs** as the dominant 2026 build path |
| [[2026-05-11-karten-zhang-continual-harness-online-adaptation\|Karten, Zhang et al. / arXiv 2605.09998, May 2026]] | **The first peer-track academic paper with "harness" in the title.** Formal definition *H* = *(p, G, K, M)* — system prompt, sub-agents, skills, memory — plus meta-tool API (`define_agent`, `run_code`, `process_memory`) for editing each component in place. **Continual Harness** = reset-free framework where an LLM Refiner edits the full harness state from the most recent trajectory window during a single continuous episode, generalising prompt-optimisation methods that rewrite only *p* between complete-episode resets. Two-loop architecture (inner = agent step; outer = harness refinement every *F* steps). Co-learning loop trains open-source model weights (Gemma-4 E2B/E4B/26B-MoE/31B-dense) via SFT + offline GRPO warm-up + online DAgger+PRM through the live-refining harness. Empirical anchors on Pokémon Red/Emerald across Gemini 3 Pro/Flash/Flash-Lite: **~40% cost reduction at 100% completion on Pro; capability-floor failure on Flash-Lite** (every Continual Harness variant **underperforms** the minimalist baseline). Power Plant Route Loop case study (1,003-turn stagnation, 842 repeated schema-mismatched calls) is the strongest single failure-mode write-up in the wiki on agent self-tooling. **Resolves the wiki's open-question on the Khattab Meta-Harness paper** — Karten cites it as **Lee, Nair, Zhang, Lee, Khattab, Finn — arXiv:2603.28052, 2026** | the **formal-academic anchor vantage** — first peer-track formalisation. The *(p, G, K, M)* notation gives the construct mathematical handles; the meta-tool API gives harness-editing a tractable signature; the capability-floor result gives the *"harness > model"* claims their sharpest qualifier yet. Marks the harness construct's transition from practitioner vocabulary to academic vocabulary within a single calendar year (PokeAgent Challenge benchmark Feb 2026 → Continual Harness May 2026) |

This is the strongest cross-source convergence in the wiki on a *runtime-engineering* construct — eleven sources, eight vantages (two big-vendor announcements / two Medium practitioner essays / MIT SMR column / YouTube empirical synthesis / venture-capital-keynote interview), all describing the same architecture. Two of the six — [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] (8 April) and [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]] (22 April) — are vendor-side productisations within two weeks of each other. The sixth — [[2026-05-04-rethinking-agents-harness-is-all-you-need|the YouTube synthesis]] — is the wiki's first *empirical* source, summarising two academic papers (Pan et al. Tsinghua March 2026, Khattab et al. DSPy team) and turning *"the harness is the moat"* from a rhetorical assertion into a measured one (transfer of one optimised harness across five models without re-tuning).

## The harness-engineering discipline (Osmani synthesis, May 2026)

[[2026-05-15-osmani-agent-harness-engineering|Osmani's O'Reilly Radar essay]] is the wiki's first source that names the prior cluster **as a single emerging discipline** under the explicit term **harness engineering** — coined per Osmani by **Viv Trivedy**. The essay's contribution is not architectural (the four-layer / seven-building-block / brain-hands-session taxonomies above already cover that ground) but **operationalising**: a working rule-set for *how to do the engineering*. Three rules are load-bearing for the concept:

1. ***"A decent model with a great harness beats a great model with a bad harness."*** The category-error fix at the model-versus-harness debate.
2. **The ratchet.** *Every mistake becomes a rule. You only add constraints when you've seen a real failure. You only remove them when a capable model has made them redundant.* **Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong** — *ratchet, don't brainstorm.*
3. ***"The gap between what today's models can do and what you see them doing is largely a harness gap."*** Direct corollary of the **Terminal Bench Top 30 → Top 5 by changing only the harness** transfer result (Viv's team).

Osmani's design pattern — *behavior we want (or want to fix) → harness design to help the model achieve this* — generalises the [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee Friday-in-March story]]: every harness component should map to a specific behaviour it exists to deliver, and *if you can't name the behavior a component exists to deliver, it probably shouldn't be there*. This is the operational test for the *earn-each-line* principle the wiki has already absorbed at AGENTS.md scope (Lopopolo) and now generalises to the whole harness.

Two observations from the essay belong on the concept page as **first-class wiki claims**:

- **Harnesses don't shrink; they move.** As models improve, the space of interesting harness combinations doesn't shrink — it *moves*. Opus 4.6 largely killed Sonnet 4.5's context-anxiety failure mode, retiring a class of anxiety-mitigation scaffolding; but the ceiling moved with the model, opening new task spaces that need new scaffolding (multiday memory policies, three-agent coordination, evaluator agents for design quality). Anthropic's clean phrasing Osmani names: **"Every component in a harness encodes an assumption about what the model can't do on its own"** — when the model gets better at something, that component becomes load-bearing for nothing and should come out; when the model unlocks something new, new scaffolding is needed.
- **The convergence of top coding agents.** *Look at the top coding agents side by side (Claude Code, Cursor, Codex, Aider, Cline) and they look more like each other than their underlying models do.* The models are different. **The harness patterns are converging.** Not an accident — the industry is finding the load-bearing scaffolding pieces that turn a generative model into something that ships.

### Harness as a service (HaaS)

Osmani names the **HaaS substrate-shift** as the dominant 2026 build path: from building on **LLM APIs** (which give you a completion) to building on **harness APIs** (which give you a runtime). The Claude Agent SDK, Codex SDK, and OpenAI Agents SDK all point the same way. The four-pillar configuration surface (system prompt, tools, context, subagents) is what the harness framework hands you; domain-specific prompt and tool design is what you put on top.

The HaaS claim has **direct news-side confirmation in [[2026-05-05-loukides-radar-trends-may-2026|the May 2026 Radar Trends digest]]** Loukides published ten days before Osmani: **OpenAI decoupled its agent harness and released it open-source via the Agents SDK**; Anthropic shipped **Claude Managed Agents** as a prebuilt harness; Amazon launched **agent registry within AWS Bedrock AgentCore**; **Cursor 3 repositioned as agent orchestrator, demoting the IDE to secondary role**. Four vendors converged on the HaaS productization within a single month — the editorial digest is the empirical anchor for Osmani's rhetorical claim.

## The formal-academic anchor: *(p, G, K, M)* + meta-tools (Karten et al., May 2026)

[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten, Zhang et al. — *Continual Harness: Online Adaptation for Self-Improving Foundation Agents* (arXiv:2605.09998v1, 11 May 2026)]] is the wiki's first peer-track academic paper with **"harness" in the title**. It contributes three things to this concept page that no practitioner source has provided:

1. **Mathematical notation.** A harness is *H* = *(p, G, K, M)* where *p* is the system prompt, *G* is the sub-agent set, *K* is the skill library (text heuristics + executable routines), and *M* is the persistent memory. Updates are CRUD operations on each component. This collapses the practitioner taxonomies ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]'s 4 layers, [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]]'s 7 building blocks, [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic]]'s brain/hands/session) into a single four-tuple that all of them can be expressed in.

2. **Meta-tool API as a formal surface.** The paper names `define_agent`, `run_code`, `process_memory` as the **meta-tools through which an agent — or a separate Refiner — edits *p*, *G*, *K*, *M* in place**. This is the **first wiki source that gives harness-editing-as-tool-call a tractable API signature**. [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *"harness is a living system, not a config file you set up once"* claim is operationalised here as a concrete set of tool calls the model itself can invoke.

3. **The capability floor.** *"A capability floor exists below which the refinement loop cannot bootstrap: Flash-Lite stalls below 20% on Emerald, and every Continual Harness variant on Flash-Lite underperforms the minimalist baseline."* This is **the sharpest qualifier yet in the wiki** for naive readings of *"harness > model"* claims. Below a model-capability threshold, harness engineering doesn't help — and may actively hurt. Strongest single empirical anchor against the *"infinite scaffolding can rescue any model"* corollary that some practitioner sources (Chatterjee, Tan) flirt with rhetorically.

### Closure on the Meta-Harness primary-source open question

The wiki has carried an open question on the **Khattab "Meta-Harness"** paper since the [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]] ingest cited it second-hand. Karten et al.'s reference [10] **closes the identification**:

> **Y. Lee, R. Nair, Q. Zhang, K. Lee, O. Khattab, and C. Finn. *Meta-harness: End-to-end optimization of model harnesses.* arXiv preprint arXiv:2603.28052, 2026.**

O. Khattab is the DSPy author; the author list confirms this is the **DSPy-team Meta-Harness paper** Osmani referenced via Viv Trivedy. **Triple-confirmed 2026-05-17** by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]] independently citing arXiv:2603.28052v1. The PY video adds one substantive detail Karten doesn't: **Meta-Harness reached rank 1 on TerminalBench with [[Haiku]]** — a small frontier model — *"proving a smaller model with a better harness can outrank larger models."* Strongest single statement in the wiki to date of the *"small model + great harness beats large model + bad harness"* claim. The identification open-question is now reduced to a **primary-source ingest target**: arXiv:2603.28052.

### Closure on the Pan et al. primary-source open question

The wiki has carried an open question on the **Pan et al. "Natural-Language Agent Harnesses" (Tsinghua, March 2026)** paper since the [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]] ingest cited it second-hand. **Closed 2026-05-17** by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]]:

> **Pan et al., *Natural-Language Agent Harnesses* — arXiv:2603.25723, March 2026.**

The PY description triple-confirms the substantive empirical anchors the wiki has been carrying second-hand: (a) **LangChain Top 30 → Top 5 on TerminalBench 2.0 by changing only harness infrastructure** (this turns out to be the canonical Pan et al. result — *the same datapoint [[2026-05-15-osmani-agent-harness-engineering|Osmani]] attributes to "Viv's team" originates with Pan et al.*); (b) **Full vs. stripped harness configurations achieve the same ~75% pass rate on SWE-bench while the bloated version burns 14× the compute**; (c) **Verifier addition hurts OSWorld by -8.4** (the canonical *"why do verifiers hurt"* anchor); (d) **NL-control-logic migration improves OS-Symphony accuracy 30.4% → 47.2%**. Now reduced to **primary-source ingest target**: arXiv:2603.25723.

### Subtraction discipline: when to *remove* structure

[[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY's video]] closes with the framing *"knowing when to **remove** structure rather than add it."* This sits in productive tension with [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] **ratchet** discipline (*"every line in AGENTS.md should be traceable back to a specific thing that went wrong"*) — Osmani's framing implies the harness grows; PY's framing (anchored in the Pan et al. **verifier-hurts** ablation result and the **stripped configuration at equivalent quality** finding) implies the harness *should sometimes shrink*. The wiki holds both as a **bidirectional discipline**:

- **Add** a constraint when you've seen a real failure (Osmani's ratchet, [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten's]] CRUD-create).
- **Remove** a constraint when a capable model has made it redundant *or when ablation shows it hurts* (PY framing, Karten's CRUD-delete — *"deletes entries not invoked productively"*).

The subtraction direction is the wiki's strongest single corrective to *"infinite scaffolding can rescue any model"* readings of the harness-as-moat claim.

### New primary-source ingest targets surfaced (not yet ingested)

The PY description names two harness-engineering arxiv papers not previously in the wiki: **AutoHarness** (arXiv:2603.03329, Feb 2026 — *"improving LLM agents by automatically synthesizing a code harness"*) and **AgentSpec** (arXiv:2503.18666 — *"Customizable Runtime Enforcement for Safe and Reliable LLM Agents"*). Also: **Anthropic's *Effective Harnesses for Long-Running Agents*** (Nov 2025) — predating the [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents]] post by ~5 months on the same architecture argument — is a vendor-side primary-source the wiki should ingest before the cluster expands further.

## The March 2026 academic-anchor triple — and the December 2024 foundational vendor anchor

The wiki's **2026-05-17 ingest batch** (later in the day, after the morning's Karten / Nodus Labs / PY ingests) added **seven** primary sources that close nearly every open empirical-anchor question on this concept page:

| Source | Date | Vantage | Load-bearing contribution |
|---|---|---|---|
| [[2024-12-19-anthropic-building-effective-agents\|Anthropic *Building Effective Agents*]] (Schluntz & Zhang) | **Dec 2024** | **The foundational vendor primary** | Workflows-vs-agents architectural distinction; 5 composable patterns (chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer); 3 core principles (simplicity / transparency / careful ACI); MCP first introduced as part of the agentic systems architecture. **Predates the *naming* of "harness engineering" by 14-17 months while articulating the construct in mature form** |
| [[2025-11-26-anthropic-effective-harnesses-long-running-agents\|Anthropic *Effective Harnesses for Long-Running Agents*]] (Young) | **Nov 2025** | Vendor-engineering pattern for multi-context-window work | **Initializer agent + coding agent + feature_list.json + claude-progress.txt + git** as the canonical pattern. ***"Compaction isn't sufficient"*** at frontier-model scale. JSON over Markdown for agent-edited persistent state. 4 named failure modes + structured solutions. The production-engineering origin of what [[2026-03-26-pan-natural-language-agent-harnesses\|Pan]] later formalises as path-addressable, compaction-stable file-backed state |
| [[2026-02-17-langchain-improving-deep-agents-harness-engineering\|LangChain *Improving deep agents with harness engineering*]] | **Feb 2026** | Framework-vendor primary | Names "harness engineering" as a discipline alongside [[2026-02-11-lopopolo-codex-harness-engineering\|OpenAI Codex / Lopopolo]] (Feb 2026); likely source of the *"Top 30 → Top 5 on TerminalBench 2.0"* claim circulating in secondary summaries (PY video, Osmani). **Metadata-only at this ingest** — substantive body not captured |
| [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis\|AutoHarness (Lou, Lázaro-Gredilla, Dedieu, Wendelken, Lehrach, Murphy)]] | **March 2026** | **Google DeepMind academic primary; harness-synthesis-via-search vantage** | **78% of Gemini-2.5-Flash chess losses are illegal moves** (motivating empirical anchor for "agent failures are usually harness failures"). Three harness types: action-filter / action-verifier / **harness-as-policy** (the LLM generates pure code policy; zero inference-time LLM calls). Thompson-sampling tree search over code refinements. **Gemini-2.5-Flash + AutoHarness wins 9/16 2P games vs Gemini-2.5-Pro** at significantly lower cost. Harness-as-Policy 0.870 reward beats GPT-5.2-High 0.844 at near-zero inference cost. **The earliest of the four academic primaries** |
| [[2026-03-26-pan-natural-language-agent-harnesses\|Pan, Zou, Guo, Ni, Zheng — *Natural-Language Agent Harnesses*]] (Tsinghua + HITSZ) | **March 2026** | **Academic primary; harness-representation vantage** | NLAH (Natural-Language Agent Harnesses) + IHR (Intelligent Harness Runtime). 5 NLAH ingredients: contracts / roles / stage structure / adapters / state semantics + failure taxonomy. Three RQs answered. **The "Verifier hurts OSWorld -8.4" claim** (Δ from Basic baseline 41.7) **closed and verified**. **The "OS-Symphony NL migration 30.4% → 47.2%" closed and verified**. **The "14× compute reduction at equivalent SWE-bench pass rate" closed and verified** (Table 1: TRAE w/o HS vs Full IHR). |
| [[2026-03-30-lee-meta-harness-end-to-end-optimization\|Lee, Nair, Zhang, Lee, Khattab, Finn — *Meta-Harness*]] (Stanford + KRAFTON + MIT) | **March 2026** | **Academic primary; harness-search vantage** | **The 6× single-benchmark performance gap headline claim** (the wiki's strongest single-sentence anchor for *"harness > model"*). Outer-loop search with **Claude Code (Opus-4.6) as proposer reading full filesystem of all prior candidates** (median 82 files / iteration). **Raw traces > summaries empirically anchored** (Table 3: Scores-only 34.6 / Scores+Summary 34.9 / Full filesystem 50.0). **Meta-Harness #2 on Opus 4.6 (76.4%) and #1 on Haiku 4.5 (37.6%) on TerminalBench-2** (the substantive *"small model + great harness > large model + bad harness"* anchor). **Transferability across 5 held-out models** on math reasoning (+4.7 pts avg). **Closes the wiki's 2-week-old "Meta-Harness paper" identification open question** primary-source. |
| [[2025-07-31-wang-agentspec-runtime-enforcement-llm-agents\|Wang, Poskitt, Sun — *AgentSpec*]] (Singapore Management University; **ICSE '26 accepted**) | **July 2025** | **Peer-reviewed academic primary; harness-safety vantage** | **First peer-reviewed paper in the wiki's harness cluster.** Domain-specific language with `rule / trigger / check / enforce / end` syntax for runtime enforcement. Built on LangChain 0.13.13; framework-agnostic. **Prevents >90% unsafe code executions; eliminates all hazardous embodied actions; 100% AV compliance in 5/8 law scenarios**. LLM-generated rules (OpenAI o1, few-shot): 87.26% / 95.56% / 5-of-8 enforcement precision. **Operationalises [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee's]] Constraints layer as a formal DSL**. Millisecond-scale overhead. |

### The construct's history is older than its name

This batch makes one structural point explicit: **the *construct* of harness engineering predates its *naming* by 14-17 months**. Anthropic's *Building Effective Agents* (December 19, 2024) articulates the construct in essentially mature form (workflows-vs-agents distinction + 5 patterns + 3 principles + ACI framing) before any practitioner had named it as a discipline. The *naming* happened in **February 2026**, when [[2026-02-11-lopopolo-codex-harness-engineering|OpenAI Codex / Lopopolo]] and [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain]] independently published posts using *"harness engineering"* as the noun phrase within ~one week of each other. The 14 intervening months were spent rediscovering, formalising, and operationalising what was already in Anthropic Engineering's December 2024 post.

This sharpens [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *"the harness is older than its discipline"* observation: by the time the practitioner-essay literature named harness engineering (Feb-May 2026), the architecture was already shipping in production at multiple frontier vendors and being formalised academically at three independent research groups (Tsinghua + Stanford/MIT + Google DeepMind) within 25 days of each other (March 5 → March 30, 2026).

### Closed open questions (all closed in this batch)

| Open question | Status |
|---|---|
| ~~Pan et al. (Tsinghua) primary-source identification~~ | **Closed** — arXiv:2603.25723. Closed twice (PY video + this paper ingest). |
| ~~Pan et al. primary-source ingest~~ | **Closed** — full paper read; key results verified. |
| ~~Lee/Khattab Meta-Harness identification~~ | **Closed** — arXiv:2603.28052. Closed twice (Karten reference [10] + PY description). |
| ~~Lee/Khattab Meta-Harness primary-source ingest~~ | **Closed** — full paper read; all three empirical anchors (TerminalBench-2 / text classification / math reasoning + transferability) verified. |
| ~~Why do verifiers hurt? (OSWorld -8.4)~~ | **Verified empirically**; mechanism partially named (Pan: *"verifier-level acceptance can still diverge from benchmark-level acceptance"*). Causal mechanism still partially open. |
| ~~Raw traces > summaries~~ | **Closed — verified by ablation** (Lee Table 3). |
| ~~Transferability of harnesses across models~~ | **Closed — verified empirically**: Lee's math retrieval harness transfers across 5 held-out models (+4.7 avg). |
| ~~Trivedy / Chatterjee author-attribution flag~~ | **Partially clarified but not closed** — Pan et al. reference 16 reveals a *third* "Anatomy of an Agent Harness" post (LangChain, March 10, 2026) that the wiki has not yet ingested. The Trivedy / Chatterjee / LangChain "Anatomy" thicket may be **three separate posts**, not one. New ingest target: the LangChain March 10, 2026 post. |
| ~~"Top 30 → Top 5 on TerminalBench 2.0" attribution to Pan et al.~~ | **Re-attributed**. **Not in Pan's paper.** Likely from [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain blog]] or the as-yet-unfetched March 10 LangChain *Anatomy of an Agent Harness* post. Lee et al.'s TerminalBench-2 results (#2 on Opus 4.6 at 76.4%, #1 on Haiku 4.5 at 37.6%) are precise but don't use the "Top 30 → Top 5" framing. |

### Adjusted attribution map (post-batch)

The wiki's prior attributions need three updates:

- **The "78% of Gemini-2.5-Flash chess losses are illegal moves" claim** — primary source is now [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|AutoHarness / Lou et al. (DeepMind)]], not generic practitioner literature.
- **The "Top 30 → Top 5 on TerminalBench 2.0 by changing only harness infrastructure" claim** — primary source is **most likely [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain's]] *Improving deep agents with harness engineering* (Feb 17, 2026) or the sister LangChain post *The anatomy of an agent harness* (March 10, 2026)** — NOT Pan et al. or Lee et al.
- **The "6× performance gap on the same benchmark" framing** — primary source is now [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al.]] (opening sentence of Meta-Harness paper, citing Bui as reference [47]).

### Reset-free is structurally important (not just convenient)

Karten et al. articulate a sharper version of the *reset-free is the practically dominant regime* argument the wiki has been carrying since [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]:

- **Failure signatures accumulate monotonically.** Earlier failures remain available to all subsequent refinement passes; reset-based methods restart this accumulation after each update.
- **Deep-in-episode failures are unreachable to reset-based methods by construction.** Late-game battles, multi-step puzzles, dialogue chains — none can be refined against by methods that reset to initial state.
- **Reset-free is the practically dominant regime** *"for long-running coding agents, embodied agents, and ops tasks where free environment resets are costly or unavailable."*

The wiki's existing **Compounding** layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]) and **process-reward** ([[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie]]) framings are subsumed by this: Karten's Refiner is the Compounding layer operationalised on a sliding-window pairwise PRM with reset-free state propagation.

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
- **~~Primary-source identification: Pan et al. (Tsinghua, March 2026).~~** **Closed 2026-05-17** by [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]]: **Pan et al., *Natural-Language Agent Harnesses* — arXiv:2603.25723, March 2026**. Open question now reduced to **primary-source ingest** of arXiv:2603.25723, which would substantiate the SWE-bench verified ablation results, the OS-Symphony migration deltas (30.4% → 47.2%), the Verifier-hurts-OSWorld result (-8.4), and the 14×-compute-reduction-at-equivalent-SWE-bench-pass-rate observation.
- **~~Primary-source identification: Khattab et al. (DSPy team, Meta-Harness).~~** **Closed 2026-05-17** by [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] reference [10]: **Y. Lee, R. Nair, Q. Zhang, K. Lee, O. Khattab, and C. Finn — *Meta-harness: End-to-end optimization of model harnesses* — arXiv:2603.28052, 2026.** Open question now reduced to **primary-source ingest** of arXiv:2603.28052 itself, which would substantiate the Terminal Bench 2 76.4%, the **transferability across five models** claim, and the *raw-traces-irreplaceable* finding (50% → 34% accuracy when traces removed; 34.9% when summarised — the signal lives in the raw failure detail).
- **Does the "raw traces > summaries" finding generalise?** Khattab et al. specifically tested this on auto-harness optimisation. If it holds for *any* compounding-loop telemetry (per Chatterjee's *Compounding* layer), it has a sharp design implication: **never summarise telemetry before the meta-learning loop reads it.** Worth tracking against future ablation work.
- **How much of the 7-building-block / 4-layer architecture is novel vs. rebranded?** Kokane's "10% genuinely novel" is a plausible-sounding heuristic, but it is rhetorical, not measured. A controlled comparison (build the same system using mature systems-engineering vocabulary vs. agent-harness vocabulary, measure delta in correctness/cost/time) would settle the rhetorical dispute.
- **The Claude Code leak.** Referenced in both new sources but not directly ingested. If a primary-source ingest becomes possible, it would substantiate or challenge the harness-pattern claims that currently rest on second-hand interpretation.
- **Why do verifiers actively hurt?** Pan et al.'s ablation shows verifiers degrade SWE-bench by 0.8 and OS World by 8.4. Mechanism unstated. Hypothesis: verifier-driven retries dilute the agent's confidence calibration, or verifiers add noise faster than they catch real failures. Worth tracking against future ablation work.
- **Manus and Warel as candidate entity pages.** Both named in [[2026-05-04-rethinking-agents-harness-is-all-you-need|the YouTube source]] as agent platforms with relevant operational claims (5× harness rewrites; −80% tools / +performance). Promote on second-source mention.
