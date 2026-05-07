---
type: source
kind: article
title: "The Anatomy of an Agent Harness"
author: ["Abhishek Chatterjee"]
publisher: "Medium"
journal_volume: "Medium, ~3 May 2026"
date_published: 2026-05-03
date_ingested: 2026-05-07
length: "~6 pages of body content (9-page PDF; 8-min reading time stated)"
raw: "../../raw/articles/The Anatomy of an Agent Harness. On the engineering that lives between a… _ by Abhishek Chatterjee _ May, 2026 _ Medium.pdf"
tags: [agent-harness, ai-agents, ai-product-management, context-management, constraints, contracts, compounding, claude-code, harness-moat, friday-in-march]
confidence: 0.75
last_confirmed: "2026-05-07"
---

# The Anatomy of an Agent Harness

A long-form practitioner essay on **Medium**, posted ~3 May 2026 ("4 days ago" at ingest), by **Abhishek Chatterjee** (building praxiomai.xyz — "world's best AI product manager agent" — and getpolaris.xyz; 17+ years software development; self-described "Claude code addict"). 8-min read. Anchored in a vivid production-failure story ("On a Friday in March, an agent we had built politely emptied a customer's workspace"). Argues that the **harness is the moat**: the model is rented and converging to commodity; the harness is owned and compounds.

The essay names a **4-layer anatomy** of agent harnesses (**Context / Constraints / Contracts / Compounding**) that complements [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] 7-component architectural diagram. Where Kokane is sceptical-provocative ("90% systems design rebranded"), Chatterjee is taxonomical-affirmative ("the harness is the only part of our stack that gets more valuable with every customer we ship to"). Both can be true and the wiki tracks them as complementary vantages on the same construct ([[agent-harness]]).

## TL;DR

- **The Friday-in-March story**: a user told the agent "clean things up before the board review"; the agent — *competent, helpful, working exactly as designed* — interpreted this as archive stale documents + prune duplicates + remove stale sources, soft-deleting two weeks of research history 40 minutes before a board meeting. Each individual action defensible; the aggregate a small disaster. **The model was not the problem.** The problem lived in *the layer around the model* that should have recognized "clean up" as a destructive intent, paused before mass archiving, surfaced a preview, requested confirmation. *That layer did not exist yet. It does now. It is called the harness.*
- **The Equation Everyone Half-Knows**: **Agent = Model + Harness**. Most VC and discourse goes to the first term. *"This is a category error."* Models are converging to commodity (rent, swap, route, replace quarterly); the harness is what is owned and compounds.
- **Four layers of harness anatomy** (in build order):
  1. **Context** — the system prompt as a **document**, assembled fresh per request, with stable parts (cached at the KV layer) and dynamic parts (rebuilt per turn from user memory + workspace knowledge + delta summary + behavioral persona). *"Context is not a feature you bolt on. It is the room the agent walks into."*
  2. **Constraints** — middleware-pattern pre-tool and post-tool hooks (destructive-verb detection; workspace isolation; loop detection; output scoring across citation coverage / source triangulation / severity distribution / density / thematic diversity). The harness as **active editor**, not passive observer. *"Constraints, done well, do not feel like restrictions to the agent. They feel like the structure that keeps the work from drifting."*
  3. **Contracts** — formal, evaluable specifications of "successful output," **calibrated to inputs available** (a synthesis contract over 5 sources is not the same as one over 50). Functions, not checklists. Make agent failures *debuggable*. Domain-specific — encoding what "good" looks like in *your* domain is *the work nobody outside your team can do for you*.
  4. **Compounding** — structured telemetry records (**not log lines**: complexity classification with reasoning, contract score breakdown, tool latency/outcome/cost, active workspace overrides, applied learned preferences) that feed a nightly meta-learning loop proposing **harness adjustments** (not model fine-tuning — the model is rented and frozen). Human reviews; approved adjustments become workspace overrides that *compound over time*. *"This is what people mean when they say AI products will get better with use. They do not mean the model is learning. The model is frozen; you cannot fine-tune Claude in production. They mean the infrastructure around the model is learning, and the surface area where learning lives is the harness."*
- **The CEO sentence** (the version that lands in a boardroom): *"the model is rented from a vendor whose competitor will outperform them within the year; the harness — our memory architecture, our quality contracts, our learned per-customer overrides, our telemetry — is what we own and what compounds; it is the only part of our stack that gets more valuable with every customer we ship to."*
- **Closing aphorism**: *"The model is what you rent. The harness is what you own."*

## What was actually ingested

Full essay body — 6 pages of substantive content (9-page PDF; pages 1, 2-6, 7 are content + author bio; pages 8-9 are page-furniture / loading skeletons). The 8-min reading time is consistent with body length.

## The Friday-in-March story (the load-bearing example)

The opening anecdote is the essay's rhetorical anchor and worth quoting at length:

