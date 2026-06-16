---
type: source
kind: video
title: "Inside YC's AI Playbook"
author: ["Y Combinator"]
publisher: "Y Combinator (Lightcone podcast YouTube channel — Pete Koomen guest with Garry Tan, Diana Hu, Harge Taggar moderating; 27 May 2026)"
url: "https://www.youtube.com/watch?v=B246K_G7mHU"
date_published: 2026-05-27
date_ingested: 2026-05-28
length: "~46:30 minutes (auto-generated English captions via yt-dlp fallback; 555 deduped ASR segments after VTT rolling-window cleanup — the youtube-transcript-skill's engagement-panel route timed out after 180s on this and ≥20-minute talks generally)"
raw: "../../raw/videos/inside-yc-ai-playbook.md"
tags: [pete-koomen, garry-tan, diana-hu, harge-taggar, jared-friedman, yc-lightcone, yc-internal-ai-playbook, multiplayer-harness, shared-tool-registry, skillify-dry-mece, resolver-table, one-database-to-rule-them-all, big-table-for-agents, jevons-paradox, self-improving-dream-cycle, two-sentence-pitch-skill, super-intelligence-compounds-at-org-level, recording-everything-as-building-layer, broadcast-by-default-agent-conversations, egalitarian-trust-by-default, $100K-token-budget-leapfrog, horseless-carriages-essay, just-in-time-software, 1984-vs-homebrew, gbrain, openclaw, hermes, pi-coding-agent, ai-as-building-layer-not-feature]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/organizational-culture
  - strategic-renewal/collaborative-approach
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-19-garg-yc-internal-ai-agent-evolves-itself
    via: "**Paired YC-internal-infrastructure vantages — Garg as 5-minute teaser, Koomen as 46-minute architecture talk.** [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg]] (19 May 2026, ~5:34 minutes): *'wrap Claude Code CLI in Python, you need a thin harness'* + three-memory-types + instructions.md framing — the founder-altitude IC-vantage on what an internal AI agent should look like. This Koomen / Lightcone source is the **substantive architecture-and-organisation talk** on the same YC-internal infrastructure: 350-tool shared registry, multiplayer-harness primitives, skillify / DRY / MECE resolver pattern, broadcast-by-default agent conversations, the self-improving dream cycle, the *one Postgres database with everything* substrate, the two-sentence-pitch skill as worked example. Pete Koomen built the org-wide layer; Garg's framing is what an IC inside that org sees. The wiki's clearest paired *IC-vantage + architecture-vantage* on a single internal-agent-infrastructure project."
    confidence: 0.9
  - type: supports
    target: 2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack
    via: "**Sibling YC-doctrinal anchors on AI-native company infrastructure at IC + org altitudes.** [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan / GStack]] (23 April 2026): Garry Tan's GStack toolkit — Claude Code wrapped with skills for office hours / design / code review / QA / browser testing; the **IC-level** packaged harness-of-skills. This Koomen / Lightcone source extends one month later (27 May 2026) with the **org-level** infrastructure: shared tool registry + shared skill registry + broadcast-by-default agent conversations + the multiplayer-harness gap. Tan is moderating this Koomen video, explicitly linking the two: *'inspired by what you guys did with tools like this idea of skillify in openclaw and then actually the most important the last part of skillify... actually like plugging it into the resolver which is like your agents.mmd with like the list of things that the agents can do.'* The skillify / resolver-table primitive is shared across both YC-vantage sources. **GStack is the IC packaging; the YC-internal infrastructure is the org-scale extension; the multiplayer-harness gap is the unsolved problem at the next level up.**"
    confidence: 0.85
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "**Load-bearing Karpathy citation throughout the Koomen talk.** Two direct references: (1) *'I would argue that that's happening now with Karpathy-style knowledge LLM wikis with Gbrain'* — denormalisation-for-agents as the corpus-shape pattern (BigTable for agents); (2) *'auto research from Karpathy again you know'* — the self-improving dream-cycle pattern. Koomen and Tan use Karpathy's framings as the conceptual substrate for what they built at YC. This Koomen / Lightcone source is the **YC-implementation-altitude operationalisation of Karpathy's vibe-coding-to-agentic-engineering thesis** + auto-research dream-cycle pattern at internal-org scale."
    confidence: 0.85
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "**Multiplayer-harness extension of Osmani's single-player harness-engineering framing.** [[2026-05-15-osmani-agent-harness-engineering|Osmani]] (15 May 2026, O'Reilly Radar): harness-engineering as a discipline — Ralph Loop / AGENTS.md / hooks / sandboxes / compaction — the **individual-developer-altitude** treatment. Koomen / Lightcone explicitly names the next-altitude problem: *'we're still kind of in the single-player era of agents where the harnesses that have gotten really popular — Claude Code, Codex, Pi, OpenClaw, Hermes — they're all designed to be used by a single human running on a single machine. ... one of the big problems that I don't think has been solved well yet by anybody is the multiplayer harness — enabling that kind of superpower but on a team or an organizational level.'* The YC internal infrastructure (shared tool registry, shared skill registry, agent-conversation broadcast, self-improving dream cycle) is Koomen's **proposed primitive set for the multiplayer-harness gap** — explicitly inspired by Osmani-style single-player harness engineering but operating one altitude above it. **The wiki's first explicit single-player → multiplayer harness-engineering progression.**"
    confidence: 0.85
