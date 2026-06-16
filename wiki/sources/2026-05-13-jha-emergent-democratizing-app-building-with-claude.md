---
type: source
kind: video
title: "How Emergent is making app building more accessible with Claude"
author: ["Claude"]
publisher: "Anthropic (Claude YouTube channel — startup customer story / Applied AI interview)"
url: "https://www.youtube.com/watch?v=IGAVa4uyo2w"
date_published: 2026-05-13
date_ingested: 2026-05-20
length: "~16:39 minutes (auto-generated English captions, ASR-cleaned, 135 segments)"
raw: "../../raw/videos/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md"
tags: [emergent, mukund-jha, carly-ryan, anthropic, y-combinator, dunzo, agent-harness, multi-agent-systems, agentic-engineering, vibe-coding, opus, claude-code, container-technology, long-term-memory, refactoring-agent, security-agent, test-time-compute, dev-shop-replacement, small-business, democratization, wingman, 100m-arr, 7m-users, customer-story]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
  - contextual/external-triggers
confidence: 0.7
last_confirmed: "2026-05-20"
accessed_at: "2026-05-20"
relationships:
  - type: supports
    target: agent-harness
    via: "Direct practitioner naming of the harness construct as the locus of product differentiation: *'agent is the product right in many ways and like the harness quality really really matters'* (~5:48) and *'our agent quality, the harness quality is really really strong and it's continuously evolving'* (~10:04). Emergent owns the full stack — container tech, multi-agent orchestration, long-term cross-session memory, pre/post-deploy security agents, refactoring agent — and frames *that whole envelope* as the harness. Strongest founder-vantage anchor the wiki holds on the harness-as-competitive-moat thesis."
  - type: supports
    target: agentic-engineering
    via: "Practitioner-side instantiation of the agentic-engineering discipline at startup scale: *test-time compute, agent-to-agent communication, multi-agent productionisation, container-tech with disk/memory snapshotting for parallel agents, long-term memory across user sessions, refactoring + pre-deploy + post-deploy security agents.* Pair with [[2026-05-08-running-an-ai-native-engineering-org|Fiona Fung's Anthropic-internal view]] — Emergent is the external-product expression of the same discipline."
  - type: supports
    target: vibe-coding
    via: "Named-company anchor for the *democratisation-of-software-creation-via-natural-language* thesis: *7M users in 190 countries, 70–80% never wrote a line of code,* serving business operators / domain experts who *'really really understand their domain really well but never had the tools to express themselves.'* Headline anecdote (Christy, Alaska psychologist + equestrian coach, ships *Equ* on the App Store after a $50K dev shop in Nova Scotia couldn't deliver) is one of the cleanest *new-user-class-now-possible* vignettes the wiki holds."
  - type: supports
    target: automation-vs-augmentation
    via: "Sits hard on the *automation* leg: Emergent users are *not* augmenting an existing dev team — they're replacing the dev-shop alternative (CEO names the comparison: *'a $250,000 price point that they would have paid if they had gone and and hired a dev shop'*). The augmentation pattern of Lyft and HubSpot fits the wage-labour side of the workforce; Emergent's pattern fits the *small-business-can-now-self-serve* side of the same shift."
  - type: supports
    target: 2026-02-06-figma-make-prompts-to-prototypes-with-claude
    via: "Same year (2026), same democratisation-of-building thesis, different audiences: Figma Make targets designers escaping the design-to-code handoff; Emergent targets non-technical business operators shipping production apps. Pair as *two practitioner instances* of the same Claude-channel narrative."
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "Anthropic-internal (Fiona Fung) vs Anthropic-external (Emergent) view of the same agentic-engineering discipline. Fung describes the *team-norms rewrite* inside Claude Code; Jha describes the *product-stack rewrite* outside, building the same kind of harness for a different user-class. Both name *the harness as load-bearing* and both rewrite their systems against each new model-class."
  - type: supports
    target: 2026-04-25-masad-replit-ceo-only-two-jobs-left
    via: "Direct category-peer — Replit and Emergent are the two named-CEO 2026 anchors the wiki holds on *natural-language-to-production-app* platforms serving non-developers. Masad: *'the people getting the most value aren't traditional devs but founders and domain experts closest to the problem'*; Jha: *'business operators who really really understand their domain really well but never had the tools to express themselves.'* Same product category, same user-class thesis, complementary technical-architecture stories (Replit on its own Agent N stack; Emergent on Claude + own multi-agent harness on Kubernetes). Read together as the wiki's *two-vantage anchor* on the AI-native app-building category."
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "Emergent operationalises Karpathy's *agentic engineering* discipline at startup-product scale. Karpathy's December-2025 phase-change (*'I just trusted the system more and more'*) is the wiki's foundational anchor; Jha's *'rewritten our systems like four times over 9 months'* is its company-stack analogue, and the *'agent is the product, the harness quality really really matters'* framing is the production-side restatement of Karpathy's discipline-distinction between vibe-coding and agentic-engineering."
  - type: supports
    target: enterprise-ai-adoption
    via: "Counter-case to the slow-enterprise-adoption framing: Emergent reached *$100M ARR in 8 months* by serving non-enterprise (SMB + entrepreneur + domain-expert) users. CEO names the deliberate enterprise → consumer/SMB pivot after observing that *'adoption in enterprise is going to be slow'* — the wiki's clearest 2026 named instance of *adoption-velocity asymmetry favouring the long tail*."
