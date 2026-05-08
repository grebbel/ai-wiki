---
type: source
kind: article
title: "Agents CLI in Agent Platform: create to production in one CLI"
author: ["Ivan Cheung", "Pier Paolo Ippolito", "Elia Secchi"]
publisher: "Google"
journal_volume: "Google Developers Blog, 22 April 2026"
url: ""
date_published: 2026-04-22
date_ingested: 2026-05-08
tags: [ai-agents, google, google-cloud, agent-platform, agents-cli, adk, agent-development-lifecycle, harness, harness-frameworks, coding-agents, gemini-enterprise, cloud-run, gke, agent-runtime, mcp, a2a, build-agents-with-agents]
length: "~5 pages (full article body, footer/related-posts excluded)"
raw: "../../raw/articles/Agents CLI in Agent Platform_ create to production in one CLI - Google Developers Blog.pdf"
---

# Cheung, Ippolito, Secchi — Agents CLI in Agent Platform: create to production in one CLI

## TL;DR

A **Google Developers Blog** announcement (22 April 2026) by Ivan Cheung (Software Engineer), Pier Paolo Ippolito (GenAI Field Solutions Architect), and Elia Secchi (Solutions Specialist) introducing **Agents CLI in Agent Platform** — a single command-line tool that bundles every stage of the **Agent Development Lifecycle (ADLC)** on Google Cloud: scaffold, evaluate, deploy, publish, observe.

The framing is unusually explicit: **the CLI is built first for AI coding agents** (Gemini CLI, Claude Code, Cursor) and second for human developers. One command — `uvx google-agents-cli setup` — injects bundled "skills" directly into the coding agent's context so it can drive the rest of the lifecycle without trawling Google Cloud documentation. The article calls this *"build agents with agents."*

A reader of the wiki's [[agent-harness]] material will recognize this as a productized harness toolkit on the Anthropic-Managed-Agents pattern — see [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]] for the parallel framing from a different vendor.

## What was actually shipped

Three integrated artifacts, all released on the same day:

1. **`google-agents-cli`** — the CLI itself, distributed as a `uvx`-runnable Python package.
2. **Agents CLI Skills** — a bundle of skill files the CLI installs into the developer's coding agent. The bundle gives the coding agent a machine-readable specification of every command, sub-command, and template the CLI exposes.
3. **Opinionated project templates** — scaffolds (`agents-cli create`) emit a directory layout aligned with Google's intended ADLC.

The product is a thin programmatic layer over the existing [[Google]] Cloud agent stack (ADK for agent code; **Agent Runtime / Cloud Run / GKE** for deployment; **Agent Platform** + ADK Eval for evaluation; **Gemini Enterprise** for distribution). What is genuinely new is the **integration surface** — one CLI exposing all of those services to one consumer (a coding agent) via one consistent command grammar.

## The fragmented stack the CLI is collapsing

The article opens by naming the problem visually (page 2 of the PDF; image reproduced below): nine boxes — Security / Data / Agent Code / CI/CD / Integration / Deployment / Evaluation / Publish / Observability — with disparate components in each, and a coding agent expected to know how they fit together.

![Fragmented Google Cloud agent stack — nine domains the Agents CLI integrates](../../raw/images/fragmented_gcp_1.original.png)

| Domain | Components named | Wiki vocabulary |
| ------ | --------------- | --------------- |
| Security | Model Armor | RAI / pre-tool guardrails |
| Data | Vector DBs, Data Pipelines | retrieval substrate |
| Agent Code | **ADK** | Layer 2 harness framework (per [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]]) |
| CI/CD | GitHub, Cloud Build | standard build/release |
| Integration | A2A, MCP, A2UI | inter-agent and tool protocols |
| Deployment | **Agent Runtime, Cloud Run, GKE** | three substrate options |
| Evaluation | Agent Platform, **ADK Eval** | offline trajectory scoring |
| Publish | **Gemini Enterprise**, Slack, WhatsApp | distribution surfaces |
| Observability | Cloud Trace, Cloud Logging, Cloud Monitoring | telemetry |

The article frames the integration cost in coding-agent-economic terms: *"wasting time and tokens ingesting massive amounts of documentation just to bridge the local-to-cloud gap."* The Skills bundle is positioned as a context-window optimization — give the coding agent the *exact sensory input and API references it needs*, not a search-and-discover problem.

## The seven specialized skills

The Skills bundle (page 2 of the PDF; image reproduced below) is the Agent-Mode entry point: prompt your coding agent in natural language and it routes the request through whichever skill applies.

