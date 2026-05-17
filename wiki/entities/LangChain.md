---
type: entity
kind: organization
aliases: ["LangChain", "LangChain Inc"]
tags: [langchain, agent-frameworks, agent-runtime, agent-harness, langgraph, langsmith, deep-agents]
since: 2022
confidence: 0.80
last_confirmed: "2026-05-10"
accessed_at: "2026-05-10"
source_count: 4
relationships:
  - type: published-by
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "company blog publishes the Agent Development Lifecycle thesis-piece"
---

# LangChain

A US-based AI company building **agent-engineering infrastructure**. Founded in 2022 by **Harrison Chase** as the open-source [`langchain`](https://github.com/langchain-ai/langchain) Python framework; expanded over 2023–26 into a layered product stack covering most of the [[agent-development-lifecycle|Agent Development Lifecycle]]. The company entered the wiki as a **named-but-unsubstantiated organization** across [[agent-harness]], [[ai-agents]], and [[generative-ai]] before [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]] (9 May) supplied the first first-party LangChain source — at which point the cumulative-mention threshold for entity promotion was met.

## Why LangChain matters in this wiki

LangChain's product stack is the **clearest worked example** of the four-layer Build vocabulary [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]] articulates — *frameworks / runtimes / harnesses / no-code* — because LangChain ships at every layer:

| Layer ([[2026-05-09-chase-agent-development-lifecycle\|Chase 2026]]) | LangChain product | What it is |
|---|---|---|
| **Frameworks** | LangChain | Open-source abstractions for model calls, tools, prompts, retrieval, structured outputs, agent loops |
| **Runtimes** | LangGraph | Stateful agent runtime; control flow / branching / looping / persistence / pause-resume |
| **Harnesses** | Deep Agents | Prompts, skills, MCP servers, hooks, middleware, memory, virtual filesystem |
| **No-code** | LangSmith Fleet | Domain-expert-facing UI to create and configure agents without code |
| **Test / Deploy / Monitor** (lifecycle phases) | LangSmith Platform (Observability, Evaluation, Deployment, Sandboxes) | Tracing, evals, durable runtime, sandboxes |

This makes LangChain a **vendor whose product taxonomy *is* the wiki's vocabulary** for the [[agent-development-lifecycle|ADLC]] — both because Chase coined the four-layer Build split, and because LangChain ships at all four layers.

## Products referenced in this wiki

- **LangChain** (the framework) — the original 2022 release; agent abstractions over LLM providers.
- **LangGraph** — agent runtime for stateful, durable, human-in-the-loop graph-shaped workflows.
- **Deep Agents** — open-source pattern (`langchain-deep-agents`) demonstrating the harness layer with virtual-filesystem-as-working-memory.
- **LangSmith** — eval/observability/deployment platform.
  - **LangSmith Platform** — the umbrella.
  - **LangSmith Observability** — traces, signals, feedback, dashboards.
  - **LangSmith Evaluation** — datasets, metrics, experiments.
  - **LangSmith Deployment** — durable agent runtime hosting.
  - **LangSmith Sandboxes** — isolated execution environments.
  - **LangSmith Fleet** — no-code agent configuration.
  - **LangChain Academy** — educational resources.

## Concepts LangChain co-shapes in this wiki

- [[agent-development-lifecycle]] — Chase's 4-phase + governance ring is the wiki's second formalization of the ADLC and the source most influential on the concept page's current shape.
- [[agent-harness]] — the *frameworks vs. runtimes vs. harnesses vs. no-code* sub-layering refines the wiki's harness vocabulary.
- [[ai-agents]] — LangChain has been named throughout the wiki as a top-of-mind framework when the topic is agent abstractions.
- [[generative-ai]] — LangChain is named in the deployed-tools landscape.

## People

- **Harrison Chase** — co-founder/CEO of LangChain. **First wiki source mention by name** is [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]]. Per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion), do not promote to entity page on a single source — listed as Dangling. Promote on second-source mention.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "langchain") OR contains(tags, "langgraph") OR contains(tags, "langsmith") OR contains(tags, "deep-agents")
SORT file.name ASC
```

## Open questions

- **Customer evidence**. The wiki has not yet ingested a customer case study deploying LangChain at production scale. Chase's piece references "LangSmith customers" abstractly; substantive case studies would substantiate concept pages further.
- **Open-source community vs. commercial product**. LangChain straddles open-source (the `langchain` framework, LangGraph, Deep Agents) and commercial (LangSmith Platform). The boundary is operationally important for procurement and lock-in concerns; the wiki has not yet substantiated it.
- **Comparative positioning**. CrewAI, Claude Agents SDK, AWS AgentCore, Daytona, E2B, Temporal, n8n are all named alongside LangChain in [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]]. None has been substantiated independently. A market-landscape source (analyst report, comparison study) would resolve the relative positioning question.
