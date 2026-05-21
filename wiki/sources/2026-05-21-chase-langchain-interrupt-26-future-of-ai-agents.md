---
type: source
kind: video
title: "The Future of AI Agents: What Will Interrupt 2027 Look Like? | Interrupt 26"
author: ["LangChain"]
publisher: "LangChain (LangChain YouTube channel — Interrupt 26 conference, Day 2 keynote; Harrison Chase + Brace Sproul + Caroline di Vittorio)"
url: "https://www.youtube.com/watch?v=R9K2574YEAg"
date_published: 2026-05-21
date_ingested: 2026-05-21
length: "~22:10 minutes (manual English captions, 193 segments)"
raw: "../../raw/videos/the-future-of-ai-agents-what-will-interrupt-2027-look-like-interrupt-26.md"
tags: [langchain, harrison-chase, brace-sproul, caroline-di-vittorio, interrupt-26, langchain-labs, langsmith-fleet, deep-agents, fireworks-ai, two-types-of-agents, long-horizon-agents, customer-experience-agents, voice-agents, sandboxes, open-source-models, agent-identity, agent-auth, continual-learning, model-harness-context, three-layer-learning, metaharness, evals-as-gradient, go-to-market-agent, domain-experts-building-agents, no-code-agents, mcp, arcade-tools]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/strategic-agility
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Same speaker ([[Harrison Chase]]) 12 days later at LangChain's own Interrupt 26 conference. The ADLC blog-post (9 May) named the **frameworks / runtimes / harnesses / no-code** four-layer Build vocabulary; this Interrupt keynote (21 May) operationalises and **extends** that vocabulary along two new structural axes: (1) **two types of agents** typology (long-horizon vs customer-experience) — a parallel-vertical split orthogonal to the four-layer split; and (2) **three layers of continual learning** (model / harness / context) — a per-agent improvement-loop sub-structure inside the *Build* phase. The Fleet operationalisation (84% weekly usage on LangChain's own GTM agent; 240% lead-to-qualified conversion; 40 hours saved per rep per month) is the most-concrete in-LangChain operational anchor on the *no-code* layer Chase's ADLC piece names but does not yet quantify."
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "**Chase cites MetaHarness by name on stage at Interrupt 26** as the canonical *learn at the harness layer* worked example — *'a great paper out of MIT and Stanford called MetaHarness, where they used an agent to optimize a coding harness... it wasn't changing the model at all, it was just editing the harness, and they got a really good score there.'* This is the first founder-CEO-vendor-altitude on-stage citation of the Lee et al. paper the wiki holds at academic-primary-source altitude. The MetaHarness experiment is reasserted as the **paradigm example** of *evals-as-gradient* — *'these evaluations, terminal bench two, you run the agent on terminal bench, you get some feedback, you then pass that into the agentic system and updates it. Those evals are providing a similar type of this training gradient.'*"
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "**The third primary-source confirmation of the LangChain Top 30 → Top 5 on Terminal Bench 2 claim**, on stage from CEO Harrison Chase at Interrupt 26. First instance: Trivedy's 10 March 2026 LangChain Engineering blog post; second: Lopopolo's 11 February OpenAI Codex paper referenced the same magnitude-of-gain pattern; Chase's confirmation makes it canonical at the vendor-CEO altitude (*'we moved from top 30 on terminal bench two to top five just by changing the harness itself. So no changes to the model, only changes to the harness, and we saw a big increase in performance'*). The claim is now anchored at three independent primary sources spanning research-blog, academic-paper-adjacent, and CEO-stage altitudes — the strongest single-claim convergence in the wiki's *harness > model* corpus."
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Chase's **three-layer continual learning model** (model / harness / context) is the vendor-CEO operationalisation of the academic formalisation Karten & Zhang published on arXiv 10 days earlier. Karten's 4-component harness decomposition (p, G, K, M = system prompt / sub-agents / skills / memory) sits inside Chase's *harness layer*; the *context layer* sits adjacent (the agent.md + skill files that *configure* the harness for a particular task). Chase names the **LangSmith trace + feedback dataset** as the foundation for continual learning on the harness and context layers — the vendor-side data substrate for the academic loops Karten formalises. **LangChain Labs is announced as a research group aimed in particular at continual learning** — the institutional commitment paired with the academic agenda."
  - type: supports
    target: 2026-02-17-langchain-improving-deep-agents-harness-engineering
    via: "Same vendor blog → conference talk arc. Deep Agents was the LangChain harness pattern Trivedy and the LangChain Engineering blog had been articulating since Feb 17 2026; this Interrupt 26 keynote *productizes* it: **LangSmith Fleet is built on top of deep agents** (per Brace Sproul, ~17:23). The deep-agents-as-substrate-of-Fleet relationship makes the deep-agents pattern the foundational harness layer of the LangChain product stack — the most concrete *open-source-harness-as-substrate-of-no-code-product* worked example in the wiki."
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "Paired *founder/CEO articulations of layered-agent-system thinking* landing within 24 hours. Tan/Hu (CS153, 20 May) maps **agentic-primitives → company-structure** (skills = employees, resolvers = org chart, check-resolvable = audit, trigger evals = performance reviews). Chase (Interrupt 26, 21 May) maps **learning-systems → agentic-system-layers** (model / harness / context, each independently improvable with evals-as-gradient). Same architectural move (decompose-and-map) applied to two different domains: *what an organisation looks like with agents at its core* vs *what improvement-loops look like inside an agentic system*. Both founders articulate the *everyone-builds-agents* corollary: Hu's *AI founder / IC / DRI* org structure + Chase's *domain experts will be building agents, not just giving feedback*."
---

