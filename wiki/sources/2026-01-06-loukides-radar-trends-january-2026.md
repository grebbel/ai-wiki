---
type: source
kind: article
title: "Radar Trends to Watch: January 2026"
author: ["Mike Loukides"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar — Radar Trends to Watch (monthly)"
url: "https://www.oreilly.com/radar/radar-trends-to-watch-january-2026/"
date_published: 2026-01-06
date_ingested: 2026-05-16
length: "~6-section monthly trend digest covering ~38 items; web article only (no PDF in raw)"
raw: null
tags: [radar-trends, monthly-digest, oreilly-radar, agent-skills, mcp, gpt-5-2, gemini-3, llm-models, function-calling, rust-in-linux, cognitive-architect, prompt-injection]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
relationships:
  - type: supports
    target: 2026-01-09-baron-signals-for-2026
    via: "the January monthly digest names the same paradigm vocabulary (agentic dev, MCP, cognitive-architect role) that Baron's annual outlook foregrounds three days later — the digest is the granular feed, Signals is the editorial crystallisation"
  - type: supports
    target: 2026-02-03-loukides-radar-trends-february-2026
    via: "first installment in the wiki's Loukides monthly-digest series; each month threads forward to the next via the recurring topic blocks (Skills/Agents/MCP/Hooks/Security)"
---

# Loukides — Radar Trends to Watch: January 2026

The **first installment** in the wiki of [[Mike Loukides]]'s monthly *Radar Trends to Watch* digest at O'Reilly Radar — a curated, six-section roundup of the prior month's tech news, with editorial weighting toward the threads Loukides expects to compound. Published **6 January 2026**, covering events from the December 2025 holiday window.

Opening framing notes that December was truncated by O'Reilly's holiday break, but two foundational reads are recommended: **Andrej Karpathy's LLM year review** (the upstream conceptual spec for this wiki) and the **Resonant Computing Manifesto**. OpenAI's year-end push to release **GPT-5.2** and to secure **Disney's character-licensing deal for Sora** is named as the headline story.

## TL;DR — the month's standout threads

- **Agent Skills become an open spec.** **Anthropic opened the Claude Skills spec**; **OpenAI quietly adopted them**. The Skills-as-portable-package primitive is becoming cross-vendor.
- **GPT-5.2 released in three versions** targeting professional knowledge workers — the year-end model push that frames January's framing.
- **Gemini 3 Flash** named as Google's *"final"* model combining reasoning, speed, and economy.
- **Rust enters the Linux kernel without the experimental flag**; **Tor Project ships Arti** (its Rust rewrite) as production-ready. **Ruby 4.0** released on Christmas (Matz tradition).
- **"Cognitive Architect" role surfaces** — developer decomposes problems and emphasises higher-order thinking. Adjacent to the wiki's [[agentic-engineering]] vocabulary.
- **PARK stack** (PyTorch + AI + Ray + Kubernetes) named as the shape of open-source AI development infrastructure.
- **Prompt injection consolidates as a first-class security threat.** **Chrome ships a "User Alignment Critic"** that monitors Gemini actions for indirect prompt injection (the wiki's first browser-side prompt-injection countermeasure source). MITRE's **Top 25 weaknesses 2025** retains XSS / SQL injection / CSRF on the list — *normalization of deviance in AI* surfaces as a security framing.
- **Poetry as LLM jailbreak.** Writing prompts as verse evades model defenses — a new attack pattern Loukides flags.

## Sectional summary

**AI (14 items).** Function-calling adaptations (FunctionGemma — Google's function-calling 270M Gemma 3); Agent Skills spec opened by Anthropic; Gemini 3 Flash; GPT-5.2; Disney–OpenAI Sora licensing deal; Nemotron 3 Nano (NVIDIA, 30B MoE, fully open source); Google's **Titans architecture** (efficient memory handling); Mistral 3 + three smaller variants with open weights; DeepSeek V3.2 (sparse attention + RL + task synthesis); FLUX.2 (Black Forest Labs vision model approaching Google Nano Banana quality).

**Programming (9 items).** Ruby 4.0 Christmas release; Tor Project's Rust rewrite (Arti); **Cognitive Architect role**; Rust in Linux kernel out of experimental status; **PARK stack** (PyTorch / AI / Ray / Kubernetes); Go vs Rust vs Zig technical comparison; Stack Overflow AI Assist (conversational search for Stack Exchange); **DocumentDB open source** (MIT-licensed Mongo-/Postgres-hybrid); Christina Wodtke argues **user experience as moat, not model**.

**Security (7 items).** SantaStealer malware (rebranded BluelineStealer; browsers + wallets + services); MITRE Top 25; **normalization of deviance in AI** (false safety sense around prompt injection); AI-edited image consequences (a bridge-collapse image cancelled train services); virtual-kidnapping scams (doctored social media used as ransom "proof"); **poetry as LLM jailbreak**; GrayNoise IP-check tool (free botnet IP scanner).

**Web (5 items).** **Chrome User Alignment Critic** (monitors Gemini for indirect prompt injection); **Android XR smart glasses** (Google prototypes monocular/binocular Gemini-backed frames); **Lightpanda** (browser engineered for crawlers / automated apps); **Nook Browser** (open-source privacy-preserving fast browser for humans); **Brave AI-Assisted Mode** (Leo for privacy-preserving agentic multistep tasks).

**Hardware (2 items).** Arduino vs Adafruit licensing controversy; NYU researchers on **democratising microchip design**.

**Operations (1 item).** **Cloudflare outage analysis** — detailed examination of November's internet-wide disruption.

## Cross-positioning with the wiki

- **Sub-monthly granular feed for [[2026-01-09-baron-signals-for-2026|Signals for 2026]]** — Baron's annual outlook crystallises three days later; the January digest is the underlying news log. *MCP, Skills, agentic dev, cognitive architect, prompt injection* appear in both.
- **First "User Alignment Critic" mention** in the wiki — a structural countermeasure to prompt injection at the browser/agent boundary. Will surface again across multiple monthly digests as agent-side defences mature.

## Named entities (this ingest)

- [[Mike Loukides]] — O'Reilly Radar editor; recurring author of this monthly digest. **First wiki mention; promoted to entity in this batch** (5 source pages in batch).
- [[O'Reilly Media]] — Publisher. **Promoted to entity in this batch.**

Plus dangling first-mentions of: GPT-5.2, Gemini 3 Flash, Mistral 3, FLUX.2, Nemotron 3 Nano, DeepSeek V3.2, Titans architecture, PARK stack, Christina Wodtke, MITRE.

## Source-quality notes

- **Genre**: monthly editorial-curatorial digest. **Not peer-reviewed; not empirical.** Items are pointer-summaries with embedded links to original sources; this source page captures the *editorial weighting and threading* rather than the underlying news.
- **Confidence: 0.65.** Per Lifecycle: single secondary-summary source, +0.05 for O'Reilly editorial bar; the underlying claims trace to the embedded links rather than to Loukides' own analysis. **Citations from this page should reference the underlying primary source where available**; the digest page itself is best used as a **thread index** into the month's trend space.
