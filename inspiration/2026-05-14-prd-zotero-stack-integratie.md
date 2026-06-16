---
title: "PRD — Zotero-stack-integratie met ai-wiki"
date: 2026-05-14
status: draft
tags: [prd, zotero, ai-consultant, ai-wiki, architectuur]
sources:
  - ../../../ai-consultant/docs/product/2026-05-14-strategisch-overzicht.md
  - ../../../ai-consultant/docs/domain/zotero-integration-tdd.md
---

# PRD — Zotero-stack-integratie met ai-wiki

> **Doel van dit document.** Op de tafel ligt de **Zotero-stack** uit `ai-consultant` Spoor 2 (Plans 13–18, april 28–30; zie [strategisch overzicht](../../../ai-consultant/docs/product/2026-05-14-strategisch-overzicht.md) §2 *Spoor 2*) — een multi-tenant, multi-account, agent-gerichte bronnen-pijplijn op GCP. Daarnaast staat de persoonlijke **ai-wiki**: een single-user, markdown-in-git, Quartz-gepubliceerde wiki met handmatige ingest-discipline. Dit PRD inventariseert vier integratie-opties, scoort elk op feasibility, maintenance en value, en eindigt op een gefaseerd aanbevolen pad.

---

## 1. Context en probleem

Beide systemen zijn knowledge-management-systemen, maar gebouwd voor tegenovergestelde gebruiks-modellen:

| Dimensie | ai-wiki (deze repo) | ai-consultant Zotero-stack |
|---|---|---|
| Gebruikers | 1 (auteur = lezer) | n (consultants per tenant) |
| Source-of-truth | git + markdown | Firestore (`BibliografischeBron`) |
| Schrijver | Claude in-session | `zotero-sync-job` Cloud Run Job |
| Hoofd-lezer | Mens (Obsidian + Quartz site) | LLM-agents (via MCP) |
| Schema-bewaking | Hooks (`scripts/lint-page.mjs`) | Pydantic v2 + Firestore-rules |
| Citatie-werk | Handmatig `wiki/sources/`-frontmatter | Zotero → `BibliografischeBron` auto-sync |
| Retrieval | FlexSearch (build-time) | Vertex AI RAG (runtime, per tenant) |
| Provenance-discipline | Body-wikilink + frontmatter-relationships | `bibliografische_bron_id` + axioma 7-gate |
| Levenscyclus-velden | `confidence`, `source_count`, `last_confirmed` | `version_chain`, `superseded`-merge |

De **schema-congruentie** is opvallend groot: Zotero's `BibliografischeBron` (titel, auteurs, jaar, DOI, ISBN, URL, attachment-pad) komt direct overeen met de bestaande [wiki source-page-conventie](../CLAUDE.md#source-page-conventions-specific-to-videos). Dat maakt schema-mapping eerder verlies-arm dan dubbelop.

