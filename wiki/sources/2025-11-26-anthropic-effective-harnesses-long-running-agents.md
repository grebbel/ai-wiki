---
type: source
kind: article
title: "Effective harnesses for long-running agents"
author: ["Justin Young"]
publisher: "[[Anthropic]]"
section: "Engineering at Anthropic"
url: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
date_published: 2025-11-26
date_ingested: 2026-05-17
length: "~8-page web essay; read in full"
raw: "../../raw/articles/06_Anthropic_Effective-Harnesses-Long-Running-Agents.pdf"
tags: [agent-harness, anthropic-engineering, long-running-agents, initializer-agent, coding-agent, claude-progress, feature-list-json, claude-agent-sdk, opus-45, multi-context-window, compaction-insufficient, harness-engineering, claude-ai-clone]
relationships:
  - type: supports
    target: 2024-12-19-anthropic-building-effective-agents
    via: "direct continuation, 11 months later. The Dec 2024 post named workflows-vs-agents and the 5 patterns; this Nov 2025 post applies those principles to multi-context-window long-horizon work, surfacing failure modes the original post didn't address."
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Anthropic's two-fold (initializer agent + coding agent) solution for context-window-spanning work is the production-engineering equivalent of Karten's reset-free episode framing. Where Karten's emulator state propagates the trajectory, Anthropic uses init.sh + claude-progress.txt + feature_list.json as the file-backed handoff equivalent."
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "this Nov 2025 post lays the architectural foundation for the brain/hands/session decomposition that Anthropic Managed Agents (Apr 2026) productises 5 months later"
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Anthropic's explicit naming of 4 failure modes + structured solutions (initializer agent + coding agent + feature_list.json + claude-progress.txt) is the canonical operationalisation of Osmani's ratchet — each line in the solution is traceable to a documented failure"
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "Anthropic's claude-progress.txt + feature_list.json pattern is the vendor-production form of Pan's path-addressable, compaction-stable file-backed state module"
  - type: uses
    target: agent-harness
---

# Young — *Effective harnesses for long-running agents*

A **~8-page Engineering at Anthropic blog post**, published **26 November 2025** by **Justin Young**. **The wiki's first primary-source from Anthropic Engineering on the long-running-agent / multi-context-window problem specifically** — explicitly built atop the Dec 2024 [[2024-12-19-anthropic-building-effective-agents|*Building effective agents*]] foundation. Listed by [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video]] as a foundational reference; cited by [[2026-05-15-osmani-agent-harness-engineering|Osmani]] as the *"best public breakdown of how to design a harness for long-running work"*; cited by [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al.]] (Anthropic 2025b in references); cited by [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] indirectly via the harness-engineering thread.

This post pre-dates the wiki's existing [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] source by **5 months** and operates at the *engineering-pattern* layer below the *architecture-productisation* layer. **The wiki's strongest single vendor-side primary on the practitioner discipline that became known as harness engineering.**

## TL;DR

- **The thesis.** *"Agents still face challenges working across many context windows. We looked to human engineers for inspiration in creating a more effective harness for long-running agents."* The core problem: agents work in discrete sessions; each new session begins with no memory of what came before. *"Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift."*
- **Compaction is not sufficient.** *"Out of the box, even a frontier coding model like Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows will fall short of building a production-quality web app if it's only given a high-level prompt, such as 'build a clone of claude.ai.'"* — **First wiki source naming compaction as insufficient at the engineering-pattern layer.** Two named failure modes:
  - The agent *tries to do too much at once* (one-shot the app) → context exhaustion mid-implementation; next session inherits half-done feature with no documentation.
  - Later sessions *declare premature victory* after seeing some features built.