# Chase, Sproul & di Vittorio — The Future of AI Agents: What Will Interrupt 2027 Look Like? (LangChain Interrupt 26)

> Harrison Chase, Brace Sproul, and Caroline di Vittorio kicked off Day 2 of Interrupt 26 with an inside look at where AI agents are headed, the unveiling of LangChain Labs, as well as the latest features in LangSmith Fleet.
>
> — channel description, LangChain

## TL;DR

A ~22:10 LangChain Interrupt 26 Day 2 keynote (manual English captions, 193 segments), published 2026-05-21 on the [[LangChain]] YouTube channel. Three speakers: **[[Harrison Chase]]** (co-founder and CEO; segments 1–10 + closing), **Brace Sproul** (LangChain; segments 11–13 product walkthrough), and **Caroline di Vittorio** (LangChain; segment 13 live Fleet demo). The framing device: *imagine Interrupt 2027 — what would the topics be a year from now?*

**The substantive contributions are six.**

**1. The two-types-of-agents typology (~1:22–2:42).** Chase predicts a divergence — already emerging — in the agents being built:

| Type | Characteristics | Examples |
|---|---|---|
| **Long-horizon agents** | Run for minutes / hours / days; code execution, planning, sub-agents, multi-agent systems, skills; *outcomes and goals* as ways to extend the horizon | Knowledge-work agents that do more and more valuable work over time |
| **Customer-experience agents** | Latency-critical; voice (and maybe video) as modality; brand-sensitive; talking to an end user | Customer support, sales, end-user-facing |

*"There is a shared stack underneath. There are also differences in terms of the technology. And I think one of the big questions that we'll be thinking about over the next year is how common is this shared stack versus how particular are the technology pieces that you need for each?"* This is the wiki's first **structural typology of agent-product surfaces** distinct from the *frameworks/runtimes/harnesses/no-code* Build-layer typology of [[2026-05-09-chase-agent-development-lifecycle|Chase's ADLC piece]] — the new axis is *what the agent runs against (the world / time horizon vs end-user-experience)*, not *where the agent lives in the build stack*.

**2. Voice agents — pipeline vs native (~2:42–3:58).** Today's voice pipeline = speech-to-text → agent (operating in text space) → text-to-speech sandwich. Emerging = native speech-to-speech models (*"OpenAI released V2 of theirs two weeks ago"* — i.e. around 7 May 2026). *"While I would say the consensus today seems to be for applications where you really care about having control, they're not quite steerable enough yet, we do expect that to change."* The open question for Interrupt 2027: pipeline / native / combination.

**3. Every agent needs a sandbox (~3:58–4:47).** *"We think all agents will need a sandbox, especially these long-horizon style agents. So coding is really good for a variety of tasks. It's not just writing software — it's for data analysis, it's for web browsing, it's for image gen, for deep research."* The framing anecdote: *"when they think about building agents for their marketing team, one of the ways they think about it is they think about giving that marketing team a software engineer. What would that software engineer build? What apps would it build to make the marketing team's job easier? That's what giving an agent the ability to write and execute code is."* LangChain launched sandboxes "yesterday" (Interrupt 26 Day 1).