De **divergentie zit in de lezer**: de wiki optimaliseert voor menselijke narratieve cohesie (Claude synthetiseert tot lees-bare concept-pagina's); de Zotero-stack optimaliseert voor agent-toegang met provenance-injectie (`zotero-mcp` injecteert `bron`-string en `betrouwbaarheid` bij elke RAG-passage).

Vraag van dit PRD: **welke onderdelen van de Zotero-stack-architectuur zijn waardevol voor de ai-wiki, zonder de "markdown-in-git is alles"-discipline op te geven die de wiki vandaag bruikbaar maakt?**

## 2. Doelen en niet-doelen

**Doelen.**
- G1. Manueel werk bij ingest verminderen — vooral het opmaken van `wiki/sources/`-frontmatter voor papers, artikelen en boeken waarvan citatie-metadata al elders bestaat.
- G2. Een pad creëren naar machine-leesbaarheid van de wiki — zodat Claude (en eventueel andere agents) de wiki kunnen bevragen als getypeerde knowledge-graph in plaats van als markdown-bestanden.
- G3. Optionele afstemming met de ai-consultant-stack zodat schema-leerpunten overdraagbaar zijn (en omgekeerd).
- G4. Geen verlies van publicatie-vermogen (Quartz → GitHub Pages moet blijven werken).

**Niet-doelen.**
- N1. Het maken van ai-wiki multi-user. De wiki blijft personal in v1.
- N2. Het opgeven van markdown-in-git als waarheid. Git-history en diff-baarheid zijn niet onderhandelbaar.
- N3. Het runnen van ai-consultant-Cloud-Run-services voor de wiki. GCP-infra voor een single-user-wiki is overkill.
- N4. RAG over de hele wiki vandaag. FlexSearch (Quartz) is goed genoeg voor de huidige corpus-grootte (≈26 concepts, 81 entities, 62 sources).

## 3. Huidige situatie ai-wiki

> **Diagram 1** — [`2026-05-14-prd-zotero-stack-integratie-architectuur.excalidraw`](2026-05-14-prd-zotero-stack-integratie-architectuur.excalidraw) (open in VS Code met de [Excalidraw-extensie van pomdtr](https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor)).

De pipeline is bewust simpel: `raw/` (immutable) → Claude leest → `wiki/` (LLM-owned markdown) → Quartz build → GitHub Pages. Hooks (`scripts/lint-page.mjs`, `session-end.mjs`) bewaken schema en regenereren `wiki/.graph.json`. Geen runtime-services; alle "intelligence" zit in Claude-sessies en in de schema-discipline van [`CLAUDE.md`](../CLAUDE.md).

Pijnpunten vandaag:

- **Ingest-frictie.** Een paper of artikel toevoegen vraagt: PDF in `raw/papers/` zetten, slug bedenken, source-page schrijven met handmatig getypte frontmatter (titel, auteurs, jaar, DOI), entities/concepts updaten, `index.md` en `log.md` bijwerken. Tijd: ≈20–40 minuten per source.
- **Citatie-metadata niet gestandaardiseerd.** Auteurnamen lopen uiteen (`Brynjolfsson` vs `Erik Brynjolfsson`); aliassen werken maar zijn handmatig.
- **Geen tool-toegang voor andere sessies.** Een Claude-sessie buiten deze repo kan de wiki alleen via file-reads bereiken — geen typed graph-query.

## 4. Referentie — Zotero-stack uit ai-consultant Spoor 2

> **Diagram 2** — [`2026-05-14-prd-zotero-stack-referentie.excalidraw`](2026-05-14-prd-zotero-stack-referentie.excalidraw).

Korte recap (volledig in [`zotero-integration-tdd.md`](../../../ai-consultant/docs/domain/zotero-integration-tdd.md)):

- **`api.zotero.org`** = curated source. Per consultant een eigen account, eigen API-key (in Secret Manager).
- **`zotero-sync-job`** (Cloud Run Job, 15min-cadans) trekt items, normaliseert dedup-sleutels (DOI → ISBN → URL-canonical → Zotero item key), mirror naar Firestore + GCS.
- **`zotero-webdav`** (Cloud Run) accepteert WebDAV-push voor PDF-bytes vanuit Zotero-client.
- **`zotero-converter`** consumeert Pub/Sub-events (`zip → canonical → RAG-import`).
- **`zotero-mcp`** is de enige agent-interface (5 tools: `search_bronnen`, `get_bron`, `find_by_doi`, `resolve_attachment`, `rag_query`). Injecteert `bron`-string en `betrouwbaarheid` in elke return — agents kunnen niet hallucineren over provenance.
- **Vertex AI RAG** is per-tenant corpus, replayable vanaf Firestore.

Drie principes uit ADR-004 en ADR-009:

1. Firestore is SoT; `api.zotero.org` is upstream maar niet kritiek pad voor agents.
2. MCP is **enige** agent-interface (geen directe HTTP-calls vanuit agents).
3. RAG-corpus is afgeleid — reindex via Cloud Run Job.

## 5. Integratie-opties

> **Diagram 3** — [`2026-05-14-prd-zotero-stack-opties.excalidraw`](2026-05-14-prd-zotero-stack-opties.excalidraw).

### Optie A — Zotero-als-source (light ingest-laag)

**Idee.** Voeg Zotero toe als één extra ingest-bron-type, parallel aan de bestaande `articles/`, `papers/`, `videos/`. Een klein script (`scripts/zotero-sync.mjs` of `.py`) gebruikt `pyzotero` om items uit een door de gebruiker geconfigureerd Zotero-account te trekken; voor elk nieuw item schrijft het script een markdown-stub in `raw/articles/<slug>.md` (of `raw/papers/`) met YAML-frontmatter (titel, auteurs, jaar, DOI, URL, abstract). Bijbehorende PDF wordt naar `raw/papers/<slug>.pdf` gedownload.

Daarna volgt de **normale ingest-flow** (Claude leest, schrijft `wiki/sources/<date>-<slug>.md`, update entities/concepts, update `index.md` en `log.md`).

**Architectuur-delta.**
- 1 script (~150 regels Python of JS).
- Eén optionele config file (`.zotero-config.json`, gitignored): account-ID, API-key, sync-collectie.
- Geen GCP, geen Cloud Run, geen Firestore, geen RAG. De wiki blijft markdown-in-git.

**Wie blijft auteur.** Claude blijft auteur van de wiki-laag. Zotero is alleen vóór-de-raw-grens.

**Waar het waarde toevoegt.** Voor papers en artikelen met sterke citatie-data (DOI, peer-reviewed journals) bespaart het script ≈10–15 minuten frontmatter-werk per ingest. Auteurnamen komen geconsolideerd uit Zotero — minder alias-drift.

**Waar het waarde mist.** Voor video's en HTML-clipper-artikelen (geen DOI) verandert er weinig; die ingest-paden blijven zoals ze zijn. Verbetert *niet* de query-flow.

### Optie B — Zotero-als-mirror (deep schema-share)

**Idee.** Maak Zotero de source-of-truth voor `wiki/sources/`. Het sync-script schrijft niet stubs in `raw/`, maar genereert direct `wiki/sources/<date>-<slug>.md`-pagina's met volledige frontmatter (gemapped uit het `BibliografischeBron`-schema). Claude vult dan alleen nog de body (TL;DR, what was actually ingested, linked entities) en doet de cross-cutting updates.

**Architectuur-delta.**
- Volledige schema-mapping tussen `BibliografischeBron` (Pydantic) en wiki-source-frontmatter (YAML).
- Two-way conflict-policy: wat als Claude de frontmatter wijzigt en Zotero ook? Default: Zotero wint voor citatie-velden (titel, auteurs, DOI); wiki wint voor wiki-eigen velden (`confidence`, `tags`, `aliases`, `last_confirmed`).
- Nieuwe hook: `scripts/lint-zotero-drift.mjs` — detecteert frontmatter die niet meer synct met Zotero.

**Wie blijft auteur.** Verdeeld: Zotero is auteur van citatie-data; Claude blijft auteur van narratieve body. Provenance-discipline van [§Lifecycle in CLAUDE.md](../CLAUDE.md#lifecycle) moet uitgebreid worden met "wat is door Zotero geschreven vs. handmatig getypt".

**Waar het waarde toevoegt.** Sterk voor zware citatie-werkstromen (≥5 nieuwe bronnen per week, veel papers met DOI's). Multi-author-aliassen kunnen direct van Zotero komen — geen `aliases:`-lijsten meer onderhouden.

**Waar het waarde mist.** Voor de huidige cadans (≈12 sources per maand, gemixt video/article/paper) is de schema-onderhoudslast groter dan de besparing. Two-way conflict-policy is moeilijk om robuust te krijgen voor één gebruiker.

### Optie C — MCP-server op de wiki (read-only agent-toegang)

**Idee.** Bouw een lokale MCP-server (`wiki-mcp`, stdio-transport) die de wiki als getypeerde knowledge-graph exposeert aan elke Claude-sessie die hem connect. De server leest:
- `wiki/**/*.md` (frontmatter via gray-matter)
- `wiki/.graph.json` (al gegenereerd door [`scripts/graph-export.mjs`](../scripts/graph-export.mjs))
- Optioneel FlexSearch-index uit een Quartz-build

**Tools.**

| Tool | Argument | Return |
|---|---|---|
| `search_wiki` | `{q, type?, top_k=10}` | lijst page-summaries (slug, type, confidence, snippet) |
| `get_page` | `{slug}` | volledige page (frontmatter + body) |
| `related` | `{slug, edge_type?}` | typed neighbours uit `relationships:` |
| `graph_neighbors` | `{slug, depth=1}` | walk over body-wikilinks (bidirectioneel) |
| `list_threads` | `{open=true}` | open threads voor synthese |
| `find_by_alias` | `{name}` | entity-page via `aliases:` |

**Architectuur-delta.**
- 1 lokale Node.js of Python MCP-server (≈300 regels), in `tools/wiki-mcp/`.
- Toevoeging aan `~/.config/claude/mcp.json` (stdio-binding).
- Geen wijziging aan de wiki zelf.

**Wie blijft auteur.** Niemand verandert. Dit is een lezer-laag, geen schrijver-laag.

**Waar het waarde toevoegt.** Een Claude-sessie buiten deze repo (bijv. een sessie in `ai-consultant` of `straor-ond-workshop`) kan de wiki bevragen met typed tools — geen file-reads, geen full-corpus-grep. Maakt cross-repo synthese realistisch (bijv. "vind alle wiki-concepts die contradicteren met een claim die de gebruiker maakt"). Aligneert met ai-consultant's ADR-009: MCP is enige agent-interface.

**Waar het waarde mist.** Verbetert *niet* de ingest-flow. Voor sessies die in `ai-wiki` zelf draaien is file-access via `Read` al snel genoeg.

### Optie D — Volledige convergentie (ai-wiki = tenant in ai-consultant-stack)

**Idee.** De wiki wordt één tenant in de bestaande ai-consultant-infrastructuur. Firestore vervangt git als source-of-truth voor `wiki/concepts/` en `wiki/entities/`. GCS slaat attachments op. Vertex RAG draait over de hele corpus. Een `wiki-mcp`-service (Cloud Run) exposeert tools naast `zotero-mcp`. Git en Quartz blijven bestaan als **export-laag** voor de publieke site.

**Architectuur-delta.**
- GCP-project, IAM, Workload Identity, Secret Manager.
- Schema-migratie: alle `wiki/**/*.md` → Firestore-documenten (≈170 pages).
- Continue 2-way sync git ↔ Firestore (of: git wordt read-only export).
- Verlies van "markdown-in-git is alles"-discipline: pages bestaan eerst in Firestore, daarna in git.

**Wie blijft auteur.** Onduidelijk; Claude schrijft Firestore via wiki-mcp, of via een nieuwe `wiki-sync-job`. Diff-baarheid via git wordt commit-na-sync ipv commit-bij-edit.

**Waar het waarde toevoegt.** Multi-user (niet in scope, zie N1). Cross-tenant agent-toegang (niet in scope). Eén schema voor twee projecten.

**Waar het waarde mist.** Voor één gebruiker met één wiki is dit overdreven infrastructuur. De kosten (GCP-billing, IAM-onderhoud, schema-sync-debugging) staan niet in verhouding tot de baten.

## 6. Scoring

Schaal 1–10 per dimensie. Totaal is som (max 30).

| Optie | Feasibility | Maintenance | Value | **Totaal** |
|---|:---:|:---:|:---:|:---:|
| A — Zotero-als-source | **8** (1 script, bestaande libraries) | **9** (script-only, geen runtime) | **6** (ingest-besparing, geen query-winst) | **23** |
| B — Zotero-als-mirror | 6 (schema-mapping, conflict-policy) | 5 (two-way sync onderhoudslast) | 8 (hoog *mits* aktief Zotero-gebruik) | 19 |
| C — MCP-server op de wiki | **8** (300-regel MCP, `wiki/.graph.json` bestaat al) | **7** (lokaal, geen GCP) | 7 (cross-repo agent-toegang) | **22** |
| D — Volledige convergentie | 3 (GCP-infra, schema-migratie) | 2 (twee systemen-of-record) | 3 (overkill voor 1 user) | 8 |

**Waarom A en C dicht bij elkaar liggen.** Beide zijn composeerbaar, lokaal, niet-invasief voor het wiki-schema. Ze adresseren **verschillende** pijnpunten: A verbetert ingest, C verbetert query/cross-repo-toegang. Geen van beide blokkeert de ander.

**Waarom B onder C zakt.** B's value-cap is hoog (8) maar conditioneel op aktief Zotero-gebruik dat vandaag niet bestaat. Maintenance-kost (5) is bovendien voor altijd. C heeft een lagere value-cap maar onvoorwaardelijk.

**Waarom D onder de drempel valt.** Drie negatieve factoren tegelijk: GCP-infra opzetten, schema verliezen, en geen multi-user-payoff binnen scope. Pas heroverwegen als N1 (single-user-constraint) verdwijnt.

## 7. Aanbeveling — A + C in fasering

**Fase 1 (week 1–2): Optie A — Zotero-als-source.**

1. Voeg `scripts/zotero-sync.mjs` toe — `pyzotero`-wrapper die items uit een geconfigureerde Zotero-collectie naar `raw/articles/` of `raw/papers/` schrijft.
2. Schema voor de raw stub: YAML-frontmatter met `title`, `authors`, `year`, `doi`, `isbn`, `url`, `abstract`, `zotero_item_key`. Body krijgt `[[YouTube-style description blockquote]]`-equivalent als Zotero een abstract heeft.
3. Documenteer in `CLAUDE.md` een nieuwe subsectie *Verifying sources before ingest → Pre-flight check: Zotero-stubs* met velden-mapping en pre-flight check.
4. Eerste smoke-test: ≥3 papers uit een testaccount syncen, normaal ingest-en door Claude.

**Fase 2 (week 3–4): Optie C — MCP-server op de wiki.**

1. Maak `tools/wiki-mcp/` met TypeScript MCP-server (stdio-transport, gebruik `@modelcontextprotocol/sdk`).
2. Implementeer de zes tools uit §5 Optie C. `wiki/.graph.json` wordt gelezen door `graph_neighbors` en `related`.
3. Voeg de MCP-binding toe aan de gebruiker's `~/.config/claude/mcp.json` (gedocumenteerd, niet auto-installed).
4. Smoke-test: open een Claude-sessie buiten deze repo, vraag "wat zegt de wiki over [[Erik Brynjolfsson]]" — verifieer dat `find_by_alias` + `get_page` + `related` werken.

**Fase 3 (open, conditioneel): heroverweeg B en D.**

- **B (mirror)** wordt aantrekkelijk als de gebruiker Zotero-aktief gaat gebruiken (>5 nieuwe bronnen/week voor minstens 4 weken). Trigger: handmatig.
- **D (convergentie)** wordt pas relevant als N1 vervalt (wiki wordt multi-user) of als de Zotero-stack uit ai-consultant ergens een tenant nodig heeft die ai-wiki zou kunnen zijn. Trigger: extern.

## 8. Risico's en mitigaties

| Risico | Kans | Impact | Mitigatie |
|---|---|---|---|
| Zotero-sync produceert duplicate `raw/`-files (zelfde paper twee keer in Zotero) | Midden | Laag | Dedup op `zotero_item_key` in `raw/`-frontmatter; script skipt bestaande items. |
| `wiki-mcp` raakt out-of-sync met `wiki/` na een edit | Laag | Laag | Geen cache; alle reads zijn live op disk. `wiki/.graph.json` is al gehookt via [`scripts/session-end.mjs`](../scripts/session-end.mjs). |
| MCP-tools verleiden Claude om body-wikilinks te overslaan ("ik gebruik gewoon de tool") | Midden | Midden | Body-wikilink-rule in [CLAUDE.md §Graph](../CLAUDE.md#body-wikilink-rule-load-bearing) blijft contract. Lint blokkeert frontmatter-only relationships. |
| Schema-drift Zotero `BibliografischeBron` ↔ wiki source-frontmatter | Laag (A) / Hoog (B) | Midden | A: niet relevant (raw-stub is tussenstap). B: dedicated hook. |
| Auteurnamen uit Zotero matchen niet met wiki-aliases | Midden | Laag | Eerste-pre-flight-check in A-script: vergelijk `authors:` met bestaande `wiki/entities/`-aliases; report-only. |

## 9. Open vragen

- **V1.** Welk Zotero-account is de doel-account voor Fase 1 — een persoonlijke library of een nieuwe shared library? *(Beslissing voor uitvoering, niet voor dit PRD.)*
- **V2.** Wil de gebruiker dat het sync-script bij elke run een log-entry prepended naar `wiki/log.md` (`op: ingest-zotero-batch`), of blijft logging een handmatige Claude-handeling? *(De [hook-non-negotiable-regel in CLAUDE.md §Hooks](../CLAUDE.md#non-negotiable-rule) verbiedt hook-writes aan content-pagina's; `log.md` is grenzgebied — vandaag handmatig.)*
- **V3.** Voor `wiki-mcp`: tools per default read-only, of een opt-in write-tool (`save_synthesis(slug, frontmatter, body)`)? Default-aanbeveling: read-only in v1; write-tool pas in v2 met expliciete user-approval-flow.
- **V4.** Hoort dit PRD ook in `wiki/threads/`? *(Voorstel: ja, als `wiki/threads/zotero-stack-integratie.md` met `derived_from`-link naar dit `inspiration/`-document. Synthese later als Fase 1+2 zijn uitgevoerd.)*

## 10. Verwijzingen

- Bron: [`ai-consultant/docs/product/2026-05-14-strategisch-overzicht.md`](../../../ai-consultant/docs/product/2026-05-14-strategisch-overzicht.md) §2 *Spoor 2 — Zotero-stack*.
- Architectuur: [`ai-consultant/docs/domain/zotero-integration-tdd.md`](../../../ai-consultant/docs/domain/zotero-integration-tdd.md).
- Plans 13–18: zie [`ai-consultant/docs/product/plans/`](../../../ai-consultant/docs/product/plans/) (`2026-04-28-plan-13-zotero-backend-sync.md` t/m `2026-04-30-plan-18-zotero-webdav-converter.md`).
- Wiki-schema: [`../CLAUDE.md`](../CLAUDE.md).
- Diagrammen (open in VS Code met de [Excalidraw-extensie](https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor)): [`…-architectuur.excalidraw`](2026-05-14-prd-zotero-stack-integratie-architectuur.excalidraw), [`…-referentie.excalidraw`](2026-05-14-prd-zotero-stack-referentie.excalidraw), [`…-opties.excalidraw`](2026-05-14-prd-zotero-stack-opties.excalidraw).