![The Agents CLI's seven specialized skills](../../raw/images/agents_cli_skills.original.png)

| Skill | Purpose | Maps to harness layer |
| ----- | ------- | --------------------- |
| **Workflow** | Development lifecycle, code-preservation rules, model selection | meta — orchestrates the others |
| **ADK Code** | Python API reference for ADK (agents, tools, orchestration, callbacks, state) | Layer 2 framework primitives |
| **Scaffold** | Project scaffolding via opinionated templates | directory layout + boilerplate |
| **Evaluation** | Methodology — metrics, evalsets, LLM-as-judge, trajectory scoring | Contracts + Compounding (per Chatterjee taxonomy) |
| **Deployment** | Deployment to Agent Engine / Cloud Run / GKE; CI/CD; secrets | Layer 3 substrate operations |
| **Publish** | Registration with Gemini Enterprise for centralized distribution | distribution surface |
| **Observability** | Cloud Trace, Cloud Logging, third-party observability integrations | telemetry plumbing |

The Skills are distributed as agent-readable specifications (the article does not specify the file format, but the term-of-art "skills" in AI-coding-agent vocabulary indicates structured prompt-and-tool-spec bundles).

## Two modes: Agent Mode + Human Mode

Two-mode design is one of the article's named architectural commitments:

- **Agent Mode** — the CLI is *optimized for agent consumption*. The coding agent reads the bundled skills, decides which sub-command to call, fills in arguments, and runs the CLI as a subprocess. The article's worked example: a developer prompts their coding agent — *"I want to create a travel expense agent that can help me auto-approve expenses under $50 and require HITL to approve anything over $50, or any expense that might look out of the norm."* — and the agent scaffolds, deploys, and registers the agent without further intervention.
- **Human Mode** — the same commands run directly in a terminal for *immediate, deterministic execution*. The article frames this as developers needing to "step in whenever you want to guide the hands and eyes of the AI."

Concrete commands shown in the article:

```bash
# install
uvx google-agents-cli setup

# scaffold
agents-cli create finance-agent -y --deployment-target agent_runtime
cd finance-agent

# evaluate
agents-cli eval run
agents-cli eval compare evals/run_v1.json evals/run_v2.json

# deploy + publish
agents-cli infra single-project
agents-cli deploy
agents-cli publish gemini-enterprise
```

The mode dichotomy mirrors a recurring wiki theme — agents as *augmentation* surface (the human-driven CLI) vs *automation* surface (the coding-agent-driven CLI). See [[automation-vs-augmentation]] for the cross-cutting frame and [[2026-05-07-anthropic-economic-index-5-learning-curves|the AEI 5th report]] for the empirical Claude.ai-vs-API split.

## The Agent Development Lifecycle (ADLC)

The article's most distinctive contribution is the explicit naming of an **Agent Development Lifecycle** — a 9-stage wheel (page 4 of the PDF; image reproduced below) that the CLI is positioned as the operational backbone for.

![Agent Development Lifecycle (ADLC) with Agents CLI](../../raw/images/agents_cli_lifecycle.original.png)

The nine numbered stages, traced clockwise from the top:

1. *(implicit start: idea / requirement)*
2. **Capability & Tool Exploration** — what does the agent need to do; what tools exist
3. **Design Cognitive Architecture** — agent topology, model selection, orchestration shape
4. **Implement Tools** — actual tool/function code
5. **Context Engineering** — system prompt assembly, retrieval, state shape
6. **Evaluate** — evalsets, trajectory scoring, contract checks
7. **User Acceptance Testing** — human-in-the-loop validation
8. **Deploy Infrastructure** — provision Agent Runtime / Cloud Run / GKE
9. **CI/CD & Production** — release pipeline, secrets, observability

with an inner arrow labelled **"Iterate on approach"** pointing back from late stages into Design Cognitive Architecture — the wheel is not linear.

This is the wiki's first ingest of an explicit, vendor-named lifecycle for agent development. Compared to existing wiki vocabulary, ADLC is a *process* construct (parallel to SDLC) where [[agent-harness]] is a *runtime* construct. They overlap heavily: the ADLC's Stages 4–7 (Implement Tools → Evaluate) are mostly harness-construction work, and the wheel's Stages 5–6 (Context Engineering, Evaluate) map directly to Chatterjee's Context and Contracts layers.

The wiki creates [[agent-development-lifecycle]] as a stub concept page on the basis of this single source.

## Cross-source positioning

This article is **the Google-side companion** to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's Managed Agents post]]: same week of late April 2026, both vendors productizing the harness/runtime layer, both framing the work as integration-and-decoupling rather than model-improvement. Specific contrasts the wiki should track:

- **Vantage.** Anthropic's post is an engineering retrospective ("we tried X, hit pathologies, switched to Y") with concrete TTFT numbers. Google's is a product announcement with command examples and a lifecycle diagram. Different rhetorical register; overlapping technical territory.
- **Decoupling axis.** Anthropic decouples *brain / hands / session* — interfaces designed to outlast specific harness implementations. Google decouples *Agent Mode / Human Mode* and *coding-agent-as-driver / human-as-driver* — interfaces designed to be consumed by AI coding agents. Both are "build infrastructure that survives the substrate moving"; the substrates they expect to move are different.
- **Distribution surface.** Anthropic exposes Managed Agents on the Claude Platform; Google exposes Agents CLI plus Gemini Enterprise as the publish target. **Three vendors** now in the wiki productizing the harness layer — Microsoft Agent Framework v1.0 named in [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane]] is the third.

