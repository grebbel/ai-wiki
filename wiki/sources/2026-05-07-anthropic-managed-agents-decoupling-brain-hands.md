---
type: source
kind: article
title: "Scaling Managed Agents: Decoupling the brain from the hands"
author: ["Lance Martin", "Gabe Cemaj", "Michael Cohen"]
publisher: "Anthropic"
journal_volume: "Engineering at Anthropic blog, 8 April 2026"
url: "https://www.anthropic.com/engineering/scaling-managed-agents"
date_published: 2026-04-08
date_ingested: 2026-05-07
tags: [ai-agents, anthropic, managed-agents, claude-platform, agent-architecture, harness, sandbox, session, long-horizon-agents, security-boundary, prompt-injection]
length: "~6 pages of body content (article body; site-footer/nav excluded)"
raw: "../../raw/articles/Scaling Managed Agents_ Decoupling the brain from the hands _ Anthropic.pdf"
---

# Anthropic Engineering — Scaling Managed Agents: Decoupling the brain from the hands

## TL;DR

An **Engineering at Anthropic** blog post (8 April 2026) by Lance Martin, Gabe Cemaj, and Michael Cohen announcing **Managed Agents**, a hosted service in the Claude Platform for long-horizon agent work. Built around interfaces designed to *outlast specific harness implementations*. The article is part engineering retrospective ("here's what failed first") and part architecture spec — it documents the brain/hands/session decoupling pattern that the team converged on, and the specific interfaces they chose to virtualize.

**Central design metaphor:** decouple the **brain** (Claude + harness) from the **hands** (sandbox + tools) and the **session** (durable event log). Each is independently replaceable; each fails in isolation; each is reachable across infrastructure boundaries.

This is the most concrete public-facing engineering description of [[ai-agents|production agent architecture]] in the wiki to date — closer to a systems-design paper than a marketing post.

## Why the team rebuilt the architecture

The team started by placing all agent components into a single container: session, harness, and sandbox shared one environment. Direct file edits via syscall, no service boundaries, simpler to ship — but it produced two pathologies:

1. **The "pet" problem.** Containers became hand-tended individuals — if one failed, the session was lost; if it became unresponsive, engineers had to nurse it back to health. In the pets-vs-cattle distinction, they had pets when they wanted cattle.
2. **Debugging blindness.** Stuck sessions had only the WebSocket event stream as a window — but it couldn't tell *where* failures arose. A bug in the harness, a packet drop, a container going offline all looked the same. Opening a shell into the container risked touching user data.
3. **Network coupling.** When customers asked to connect Claude to their own VPC, they had to peer their network with Anthropic's or run the harness in their environment. An assumption baked into the harness ("everything Claude works on lives in this container with it") became a hard constraint.

**Concrete model-version anecdote** the article uses to motivate "harnesses encode assumptions that go stale": Claude Sonnet 4.5 wrapped up tasks prematurely as it sensed context limits approaching ("**context anxiety**"). The team patched this with context resets in the harness. When the same harness was deployed against Claude Opus 4.5, the behavior was gone — and the resets had become dead weight. The harness needed to be replaceable as models changed.

## The decoupled architecture

> "We virtualized the components of an agent: a session (the append-only log of everything that happened), a harness (the loop that calls Claude and routes Claude's tool calls to the relevant infrastructure), and a sandbox (an execution environment where Claude can run code and edit files). This allows the implementation of each to be swapped without disturbing the others. We're opinionated about the shape of these interfaces, not about what runs behind them."

**The component interfaces (pseudocode, abridged):**

| Component | Interface | Satisfied by |
| --------- | --------- | ------------ |
| **Session** | `getSession(sid) → (Session, Event[])`, `getEvents(sid) → PendingEvent[]`, `emitEvent(id, event)` | Any append-only log accepting idempotent appends — Postgres, SQLite, in-memory array, etc. |
| **Orchestration** | `wake(sid) → void` | Any scheduler — cron, queue consumer, while-loop |
| **Harness** | `yield Effect<T> → EffectResult<T>` | Any loop that yields effects and appends progress to the session |
| **Sandbox** | `provision({resources})`, `execute(name, input) → String` | Any executor — local process, remote container, hosted IDE |
| **Resources** | `[{source_ref, mount_path}]` | Any durable store — Filestore, GCS, git remote, S3 |
| **Tools** | `{name, description, input_schema}` | Any capability describable as a name and input shape — MCP server, custom tool |

