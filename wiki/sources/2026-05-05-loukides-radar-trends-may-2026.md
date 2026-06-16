---
type: source
kind: article
title: "Radar Trends to Watch: May 2026"
author: ["Mike Loukides", "Claude"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar — Radar Trends to Watch (monthly)"
url: "https://www.oreilly.com/radar/radar-trends-to-watch-may-2026/"
date_published: 2026-05-05
date_ingested: 2026-05-16
length: "~7-section monthly trend digest; web article only (no PDF in raw)"
raw: null
tags: [radar-trends, monthly-digest, oreilly-radar, claude-mythos, gpt-55, workspace-agents, claude-managed-agents, agent-runtimes, npm-supply-chain, post-quantum-ransomware, gpt-rosalind, robotics, ai-becoming-operational]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
  - digital-seizing/balancing-digital-portfolios
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-07-loukides-radar-trends-april-2026
    via: "fifth installment in the Loukides monthly digest; extends the workspace-agent / agent-runtime threads from April and adds 'AI becoming operational' as the framing"
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "the May digest names Claude Managed Agents and the OpenAI-decoupled-harness-Agents-SDK release as the headline agent-runtime stories — direct news-side companion to the Anthropic engineering blog post"
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "the May digest names OpenAI 'decoupled its agent harness, releasing it open-source via the Agents SDK' and Anthropic launched Managed Agents — both directly support Osmani's harness-as-a-service (HaaS) section"
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "the May digest names Stanford's 2026 AI Index Report (400+ pages) as a published-this-month event"
---

# Loukides — Radar Trends to Watch: May 2026

The **fifth (and most recent) installment** of the monthly digest, published **5 May 2026**, covering April 2026. **Co-authored with Claude** (first time the digest carries an explicit human-AI co-byline). **Opening framing — "AI is becoming operational"**: the highlight tension is between **Anthropic's restricted approach to Claude Mythos** (limiting access through *Project Glasswing*) and **OpenAI's public release of GPT-5.5** (offering *"Mythos-like hacking" capabilities widely*). The piece emphasises that **AI is moving beyond language games to enterprise process automation through shared team agents**.

The structural story is **agent runtimes / harnesses-as-a-service productizing** — exactly the [[2026-05-15-osmani-agent-harness-engineering|HaaS framing]] Osmani names ten days later. Anthropic ships **Claude Managed Agents**; OpenAI **decouples its agent harness and releases it open-source via the Agents SDK**; Amazon launches **agent registry within AWS Bedrock AgentCore**; Cursor 3 **repositions as agent orchestrator, demoting the IDE to secondary role**. Four vendors converging on the same productization within a single month.

## TL;DR — the month's standout threads

- **AI becoming operational.** *AI is moving beyond language games to enterprise process automation through shared team agents.* The framing line of the month.
- **Claude Mythos under restricted access; GPT-5.5 public.** The capability-gap-and-safety-policy split between Anthropic and OpenAI is now public knowledge. **AISI analysis: Mythos "represents a step up over previous frontier models."** But **small open-weight models can match Mythos performance at vulnerability discovery** — the capability gap may be narrower than the safety-policy gap suggests.
- **Workspace agents become productized.** OpenAI workspace agents (team-wide tool sharing and automation); **Anthropic Claude Managed Agents** (prebuilt harness infrastructure for agentic workflows); **Anthropic Claude Code routines** (scheduled/triggered packages with prompts and connectors); **OpenAI decouples harness → Agents SDK open-source**; **Amazon agent registry in Bedrock AgentCore**; **Cursor 3 as orchestrator, IDE secondary**. **Five vendor-side moves toward HaaS in a single month.**
- **Stanford 2026 AI Index Report (400+ pages)** published this month — the wiki's standalone ingest is [[2026-04-30-ai-index-report-2026]].
- **DeepSeek V4 preview** — *"large model (over 1T parameters)"* with frontier-level performance.
- **npm supply-chain attack** allowed credential theft and self-propagating malware insertion. **Kyber ransomware gang transitioning to post-quantum encryption on Windows systems.** Two structural security shifts in one month.
- **GPT-Rosalind** — OpenAI's biology-tuned model for 50 common laboratory workflows with skepticism bias. **First wiki source on a science-domain-tuned frontier model with bias baked in by design.**
- **Robotics inflection.** **Boston Dynamics Spot reads gauges and thermometers using Gemini Robotics-ER 1.6**. **MLB deploys robotic system for ball/strike challenge rulings.** Robotics and embodied AI moving from demo to production deployment.
- **Anthropic's 3.5 GW compute deal** with Google and Broadcom — power consumption specified rather than chip counts. Direct convergence with [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI's omniscaler / Apollo-comparison]] thesis about AI-foundation capex scale.

## Sectional summary

