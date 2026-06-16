---
type: source
kind: article
title: "Harness engineering: leveraging Codex in an agent-first world"
author: ["Ryan Lopopolo"]
publisher: "OpenAI — Engineering blog"
url: "https://openai.com/index/harness-engineering/"
date_published: 2026-02-11
date_ingested: 2026-05-10
length: "~12-page article (~5,500 words; 18:04 audio version)"
raw: "../../raw/articles/Harness engineering_ leveraging Codex in an agent-first world _ OpenAI.pdf"
tags: [openai, codex, agent-harness, agentic-engineering, agents-md, progressive-disclosure, observability, doc-gardening, repository-as-system-of-record, agent-legibility, layered-architecture, ralph-wiggum-loop]
---

# Harness engineering: leveraging Codex in an agent-first world

A first-person engineering post from OpenAI documenting **five months of building and shipping a real internal product with zero manually-written code** — every line (application, tests, CI, documentation, observability, internal tooling) authored by [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Codex]]. The team's headline framing — *"Humans steer. Agents execute."* — and their hard constraint (no manually-written code) are deliberate constraints designed to force the team to "build what was necessary to increase engineering velocity by orders of magnitude."

This is the wiki's **first vendor-side production case study** of the [[agent-harness|harness pattern]] applied to its own engineering workflow at meaningful scale. Where [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] argue *what the harness is*, and [[2026-05-04-rethinking-agents-harness-is-all-you-need|the YouTube source]] supplies the *empirical anchor* for harness importance, **Lopopolo supplies the worked example**: how the harness layer evolves over five months when an engineering team is forced to live inside it.

## TL;DR

- **Five months, ~1 million LOC, ~1,500 PRs, 7 engineers, 3.5 PRs / engineer / day** — and throughput *increased* as the team grew. Built with **0 lines of manually-written code**. The product has hundreds of internal users, including daily power users.
- **Engineering work shifted from writing code to designing environments.** "Building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code. The tooling, abstractions, and feedback loops that keep the codebase coherent are increasingly important."
- **Repository-as-system-of-record.** "From the agent's point of view, anything it can't access in-context while running effectively doesn't exist." Knowledge in Google Docs, Slack threads, or people's heads is *illegible* to Codex. So the team pushed all context into the repo as versioned markdown — design docs, ADRs, exec plans, quality scores, taste invariants.
- **AGENTS.md as table of contents, not encyclopedia.** Tried "one big AGENTS.md" → failed in four predictable ways (context is scarce; too much guidance becomes non-guidance; rots instantly; hard to verify mechanically). Replaced with **progressive disclosure**: a ~100-line top-level AGENTS.md that maps to deeper sources (DESIGN.md, ARCHITECTURE.md, exec-plans/, generated/, references/), each with verification status, ownership, freshness checks, and a "doc-gardening" agent that scans for stale docs and opens fix-up PRs.
- **Layered architecture, mechanically enforced.** Each business domain is divided into a fixed set of layers (Types → Config → Repo → Service → Runtime → UI), with strictly validated dependency directions and a single Providers interface for cross-cutting concerns. Custom linters (Codex-generated, of course) enforce the boundaries. *"This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it's an early prerequisite: the constraints are what allows speed without decay or architectural drift."*
- **Throughput changes the merge philosophy.** Minimal blocking merge gates; PRs are short-lived; test flakes are addressed with follow-up runs rather than blocking progress. *"In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive."*
- **"Golden principles" + scheduled GC.** Encoded opinionated, mechanical rules (prefer shared utilities; never probe data, validate at boundaries with typed SDKs); background Codex tasks scan for deviations and open targeted refactoring PRs, mostly auto-merged. *"Technical debt is like a high-interest loan: it's almost always better to pay it down continuously in small increments than to let it compound."*
- **The hard problem now isn't code, it's environment design.** *"Our most difficult challenges now center on designing environments, feedback loops, and control systems that help agents accomplish our goal: build and maintain complex, reliable software at scale."*

## What was actually ingested

Full ~12-page PDF read end-to-end — the whole article (introduction, "We started with an empty git repository," "Redefining the role of the engineer," "Increasing application legibility," "We made repository knowledge the system of record," "Agent legibility is the goal," "Enforcing architecture and taste," "Throughput changes the merge philosophy," "What 'agent-generated' actually means," "Increasing levels of autonomy," "Entropy and garbage collection," "What we're still learning") plus tags, author card, and acknowledgments. No appendix or supplementary material referenced.

