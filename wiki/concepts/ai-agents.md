---
type: concept
aliases: ["AI agent", "AI agents", "agentic AI", "autonomous agents", "agent", "agents"]
tags: [ai-agents, agentic-ai, generative-ai, automation, ai-deployment]
confidence: 0.95
last_confirmed: "2026-05-21"
accessed_at: "2026-05-21"
source_count: 16
relationships:
  - type: instance-of
    target: generative-ai
    via: "agents are the orchestrating tier on top of LLM-based GenAI"
  - type: uses
    target: foundation-models
quality_score: 0.67
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)', '6 broken body wikilink(s)']
---

# AI Agents

Software systems that **pursue complex goals autonomously**, with independent decision-making, planning, and adaptable execution in dynamic environments — typically built on top of [[foundation-models]] with tool-use, memory, and orchestration scaffolding. Agents are distinct from chatbots (which simulate conversation) and from multi-agent systems (which coordinate multiple agents).

As of 2024–2025, agents have moved from research-grade demos to **early enterprise deployment**, with growing convergence on a 3-stage progression and on the kinds of tasks where agents are economically viable today. By April–May 2026 the wiki's sources also converge on a **runtime-engineering** vantage: the [[agent-harness]] (the wrapper around the model) drives more performance variation than the model itself — see [[2026-05-04-rethinking-agents-harness-is-all-you-need|the empirical anchor]] showing same-model 6× variance and harness optimisations transferring across model families. [[Andrej Karpathy]]'s practitioner framing in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]] (29 April 2026) names the discipline that wields all this — [[agentic-engineering]] — and frames agents themselves as **intern entities**: *"remarkable, but you basically still have to be in charge of the aesthetics, the judgment, the taste, and a little bit of oversight."* The intern-entities framing is now the wiki's working idiom for *what kind of workforce* agents constitute.

## Working definition

The cleanest definition in this wiki comes from [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]'s 3-stage progression:

| Stage | What it is | Examples |
|---|---|---|
| **AI chatbot** | Simulates and processes human conversation, written or spoken | Customer support FAQ bots; ChatGPT in default mode |
| **AI agent** | Pursues complex goals autonomously, with independent decision-making, planning, and adaptable execution in dynamic environments | Salesforce Agentforce (business operations); Italgas DANA (network control); coding agents |
| **Multi-agent system** | Multiple AI agents collaborate to pursue complex goals autonomously in dynamic environments | (Emerging — fewer production examples as of 2025) |

A useful complementary lens is the [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] 2×2: agents thrive in the **"no regrets zone"** (low cost of errors + explicit data) where AI does the work without humans in the loop — addressing bulk customer inquiries, summarizing documents, screening résumés. As error costs rise, agents become assistants rather than autonomous executors.

The simplest one-sentence operational definition — adopted by the wiki from [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]] (citing the Simon Willison formulation): ***"an agent is an LLM that autonomously uses tools in a loop."*** This is the *agentic loop* that wraps every agent system: an LLM at the centre reasons about the task, calls **tools** to read/write external state, observes results, and continues until an exit condition is reached. Three components are always present: (1) the underlying LLM or reasoning model, (2) tools the agent calls (APIs / CLIs / [[MCP]] servers / computer-use primitives), (3) instructions in the system prompt that specify the agent's expected behaviour. The [[agent-harness|harness]] is what assembles those three components into a runtime.

## Key claims

### The 2024–25 inflection