---

# Koomen / YC Lightcone — *Inside YC's AI Playbook* (talk + panel, 2026-05-27)

> How do you build super intelligence inside a company? Part of the key thing is not to just use AI as a copilot. This is the thing where you use it as the building layer for everything. And you need to start recording all the artifacts. It's like a shared organizational brain. It's like the closest thing to us being able to connect our brains. If you frame this as a way for everyone in an organization to get better at what they do using the collective skill and instinct of the people they work with, it's incredibly powerful.
>
> Building superintelligence inside a company isn't about adding AI as a feature. It's about making it the operating system the whole organization runs on. In this episode of the Lightcone, we sat down with YC's Pete Koomen to talk for the first time about how he led the effort to build YC's internal agent infrastructure from the ground up. We cover how giving agents unrestricted access to one database changed everything, the self-improving skill loops that get smarter overnight and why he thinks we've arrived at the personal computer moment for AI.

(YouTube description, [[Y Combinator]] channel — Lightcone podcast format.)

A ~46:30 talk + panel on the [[Y Combinator]] *Lightcone* podcast, published 27 May 2026. Auto-generated English captions via yt-dlp fallback; the [[youtube-transcript-skill]] engagement-panel route timed out at 180s (recurring failure mode on ≥20-minute talks). VTT rolling-window dedup applied; 555 segments.

**Speakers:**
- **Pete Koomen** — YC General Partner; co-founder of Optimizely (A/B testing platform); author of the *Horseless Carriages* essay critiquing AI-as-feature software. **The architect of YC's internal AI infrastructure.** *First-mention in the wiki; deferred under [[CLAUDE|§Lifecycle author-entity promotion]] (single-source rule).*
- **[[Garry Tan]]** — YC President and CEO; hosts. Already a substantive entity in the wiki via [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|GStack talk]] and the [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Stanford CS153 talk with Diana Hu]].
- **[[Diana Hu]]** — YC partner; co-host. Already substantive.
- **Harge Taggar** — YC partner; co-host. *First-mention; deferred.*
- **Jared Friedman** — YC partner; mentioned by Koomen as the engineer who built the first SQL-against-production-database tools. *First-mention; deferred.*

