---
type: source
kind: article
title: "The Anatomy of an Agent Harness"
author: ["Vivek Trivedy"]
publisher: "[[LangChain]]"
section: "LangChain Engineering blog"
url: "https://www.langchain.com/blog/the-anatomy-of-an-agent-harness"
date_published: 2026-03-10
date_ingested: 2026-05-17
length: "12-minute web essay; full body captured via WebFetch (no PDF available); ~3,000 words"
raw: "../../raw/articles/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md"
tags: [agent-harness, harness-engineering, langchain, vivek-trivedy, agent-equals-model-plus-harness, terminal-bench-2, ralph-loop, agents-md, context7, context-rot, opus-cross-harness-variance, working-backwards-from-behavior, deepagents]
relationships:
  - type: supersedes
    target: 2026-02-17-langchain-improving-deep-agents-harness-engineering
    via: "the Feb 17 LangChain post was ingested metadata-only because the PDF capture was empty. This March 10 post is by the same author (Vivek Trivedy) at the same channel (LangChain Engineering blog) and represents the substantive expansion of the harness-engineering framework that the Feb post introduced. Trivedy's footnote 'In a previous blog, we showed how we improved our coding agent Top 30 to Top 5 on Terminal Bench 2.0 by only changing the harness' refers back to the Feb 17 post."
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Osmani's O'Reilly Radar essay is a near-direct synthesis-with-expansion of THIS post. Multiple verbatim quotes match ('If you're not the model, you're the harness'); the working-backward-from-behavior pattern; the same six harness primitives in the same order; the same three open problems list. Osmani's piece is Trivedy's framework propagated to an O'Reilly Radar audience with attribution but minor compression."
  - type: supports
    target: 2024-12-19-anthropic-building-effective-agents
    via: "Trivedy operates within Anthropic's Dec 2024 workflows-vs-agents architecture, applying the same simplicity / transparency / careful-ACI principles at the framework-vendor (LangChain) altitude that Anthropic articulated at the model-vendor altitude"
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Pan et al. reference 16: 'LangChain. 2026a. The anatomy of an agent harness. Engineering blog. Published: 2026-03-10.' This is the canonical academic-paper citation of this post."
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "Chatterjee's Medium post (May 3, 2026) carries a similar title but is a different artifact by a different author with different content (Friday-in-March story, 4C anatomy). The titles share words but the posts are distinct — confirmed by user note 2026-05-17. The wiki holds both as legitimately co-existing under the 'Anatomy of an Agent Harness' lexical family."
  - type: uses
    target: agent-harness
---

# Trivedy — *The Anatomy of an Agent Harness*

A **12-minute Engineering at LangChain blog post**, published **10 March 2026** by **Vivek Trivedy** (LangChain). **The canonical "Anatomy of an Agent Harness" piece the wiki has been triangulating across multiple ingest batches** — the post Osmani referenced as *"Viv's anatomy"* and that Pan et al. cited as reference 16. **First-person primary source** for several claims the wiki has been carrying second-hand. Author byline confirmed via direct WebFetch (full HTML reproduction archived at `raw/articles/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md`).

**Closes the Trivedy / Chatterjee / LangChain three-post thicket** the wiki has been carrying as an open question since 2026-05-15. **Vivek Trivedy = "Viv Trivedy"** in Osmani's reference. **The Trivedy LangChain post (this) and Chatterjee's Medium piece are two distinct artifacts** (confirmed by user note 2026-05-17) with similar titles but different content. The wiki's [[2026-05-07-chatterjee-anatomy-of-agent-harness|existing Chatterjee source page]] is correctly attributed and stays in place; this post is a separate, parallel ingest.

## TL;DR