**4. The rise of open-source models — three drivers (~4:47–6:01).** (a) **Capability**: *"the performance of these base open models without any type of post training for particular tasks is already approaching that of frontier models"* — benchmark gap closing fast; (b) **Cost**: *"in particular for coding agents, these agents are burning through a ton of tokens really, really fast — open models offer a cheap alternative"*; (c) **Trainability for particular domains**: *"they can be trained for your particular domain... as companies build up a lot of these traces, a lot of these agent runs, how can you use those to improve the model over time?"* — directly setting up the continual-learning section.

**5. Agent identity & auth patterns (~6:01–7:26).** *"How do agents take actions? On whose behalf do they take those actions?"* Two emerging patterns Chase observes — both will coexist:

- **Act-on-behalf-of-user**: agent uses the calling user's credentials; *"if I'm accessing an agent and that agent has access to Slack and I tell it to look up something in Slack, it will use my credentials and it'll have access to whatever I see in Slack. If Julia or a colleague uses it, they might get a different answer because it might see different things."*
- **Fixed-service-account**: *"whoever is interacting with that agent, they will always use that fixed set of credentials, so they'll see the same responses."* Started with OpenAI's GPTs pattern; *"we started to see actually some SaaS providers make it really easy for agents to create their own accounts so that they could have their own fixed set of credentials."*

The forward-looking claim: *"being really, really precise about when to use which one and making that clear to users will be important."* This is the wiki's first articulation of **agent-auth-pattern as a structural product-design choice**, not just an engineering detail.

**6. Continual learning across three layers (~7:26–10:42) — the conceptual centerpiece.** Chase articulates a **three-layer model of any agentic system**, each independently improvable:

| Layer | What it is | Examples |
|---|---|---|
| **Model** | The base foundation model | Sonnet, GLM4, GPT-4 |
| **Harness** | *"The code surrounding the model that connects it to the environment"* | Deep Agents, Claude Code, pi |
| **Context** | *"What we provide to the harness as ways to guide it on particular tasks"* | `agent.md`, skills |

Continual learning worked examples Chase names from stage:

- **Model layer**: Ramp + Prime Intellect fine-tuned **Qwen 3.5** to be really good at Ramp sheets; *"latency is very, very low and the accuracy is very, very high."* The example of why open models matter — they're fine-tunable.
- **Harness layer**: **[[2026-03-30-lee-meta-harness-end-to-end-optimization|MetaHarness]]** (MIT + Stanford) — *"used an agent to optimize a coding harness... outperforms human-written harnesses... it wasn't changing the model at all, it was just editing the harness."*
- **LangChain's own**: *"we moved from top 30 on terminal bench two to top five just by changing the harness itself. So no changes to the model, only changes to the harness, and we saw a big increase in performance."* The third primary-source confirmation of this exact claim, following [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain Engineering blog (10 March)]] and the broader pattern from [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex (11 Feb)]].

**The classical-ML analogy** (~9:20–10:01) — the conceptual move that ties it together:

> *"In classical machine learning, you have the model, you have the training data, you do some gradient descent, and that updates the weights of the model. When you're updating the agent in general, depending on the layer you're at, if you're working at the harness or context layer, it's not exactly gradient descent, but the **evals that you write act as a forcing function**. So in the example of the MetaHarness... those evals are providing a similar type of this training gradient. And so evals and traces are incredibly important for this learning."*

This is the wiki's clearest single articulation of **evals-as-gradient** for non-model layers — a load-bearing framing that ties [[concepts/agent-development-lifecycle|the ADLC's eval phase]] to the continual-improvement substrate of every other phase.

**LangChain Labs and Fleet (~10:42 onward).** Chase announces **LangChain Labs** as a research group inside LangChain *"aimed in particular at continual learning"*; *"LangSmith, with all these traces already in there and all the feedback associated with it, this is a really, really solid foundation for doing this type of continual learning."* Brace Sproul then walks through **LangSmith Fleet** updates: 200+ built-in tools; **first-class Arcade partnership for 7,500+ additional tools**; **MCP support**; native Slack / Gmail / Outlook channel integration; sharing model like Google Docs; auth management; cost tracking and usage controls; first-class human-in-the-loop; built on **deep agents** open-source harness; **downloadable agent files for code modification**.