---

# How Emergent is making app building more accessible with Claude — Mukund Jha (Emergent CEO) interviewed by Carly Ryan (Anthropic Applied AI)

> Emergent reached $100M ARR in eight months, with 70–80% of users having never written a line of code. In this conversation, Co-founder and CEO Mukund Jha sits down with Anthropic's Carly Ryan to talk about the technical decisions behind building on Claude and how Emergent thinks about durability in a category moving this fast.
>
> Read the full story: claude.com/customers/emergent
>
> *— [Claude YouTube channel description](https://www.youtube.com/watch?v=IGAVa4uyo2w)*

A **~17-minute Applied-AI-team interview** on the [[Anthropic]] Claude channel (published **13 May 2026**), between **Mukund Jha** (CEO and co-founder of **Emergent**) and **Carly Ryan** (Anthropic Applied AI team, startups). Format is a two-person studio conversation — much more substantive than the typical Claude-channel customer testimonial — and reads as a founder-vantage anchor on the *agent-harness-as-product* thesis at scale. The underlying long-form customer story is at `claude.com/customers/emergent`.

This source's structural value: it pairs [[2026-05-08-running-an-ai-native-engineering-org|Fiona Fung's *inside-Anthropic team-norms rewrite*]] with the **outside-Anthropic product-stack rewrite** that the same discipline produces for a different user-class. Where Fung names what Claude Code's team had to rewrite to ship the 10×-plus product, Jha names what Emergent had to rewrite — *four times in nine months* — to ship the *natural-language → production-ready app* product for **7M users across 190 countries**, **70–80% of whom never wrote a line of code**.

## TL;DR

Seven contributions to the wiki's running picture of agentic engineering at scale:

1. **The headline numbers.** *$100M ARR in 8 months. 7M users in 190 countries. 70–80% have never written code. Deployment success rate 84% (a few months ago) → 98% today.* The growth numbers are vendor-cited and unaudited; the *deployment-success-rate-as-product-quality-metric* framing is the more durable wiki contribution — it's the *outcome metric* a coding-agent harness team manages to.
2. **The harness, named.** *"Agent is the product right in many ways and like the harness quality really really matters"* (~5:48). *"Our agent quality, the harness quality is really really strong and it's continuously evolving"* (~10:04). The wiki's clearest **founder-vantage** anchor on harness-as-product-moat — to set alongside [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] / [[2026-05-15-osmani-agent-harness-engineering|Osmani]] / [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe]]'s engineering- and eval-side framings.
3. **Why own the whole stack.** *"To really really build an automated software engineering platform, you will have to own every layer of the stack, [...] and you have to almost co-build the infrastructure to support your agent and an agent to sort of support the infrastructure."* Concrete instances: **container tech built on Kubernetes with disk-snapshotting and memory-snapshotting** so agent states can be saved and parallel agents can run; **agent-to-agent communication**; **multi-agent system productionisation** (one of the first teams to do so); **long-term memory** *across* user sessions (not just within a session) so the agent learns from *every* error / library upgrade seen across the platform.
4. **Pre-deploy / post-deploy / refactoring agents — security and durability as agent-level concerns.** *"We have a refactoring agent that'll come and refactor your app. We have a post-deployment agent and a pre-deployment agent that'll check for all security flaws. They'll sort of make sure that there are no key leakages [...]. Approaching the problem from the outcome-first perspective allows us to sort of really design the system for that."* Practitioner-side enumeration of the *Swiss-cheese* agent-stack that [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's eval taxonomy]] anticipates from the evaluation side.
5. **Index on highest reasoning, not speed or cost. Opus as workhorse.** *"For us being on the frontier the the highest reasoning possible is is something that we sort of index a lot on internally. We index a lot on like just highest quality output versus you know the fastest output. [...] Opus has been sort of our workhorse [...] really great at instruction following and if you have the right tight feedback loops [...] you can actually keep them running for a much longer time. Today our agents can run for hours trying to build the software."* Counters the *"frontier-quality is too expensive, use a cheaper model"* default: when users are comparing the output to a **$250K, 3-month dev-shop project**, neither price nor latency is the binding constraint — outcome quality is.
6. **The user class is not who Emergent expected.** *"When we started we thought that we were building for mostly like semi-technical users, program managers, product managers, designers. But we were surprised to see [...] a lot of our users were actually business operators who were using us to build serious applications."* Headline vignette: **Christy, a clinical psychologist and equestrian coach in Alaska**, had paid $50K to a Nova Scotia dev shop for an app that didn't work; switched to Emergent and shipped *"Equ"* on the App Store with *"hundreds of users"* today. *"She had been waiting for 10 years to sort of marry these two fields."* Small-businesses-as-domain-experts: *"70% of employment, 50% of GDP — they've never had the tools [...] for the first time you can actually serve all of these million niches at zero marginal cost."*
7. **The next step is *Wingman* — agents-for-business-operations, not just code.** *"We are very soon launching a new product. It's called Wingman. It's kind of agents for businesses and it's going to automate all of your business processes including finances, including operations, sales, marketing. 2026 is going to be year where people start automating large part of their businesses."* The wiki should track Wingman as a forthcoming proof point on the *agent-coordination-for-business-process-automation* thesis — adjacent to [[concepts/industrial-ai-agents|industrial-ai-agents]] but consumer-business-facing.

## Why this matters (for the wiki)

- **The harness-as-product-moat thesis gets its strongest founder-side practitioner anchor.** Chatterjee, Kokane, Osmani, Wolfe, and the broader [[concepts/agent-harness|agent-harness]] cluster have established the thesis from the engineering- and eval-side; Emergent supplies the *company-built-on-it-is-now-doing-$100M-ARR* practitioner data point. The wiki had been missing a *named-startup* anchor at this scale.
- **Adoption-velocity asymmetry favouring the long tail** is named explicitly. The pivot from *first launched as enterprise-targeted → research preview in June → exploded with SMB / non-coder users* is the wiki's clearest 2026 vignette of the *adoption-velocity-asymmetry* claim — that the *fastest-adopting* AI customers in 2026 are not Fortune 500 enterprises but the long-tail of SMBs / domain experts / business operators who *never had software at all*. Sits in productive tension with [[2026-04-28-mittri-cisco-ai-enabled-enterprise|Cisco's *AI-enabled enterprise*]] and [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar/Nohria's *end of one-size-fits-all*]] enterprise-adoption framings.
- **The *vibe-coding democratisation* concept page now has its strongest 2026 named-company anchor.** [[concepts/vibe-coding|vibe-coding]] previously rested on [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's foundational framing]] and Anthropic's internal usage; Emergent supplies the *user-class-now-possible* data the concept was waiting for. Direct category-peer to [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad/Replit]] — the two named-CEO 2026 anchors the wiki now holds on *natural-language-to-production-app* platforms (Masad: *"the people getting the most value aren't traditional devs but founders and domain experts closest to the problem"*; Jha: *"business operators who really really understand their domain really well but never had the tools to express themselves"*).
- **The *every-new-model-class-delete-and-reimagine* discipline** is a small but important contribution to the [[concepts/agentic-engineering|agentic-engineering]] page. Jha: *"My belief has always been that every time like a new class model shows up, let's delete everything we have done. Let's reimagine the world from this lens of the new model. So we have rewritten our systems like four times over 9 months."* Same operational pattern as Fung's *"What may have served you prior may not serve you any longer."*
- **Carly Ryan's *moats that intelligence alone can't overcome*** triplet (deep user understanding, proprietary infrastructure / regulated-space barriers, human trust) is a compact framing the wiki can reuse when discussing *durable defensibility* in AI-native categories. Closest existing wiki cousin is [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath at Stanford AI Club]]'s *complex-reliability-bottleneck* thesis.