- **The equation.** ***Agent = Model + Harness***. *"If you're not the model, you're the harness."* These two lines — quoted across the wiki's harness cluster — are **Trivedy's coinages** in this post. The wiki has been carrying them second-hand via [[2026-05-15-osmani-agent-harness-engineering|Osmani]]; this is the **primary source**.
- **A harness is** *"every piece of code, configuration, and execution logic that isn't the model itself. A raw model is not an agent. But it becomes one when a harness gives it things like state, tool execution, feedback loops, and enforceable constraints."*
- **Five harness component categories.** System prompts; Tools/Skills/MCPs + their descriptions; Bundled Infrastructure (filesystem, sandbox, browser); Orchestration Logic (subagent spawning, handoffs, model routing); Hooks/Middleware for deterministic execution (compaction, continuation, lint checks).
- **The design pattern.** *"Behavior we want (or want to fix) → Harness Design to help the model achieve this."* Trivedy explicitly works backwards from desired agent behaviors to derive each harness primitive — the same pattern Osmani adopts.
- **Six harness primitives derived from "things a model cannot do out of the box":**
  1. **Filesystems for durable storage and context management** — the most foundational harness primitive. Unlocks workspace, incremental offloading, multi-agent collaboration surface. Git adds versioning.
  2. **Bash + code as a general-purpose tool** — *"giving models a computer and letting them figure out the rest autonomously"*. The model designs its own tools on the fly via code.
  3. **Sandboxes and tools to execute & verify work** — safe operating environments + good default tooling (language runtimes, CLIs, browsers) + self-verification loops via test runners, logs, screenshots.
  4. **Memory & search for continual learning** — AGENTS.md as memory file standard injected into context on start; Context7 MCP + Web Search for post-knowledge-cutoff information.
  5. **Battling Context Rot** — *"Harnesses today are largely delivery mechanisms for good context engineering"*. Three named strategies: **compaction** (window-near-full handling), **tool call offloading** (head/tail kept in context, full output to filesystem), **Skills** (progressive disclosure to prevent tool-description clutter on agent start).
  6. **Long-horizon autonomous execution** — combines all prior primitives. **Filesystems + git** for cross-session work tracking. **Ralph Loops** — *"a harness pattern that intercepts the model's exit attempt via a hook and reinjects the original prompt in a clean context window, forcing the agent to continue its work against a completion goal"*. **Planning + self-verification** via test-suite hooks + LLM self-evaluation.