**Internal-LangChain operational metrics (Caroline di Vittorio's live demo, ~13:40–19:05).** LangChain's own go-to-market agent (built in Fleet without code, integrated with Salesforce / BigQuery / Slack / Gmail) reports:

- **84% of the go-to-market team uses it weekly**
- **Lead-to-qualified conversion up 240%**
- **40 hours saved per rep per month on average**

The agent was *"originally built by an engineer directly in code, but when we built Fleet, we rebuilt this agent directly in Fleet so the go-to-market team could own this agent's implementation entirely end-to-end without having to write a single line of code."* The wiki's first concrete *"engineer-built-it-in-code → rebuilt-it-in-no-code so the domain team could own it"* migration with quantified outcome metrics.

**Closing operational note**: *"We actually added a free model in [Fleet]. For a limited time there'll be a free model — and backing up what we were talking about earlier, it's an open-source model powered by [[Fireworks AI]], one of our fantastic partners here."* The product release is congruent with the open-source-models-rising thesis from the keynote's first half.

**Caveats.** Vendor-CEO keynote on the company's own conference channel; every metric is vendor-cited. The 84% / 240% / 40h GTM-agent claims are unaudited internal LangChain operational data — verifiable only if LangChain publishes the methodology. The two-types and three-layer typologies are predictive frameworks Chase explicitly flags as *"I'm going to be wrong in a lot of these, this is going to look really silly and really stupid"* — treat as forward-looking commitments, not empirical observations. The Top 30 → Top 5 claim was already on the wiki via [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy]] in March; what's new is Chase repeating it as a vendor-CEO stage claim.

## Why this matters in the corpus

This source lands three structural extensions to the wiki's existing LangChain corpus:

1. **The Chase / LangChain anchor doubles.** Prior wiki: one Chase source ([[2026-05-09-chase-agent-development-lifecycle|ADLC, 9 May]]) + three other LangChain-affiliated sources ([[2026-02-17-langchain-improving-deep-agents-harness-engineering|deep-agents-harness Feb 17]], [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy March 10]], [[Y Combinator|Y Combinator]]-channel cross-references). This Interrupt keynote is **Chase's second substantive source** — triggers entity-page promotion per the [[CLAUDE.md|second-source rule]]. LangChain entity: 4 → 5 sources.
2. **The three-layer continual-learning model** (model / harness / context) is the wiki's clearest single articulation of *what continual learning of an agentic system actually means*, complementing [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten/Zhang's academic formalisation]] at the vendor-CEO altitude. Together they bracket the *continual-improvement-of-the-agentic-system* thesis on the academic and product-vendor altitudes.
3. **The Top 30 → Top 5 LangChain claim now has a third primary-source confirmation** — Chase's stage assertion at Interrupt 26 on top of [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy/LangChain blog (10 March)]] and the cohort of corroborating *harness > model* claims (Karten & Zhang, Lee et al. MetaHarness, Pan et al. NLAH). This makes it the **strongest single-claim convergence in the wiki's harness > model corpus** — three independent primary-source citations of the same numerical magnitude.

**Pair with [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]] (one day earlier).** Both Chase and Tan articulate **layered-system decompositions of agent thinking**, landing within 24 hours of each other in late May 2026:

| Source | Axis | Decomposition |
|---|---|---|
| Tan / CS153 (20 May) | **Agentic-primitives → company-structure** | Skills = employees / Resolvers = org chart / GBrain = internal process / Check-resolvable = audit / Trigger evals = performance reviews |
| Chase / Interrupt 26 (21 May) | **Learning-systems → agentic-system-layers** | Model / Harness / Context — each independently improvable, with evals-as-gradient |

Both founders extend the *everyone-builds-agents* corollary: Hu's *AI founder / IC / DRI* org structure (24 April) + Chase's *domain experts will be building agents, not just giving feedback* (this source). The 2026 founder-CEO doctrine is converging on **decompose-the-agent-stack and let-domain-experts-own-each-layer** as the operating posture.

## What was actually ingested

The full ~22:10 transcript was read end-to-end. Manual English captions are available alongside auto-generated; the youtube-transcript-skill picks the manual track when present, which gives noticeably higher transcript quality than the YC Root Access yt-dlp fallback batches earlier in this session. Speaker transitions are clearly marked in the transcript (Chase → Sproul at ~17:38 via *"Now, I'm going to hand it off to Caroline"* — though actually Brace hands off *back* to Caroline at 17:46; minor mid-keynote handoff confusion noted in the body).

