---
type: source
kind: video
title: "Fix Karpathy's LLM Wiki with a Knowledge Graph | Claude Code + Obsidian + InfraNodus"
author: ["Nodus Labs"]
url: "https://www.youtube.com/watch?v=yYSTsKo8moU"
publisher: "[[Nodus Labs]]"
date_published: 2026-04-11
date_ingested: 2026-05-17
length: "~26:09 minutes (transcript 556 lines; ASR caption track, auto-generated, lightly proper-noun-checked at ingest)"
raw: "../../raw/videos/fix-karpathys-llm-wiki-with-knowledge-graph-claude-code-obsidian-infranodus.md"
tags: [llm-wiki, knowledge-graphs, infranodus, gap-analysis, ontology-graph, obsidian, claude-code, mcp-server, karpathy, content-gaps, living-memory]
relationships:
  - type: supports
    target: 2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks
    via: "both are early (≤ 1 week post-Karpathy-gist) third-party operationalisations of the LLM Wiki pattern. OceanBase = vendor implementation with embedded DB; Nodus Labs = knowledge-graph augmentation with MCP server. Both promote knowledge-graph integration as the load-bearing pattern."
  - type: supports
    target: 2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained
    via: "Raju's article and the Nodus Labs video are sibling Apr 2026 LLM-Wiki-explainer artefacts. Raju explains the pattern; Nodus Labs proposes an architectural fix (knowledge graphs) for the pattern's identified limitation (generic outputs when LLMs traverse a flat wiki structure)."
  - type: supports
    target: 2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers
    via: "Liu's comparative-architecture article distinguishes RAG / LLM Wiki / GBrain by retrieval semantics. The Nodus Labs video extends the LLM Wiki branch with a fourth option — KG-augmented LLM Wiki — that Liu's framework does not yet name."
  - type: supports
    target: 2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide
    via: "SurrealDB names the KG-as-deterministic-grounding-substrate principle for agents; the Nodus Labs video instantiates the same principle on a different substrate (LLM Wiki) and adds a gap-analysis workflow that operationalises *KG-as-attention-direction*"
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "Karpathy's LLM Wiki gist (4 April 2026) is the upstream artefact this video reacts to. The video positions itself as a *fix*, framed as identifying a concrete gap in Karpathy's pattern and proposing a structural augmentation."
  - type: contradicts
    target: 2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks
    via: "OceanBase's ex-brain ingests sources via *smart compilation* (event/status/fact detection); Nodus Labs ingests via *concept extraction + manual ideation*. Both wrap LLM Wiki but disagree on whether the pipeline should be (a) status-driven and automatic (OceanBase) or (b) ontology-graph-and-gap-driven with human curation (Nodus Labs)."
---

# Nodus Labs — *Fix Karpathy's LLM Wiki with a Knowledge Graph (Claude Code + Obsidian + InfraNodus)*