The interpretive framing — "is harness productization a market-defining moment?" — belongs in [[agent-harness]] and any future synthesis page, not here. (Cross-source neutrality rule.)

Other cross-references:

- **[[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]]** — already names Google ADK in the Layer 2 harness-frameworks list. This source is the Google primary that anchors that mention.
- **[[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]** — the 4-layer Context/Constraints/Contracts/Compounding taxonomy maps cleanly onto the Agents CLI's seven skills: ADK Code (framework primitives), Scaffold (Context substrate), Evaluation (Contracts), Observability (Compounding telemetry).
- **[[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]]** — also Google-published (Google Research) within ten days of this. Different team, different surface, but the wiki's two recent Google primaries together start to sketch what Google's agent-platform thesis is: agent runtime + assessment infrastructure as productizable layers around the Gemini family.
- **[[micro-productivity-trap]]** — the Skills-into-coding-agent-context pattern is precisely the "give the agent the platform's structured affordances rather than expecting it to discover them via documentation search" move. The article's pitch ("from idea to production in hours, not weeks") is a direct claim against the trap, though without empirical anchor.

## Source-quality flag

- **Type:** Vendor product announcement on a developer-relations blog. Promotional surface (*"AI agents are transitioning from experimental scripts to production services"*; *"The Agentic Internet is here. Let your agents build it."*).
- **Empirical content:** none. No latency numbers, no time-to-production data, no comparative benchmark vs. doing the work without the CLI. The claim "*idea to production in hours, not weeks*" is unsubstantiated in the article body.
- **Architectural content:** substantive — the CLI command grammar, the seven Skills enumeration, the ADLC wheel, and the fragmented-stack diagram are concrete enough to triangulate against [[agent-harness]] and the Anthropic Managed Agents post.
- **Confidence boost:** +0.05 per the [§Lifecycle](../../CLAUDE.md#lifecycle) "additional supporting source" rule for [[agent-harness]] and [[ai-agents]]; **no peer-review or large-N bonus**; treat as *vendor-promotional* (cap at 0.75 unless independently corroborated). The architectural claims are corroborated by [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's parallel post]] and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] / [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] taxonomies, so the cross-source convergence is solid.
- **Vendor-of-deployment flag:** Google publishes this as platform-builder *and* as customer-acquisition. Read with that vantage in mind.

## Linked entities and concepts

**Entities (this wiki):** [[Google]] (publisher; new entity created on this ingest); [[Google Research]] (sibling org; not directly involved in this article but adjacent). **Dangling** (single-source mention, deferred): Ivan Cheung, Pier Paolo Ippolito, Elia Secchi (article authors); **Google Cloud Agent Platform / Agents CLI / google-agents-cli / Agent Runtime / Gemini Enterprise / Cloud Run / GKE / Cloud Build / Cloud Trace / Cloud Logging / Cloud Monitoring / ADK / ADK Eval / Model Armor / A2A / A2UI / MCP** (Google products and protocols; promote on second-source coverage).

**Concepts:** [[agent-harness]] (heavy enrichment — productized vendor toolkit instantiating the runtime layer; bumps `source_count` 4→5), [[ai-agents]] (light — adds vendor-side architecture to the chatbot → agent → multi-agent progression), [[agent-development-lifecycle]] (created — single source so far). Adjacent: [[automation-vs-augmentation]] (Agent Mode vs Human Mode operationalizes the dichotomy at CLI level), [[micro-productivity-trap]] (Skills-as-context-injection is structural escape from "just call the model").

**Threads/syntheses:** none directly affected.

## Source

- **Raw PDF (~5 pages of body content):** [article file](../../raw/articles/Agents%20CLI%20in%20Agent%20Platform_%20create%20to%20production%20in%20one%20CLI%20-%20Google%20Developers%20Blog.pdf)
- **Images extracted from the article (raw):**
  - [`fragmented_gcp_1.original.png`](../../raw/images/fragmented_gcp_1.original.png) — the nine-domain fragmented stack diagram
  - [`agents_cli_skills.original.png`](../../raw/images/agents_cli_skills.original.png) — the seven specialized skills grid
  - [`agents_cli_lifecycle.original.png`](../../raw/images/agents_cli_lifecycle.original.png) — the ADLC 9-stage lifecycle wheel
- **Publisher:** Google (Google Developers Blog)
- **Date:** April 22, 2026
- **Authors:** Ivan Cheung (Software Engineer), Pier Paolo Ippolito (GenAI Field Solutions Architect), Elia Secchi (Solutions Specialist)
- **Categories tagged on the post:** AI · Cloud · Announcements · Problem-Solving (Solve)
