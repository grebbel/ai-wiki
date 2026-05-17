---
type: source
kind: article
title: "Building effective agents"
author: ["Erik Schluntz", "Barry Zhang"]
publisher: "[[Anthropic]]"
section: "Engineering at Anthropic"
url: "https://www.anthropic.com/research/building-effective-agents"
date_published: 2024-12-19
date_ingested: 2026-05-17
length: "~10-page web essay; read in full"
raw: "../../raw/articles/05_Anthropic_Building-Effective-Agents.pdf"
tags: [agent-harness, anthropic-engineering, building-effective-agents, workflows-vs-agents, augmented-llm, prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, ACI, simplicity, transparency, foundational, mcp]
relationships:
  - type: supports
    target: 2025-11-26-anthropic-effective-harnesses-long-running-agents
    via: "Anthropic's *Effective Harnesses for Long-Running Agents* (Nov 2025) is the direct continuation of this Dec 2024 post — both authored by Anthropic Engineering, both published as Engineering at Anthropic blog posts, applying the same simplicity/transparency/ACI principles to longer-horizon tasks"
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Anthropic's three core principles — simplicity, transparency, careful Agent-Computer Interface (ACI) design — anticipate by 17 months the discipline Osmani names *harness engineering*. The ACI tools-as-API principle is the canonical pre-formalisation of the Constraints + Contracts layers"
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "the *augmented LLM* building block diagram (LLM + Retrieval + Tools + Memory) is the structural ancestor of Chatterjee's 4-layer harness anatomy. Each pattern (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) decomposes the Constraints + Contracts work that Chatterjee names rhetorically"
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Anthropic's workflows-vs-agents architectural distinction is the canonical version of Pan's harness-vs-runtime distinction — Pan's NLAH formalises the patterns Anthropic enumerated practitioner-style 16 months earlier"
  - type: uses
    target: agent-harness
---

# Schluntz & Zhang — *Building effective agents*

A **~10-page Engineering at Anthropic blog post**, published **19 December 2024**. **The wiki's earliest primary-source on the harness-engineering construct by ~14 months** — predates [[2025-11-26-anthropic-effective-harnesses-long-running-agents|Anthropic's own follow-up *Effective Harnesses for Long-Running Agents*]] (Nov 2025), [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex]] (Feb 2026), and the academic primary sources Pan/Lee/Lou/Karten by 14-17 months. Authored by **Erik Schluntz** (Anthropic Engineering) and **Barry Zhang**.

Listed by [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video]] as a foundational reference. Also cited by [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al. reference list]] (Anthropic 2024, *Building effective agents*), [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]], and by [[2026-05-15-osmani-agent-harness-engineering|Osmani]]'s broader citation network. **This is now the primary-source ingest** — closing the wiki's longest-standing harness-cluster ingest target.

## TL;DR

- **The thesis** (the opening claim that everything else flows from). *"Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."* The wiki's strongest vendor-side anchor for *frameworks-vs-direct-API* skepticism — predating Osmani's HaaS observation by 17 months.
- **The architectural distinction** (the wiki's canonical workflows-vs-agents framing):
  - **Workflows** — *"systems where LLMs and tools are orchestrated through predefined code paths."*
  - **Agents** — *"systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."*
  - Both are "agentic systems"; the architectural split is **who decides the next step** (the code or the model).
- **When (and when not) to use agents.** *"Find the simplest solution possible, and only increase complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."* The wiki's earliest vendor-side anchor for the **"agents are not always the right answer"** counter-thesis the practitioner literature later sharpens.
- **When and how to use frameworks.** Anthropic names: **Claude Agent SDK, Strands Agents SDK by AWS, Rivet, Vellum**. *"Frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug."* Strong recommendation: *"start by using LLM APIs directly: many patterns can be implemented in a few lines of code."* **This is the direct ancestor of [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] HaaS substrate-shift framing — Anthropic was already arguing in Dec 2024 for the same simplicity-over-framework principle that became practitioner consensus 17 months later.**
- **The augmented LLM building block.** *"The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities — generating their own search queries, selecting appropriate tools, and determining what information to retain."* Recommends **Model Context Protocol (MCP)** as one approach to implementing these augmentations — *the canonical first mention of MCP in the context of agent-harness construction*.
- **Five workflow patterns**, with named when-to-use heuristics:
  1. **Prompt chaining** — decompose a task into a sequence of steps where each LLM call processes the output of the previous. Add programmatic gates between steps. *"Ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. Trades latency for higher accuracy."* Examples: marketing copy + translation; outline-then-document.
  2. **Routing** — classifies an input and directs it to a specialized followup task. *"Works well for complex tasks where there are distinct categories that are better handled separately."* Examples: customer service queries (general / refund / technical) routed differently; easy questions to Haiku, hard ones to Sonnet.
  3. **Parallelization** — two variations:
     - **Sectioning** — break a task into independent subtasks run in parallel.
     - **Voting** — run the same task multiple times for diverse outputs.
     *"Effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed."* Examples: guardrail-as-sectioning (one model screens for inappropriate content while another responds); vulnerability voting in code review.
  4. **Orchestrator-workers** — a central LLM dynamically breaks down tasks, delegates to worker LLMs, synthesizes results. *"Well-suited for complex tasks where you can't predict the subtasks needed."* Examples: multi-file coding products; multi-source search.
  5. **Evaluator-optimizer** — one LLM generates a response; another provides evaluation and feedback in a loop. *"Effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."* Examples: literary translation with nuance; multi-round search.
- **The autonomous agent.** *"Agents are emerging in production as LLMs mature in key capabilities — understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors."* Operating loop: human command → plan independently → return for human input or judgement at checkpoints / blockers. Stopping conditions named (max iterations, completion). **Anthropic's named examples**: a coding agent solving SWE-bench tasks; computer-use reference implementation. *"While the topographically similar [to parallelization], the key difference from parallelization is its flexibility — subtasks aren't pre-defined, but determined by the orchestrator based on the specific input."*
- **The three core principles** (the closing summary — the wiki's strongest single-paragraph anchor):
  1. ***Maintain simplicity in your agent's design.***
  2. ***Prioritize transparency by explicitly showing the agent's planning steps.***
  3. ***Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.***
- **The Agent-Computer Interface (ACI) framing** (Appendix 2). *"As much effort should go into creating good agent-computer interfaces (ACI) as into human-computer interfaces (HCI)."* The pre-formalisation of what [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al.]] later automate by code-search and what [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al.]] later represent as natural-language NLAH. Concrete advice: *"Put yourself in the model's shoes"; "Test how the model uses your tools"; "Poka-yoke your tools — change arguments so it's harder to make mistakes."* Quoted example: *"While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt. We found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths — and we found that the model used this method flawlessly."*
- **Appendix 1: Agents in practice.** Two named domains where Anthropic's customers have found agentic value: **(A) Customer support** (conversation + action + clear success metric + usage-based pricing for successful resolution); **(B) Coding agents** (SWE-bench Verified specifically named as the benchmark).

