---
type: source
kind: video
title: "How to Build an Internal AI Agent That Evolves Itself"
author: ["YC Root Access"]
publisher: "Y Combinator (YC Root Access YouTube channel — recent-batch talk series)"
url: "https://www.youtube.com/watch?v=DGD9b8K42lk"
date_published: 2026-05-19
date_ingested: 2026-05-21
length: "~05:34 minutes (transcript ~1,025 words; no YouTube chapters)"
raw: "../../raw/videos/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md"
tags: [agent-harness, agentic-engineering, internal-ai-agents, self-extending-agents, claude-code, yc-batch-talks, founder-vantage, three-memory-types, instructions-md, ai-native-startup-structure, garg, answer-this]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/balancing-digital-portfolios
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "Garg's stated recipe — 'wrap Claude Code CLI in Python … you need a thin harness' — is the founder-vantage operationalisation of the harness-is-all-you-need thesis; both make harness software the load-bearing layer and treat Claude Code as the substrate"
    confidence: 0.85
  - type: supports
    target: 2026-05-13-jha-emergent-democratizing-app-building-with-claude
    via: "twin founder-vantage on Claude Code as substrate landed within a week; Jha builds *external* low-code apps for end-users with Claude, Garg builds *internal* ops automation for his own 2-FTE company with Claude — same substrate, opposite product surface, same harness-engineering discipline"
    confidence: 0.80
  - type: supports
    target: 2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer
    via: "Garg is operationally Forsgren/Macvean's Pattern 3 ('designing environments, setting the guardrails') at startup scale; the self-extending tool authoring matches the Google Search-org PM platform story (intent translated into working features through a platform that encodes deep core-SWE expertise); both prescribe agent-editable instruction files as the team's behavioural-memory artifact"
    confidence: 0.80
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "Fung's flat-org / pods / every-manager-an-IC architecture taken to its structural limit: a 2-FTE company where the org chart is a Slack channel plus a self-extending agent; both treat the agent as a team-mate that gets feedback in natural language and ratchets on those mistakes"
    confidence: 0.75
  - type: supports
    target: 2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack
    via: "Garg's talk is the YC-portfolio-founder downstream of Tan's YC-president *Claude-Code-as-skills* framing: where Tan ships GStack (the partner-mediated YC primitives packaged as skills), Garg ships the founder-side equivalent (Stripe, Intercom, Fathom CLIs + a coding sub-agent that authors new ones on demand) — same packaging philosophy, different domain primitives"
    confidence: 0.75
  - type: supports
    target: 2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up
    via: "Garg's '$2M ARR with 2 FTEs' is the worked-example anchor for Hu's *token-maxing-not-headcount-maxing* + *closed-loop company* thesis; the AnswerThis ops-agent setup is the operational embodiment of Hu's *AI-as-operating-system* framing applied to back-office workflows rather than the product"
    confidence: 0.75
  - type: supports
    target: 2026-04-25-masad-replit-ceo-only-two-jobs-left
    via: "Garg's 2-FTE setup is the smallest-scale data point for Masad's *builders-plus-salespeople* company-of-the-future thesis; the agent is the variable-headcount layer Masad describes; Ryan teaching the agent via Slack feedback is the *vibe-coding-resident team* function compressed into one non-technical co-founder"
    confidence: 0.70
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "the instructions.md / 'editable personality' pattern is Osmani's *ratchet-don't-brainstorm AGENTS.md* rule realised in production: every line in Garg's instructions.md is traceable back to a specific support-mistake class Ryan flagged in Slack and the agent then internalised"
    confidence: 0.75
  - type: supports
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "Garg's *three-memory-types* framework (factual = codebase+DB, behavioural = instructions.md, procedural = self-authored tools) is the founder-vantage articulation of unified agentic memory; Bratanic provides the harness-layer primitive (hooks across memory subsystems), Garg provides the founder-scale exemplar that names the three subsystems explicitly"
    confidence: 0.75