- **The two-fold solution** (the wiki's strongest primary anchor for the initializer-agent / coding-agent pattern):
  - **Initializer agent** — runs in the first session. Sets up the environment: an `init.sh` script that can run the development server; a `claude-progress.txt` file that keeps a log of what agents have done; an initial git commit that shows what files were added. Plus: a `feature_list.json` file with all the end-to-end features described in detail, all initially marked `"passes": false`.
  - **Coding agent** — every subsequent session asks the model to make incremental progress, then leave structured updates. Reads `pwd` / `claude-progress.txt` / `feature_list.json` / git log on session start. Works on one feature at a time. Commits to git with descriptive messages. Writes summaries of progress to the progress file.
- **The feature_list.json pattern.** *"To address the problem of the agent one-shotting an app or prematurely considering the project complete, we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user's initial prompt. In the claude.ai clone example, this meant over 200 features."* Strict edit policy: *"We prompt coding agents to edit this file only by changing the status of a `passes` field, and we use strongly-worded instructions like 'It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.'"* **JSON over Markdown because *"the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."*** The wiki's strongest single empirical observation on file-format choice for agent-edited persistent state.
- **Testing the harness must include browser automation.** *"Absent explicit prompting, Claude tended to make code changes, and even do testing with unit tests or `curl` commands against a development server, but would fail recognize that the feature didn't work end-to-end."* Solution: explicit prompting + Puppeteer MCP server screenshots. *"Some issues remain, like limitations to Claude's vision and to browser automation tools making it difficult to identify every kind of bug. For example, Claude can't see browser-native alert modals through the Puppeteer MCP, and features relying on these modals tended to be buggier as a result."*
- **The "getting up to speed" sequence** (every coding-agent session starts with):
  1. Run `pwd` to see the directory.
  2. Read git logs and progress files to see recent work.
  3. Read the features list file and choose the highest-priority not-yet-done feature.

  *"This approach saves Claude some tokens in every session since it doesn't have to figure out how to test the code."*
- **The 4 named failure modes + initializer/coding agent solutions** (the wiki's canonical table for this pattern):

| Problem | Initializer Agent Behavior | Coding Agent Behavior |
|---|---|---|
| Claude declares victory on entire project too early | Set up feature list file: structured JSON file with list of end-to-end feature descriptions | Read the feature list file at session start. Choose a single feature to work on |
| Claude leaves the environment in a state with bugs or undocumented progress | An initial git repo and progress notes file is written | Start session by reading the progress notes file and git commit logs; run basic test on dev server. End session by writing git commit and progress update |
| Claude marks features as done prematurely | Set up a feature list file | Self-verify all features. Only mark features as "passing" after careful testing |
| Claude has to spend time figuring out how to run the app | Write an `init.sh` script that can run the development server | Start session by reading `init.sh` |
- **The Claude.ai clone worked example.** 200+ features in the initial JSON. Initializer agent generates these from the high-level prompt. Coding agents iterate one feature at a time. Puppeteer MCP for browser-side end-to-end testing. The agent "always started the local development server and used the Puppeteer MCP to start a new chat, send a message, and receive a response."
- **Closing on multi-agent.** *"It's still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture. It seems reasonable that specialized agents like a testing agent, a quality assurance agent, or a code cleanup agent, could do an even better job at sub-tasks across the software development lifecycle."* — Anticipates by 5 months [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]'s brain / hands / session decomposition.
- **Acknowledgements.** Written by **Justin Young**. Special thanks to David Hershey, Prithvi Rajasakeran, Jeremy Hadfield, Naia Bouscal, Michael Tingley, Jesse Mu, Jake Eaton, Marius Buleandara, Maggie Vo, Pedram Navid, Nadine Yasser, Alex Notov. Notes: *"This work reflects the collective efforts of several teams across Anthropic who made it possible for Claude to safely do long-horizon autonomous software engineering, especially the code RL & Claude Code teams."*
- **Footnote on "agents".** *"We refer to these as separate agents in this context only because they have different initial user prompts. The system prompt, set of tools, and overall agent harness was otherwise identical."* — Strong vendor-side confirmation that **"agents" in the Anthropic vocabulary are differentiated by prompt + role, not by underlying harness**.

## What was actually ingested

Full ~8-page web article. All 4 named failure modes + initializer/coding solutions table. The Claude.ai clone worked example with Puppeteer screenshots referenced. Future work section. Acknowledgements.

## Cross-positioning with the wiki

### Closes a load-bearing primary-source ingest target

This post has been a wiki ingest target since the [[2026-05-15-osmani-agent-harness-engineering|Osmani]] cluster ingest (yesterday's batch) named it as a key reference. Multiple downstream wiki claims now have a primary-source anchor:

| Wiki claim (status before this ingest) | Status after |
|---|---|
| **Initializer agent + coding agent pattern** (carried second-hand via Osmani's HaaS framing) | **Closed — primary source ingested.** The pattern is exactly: init.sh + claude-progress.txt + feature_list.json + git commits. |
| **"Compaction alone wasn't sufficient"** (Osmani referenced this as an Anthropic claim) | **Closed — verified.** *"Compaction isn't sufficient. Out of the box, even Opus 4.5 will fall short of building a production-quality web app."* |
| **JSON over Markdown for agent-edited persistent state** (no prior wiki source) | **New finding.** Models are less likely to inappropriately change or overwrite JSON files compared to Markdown files. |
| **The "every line of AGENTS.md traceable to a failure" ratchet** (Osmani) | **Confirmed empirically.** The 4-failure-modes-table is the canonical Anthropic-Engineering form of the ratchet — each of the 4 patterns was added to address a documented failure. |
| **"Multi-context-window engineering is its own discipline"** | **Closed — verified.** *"Most complex projects cannot be completed within a single window, agents need a way to bridge the gap between coding sessions."* |

### The architectural lineage to Anthropic Managed Agents

| | This post (Nov 2025) | Anthropic Managed Agents (Apr 2026) |
|---|---|---|
| **Mechanism for bridging sessions** | init.sh + claude-progress.txt + feature_list.json + git commits | session as the explicit orchestration primitive outliving any one context window |
| **Trust model** | Coding agent reads structured state before acting | Brain produces intent; hands decide whether to execute; session holds state |
| **Specialised roles** | Initializer + coding agent | Brain + hands + session |
| **Compaction status** | "Not sufficient" | Implied — same direction |

The 5-month evolution Anthropic took (Nov 2025 → Apr 2026) is **from prompt-pattern (initializer / coding) to architectural primitive (brain / hands / session)**. The wiki should body-link this lineage on [[concepts/agent-harness]].

### Anticipates Pan et al.'s file-backed state module

[[2026-03-26-pan-natural-language-agent-harnesses|Pan et al.]] formalise file-backed state with three properties: **externalized**, **path-addressable**, **compaction-stable**. Anthropic's claude-progress.txt + feature_list.json + git commit log satisfy all three. **This post is the production-engineering origin of what Pan et al. later formalise.** Worth a body-link on Pan's source page.

### Anticipates Karten's reset-free framing

[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]]'s Continual Harness operates reset-free with state propagation across iterations. Anthropic's Nov 2025 post is the engineering origin: *"the emulator state at the end of iteration k is loaded as the start of iteration k+1"* (Karten) ≈ *"the next iteration of the coding agent was then asked to work on only one feature at a time"* (Young) **with the same intent — durable state propagation across what would otherwise be reset boundaries**.

## Named entities (this ingest)

- [[Justin Young]] — Anthropic Engineering, post author. **First mention. Dangling.**
- [[David Hershey]], [[Prithvi Rajasakeran]], [[Jeremy Hadfield]], [[Naia Bouscal]], [[Michael Tingley]], [[Jesse Mu]], [[Jake Eaton]], [[Marius Buleandara]], [[Maggie Vo]], [[Pedram Navid]], [[Nadine Yasser]], [[Alex Notov]] — Anthropic Engineering / collaborators. All thanked in acknowledgements. **First mentions. Dangling.**
- [[Puppeteer MCP]] — browser-automation MCP server. **First mention.**
- Anthropic *code RL & Claude Code teams* — internal team references.

## Source-quality notes

- **Genre**: vendor engineering blog post (Anthropic). Highly influential — cited across the harness cluster.
- **Empirical content**: zero formal measurement; the post is **production-engineering pattern documentation** built around the Claude.ai-clone worked example. Anthropic engineering's vantage on agent deployments is its credibility.
- **Reproducibility**: explicit reference to the [Claude Agent SDK quickstart](https://docs.claude.com/en/docs/claude-code/sdk/sdk-quickstart) for working code. The post pre-figures (but doesn't fully demonstrate) the harness as a productizable artifact.
- **Confidence: 0.80.** Per Lifecycle: single source +0.05 for vendor-engineering primary-source +0.05 for being the canonical Osmani-referenced anchor on long-running-agent harness = 0.80.

## Open questions

- **JSON-over-Markdown for agent-edited state — does this generalise?** Anthropic claims this empirically. Worth tracking against other vendors' experience (LangChain, OpenAI Codex). Has implications for [[concepts/llm-wiki]] which uses markdown for the wiki layer — if model-induced markdown-overwrite is a real risk, the wiki may need to migrate certain LLM-edited state to JSON.
- **Single general-purpose agent vs multi-agent.** Anthropic flags this as open. Five months later [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] explicitly endorses the multi-agent direction (brain/hands/session). Worth a body-note on Managed Agents' relationship to this open question.
- **Beyond web-app development.** Future-work section: *"this demo is optimized for full-stack web app development. A future direction is to generalize these findings to other fields. It's likely that some or all of these lessons can be applied to the types of long-running agentic tasks required in, for example, scientific research or financial modeling."* Worth tracking.