## Selected quotes

On agent-harness as the product:
> *"For us what's been sort of really really insightful has been that agent is the product right in many ways and like the harness quality really really matters."* (~5:48)
>
> *"Our agent quality the harness quality is really really strong and it's continuously evolving."* (~10:04)

On owning the whole stack:
> *"To really really build an automated software engineering platform, you will have to own every layer of the stack. [...] We had to actually invent and build sort of our own container technology on top of Kubernetes which does disk snapshotting, memory snapshotting. So you could actually save the states and run parallel agents."* (~5:32)

On long-term memory across sessions:
> *"We also have built this what we internally call long-term memory where an agent is not just learning from within the user session, but is learning across all of the apps that are getting built. So first time it sees an error, a new error or a new library upgrade, it's able to learn that and sort of do that in the next iteration in much less tokens with much more accuracy."* (~6:44)

On indexing on quality, not cost:
> *"They're not price sensitive. They're also not like latency sensitive that much because they're comparing us to a 3 months project that would have been executed outside. [...] For us being on the frontier the the highest reasoning possible is is something that we sort of index a lot on internally."* (~8:00)

On the user class:
> *"We are building for like small businesses today. Small businesses globally account for 70% of employment, accounts for like 50% of GDP of the world. But they've never had the tools to sort of really express themselves because like there are million niches in small businesses. But for the first time with AI, you can actually serve all of these million niches at zero marginal cost."* (~14:54)

On rewriting against every new model class:
> *"My belief has always been that every time like a new class model shows up, let's delete everything we have done. Let's reimagine the world from this lens of the new model. [...] We have rewritten our systems like four times over 9 months."* (~13:13)

On Carly Ryan's moat triplet:
> *"Moats that intelligence alone can't overcome. [...] Proprietary data or infrastructure, building in a highly regulated space [...] AI is not going to automate compliance regulation fully soon. The final one is like human trust — anywhere like human trust is not something that's going to be automated soon."* (~12:02)

## Dynamic-capabilities reading

- **`digital-seizing/rapid-prototyping`** — Emergent's product *is* the rapid-prototyping cell, productised: natural-language → deployed production app in one user-facing motion. The 98%-deployment-rate metric is the rapid-prototyping cell's outcome measure made explicit.
- **`digital-seizing/strategic-agility`** — *"rewrote our systems four times over 9 months"* and the deliberate enterprise → SMB pivot after observing slow enterprise adoption. *Rapidly reallocating resources; accepting redirection and change; pacing strategic responses* in textbook form.
- **`digital-seizing/balancing-digital-portfolios`** — the enterprise → consumer/SMB pivot is a portfolio-rebalancing move; the *Wingman* business-operations-automation product launch is a second portfolio bet adjacent to the core coding-agent product.
- **`digital-transforming/improving-digital-maturity`** — Emergent's external value proposition *is* the digital-maturity uplift of its users (SMBs, domain experts) who *"never had the tools to express themselves."*
- **`strategic-renewal/business-model`** — the value-creation logic of *coding-agent-as-dev-shop-replacement* is genuinely new; users compare Emergent's output to a $250K / 3-month dev-shop project, not to an IDE or a low-code tool. The pricing model and the user expectation are both refreshed.
- **`contextual/external-triggers`** — the *frontier-model-makes-longer-horizon-agents-possible* trigger is named explicitly: *"Opus like really feels like a different class of model and much more capable of longer horizon task especially like now we can have multiple agents coordinating on the same task."*