confidence: 0.75
last_confirmed: "2026-05-21"
accessed_at: "2026-05-21"
---

# Garg — How to Build an Internal AI Agent That Evolves Itself

> AnswerThis builds AI agents for evidence-based scientific workflows and has scaled past $2 million in ARR with just two full-time employees — largely because they built an internal AI ops agent that processes over 100 emails a day, closes support tickets, and updates their CRM automatically. In this recent batch talk, founder Ayush Garg breaks down the architecture of a self-extending agent that builds its own tools when it encounters tasks it can't handle yet, how his non-technical co-founder trains the agent by giving it feedback in Slack, and the three types of memory — factual, behavioral, and procedural — that any founder can copy to build an internal agent for their own business.
>
> *— [YC Root Access YouTube channel](https://www.youtube.com/watch?v=DGD9b8K42lk)*

A **~5:34-minute YC batch talk** (YC Root Access channel, published 19 May 2026) by **Ayush Garg**, founder of [AnswerThis](https://answerthis.io). Garg is one speaker in a **multi-talk YC session on agent-harness engineering** — the talk explicitly references prior speakers (*"as Pete and Tom and Gary mentioned"*, *"Pete, Gary, and Tom have already mentioned why you need a thin harness"*), placing this inside a session whose other slots almost certainly feature **Pete Koomen** (YC partner), **Tom Blomfield** (YC managing director), and **Garry Tan** (YC president — already a wiki source with [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|GStack]]).

The talk is the wiki's **first founder-side single-team operational case study** at micro-scale: $2M ARR with 2 FTEs (+ 2–3 contractors for design/outbound), where the internal AI ops agent absorbs the work that would otherwise consume founder time. It is structurally the **portfolio-founder downstream** of the [[Y Combinator]] entity's existing three-source anchor triple (Tan / Hu / Masad, 23–25 April 2026): if Tan supplied the YC-president framing, Hu the YC-partner prescription, and Masad the portfolio-founder worked example at platform scale, **Garg supplies the portfolio-founder worked example at startup scale**.

## TL;DR

- **The headline metric**: $2M ARR with 2 FTEs (+ 2–3 contractors). The internal AI ops agent processes 100+ emails/day, has closed 400+ customer support tickets, runs CRM updates after meetings, and collects user feedback across channels. The business becomes **instantly queryable** in Slack (*"what's the status of a lead?"*, *"what are the open issues for customer X?"*) rather than requiring tab-switching across SaaS tools.
- **The architecture** (Garg's stated recipe, in order):
  1. **Claude Code CLI wrapped in Python** as the main agent harness; new messages from Slack / email / other channels go into a task queue; the agent picks tasks up and works them iteratively.
  2. **Read-only snapshot of the database + codebase**, cron-refreshed on each release, as the agent's factual grounding for business logic (subscription rules, app layout, where things live).
  3. **SaaS-tool CLIs** for everything the startup operationally depends on — Intercom, Fathom, Stripe, etc.
  4. **A general coding agent also exposed as a CLI**, with edit-access to the main agent's own code. *"Whenever we ask it to do a task it cannot do yet, it is simply able to just code that tool into existence and handle the task."*
  5. **An `instructions.md` file**, loaded on every agent turn, **agent-editable**. Feedback from humans (often via Slack) gets internalised by the agent rewriting this file.
- **The self-extending claim — the talk's load-bearing point**: started as a skeleton, *"has gone from just being a skeleton to being this full-blown tool with over 45 CLIs that it has made itself."* Self-authored a cron job to monitor landing-page uptime when asked. Tools become permanent and available in future sessions.
- **The three-memory framework** — Garg's named ontology:
  - **Factual memory** = codebase + database (operational truth, how things work)
  - **Behavioural memory** = `instructions.md` (what you teach the agent — feedback, conventions, mistake corrections)
  - **Procedural memory** = the tools the agent creates itself (regular tasks codified into executable primitives)
- **The Ryan-feedback story** — the non-technical co-founder loop: when the agent was rolled out for customer support and Garg's non-technical co-founder Ryan noticed a class of support mistakes, he didn't open the codebase or file a ticket — *"he just messaged the agent in Slack and told it what was wrong. The agent updated its own instruction set and tool link and then that entire class of mistakes stopped happening again."*
- **The copy-this-architecture closing**: *"if you want to copy this entire agent, just take a picture of this and give it to your cloud code"* — the talk is explicitly designed to be a recipe other YC founders can clone.

## What was actually ingested

Full ~5:34 transcript (~1,025 words after VTT roll-up dedup and ASR cleanup). No YouTube chapters. The talk is content-dense — every segment names a specific architectural choice or operational practice. The on-stage slide showing the recipe ("just take a picture of this") was not captured as an image at ingest time; the recipe content is preserved in prose.

Acquired via `yt-dlp` fallback because the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md)'s Playwright path hit the panel-render failure documented in [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2). VTT rolling-overlap was deduplicated; segments regrouped into ~3–4-sentence paragraphs with timestamp anchors at each paragraph boundary.

## Why this matters

The wiki's harness cluster has accumulated three vantages on what agent-harness engineering *looks like as work*:

1. **The paradigm vantage** — [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy at Sequoia AI Ascent]] naming the discipline.
2. **The inside-the-lab engineering vantage** — [[2026-05-08-running-an-ai-native-engineering-org|Fung at Anthropic / Code with Claude]] and [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren/Macvean at Google I/O]] — the engineering-leadership view inside major AI labs.
3. **The vendor-of-platform vantage** — Tan ([[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|GStack]]), Anthropic's [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents]], Google's [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI]] — vendors productizing the harness layer.