> "The user had asked it to 'clean things up before the board review.' The agent — competent, helpful, working exactly as designed — interpreted this as a request to archive stale documents, prune duplicate insights, and remove sources that hadn't been touched in a while. Each individual action was defensible. The aggregate was a small disaster. By the time the customer noticed, two weeks of research history was sitting in soft-deleted state and their board meeting was forty minutes away.
>
> We restored everything. We apologized. And then we did the more important work: we asked why our system had let this happen.
>
> The model was not the problem. The model had reasoned correctly given what it was asked. The problem lived in the layer around the model — the layer that should have recognized 'clean up' as a destructive intent, paused before mass archiving, surfaced a preview, requested confirmation. That layer did not exist yet. It does now."

The story does three things at once: (a) makes the harness layer concrete (we know exactly what was missing); (b) anchors the **Constraints** layer's destructive-verb-detection example; (c) establishes that **agent failures are usually harness failures, not model failures** — a claim that propagates through [[ai-agents]], [[responsible-ai]], and [[micro-productivity-trap]].

## The four layers — full treatment

### 1. Context — "the room the agent walks into"

The system prompt is **not a string. It is a document, assembled fresh on every request, from many sources, with deliberate structure.**

- **Stable parts** (top of the prompt): agent identity, workspace, rules. **Cached at the model's KV layer** and reused across thousands of requests. *"At scale this is not a stylistic choice. It is the difference between a sustainable cost curve and one that bankrupts you."*
- **Dynamic parts** (below): rebuilt every turn from
  - the user's accumulated memory
  - the workspace's accumulated knowledge
  - a delta summary of what has changed since the last conversation
  - a **behavioral persona inferred from what the user appears to be trying to do**
- *"The same model, asked to synthesize research versus draft a strategy memo, should not receive the same instructions. The harness's job is to recognize the difference and quietly inject the right scaffolding."*
- **The most expensive mistake**: passing a static system prompt and letting context retrieval happen later in tool calls, mid-conversation. The right context, **assembled before the first token is generated**, is the difference between an agent that produces a useful first draft and one that needs to be coaxed across three turns to reach baseline competence.

### 2. Constraints — middleware before/after every tool call

> *"Every tool call in a production agent should pass through a checkpoint. Most do not. This is the single most common failure I have seen in agents that work in demos and break in production."*

**Pre-tool hooks** (allow / modify / reject):
- destructive-verb recognition → route to soft alternatives (the Friday-in-March remediation)
- workspace-isolation checks (Customer A's agent cannot touch Customer B's data)
- **loop detection**: agent has called the same search 6 times → surface exhaustion warning rather than burn another twenty cents in tokens

**Post-tool hooks** (record / score / inject corrective context):
- score synthesized output across **citation coverage, source triangulation, severity distribution, density, thematic diversity**
- when output falls below threshold, *inject corrective context into the agent's next turn*: *"your last synthesis scored a C, here is why, try again with these specific corrections"*

The harness becomes an **active editor**, not a passive observer.

### 3. Contracts — formal, evaluable, input-calibrated

**Two failure modes around stopping**:
- agents stop *too early* (output technically answers the question, adds no value)
- agents stop *too late* (refining work that was already good until it becomes worse)

The **contract** is a formal specification of successful output **calibrated to the inputs available**. *"A synthesis contract over five research sources should not impose the same minimums as one over fifty. The contract is a function, not a checklist; it scales with context."*

After execution, the contract evaluates: passed / failed, score 0–1, specific issues enumerated. The harness then chooses: **accept, request a targeted revision, or surface the partial result with a note**.

> *"The most underrated benefit of contracts is that they make agent behavior **debuggable**. A failed run with a structured contract result tells you why it failed. A failed run without one leaves you reading transcripts."*

**Domain-specific by construction**: research synthesis ≠ competitive analysis ≠ customer-support reply. *"Encoding what 'good' looks like in your domain — explicitly, in evaluable form — is the work nobody outside your team can do for you. It is also the work that, once done, compounds: every contract you write makes the next agent you ship cheaper to build and faster to trust."*

### 4. Compounding — telemetry as training data for the harness itself

The fourth layer "**distinguishes a harness from a system, and a system from a product that gets better with age.**"

- Every execution emits a **structured telemetry record** — *not log lines*: complexity classification with reasoning, contract score with breakdown, tool calls with latency and outcome, cost in dollars, active workspace overrides, applied learned preferences. *"The shape of the record is the shape of the system's self-knowledge."*
- *"This telemetry is not for dashboards. It is training data for the harness itself."*
- A nightly process reads across executions and identifies patterns:
  - workspace whose synthesis runs consistently produce low citation coverage
  - user who consistently rejects the first draft and accepts the second
  - workflow where the agent loops on search more than the population mean
- Proposes adjustments **to the harness configuration, not the model** (the model is rented and frozen):
  - raise the minimum source threshold for this workspace
  - lower the complexity threshold for these query types
  - adjust the checkpoint frequency for this risk profile
- Proposals enter a queue with confidence scores and evidence; **a human reviews them**; approved adjustments become **workspace overrides** — durable changes that compound.

