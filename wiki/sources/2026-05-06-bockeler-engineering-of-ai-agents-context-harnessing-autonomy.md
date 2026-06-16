---
type: source
kind: video
title: "The Engineering of AI Agents: Context, Harnessing, and Autonomy"
author: ["InfoQ"]
url: "https://www.youtube.com/watch?v=_R83pFpUWyM"
date_published: 2026-05-06
length: "~42:01 minutes (transcript ~191 grouped segments from 1198 raw ASR lines)"
raw: "../../raw/videos/bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md"
tags: [agent-harness, harness-engineering, context-engineering, agentic-engineering, vibe-coding, lethal-trifecta, ai-security, structural-tests, agent-autonomy, qcon-london-2026, thoughtworks]
relationships:
  - type: supports
    target: agent-harness
    via: "first independent-practitioner-consultancy vantage on harness engineering as a discipline; adds feed-forward/feedback decomposition, CPU-vs-GPU framing, structural tests as feedback, enhanced lint messages as good prompt injection"
  - type: supports
    target: agentic-engineering
    via: "Thoughtworks consultancy lens on the discipline across many client codebases — corroborates Karpathy / Fung / Lopopolo from a multi-project observer vantage"
  - type: supports
    target: micro-productivity-trap
    via: "Goldilocks speed framing + Amazon-adding-senior-engineer-gateways reaction is the same diagnosis as Bain/OpenAI and Sternfels — speed pressure without supervision integrity erases productivity gains"
  - type: supports
    target: vibe-coding
    via: "QCon-London-2025 anchor (term was ~2 months old then) corroborates the timeline; identifies vibe coding as one end of an autonomy spectrum that harness engineering attempts to widen safely"
  - type: supports
    target: jagged-frontier
    via: "probability x impact x detectability risk-assessment framework is the practitioner-operational form of jagged-frontier navigation"
---

# The Engineering of AI Agents: Context, Harnessing, and Autonomy

> As we move from simple autocompletion to autonomous AI agents, "vibe coding" isn't enough for enterprise-grade software.
>
> Birgitta Böckeler (Thoughtworks) explores the shift from prompt engineering to "Harness Engineering" — the practice of building deterministic safety nets around non-deterministic models.

(Channel description, InfoQ.)

A 42:01 keynote-style talk delivered by **Birgitta Böckeler** ([[Thoughtworks]]) at **QCon London 2026**, published to the [[InfoQ]] YouTube channel on 6 May 2026. Böckeler returns to QCon after a year-earlier *From Autocomplete to Agents* talk and uses this slot to do a structured year-on-year review: what changed in AI coding agents between QCon London 2025 and QCon London 2026, with the **harness** as the load-bearing concept tying it together.

Auto-generated transcript (caption track `kind: asr`); fetched via the `youtube-transcript-api` fallback path after the Playwright skill hit the documented [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) `transcript panel did not render` timeout on talks over 20 minutes. ASR cleanup applied: non-speech `[music]`/`[applause]` markers dropped, `>>` speaker indicators normalised, YouTube's own chapter list preserved as section headings, segments grouped into ~12-second windows.

## TL;DR

Böckeler's structural argument is that **the past year has resolved one question and exposed another**.

1. **Resolved**: *what does a serious AI-coding setup look like?* — it looks like a **harness**. The pieces (rules / commands / [[Anthropic-Skills]] / MCP / subagents / plugins / specs / structural tests / sandboxes / language-server access) that practitioners have been bolting together since QCon 2025 are now coherent enough to be named as one thing. The OpenAI Codex team explicitly coined **harness engineering** for this; Böckeler propagates the term into the broader engineering audience and gives it a two-axis decomposition (**feed-forward** + **feedback**, each containing both **CPU-based deterministic** and **GPU-based inferential** elements).

