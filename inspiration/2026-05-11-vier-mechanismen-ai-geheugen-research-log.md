---
type: research-log
topic: "Hoe verhoudt de AI-wiki (Karpathy's LLM Wiki-patroon) zich tot RAG, knowledge graphs en lang contextvenster als mechanismen om een LLM van kennis te voorzien?"
date: 2026-05-11
output_target: "LinkedIn-artikel MT/CEO — hybride storyline (vendor-hook + architectuur-2×2 + repo-CTA)"
related_output: "inspiration/linkedin-post-mt-vier-mechanismen-ai-geheugen.md"
---

# Research log — Vier mechanismen, één label "geheugen"

## Niveau 0 — startvragen

1. **Welke vier mechanismen** worden onder de noemer "AI-geheugen" verkocht, en wat zegt elk wiki-concept (RAG / KG / LLM Wiki / contextvenster) feitelijk over hun werking?
2. **Hoe verhouden** die mechanismen zich op vijf executive-KPI's — kosten per query op schaal, drift over zes maanden, auditbaarheid bij fouten, portabiliteit/lock-in, en time-to-first-answer?
3. **Hoe resolveert** het "RAG is dead"-debat in de wiki — gaat het over de term of de techniek, en welke convergentie zien Raju, Liu en Huber/Chroma?

## Niveau 1 — pagina's uit `wiki/index.md`

Geselecteerd uit de index op basis van de drie startvragen:

- [[concepts/llm-wiki]] — voor Q1 (LLM Wiki-definitie), Q3 (RAG is dead-debat). Confidence 0.91, 5 sources.
- [[concepts/knowledge-graphs]] — voor Q1 (KG-definitie + GraphRAG), Q2 (drie genoemde failure-modes voor vector-only RAG). Confidence 0.87, 5 sources.
- [[concepts/agent-harness]] — voor Q1 (contextvenster via OS-analogie), Q2 (Chatterjee Compounding-laag = waardebehoud-as-KPI). Confidence 0.95, 20 sources.

### Antwoorden

- **Q1 — vier mechanismen, scherp benoemd:**
  - **Contextvenster** = "RAM — snel maar gelimiteerd"; "de ruwe LLM is de CPU — krachtig maar inert. Geen geheugen, geen storage, geen IO" (OS-analogie in [[concepts/agent-harness]], via Prompt Engineering YouTube, mei 2026).
  - **RAG / vector-retrieval** = "stateless"; "retrieves 3 chunks per query; fragments of the paper; no connections preserved; never compounds" ([[concepts/llm-wiki]], via Raju 2026). Drie failure-modes bij schaal: context-clash, context-confusion, dense-neighbourhood-degradation ([[concepts/knowledge-graphs]], via Martin/SurrealDB).
  - **Knowledge graph** = "heterogene grafen met getypeerde nodes en getypeerde edges als deterministische, queryable substraten voor AI-agent grounding" ([[concepts/knowledge-graphs]], Leskovec). "LLMs are very good storytellers — but if they don't have factual data or context, they are just going to hallucinate. The idea is to put them together — a very good storyteller generating answers, but a very good knowledge graph that as deterministic as possible generates good contexts" (Martin via [[concepts/knowledge-graphs]]).
  - **LLM Wiki / compiled wiki** = "knowledge management pattern where an LLM compiles raw source materials into a persistent, interlinked markdown wiki that the LLM owns and maintains. Knowledge compounds; the synthesis, the cross-references, the identified contradictions are built once and kept current, not re-derived on every query" ([[concepts/llm-wiki]]). Karpathy's canonieke analogie: "Your files are raw ingredients. The LLM Wiki is the cooked meal. With RAG, you cook every time you are hungry."

- **Q2 — vijf executive-KPI's:** beantwoord door (a) Raju's 10-dimensies vergelijkingstabel in [[concepts/llm-wiki]], (b) Martin's beslisregels in [[concepts/knowledge-graphs]], (c) Chatterjee's "model rented, harness owned" framing in [[concepts/agent-harness]]. De vijf KPI's blijken empirisch ondersteund:
  - **Kosten per query op schaal** — RAG: snelle vector-search, schaalbaar; Wiki: bijna-nul query-cost, hoge ingest-cost; KG: matig; contextvenster: nul marginal, hoge inference; "stable parts cached at the model's KV layer = sustainable cost curve vs bankrupting you" (Chatterjee).
  - **Drift over zes maanden** — Wiki heeft een expliciete `lint`-operatie hiervoor; contextvenster evaporeert per sessie; RAG: bronnen verouderen; KG: vereist ETL-refresh.
  - **Auditbaarheid bij fouten** — Wiki: "specific page citations"; RAG: "close in embedding space" (vaag); KG: deterministische traversal + uitleg. Drie van de vier scoren slecht op deze KPI.
  - **Portabiliteit / lock-in** — Geheugen is overdraagbaar tussen harnesses als het in hooks zit, vendor-locked als het in vendor-interne session state zit (Bratanic via [[concepts/agent-harness]]).
  - **Time-to-first-answer** — Contextvenster: direct; RAG/KG: matig; Wiki: matig-tot-langzaam (schaalt met grootte).