- **The model-harness co-training feedback loop.** *"Today's agent products like Claude Code and Codex are post-trained with models and harnesses in the loop... Useful primitives are discovered, added to the harness, and then used when training the next generation of models. As this cycle repeats, models become more capable within the harness they were trained in."* **The overfitting side effect named**: the Codex-5.3 prompting guide's `apply_patch` tool logic is cited as a concrete example — *"a truly intelligent model should have little trouble switching between patch methods, but training with a harness in the loop creates this overfitting."*
- **The Terminal Bench 2.0 anchor** (the wiki's load-bearing claim — now first-person primary): ***"Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses. In a previous blog, we showed how we improved our coding agent Top 30 to Top 5 on Terminal Bench 2.0 by only changing the harness. There's a lot of juice to be squeezed out of optimizing the harness for your task."*** The "previous blog" reference points to LangChain's earlier [*Improving deep agents with harness engineering*](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) (Feb 17, 2026, by the same author).
- **The future direction.** *"As models get more capable, some of what lives in the harness today will get absorbed into the model. Models will get better at planning, self-verification, and long horizon coherence natively, thus requiring less context injection for example. That suggests harnesses should matter less over time. But just as prompt engineering continues to be valuable today, it's likely that harness engineering will continue to be useful for building good agents."*
- **Three named open problems** that Trivedy is actively exploring at LangChain (within the **deepagents** harness-building library):
  - **Orchestrating hundreds of agents working in parallel on a shared codebase**
  - **Agents that analyze their own traces to identify and fix harness-level failure modes**
  - **Harnesses that dynamically assemble the right tools and context just-in-time for a given task instead of being pre-configured**
- **Closing aphorism.** ***"The model contains the intelligence and the harness is the system that makes that intelligence useful."***

## What was actually ingested

Full body of the ~3,000-word post captured via WebFetch (no PDF version exists at the canonical URL; the LangChain blog renders dynamically). HTML-to-markdown reproduction archived at `raw/articles/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md`. All 6 derived harness primitives + all section headings + the Terminal Bench anchor + the three open problems + closing aphorism. Embedded references preserved (ReAct loop docs, Codex-5.3 prompting guide, Context7, Chroma Context Rot research, Terminal Bench 2.0 leaderboard).

## Cross-positioning with the wiki

### Closes the Trivedy / Chatterjee / LangChain three-post thicket

The wiki has been carrying this open question across three ingest batches (2026-05-15, 2026-05-16, 2026-05-17 morning). **Resolved cleanly with two distinct posts:**

| Post | Author | Channel | Date | Status |
|---|---|---|---|---|
| **The Anatomy of an Agent Harness** | **Vivek Trivedy** | LangChain Engineering blog | **10 March 2026** | **THIS source page** — primary; canonical "Anatomy" reference |
| *The Anatomy of an Agent Harness* | Abhishek Chatterjee | Medium | ~3 May 2026 | [[2026-05-07-chatterjee-anatomy-of-agent-harness|Existing source page]] — separate piece; correctly attributed; *similar title only* (per user note 2026-05-17) |

The wiki's prior author-attribution flag on "Trivedy vs Chatterjee" is now **closed** — they're separate authors of separate posts. The titles overlapping is a coincidence of the harness-anatomy framing being a natural Q1-Q2 2026 vocabulary move.

### Re-anchors load-bearing claims to a first-person primary

Multiple wiki claims now have a **first-person primary anchor**:

| Wiki claim (status before this ingest) | Status after |
|---|---|
| ***"Agent = Model + Harness"*** equation (carried via Osmani / Chatterjee) | **Closed — first-person primary anchored.** Trivedy's coinage in this post. |
| ***"If you're not the model, you're the harness"*** (carried via Osmani) | **Closed — first-person primary anchored.** Trivedy's coinage in this post. |
| ***"Top 30 → Top 5 on Terminal Bench 2.0 by only changing the harness"*** (carried via PY video / Osmani; re-attributed away from Pan et al. earlier today) | **Closed — first-person primary anchored as Trivedy's own LangChain result.** Attributed by Trivedy to "a previous blog" (likely LangChain *Improving Deep Agents with Harness Engineering*, Feb 17, 2026). |
| ***"Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses"*** (carried via Osmani) | **Closed — first-person primary anchored.** Trivedy's direct observation. |
| **Ralph Loops** as a named harness primitive (referenced across multiple wiki sources) | **First-person definition anchored**: *"intercepts the model's exit attempt via a hook and reinjects the original prompt in a clean context window."* |
| **The "working-backward-from-behavior" design pattern** (carried via Osmani as Trivedy-attributed) | **Closed — first-person primary anchored.** Trivedy's coinage in this post, explicitly used as the structural argument for each primitive. |
| **The three named open problems** (parallel-agents / trace-analysing-self-correction / dynamic-just-in-time-assembly) | **Closed — first-person primary anchored.** Trivedy's enumeration in the closing section. Osmani's identical list is a faithful reproduction. |

### Repositions Osmani's essay as derivative-of-Trivedy

[[2026-05-15-osmani-agent-harness-engineering|Osmani's O'Reilly Radar essay]] (May 15, 2026) is now confirmable as **a near-direct synthesis-with-expansion of this Trivedy post**, published 9 weeks later for the O'Reilly Radar audience. Verbatim and near-verbatim correspondences:

| Trivedy (March 10) | Osmani (May 15) |
|---|---|
| *"If you're not the model, you're the harness."* | *"If you're not the model, you're the harness."* (direct quote with attribution to Viv) |
| *"Behavior we want (or want to fix) → Harness Design to help the model achieve this"* (the design pattern) | Same diagram with attribution to Viv |
| 6 harness primitives in the order: filesystem / bash+code / sandboxes / memory+search / context rot / long-horizon | Same 6 primitives in the same order |
| Three open problems (parallel-agents / trace-self-correction / dynamic-assembly) | Identical three open problems |
| *"Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses"* | Same observation with attribution to Viv |
| Top 30 → Top 5 LangChain result | Same result attributed to "Viv's team" |

Osmani's contribution beyond Trivedy: **(a)** explicit cross-author synthesis citing Anthropic / HumanLayer (Dex Horthy) / Bockeler / Fareed Khan / Simon Willison alongside Trivedy; **(b)** the *ratchet* discipline framing ("every line in AGENTS.md should be traceable back to a failure"); **(c)** the HaaS substrate-shift framing. Trivedy is the **direct source of the technical content**; Osmani is the **cross-author synthesis that landed it at a broader audience.**

This re-positioning has implications for [[concepts/agent-harness]]: claims previously attributed to "the practitioner cluster" can be more sharply attributed to Trivedy-as-source + Osmani-as-popularisation. Worth a body-note update.

### Confirms Trivedy as the originator of the term *harness engineering*

Trivedy uses *"harness engineering"* as a noun phrase throughout this post and his earlier Feb 17 LangChain post. Within the wiki's Q1 2026 vocabulary-coinage window:

| Post | Date | Author | Uses *"harness engineering"* as a discipline noun? |
|---|---|---|---|
| [[2026-02-11-lopopolo-codex-harness-engineering\|OpenAI Codex / Lopopolo]] | Feb 11, 2026 | Lopopolo | ✓ (title) |
| LangChain *Improving Deep Agents with Harness Engineering* | Feb 17, 2026 | (Trivedy, inferred) | ✓ (title) |
| **THIS post (Trivedy / LangChain)** | **Mar 10, 2026** | **Trivedy** | ✓ (throughout) |

Lopopolo and Trivedy / LangChain coined the term within ~6 days of each other in February 2026. Bockeler at QCon (May 2026) [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|credits Lopopolo / OpenAI Codex with the name]]. The wiki should hold Lopopolo + Trivedy as **near-simultaneous co-coiners** of the term as a discipline noun, with **Trivedy's coinage of *Agent = Model + Harness* / *If you're not the model, you're the harness*** as the load-bearing vocabulary primitives Osmani propagated.