## Key claims in detail

### Repository as system of record

> *"From the agent's point of view, anything it can't access in-context while running effectively doesn't exist. Knowledge that lives in Google Docs, chat threads, or people's heads are not accessible to the system."*

This is the operational principle the rest of the architecture flows from. Knowledge that does not live in repository-local, versioned markdown is *invisible* to Codex; therefore every instruction, design decision, taste invariant, and architectural rule must be encoded in the repo. The post's diagram (*"What Codex can't see doesn't exist"*) shows three boxes — Google doc / Slack message / tacit knowledge — with arrows labelled "Encode into codebase as markdown" pointing into "Codex's knowledge."

This is a sharper restatement of what [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] called the **Context layer** ("the room the agent walks into"): the harness's job is to make the right information present in-context at the moment it's needed. Lopopolo extends this with a procedural rule: *if a Slack thread aligned the team on an architectural pattern, that decision is illegible to the agent until it's encoded in the repo.* The remediation is mechanical (doc-gardening agent that opens fix-up PRs against stale or missing docs).

### AGENTS.md as table of contents — progressive disclosure

The "one big AGENTS.md" approach fails in four named ways:

1. **Context is a scarce resource.** A giant instruction file crowds out the task, the code, and the relevant docs.
2. **Too much guidance becomes non-guidance.** When everything is "important," nothing is. Agents pattern-match locally instead of navigating intentionally.
3. **It rots instantly.** A monolithic manual turns into a graveyard of stale rules. Humans stop maintaining it.
4. **It's hard to verify.** A single blob doesn't lend itself to mechanical checks (coverage, freshness, ownership, cross-links).

The replacement: ~100-line top-level AGENTS.md as a *map* with pointers to deeper sources, organized as a directory:

```
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/      ← verification status + core beliefs
├── exec-plans/       ← active / completed / tech-debt-tracker
├── generated/        ← e.g. db-schema.md
├── product-specs/    ← index.md + new-user-onboarding.md
└── references/       ← design-system-reference-llms.txt, nixpacks-llms.txt, ...
DESIGN.md
FRONTEND.md
PLANS.md
PRODUCT_SENSE.md
QUALITY_SCORE.md
```

Each subdirectory is "the system of record" for a specific concern, with quality grades that track "gaps over time." Active plans, completed plans, and known technical debt are *all versioned and co-located, allowing agents to operate without relying on external context.*