A **26-minute YouTube tutorial** by **[[Nodus Labs]]** (creators of **[[InfraNodus]]**, a knowledge-graph visualisation tool the speaker says they've been building *"for the last 10 years"*). Published **11 April 2026** — *one week after [[Andrej Karpathy|Karpathy]]'s LLM Wiki gist (4 April 2026)* — making this the wiki's **earliest third-party "fix" / extension proposal** for the LLM Wiki pattern, and one of three early-April / mid-April LLM-Wiki engagements already in the wiki ([[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain]] / [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju explainer]] / *this video*).

The presenter is the **InfraNodus founder** (named in the description as Dmitry Paranyushkin — the speaker self-identifies as having worked on InfraNodus for ten years, consistent with that attribution; the wiki defers a named-entity promotion to next ingest for verification). Channel-style: hands-on tutorial with screen-recording demo. The video positions itself as an immediate response to a perceived limitation in Karpathy's pattern.

## TL;DR

- **The diagnosis** (the load-bearing claim). Karpathy's LLM Wiki is a *"really good framework"* but **"not aware of itself."** When a user queries the wiki, the LLM scans the structure, extracts concepts, and *"produces the most probable outcome — because that's what LLMs are trained to do."* Result: **the wiki has structure, but querying it still yields generic outputs** because the LLM is using flat-prompt next-token logic to navigate it. *"Even though you have the structure, you still need something to navigate through it."*
- **The proposed fix** — knowledge-graph augmentation, three integration depths.
  1. **External tool** — open InfraNodus's web app on the wiki content; visualise clusters and gaps; copy back insights to Claude.
  2. **MCP server** — connect InfraNodus to Claude Code via MCP; `generate_knowledge_graph` and gap-analysis tools become directly callable from inside the LLM session. *"You can also use the InfraNodus MCP server inside Claude Code itself, which is basically an API that connects this whole content to InfraNodus."*
  3. **KG-integrated wiki** (the deepest layer) — the Nodus Labs skill *bakes knowledge-graph generation into the LLM Wiki workflow itself*. After ingest, the wiki contains both `concepts/` markdown files *and* an `infranodus/` folder holding **ontology graphs** generated on every interaction. *"It's some kind of living memory of what's happening in the system — every time you come back to it, Claude (or whatever system you use) will have access to this system of rules of how the concepts connect in your wiki."*
- **The novel mechanism** — *KG-as-attention-direction*, not just KG-as-retrieval-substrate. The gap-analysis workflow: (1) compute clusters from concept-page co-occurrence; (2) find pairs of clusters with low betweenness (the "gap"); (3) copy the **gap prompt** (a structured representation of two clusters and their disconnection) back to Claude; (4) ask Claude to generate insights *that bridge* the two clusters using the underlying source documents. *"I point the LLM's attention to the gap that exists. I provide the underlying structure. I give it some context, and then I say okay, use the documents in the concepts folder in order to generate an interesting idea that would connect these ideas together."* **The KG isn't substituting for retrieval — it's steering attention to where the wiki is missing connections.**
- **The opinionated stack** (worked example demonstrated in screen-record):
  - **[[Obsidian]]** — viewer / human-navigation layer. Includes the InfraNodus Obsidian plug-in for graph view alongside the wiki.
  - **[[Claude Code]]** / **Cursor** — LLM interaction layer.
  - **InfraNodus VS Code extension** + **InfraNodus Obsidian plug-in** + **InfraNodus MCP server** — three install paths into the same KG primitives.
  - **The Nodus Labs `skill-llm-wiki` Claude skill** — published at *github.com/infranodus/skills/blob/master/skill-llm-wiki/SKILL.md* — the **first wiki source on a third-party-shipped Claude skill that operationalises the LLM Wiki pattern**.
- **"Living memory" framing.** Every Claude session generates new InfraNodus ontology graphs that get saved alongside the wiki. The wiki's `concepts/` are *what is known*; the `infranodus/` graphs are *how the concepts relate, captured at successive points in time*. **The graph layer is treated as compounding state in its own right** — not just a derived view. This is structurally parallel to [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *"harness is a living system"* claim applied at the wiki-content layer rather than the agent-runtime layer.
- **The gap-analysis demo** (Chapter 13–14, 18:00–22:00). The speaker walks through a real wiki on a research topic ("financial flows" + "regression analysis" identified as two clusters with a gap between them). InfraNodus emits a structured gap-prompt that names the two clusters, the candidate bridge questions, and the most-dense source extracts from each cluster. Claude reads this gap-prompt + the underlying concept files and generates a bridging analysis. **The output is markedly less generic than a flat-prompt query of the same wiki.**
- **The MCP-server-without-graph-UI option** (Chapter 16, 23:15-end). If the user doesn't want to open the graph UI, they can simply tell Claude *"run gap analysis on the wiki"* and Claude uses the InfraNodus MCP `gap_analysis` tool to perform the same workflow — read all concept files, identify clusters, find gaps, generate bridging questions, save the ontology graph back to `infranodus/`. **First wiki source on KG-gap-analysis as a callable agent primitive, not just a human-visualisation tool.**
- **Closing recommendation** to the channel's audience. *"You can use the graph if you want, or you can also use the MCP server inside Claude Code itself. … If you feel uncomfortable using the graph interface, you can just delegate all this responsibility to your LLM."* Pragmatic — both interfaces are valid; the underlying primitive is the same.

## What was actually ingested

The full 26:09 transcript (**556 ASR segments**) at `raw/videos/fix-karpathys-llm-wiki-with-knowledge-graph-claude-code-obsidian-infranodus.md`. Auto-generated captions, fetched 2026-05-17 at `--timeout 180000` after the initial 60-second attempt failed with the *transcript-panel-did-not-render* symptom (now a recognised long-format-video failure mode — see [[2026-05-15]] log entry on the MGI virtual-event retry pattern). 16-chapter structure preserved from the YouTube description. Light proper-noun verification at ingest time (Karpathy / InfraNodus / Obsidian / Claude Code spelled correctly in the body).

## Cross-positioning with the wiki

### The early-April LLM-Wiki cluster (one week post-Karpathy gist)

The wiki now holds three **independent third-party engagements** with Karpathy's LLM Wiki pattern published within ~1-2 weeks of the upstream gist:

| Source | Date | Vantage |
|---|---|---|
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase ex-brain]] | 9 April 2026 (5 days post-gist) | **Vendor implementation** — *ex-brain* CLI tool with smart-compilation pipeline, embedded seekdb DB, MCP server integration |
| [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus\|Nodus Labs / InfraNodus video]] **(this)** | 11 April 2026 (7 days post-gist) | **Architectural augmentation** — KG-as-attention-direction layer, gap-analysis workflow, MCP server, Claude skill |
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju explainer]] | 16 April 2026 (12 days post-gist) | **Conceptual explainer + 10-dim RAG-vs-LLM-Wiki comparison** |