What was *missing* was a **single-team founder-vantage operational case study** at micro-scale: a small team running a real business with a real harness, talking openly about exactly how it's wired. The May customer-story batch (Lyft / HubSpot / Figma Make / Emergent) sits adjacent — those are mid-size or larger team testimonials. Garg adds the 2-FTE end of the scale: same harness primitives, drastically smaller team, internal-ops-focused rather than product-focused.

The talk's **three-memory framework** is also the wiki's first founder-vantage articulation of memory ontology — the [[inspiration/Agent Memory Systems and Decision Tree|inspiration doc]] on agent memory previously held this content unpromoted; Garg's framing gives it a concrete operational anchor.

## The architecture, in five components

Garg presents the architecture as five things any founder can copy. The wiki tracks each as a primitive of the harness layer.

### 1. Claude Code CLI wrapped in Python

> *"The first thing you should do is have a Claude Code CLI wrapped in Python, where new messages from Slack, email, and other channels go into a task queue. The agent picks up these tasks and then works through them iteratively."*

The wrapping decision is load-bearing for the same reason [[2026-05-15-osmani-agent-harness-engineering|Osmani's harness-engineering essay]] gives: top coding agents already know how to inspect files, run commands, and use CLIs — *"Cloud Code works exceptionally well because it already knows how to inspect files, run commands, and use CLIs."* The harness inherits all of that for free.

This is the **founder-vantage instance of the [[concepts/agent-harness|agent-harness]] thesis** — the harness is the substrate-agnostic application layer; the model underneath is rented and swappable.

### 2. Read-only DB + codebase snapshot as factual ground truth

> *"A great way that we've found to be able to do this is by giving the agent a read-only copy of both our database as well as our code base, where it has a cron job that basically gives it an updated version every time we do a release. And whenever a customer support query comes now and they ask some question about the business, the agent can just read our code base to be able to figure that out, including things like what our subscription logic is and where things inside of our app are located."*

The codebase becomes **business documentation by reference**. Subscription rules, app layout, edge-case logic — all are queryable by the agent without separate documentation maintenance. This is the operational counterpoint to the documentation-as-living-artifact pattern other harness sources discuss: in Garg's setup, *the code is the documentation*, and the agent re-reads it after every release.

This relates closely to the [[concepts/agentic-engineering|agentic engineering]] *spec-as-source-of-truth* claim from [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren/Macvean]] — but inverted. Forsgren/Macvean see the *spec* as the source of truth that gets propagated to agents; Garg sees the *code itself* as the source of truth that the agent re-reads. Both work; the choice reflects what is most stable in each org.

### 3. SaaS-tool CLIs as the tool layer

Intercom, Fathom, Stripe — each major SaaS surface is exposed to the agent as a CLI. The agent doesn't call APIs directly; it calls CLI wrappers. This is the pattern [[2026-05-15-osmani-agent-harness-engineering|Osmani]] names *"every line in a good AGENTS.md should be traceable back to a specific thing that went wrong"* applied at the tool-integration layer: each CLI is a stable, named, version-controlled primitive the agent's instruction file can refer to.

### 4. A coding agent as CLI, with edit access to the main agent — the self-extending mechanism

> *"At the same time, it has a general coding agent also as a CLI, which can edit the agent code itself. And what this means is that whenever we ask it to do a task it cannot do yet, it is simply able to just code that tool into existence and handle the task. To us it's magical because we only ask it to do things, but it's able to self-author tools and has gone from just being a skeleton to being this full-blown tool with over 45 CLIs that it has made itself."*

This is the talk's most distinctive architectural claim. The agent's tool set is not fixed — it grows as the agent encounters new work. The closing-the-loop example: *"when we just wanted to monitor our landing pages to make sure they're always up for ads, and we just sort of told it and it created a cron job into existence that does this."*

The wiki frames this as **procedural-memory accretion** — regular tasks get encoded into reusable executable primitives, which the agent can then re-invoke without rebuilding. This is what makes the harness *compound* over time rather than plateauing.

This is the founder-vantage instance of what [[2026-05-04-rethinking-agents-harness-is-all-you-need|Pan/Khattab]] called the *transfer-across-models* property — the value lives in the harness's accreted tool/skill library, not in the underlying model.

### 5. `instructions.md` — the editable personality

> *"There's one very important thing that also this agent needs to have, which is an editable personality or memory. We do this by an `instructions.md` file that is loaded on every agent turn, and the agent is able to edit this. This is how we are able to self-evolve the agent because we can give it feedback like we would give feedback to an employee and it just updates this `instruction.md` file which then gets appended to the next run."*

The pattern: agent-loaded-on-every-turn instruction file, but **the agent can edit it in response to feedback**. This is the founder-scale realisation of [[2026-05-15-osmani-agent-harness-engineering|Osmani's *ratchet-don't-brainstorm AGENTS.md* rule]] — but with the agent itself doing the ratcheting in response to natural-language feedback rather than the engineer doing it manually after each incident.

The customer-support story is the clearest instance:

> *"When we had just rolled out this agent to start doing customer support, my co-founder Ryan, who's non-technical, noticed a class of support mistakes. Instead of opening the code base or telling me or filing a ticket, he just messaged the agent in Slack and told it what was wrong. The agent updated its own instruction set and tool link and then that entire class of mistakes stopped happening again."*

This is the **non-technical-co-founder feedback loop** — the *vibe-coding-resident-team* pattern from [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad]] compressed into a single Slack channel. The wiki tracks this as evidence for the broader claim that, in an AI-native organisation, **natural-language feedback in chat replaces ticket-filing and codebase-editing as the dominant change mechanism for many classes of error**.