## What was actually ingested

Full ~10-page web article (5 workflow patterns + agents + appendices 1 + 2 on agents-in-practice and prompt-engineering-your-tools). All diagrams. Acknowledgements name Erik S. and Barry Zhang as authors.

## Cross-positioning with the wiki

### The foundational practitioner-vendor anchor

This post **predates every other harness-construct source in the wiki**, with a 14-17 month head-start. Its claims have proven durable: the 5 workflow patterns + the autonomous-agent extreme + the simplicity / transparency / ACI principles are still load-bearing in 2026's harness-engineering discourse. **The Anthropic engineering team articulated the construct in essentially-mature form in December 2024**; the subsequent 17 months of practitioner essays (Bockeler, Chatterjee, Kokane, Osmani) and academic papers (Pan, Lee, Lou, Karten) have *substantiated, formalised, and extended* this framing rather than overturned it.

This carries a sharp implication for the wiki's [[concepts/agent-harness]] page: **the term "harness engineering" is newer than the concept**. The construct's intellectual foundations are December 2024; the *naming* of the discipline is February 2026 ([[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex]] is the post that coined *harness engineering* per Bockeler's attribution). The 14 intervening months were spent rediscovering, formalising, and operationalising what Anthropic Engineering had already published.

### The MCP first-mention thread

This is the wiki's primary-source citation for **Model Context Protocol (MCP)** being introduced as part of the agentic systems architecture. The MCP-as-tool-substrate framing pervades the wiki's harness cluster — this is the post that named it as a deliberate engineering choice.

### Workflows-vs-agents as durable vocabulary

The architectural distinction has proven durable. [[2026-05-09-chase-agent-development-lifecycle|Chase / LangChain]]'s ADLC and [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] both inherit this split. The wiki should consider promoting *"workflows-vs-agents"* as a vocabulary candidate at next concept-page revision.

## Named entities (this ingest)

- [[Erik Schluntz]] — Anthropic Engineering. **First mention. Dangling.**
- [[Barry Zhang]] — Anthropic Engineering. **First mention. Dangling.**

Plus named tools/frameworks (existing or first mention):
- [[Claude Agent SDK]] — already in wiki ecosystem.
- [[Strands Agents SDK]] (AWS) — **first mention**.
- [[Rivet]] (drag-and-drop GUI LLM workflow builder) — **first mention**.
- [[Vellum]] (GUI tool for testing complex workflows) — **first mention**.
- [[Model Context Protocol]] — already in wiki ecosystem.

## Source-quality notes

- **Genre**: vendor engineering blog post (Anthropic). **Highly influential** — cited by all four academic papers in this batch (Pan, Lee, Lou, Karten) and by every major practitioner essay (Chatterjee, Kokane, Osmani, Bockeler).
- **Empirical content**: zero quantitative data; the post is **practitioner-experience-based observation distilled across "dozens of teams"**. No measurements; no ablation. Its credibility rests on the operating-leverage of Anthropic Engineering's vantage on agent deployments.
- **Reproducibility**: explicit cookbook reference for sample implementations.
- **Confidence: 0.78.** Per Lifecycle: single source +0.05 for vendor-engineering primary-source +0.05 for being the canonical-cited foundational reference across the literature = 0.80; capped at 0.78 because the source itself reports no empirical anchor.

## Open questions

- **The retrospective: how durable were the 5 patterns?** 17 months on, the patterns are still the canonical vocabulary. But the *evaluator-optimizer* pattern has been extended substantially (Karten's Refiner, Lee's Meta-Harness proposer). The wiki should track whether the 5-pattern list still holds when re-evaluated against 2026's discourse.
- **The framework-skepticism prediction.** Anthropic recommended in Dec 2024 *"start with LLM APIs directly"*. By May 2026, Anthropic itself ships the Claude Agent SDK + Claude Managed Agents — a productised HaaS layer. Whether this is a contradiction or a graduated path (build-from-scratch first, adopt-HaaS once mature) is worth asking the wiki to track.
- **Authorship continuity.** Schluntz and Zhang authored this post in Dec 2024. [[2025-11-26-anthropic-effective-harnesses-long-running-agents|*Effective Harnesses for Long-Running Agents*]] (Nov 2025) is authored by Justin Young. **Different authors, similar voice** — worth tracking how Anthropic's harness-engineering thought leadership has rotated through the engineering team.