- **Salesforce launched Agentforce** in September 2024 — a suite of autonomous AI agents for business operations across the Salesforce platform. Source: [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.1 timeline.
- **>80% of organizations plan to integrate AI agents within 1–3 years** ([[Capgemini]] research via [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]).
- **AI agents could double the capacity** of knowledge professionals and field-support roles ([[PwC]] prediction via MITTRI/Cisco).
- [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]'s Four Stages framework places "exploring autonomous agents" as a **Stage 3** (Develop AI ways of working) attribute, and "combining traditional + generative + agentic + robotic AI" as a **Stage 4** (Become AI future-ready) attribute. Stage 4 covers only **7%** of firms (2022 baseline) — agents at scale remain rare.

### Capability evidence (RE-Bench, 2024)

[[2026-04-28-ai-index-report-2025|AI Index 2025]] §2 discusses **RE-Bench** — a 2024 benchmark for evaluating complex tasks for AI agents under time budgets:
- In **2-hour budgets**: top AI systems score **4× human experts**.
- At **32-hour budgets**: humans win **2:1** over AI.
- AI agents already match human expertise on select tasks (e.g., writing Triton kernels) — at lower cost and higher speed.

The time-budget pattern is a sharp framing: **agents win at short horizons, humans still win at long horizons.** Most enterprise tasks have short horizons, which is why agent deployment is accelerating despite long-horizon weakness.

### Where agents are deployed in 2024–25

- **Salesforce Agentforce** (cross-functional enterprise agents)
- **GitHub Copilot** family (coding assistance evolving toward agents) — see [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]]
- **Harvey** (legal contract drafting) — Anand-Wu cite it for the "quality control zone"
- **Italgas DANA** — generative-AI-based network control system for natural gas distribution. Source: [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan]].
- **Cisco's customer-support agents** — Cisco internal deployment per [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]].
- **Claude Code** ([[Anthropic]]) — agentic coding harness now leaving a *measurable* signature in usage data: per the [[2026-05-07-anthropic-economic-index-5-learning-curves|fifth Anthropic Economic Index report]] (Feb 2026), the 1P API task-share for "Computer & Mathematical" jumped from 36% (Aug 2025) to 47% (Feb 2026), driven in large part by coding agents that decompose work into many shorter task-labelled API calls. Where Claude.ai shows a single user-Claude conversation per task, an agentic harness shows up as N labelled calls per task — agents are visible in the data, not just in product launches.

### The application-layer counterpart: the agent harness

Throughout April–May 2026 a body of practitioner writing converged on **[[agent-harness|agent harness]]** as the dominant frame for production-grade agent engineering at the application layer — *complementary* to Anthropic's brain/hands/session at the platform layer. Two new wiki sources name the construct directly:

- [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] — provocation-style argument that "agent harness" is mostly **systems design we've always done** with a 10% genuinely novel kernel (non-determinism at the execution layer + context as a degrading resource). 4-layer stack: Your App / Harness Frameworks (LangChain, Microsoft Agent Framework, Google ADK, LlamaIndex, CrewAI, Haystack, DSPy) / Agent Harness Runtime / swappable Model Layer.
- [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] — taxonomical 4-layer anatomy: **Context** (system prompt as a document, KV-cached stable parts + dynamic parts) / **Constraints** (pre/post-tool middleware: destructive-verb detection, workspace isolation, loop detection, output scoring) / **Contracts** (formal evaluable specifications of "successful output" calibrated to inputs) / **Compounding** (telemetry as training data for the harness itself, with human-reviewed workspace overrides).

The full treatment of the harness construct lives in the dedicated [[agent-harness]] concept page; this section flags the connection from the [[ai-agents|ai-agents]] page.

**Worked failure mode worth flagging here**: Chatterjee's *Friday-in-March* story — a user said "clean things up before the board review"; the agent — *competent, helpful, working exactly as designed* — interpreted this as archive stale documents + prune duplicates + remove stale sources, soft-deleting two weeks of research history 40 minutes before a board meeting. **The model was not the problem.** The problem was the absence of an intent-validation layer in the harness. The lesson generalizes: **most agent failures in production are harness failures, not model failures.**

**Practitioner consensus on the implication**: build constraints before you build cleverness; the model is rented and replaceable; the harness is owned and compounds.

### Engineering pattern: brain / hands / session decoupling

The [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] engineering post (8 April 2026) names the architecture beneath production-grade agents — the layer the working-definition table abstracts over. Three concerns are deliberately split into independently-scaled tiers:

| Tier | What it is | Why decoupled |
|---|---|---|
| **Brain** | The model + tool-use/reasoning loop | LLM inference is bursty and stateless; scale on its own clock |
| **Hands** | Tool execution surface (code interpreter, browser, MCP servers, file system) | Each tool has its own latency, blast-radius, and security profile; isolation per-tool is mandatory |
| **Session** | Long-running orchestration state — memory, conversation history, intermediate artefacts that outlive any one model call | A *session* is **not** the same as the model's context window: sessions can run for hours and span context resets |

Two consequences worth marking:

- **Security as structural unreachability, not as policy.** The hands tier runs in a sandbox the brain cannot directly drive — the model emits tool-call requests, and a separate executor decides whether and how to run them. This is the engineering version of the [[responsible-ai|"agent risk"]] story: rather than relying on the model to *refuse* dangerous actions, the architecture makes most dangerous actions structurally unreachable.
- **"Context anxiety" is model-specific.** The post observes that [[Claude Sonnet 4.5]] sometimes wraps up tasks prematurely when its context window fills — a failure mode not present on **Claude Opus 4.5** under the same harness. This is the first empirical evidence in this wiki that long-horizon agent reliability varies by model within a family, not just across families. It also reframes the RE-Bench 32-hour finding: long-horizon weakness is partly an **architectural** problem (context window saturation) and partly a **model-quality** problem (how the model responds when saturation looms).

### Capgemini's expected agent benefits (n unknown, sponsor-cited)

| Expectation | % agreeing |
|---|---|
| AI agents will help drive higher levels of automation in workflows | 71% |
| AI agents will significantly improve customer service, leading to improved satisfaction | 64% |
| AI agents would help me focus on more value-added activities | 64% |
| The potential of AI agents to improve productivity outweighs the risks | 57% |

Source: [[Capgemini]] 2025 via [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]. **Caveat:** the 57% on "outweighs the risks" is the lowest-scoring item — material minority concern.

### The CX angle

Customer experience (CX) is the most-cited near-term agent application. Per [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]:
- Customers are **3.8× more likely to purchase again** following a successful service experience.
- "It's not about replacing roles. It's about where we can give agency, with some human oversight and governance, to improve tasks within a workflow." — [[Liz Centoni]], EVP & Chief CX Officer, [[Cisco]].

### Agentic commerce at consumer scale (China, May 2026)

The MITTRI/Cisco / Anand-Wu *agents-as-strategic-aspiration* framing assumes agents are still inching past the demo phase in production environments. [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni's E-commerce Berlin Expo keynote]] supplies the **first wiki source naming agentic-commerce systems deployed at consumer scale today with revenue lines attached**:

- **Alibaba's Qen one-sentence-purchase agent** — *"Book me a cool hotel in Hangzhou and the train to get there, and buy me an umbrella or a hat depending on the weather."* Served via Alibaba's integrated ecosystem (Fliggy travel + map + weather + e-commerce + payment) with **tokenized mandates** as guard rails. **More than 100 million users today** — *"not a test, something live and getting actually used."*
- **JD.com's Joy Streamer** — virtual digital-twin live-stream hosts replacing human KOLs (key-opinion-leaders) on JD's e-commerce platform. **2.3 billion RMB (~$250M) in sales during the last Double 11 (11 November) season; more successful than 80% of human hosts.** A deployed agentic system at material revenue scale.
- **Alibaba's AQ (Accio)** — an agent that builds physical supply chains end-to-end: market research → design suggestions → supplier match → cross-language chat (German↔Mandarin with Alibaba's translation-quality guarantee as the liability anchor) → executed contract. The Christmas-slippers worked example.

The wiki's prior position on agents was *"early enterprise deployment / mostly aspirational at consumer scale."* Ognibeni's evidence shifts that to: **at consumer scale, agentic commerce already runs at 100M+ DAU with named revenue lines — outside the Western/Anglophone press's habitual reading view.** The mechanism that made this deployable: not better models, but **trust-scaling mechanisms** (Alibaba's liability-shift on translation accuracy; tokenized mandates as guard rails) that make consumers comfortable letting agents execute irrevocable transactions.

### Agents as strategic threat to incumbent customer relationships (May 2026)