Two ASR-style spellings to flag (despite manual captions): *"LinkedIn"* at 0:41 is almost certainly *"LangChain"* (Chase saying *"one of the things that we think a lot about at LangChain — it's actually in our mission and vision statement"*) — likely a transcription mis-edit or punctuation artifact. *"GLM4"* (referring to the Zhipu/THUDM open model) and *"Qwen 3.5"* (Alibaba open model) are spelled correctly. The chapter `start_ms: 0` fields in raw frontmatter remain a known YouTube-metadata bug — the build script's chapter-interleaving parses the `start:` string instead.

## Linked entities and concepts

**Entities promoted by this source:**

- [[LangChain]] — already entity (4 sources); bumps to 5 with new section on the Interrupt 2027 keynote and the three-layer continual-learning model.
- **[[Harrison Chase]] promoted from Dangling to entity page** — this is his second substantive source (first: [[2026-05-09-chase-agent-development-lifecycle|ADLC, 9 May]]). New entity page filed.

**Dangling — single-source mention, deferred:**

- **Brace Sproul** — LangChain (product walkthrough segments 11–13). First wiki mention.
- **Caroline di Vittorio** — LangChain (live Fleet demo segment). First wiki mention.
- **LangChain Labs** — new research group announced; first wiki mention.
- **LangSmith Fleet** — already named on the [[LangChain]] entity page; this source quantifies its operational metrics (84% weekly usage on internal GTM agent, etc.).
- **LangSmith Engine** — referenced in the description's *"extra resources"* link; not substantively discussed in the talk body.
- **Fireworks AI** — open-source model partner powering Fleet's free-tier model. First wiki mention.
- **Arcade** — tool-integration partnership (7,500+ tools beyond Fleet's 200+ built-ins). First wiki mention.
- **Ramp** + **Prime Intellect** — named on stage as the Qwen-3.5-fine-tuning collaboration; first wiki mentions.
- **Pied Piper account** — Caroline's demo CRM example (named after the Silicon Valley HBO show); not promoted.

**Concept pages touched:**

- [[concepts/agent-harness]] — adds the **three-layer continual-learning model** (model / harness / context) as a structural sub-decomposition of the harness concept itself; adds the *evals-as-gradient* framing for harness-and-context-layer improvement; adds the third primary-source citation of the Top 30 → Top 5 LangChain Terminal Bench 2 claim.
- [[concepts/agent-development-lifecycle]] — extends the *Build* phase with the two-types-of-agents typology (long-horizon vs customer-experience); extends the *Eval* phase as the structural source of the *gradient* for continual learning on harness and context layers; the LangChain Labs announcement is the vendor commitment to continual learning as a first-class lifecycle phase.
- [[concepts/ai-agents]] — adds the two-types-of-agents structural typology (long-horizon vs customer-experience) — orthogonal to existing taxonomies; useful for product-design framing.
- [[concepts/enterprise-ai-adoption]] — adds the *domain-experts-building-agents-not-just-giving-feedback* thesis at the vendor-CEO altitude; the *rebuilt-in-Fleet-so-the-domain-team-could-own-it* migration is a worked example of the no-code-layer enabling org-design shift Hu and Tan articulate from the accelerator-CEO altitude.
- [[concepts/foundation-models]] — adds the *rise of open-source models* three-driver framing (capability / cost / trainability for particular domains); names the Fireworks AI partnership as the open-model commercial-deployment surface.

## Source quality

- **Channel**: [[LangChain]] official YouTube — vendor channel; conference keynote format.
- **Format**: ~22-minute three-speaker keynote with a live demo; manual English captions (highest-quality transcript source in the wiki's video-ingest pipeline).
- **Empirical anchors**: LangChain's own GTM-agent metrics (84% weekly usage / 240% lead-to-qualified / 40h saved per rep per month) are vendor-cited and falsifiable only by LangChain. The Top 30 → Top 5 on Terminal Bench 2 claim is now anchored across three independent primary sources (Trivedy March 10, Chase Interrupt 26 stage assertion, and the cohort of *harness > model* corroborating papers).
- **Bias / motive**: Vendor-CEO keynote on the vendor's own conference channel. Read every forward-looking claim (two-types typology, voice future, sandbox necessity, open-models rise, identity/auth patterns, continual learning) as a **bet LangChain is making and product-strategising around** — useful as forward-looking-intent data, not as neutral observation. The Fleet metrics are LangChain-internal and would benefit from a third-party comparison.
- **Transcript provenance**: youtube-transcript-skill (Playwright path); manual English captions automatically preferred over ASR; first ingest in this session where the Playwright path succeeded on first attempt without yt-dlp fallback.