- **Q3 — "RAG is dead"-debat:** [[concepts/llm-wiki]] is hier eenduidig: *"The internet's 'RAG is dead' meta-debate is dismissed by both Raju and Liu as missing-the-point; they argue for **complement, not replace**."* Liu's faseschema: 2023 RAG → 2025 Wiki + Skills emerge → 2026+ convergence. De drie sources zijn convergent — Huber's bijdrage is dat het de **term** is die wordt afgeschaft, niet de techniek; nieuwe term: **context engineering**.

### Niveau-1 vervolgvragen

Van [[concepts/llm-wiki]]:
- 1.1. Wat zegt Huber/Chroma specifiek over wat met de **term** RAG gebeurt — en welke nieuwe term komt ervoor in de plaats?
- 1.2. Wat is Raju's exacte 10-dimensies vergelijkingstabel — kunnen we de KPI-cellen direct ontlenen?
- 1.3. Welke drie limitaties van LLM Wiki worden expliciet benoemd?

Van [[concepts/knowledge-graphs]]:
- 2.1. Welke specifieke vendor-lock-in scenario's noemt Bratanic voor knowledge graphs en agentic memory?
- 2.2. Hoe verhoudt Martin's beslisregel (vector-only vs KG) zich tot een MT-koopbeslissing?
- 2.3. Wat is de KG-ETL-pipeline volgens Martin — relevant voor "ingest-kost" als KPI?

Van [[concepts/agent-harness]]:
- 3.1. Hoe verhoudt Chatterjee's "model rented, harness owned" zich tot de KPI portabiliteit?
- 3.2. Wat is de "context rot" mechanisme specifiek (Kokane's 10% novel claim)?
- 3.3. Welke vendor-productisaties van het harness-laag bestaan al (Anthropic Managed Agents, Google Agents CLI) — bewijs dat dit een markt is, niet alleen theorie?

## Niveau 2 — links gevolgd

Geselecteerd voor vragen die het meest direct het artikel ondersteunen (MT-vendor-critique + architectuur-frame):

- [[2026-05-11-huber-chroma-rag-is-dead-agentic-search]] — voor 1.1 (term-vs-techniek).
- [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained]] — voor 1.2 (10-dimensies tabel) en 1.3 (drie limitaties).
- [[2026-05-08-bratanic-unified-agentic-memory-hooks]] — voor 2.1 en 3.1 (portabiliteit).

### Antwoorden

