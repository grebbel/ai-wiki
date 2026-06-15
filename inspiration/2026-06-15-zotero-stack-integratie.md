---
title: "Connecting the wiki to a local Zotero library"
date: 2026-06-15
status: notes
tags: [zotero, ingest, acquire, mcp, tooling, integration, reference-manager, infrastructure, provenance]
---

# Connecting the wiki to a local Zotero library

> Research + decision notes (not a wiki thread). Updates the May-2026 PRD (`2026-05-14-prd-zotero-stack-integratie.md`) with the Zotero 7 local-API reality. Lives in `inspiration/` — outside the Claude-owned `wiki/` contract.

## The question

Can the wiki read sources directly from a **local** Zotero instance so that adding a source no longer means hand-copying and converting files into `raw/` — and which integration shape does this *without* giving up the immutable-`raw/` provenance discipline that makes the wiki trustworthy?

Sub-questions:

- What does a *local* Zotero (no cloud account) actually expose to a program or an agent?
- Where does Zotero plug into the wiki's pipeline — does it replace `raw/`, feed `raw/`, or sit beside it as a live read surface?
- How do we scope the connection so only material the user *chooses* enters the wiki, not the whole personal library?
- Where do binary PDFs live once Zotero is in the loop — in git, or only in Zotero?
- What is the smallest build that captures the win, and what stays manual?

## Background — prior art in this repo

The May 2026 PRD (`2026-05-14-prd-zotero-stack-integratie.md` (sibling in `inspiration/`)) already scoped four options (A — Zotero-as-source / B — Zotero-as-mirror / C — MCP-on-the-wiki / D — full convergence) and recommended **A + C** in phasing. But it framed everything around the **cloud** Web API (`api.zotero.org`, per-account API keys) and the multi-tenant `ai-consultant` GCP/Firestore/Vertex stack. This thread **updates that PRD with the local-API reality**, which sharply lowers the cost of the "light" path and adds a cleaner option the PRD did not have.

## What we know so far

### Zotero 7 ships a read-only local HTTP API

Zotero 7 exposes `http://localhost:23119/api/` over the desktop app — **no API key, no cloud sync**. Enable it via *Settings → Advanced → "Allow other applications on this computer to communicate with Zotero"*; address the local library as `users/0`. It is GET-only (read-only) and covers item metadata, collections, tags, saved searches, **and the full text Zotero already extracted from PDF attachments**. `pyzotero` speaks to it directly via `Zotero(..., local=True)`. Write-back (creating items/attachments) is not in the native API and needs a community add-on — but the wiki only needs to read documents *in*, so that gap does not bite.

### Local-Zotero MCP servers now exist

Mature MCP servers point at exactly that local API — e.g. `54yyyu/zotero-mcp` (`ZOTERO_LOCAL=true`, no key; semantic + keyword search, metadata in markdown/BibTeX, PDF full-text, annotation extraction) and ZotPilot. This is a *different* thing from the PRD's "Optie C" (an MCP server on the *wiki*); this is an MCP server on *Zotero*. It lets any Claude session read the library live, copying nothing.

### Better BibTeX and the Obsidian-side ecosystem

Better BibTeX's *"Keep up to date"* auto-exports a collection to CSL-JSON/BibTeX on every change — useful underneath the acquire path to give stable citekeys and consolidated author names (directly attacking the wiki's alias-drift pain). Obsidian-side plugins (ZotLit, the Citations plugin) generate literature notes in the vault from Zotero, but they write *outside* the Claude-owned `wiki/` contract, so they are a parallel human-notes layer, not a Claude ingest path.

### `raw/` binaries are gitignored, not absent (corrected 2026-06-15)

An initial scan of the *committed* repo showed only markdown under `raw/`, and this thread first recorded that as "raw/ is markdown-only." **That was a git-only artifact and is wrong.** `.gitignore` deliberately excludes every raw binary — `raw/**/*.pdf`, `.docx`, `.epub`, `.mobi`, `.mp4`, `.mp3`, `.png`, … — *"kept local-only for copyright/distribution reasons."* The user's **local** `raw/` working copy does hold the original PDFs, **co-located by type** (e.g. `raw/articles/<slug>.pdf` next to its markdown). So the real convention is: keep the binary locally in its typed folder, gitignore it, and commit only the markdown stub + the citation that lets a reader of the public repo locate the original. (This also means CLAUDE.md's "keep the original PDF in `raw/assets/`" prose is the real drift — practice co-locates by type, not in `assets/`.) The Zotero acquire path fits this unchanged.

## Options considered

