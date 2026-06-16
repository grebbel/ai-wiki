---
type: entity
kind: organization
aliases: ["Microsoft", "Microsoft Corporation", "Microsoft Visual Studio", "MSFT"]
tags: [microsoft, azure, azure-devops, visual-studio-code, vs-code, github-parent, copilot, responsible-ai, azure-sre-agent, openai-partner, developer-tools, agentic-devops]
website: "https://microsoft.com"
confidence: 0.8
last_confirmed: "2026-06-09"
accessed_at: "2026-06-09"
source_count: 1
relationships:
  - type: employs
    target: GitHub
    via: "GitHub has operated as a Microsoft subsidiary since the 2018 acquisition"
  - type: published-by
    target: 2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life
    via: "Published on the Microsoft Visual Studio YouTube channel; demos Azure DevOps, VS Code, the Microsoft responsible-AI pipeline, and the Azure SRE Agent (22 Dec 2025)"
---

# Microsoft

**Microsoft** is the cloud-and-developer-tools giant that owns [[GitHub]] (since 2018), partners deeply with [[OpenAI]], and ships the developer surfaces central to the wiki's agentic-coding corpus: **Azure**, **Azure DevOps**, **Visual Studio Code**, and the **responsible-AI pipeline** that proxies Copilot requests. Promoted to an entity page on 9 June 2026 via **cross-page-presence promotion** (precedent: [[LangChain]], [[Andrej Karpathy]]): Microsoft is a plain-text mention across ~21 source pages, and the [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life|Agentic DevOps keynote]] — published on the **Microsoft Visual Studio** channel — is the first source centred on Microsoft's own agentic developer tooling.

> **Backlinking note.** `source_count` is set to **1** (formal inbound source-page wikilinks), not ~21 (plain-text mentions). Backfilling the historical mentions into wikilinks is a deferred lint cleanup.

## Role in the wiki

Microsoft is the **platform-and-cloud vantage** on agentic development — the vendor whose IDE (VS Code), cloud (Azure), ALM tooling (Azure DevOps), and safety layer (responsible-AI pipeline) host the agentic workflows that [[GitHub]]'s Copilot drives. The channel-author convention applies: *Microsoft Visual Studio* (the YouTube channel) maps to **Microsoft** as the publishing entity.

### Visual Studio Code

Microsoft's cross-platform editor — the keynote's hub for agentic development. The **four Copilot interaction modes**: **Ask / Edit / Agent / Plan** (*Plan* is the newest — the agent states its implementation plan before acting, bounding the over-autonomy failure mode). Instructions files encode house rules + exemplars; agents run locally (CPU/GPU) or push to GitHub's cloud; profiles swap toolsets; **Ollama + the Continue extension** enable offline/local-model agents.

### Azure DevOps + the responsible-AI pipeline

Copilot agents are coming to **Azure DevOps** (private preview) — but routed through [[GitHub]] (*"you still have to link it up to GitHub"*). Every Copilot request passes through **Microsoft's responsible-AI pipeline**, which validates input and the returned code (security vulnerabilities, NSFW) **even when the chosen model is third-party** ([[Anthropic]]/[[Google]]) — sending only enough across the wire and checking the response before it reaches the developer, in milliseconds. See [[responsible-ai]].

### Azure SRE Agent

Microsoft's autonomous cloud-monitoring + incident-response agent (preview). Scope it to an Azure resource group; it performs incident management, can be permissioned to **autonomously remediate** certain conditions, and files health/security reports — framed as *"a site reliability engineer on my team."* A worked instance of an [[agentic-engineering|autonomous agent]] in the IT-operations (not just coding) domain.

### OpenAI partnership

Microsoft hosts and routes [[OpenAI]] models (and now the Codex agent inside Copilot), alongside [[Anthropic]] and [[Google]] models. The keynote frames model choice as a developer decision, with Microsoft's proxy doing the safety validation regardless of model.

## Open questions

- **Full backlinking.** ~21 plain-text "Microsoft" mentions across the corpus await promotion to wikilinks.
- **Product sub-pages.** Azure, VS Code, Azure DevOps, and the Azure SRE Agent are Dangling product mentions; promote on a second source each.
- **The Microsoft–OpenAI commercial relationship.** Referenced but not characterised; a dedicated source would let the wiki track it properly.

## Mentioned in

- [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life]] — the promotion trigger: VS Code modes, Azure DevOps, responsible-AI pipeline, Azure SRE Agent.
- [[GitHub]] — Microsoft subsidiary; the developer-platform half of the keynote.
