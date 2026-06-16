---
type: source
kind: article
title: "Agent Harness Engineering"
subtitle: "A coding agent is the model plus everything you build around it. Harness engineering treats that scaffolding as a real artifact, and it tightens every time the agent slips."
author: ["Addy Osmani"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar"
url: "https://www.oreilly.com/radar/agent-harness-engineering/"
original_venue: "addyosmani.com (Addy Osmani's blog)"
date_published: 2026-05-15
date_ingested: 2026-05-16
length: "~17 minute read (20-page PDF print; substantial body with two named diagrams)"
raw: "../../raw/articles/Agent Harness Engineering – O'Reilly.pdf"
tags: [agent-harness, agentic-engineering, harness-engineering, claude-code, ralph-loop, agents-md, hooks, sandboxes, compaction, harness-as-a-service, oreilly-radar]
dynamic_capabilities:
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "Osmani names the same 4-layer pattern (Context/Constraints/Contracts/Compounding) under different vocabulary and credits Viv (Chatterjee's referenced framing) as the originator of the 'harness engineering' term"
  - type: supports
    target: 2026-05-07-kokane-agent-harness-vs-systems-design
    via: "shares the operating-system-style decomposition (filesystem / bash / sandbox / memory / planning) and treats harness as a configurable surface"
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "explicitly cites Anthropic's harness write-up as the best public breakdown of long-running agent design and quotes its 'every harness component encodes an assumption about what the model can't do on its own' line"
  - type: supports
    target: 2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy
    via: "Osmani names Bockeler as one of the practitioners tracking the harness pattern and shares Bockeler's user-side framing of context/harnessing/autonomy"
  - type: supports
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "Bratanic operationalises hooks as a portable primitive; Osmani's 'Hooks: The enforcement layer' section names the same architectural slot with the same enforcement rationale ('Success is silent; failures are verbose')"
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "shares the Terminal Bench transfer-across-models finding (Viv's team moving Top 30 → Top 5 by changing only the harness) as the load-bearing empirical anchor for the harness-not-model thesis"
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "ratifies Karpathy's agentic-engineering frame from a working-engineer vantage; the 'ratchet — every mistake becomes a rule' pattern is agentic-engineering's discipline made concrete"
  - type: supports
    target: 2026-02-11-lopopolo-codex-harness-engineering
    via: "Lopopolo names the vendor-side production case; Osmani names the practitioner-side discipline. The 'harness is a living system, not a config file you set up once' line and AGENTS.md-as-table-of-contents pattern explicitly echo Lopopolo's invariants"
---

# Osmani — Agent Harness Engineering

A **17-minute O'Reilly Radar essay** by **[[Addy Osmani]]** (Google engineering leader; longtime web-performance / Chrome DevRel author), reposted from his personal blog by O'Reilly with permission. Published **15 May 2026**. Pulls together the harness-engineering threads from **Viv Trivedy** (originator of the term), **Dex Horthy / HumanLayer**, **Anthropic's engineering team**, and **Birgitta Böckeler** (Thoughtworks) — all of which are already in the wiki as discrete sources — into the **first consolidated practitioner-facing field guide** under the explicit name **"harness engineering"**.

Osmani's contribution is not the architecture (Chatterjee, Kokane, Anthropic, Bockeler, Bratanic have all named pieces of it) but the **operationalising discipline**: a working rule-set for *how to do the engineering*, derived from the failure surface of his own work and the named practitioners' write-ups. Three of those rules are load-bearing for the wiki:

1. **"A decent model with a great harness beats a great model with a bad harness."**
2. **"Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."** *Ratchet, don't brainstorm.*
3. **"The gap between what today's models can do and what you see them doing is largely a harness gap."**

## TL;DR

- **The category-error fix.** The two-year industry debate over "which model is smartest" is missing half the system. The model is one input; the rest — prompts, tools, context policies, hooks, sandboxes, subagents, feedback loops, recovery paths — is **the harness**. *"If you're not the model, you're the harness."* Mature engineering attention is moving from the left-hand side of `agent = model + harness` to the right.
- **The "skill issue" reframe.** When an agent makes a mistake, the default move is to blame the model and wait for the next version. Harness engineering rejects that default. *Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again* — add it to AGENTS.md, write a hook that blocks it, split the task into planner + executor, add a typecheck back-pressure signal. **HumanLayer**: *"It's not a model problem. It's a configuration problem."*
- **The Terminal Bench transfer-across-models data point.** **Claude Opus 4.6 inside Claude Code scores far lower than the same model in a custom harness.** **Viv's team moved a coding agent from Top 30 to Top 5 on Terminal Bench 2.0 by changing only the harness.** Posttraining couples a model to the harness it was trained against; moving it into a different harness with better tools / tighter prompt / sharper backpressure can unlock capability the original harness was leaving on the floor. *This is the opposite of the "just wait for GPT-6" narrative.*
- **The ratchet.** *Every mistake becomes a rule. You only add constraints when you've seen a real failure. You only remove them when a capable model has made them redundant.* Worked examples Osmani gives: commented-out test merged by accident → next AGENTS.md says "never comment out tests; delete them or fix them" → precommit hook greps for `.skip(` and `xit(` → reviewer subagent flags commented-out tests as blockers. **Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong.**
- **Working backward from behavior** (the design pattern Osmani credits to Viv). Start from the behavior you want or want to fix; derive the harness piece that delivers it. *Behavior we want (or want to fix) → harness design to help the model achieve this.* The corollary: *if you can't name the behavior a component exists to deliver, it probably shouldn't be there.*
- **Six harness primitives**, each existing because the model can't do something on its own:
  - **Filesystem + Git** — durable state. Workspace + intermediate-work offload + shared coordination surface + free versioning. *"Most of the other harness primitives end up pointing at the filesystem for something."*
  - **Bash + code execution** — general-purpose tool. *"Teaching someone to use a single kitchen gadget vs handing them a kitchen."* **Simon Willison**'s essence: an agent is a system that *"runs tools in a loop to achieve a goal."*
  - **Sandboxes + default tooling** — safe execution surface. Allow-list commands, network isolation, on-demand spin-up. Good defaults: pre-installed runtimes, Git + test CLIs, headless browser. Browsers + logs + screenshots + test runners are what let the agent **observe its own work** and close the self-verification loop.
  - **Memory + search** — continual learning. AGENTS.md as memory file standard. Web search + MCP (Context7) bridge knowledge that didn't exist at training time.
  - **Context-rot countermeasures** — *compaction*, *tool-call offloading* (head/tail kept, full output offloaded to filesystem), *skills with progressive disclosure*. Anthropic's contribution: **full context resets** — *compaction alone wasn't sufficient*; sometimes you need to start fresh with a structured handoff brief. *Closer to onboarding a new engineer than to "memory."*
  - **Long-horizon execution** — **Ralph loops**, **planning** as decomposition-into-plan-file, **self-verification** via predefined test suites looped back to the model, **planner/generator/evaluator splits** (separating generation from evaluation outperforms self-evaluation because *agents reliably skew positive when grading their own work — it's GANs for prose*), and the **sprint contract** pattern (negotiate "done" before code is written). *Writing down the done condition before starting has caught more scope drift than any prompt change I've ever made.*
- **Hooks: the enforcement layer.** *Hooks are what separate "I told the agent to do X" from "the system enforces X."* Lifecycle script slots — before tool call, after edit, before commit, on session start — for things the agent should never forget but often does: typecheck + lint + tests after every edit; block destructive bash (`rm -rf`, `git push --force`, `DROP TABLE`); require approval before opening PRs / pushing to main; auto-format on write. The HumanLayer principle Osmani converges on: **"Success is silent; failures are verbose."** If typecheck passes the agent hears nothing; if it fails, the error text is injected into the loop and the agent self-corrects. The feedback loop is almost free in the common case and directly actionable when something goes wrong.
- **AGENTS.md hygiene** — flat markdown rulebook at the root of your repo; lands in the system prompt every turn. Two hard-won lessons: **(1) keep it short** (HumanLayer keeps theirs <60 lines; *"pilot's checklist, not style guide"*); **(2) earn each line** (rules should trace to a specific past failure or hard external constraint — *"ratchet, don't brainstorm"*). Same discipline for tools: **ten focused tools outperform fifty overlapping ones** because the model can hold the menu in its head. HumanLayer's surface-level security concern: **tool descriptions populate the prompt, so any MCP server you install is trusted text the model will read** — a sloppy or malicious MCP can prompt-inject your agent before you've typed anything.
- **"Harnesses don't shrink; they move."** Anthropic's observation Osmani names explicitly: as models improve, the space of interesting harness combinations doesn't shrink — *it moves*. **Opus 4.6 largely killed Sonnet 4.5's context-anxiety failure mode** (the premature wrap-up problem); a whole class of anxiety-mitigation scaffolding Osmani was writing six months ago is now dead code. But *the ceiling moved with the model* — tasks that were unreachable are now in play, and they have their own failure modes that need their own scaffolding. **Anthropic's clean phrasing: "Every component in a harness encodes an assumption about what the model can't do on its own."** When the model gets better at something, that component becomes load-bearing for nothing and should come out. When the model unlocks something new, new scaffolding is needed to reach the new ceiling.
- **The model-harness training loop.** Today's agent products are posttrained with harnesses in the loop. *The model gets specifically better at the actions the harness designers think it should be good at: filesystem ops, bash, planning, subagent dispatch.* Why Opus 4.6 feels different inside Claude Code than inside someone else's harness; why changing a tool's logic sometimes causes strange regressions. A genuinely general model wouldn't care whether you used `apply_patch` or `str_replace`, but **cotraining creates overfitting**. The practical implications: (a) **a harness is a living system, not a config file you set up once**; (b) the "best" harness isn't necessarily the one the model was trained inside — *it's the one designed for your task*. *Viv's Top 30 → Top 5 Terminal Bench jump is the clearest proof point.*
- **Harness as a service (HaaS) — Viv's framing.** We're moving from building on **LLM APIs** (which give you a completion) to building on **harness APIs** (which give you a runtime). The Claude Agent SDK, the Codex SDK, the OpenAI Agents SDK all point the same way. You get the loop, the tools, the context management, the hooks, and the sandbox primitives out of the box, and you customise them. The default path used to be: build your own loop, wire up your own tool-calling, handle your own conversation state, invent your own approval flow. **Now the default path is: pick a harness framework, configure it along the four pillars (system prompt, tools, context, subagents), and put the rest of your effort into domain-specific prompt and tool design.** *That's what makes "skill issue" tractable — you're not rebuilding an agent from scratch every time something goes wrong; you're tuning a configuration surface that's already well-factored.*
- **The convergence observation.** *Look at the top coding agents side by side (Claude Code, Cursor, Codex, Aider, Cline) and they look more like each other than their underlying models do.* The models are different. **The harness patterns are converging.** Not an accident — the industry is slowly finding the load-bearing pieces of scaffolding that turn a generative model into something that can ship.
- **Viv's open problems** (Osmani's most-exciting frame): orchestrating many agents working in parallel on a shared codebase; agents that analyse their own traces to identify and fix harness-level failure modes; harnesses that **dynamically assemble the right tools and context just-in-time for a given task** instead of being preconfigured at startup. *"That last one, in particular, feels like where harnesses stop being static config and start becoming something closer to a compiler."*

## What was actually ingested

The full 20-page PDF print of the O'Reilly Radar article (the body is around 17 reading-minutes / ~6,000 words plus two named diagrams: the Agent-Model-Harness "circuit board" and the bridges-over-canyons "harness primitives" illustration). No appendix or external attachments. The article is a reposted-with-permission version of Osmani's blog essay; the O'Reilly version is the canonical citation per his blog header.

## Why this lands in the wiki right now

The wiki's harness-engineering cluster reached ~20+ sources by mid-May 2026 (per [[concepts/agent-harness]]). The cluster has had:

- **Originating practitioner anchor** ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 4-layer anatomy]]);
- **Sceptical-provocative second** ([[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 7 components]]);
- **Vendor-side production case study** ([[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex]]);
- **Vendor-side architecture write-ups** ([[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]], [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]]);
- **Empirical anchor with ablation data** ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]]);
- **Paradigm anchor** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy at Sequoia]]);
- **Hooks-as-portable-primitive operationalisation** ([[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic / TDS]]);
- **User-side framing** ([[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Bockeler / Thoughtworks]]).