2. **Exposed**: *how much autonomy is appropriate, and at what cost?* — autonomy increased fast (cloud agents, agent teams, agent swarms à la [[Steve-Yegge]]'s "Gas Town" stage 6+), costs migrated from $20 flat to $200 flat to **$380/day metered tokens** (= ~$91k/year, "a developer salary in Germany"), and the [[lethal-trifecta]] (untrusted content + private-data access + external comms — credited to Simon Willison, June 2025) makes the security surface unforgiving. Böckeler's response is a **risk-assessment trio** — *probability* of AI error in this context, *impact* if it errs, *detectability* of the error — and a **Goldilocks speed** counter-framing to the speed-at-all-costs zeitgeist: Amazon reportedly responded to AI-code-related outages by adding senior-engineer gateways, defeating the speed gain.

The "harness templates" peroration — an analogy to service templates that lets teams pick a workflow topology (data dashboard / CRUD service / event processor) and instantiate a pre-built harness rather than rebuild it — is Böckeler's offered prediction for the next abstraction layer.

## What was actually ingested

Full talk transcript (~41:50 of speech, ~191 windowed segments). Böckeler's slides are referenced verbally; visual content (screenshots, GIFs, diagrams) is not captured by the transcript. The chapter list YouTube published runs to 28:15 and stops there, but the talk continues for ~14 more minutes under the final chapter heading — this is a YouTube-side authoring artefact, not a transcript gap.

## Year-on-year: what changed since QCon London 2025

Böckeler opens with three temporal anchors that calibrate the wiki's chronology:

- *"the term vibe coding was about 2 months old"* at QCon 2025 — placing [[vibe-coding|the term's coinage]] around early 2025, consistent with the wiki's existing dating of [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's]] retrospective.
- *"MCP was all the rage"* at QCon 2025 — confirming MCP's hype peak preceded its operational maturity.
- *"Claude Code was still in diapers"* — confirming Claude Code went from preview to general availability across the QCon 2025 → 2026 window.

These confirm the wiki's existing "December 2025 phase change" framing (per [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] and Karpathy) from the **conference-circuit observer's** angle.

## Context engineering as a named practice

[[context-engineering]] (not yet a wiki concept page; first source) is defined by Böckeler as **curating the information that your model or agent sees to get better results**. The term *"started floating around June"* (2025) and now spans:

- **Rules files** — workspace-level `agents.md` / `claude.md` files for typical pitfalls and repeated errors.
- **MCP servers** — dynamic data retrieval for the agent.
- **Anthropic Skills** — modularised, JIT-loadable subfolders containing rules, scripts, and references. *"Progressive lazy loading of context"*. Skills can include scripts and instruct the agent to use CLIs already on the machine, *"which has had a lot of people shift away from MCP in agent coding"*. Skills are the wiki's first dedicated framing of this mechanism.
- **Commands, subagents, plugins, specs** — the rest of the surface area accumulating around the practice.

Böckeler zooms in on two structural moves:

1. **Modularisation + lazy loading**: rather than one big rules file always sent to the agent, the agent receives a *description* of each available skill; if it judges the skill relevant, it loads that skill's full content. The implication for context-window economics is significant — a 15%-full context immediately after session start (Böckeler's screenshot) becomes the practitioner's baseline.

2. **Context interfaces**: the *list-of-tools* surface — Skills descriptions, MCP server tool lists, built-in coding-agent tools — is the new pressure point. *"It's all about how can you get this to be intelligently loaded just in time."* The agent's runtime decision-making about *what to load when* is itself the new engineering work.

Böckeler closes the section with **open questions** that the wiki should track:

- **Versioning and distribution** — *"plugin marketplaces, some of you might have heard of them, again introduced by Anthropic and the Cloud Code team"* — early but immature.
- **Are skills actually helping?** — *evals*. Anthropic released eval tooling; "Tessell" (ASR-uncertain transcription) released a skills registry. Early stage.

## The cost reality: $380/day and the end of flat-rate pricing

Two cost anchors:

- **Early 2024**: a keynote speaker quoted *"generating 100 lines of code only costs about 12 cents"*. Böckeler concedes lines of code is a bad value metric but uses the figure as a temporal anchor.
- **Summer 2025**: a Reddit/community post documented a developer averaging **$380/day** in token usage — extrapolated to *"$91,200/year, which is not a bad developer salary in Germany"*.

Pricing structure migration:

| Era | Pricing | Failure mode |
|---|---|---|
| Late 2023 – early 2024 | $10–$20 flat-rate (Copilot, early Claude) | none — the model couldn't yet exhaust the bandwidth |
| 2024 – early 2025 | $20–$50 flat-rate | rate-limiting starts to bite |
| 2025 | $200 flat-rate | not really flat — *"middle of the month and I'm out of tokens"* posts on Reddit |
| Late 2025 onward | Metered / consumption-based | $380/day is observable in the wild |

Mechanism for the cost expansion: the agentic-coding loop *itself* burns tokens. Where 2024 autocomplete was a single inference per accept/reject, the 2026 loop is **research the existing code → make a plan → review and adjust the plan → start implementation → run the tests → fix the tests → check the lint errors → fix the lint → check the browser → run a code-review agent → react to that → have a summarization** — and it might still be only two lines of code at the end. This is direct corroboration for [[micro-productivity-trap|the micro-productivity trap]]'s mechanism from the **token-economics angle**.

## The autonomy spectrum and agent swarms

Böckeler frames the supervision question as a spectrum, not a binary:

- **Supervised**: developer in front of the session, steers each step.
- **Unsupervised cloud agent**: send a task off for ~20 minutes (the post-Codex pattern, mid-2025 onward; Cursor, Claude Code, Copilot now all offer cloud-mode plus CLI-headless modes that integrate into CI/CD).
- **Agent teams** (Claude Code preview feature): small-N orchestrated coordination — Böckeler tried ~5.
- **Agent swarms**: dozens or hundreds. Steve Yegge's "Gas Town" *eight stages of dev evolution to AI* — stage 6 = 3 parallel Claude Code instances, stage 7 = 10, stage 8 = swarms. Böckeler tried three: *"I kept typing the wrong thing into the wrong session"*.

She singles out two **agent-swarm experiments that made people nervous**:

- **Cursor**: ~1 week run building a browser.
- **Anthropic**: building a C compiler.

Both were taken by the audience as evidence of imminent AI software autonomy. Böckeler pushes back: *"both of those use cases are very, very well-specified problems"* — browsers and C compilers have public specifications and (especially the compiler) elaborate public test suites the agent can use as feedback. **Enterprise software typically lacks both.** This is the wiki's first explicit statement of the **selection-bias caveat** on agent-swarm demos.

## The lethal trifecta and the new security surface

Böckeler attributes [[lethal-trifecta|the lethal trifecta]] to **Simon Willison (June 2025)**: an agent that has all three of

- **Exposure to untrusted content** (the web, user-uploaded files, GitHub issues from third parties)
- **Access to private data**
- **External communication ability**

has a high data/security risk. *"It's not a technical problem. It's a conceptual problem"* — and it applies as much to business agents (email read + send) as to coding agents.

Worked examples from "the past 11 days":

- **Unwanted command execution** via prompt injection slipping past allow-list patterns.
- **Secret extraction**: a prompt injection in a GitHub issue triggered an agent without supervision, which then exfiltrated credentials enabling NPM-registry pushes to a popular open-source tool.

Böckeler's response: **sandboxing locally**, not just in the cloud — dev containers, plus a wave of new products with new sandboxing ideas. And: **AI security literacy** in the engineering organisation, with explicit norms against YOLO-mode (auto-allow everything).

## Harness engineering as a named discipline

Böckeler's framing of the harness is the substantive contribution of the talk. She **explicitly credits the OpenAI Codex team for the name**: *"the team called this harness engineering"* — which is the [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo article in OpenAI's engineering blog]] that the wiki already holds as the vendor-side production case study.

### Two-axis decomposition

| | **Feed-forward** (anticipate what the agent might do wrong) | **Feedback** (after generation, give it correction signal) |
|---|---|---|
| **GPU-based** (LLM inference) | Principles, conventions, reference docs, how-to skills, prompt instructions | Code-review subagents, summarisation subagents |
| **CPU-based** (deterministic) | CLIs, bootstrap scripts, codemods (OpenRewrite recipes), language-server refactoring (IntelliJ rename-symbol via MCP) | Static analysis, structural tests, custom linters, browser checks, application-runtime feedback |

The CPU-vs-GPU framing is **borrowed from a company Böckeler called "Modern"** in the ASR (likely *Modal* — modal.com — but ASR-uncertain). The framing's substantive claim: the harness should mix deterministic CPU-side tooling with non-deterministic GPU-side inference, with the deterministic side carrying *more* of the harness load than enterprise teams currently invest in.

### Structural tests as agent feedback

The novel-feeling mechanism in the talk: **encode architectural constraints as automated checks the agent must satisfy**.

- **Java**: [[ArchUnit]] — package-layer dependency rules as unit tests.
- **Spring**: [[Spring-Modulith]] — module boundary enforcement.
- **TypeScript**: [[Dependency-Cruiser]] (Böckeler's experiment) — dependency rules across layered folders.

Böckeler's worked example: a rule that *"external SDKs may only be imported by files in the /clients folder"* (where you have lots of clients for other APIs) and *"may not be imported in the /domain folder"* — encoded as a structural test, fails the build if violated, becomes a *feedback signal the agent reads and corrects against*.

Böckeler's observation: *"we've had these tools for quite a while, but I think a lot of people haven't used them because we think we were working on the code"* — i.e. structural-rule enforcement was always available, just under-adopted because humans rationalise *"I know how to modularise"*. The agent is the new consumer of these tools.

### Enhanced lint messages as "good prompt injection"

A second mechanism: **edit the lint-error text itself to include the refactoring hint**. Example: a 500-line-per-file rule could include *"this is often a smell for a design problem; consider refactoring rather than splitting statements"* — which gives the agent the *meta*-correction (rethink the structure) rather than the *immediate* correction (collapse into multi-statement lines). Böckeler frames this as *"a good type of prompt injection"* — the message text reaches the agent's context as instruction.

### Harness templates as the next abstraction

Speculative but explicit. Just as **service templates** standardised the bootstrap of a new microservice with the right tech-stack + scaffolding, Böckeler proposes **harness templates** standardising agentic-workflow scaffolding: pick a workflow topology (data dashboard / CRUD service / event processor / etc.), instantiate a pre-built harness with the relevant CLIs, MCPs, structural tests, lint rules, codemods. The decision metric shifts: *"is there an existing harness?"* may matter more than *"React or Vue?"* — *"because then I don't have to build that up initially"*.

### Direct cross-reference to the wiki's existing Lopopolo source

The most load-bearing single passage in the talk for cross-source weaving:

> *"There was an interesting article recently by a team at OpenAI that says they have been working on a code base for the last 5 months. It started as a greenfield code base, and their kind of rule for themselves was: we don't want to touch the code directly. We just want to interact with the agent and then continuously improve the setup around it ... It was a mix of these things — a lot of that context engineering stuff, like skills ... custom linters and structural tests ... and then they still said they kind of had entropy increasing and drift happening. So they had what they called garbage collection."*

This is a direct, unambiguous reference to [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's "Harness engineering: leveraging Codex in an agent-first world"]] (11 February 2026). Böckeler's talk **substantiates Lopopolo's findings from an external practitioner-observer vantage** — Lopopolo is the operator's account; Böckeler is the consultant's reading of the operator's account, and she finds the substance persuasive enough to make harness engineering the spine of her year-on-year review.

## Risk assessment: probability × impact × detectability

Böckeler's offered decision-framework for *how much supervision a task warrants*:

- **Probability** that AI will get *this* task wrong — assessed by *knowledge of the context given*, *experience using the tool for similar tasks*, *confidence in the requirements*.
- **Impact** if it gets it wrong — proof-of-concept vs. *"out of bed at 2 a.m. on the weekend"* critical-path.
- **Detectability** of error — quality of feedback loops; test automation, lint, browser checks, runtime telemetry.

The decision the trio drives: *workflow elaborateness* (heavy planning vs. quick prompt), *review depth* (every line vs. spot-check vs. none), *time off-leash* (longer unsupervised → larger review burden after).

Böckeler notes that only the **first** (probability of AI error in *this* context) is genuinely new to experienced engineers — the other two are pre-existing engineering judgements applied to the new tool. The talk's most concise statement of the *operator-skill* required:

> *"You have to be this tall to ride the roller coaster — you have to be this tall to reduce supervision."*

## The "Goldilocks speed" peroration

Böckeler's counter-framing to the speed-at-all-costs zeitgeist:

> *"How much speed do we actually need? What is the Goldilocks speed that is fast enough but not too fast?"*

Anchor anecdote: **Amazon reportedly added senior-engineer review gateways** in response to outages believed to be related to AI-generated code — *"weren't we supposed to be faster going into production, and now we're putting in more gateways?"* The implication: speed pressure without harness investment → corner-cutting → outages → more gateways → *less* speed than the pre-AI baseline. This is direct convergence with the wiki's existing [[micro-productivity-trap|micro-productivity trap]] thesis, now reinforced by a **third consulting/observer firm** (Thoughtworks, after Bain via [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt-Chatterji 2026]] and McKinsey via [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026]]) reaching essentially the same diagnosis.

Cognitive-overload anecdotes: practitioners reporting burnout from running 3+ Claude Code sessions in parallel; *"yeah, you said no, but I thought you meant something else"* style Reddit-viral agent confabulations.

Final framing: AI is *"a Swiss Army knife with lots and lots of potential use cases"* — many are *"useful as enhancement of yourself"* with supervision. The framing concedes ground to the through-line of full-automation discourse while pushing back on its hegemony.

## Convergence and contradictions with existing wiki sources

| Source | Connection |
|---|---|
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex 2026]] | **Direct reference**. Böckeler propagates Lopopolo's *harness engineering* term and case study to the QCon-London audience; her feed-forward/feedback decomposition is compatible with Lopopolo's repository-as-system-of-record + custom-linters + golden-principles-GC pattern. Lopopolo is the operator vantage; Böckeler is the consultant vantage on the same operator. |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026 (Anthropic / Claude Code engineering)]] | **Org-shape complement**. Fung described what running an agent-native engineering team looks like inside the vendor; Böckeler describes what observing that pattern from outside (across many client engagements) implies for consulting practice. Fung + Lopopolo + Böckeler now form a **three-vantage cluster** on the same construct: team norms, codebase artefact shape, observer's discipline name. |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | **Paradigm anchor**. Karpathy named the [[agentic-engineering]] discipline; Böckeler propagates the discipline-name *harness engineering* (the sibling/synonym used by the Lopopolo case). The wiki should hold both — Karpathy frames the practitioner identity; Böckeler frames the artefact-construction activity. |
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Prompt Engineering YouTube, May 2026]] | **Empirical bookend**. The PE-YouTube source provides the ablation data (same model, 6x variance across harnesses); Böckeler provides the consultancy-observer vantage saying the same thing is happening at her client sites. Together they form a *measured + observed* pair. |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic Managed Agents]] | **Sandboxing convergence**. Anthropic's *structural unreachability* and Böckeler's *sandbox locally and in cloud* both name the Constraints layer of the harness as the primary security mechanism (vs. policy-based controls). |
| [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt-Chatterji 2026]] (Bain, OpenAI) | **Third-vantage on micro-productivity trap**. Goldilocks-speed = the trap from the consulting-observer angle; Bain + McKinsey + Thoughtworks have now reached the same diagnosis. |
| [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting\|Sternfels 2026 (McKinsey)]] | **Second consulting vantage on the trap** that Böckeler now joins. *"Half, if not more, of the secret sauce is organisational change"* (Sternfels) is compatible with Böckeler's *Goldilocks speed* + *risk-assessment trio* — both push back on technology-as-acceleration framing. |
| [[2026-05-05-nishar-nohria-end-of-one-size-fits-all\|Nishar-Nohria 2026]] | **Outcome-based pricing × cost-economics complement**. Nishar-Nohria names outcome pricing as the macro trend; Böckeler documents the micro-economics ($380/day metered) that makes flat-rate developer tooling untenable and forces the outcome conversation at the developer-tool layer. |