- **1.1 — Wat gebeurt met "RAG" als term (Huber/Chroma):**
  > *"RAG is dead — the term, not the technique. If you ask 25 people to define RAG, they'll all define it a slightly different way. RAG is banned. Oh by the way, vector database is also banned."*

  Vervangterm: **context engineering**. Drie failure-axes: too much / too little / confusing — strikte uitbreiding van SurrealDB's drie (clash / confusion / dense-neighbourhood). Empirische anker: Chroma's *Context Rot* rapport (45 pagina's, 2025): de "dumb zone" begint tussen 20.000 en 120.000 tokens, afhankelijk van use case. "I've not found anybody who really trusts a million tokens to do anything that's any kind of good."

  Bonus-vondst voor het artikel: Huber's structurele collapse: *"Memory is actually in some sense a task of context distillation. ... memory, context compaction, distillation — they're actually all the same thing once you unpack it."* — dit is **direct relevant voor de provocatie in het artikel**: "memory" is geen ding, het is een familie van bewerkingen.

- **1.2 + 1.3 — Raju's 10-dimensies tabel + drie limitaties:**
  10 dimensies (knowledge accumulation / cross-document synthesis / contradiction detection / retrieval explainability / infrastructure / scale / latency / real-time / human readability / multi-user / hallucination). Wiki wint op 6/10, RAG wint op 4/10. Drie expliciet benoemde limitaties van LLM Wiki:
  - **Scale ceiling** — Karpathy runt ~100 artikelen / 400.000 woorden; *"the 'bye-bye RAG' framing quietly assumes that what works at 100 pages works at 10,000. It does not."*
  - **Hallucination baking** — *"In RAG, that's a wrong answer. In the wiki, that's a wrong page that every future query trusts. Organized, persistent mistakes are harder to spot than individual errors."*
  - **Ingest is not free** — *"That work doesn't disappear — it moves to ingest. ... If your data changes frequently, re-ingesting to keep the wiki current is expensive."*

  Plus de eindslogan: *"Karpathy hasn't killed RAG. He's articulated something more important: that knowledge should compound, not evaporate."*

- **2.1 + 3.1 — Bratanic over portabiliteit:**
  > *"If you don't own your memory, you don't own your agent. Every harness today builds its own walled garden of context, preferences, and session history. Switch them and you start from zero."*

  Vijf hook-events zijn cross-vendor standaard (Claude Code / Codex / Cursor): SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop. Geheugen dat via hooks geschreven wordt is overdraagbaar; geheugen in vendor-interne session state is locked-in. Direct relevant voor de portabiliteit-KPI in het artikel.

  Bratanic's dream-phase markdown-wiki is structureel identiek aan Karpathy's LLM Wiki — dat sluit het architectuur-cirkel.

### Niveau-2 vragen

- A1. Wat is Liu's exacte drie-architectuur decision matrix (RAG / Wiki / Skills)?
- A2. Wat zegt OceanBase precies over "smart compilation" vs static appending?
- A3. Hoe verhoudt Manditereza's industriële-OT framing zich tot enterprise-MT-vragen?

## Niveau 3 — verkort

**Niveau 3 is bewust verkort uitgevoerd.** Reden:

- De drie Niveau-1 concept-pagina's plus drie Niveau-2 source-pagina's leveren al **verzadigd bewijs** voor de drie startvragen op. Verder lezen voegt geen nieuwe categorieën toe — alleen extra worked examples.
- Eerdere parallele Explore-agenten (zie research-paths 1–3 in `/Users/witoldtenhove/.claude/plans/i-want-to-write-cheeky-naur.md`) hebben Liu / OceanBase / SurrealDB-sources al gelezen en hun kernpunten in conversation-context geleverd. Niveau-3-vragen A1/A2/A3 zijn daarmee al beantwoord buiten deze formele query — dubbel werk vermijden.
- Het uiteindelijke output-formaat is een LinkedIn-artikel van ~1.800 woorden, niet een synthesis-pagina. Verdere bron-diepte zou de output niet rijker maken; alleen mijn context vullen.

**Wat in Niveau 3 wel meegenomen wordt (uit eerder agent-werk, niet uit nieuwe reads):**

- Liu's decision-driehoek RAG / Wiki / Skills met Karpathy's "rereads the same books for every exam, never actually learning the material" quote — gebruik in het artikel als RAG-quote.
- OceanBase's "knowledge should update itself when new information arrives, not just accumulate" — gebruik in het artikel als bewijs dat compiled wikis al in productie draaien bij vendors.
- Karpathy's Sequoia AI Ascent quote (29 april 2026): *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles ..."* — gebruik als bewijs dat de auteur van het patroon het zelf nog gebruikt.

## Synthese

Kern-elementen die in het LinkedIn-artikel worden verwerkt:

1. **Vier mechanismen scherp benoemd** met vendor-pitch-taal vs wiki-grounded reality (uit Niveau 1).
2. **Het 2×2 dat de keuze structureert:** synthesis time (ingest vs query) × state (stateless vs compounds). Dit is *niet* de "chunks vs typed" as die in de oorspronkelijke planschets stond — het wiki-eigen framing is sterker.
3. **5×4 KPI-tabel** met geciteerde brongegevens per cel (uit Niveau 1 + 2).
4. **"RAG is dead"-debat opgelost** met Huber's term-vs-techniek + drie-source convergentie op complement-not-replace (uit Niveau 2).
5. **Eerlijke architectuurkritiek** met drie limitaties van compiled wiki (Raju), plus Chroma's *Context Rot* empirische anker (20K-120K dumb zone) (uit Niveau 2).
6. **Karpathy lineage en eigen gebruik** (Niveau 1 + Niveau 3-via-agent), CLAUDE.md schema-laag als authoriteitsclaim, repo-URL als CTA.
7. **Maandagochtend-vraag** geconstrueerd uit Bratanic's "if you don't own your memory" + Chatterjee's "model rented, harness owned" → één diagnostische vraag over compounding én portabiliteit (uit Niveau 2).
8. **GIF-plaatsing:** `search-wiki.gif` na het 2×2 (compiled-wiki-zoals-mens-hem-ziet); `agent-wiki.gif` als climax onder de B-closer (compiled-wiki-zoals-model-hem-ziet).

## Bronnenmatrix

| Wiki-pagina | Gebruikte claim |
| ----------- | --------------- |
| [[concepts/llm-wiki]] | Drie-laag-architectuur (raw / wiki / schema); drie operaties (ingest / query / lint); compounding-vs-evaporation framing; "complement not replace" verdict; Karpathy's cooked-meal-analogie |
| [[concepts/knowledge-graphs]] | KG-definitie (heterogeneous graphs met typed nodes/edges); GraphRAG mechanic; Martin's drie failure-modes voor vector-only RAG; KG-ETL pipeline; "storyteller + knowledge graph" quote |
| [[concepts/agent-harness]] | OS-analogie (LLM = CPU, contextvenster = RAM); Chatterjee "model rented, harness owned"; vendor-productisaties (Anthropic, Google); hooks-as-portable-primitive |
| [[2026-05-11-huber-chroma-rag-is-dead-agentic-search]] | "RAG is dead — the term, not the technique"; vervangterm: context engineering; *Context Rot* dumb zone 20K-120K tokens; "memory ≈ context compaction" structurele collapse |
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained]] | 10-dimensies vergelijkingstabel; drie limitaties (scale ceiling / hallucination baking / ingest cost); Karpathy gist-statistieken (17M views); "compound not evaporate" slotzin |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks]] | Portabiliteit-claim: "if you don't own your memory, you don't own your agent"; vijf cross-vendor hook-events; dream-phase markdown-wiki als convergentiebewijs |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers]] (via eerdere agent-read) | Phase-timeline (2023 RAG → 2025 Wiki + Skills → 2026+ convergence); Karpathy "rereads books for every exam"; complement-not-replace |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks]] (via eerdere agent-read) | Vendor-implementatie bewijs; "knowledge should update itself when new information arrives, not just accumulate" |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] (via Niveau-1) | Karpathy's Sequoia continued-use quote (29 april 2026) — anker dat de auteur van het patroon het zelf nog gebruikt |