## The three-memory framework

Garg's most quotable framing — the talk's broader lesson:

> *"An internal agent needs sort of three sorts of memories. It needs factual memories, which is your code base and your database, things how they work operationally within your startup. It needs behavioural memories. This is what you teach the agent. It's things like instruction and feedback. That is what we have the `instructions.md` file for. And it needs procedural memory, regular tasks that you're doing. This is what we encode into the tools that the agent is able to create itself."*

| Memory type | What it is | Where it lives in Garg's setup | What it maps to in the wiki |
|---|---|---|---|
| **Factual** | Operational truth about how the startup works | Read-only codebase + database snapshot (cron-refreshed each release) | The harness's *context layer*; analogous to retrieval-augmented grounding |
| **Behavioural** | What you teach the agent — corrections, conventions, taste | `instructions.md`, agent-editable, loaded every turn | The harness's *constraints/contracts layer*; the AGENTS.md / skill-file pattern in [[2026-05-15-osmani-agent-harness-engineering|Osmani]] and [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]] |
| **Procedural** | Regular tasks codified as reusable, executable primitives | The 45+ self-authored CLIs the agent has built itself | The harness's *compounding layer*; the tool/skill library that accretes over time |

The mapping onto the wiki's existing [[concepts/agent-harness|four-layer harness anatomy]] (Context / Constraints / Contracts / Compounding from [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]) is clean:

- Factual ⟷ Context
- Behavioural ⟷ Constraints + Contracts (the rule layer)
- Procedural ⟷ Compounding (the tool/skill accretion layer)

What Garg adds that the wiki didn't previously articulate at founder scale is the **agency** dimension: the agent itself is the active manager of all three memory subsystems. It re-reads the codebase, rewrites the instructions, and authors new procedural tools. Humans set direction; the agent maintains its own memory.

## Cross-source positioning

| Source | Construct | What this Garg talk adds |
|---|---|---|
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Pan/Khattab 2026]] | Harness >> model for compound performance | The founder-vantage *"wrap Claude Code CLI in Python … thin harness"* operationalisation at micro-scale: the harness is doing the work, the model is interchangeable substrate. |
| [[2026-05-13-jha-emergent-democratizing-app-building-with-claude\|Jha 2026]] | Founder-on-Claude — building apps for end users | Founder-on-Claude — building **internal ops** for *yourself*. Twin founder-vantages on Claude as substrate landed within a week, different product surfaces. |
| [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer\|Forsgren/Macvean 2026]] | Designing environments not vibe-coding; spec as source of truth | Pattern 3 at startup scale; spec/instructions-as-behavioural-memory; agent-editable rather than human-curated. |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026]] | Flat org / pods / Claudify everything | Flat-org *limit case*: 2-FTE company where the agent is the headcount-stretching layer. |
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan 2026]] | Skills wrap Claude Code with YC primitives | Founder-side equivalent: SaaS-tool CLIs + self-authored CLIs wrap Claude Code with AnswerThis primitives. Same packaging philosophy, different domain primitives. |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu 2026]] | Token-maxing not headcount-maxing; closed-loop company | Worked-example anchor: $2M ARR / 2 FTE is the operational embodiment. |
| [[2026-04-25-masad-replit-ceo-only-two-jobs-left\|Masad 2026]] | Builders + salespeople; vibe-coding-resident team | Smallest-scale data point: vibe-coding-resident team compressed into one non-technical co-founder feeding Slack. |
| [[2026-05-15-osmani-agent-harness-engineering\|Osmani 2026]] | Ratchet-don't-brainstorm AGENTS.md | `instructions.md` as the ratcheted artifact; **the agent itself does the ratcheting** in response to natural-language Slack feedback. |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026]] | Unified agentic memory via hooks | The three-memory framework (factual / behavioural / procedural) is the founder-vantage articulation of what Bratanic provides as a harness-layer primitive. |

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[concepts/agent-harness|agent-harness]] — heavy: this is the founder-vantage micro-scale instance; the five-component architecture maps onto the four-layer harness anatomy.
- [[concepts/agentic-engineering|agentic-engineering]] — heavy: Garg is doing agentic engineering, with the harness as the operational artifact and `instructions.md` as the spec.
- [[concepts/agent-development-lifecycle|agent-development-lifecycle]] — moderate: agent-editable `instructions.md` + procedural-memory accretion are ADL primitives at founder scale.
- [[concepts/ai-agents|ai-agents]] — moderate: the self-extending tool-authoring claim is a sharper instance of the agency dimension than most ai-agents sources carry.
- [[Y Combinator]] — heavy: bumps `source_count` from 3 → 4; extends the existing YC-batch-context anchor triple (Tan / Hu / Masad, 23–25 April) to a four-source anchor adding the May portfolio-founder vantage at startup scale.
- [[Anthropic]] — moderate: Claude Code is named as the substrate; bumps `source_count`.

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):**