**AI Models.** Google publishes a catalogue of *"1,302 real-world use cases for generative AI"*; OpenAI launches GPT Images 2 (image-reasoning before generation); **Anthropic demonstrates Claude supervising alignment research, outperforming human researchers**; Moonshot Kimi K2.6 + Vendor Verifier tool; Alibaba Qwen3.6-35B-A3B MoE (3B active params); Stanford 2026 AI Index Report (400+ pages); **DeepSeek V4 preview (>1T params)**; **OpenAI GPT-5.5** (reduced token counts; *increased hallucination rates*); Google Gemma 4 (iPhone/Android on-device).

**Software Development.** OpenAI workspace agents; **Microsoft Critique and Council** (combining Claude and GPT for research problems); **Stash** (open-source memory layer); **Anthropic addresses Claude Code performance regression** (detailed postmortem); **Glif** agent (multi-LLM unified access with auto-selection); **OpenAI decouples agent harness → Agents SDK open-source**; **Anthropic Claude Code routines** (scheduled/triggered packages); **Anthropic Claude Managed Agents** (prebuilt harness); **Amazon AWS Bedrock AgentCore agent registry**; **Cursor 3** repositioned as agent orchestrator.

**Security.** Firefox 150 patches Tor de-anonymization vulnerability; **Kyber ransomware → post-quantum encryption on Windows**; **npm supply-chain credential theft + self-propagating malware**; Signal iOS notifications vulnerability (environmental, not protocol); **Google Security Operations adds three AI agents** (Threat Hunting, Detection Engineering, Third-Party Context); Microsoft reports Teams help-desk impersonation attacks; NIST stopped scoring lower-priority CVEs; **Anthropic Project Glasswing restricts Claude Mythos to critical-infrastructure use**; AISI Mythos analysis; **small open-weight models match Mythos at vulnerability discovery**.

**Infrastructure and Operations.** Microsoft allows enterprise admins to uninstall Copilot; **Google 8th-gen TPUs** (8t for training, 8i for inference); Google open-sources **Scion** (agent-orchestration testbed); **Anthropic 3.5 GW compute deal with Google + Broadcom** (power specified, not chip counts); Ollama adopts Apple MLX for Apple-silicon performance.

**Web.** *"Who Will Maintain the Web When PHP's Veterans Retire?"*; Laravel injecting cloud-service ads into agents; **IPv8 proposal** (full IPv4 backward compatibility + security + address depletion); Cloudflare **EmDash** (WordPress alternative); *Is BGP Safe Yet?* web app (ISP routing protocol implementation test).

**Biology.** **OpenAI GPT-Rosalind** (biology-tuned model, 50 common lab workflows, skepticism bias baked in).

**Robotics.** **Boston Dynamics Spot reads gauges + thermometers via Gemini Robotics-ER 1.6**; **MLB deploys robotic ball/strike challenge ruling**.

## Cross-positioning with the wiki

- **HaaS news-side companion to [[2026-05-15-osmani-agent-harness-engineering|Osmani's harness-engineering essay]].** Osmani's HaaS section names *Claude Agent SDK, Codex SDK, OpenAI Agents SDK* as the substrate trio. This digest reports **OpenAI decoupling and open-sourcing its harness** and **Anthropic shipping Managed Agents** — the productization of HaaS in real time.
- **Empirical-anchor companion to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] source page.** The Anthropic primary source ingest from 8 April; the digest names it again as the month's top runtime story.
- **AI-foundation capex scale companion to [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI 2026]].** Anthropic's 3.5 GW power deal is the first wiki source where compute-deal capacity is specified in *power-consumption* terms rather than chip counts — a structural shift toward the *power-as-bottleneck* framing MGI's 2040-projection scenario names.

## Named entities (this ingest)

- [[Mike Loukides]] — see January. Also **Claude** as co-author on this issue (the wiki does not have an "AI-coauthor" entity convention; treating Claude as a tool-credit rather than an entity-page subject).
- [[O'Reilly Media]] — see January.

Plus dangling first-mentions of: GPT-5.5, GPT Images 2, Claude Mythos, Project Glasswing, AISI (AI Security Institute), Kimi K2.6, Qwen3.6-35B-A3B, DeepSeek V4, Gemma 4, Claude Managed Agents (entity-eligible: ingested separately), OpenAI Agents SDK, Cursor 3, Amazon Bedrock AgentCore, Kyber ransomware gang, GPT-Rosalind, Boston Dynamics Spot, Gemini Robotics-ER 1.6, MLB, IPv8, EmDash, Glif, Stash, Plumb (April carry), Critique and Council.

## Source-quality notes

Same as January (single secondary-summary source; confidence 0.65), with an additional **provenance note**: this issue is co-authored by Mike Loukides and Claude. The wiki treats this as **transparency from the publisher about AI-assisted curation**, not as a downgrade of the digest's authority.
