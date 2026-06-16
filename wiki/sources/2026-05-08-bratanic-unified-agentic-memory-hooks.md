---
type: source
kind: article
title: "Unified Agentic Memory Across Harnesses Using Hooks"
author: ["Tomaz Bratanic"]
publisher: "Towards Data Science (Insight Media Group)"
url: "https://towardsdatascience.com/unified-agentic-memory-across-harnesses-using-hooks/"
date_published: 2026-05-08
date_ingested: 2026-05-10
length: "~9-min read (17-page PDF, ~2,800 words + 8 diagrams + code refs)"
raw: "../../raw/articles/Unified Agentic Memory Across Harnesses Using Hooks _ Towards Data Science.pdf"
tags: [agent-harness, hooks, agentic-memory, neo4j, claude-code, codex, cursor, mcp, dream-phase, lifecycle-events, harness-portability, knowledge-graph, persistent-memory]
---

# Unified Agentic Memory Across Harnesses Using Hooks

A practitioner essay arguing that **agentic memory should live outside any single [[agent-harness|harness]]**, integrated via the **lifecycle hooks** that Claude Code, Codex, and Cursor each expose with near-identical contracts. The author (Tomaz Bratanic, Neo4j) builds a working demonstration: shared Python hook scripts (`log_event.py`, `inject_memory.py`) + Neo4j as the persistent store + a periodic "dream phase" batch job that distills events into durable Markdown memories. Result: switch from Cursor to Claude Code to Codex mid-project and pick up exactly where you left off.

This is the wiki's **first source** that names *hooks* as a first-class harness primitive — distinct from MCP tools — and articulates the architectural trade-offs. The piece also operationally demonstrates [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy-style]] markdown memory at the agentic level: "*the notes themselves imitate a markdown wiki, the same shape Karpathy and others have been gravitating toward for personal LLM memory and the same shape Anthropic's skills already use.*"

## TL;DR

