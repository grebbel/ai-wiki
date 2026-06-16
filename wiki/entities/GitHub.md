---
type: entity
kind: organization
aliases: ["GitHub", "GitHub Inc.", "github.com"]
tags: [github, microsoft-subsidiary, github-copilot, copilot-coding-agent, agent-hq, github-advanced-security, secret-scanning, code-scanning, copilot-autofix, state-of-the-octoverse, developer-platform, agentic-devops, version-control]
parent: "[[Microsoft]]"
website: "https://github.com"
confidence: 0.8
last_confirmed: "2026-06-09"
accessed_at: "2026-06-09"
source_count: 1
relationships:
  - type: part-of
    target: Microsoft
    via: "GitHub has operated as a Microsoft subsidiary since the 2018 acquisition; *\"GitHub is the center of the universe for Microsoft's developer agentic tooling\"*"
  - type: published-by
    target: 2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life
    via: "Mickey Gousset (Staff DevOps Architect, GitHub) co-presents the Agentic DevOps keynote demoing Copilot coding agent + Agent HQ + Advanced Security (22 Dec 2025)"
---

# GitHub

**GitHub** is the Microsoft-owned developer platform (version control, code hosting, CI/CD, and — central to the 2025–2026 wiki corpus — the **Copilot** family of AI coding agents). Promoted to an entity page on 9 June 2026 via **cross-page-presence promotion** (precedent: [[LangChain]], [[Andrej Karpathy]], Jack Clark): GitHub is referenced as a plain-text mention across ~31 source pages, and the [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life|Agentic DevOps keynote]] is the first source dedicated to GitHub's agentic tooling — co-presented by a GitHub staff architect.

> **Backlinking note.** `source_count` is set to **1** (formal inbound source-page wikilinks), not ~31 (the count of plain-text mentions). Converting the historical plain-text "GitHub" mentions into wikilinks is a deferred lint cleanup; until then this page is reached via the one source that wikilinks it plus the [[Microsoft]] parent.

## Role in the wiki

GitHub is the **developer-tooling vantage** on the 2025–2026 agentic-coding buildout — the layer where AI coding agents meet version control, code review, and security scanning. Where [[LangChain]] is the *agent-framework* vendor and [[Anthropic]] / [[OpenAI]] / [[Google]] are the *model* vendors, GitHub is the *developer-workflow-platform* vendor whose products (Copilot, Agent HQ, Advanced Security) operationalise [[agentic-engineering]] inside the everyday dev loop.

### GitHub Copilot + the coding agent

GitHub's AI pair-programmer, now extended into an **autonomous coding agent**: assign a GitHub issue (or, via integration, an Azure DevOps work item) to Copilot and it opens a draft PR, works in the background (reads files, runs tests and bash), and returns for human review. A load-bearing safety default surfaced in the keynote: **the person who initiated a Copilot request cannot be the final approver to merge** into the parent branch — a structural human-in-the-loop control (see [[responsible-ai]]).

### Agent HQ

Announced at **GitHub Universe** (late 2025). A centralized surface to **monitor, steer (mid-run), and audit** active and past agent sessions. Its **open architecture** lets non-GitHub agents — the [[OpenAI]] **Codex** agent, with [[Anthropic|Claude]] and [[Google|Gemini]] agents following — run from inside VS Code under the Copilot license, without a separate vendor account. This positions GitHub as an *agent-orchestration host*, not just a single-vendor agent.

### GitHub Advanced Security

Secret scanning + code scanning, now with **Copilot autofix** (*"found means fixed"* — a generate-fix button on a detected vulnerability). Keynote stat: GitHub secret protection **blocked 4.4 million credential leaks in 2024**. The keynote's worked example of why this matters in the vibe-coding era: AI agents (Claude + Codex) shipped a URL-injection vulnerability that Advanced Security caught — see [[vibe-coding]].

### State of the Octoverse

GitHub's annual developer-activity report. The keynote cites the **2025** edition: **TypeScript** is now the most-used language on GitHub, ahead of Python (#2); ~180 million developers on the platform.

## Open questions

- **Full backlinking.** ~31 source pages mention GitHub in plain text; promoting those to wikilinks (and recomputing `source_count`) is the obvious next lint pass.
- **GitHub Copilot as its own product page.** Currently a Dangling product mention; a second Copilot-centric source would justify a dedicated [[document-intelligence]]-style product/concept page.
- **Relationship to the model vendors.** GitHub hosts [[OpenAI]], [[Anthropic]], and [[Google]] models/agents inside Copilot; the commercial and routing relationships (the Microsoft responsible-AI proxy) are only sketched.

## Mentioned in

- [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life]] — the promotion trigger: Copilot coding agent, Agent HQ, Advanced Security, State of the Octoverse.
- [[Microsoft]] — parent company.