**Three properties this enables:**

### 1. The harness leaves the container

The harness no longer lives inside the sandbox. It calls the sandbox the way it calls any other tool: `execute(name, input) → string`. If the container dies, the harness catches the failure as a tool-call error and passes it back to Claude. If Claude decides to retry, a new container reinitializes via `provision({resources})`. Containers became cattle.

### 2. Recovering from harness failure

Because the session log sits outside the harness, **nothing in the harness needs to survive a crash**. When a harness fails, a new one boots with `wake(sessionId)`, calls `getSession(id)` to retrieve the event log, and resumes from the last event. The harness writes to the session via `emitEvent(id, event)` to keep the durable record current.

### 3. The security boundary

Untrusted code generated by Claude must not reach credentials. The team uses two patterns:

- **Auth bundled with the resource.** For Git: each repository's access token is used during sandbox initialization and wired into a local Git remote. `git push` and `pull` work from inside the sandbox without the agent ever handling the token.
- **Auth held in vault outside the sandbox.** For custom tools: MCP-via-proxy. Claude calls MCP tools via a dedicated proxy; the proxy holds OAuth tokens in a secure vault and authenticates upstream. The harness is never made aware of any credentials.

This is the structural fix for prompt-injection attacks that try to convince Claude to read credentials from its own environment — narrow scoping is mitigation; making credentials structurally unreachable is the fix.

## The session is not Claude's context window

The most architecturally distinctive choice in the article. Long-horizon tasks routinely exceed context window length, and the standard fixes (compaction, memory tools, context trimming) all involve **irreversible decisions about what to keep**. If a compacted message is later needed, it's gone unless explicitly stored.

The Managed Agents pattern: **the session is a context object that lives outside the context window.** The harness fetches events via `getEvents()` and selects positional slices of the event stream — it can pick up wherever it last stopped, rewind a few events to see the lead-up, or re-read context before a specific action. Any fetched events can also be transformed in the harness before being passed back to Claude — including **context organization to maximize prompt cache hit rate** and arbitrary context engineering.

The architectural separation matters: *the session guarantees durability and interrogability; the harness guarantees context engineering*. They're separate concerns because the team can't predict what specific context engineering future models will need.

## Many brains, many hands

**Many brains.** Decoupling solved an early customer complaint: when teams wanted Claude to work against their own VPC, the previous architecture required network peering. With the harness no longer in the container, that assumption disappears. Plus a TTFT (time-to-first-token) win: when the brain was in a container, every session paid the full container setup cost up-front (clone the repo, boot the process, fetch pending events). Decoupled, **containers are provisioned only when actually needed**. p50 TTFT dropped ~60%; p95 dropped over 90%.

**Many hands.** Each hand becomes a tool: `execute(name, input) → string`. The harness doesn't know whether the sandbox is a container, a phone, or a Pokémon emulator. And because no hand is coupled to any brain, **brains can pass hands to one another**.

## Conclusion: meta-harness as design philosophy

> "Managed Agents is a meta-harness in the same spirit [as operating systems], unopinionated about the *specific* harness that Claude will need in the future. Rather, it is a system with general interfaces that allow many different harnesses."

Specific examples named: **Claude Code** is "an excellent harness that we use widely across tasks"; task-specific agent harnesses excel in narrow domains. Managed Agents accommodates any of these, matching Claude's intelligence over time.

## Cross-source positioning

This article is the wiki's first **production-grade engineering description** of long-horizon agent architecture. It complements rather than supersedes existing agent-related material:

- **Extends [[ai-agents]] substantially.** The chatbot → agent → multi-agent progression now has an *engineering* layer beneath it. The brain/hands/session decoupling explains *how* multi-agent systems can scale (many brains, many hands, brains passing hands to one another) and *why* prior attempts produced the "pet" pathology.
- **Reinforces [[2026-04-28-anthropic-economic-index-q4-2025|the AEI 4th report's]] task-horizon discussion.** That report observed that Claude Sonnet 4.5 reached 50% success at ~19h on Claude.ai (vs ~2h on METR's fixed benchmark). The session-as-context-outside-the-window architecture is part of *why* — Claude.ai effectively uses durable session state to extend effective horizons via decomposition + feedback loops, exactly the pattern Managed Agents productizes.
- **Concrete instance of the [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria firm-boundary "Buy Outcomes"]] model.** Anthropic deploying Managed Agents directly with the customer (running long-horizon work on the customer's behalf, with general interfaces meant to outlast specific implementations) is the operational shape of "buy outcomes, not tools" from the customer's vantage.
- **Engineering analogue to [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al.'s]] Vantage Executive LLM.** Both papers are about *infrastructure for stateful, multi-turn AI work* — Vantage steers conversation toward eliciting durable-skill evidence; Managed Agents virtualizes the agent components so long-horizon agent work survives failures and model changes. Different domains (assessment vs production), same architectural sensibility (separate the cognitive layer from the persistence layer).
- **Touches [[responsible-ai]] via the security-boundary discussion.** Prompt-injection mitigation as *structural unreachability* of credentials, not as *narrow scoping*, is a notable RAI-engineering pattern.

## Source-quality flag

- **Type:** Engineering blog post, not a peer-reviewed paper. Marketing surface ("Get started with Claude Managed Agents by following our docs") but the technical content is substantive.
- **Empirical content:** specific TTFT numbers (p50 ~60% drop, p95 90%+) and concrete model-behavior anecdotes (Sonnet 4.5 context anxiety; Opus 4.5 not exhibiting it). No formal experiments or A/B test data.
- **Confidence boost:** +0.05 per the [§Lifecycle](../../CLAUDE.md#lifecycle) "additional supporting source" rule, with no peer-review or large-N empirical bonus. Treat as *high-quality engineering documentation* — closer to an OS-paper from a major lab than a typical product announcement, but not academic-grade.
- **Vendor-of-deployment flag:** Anthropic publishes this both as engineering authority and as customer-acquisition material for the Claude Platform. Read with that vantage in mind. Specific architectural claims (e.g., "TTFT p50 dropped ~60%") are unverifiable from outside.

## Linked entities and concepts

**Entities (this wiki):** [[Anthropic]] (publisher; bumps `source_count`). **Dangling** (single-source mention, deferred): Lance Martin, Gabe Cemaj, Michael Cohen (article authors), Nodir Turakulov, Jeremy Fox, Jake Eaton (acknowledged); Claude Platform / Claude Managed Agents (Anthropic product; promote on 2nd-source coverage); Claude Code (mentioned as "an excellent harness").

**Concepts:** [[ai-agents]] (heavy enrichment — engineering architecture for long-horizon agents), [[foundation-models]] (light — Claude Sonnet 4.5 vs Opus 4.5 model-behavior anecdote), [[responsible-ai]] (light — security boundary as structural unreachability), [[generative-ai]] (light — Anthropic platform infrastructure). Adjacent: [[automation-vs-augmentation]] (multi-agent infrastructure pushes toward higher AI autonomy on the API side), [[enterprise-ai-adoption]] (Managed Agents is enterprise-deployment infrastructure).

**Threads/syntheses:** none directly affected.

## Source

- **Raw PDF (~12 pages incl. site footer; ~6 pages of article body):** [article file](../../raw/articles/Scaling%20Managed%20Agents_%20Decoupling%20the%20brain%20from%20the%20hands%20_%20Anthropic.pdf)
- **Publisher:** Anthropic (Engineering at Anthropic blog)
- **Date:** April 8, 2026
- **Authors:** Lance Martin, Gabe Cemaj, Michael Cohen
- **Acknowledgements:** Nodir Turakulov, Jeremy Fox; Agents API team; Jake Eaton
