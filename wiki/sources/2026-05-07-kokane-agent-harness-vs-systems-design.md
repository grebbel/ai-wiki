---
type: source
kind: article
title: "What is Agent Harness? How it is different than System Design?"
author: ["Akshay Kokane"]
publisher: "Level Up Coding (Medium)"
journal_volume: "Level Up Coding, 10 April 2026"
date_published: 2026-04-10
date_ingested: 2026-05-07
length: "~4 pages of body content (8-page PDF; 4-min reading time stated)"
raw: "../../raw/articles/What is Agent Harness_ How it is different than System Design_ _ by Akshay Kokane _ Apr, 2026 _ Level Up Coding.pdf"
tags: [agent-harness, systems-design, ai-agents, llm-non-determinism, context-management, claude-code-leak, harness-frameworks, langchain, microsoft-agent-framework]
confidence: 0.70
last_confirmed: "2026-05-07"
---

# What is Agent Harness? How it is different than System Design?

A **provocation-style practitioner article** in *Level Up Coding* (Medium publication, 326K followers), 10 April 2026, by **Akshay Kokane** (Enterprise AI Architect, ex-Microsoft, ex-AWS). 4-min read. Argues that the term "agent harness" is mostly a **rebranding of systems design that engineers have been doing for decades**, with a small but genuine ~10% kernel of novelty. Anchored in observations from the (then-recent) **Claude Code source-code leak** that surfaced Anthropic's internal harness patterns.

The article is part of a small wave of "agent harness" essays appearing across the practitioner blogosphere in April–May 2026 — alongside [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's The Anatomy of an Agent Harness]] (Medium, 4 days before this ingest) and pieces from LangChain, Salesforce, and DistributedApps.ai. This source is the *most sceptical* of the three — useful as the rhetorical counterweight to the "harness is the moat" framing.

## TL;DR

- **Agent harness** ≈ a runtime layer wrapping an LLM with: context manager, permission/guardrails, state/memory, tool executor, retry/error handler, human-in-the-loop, observability.
- **The provocation**: most of what "agent harness" describes is **systems design we've always done** (cache management, database + job queue, API middleware, approval workflows, summarization + offload, process lifecycle). The patterns are identical — only the wrapped surface (an LLM instead of a database driver) is new.
- **Three reasons for the rename**: (1) genuine — LLMs introduce **non-determinism at the core logic layer**, requiring intent-validation rather than just output-format validation; (2) cynical — companies need a category to sell; (3) cynical — new entrants need vocabulary, and incumbents who coin it get the SEO/mindshare.
- **What's actually new** (per the Claude Code leak): (a) non-determinism at the execution layer (classical middleware assumes the wrapped service behaves consistently; LLMs don't); (b) **context as a first-class degrading resource** (working memory that actively gets worse the longer it runs; "garbage collection is not the same thing as semantic drift correction").
- **Honest verdict**: 90% systems design + 10% genuinely novel. "If you've shipped real backend systems, you're already 80% of the way there."

## What was actually ingested

Full article body — 4 pages of substantive content (an 8-page PDF; pages 1–5 are content + references, pages 6–8 are author bio + page-furniture / loading skeletons). The 4-min reading time stated by the publisher is consistent with the body length.

## The 4-layer architecture (Kokane's diagram)

Kokane presents AI applications as a **4-layer stack**, with the Agent Harness as the runtime layer:

| Layer | What it does | Examples |
|---|---|---|
| **1. Your App** | Business logic, the product, what the user sees | (any AI product) |
| **2. Harness Frameworks** | Pre-assembled harness kits — chains, agents, memory modules, tool wrappers | LangChain / LangGraph (chains, agents, memory, tools, LCEL); **Microsoft Agent Framework v1.0** (agents, graph workflows, HITL, state, A2A, MCP — successor to Semantic Kernel + AutoGen, GA April 2026); Google Agent Development Kit; LlamaIndex; CrewAI; Haystack; DSPy |
| **3. Agent Harness (runtime layer)** | Context manager, permission & guardrails, state & memory, tool executor, retry/error handler, human-in-the-loop, observability | (the runtime itself; frameworks in Layer 2 implement these primitives under the hood) |
| **4. Model Layer (swappable)** | Indeterministic core engine; generates results from user requests | Azure OpenAI / GPT-5; Claude (Anthropic); Gemini / Llama / Ollama; AWS Bedrock |