## Bron-diversiteit check

- Concept-pagina's geraadpleegd: 3 (llm-wiki / knowledge-graphs / agent-harness) — covers alle drie load-bearing concepts in de wiki.
- Source-pagina's geraadpleegd: 3 direct (Huber / Raju / Bratanic) + 3 indirect via eerdere agent-reads (Liu / OceanBase / Karpathy-Sequoia) = 6 unieke sources.
- Vantage-diversiteit: vendor-CEO (Huber/Chroma), conceptual-explainer (Raju/Medium), practitioner-implementer (Bratanic/Neo4j+TDS), vendor-implementation (OceanBase), comparative-architecture (Liu/AI Advances), upstream-spec author (Karpathy/Sequoia). **Zes vantages.**
- Convergentie-bewijs: drie onafhankelijke sources (Raju, Liu, Huber) komen uit op dezelfde conclusie ("complement, not replace") — sterk genoeg om als artikel-climax te dienen.

## Methodologie-notities voor toekomstige queries

- De drie startvragen waren goed gekozen: één definitievraag (Q1), één KPI-vergelijking (Q2), één debat-resolutie (Q3). Geen overlap; alle drie verschenen in afzonderlijke artikel-secties.
- Niveau 1 leverde **meer** dan ik verwachtte op de KPI-as: Raju's 10-dimensies tabel in [[concepts/llm-wiki]] is in feite al een mini-KPI-tabel — het artikel ontleent zes van de tien dimensies direct.
- Niveau 2 leverde **één onverwachte bonusvondst**: Huber's structurele collapse van memory ≈ context compaction ≈ distillation als dezelfde taak. Dit is direct relevant voor het artikel's provocatie en zat niet in de oorspronkelijke planschets.
- Plan-mode beperking: de iterative-wiki-query skill kon pas na exit-plan-mode draaien (schrijft naar inspiration/). Dit was geen probleem omdat het LinkedIn-artikel zelf ook pas na plan-approval geschreven kon worden — beide stappen vielen samen.
