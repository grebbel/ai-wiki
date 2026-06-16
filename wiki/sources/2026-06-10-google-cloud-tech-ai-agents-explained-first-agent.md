---
type: source
kind: video
title: "AI agents explained: Build your first agent in 8 minutes"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech (YouTube)"
url: "https://www.youtube.com/watch?v=Zqno_vux6d8"
date_published: 2026-06-10
date_ingested: 2026-06-12
length: "~8:29 minutes (transcript ~183 segments; manual English CC track, kind: manual, light cleanup applied)"
raw: "../../raw/videos/ai-agents-explained-build-your-first-agent-in-8-minutes.md"
tags: [react, ai-agents, agentic-loop, google-adk, agent-development-kit, sequential-agents, reactive-agents, planning-agents, loop-agent, multi-agent, validation-checker, python-tutorial, google-cloud, developer-education]
relationships:
  - type: published-by
    target: Google
    via: "Google Cloud Tech YouTube channel"
  - type: uses
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "tutorial defines a modern agent via the ReAct reason–act–observe loop and cites the paper by name as the clearest explanation"
  - type: uses
    target: 2026-04-22-cheung-ippolito-secchi-google-agents-cli
    via: "builds the worked blog-writer agent with Google ADK (LLM agents, loop/workflow agents, root agent + tools) — the same framework the Agents CLI source documents"
---

# AI agents explained: Build your first agent in 8 minutes

> Follow the codelab → https://goo.gle/3Q5TSt3
> GitHub repo → https://goo.gle/4fsahT8
> Google Agent Development Kit (ADK) → https://goo.gle/3Q3enqf
>
> At the simplest level, an AI agent doesn't just answer—it decides and takes action. In this video, Smitha goes beyond basic chatbots and demonstrates how to build a fully autonomous, self-correcting multi-agent system from scratch using Google's Google Agent Development Kit (ADK). First, Smitha breaks down the theory behind modern agents: the ReAct Framework (reasoning and acting) and the 3 main agent patterns (sequential, reactive, and planning). Then, she jumps straight into Python to build a practical *Blog Writing Agent*. Watch along and learn how to combine *Planner* and *Writer* agents with validation checkers and loop agents to create an AI that catches its own mistakes and automatically retries until it gets it right.
>
> *— [Google Cloud Tech YouTube channel description](https://www.youtube.com/watch?v=Zqno_vux6d8)*

An **~8½-minute developer tutorial** from the **Google Cloud Tech** channel (presenter named in the video as **Smitha**, 10 June 2026). It is the wiki's first source that pairs the **[[react-reasoning-acting|ReAct]] theory** with a **hands-on [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google ADK]] build** — making it the practical, operational bookend to the [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|2022 ReAct paper]] ingested in the same batch. Where the paper proves the reason-act loop, this video shows a 2026 framework wiring it up in Python.

## TL;DR

- **Defines an agent as ReAct in practice.** "An agent is software that doesn't just answer, it can decide and take action." The clearest explanation, per the video, "comes from the research paper ReAct: Synergizing Reasoning and Acting in Language Models" — the cycle of **reason → act (call a tool/API) → observe → adjust** is "the foundation of how modern AI agents work." This is a direct line from the [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|primary paper]] to a 2026 vendor tutorial.
- **Three agent patterns** (a teaching taxonomy): **sequential** (assembly-line, step 1→2→3 — predictable but rigid); **reactive** (decide in the moment from current state — flexible, doesn't plan ahead); **deliberate/planning** (pause, sketch a plan, then execute — for multi-step goals with dependencies, e.g. booking travel). Choice depends on the problem: simple/predictable → sequential, dynamic → reactive, multi-step with dependencies → planning.
- **Worked build: a self-correcting blog-writer (multi-agent in ADK).** Topic in → structured outline → full post → alternative titles & hooks. Architecture:
  - **Planner agent** (LLM agent) — produces a markdown outline (title, intro, 4–6 sections, conclusion); writes to shared state under `output_key: blog_outline`.
  - **Outline validation checker** (LLM agent) — reads state; answers `OK` if the outline is complete, else `retry` with the reason.
  - **`robust_blog_planner`** — a **loop agent** (a *workflow* agent in ADK) wrapping planner + checker; re-runs the planner up to **3 times** until the checker passes. A built-in safety net.
  - **Writer agent** — turns the saved outline into a full markdown post (audience: software engineers; explain how *and* why; short code snippets); saves to `blog_post`.
  - **Blog-post validation checker** + **`robust_blog_writer`** loop — same retry pattern for the draft.
  - **Root agent (`blogger`)** — exposes the two robust loops *as tools*; on a topic it calls planner → writer, then adds 3 alternative titles + 2 tweet-length hooks. "The root agent only has access to the two tools we exposed, so its workflow is clear and controlled."
- **The auto-correction pattern is the lesson.** Validation checkers + loop agents give the system a structural retry/self-repair mechanism — the tutorial-scale echo of the wiki's [[agent-harness|harness]] argument that *constraints and contracts around the model* (not the model alone) deliver reliable agents. ADK's `LlmAgent` / `LoopAgent` / `BaseAgent` (subclass for custom agents) are the framework primitives.
- **Run surface**: `adk web` launches a local UI to interact with the agent; demoed with "generate a blog on the top 10 use cases for AI agents."

## What was actually ingested

The full manual English closed-caption track (~183 transcript segments, runtime 8:29). The fetcher also returned a duplicate auto-generated (ASR) pass which was discarded in favour of the human-curated CC. Light caption cleanup applied (ADK product names, "robust blog," "writes will be stored"). Chapter headings from YouTube macro-markers are interleaved in the raw transcript.

## Linked entities and concepts

- Concepts: [[react-reasoning-acting]], [[ai-agents]], [[agent-harness]], [[agent-development-lifecycle]].
- Entity / framework: [[Google]] (ADK; Google Cloud Tech channel). Presenter "Smitha" named in body only (single-mention, no entity — per author-promotion rule).

## Relationships

- *uses* [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting]] — the tutorial's conceptual foundation is this paper's reason-act loop, cited by name.
- *uses* [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] — builds on Google ADK, the harness framework that source documents (the CLI's ADK Code skill is the Python-API surface used here).
- *published-by* [[Google]].