This source is the wiki's **substantive architecture-and-organisation talk on YC's internal AI infrastructure** — the same project [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg's 5-minute talk]] introduced at the IC altitude, now described at the org-architecture altitude by the partner who built it.

## TL;DR

Seven substantive contributions:

**1. The multiplayer-harness gap and its primitive set** — the single most-load-bearing contribution. Koomen's framing: *"we're still kind of in the single-player era of agents where the harnesses that have gotten really popular — Claude Code, Codex, Pi, OpenClaw, Hermes — they're all designed to be used by a single human running on a single machine. ... one of the big problems that I don't think has been solved well yet by anybody is the multiplayer harness — enabling that kind of superpower but on a team or an organizational level."* YC's proposed primitive set for the multiplayer-harness gap:

| Primitive | What it is | Why it matters |
|---|---|---|
| **One database to rule them all** | Single Postgres with companies / founders / financial transactions / CRM notes — *"a database with every important piece of context"* | Agent answers arbitrary cross-domain business questions; *"BigTable for agents"* — denormalisation-for-retrieval pattern. |
| **Shared tool registry (350 tools)** | Started at ~20 tools (SQL access, model-file read); grew to 350; every team adds tools for its own workflows | The same tools are available to **internal agents** AND to **individual Claude Code instances** running on partner laptops. |
| **Shared skill registry with resolver pattern** | Skills as markdown files; agents reference via *"resolvers"* (≈ `AGENTS.md`); meta-skill **skillify** auto-promotes new behaviours into reusable skills | *"Cloud Code has a skill, the skill registry in cloud code is actually a resolver. Our tool registry is actually a resolver."* — convergent primitive across harnesses. |
| **Broadcast-by-default agent conversations** | Every agent conversation broadcast to an internal Slack channel; any full-time employee can read | *"People learned how to use it from watching how other people used it"* + functions as a social-control layer on what people do with high-context agents inside high-trust orgs. |
| **The self-improving dream cycle** | Overnight, an agent reads all agent conversations from the day, identifies inefficiencies, suggests skill improvements | OpenClaw + GBrain both have dream cycles. Koomen: *"auto research from Karpathy again, you know."* Convergent with Codex SLG-Goal. |
| **DRY + MECE resolver discipline** | Skills checked against *"don't repeat yourself"* + *"mutually exclusive, collectively exhaustive"* (the McKinsey term) — Koomen runs a *check resolvable* meta-skill regularly | *"It's bad to have 10 skills that do all the same thing. It's good to have one skill or one tool that has parameters that then let you call them."* |
| **Model router underneath** | Common substrate so any tool / skill can invoke any model | Removes the *which-model-this-week* coupling from tool authorship. |

**2. The SQL-as-magic-moment empirical anchor** — Koomen's narrative of how YC's internal AI infrastructure started. The finance team had a workflow problem (booking journal entries / logging priced rounds): engineer-and-finance back-and-forth was inefficient relative to what agentic coding tools (Cursor, Windsurf, Claude Code) gave engineers individually. Solution: give finance the agentic tools directly, with a tool registry. Jared Friedman built read-only SQL access to YC's production Postgres — *"surreptitiously pushed it out maybe late at night"* — and it worked extraordinarily well. Non-technical finance partners (*"granted very smart people"*) could ask: *"show me all of the investors who invested in a space-related company in the last four batches."* What used to be *"several hours of writing SQL"* became seconds. This is a worked example of the *"give the agent unrestricted access; safety / privacy concerns were the actual blocker"* observation that recurs as a sub-theme throughout the talk.

**3. The Jevons-paradox claim for agent-mediated work** — *"It didn't just make it easier to answer questions. It dramatically increased the number of questions that we would ask and dramatically increased the scale and complexity of the questions that we would dare to ask. ... If in order to ask some kind of complex question about YC I have to go and knock on the data science team's door and wait for them to get it through their backlog, I'm just going to ask far fewer questions."* Koomen and Tan are explicit that removing the data-team-as-gatekeeper unlocked *order-of-magnitude more questions*, not just faster answers. This is the wiki's clearest YC-altitude statement of [[Jevons' paradox for agents|Jevons' paradox applied to organisational analytics]].

**4. The two-sentence-pitch skill as worked example of org-scale super-intelligence compounding** — a YC partner (*"Tom"*) wrote a skill teaching agents to compress a company's context into a two-sentence pitch. A couple of other partners then ran a group-office-hours session with founders, generated transcripts of feedback on bad two-sentence pitches, fed the transcripts back to the agent with the prompt *"given what you've learned by reading through this context, improve the two-sentence-description skill,"* and the skill *"got noticeably better after that ... this thing is now better than I am, I would argue, at writing those."* Tan's interpretation: *"This is how super-intelligence happens inside organizations. ... You can look at the operation of any organization as the aggregate of, you know, the two-sentence pitch is one of like thousands of things that I would argue we do for founders. ... How do you build super-intelligence inside a company? You do that on everything you do. And it's not more complicated than that."* The Jack Dorsey / Block-as-mini-AGI analogy is invoked here. **The wiki's clearest single worked-example of *micro-skill iteration → org-scale superintelligence compounding*.**

**5. The egalitarian + trust-by-default precondition** — *"It betrays two traits of truly agentic 1000× super-intelligent organizations that I would not have necessarily guessed would exist but are now must exist if you want to create this type of organization. You have to be relatively egalitarian and you also have to be trust by default. And ... neither of those things actually are most organizations in the world."* Broadcast-by-default agent conversations only work in high-trust environments — they substitute social control for technical access control. *"If you're the founder of an organization, you actually have to have those at the core of what you're doing."* This is named explicitly as a precondition for the multiplayer-harness primitive set — and as a reason this works best at startups, not Fortune 500s. Connect to [[strategic-renewal]] and any future *AI-native organisational culture* concept page.

**6. The $100K-token-budget leapfrog argument** — *"You have to be willing to spend like $10 to $100,000 a year on tokens. But if you're willing to do it and you invest in the skills and you actually do everything in an open way with your team that way, what I realized is it allows you to live in 2028, right? Like what you spend a $100,000 or a million dollars a year on now it will be commonplace in two years. ... It'll cost 10,000 and the year after that it'll be like a couple hundred bucks, and everyone will do it and we'll call it 'this is how companies are now.' So basically there's a one-time time warp where you can leapfrog every incumbent, all Fortune 500s, all startups that exist by doing this."* The wiki's clearest *time-arbitrage-on-token-cost-deflation* framing — a structural argument for why early adopters can build a durable advantage. Useful as economic anchor for [[enterprise-ai-adoption]] strategy discussions.

**7. The *raising the floor* observation about employee onboarding** — *"A new employee joining and maybe it would have taken them six months to ramp up. But with this, it's sort of like they automatically get a lot of the context from the company working and they know how the best people and the star players in the organization do things by apprenticeship automatically with AI ... I think it helps all the new entrants in the organization just be a mini-version of you a lot faster."* + *"All of the dumb questions I was too embarrassed to ask, I had no trouble asking the agent."* — apprenticeship-without-the-social-cost. Useful as anchor for [[ai-employment-effects]] discussion of the *onboarding-cycle compression* mechanism that runs counter to the *junior-developer-hiring-collapse* observation.

## The just-in-time-software / chat-is-the-right-UI evolution

Both Tan and Koomen describe a personal arc — both *"used to be in the camp"* that chat was the wrong UI for AI applications; both changed their minds. Tan's framing: *"chat is probably the better interface because it's the closest thing to human language and human language and writing is basically the closest thing to expression of thinking. So chat is the closest stepping stone to clear intelligence."* Multimodal extensions (voice memos, screenshots, files) make chat-the-UI sufficient. Koomen's framing connects to **just-in-time software**: *"It could make the software and build it as a single-page JavaScript just purposely built for you at that moment. ... it could be a skill file that could be called anytime you want."* — agent generates a one-off UI on demand when chat isn't enough.

Tan adds a Gary's-List-2.0 worked example: he spent January-February 2026 building *"half a million lines of code for a Rails app, which was Gary's list"* the way he would have built software in 2013 (with Claude Code as substrate). When rewriting as [[GBrain]] (the current open-source agentic retrieval system, *"10,000 lines of TypeScript and maybe 2,000 lines of markdown"*) it became dramatically simpler and more dynamic — *"my editor-in-chief can just change [the second paragraph's biography format] on the fly and I didn't touch it."* The contrast is a worked example of the [[Horseless Carriages|*horseless-carriages*]] failure mode being avoided: less deterministic-software-wrapping-AI, more agent-wrapping-deterministic-tools.

## The Horseless Carriages essay reference

Koomen wrote the *Horseless Carriages* essay after building YC's internal infrastructure, critiquing the *AI-as-feature-inside-deterministic-software* pattern (Gmail's AI email-writer as the canonical example). The essay's conclusion as restated here: *"as we get better at building AI-native software, it's going to look a lot more like the agent wrapping software-deterministic tools rather than deterministic software wrapping AI."* The YC infrastructure is the institutional operationalisation of this thesis — agent-wraps-tool-registry rather than deterministic-software-with-AI-features-bolted-on.

## The 1984-vs-Homebrew framing (Tan's closing argument)

Tan closes with a political argument for personal AI: two possible 2034 futures, *"the 1984 case"* of five centralised kings (ChatGPT-style locked MCP, no own-prompt control, all compute in a few hyperscaler data centres) vs the *"Homebrew Computer Club"* future where billions of users *"control and program for themselves"* via open-weight models, own-prompt control, own private repos. *"This is like the Apple I moment right now. We are coming up with the primitives."* Cited tools on the *"open"* side: [[OpenClaw]] / Hermes Agent / [[GBrain]] / [[Pi (coding agent)|Pi]] (the minimal open-source self-extending coding agent). Cited on the *"closed"* side: ChatGPT MCP (*"really locked down"*), Claude (*"a little more open but not really"*), Perplexity Computer (*"the best version of it, but still pretty limited"*).

Koomen's coda: *"I always really bristle when I see AI framed as a way to replace people because it just doesn't match the way that I have experienced it ... not as a replacement for humans but as a thing that empowers."* The wiki's clearest YC-doctrinal-altitude pushback on the *AI-as-replacement* framing, with the historical-precedent argument (mainframes → PCs → internet → AI as successive empowerment platforms).

## Why this matters in the corpus

Three sub-corpus roles for this source:

1. **The wiki's clearest paired *IC-vantage + architecture-vantage* on a single internal-agent-infrastructure project.** [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg]] (19 May) is the 5-minute IC teaser; this Koomen / Lightcone source (27 May, 8 days later) is the 46-minute architecture-and-organisation talk. Together they document the same project from two altitudes inside the same firm.

2. **The wiki's first explicit *single-player → multiplayer harness-engineering progression*.** [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / [[2026-05-15-osmani-agent-harness-engineering|Osmani]] / [[2026-05-04-rethinking-agents-harness-is-all-you-need|Khan]] all anchor *single-player-harness* engineering as a discipline. Koomen names the next-altitude problem (multiplayer harness for team / org scale) and proposes a primitive set (shared tool registry + shared skill registry + broadcast-by-default conversations + dream cycle). Plausible single-source-deferred concept-page candidate: *multiplayer-harness*.

3. **The wiki's clearest single worked-example of *micro-skill iteration → org-scale superintelligence compounding*** — the two-sentence-pitch skill case (point 4 above). Connects to the [[enterprise-ai-adoption]] *workflow-not-task imperative* from [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee/MGI]] via a different operational unit: not workflows but **skills as the atomic unit of org-scale compounding**.

The W&W tagging (8 cells — among the broadest cell coverage in the wiki, alongside [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng AI Dev 26 SF]] at 9 cells and [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen AWS London Exec Forum]] at 10 cells) reflects this source's reach across the W&W process model — touching three of five buckets substantively. The **strategic-renewal/organizational-culture + strategic-renewal/collaborative-approach** cells in particular pick up Koomen's *egalitarian + trust-by-default + broadcast-by-default* preconditions, which are organisational-culture refresh claims, not just digital-capability claims.