This is operationally the same pattern [[2026-05-04-rethinking-agents-harness-is-all-you-need|the Prompt Engineering YouTube source]] called *"natural-language harness representation"* (Pan et al.'s OS-Symphony migration: 30.4 → 47.2% by rewriting a code-based harness in structured natural language with the same strategy). Lopopolo's AGENTS.md hierarchy *is* the natural-language harness, scaffolded as a directory tree.

### Application legibility — chrome-devtools-mcp + observability stack

The team made the application UI, logs, and metrics *directly legible to Codex*:

- **Chrome DevTools Protocol wired into the agent runtime.** Codex can launch one app instance per git worktree, take DOM snapshots, take screenshots, navigate, and reason about UI behaviour directly. The diagram shows the loop: *select target → snapshot before → trigger UI path → snapshot after → apply fix → re-run validation* until clean.
- **Local observability stack per worktree.** Logs (Vector → VictoriaLogs / LogQL), metrics (VictoriaMetrics / PromQL), traces (TraceQL). Ephemeral per worktree. Codex can write prompts like *"ensure service startup completes in under 800ms"* or *"no span in these four critical user journeys exceeds two seconds"* and they become tractable.
- **Single Codex runs work on a single task for upwards of six hours** (often while humans are sleeping).

This makes operational the *empirical-validation-by-the-agent-itself* loop that [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]'s Constraints layer (post-tool hooks scoring output) gestured at.

### Layered architecture, mechanically enforced (Types → Config → Repo → Service → Runtime → UI)

> *"Agents are most effective in environments with strict boundaries and predictable structure."*

Each business domain is a layered stack with **strictly validated dependency directions** and **a single Providers interface** for cross-cutting concerns (auth, connectors, telemetry, feature flags). Anything else is disallowed and enforced mechanically by custom linters (Codex-generated). Within those boundaries, agents have *significant freedom* in how solutions are expressed.

Three claims this generates:

1. **The architecture is a leverage multiplier in agent-driven engineering, not a tax.** The constraints are what enables speed without decay.
2. **It looks like leading a large engineering platform org.** Enforce boundaries centrally; allow autonomy locally.
3. **The resulting code does not always match human stylistic preferences. That's okay** — as long as output is correct, maintainable, and legible to *future agent runs*.

### "Taste invariants" — promoting human judgment to mechanical rules

> *"Human taste is fed back into the system continuously. Review comments, refactoring pull requests, and user-facing bugs are captured as documentation updates or encoded directly into tooling. When documentation falls short, we promote the rule into code."*

This is the operational mechanism behind [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] **Compounding** layer (telemetry as training data for the harness): *every instance of human taste correction becomes either a doc update or a custom lint rule.* The harness gets sharper with every review.

### Throughput inverts the merge philosophy

> *"In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive. This would be irresponsible in a low-throughput environment. Here, it's often the right tradeoff."*

Operational consequences:

- Minimal blocking merge gates.
- Pull requests are short-lived.
- Test flakes addressed with follow-up runs rather than blocking progress indefinitely.
- *"Most refactoring PRs can be reviewed in under a minute and automerged."*

This contradicts the pre-agent norm where blocking gates were the price of correctness. With agent throughput, blocking gates *cost more than they protect*.

### "Golden principles" and entropy / garbage collection

> *"Codex replicates patterns that already exist in the repository — even uneven or suboptimal ones. Over time, this inevitably leads to drift."*

The team initially spent every Friday (20% of the week) cleaning up "AI slop." That didn't scale. They replaced it with:

- **Encoded golden principles** — opinionated mechanical rules. Two examples: *"prefer shared utility packages over hand-rolled helpers,"* and *"don't probe data 'YOLO-style' — validate at boundaries or rely on typed SDKs so the agent can't accidentally build on guessed shapes."*
- **Background Codex tasks** scan for deviations on a regular cadence, update quality grades, and open targeted refactoring PRs. Most can be reviewed in under a minute and automerged.

> *"Technical debt is like a high-interest loan: it's almost always better to pay it down continuously in small increments than to let it compound and tackle it in painful bursts."*

This is the **Compounding** layer working in reverse — instead of harness *learning* getting better with use, it's harness *self-maintenance* preventing drift. Both are part of the same compounding-vs-consumption distinction [[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage]] make at the organizational level.

### Increasing levels of autonomy — Codex now drives features end-to-end

> *"Given a single prompt, the agent can now: validate the current state of the codebase; reproduce a reported bug; record a video demonstrating the failure; implement a fix; validate the fix by driving the application; record a second video demonstrating the resolution; open a pull request; respond to agent and human feedback; detect and remediate build failures; escalate to a human only when judgment is required; merge the change."*

This is a **Ralph Wiggum Loop** scaled to a real codebase — the agent reviews its own output, requests additional agent reviews, and iterates until reviewers are satisfied. *"Humans may review pull requests, but aren't required to. Over time, we've pushed almost all review effort towards being handled agent-to-agent."*

Caveat from the post: *"This behavior depends heavily on the specific structure and tooling of this repository and should not be assumed to generalize without similar investment — at least, not yet."*

### What's still unknown

The post is honest about three open questions:

1. **How architectural coherence evolves over years in a fully agent-generated system.** Five months is not enough.
2. **Where human judgment adds the most leverage** — and how to encode it so it compounds.
3. **How the system evolves as models continue to improve.** Compatible with [[2026-05-04-rethinking-agents-harness-is-all-you-need|the subtraction principle]] — components encoding "what the model can't do alone" expire when models improve.

## Cross-source resonance

| Source | What this source confirms or extends |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] (Sequoia AI Ascent) | **Agentic engineering** as the named discipline — Karpathy framed the shift; Lopopolo provides the production case study. The "no manually-written code" constraint is [[vibe-coding|vibe coding]] taken to its logical endpoint. |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | **Concrete worked examples** of the four layers: Context (AGENTS.md hierarchy + repository-as-system-of-record), Constraints (custom linters + structural tests + Providers interface), Contracts (quality grades, taste invariants), Compounding (golden principles + background Codex tasks for GC + doc-gardening agent). |
| [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] | Confirms Kokane's "10% novel" kernel (non-determinism + context-as-degrading-resource) and his "if you've shipped real backend systems you're 80% there" thesis — Lopopolo's team is doing classic systems engineering at agent throughput. |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung at Code with Claude 2026]] | Operational analogue at Anthropic: AI-native engineering org, agents-first workflow. Lopopolo's *"the discipline shows up more in the scaffolding rather than the code"* and Fung's framing of *engineering org as harness configuration* are the same claim from two vendors. |
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Prompt Engineering YouTube, May 2026]] | The OS-Symphony NL-migration result (Pan et al.) is what the AGENTS.md / DESIGN.md / exec-plans/ hierarchy *is* — a structured natural-language harness representation. Lopopolo's "doc-gardening agent" is the empirical analogue of Pan et al.'s "self-evolution" — the only ablation module that consistently helped. |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic Managed Agents]] | Same architecture, different vantage. Anthropic externalized the brain/hands/session split as a hosted service; Lopopolo's team built the same layering inside a single repo. |
| [[2026-04-22-cheung-ippolito-secchi-google-agents-cli\|Google Agents CLI]] | The 9-stage [[agent-development-lifecycle|ADLC]] wheel (capability → design → tools → context → evaluate → UAT → deploy → CI/CD) maps cleanly onto Lopopolo's workflow, but Lopopolo's account flattens the wheel: *every* PR cycles through capability → design → tools → context → evaluate → UAT → deploy in minutes, agent-driven, end-to-end. |
| [[2026-05-07-anthropic-economic-index-5-learning-curves\|Anthropic Economic Index 2026]] | The "tasks shifting from execution to direction-setting" pattern observed at population scale; Lopopolo provides one team's instantiation: humans prioritize work, translate user feedback into acceptance criteria, validate outcomes — Codex does everything else. |