**Building blocks** of Layer 3 in detail (per Kokane's first diagram):
- **Context manager**
- **Permission & guardrails**
- **State & memory**
- **Agentic loop / Orchestrator** (containing: LLM/Model — inference only; Tool Executor — execution only; Retry & error handler; Human-in-the-loop)
- **Observability**

The architectural separation between **inference-only** (model) and **execution-only** (tool executor) directly echoes [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]'s **brain / hands** decomposition — the same pattern named differently.

## The rename, mapped out

The article's most quotable artifact — a side-by-side translation table:

| Agent Harness term | What we called it before |
|---|---|
| Context management | Session / cache management |
| State persistence | Database + job queue |
| Tool orchestration | API middleware |
| Human-in-the-loop | Approval workflows |
| Context rot | Memory leak / stale state |
| Compaction | Summarization + offload |
| Harness lifecycle | Process / worker lifecycle |

The argument: *"The patterns are identical. What changed is the surface you're wrapping: instead of a database driver or an HTTP client, you're wrapping an LLM. And that one difference is actually doing a lot of work."*

## Why the new term exists — three reasons (one genuine, two cynical)

### 1. Genuine: non-determinism at the core logic layer

LLMs **hallucinate tool calls, return semantically wrong responses, lose track of original goals 40 turns in**. Old retry-and-log infrastructure isn't enough — you need to **validate intent, not just output format**. The Claude Code permission pipeline confirms this: it doesn't just check if a tool call is syntactically valid, it checks whether the model is **authorized to want what it wants**.

### 2. Cynical #1: category creation as commercial play

> "Companies need a platform to sell. Naming existing patterns as new primitives creates a new market. If 'agent harness' is a category, they can own the category."

### 3. Cynical #2: SEO + vocabulary capture

> "A lot of people entering AI engineering are not systems engineers. They need vocabulary. And incumbents who coin the vocabulary get the SEO, the conference talks, and the mindshare. That's a rational business move, not a technical contribution."

## What is actually new (the 10% kernel)

The Claude Code leak makes two patterns concrete that don't map cleanly onto prior systems design:

1. **Non-determinism at the execution layer.** Classical middleware assumes your wrapped service behaves consistently. LLMs don't. *You can't unit test for it. You can't formally specify it.* That requires a new design discipline.
2. **Context as a first-class degrading resource.** *"We've never had to architect around working memory that actively gets worse the longer it runs. Garbage collection is not the same thing as semantic drift correction."* The named phenomenon is **context rot** — semantic-quality decay as conversations accumulate.

## The honest verdict

> *"90% of agent harness engineering is systems design you already know, applied to a new substrate. The remaining 10% is genuinely novel: designing around non-deterministic outputs and finite, degradable context windows. The Claude Code leak didn't reveal a new paradigm. It confirmed that the best engineers in AI are doing what good engineers always do — wrapping complexity in clean abstractions. Don't let the vocabulary make you feel like a beginner. But respect those 10% edge cases. That's where production agents actually fail."*

The practical implication for engineers: **"If you've shipped real backend systems, you're already 80% of the way there. Your instincts on retries, state machines, idempotency, and observability are directly transferable. The skill gap isn't architecture. It's learning to think about prompt state as program state, and treating the context window as your most constrained and most expensive resource."**

## The Claude Code leak (referenced source)

Both this article and [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] reference a **leak of Anthropic's Claude Code source code** that occurred shortly before April 2026. The leak surfaced 10 agentic AI harness patterns analysed at length by DistributedApps.ai (Ken Huang substack) and reported in arstechnica ("a persistent agent, stealth 'Undercover' mode, and… a virtual assistant named Buddy?"). Kokane uses the leak as evidence that *"even Anthropic, building the most capable coding agent on the planet, is solving for those same constraints with the same fundamental tools we've always had."*

This source does not link to any of these references in a way the wiki can directly ingest, but they are flagged here as **dangling 2nd-source candidates** for future ingestion. The leak itself is not separately ingested.

## Cross-source positioning

- **Direct co-reference with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]**: Kokane's article cites Vivek Trivedy's *The Anatomy of an Agent Harness* (LangChain blog) — a different piece from Chatterjee's similarly-titled Medium article, but the lineage is shared. Both Kokane and Chatterjee are in the same ~30-day "agent harness" essay wave (April–May 2026).
- **Reinforces [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]**: Kokane's "inference-only model + execution-only tool executor" maps directly to Anthropic's brain/hands decomposition. Same engineering pattern, different vocabulary.
- **Connects to [[ai-agents]]**: provides the *application-layer* anatomy beneath the chatbot → agent → multi-agent progression.
- **Connects to [[micro-productivity-trap]]**: the harness IS the operational machinery that escapes the trap; without it, orgs are stuck in consumption mode.
- **Tension with the rest of the wiki's "harness as moat" framing**: Kokane's *"don't let the vocabulary make you feel like a beginner"* is a useful corrective to the [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / Boris Cherny / [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage]] framing that the harness is *the* differentiator. Both can be true: harness work is mostly mature systems engineering applied to a new substrate, *and* it's where AI products differentiate themselves at the application layer.

## Source-quality flag

- **Strengths**: practitioner author with explicit credentials (ex-Microsoft, ex-AWS, currently Enterprise AI Architect / Forward Deployed Engineer); recent (publication 27 days before ingest); concise and well-illustrated with diagrams; contributes a useful side-by-side rename table.
- **Caveats**: opinion essay, not empirical research. The "Claude Code leak" anchor is third-hand (Kokane is interpreting analyses of the leak by others, not reading the source directly). Some of the historical claims ("Microsoft Agent Framework v1.0 GA April 2026") are time-sensitive and should be verified against primary sources before being treated as authoritative.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.7 (single supporting source) — opinion-format article with no empirical anchor; not raised to 0.75. Single-source mention of the Claude Code leak is *not* equivalent to confirmation; treat as speculation about Anthropic's internal practices. The article's main contribution is the rhetorical sceptical-vantage framing, which is durable even if specific factual claims about the leak need cross-validation.

## Open questions

- The "Claude Code leak" is referenced in both new harness articles ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] also references it implicitly via Trivedy's blog). Worth tracking if the wiki gains a primary source on the leak itself.
- **Microsoft Agent Framework v1.0** is named as the successor to Semantic Kernel + AutoGen, GA April 2026 — single-source claim warrants verification before treating as wiki canon.
- The "10% genuinely novel" framing (non-determinism + context-as-degrading-resource) is a strong claim worth tracking across future sources. If [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]'s Constraints + Contracts layers are operationally what the 10% novel work consists of, the two articles together imply: *the genuinely-novel-engineering work is enforcing semantic constraints (intent validation) and contract-based stopping criteria* — both of which require domain expertise that classical middleware doesn't.