## Named entities (this ingest)

- [[Vivek Trivedy]] — LangChain Engineering. **First wiki source by Trivedy directly; primary mention.** Multiple wiki sources have referenced "Viv Trivedy" or "Viv" second-hand (Osmani; Chatterjee Friday-in-March piece is a *different* author entirely). **Dangling pending second source.**
- [[LangChain]] / [[deepagents]] — already in wiki ecosystem. The deepagents library named explicitly as LangChain's harness-building artifact.

## Source-quality notes

- **Genre**: practitioner / framework-vendor essay (LangChain Engineering blog). **Highly cited** — Pan et al. reference 16; Osmani's reference. Trivedy's framework is now the wiki's most-frequently-cited single artifact in the harness-engineering practitioner literature.
- **Empirical content**: one named empirical anchor (Top 30 → Top 5 on Terminal Bench 2.0; cross-harness variance for Opus 4.6). Anchor is **first-person** but the underlying experiment lives in an earlier LangChain blog post — Trivedy doesn't reproduce the methodology here. **The empirical claim should ultimately trace to the Feb 17 LangChain post** (currently metadata-only ingest in the wiki); this post is the framework essay.
- **Confidence: 0.82.** Per Lifecycle: single source +0.05 for framework-vendor primary-source +0.05 for first-person primary-anchoring of multiple wiki claims (Agent = Model + Harness; If-you're-not-the-model-you're-the-harness; Ralph Loops definition; working-backward-from-behavior) +0.05 for being the most-cited practitioner essay in the harness literature = 0.85; capped at 0.82 because the empirical anchor (Top 30 → Top 5) is back-referenced rather than methodologically described here.

## Open questions

- **Ingest the Feb 17 LangChain post for substantive content.** The wiki's current [[2026-02-17-langchain-improving-deep-agents-harness-engineering|Feb 17 source page]] is metadata-only because the PDF capture was empty. With Trivedy now identified as the likely author, a WebFetch on `https://blog.langchain.com/improving-deep-agents-with-harness-engineering/` (or the canonical URL at langchain.com/blog) would close the empirical-anchor methodology for the Top 30 → Top 5 claim.
- **The "agents that analyze their own traces" open problem** is exactly what [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.'s]] Continual Harness Refiner does. Trivedy named it as open March 10; Karten et al. operationalised it May 11. Strong convergence between practitioner-named open problems and academic-paper deliverables within 2 months. Worth tracking as a meta-observation on the cluster's velocity.
- **deepagents as a productized harness.** Trivedy names it explicitly as LangChain's *"harness building library"*. The wiki should track whether deepagents emerges as a HaaS competitor to the Claude Agent SDK / Codex SDK / OpenAI Agents SDK trio Osmani named.