## Tools / projects named

- **YC internal infrastructure** — agent loop + model router + 350-tool shared registry + skill registry + broadcast Slack channel + dream cycle.
- **[[GBrain]]** — Tan's open-source agentic retrieval system; ~10K lines TypeScript + ~2K lines markdown; succeeds the half-million-line Rails app *Gary's List*.
- **[[OpenClaw]]** — agentic harness; has skillify and dream cycle.
- **Hermes Agent** — agentic harness; *"already has skillify, they call it something else."*
- **[[Pi (coding agent)|Pi]]** — *"this open-source harness called Pi which is the smallest possible coding agent. You can use Pi to modify and extend Pi."* Self-extending, self-referential. [[OpenClaw]] built on top of it.
- **[[Claude Code]]** — substrate; cited repeatedly. *"Boris obsessed with simplicity."*
- **Codex** — has SLG-Goal (Self-Learning-Goal) — Codex's version of the dream cycle / auto-research pattern.

## ASR notes

- Captions sourced via yt-dlp `--write-auto-sub` (engagement-panel route timed out at 180s — recurring for ≥20-minute talks per [[CLAUDE|§Acquire failure modes]]).
- VTT rolling-window dedup applied — second-line-of-each-cue content kept, inline `<c>` per-word timing tags stripped, HTML entities unescaped (`&gt;&gt;` → `>>`), bucketed to ~5-second segments.
- Surface artifacts: *"Pete Kumman"* in opening (correct: Pete Koomen); *"Harge"* spelled inconsistently; *"open core"* and *"open claw"* both appear (correct: **OpenClaw**, OpenAI's open-source coding-agent reference implementation).

## Linked entities and concepts

**Entities (already promoted, source_count bumped):**
- [[Y Combinator]] — channel / publisher.
- [[Garry Tan]] — host / co-presenter.
- [[Diana Hu]] — host.
- [[Andrej Karpathy]] — load-bearing citation (LLM-wikis + auto-research).
- [[Claude Code]] / [[Anthropic]] — substrate.
- [[OpenAI]] — Codex / SLG-Goal.

**Dangling first-mentions (single-source, deferred per [[CLAUDE|§Lifecycle author-entity promotion]]):**
- Pete Koomen — YC partner; co-founder Optimizely; author of *Horseless Carriages* essay.
- Harge Taggar — YC partner.
- Jared Friedman — YC partner; built the first SQL-against-production tools.
- *"Tom"* — YC partner; authored the two-sentence-pitch skill.
- Boris (Cherny) — *"Boris obsessed with simplicity"* re: Claude Code design philosophy.
- Diana — appears in dialogue but with the existing [[Diana Hu]] entity.

**Concepts (last_confirmed bumped; substantive new content possible on multiplayer-harness, enterprise-ai-adoption, agent-harness):**
- [[agent-harness]] — multiplayer-harness extension; resolver-as-AGENTS.md primitive; skillify as meta-skill.
- [[agentic-engineering]] — YC's internal infrastructure as a worked example of agentic-engineering at org scale.
- [[enterprise-ai-adoption]] — *raising the floor* + *$100K-budget leapfrog* + *trust-by-default + egalitarian preconditions* + *one-database BigTable-for-agents pattern*.
- [[agent-development-lifecycle]] — dream-cycle as the night-time iteration phase.
- [[is-rag-dead]] — Koomen explicitly says *"all the things that everyone has learned about retrieval — RAG, graph-RAG, hybrid RRF — is now inside GBrain"* — RAG-inside-agentic-harness confirmation.
- [[durable-skills]] — the *two-sentence pitch as atomic skill* + *org-scale compounding* framing.
- [[automation-vs-augmentation]] — Koomen's coda explicitly aligns with augmentation.

## Source

- **Raw transcript:** [transcript file](../../raw/videos/inside-yc-ai-playbook.md) (yt-dlp WebVTT → 5-second-bucketed segments; 555 segments; ~46:30 minutes).
- **Public URL:** [youtube.com/watch?v=B246K_G7mHU](https://www.youtube.com/watch?v=B246K_G7mHU)
- **Channel:** [[Y Combinator]] (Lightcone podcast format)
- **Published:** 27 May 2026
- **Caption track:** auto-generated; no human-curated track at time of ingest.

## Reading scope

Full ~46:30 transcript read end-to-end during ingest. Seven substantive contributions surfaced (multiplayer-harness primitive set; SQL-as-magic-moment empirical anchor; Jevons paradox for agent-mediated work; two-sentence-pitch worked example of org-scale superintelligence compounding; egalitarian + trust-by-default precondition; $100K-token-budget leapfrog argument; raising-the-floor onboarding observation). Just-in-time-software / chat-is-right-UI evolution captured. *Horseless Carriages* essay reference + 1984-vs-Homebrew framing captured. Plausible single-source-deferred concept-page candidate: *multiplayer-harness*.