[[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells|Scott Price (DFI Retail Group, May 2026)]] supplies the **first wiki source naming a CEO-level public-record articulation of agentic AI as a strategic threat** — not from the *will-it-take-my-team's-jobs* angle but from the *will-it-take-our-customer-relationship-and-the-data-and-loyalty-that-come-with-it* angle:

> *"The one thing that probably keeps me up at night a little bit on this AI is disrupting the traditional approach to digital. So, agentic AI and creating a personal assistant — the idea that an individual will have a relationship with an agentic personal assistant that says, 'Look, I need eggs. I want an appointment with the dentist and can you make sure there's a car ready to pick up the kids at 9 a.m.' And the reality is that basically disrupts the relationship that each one of those service providers has with customers today. With that goes loyalty, with that goes access to data. So there is going to be this arms race for retailers to understand in that agentic world, how do you ensure you maintain that relationship with the customer."*

This is the **seller-side mirror** of Ognibeni's buyer-side warning that *"nobody will show up in your store when you only do search-driven e-commerce."* The same disintermediation thesis, from opposite sides of the buyer/seller table — and the wiki's clearest paired articulation of the *agents-as-disintermediator-of-existing-channels* claim. Track which retailers, banks, and service providers actually publish concrete *agentic-AI-integration playbooks* (vs press-release-only AI investments) within 12–18 months.

### Agents in cybersecurity reconnaissance (May 2026)

[[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] names **"AI-Augmented Offensive & Defensive Security"** as an emerging 2026 category in which LLMs and AI agents are integrated with [[osint|OSINT]] platforms to correlate sources, identify exposures automatically, generate attack graphs, and automate reconnaissance workflows. This is the wiki's first source citing agents in a **cybersecurity/[[attack-surface-management]]** application — distinct from the coding-agent, enterprise-workflow, and agentic-commerce clusters that dominate the wiki's existing agent corpus.

The claim is currently at vendor-narrative depth (no benchmarks, no named systems, no failure modes). Worth tracking: does OSINT become the first defensive-security domain to operationalise autonomous-agent workflows at scale, ahead of more cautious internal-IT use cases? The article asserts yes; the wiki has no empirical anchor yet either way.

## Debates / contradictions

- **Where in the org does an agent sit?** The 4 sources frame agents differently:
  - [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]: agents as a **Stage 3+ attribute** — only mature orgs are exploring them.
  - [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]]: agents as a **task-quadrant attribute** — they thrive in the no-regrets zone today, regardless of org maturity stage.
  - [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]: agents as the **near-term productivity story for everyone** (>80% planning integration in 1–3 years).
  Reconciling: agents are *deployable today* in low-cost-of-error / explicit-data domains, *strategic* at higher maturity, and *projected* by most orgs. All three views can be true.
- **Agentic vs. agent.** "Agentic" is sometimes used to describe behavior (autonomous, goal-pursuing) while "agent" is the system. The wiki uses both interchangeably for now; future ingests may force more precision.
- **Hype vs. capability gap.** RE-Bench shows agents losing to humans at 32-hour budgets. Many enterprise workflows have multi-day horizons. The [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents post]] partially reframes the gap as **architectural** (context-window saturation, brain/hands coupling) rather than purely capability-based — the brain/hands/session split is precisely the bet that long-horizon weakness is fixable with scaffolding. Open question: how much of the 32-hour gap closes with better orchestration vs. requires better models?
- **Multi-agent systems are mostly aspirational.** MITTRI/Cisco frames the 3-stage progression as if multi-agent is on a near-term horizon, but production multi-agent systems remain rare. Discount accordingly.

## Related concepts

- [[agent-harness]] — the runtime engineering layer that wraps a model to make a production agent; where most agent failures actually originate
- [[generative-ai]] — the substrate; most agents are LLM-based
- [[foundation-models]] — what agents are typically built on (rented, swappable; the harness is what's owned)
- [[enterprise-ai-adoption]] — the deployment context
- [[ai-benchmarks]] — RE-Bench specifically targets agent evaluation; PlanBench tests reasoning that agents need

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-agents") OR contains(tags, "agentic-ai")
SORT file.name ASC
```