- *Ayush Garg* — speaker (founder, AnswerThis). Promote on second-source mention.
- *AnswerThis* — organisation (AI agents for evidence-based scientific workflows; $2M ARR, 2 FTE as of May 2026). Promote on second-source mention.
- *Ryan* — non-technical co-founder (surname not stated in the talk). Promote on second-source mention.
- *Pete Koomen, Tom Blomfield* — likely co-speakers in the same YC Root Access session (Garg references *"Pete and Tom and Gary"*); promote if/when their slots in the same session are ingested.
- *YC Root Access* — channel / series (the YC YouTube series these recent-batch talks live in). Sub-entity of [[Y Combinator]]; defer separate page until it accumulates source weight.

## Source-quality flag

- **Strengths**: rare founder-vantage operational case study at micro-scale (2-FTE company, $2M ARR); content-density extremely high for a 5-minute talk (every segment names a specific architectural choice or operational metric); the *three-memory framework* is a clean, transferable ontology; the *self-extending agent* claim is operationally specific (45+ CLIs, named example: landing-page-uptime cron job); the Ryan-feedback story is a clean exemplar of the natural-language-feedback-as-change-mechanism pattern.
- **Caveats**: founder-of-self testimonial — the speaker is selling the architecture as a recipe (talk closes with *"if you want to copy this entire agent, just take a picture of this and give it to your cloud code"*); no third-party verification of the $2M ARR or 100+ emails/day / 400+ tickets metrics; no detail on failure modes, eval coverage, or the cost of the self-extending behaviour going wrong (e.g. what happens when the coding sub-agent authors a bad tool? observability story is not given). The talk is also short — 5 minutes is enough to name the architecture but not enough to stress-test it.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.70 (single supporting source) + 0.05 for cross-source resonance with multiple already-ingested 2026 sources at multiple layers of the harness cluster (Pan/Khattab harness thesis; Forsgren/Macvean designing-environments pattern; Fung inside-engineering twin; Osmani ratcheted-AGENTS.md; Bratanic unified-memory; Tan/Hu/Masad YC anchor triple). Held at **0.75** (not raised further because it's a single founder testimonial without independent verification of the metrics, and because the self-extending mechanism is named but not stress-tested in the talk). **Confidence: 0.75.**

## Open questions for the wiki

- **The other three YC Root Access talks.** Garg references *"Pete and Tom and Gary"* who already covered the *thin harness* point. If those three slots are ingestible (likely Pete Koomen, Tom Blomfield, Garry Tan), they would form a four-source YC Root Access agent-harness session — a candidate for its own [[wiki/threads|thread]] page tracking the multi-talk session as a coherent argument.
- **The 45+ self-authored CLIs.** The talk names this as the *"skeleton-to-full-blown"* outcome but doesn't show what those CLIs look like or how their quality is policed. A follow-up post, blog, or open-source release from AnswerThis would let the wiki promote *self-extending agents* to a standalone concept.
- **Failure-mode story.** What happens when the coding sub-agent authors a bad tool? When the agent edits `instructions.md` in a way that introduces a regression? The talk doesn't say. The [[concepts/agent-development-lifecycle|agent-development-lifecycle]] page would benefit from a documented failure case at this scale.
- **AnswerThis as an entity.** AnswerThis is interesting enough (scientific workflows, 2-FTE, $2M ARR, evidence-based) that a second-source mention would be valuable and warrant a full entity page. Worth watching.
- **The three-memory framework as a standalone concept.** Garg's *factual / behavioural / procedural* trichotomy is clean enough to anchor a concept page if a second source articulates it. Currently sits in the [[inspiration/Agent Memory Systems and Decision Tree|inspiration doc]] without a wiki home; a second framing would justify promotion.