### Contradictions

None substantive. Böckeler's pushback on agent-swarm hype is *cautionary* relative to the Anthropic/Cursor experimental demos, but neither claims production-readiness — Böckeler is calibrating audience expectations, not disputing facts.

## Linked entities and concepts

**Existing wiki entities reinforced**:

- [[Anthropic]] — Claude Code, Anthropic Skills (the formalisation of modularised JIT-loaded context), agent-team preview feature, the agent-swarm C-compiler experiment, the plugin marketplace.
- [[OpenAI]] — Codex (referenced via the Lopopolo article), the cloud-agents kickoff.
- [[Google]] — implicit (Gemini-family models in the rented-model spectrum; not substantively discussed).
- Related concept pages updated: [[agent-harness]], [[agentic-engineering]], [[vibe-coding]], [[jagged-frontier]], [[micro-productivity-trap]].

**Dangling** (single-source first-mention, deferred per the author-entity-promotion rule):

- **Birgitta Böckeler** — speaker; Thoughtworks AI/dev-experience lead.
- **Thoughtworks** — consultancy; presenter affiliation.
- **InfoQ** — channel/publisher.
- **QCon London 2026** — venue (annual conference; the 2025 edition is implied as Böckeler's prior-talk reference point).
- **Simon Willison** — credited for the [[lethal-trifecta]] framing.
- **Steve Yegge** — Gas Town blog post (eight stages of dev evolution to AI); Cloud Flow project (renamed).
- **Modal** (likely; ASR-uncertain rendering "Modern") — credited for the CPU-vs-GPU harness framing.
- **Tessell** (ASR-uncertain) — skills registry / evals tool.
- **Cursor** — agent-swarm browser experiment; CLI mode.
- **Dependency Cruiser** — TypeScript structural-test tool used in Böckeler's worked example.
- **ArchUnit** — Java structural-test tool named.
- **Spring Modulith** — Spring modular-monolith tool named.
- **OpenRewrite** — codemod tool named in the feed-forward CPU-side cell.
- **IntelliJ** — language-server / rename-symbol refactoring via MCP, named in the feed-forward CPU-side cell.

**Concept candidates surfaced (not yet promoted)**:

- [[context-engineering]] — first wiki source naming the term as a discipline. Single-source for now; promotion on second-source mention.
- [[lethal-trifecta]] — first wiki source naming Willison's framing as a load-bearing security construct. Promotion on second-source mention.
- [[harness-engineering]] — the *naming* of the discipline (versus the artefact [[agent-harness]]). Currently lives inside the [[agent-harness]] concept page; promotion to its own page would split the artefact-vs-discipline pair the way [[vibe-coding]] / [[agentic-engineering]] are split. Defer until a third source explicitly uses the term as a discipline-name.

## Open questions raised by this source

- **Modal vs. Modular**: which company actually frames the CPU-vs-GPU harness decomposition? Verify the ASR-uncertain attribution; potential primary-source ingest.
- **Tessell**: is this a skills registry / eval tool, or an ASR mistranscription of another product name? Search target.
- **Steve Yegge's "Gas Town" essay**: a primary-source ingest would substantiate the eight-stages model and the Cloud Flow rename.
- **Amazon's senior-engineer-gateways response**: Böckeler references *"an article about Amazon reflecting on outages supposedly related to AI-generated code"* — primary-source ingest would substantiate and add precision to the Goldilocks-speed argument.
- **Cursor's browser-build agent-swarm experiment** and **Anthropic's C-compiler experiment**: primary-source ingest would let the wiki measure the selection-bias caveat against the actual claims.
- **Anthropic Skills**: primary-source ingest of the Skills launch documentation and the plugin marketplace would let the wiki give Skills its own first-class treatment rather than relying on second-hand observer characterisation.