Osmani's piece is the **first practitioner field guide that names all of the above as a single emerging discipline** and threads them into an operational rule-set. He cites: Viv ("Anatomy of an Agent Harness" — Chatterjee in our naming), Dex Horthy + HumanLayer, Anthropic's engineering team, Birgitta Bockeler, Simon Willison, Fareed Khan (Claude Code architecture diagram). The piece functions as **the wiki's first explicit cross-author synthesis post** in the harness-engineering cluster — closer in genre to a literature review than a primary contribution. That makes it load-bearing for [[concepts/agent-harness]]'s narrative arc.

## Named entities (this ingest)

**Authors and practitioners cited:**

- [[Addy Osmani]] — Google engineering leader; *Learning JavaScript Design Patterns* author; longtime Chrome DevRel; runs addyosmani.com. **First mention in the wiki.** *Dangling pending second source.*
- **Viv Trivedy** — Originator of *harness engineering* per Osmani. Already in the wiki as the *Anatomy of an Agent Harness* author surface ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] — note: the wiki currently filed the piece under "Chatterjee" as the named author; Osmani names "Viv" / "Viv Trivedy" as the author. This is a **naming-mismatch flag** worth reconciling on the [[2026-05-07-chatterjee-anatomy-of-agent-harness]] page — the piece may actually be Trivedy's; we should re-check the byline before adjusting). For now, treating "Viv (Trivedy)" and "Chatterjee" as candidate aliases for the same author until verified.
- **Dex Horthy** — Co-founder/CTO at **HumanLayer**. Quoted on *"It's not a model problem. It's a configuration problem"* and *"Success is silent; failures are verbose."* **First mention in the wiki.** *Dangling.*
- **HumanLayer** — Company building agent-control infrastructure. **First mention in the wiki.** *Dangling.*
- [[Anthropic]] — Already in the wiki. Osmani credits *"Anthropic's engineering team published what I think is the best public breakdown of how to design a harness for long-running work"* — this is the [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents]] post.
- **Birgitta Bockeler** — Already in the wiki via [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy]].
- **Simon Willison** — Names the loop-essence definition (*"runs tools in a loop to achieve a goal"*). **First mention in the wiki.** *Dangling.*
- **Fareed Khan** — Author of an "estimated" Claude Code architecture diagram Osmani names as *"the clearest public picture I've seen of a mature harness."* **First mention.** *Dangling.*