- **Memory should not be locked inside a harness.** *"If you don't own your memory, you don't own your agent. Every harness today builds its own walled garden of context, preferences, and session history. Switch them and you start from zero. That doesn't have to be the case."*
- **Hooks vs. MCP**: hooks are **system-initiated** (deterministic, fire on lifecycle events, no model attention required); MCP tools are **agent-initiated** (the model decides whether and when to call them, "remember to remember"). For *passive, deterministic logging*, hooks are the right primitive — MCP tools are the wrong primitive because they consume context and rely on model judgment. *"What you really want is passive, deterministic logging — something that captures every session event regardless of what the model is doing, without consuming any of its context or attention."*
- **Hooks are remarkably standardized across providers.** Claude Code, Codex, and Cursor all support the same five lifecycle events: `SessionStart`, `UserPromptSubmit` (or `beforeSubmitPrompt` in Cursor), `PreToolUse`, `PostToolUse`, `Stop`. The hook receives JSON on stdin and may emit JSON on stdout to inject context.
- **Two injection points**: `SessionStart` prepends to the system prompt (persistent agent-level memory); `UserPromptSubmit` appends to the user prompt (turn-level relevant memory).
- **One important constraint**: hooks run *outside* the harness's model session — you cannot reuse the LLM the agent is talking to. Any LLM-powered work inside a hook is a separate model call adding latency to *every* event. So the demonstration's hooks only do two fast, deterministic things: log events and inject pre-computed memories.
- **The dream phase** is the place LLM work happens. A periodic batch job pulls events accumulated since the last watermark, hands them to Claude with the current memory store, and asks for a small set of durable Markdown notes. *Merge, not append* — paths are living documents, not logs; if new events contradict an old note, the old note gets rewritten. Result: a tree of small self-contained markdown files (e.g. `profile/role.md`, `tools/bash/common-flags.md`, `project/neo4j-skills.md`), indistinguishable in form from a hand-authored skill.
- **Three-layer architecture**: hooks (online, log every event into Neo4j as a linked list per session — no model calls); dream phase (offline batch, distills events into markdown memories, merges); injection (online, pulls profile + relevant memories into context at session start and on each user prompt).
- **Code is on GitHub**: [tomasonjo/agent-memory-hooks-neo4j](https://github.com/tomasonjo/agent-memory-hooks-neo4j) — demonstration repo with the shared Python hook scripts.

## What was actually ingested

Full 17-page PDF read end-to-end — including the article body (introduction → "MCP tools can only get you so far with memory" → "Enter hooks" → "Shared memory layer" → "Dream phase" → "Accessing the memory" → "Getting it to work" → "Summary"), 8 diagrams, in-line screenshots of Cursor / Claude Code Desktop / Neo4j browser, and the related-articles footer. Bratanic discloses *"I work at Neo4j, so we will be using it in this example"* — vendor disclosure without compromising the *generalizability* of the hooks-as-primitive argument.

## Key claims in detail

### Why hooks beat MCP for memory

The post articulates a clean separation that the wiki has not previously named:

| Property | MCP tools | Hooks |
|---|---|---|
| Initiator | Agent (LLM-decided) | System (lifecycle-event-fired) |
| Reliability | Inconsistent — model has to "remember to remember" | Deterministic — every event fires |
| Context cost | Consumes model attention (tool description, tool call, response) | Zero context cost — runs outside the model session |
| Best for | On-demand search, store, update, delete | Passive logging, profile injection, append-only context |

> *"What you really want is passive, deterministic logging."*

Bratanic's verdict: *"In the end, I think you'll almost always need both"* — hooks for the deterministic always-on layer, MCP for the on-demand CRUD over the same store. In the demo project, only hooks are wired; the user notes the official Neo4j MCP can be plugged in to give the agent direct graph access if desired.

### The dream-phase markdown wiki

The most operationally interesting section. Memories are written by Claude (via the offline dream-phase batch job) into a tree of small self-contained markdown files at semantic paths:

```
profile/role.md
profile/identity.md
tools/bash/common-flags.md
project/neo4j-skills.md
```

Each file has YAML frontmatter and prose underneath. Claude is *told to merge rather than append*, so paths are living documents, not logs. The shape is *"indistinguishable in form from a skill, just authored by the dream phase instead of by hand."*

This is the wiki's first source documenting **markdown-as-agentic-memory-format** as a convergent practice across:

- [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's]] LLM-wiki idea (the basis of *this* repository).
- **Anthropic's Skills** (markdown files invocable via metadata).
- The auto-generated memory in this demonstration.

The convergence is not coincidental: a markdown wiki is durable across models, human-readable for review, version-controllable in git, and structurally addressable (path = topic). It is the **artifact form** that survives harness switching.

### Hook lifecycle event semantics

The five-event contract supported by Claude Code / Codex / Cursor (paraphrased from the post):

| Event | Fires | Used for |
|---|---|---|
| `SessionStart` | Once per session, *before the agent reads its system prompt* | Inject persistent agent-level memory (profile, instructions on memory use) — emitted JSON gets prepended to the system prompt |
| `UserPromptSubmit` (or `beforeSubmitPrompt` in Cursor) | On every user turn, *just before the user message is sent* | Inject turn-relevant memory (e.g. pull memories matching what the user just typed) — emitted JSON appended to the user prompt |
| `PreToolUse` | Before each tool call | Log tool name + input |
| `PostToolUse` | After each tool call | Log tool result + duration |
| `Stop` | Once when the session ends | Log `ended_at` |

The post's diagram shows session structure as a linked list: `Session → SessionStart → UserPromptSubmit → PreToolUse → PostToolUse → Stop`, with `HAS_FIRST_EVENT` and `NEXT` edges.

### The portability claim

> *"You can switch from Cursor to Claude Code to Codex mid-project and pick up exactly where you left off. Your agent's understanding of who you are, what you're working on, and how you prefer to work follows you, not the tool."*

Operationally: the same two Python scripts (`log_event.py`, `inject_memory.py`) handle all three clients; thin shell wrappers passing a `--client` flag are the only per-harness glue. Configuration lives in `.claude/settings.json`, `.codex/hooks.json`, `.cursor/hooks.json` respectively — three files, same script.

This **directly substantiates** [[2026-05-04-rethinking-agents-harness-is-all-you-need|the transferability finding]] from the Khattab et al. Meta-Harness work (a harness optimised on one model improved five other models). Bratanic's claim is one tier higher: a *shared substrate component of harness configuration* (memory) is portable across three different vendor harnesses, not just across models.

## Cross-source resonance

| Source | Connection |
|---|---|
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | Bratanic's `SessionStart` + `UserPromptSubmit` injection points are concrete implementations of Chatterjee's **Context** layer (system prompt as document with stable + dynamic parts). The dream phase is one realization of Chatterjee's **Compounding** layer (telemetry → durable harness assets), with the load-bearing detail that *raw events are preserved and distilled offline* — operationally identical to the [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Khattab et al. finding]] that *"raw traces are irreplaceable"* (50% → 34% accuracy when traces removed; 34.9% when summarised). |
| [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] | Hooks fit neatly into Kokane's 7-building-block architecture as *event-driven hook layer* — neither a tool executor nor a context manager but a separate cross-cutting concern. The post effectively argues for a **9th building block: lifecycle hooks** — a unit of harness work distinct from MCP tools / state / context / observability. |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo 2026]] (OpenAI Codex) | Lopopolo's Codex-team workflow is heavily hook-mediated (background "doc-gardening" tasks, custom linters, taste-invariant scans) — many of which are written via the same lifecycle-hook contract Bratanic documents. The two posts together name **hooks as a first-class harness primitive** with an emerging cross-vendor contract. |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | The dream-phase markdown wiki is *Karpathy's LLM-wiki idea applied at the agentic-memory layer*. This is a strong cross-source convergence: human-authored personal LLM wikis, agent-authored agentic memory, and Anthropic's Skills all converge on the same artifact format. |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic 2026]] (Managed Agents) | Anthropic's *brain / hands / session* split implies the *session* layer can be decoupled from the *brain*. Bratanic operationalizes that exact decoupling — session memory lives in Neo4j, accessible to whichever brain the user picks today. |
| **The repo's own [`scripts/session-start.mjs`](../../scripts/session-start.mjs) / `scripts/lint-page.mjs`](../../scripts/lint-page.mjs) / `scripts/session-end.mjs`** | This wiki's [`hooks` schema section](../../CLAUDE.md#hooks) is operationally the same architecture Bratanic describes: `SessionStart` injects context (catalog counts, recent log entries, lifecycle flags); `PostToolUse` lints; `Stop` re-exports the graph. The wiki does not write its own memory, but the *mechanism* is identical to Bratanic's, just bound to a different artifact type (the wiki itself). Worth noting on the `hooks` section that the convergence with practitioner work outside this repo is now substantial. |

## Linked entities and concepts

- **Author (1st mention; Dangling per [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion))**: Tomaz Bratanic (Neo4j). Promote on second-source mention.
- **Organizations (1st mention)**: **Neo4j** (graph database vendor; author's employer; substrate for the demo). Bratanic's prior writing is named in the related-articles section ("Preventing Context Overload: Controlled Neo4j MCP Cypher Responses for LLMs," Sep 2025) — same author, same vendor — but those are not yet wiki sources. Promote Neo4j on second wiki source mention.
- **Products / harnesses mentioned**: **Claude Code**, **Codex**, **Cursor**, **Claude Code Desktop**, **Neo4j MCP server**. All product/harness names; not promoted on a single mention.
- **Concepts touched**:
  - [[agent-harness]] — major. Hooks as primitive; portability of memory across harnesses. Concept page extension warranted.
  - [[ai-agents]] — agentic memory as a layer.
  - [[foundation-models]] — Claude as the dream-phase distiller.
  - **Hooks as a candidate concept**: not yet promoted to its own concept page. The combination of *Lopopolo (Codex)* + *Bratanic (TDS)* + *the repo's own [`hooks` section](../../CLAUDE.md#hooks)* gives three independent vantages on hooks-as-harness-primitive. After ingesting the Lopopolo source page in this same batch, hooks meets the **second-source convergence threshold** and is a strong candidate for promotion. Decision deferred to the concept-page sweep at the end of this ingest batch.

## Notes on confidence and lifecycle

- **Source quality**: practitioner essay on a community publication (TDS, Insight Media Group). Vendor-affiliated author (Neo4j) with disclosed conflict; the *architectural argument* (hooks vs. MCP) is independent of the choice of store and well-supported by the cross-vendor convergence on lifecycle-event contracts.
- **Page does not carry `confidence:`** — sources are evidence, not claims.
- **Working code is published** on GitHub (linked from the article); the demonstration is reproducible. Raises evidential weight above an essay-only source.

## What this source does *not* do

- It does **not** measure latency / cost overhead of always-on hooks vs. selective MCP usage. *"Hooks stay fast and deterministic"* is asserted but not measured.
- It does **not** address how the dream-phase prompt is engineered, what prevents memory bloat over months of use, or what happens when the dream phase distills *bad* generalizations into a profile note that then gets injected on every session start. The "merge not append" instruction is the safety mechanism, but operational failure modes (e.g. recency-biased memory that drifts) are not discussed.
- It does **not** compare its design to Anthropic's emerging memory tools (named in passing in [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]) or to Cursor's / Cline's built-in memory features. The implicit framing is *roll-your-own outside the harness*; built-in alternatives are not weighed.
- It does **not** address multi-user / team scenarios — the demo is single-user. Whether the same architecture works for a shared team memory (with conflict resolution, access control, redaction) is unaddressed.

These are reasonable elisions for a 9-minute essay; flag as gaps a follow-up source would need to fill.
