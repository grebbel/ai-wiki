---
type: entity
kind: organization
aliases: ["Google", "Google LLC", "Alphabet (operating subsidiary)"]
tags: [google, big-tech, hyperscaler, ai-lab, foundation-models, gemini, google-cloud, google-research]
since: 1998
confidence: 0.75
last_confirmed: "2026-05-08"
source_count: 2
relationships:
  - type: published-by
    target: 2026-04-22-cheung-ippolito-secchi-google-agents-cli
    via: "Google Developers Blog announcement of Agents CLI in Agent Platform"
---

# Google

Big-tech platform company; operating subsidiary of Alphabet. Within this wiki Google appears primarily in three roles: **AI lab** (Gemini family of foundation models, ADK harness framework), **cloud hyperscaler** (Google Cloud Platform and the Agent Platform that hosts agent-runtime infrastructure), and **research publisher** ([[Google Research]] preprints and reports). The wiki holds a small but growing primary-source footprint on Google as of May 2026 — see *Mentioned in* below for current edge count.

## Sub-organizations and brands appearing in the wiki

- [[Google Research]] — research arm; producer of the Gemini model family; anchor of the durable-skills measurement work ([[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]] / Vantage / Executive LLM platform).
- **Google Cloud / Google Cloud Platform** — hyperscaler division. Surfaces in this wiki via Cloud Run, GKE, Agent Runtime, Cloud Build, Cloud Trace / Logging / Monitoring as deployment, CI/CD, and observability substrates for agents. Sponsor of the Agents CLI announcement.
- **Google Developers** — developer-relations division publishing the Google Developers Blog; the channel for the [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI]] announcement.
- **Gemini Enterprise** — enterprise distribution surface for agents registered via the Agents CLI. (Single-source mention; promote on second-source coverage.)

## Platform / product engineering

- **Agent Platform** — Google Cloud's umbrella for agent-runtime infrastructure.
  - **Agents CLI in Agent Platform** — released 22 April 2026 as the unified programmatic backbone for the [[agent-development-lifecycle|Agent Development Lifecycle (ADLC)]]; bundles **seven specialized skills** (Workflow / ADK Code / Scaffold / Evaluation / Deployment / Publish / Observability); two-mode design (Agent Mode for AI coding agents, Human Mode for deterministic CLI use). See [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]].
  - **Agent Runtime / Cloud Run / GKE** — three deployment substrates the CLI targets via `agents-cli deploy`.
- **ADK (Agent Development Kit)** — Google's open-source agent-engineering framework. Listed in [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] Layer 2 harness-frameworks alongside LangChain, Microsoft Agent Framework, LlamaIndex, CrewAI, Haystack, DSPy. The Agents CLI's **ADK Code** skill is the Python-API reference surface for ADK.
- **A2A / A2UI / MCP integration** — Google Cloud names A2A and A2UI alongside MCP as the agent-integration protocols the platform supports natively.

## Models referenced in this wiki

- **Gemini family** — the Google Research foundation-model line referenced as the autorater substrate in [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]] (Pearson r = 0.88 vs human experts on creativity assessment).
- **Gemini CLI** — Google's coding-agent CLI; named as an Agents-CLI consumer alongside Claude Code and Cursor in the [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI]] announcement.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "google") OR contains(tags, "google-cloud")
SORT file.name ASC
```

## Open questions

- **Cross-product coherence.** Two Google primaries in the wiki within ten days (Globerson et al. 2026 from Google Research; Cheung et al. 2026 from Google Developers) hint at a broader Google agent-platform thesis. Whether Google's positioning is *Gemini-as-substrate + agent-platform-as-runtime + assessment-as-product* or something looser will become clearer with more sources.
- **ADK as concept page.** ADK is referenced from three sources but currently treated as a brand mention on this entity. If a primary ADK technical-deep-dive lands, ADK could justify its own concept (or product-entity) page.
- **Gemini family entity.** The wiki has [[Anthropic]]'s Claude family enumerated explicitly (Sonnet 4.5 / Opus 4.5 / Opus 4.6) but does not yet have the parallel for Gemini. Worth filling on second-source coverage.