**Tools / products cited:**

- [[Claude Code]] (already in wiki ecosystem), Cursor, Codex, Aider, Cline — the named convergent coding-agent harnesses.
- Claude Agent SDK, Codex SDK, OpenAI Agents SDK — the named HaaS substrates.
- Terminal Bench 2.0 — coding-agent benchmark; first wiki mention.
- AGENTS.md — flat-markdown rulebook standard. Already wiki-canonical via Lopopolo/Bratanic.
- Context7 — MCP server for current-docs bridging. First wiki mention.

## Cross-positioning with the wiki

- **With [[concepts/agent-harness]]** — Osmani is the practitioner field-guide entry in the cluster; his rule-set (ratchet / earn-each-line / hooks-as-enforcement / harnesses-don't-shrink-they-move / HaaS shift) belongs on the concept page as the **discipline** layer above the architectural taxonomy.
- **With [[concepts/agentic-engineering]]** — Osmani's "harness engineering" terminology is a near-synonym for agentic engineering at the working-engineer altitude; both name *the discipline that wields the harness*. The wiki should keep them distinct (agentic-engineering = the paradigm-level term from Karpathy; harness-engineering = the practitioner-level term from Trivedy and Osmani) but link them tightly. The convergence-observation about top coding agents looking more like each other than their underlying models do is a strong claim that belongs on both pages.
- **With [[concepts/ai-agents]]** — strengthens the wiki's *agents = model + harness* framing as the dominant 2026 vocabulary.
- **With [[2026-05-07-anthropic-economic-index-5-learning-curves|Anthropic Economic Index 5]]** — Osmani's note that **coding-agent harnesses are now an emergent automation cluster on the API** has direct empirical backing in that index report.

## Source-quality notes

- **Genre**: practitioner essay, originally posted on Osmani's personal blog and reposted by O'Reilly Radar with permission. **High-credibility within practitioner literature** — Osmani's track record (Chrome DevRel, *Learning JavaScript Design Patterns*) gives the piece weight as a synthesis read.
- **Not peer-reviewed; not empirical.** The Terminal Bench data point and the Opus 4.6 anxiety-mitigation observation are second-hand from Viv and from Anthropic respectively; Osmani doesn't run his own benchmarks here.
- **Confidence: 0.78.** Per Lifecycle heuristic: single source, +0.05 for repost-by-recognised-publisher (O'Reilly Radar editorial bar), capped at 0.80 because the empirical anchors are second-hand. The concept-page updates this triggers inherit higher confidence via the multi-source cluster they belong to.

## Open question carried forward

Is "Viv (Trivedy)" the author of the *Anatomy of an Agent Harness* piece the wiki currently files under "Chatterjee"? Osmani's repeated naming of "Viv" as the harness-engineering originator is hard to square with the Chatterjee byline. Worth a check before the next ingest in this cluster.