| Option | Plugs into | Effort | Key trade-off |
|---|---|---|---|
| MCP — live Zotero read (server on Zotero) | Query + front-half of Acquire | ~zero code | Reads whole library but copies nothing; no frozen snapshot by itself |
| Acquire script/skill (local API → `raw/` stub) | Acquire | small | Preserves immutability; still a 2-step (acquire→process) |
| Better BibTeX auto-export | Acquire (metadata feed) | zero (Zotero-side) | Flat export, metadata-centric; still needs Process |
| Obsidian plugin (ZotLit / Citations) | Human reading layer | zero (plugin) | Notes live outside the `wiki/` contract |
| PRD Optie B (Zotero-as-mirror) / D (convergence) | — | high | Re-defer per PRD §7; B needs heavy Zotero use, D needs multi-user |

## Decisions taken (2026-06-15)

1. **Pursue MCP (live read) + an Acquire skill (durable ingest)** — the PRD's A + C, updated for the local API. Discipline: *MCP for reading and exploring; a `raw/` stub for anything that becomes a wiki page.*
2. **Scope ingest to a single Zotero collection** (working name `→ ai-wiki`). The only path that lands material in the wiki is Acquire, and it reads that one collection — the wider library never syncs. The MCP may *read* the rest of the library, but it persists nothing.
3. **No binary committed to git — which is already the repo's design.** `.gitignore` excludes `raw/**/*.pdf` (and `.docx/.epub/.mp4/.png/…`), so the original never reaches GitHub. With Zotero in the loop, **Zotero's storage is the durable binary home**; the wiki commits only the markdown stub (full text from Zotero's index) + `zotero_item_key` + `doi`/`url` to re-fetch. A local PDF copy co-located in `raw/<type>/` is optional and, if kept, is gitignored automatically. (Open follow-up: reconcile CLAUDE.md's `raw/assets/` prose with the actual co-locate-by-type practice.)
4. **Source markdown routes by type** — paper → `raw/papers/<slug>.md`, article → `raw/articles/<slug>.md`, etc. (the type-based routing already in use; no special-casing).

## Build plan

**Part A — MCP runbook (runs on the user's machine, not the cloud session).** Enable the local-API checkbox; install `zotero-mcp`; register a `zotero` block in a repo-root `.mcp.json` alongside the existing qmd server (CLAUDE.md §Search, Route 3 pattern), `env: { ZOTERO_LOCAL: "true" }`; verify with a search of a known item.

**Part B — `zotero-acquire` skill (design, not yet built).** Canonical acquire-time skill (like `youtube-transcript-skill`): reads the chosen collection via the MCP/local API, dedups on `zotero_item_key`, and writes `raw/<type>/<slug>.md` with a canonical frontmatter contract (title, authors, year/date_published, doi/isbn/url, abstract, full text) — then normal Process runs. Adds a CLAUDE.md *Verifying sources before ingest → Pre-flight check (Zotero stubs)* subsection with the Zotero→source-page field mapping, paralleling the videos contract. Acquire-only batches log as `acquire | zotero-batch …` (the v0.9 `acquire` op fits exactly).

## Open questions

- **Collection mechanism**: a dedicated collection (drag-drop, recommended) vs a saved search (auto-membership by tag, e.g. `tag:wiki`) vs a plain tag.
- **Full-text quality**: Zotero's extracted text (no structure) is good enough for most ingests; for marquee papers, still run `marker` for clean markdown. Per-source-class policy TBD.
- **MCP scope**: leave the live MCP whole-library (read-only exploration) or constrain it to the collection too?
- **Logging cadence**: confirm `acquire | zotero-batch …` for stub-only runs; `ingest | …` when Acquire+Process happen together.

## Definition of done

This work is complete when (a) the Zotero MCP is registered and verified on the user's machine, and (b) the `zotero-acquire` skill + the CLAUDE.md pre-flight subsection have landed and ≥3 collection items have been acquired and processed end-to-end. End state: a CLAUDE.md §Acquire update documenting the Zotero acquire path as a first-class ingest channel.

## References

- Prior PRD: `2026-05-14-prd-zotero-stack-integratie.md` (sibling in `inspiration/`) (+ the three `…-stack-*.excalidraw` diagrams).
- Wiki schema: `CLAUDE.md` §Ingest (Acquire/Process split, the `acquire` op), §Search (the qmd `.mcp.json` registration pattern), §Verifying sources before ingest (the videos frontmatter contract this would parallel).
- Zotero local HTTP API — [dev announcement](https://groups.google.com/g/zotero-dev/c/ElvHhIFAXrY/m/fA7SKKwsAgAJ); [pyzotero docs](https://pyzotero.readthedocs.io/en/latest/).
- MCP servers — [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp); [ZotPilot](https://forums.zotero.org/discussion/130483/).
- [Better BibTeX](https://retorque.re/zotero-better-bibtex/); [ZotLit guide](https://effortlessacademic.com/connecting-zotero-and-obsidian-with-the-zotlit-plugin-templates/).