## What was actually ingested

Full ~16:39 auto-generated English transcript (135 cleaned segments), ASR-cleaned for proper-name fixes (*Mukund, Madhav, Dunzo, Equ, multi-agent, moats, Emergent*) and the *N-minutes-M-seconds* accessibility prefix that some auto-captions leak. Channel description rendered as the leading blockquote. Underlying long-form customer story at `claude.com/customers/emergent` not fetched.

## Linked entities and concepts

- Entities mentioned: [[Anthropic]], [[Y Combinator]]. **Dangling** (single-source mention, deferred per second-source promotion rule): **Mukund Jha** (CEO, Emergent), **Madhav Jha** (twin brother, co-founder), **Carly Ryan** (Anthropic Applied AI team, startups vertical), **Emergent** (company), **Dunzo** (Jha's prior company; ~500 person engineering team).
- Concept pages touched: [[concepts/agent-harness]], [[concepts/agentic-engineering]], [[concepts/vibe-coding]], [[concepts/automation-vs-augmentation]], [[concepts/enterprise-ai-adoption]], [[concepts/ai-agents]].

## Debates and supersession

- **Open tension with the *enterprise-leads-AI-adoption* assumption** — Emergent's growth shows the *fastest* 2026 AI deployment patterns may be in the SMB / non-coder long tail, not in the enterprise. Worth carrying as a productive tension on [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] rather than as a supersession of the slower-enterprise framings.
- **Open tension with the *Build cheaply, optimise quality later* heuristic** — Emergent indexes on highest-reasoning frontier models because user expectations are anchored to a *$250K, 3-month* dev-shop alternative. This **reverses** the typical SaaS *use-the-cheapest-good-enough-model* default. Worth flagging in any future synthesis on *model-selection criteria across deployment contexts*.

## Related pages

- [[2026-04-25-masad-replit-ceo-only-two-jobs-left]] — direct category-peer; same natural-language-to-production-app product space.
- [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] — foundational anchor on the vibe-coding / agentic-engineering discipline this source operationalises at company-scale.
- [[2026-05-08-running-an-ai-native-engineering-org]] — Anthropic-internal counterpart on the same agentic-engineering discipline.
- [[2026-05-07-chatterjee-anatomy-of-agent-harness]], [[2026-05-07-kokane-agent-harness-vs-systems-design]], [[2026-05-15-osmani-agent-harness-engineering]], [[2026-05-18-wolfe-agent-evaluation-detailed-guide]] — engineering- and eval-discipline framings of the harness construct that this source supplies a founder-vantage practitioner anchor for.
- [[2026-02-06-figma-make-prompts-to-prototypes-with-claude]] — incumbent-side companion on the same democratisation thesis.
- [[2026-02-18-lyft-customer-support-with-claude]], [[2026-02-09-hubspot-customer-success-with-claude]] — same Claude-channel customer-story series.
- [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]] — the *decouple brain from hands* framing aligns with Emergent's multi-agent productionisation.
- [[2026-05-09-chase-agent-development-lifecycle]] — adjacent agent-lifecycle framing.
- [[concepts/agent-harness]], [[concepts/agentic-engineering]], [[concepts/vibe-coding]], [[concepts/enterprise-ai-adoption]], [[concepts/automation-vs-augmentation]] — the concept pages this source extends.
