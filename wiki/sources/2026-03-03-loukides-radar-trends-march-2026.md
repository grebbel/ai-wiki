---
type: source
kind: article
title: "Radar Trends to Watch: March 2026"
author: ["Mike Loukides"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar — Radar Trends to Watch (monthly)"
url: "https://www.oreilly.com/radar/radar-trends-to-watch-march-2026/"
date_published: 2026-03-03
date_ingested: 2026-05-16
length: "~6-section monthly trend digest; web article only (no PDF in raw)"
raw: null
tags: [radar-trends, monthly-digest, oreilly-radar, openclaw, agent-2-human, sandboxing, ai-finds-vulnerabilities, ransomware, claude-sonnet-46, gemini-31]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-02-03-loukides-radar-trends-february-2026
    via: "third installment; February introduced OpenClaw, March names it as the top-of-AI-stack story"
  - type: supports
    target: 2026-04-07-loukides-radar-trends-april-2026
    via: "fourth installment in the Loukides series; threads forward the Anthropic / Claude / Gemini model-release cadence and the agent-sandboxing security thread"
---

# Loukides — Radar Trends to Watch: March 2026

The **third installment** of the monthly digest, published **3 March 2026**, covering February 2026. **Opening framing**: *OpenClaw's explosive growth in February* — agent-only social networks and games emerge, multiple security-focused clones appear, and Loukides positions OpenClaw as *"the next layer on top of AI agents"* per [[Andrej Karpathy]]'s assessment.

The month's structural story is **security adjacent to agent infrastructure**: the OpenClaw ecosystem produces immediate exploit-bait (HackMyClaw, IronClaw, credential-theft active operations), and the same digest cycle reports **AI finding 12 vulnerabilities in OpenSSL via Claude** and **500 zero-days discovered via Claude Opus 4.6**. The harness-as-attack-surface theme that [[2026-05-15-osmani-agent-harness-engineering|Osmani's harness-engineering essay]] later names is implicit throughout.

## TL;DR — the month's standout threads

- **OpenClaw becomes the "next layer on top of AI agents"** per Karpathy — agent-only social networks, sandbox-permission challenges, alternatives emerging (IronClaw with stronger sandboxing).
- **AI as offensive-security tool, at scale.** **500 zero-days discovered via Claude Opus 4.6 analysis**; **12 OpenSSL vulnerabilities found via Claude**; **HackMyClaw** gamified prompt-injection challenge launches.
- **Agent-to-Human (A2H) protocol** surfaces as a category — formalising agent-human handoff as a discrete primitive. Adjacent to the wiki's [[agent-development-lifecycle]] coverage.
- **Claude Remote Control** — cross-device desktop session continuation. **First wiki mention** of session-portability as a discrete agent capability.
- **C compiler via agents** — 100,000 lines of Rust, ~$20K token cost. The most concrete *agent writes a serious systems program* result in the digest series so far.
- **Ransomware evolves from encryption to extortion** — the threat-model shift Loukides flags.
- **Lyria 3** — 30-second musical clip generation from verbal prompts. Multimodal-AI continues moving up the creative stack.

## Sectional summary

**AI (10 items).** Moonshine Note Taker (local voice transcription); Nano Banana 2 / Gemini 3.1 Flash; **Claude Remote Control**; OpenClaw sandbox limitations; Alibaba Qwen 3.5; Lyria 3; **Agent-2-Human protocol**; Claude Sonnet 4.6 + Gemini 3.1 Pro releases; multimodal RAG (enterprise graphs/images); Waymo's **World Model** for traffic-behaviour simulation.

**Programming (7 items).** **Anthropic Claude Max — six months free for open-source maintainers**; Pi coding agent (minimal terminal-based); **C compiler via agents (~$20K in tokens)**; GitHub PR controls (disable/limit); Showboat and Rodney (agents demo working software); Gas Town (codeless programming exploration continues); macOS sandboxing tools (deprecated → easier alternatives).

**Security (14 items, dominant section).** Smart-glasses detection app; **Agentsh** (execution-layer security via bash replacement); attacks on time synchronization (factory infrastructure threats); **AI discovers vulnerabilities — 12 in OpenSSL via Claude**; **HackMyClaw** gamified prompt-injection challenge; OpenClaw credential theft active operations; Deno sandbox potential; **IronClaw** OpenClaw alternative emphasizing sandboxing; malicious coding challenges (hidden npm/PyPI dependencies); **500 zero-days via Claude Opus 4.6 analysis**; VS Code malware extensions exfiltrating to China; Bizarre Bazaar (LLM API attacks for resource theft); ransomware evolution (encryption → extortion); personal data removal tools.

**Web (3 items).** Markdown for Agents (Cloudflare HTML→markdown service); **WebMCP** (proposed API standard for agent-accessible web apps); Firefox 148 (AI feature opt-out).

**Operations (2 items).** Babyshark (simplified Wireshark TUI); laser-etched glass (Microsoft long-term data storage).

**Things (2 items).** Desk robots; Doom on Lego.

## Cross-positioning with the wiki

- **AI-as-offensive-security** complements [[concepts/responsible-ai]] coverage with a new dimension — the same capability that finds 500 zero-days legitimately can also be turned malicious; this is the dual-use thread that will recur in April and May digests.
- **OpenClaw's emergence as a category** is the wiki's strongest signal that **persistent always-on agent memory** is becoming infrastructure. Worth tracking for concept-page promotion once a second non-Loukides source treats it.
- **Anthropic Claude Max for OSS maintainers** is an OSS-economics datapoint that complements [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad's "only two jobs left"]] AI-native-company framing.

## Named entities (this ingest)

- [[Mike Loukides]] — see January.
- [[O'Reilly Media]] — see January.

Plus dangling first-mentions of: OpenClaw, IronClaw, HackMyClaw, Agentsh, Claude Sonnet 4.6, Gemini 3.1 Pro/Flash, Lyria 3, Waymo World Model, WebMCP, Agent-2-Human protocol, Pi coding agent, Showboat, Rodney, Babyshark, Moonshine Note Taker.

## Source-quality notes

Same as January: single secondary-summary source; confidence 0.65.