These three converge on a shared pattern: **the LLM Wiki is the durable structural primitive; the question is what to layer on top** (smart compilation / KG augmentation / RAG-bridge). The Nodus Labs piece is the most architecturally specific.

### The KG-as-attention-direction claim

Prior wiki sources on knowledge graphs ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]], [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza HiveMQ]], [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec]]) frame KGs as **retrieval substrates** (deterministic graph-traversal supplementing or replacing vector search). The Nodus Labs video adds a **second use mode**: KGs as **attention-direction primitives** — the gap-prompt is not retrieving anything; it's telling the LLM *where in its existing context to look harder*. This is a structurally different role and worth a body note on the [[concepts/knowledge-graphs]] page.

### Connection to harness engineering

The "living memory" framing — `infranodus/` folder accumulating ontology graphs across sessions — is **structurally parallel** to [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic's]] hooks-driven memory and [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *AGENTS.md memory standard*. The KG layer is to the LLM Wiki what the memory layer is to the harness: a compounding persistent-state substrate the model reads on every turn. **This is the wiki's first source that names KG-as-harness-memory-component explicitly**, even though the speaker uses the word "wiki" rather than "harness."

### Connection to this very repository

This source recommends a pattern (KG augmentation of LLM Wiki + InfraNodus MCP server + per-session ontology graphs) that **this repo does not currently use**. The repo's [[wiki/.graph.json]] (per CLAUDE.md *§Graph*) is a derived export, not an InfraNodus-style attention-direction primitive. **Open architectural question for this repo**: would adding an InfraNodus-style gap-analysis pass (probably as a `lint` operation per CLAUDE.md's four operations, or as a new `gap-analyse` operation) materially improve the wiki's value as a research substrate? The next [[2026-05-15-osmani-agent-harness-engineering|harness-ratchet]] increment would be: *make the wiki's own structure-gaps queryable as a tool the agent calls during synthesis*.

## Named entities (this ingest)

- [[Nodus Labs]] — YouTube channel + company; creators of [[InfraNodus]]. **First mention. Dangling. Channel-as-author convention applies.**
- [[InfraNodus]] — knowledge-graph visualisation tool / product / web app + Obsidian plug-in + VS Code extension + MCP server. **First mention. Dangling.**
- Speaker (channel host) — self-identifies as the InfraNodus creator who has *"been working on InfraNodus for the last 10 years."* The channel description / public-record attribution maps this to **Dmitry Paranyushkin** (InfraNodus founder); the wiki defers the named-person promotion to next ingest for direct verification.
- [[Andrej Karpathy]] — already in the wiki; cited as the upstream LLM Wiki gist author.
- Other passing entities ([[Obsidian]] / [[Claude Code]] / Cursor) already in the wiki ecosystem.

## Source-quality notes

- **Genre**: practitioner tutorial / product-demo video by a tool vendor. **Vendor-sponsored claim** — per CLAUDE.md *Lifecycle vendor-source rule*, confidence is capped at 0.75.
- **Empirical content**: zero empirical study; full video is methodology demonstration on the speaker's own research wiki. Generic claims are illustrated, not measured.
- **Strength of the contribution**: high *despite* the vendor genre. The KG-as-attention-direction framing is a genuinely new architectural primitive that the wiki's other knowledge-graph sources do not name. The 16-chapter live-demo format is unusually transparent for a vendor video — viewers can replicate the demo end-to-end from the screen recording.
- **Confidence: 0.72.** Per heuristic: single source, +0.05 for live-demo transparency, vendor-sponsored cap at 0.75. Will rise to 0.80+ if an independent practitioner reproduces the gap-analysis workflow.