## Linked entities and concepts

- **Author (1st mention; Dangling per [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion))**: Ryan Lopopolo (Member of Technical Staff, OpenAI). Acknowledgments name **Victor Zhu** and **Zach Brock** as contributors, and *"the entire team that built this new product."* Promote on second-source mention.
- **Organization**: [[OpenAI]] — already has an entity page. Add this source to its inbound-link set.
- **Products / projects mentioned**: **Codex**, **Codex CLI** (using GPT-5), **Aardvark** (an agent that also operates on the codebase, not detailed here). All product names; not promoted on a single mention.
- **Concepts touched**:
  - [[agent-harness]] — the worked example. Major concept-page extension warranted.
  - [[agentic-engineering]] — the named practitioner discipline. Lopopolo is the wiki's first vendor case study; concept page extension warranted.
  - [[ai-agents]] — Codex as the agent.
  - [[vibe-coding]] — *"no manually-written code"* is the operational endpoint of the term; concept-page minor update.
  - [[software-3.0]] — Karpathy's paradigm; this is what production looks like inside it.

## Notes on confidence and lifecycle

- **Source quality**: vendor first-person engineering essay on the company's owned blog. Authoritative on the team's *own* practice (the team is OpenAI's). Not externally replicated, so claims about generalizability are deliberately hedged in the post itself.
- **Page does not carry `confidence:`** — sources are evidence, not claims.
- **Dating note**: published **11 February 2026**; ingested **10 May 2026** — three months of latency between publication and ingest. Reflects the wiki's reactive ingest discipline rather than a freshness gap.

## What this source does *not* do

- It does **not** quantify the cost (token spend, dollar spend, GPU-hours) of running this team's setup. The economics that make *"corrections are cheap, waiting is expensive"* true are unstated.
- It does **not** describe failure modes or near-misses. Five months in, the team has shipped — but real-world incident reports would be a higher-evidence form of *what breaks* in this paradigm.
- It does **not** describe how the harness was bootstrapped. The post implies the AGENTS.md, DESIGN.md, layered architecture, and golden principles were authored *by Codex* during early development, but the bootstrap dynamics (was the first commit a hand-crafted skeleton? did Codex write its own AGENTS.md from a few seed rules?) are elided.
- It does **not** address evaluation or testing. The Constraints / Contracts / Compounding layers are visible by inference but not the centerpiece of this post — by Lopopolo's framing, *"every line of code, including tests, has been written by Codex,"* but how those tests are validated as *good* tests is not addressed.

These are reasonable elisions for a single essay; flag them as gaps a follow-up source would need to fill.