**The clearest articulation in the wiki of *what "AI products getting better with use" actually means*:**

> *"The model is frozen; you cannot fine-tune Claude in production. They mean the infrastructure around the model is learning, and the surface area where learning lives is the harness."*

This is operationally identical to [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage's]] verification → evaluation → learning capture flywheel — *same construct, two vocabularies*.

## What this means on a roadmap (Chatterjee's PM-facing prescriptions)

1. **The model decision matters less than your engineers think.** *"By the time you have shipped, there will be a better model. Plan for swap, not for marriage. Keep the harness model-agnostic where the cost of doing so is reasonable."*
2. **The harness investment is not a phase. It is a permanent allocation.** *"There is no version of this where you finish the harness. You build the first three layers in the first year and the fourth — the self-tuning compounding loop — in the second. Every quarter after that, you are calibrating, extending, hardening. This is the work."*
3. **Sequence matters. Build constraints before you build cleverness.** *"The Friday-in-March story repeats itself, in some form, in every AI product that has not yet built a hook layer. It is cheaper to build the layer than to write the apology emails."*
4. **The most under-resourced role on most AI teams is the engineer who specializes in this work.** *Not* a model researcher. *Not* a prompt engineer. *"Someone who thinks about agents the way SREs think about distributed systems: in terms of failure modes, observability, graceful degradation, and the long tail of edge cases that only emerge at production scale. Hire for this taste. It is rare and it compounds."*

## Cross-source positioning

- **Direct counterpart to [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]]**: same topic, opposite rhetorical stance. Chatterjee says "harness is the moat"; Kokane says "harness is mostly rebranded systems design with a 10% novel kernel." Both can be true — Kokane is right that the *primitives* are mature systems engineering; Chatterjee is right that the *aggregate, in production, calibrated to a domain* is what compounds and differentiates.
- **Strong cross-source agreement with [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]**: Chatterjee's Constraints layer ("validate intent, not just output format") is the application-layer counterpart to Anthropic's brain/hands decomposition (the executor decides whether to run model-emitted tool calls — security as structural unreachability). Same architectural commitment, different vantage.
- **Strong cross-source agreement with [[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage 2026]]**: Chatterjee's **Compounding** layer = Kiron-Schrage's **verification → evaluation → learning capture** flywheel. Independent convergence of two practitioner essays on the same operational mechanism, from different vantages (PM-facing engineering essay vs. MIT SMR column). Lifts the Kiron-Schrage flywheel from single-source to confirmed cross-source.
- **Reinforces [[micro-productivity-trap]]**: the Friday-in-March story is a textbook process-lock-in failure. Chatterjee's prescription ("Build constraints before you build cleverness") is the operational rule that escapes it.
- **Connects to [[ai-agents]] and [[responsible-ai]]**: agent failures are usually *harness failures* not *model failures*; the Constraints layer is where RAI policies operationalize at runtime.
- **Connects to [[foundation-models]]**: the "models are converging to commodity" argument is the strongest version in the wiki of the rent-vs-own framing. Worth a light enrichment.

## Source-quality flag

- **Strengths**: vivid load-bearing anecdote (Friday-in-March) makes the harness concept *concrete* in a way prior wiki sources have not; clear taxonomic structure (4 layers in build order); well-articulated PM-facing prescriptions; the *infrastructure-as-city* metaphor (buildings/roads/substation/drainage) is durable. Author is a working practitioner (building an AI PM agent product); the essay reads as battle-tested rather than theoretical.
- **Caveats**: opinion essay, not empirical research — no data, no n, no benchmarks. The author's company (praxiomai.xyz, getpolaris.xyz) has commercial interest in the "harness is the moat" framing; treat as practitioner-vantage rather than independent. Single-source on the Friday-in-March story (anonymized customer; details non-verifiable). Lower follower count (49 followers at ingest) suggests the article hasn't yet been peer-validated by the practitioner community at scale, though within ~30 days of ingest it could rise.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.7 + 0.05 additional supporting source (Kokane 2026 + Anthropic Managed Agents + Kiron-Schrage 2026 mutually reinforce the harness construct from different vantages) = **0.75**. Not raised to 0.80 because the source is opinion-format with no empirical anchor.

## Open questions

- The **Compounding layer** describes a *self-tuning meta-learning loop with human review*. Is there a wiki source measuring how well this works in practice (e.g., harness-tuning lift on contract scores over time)? If a future source quantifies the compounding rate, this becomes one of the wiki's first measurable claims about *AI products that get better with use*.
- **Does the "model decision matters less" thesis hold across model generations?** Anthropic Managed Agents found that Sonnet 4.5's "context anxiety" was absent on Opus 4.5 — same family, different reliability. If model-within-family variation is large, the "plan for swap" prescription needs nuance.
- **Domain-specificity of contracts**: Chatterjee says encoding what "good" looks like in *your* domain is "the work nobody outside your team can do for you." Is there an emerging market for *contract templates* by domain (legal synthesis, customer support, code review)? Worth tracking as a possible 2026–27 wiki concept.
