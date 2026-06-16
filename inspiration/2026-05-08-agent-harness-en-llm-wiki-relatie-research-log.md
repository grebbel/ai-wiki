---
type: research-log
topic: "Hoe verhouden de concepten agent-harness en llm wiki zich tot elkaar?"
date: 2026-05-08
output_target: "Synthese-antwoord in chat (geen apart output-bestand)"
related_output: "n.v.t. — antwoord direct geleverd aan gebruiker"
---

# Research log — Relatie tussen agent-harness en llm wiki

## Niveau 0 — startvragen

1. Wat is een agent-harness en wat is een llm wiki — definities en kerneigenschappen?
2. Welke rol vervullen ze elk in een AI-werkstroom — overlap of complement?
3. Waar raken ze elkaar concreet — bevat het ene het andere, of zijn ze orthogonale lagen?

## Niveau 1 — pagina's uit `index.md`

Geselecteerd:
- `wiki/concepts/agent-harness.md` — voor Q1 + Q2 + Q3 (kerndefinitie en rol)
- `wiki/concepts/software-3.0.md` — voor Q3 (architecturale relatie expliciet benoemd)
- `wiki/sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` — voor Q1 + Q3 (Karpathy = upstream-spec auteur)
- `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` — voor Q2 (CLAUDE.md letterlijk genoemd als learning-capture)

### Antwoorden

- **Q1 (definities, agent-harness)**: Runtime engineering laag tussen foundation model en gebruiker. 4 lagen (Chatterjee 2026): Context / Constraints / Contracts / Compounding. OS-analogie (Prompt Engineering YouTube, mei 2026): LLM = CPU, context window = RAM, externe stores = disk, tool integraties = device drivers, **harness = OS**. 7 wiki-bronnen converging.
- **Q1 (definities, llm wiki)**: Een persistent, compounderend markdown-archief dat tussen rauwe bronnen en LLM zit. Drie lagen: raw / wiki / schema (CLAUDE.md). LLM doet alle bookkeeping; mens cureert bronnen, stelt vragen. *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."* (`llm-wiki.md` upstream spec van Karpathy).
- **Q2 (rol, harness)**: Production-runtime — assembleert context, valideert intent, draait tools, capt telemetrie voor zelf-verbetering. *"The model is rented; the harness is owned."* (Chatterjee 2026)
- **Q2 (rol, wiki)**: Cross-sessie kennis-capture en synthese. Niet RAG-style retrieve-on-query, maar **kennis één keer compileren en bijhouden**. Vier operaties: ingest / query / lint / synthesize.
- **Q3 (raakpunt, decisief)**: Software 3.0 (`software-3.0.md`) zegt expliciet — *"a Software 3.0 program needs a runtime; that runtime is the agent harness."* En Karpathy noemt **LLM knowledge bases / wikis built from documents** als named voorbeeld van een Software-3.0 productklasse zonder 1.0/2.0-antecedent. Dus: **een llm wiki IS een Software 3.0-programma, en de harness is wat eronder draait.**
- **Q3 (raakpunt, operationeel)**: Kiron-Schrage 2026 noemt **CLAUDE.md letterlijk** als voorbeeld van learning-capture — exact het mechanisme dat Chatterjee's *Compounding* laag operationeel maakt. *"Forcing that judgment into written standards, such as the way developers write CLAUDE.md files… makes the tacit explicit for colleagues and for AI alike."* En: *"version control for organizational judgment."*
- **Q3 (Karpathy bevestigt)**: 29 april 2026 in Sequoia AI Ascent: *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles… anytime I see a different projection onto information, I always feel like I gain insight."* En: *"a lot of prompts for me to do synthetic data generation kind of over some fixed data."* — De upstream-spec auteur gebruikt zelf nog steeds dit patroon.

### Niveau-1 vragen

Van `agent-harness.md`:
- 1.1 Hoe operationaliseert agentic-engineering de samenwerking tussen mens, harness, en wiki?
- 1.2 Wat zegt brain/hands/session over waar wiki-content "leeft" in een harness?
- 1.3 Wat zegt de upstream-spec (`llm-wiki.md`) over wat een wiki *is*?

Van `software-3.0.md`:
- 2.1 Wat is "synthetic data generation over fixed data" in wiki-operatie-termen?
- 2.2 Waar past de wiki in de OS-stack mapping?
- 2.3 Wat betekent "agent-native infrastructure" voor de wiki?

Van `karpathy-from-vibe-coding-to-agentic-engineering`:
- 3.1 Wat is een "projectie op informatie"?
- 3.2 Hoe past de "spec-design step" (Karpathy's plan-mode kritiek) in mens/harness/wiki?

Van `kiron-schrage-compound-benefits`:
- 4.1 Welke andere capture systems hebben wiki-analogen?
- 4.2 Hoe verhouden decision journals / prompt repositories zich tot threads/syntheses?

## Niveau 2 — links gevolgd

Geselecteerd:
- `wiki/concepts/agentic-engineering.md` — voor 1.1
- `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` — voor 1.2
- `llm-wiki.md` (repo root, upstream spec) — voor 1.3

### Antwoorden

- **1.1 (agentic-engineering)**: *"Agentic engineering is to the harness what software engineering is to the IDE — the discipline that uses the tooling to ship reliable systems."* Mens bezit spec/judgment/aesthetics/oversight; agents doen fill-in-the-blanks. **CLAUDE.md / repo-level skill files worden continu verfijnd** door top operators (genoemd: Boris Cherny, Anthropic, met 10–15 concurrent Claude instances). Tool-mastery is the new craft (Karpathy).
- **1.2 (brain/hands/session)**: Anthropic Managed Agents 8 april 2026 introduceert decompositie:
  - **Brain** = Claude + harness loop
  - **Hands** = sandbox + tools
  - **Session** = append-only event log buiten de container
  
  Kernzin: *"the session is a context object that lives outside the context window."* En: *"harnesses encode assumptions that go stale"* — de Sonnet 4.5 "context anxiety" patch werd dood gewicht zodra Opus 4.5 het probleem niet meer had. → Wiki = session-equivalent op cross-sessie / organisatie-niveau. Knowledge survives any single context window.
  
- **1.3 (upstream `llm-wiki.md` spec)**: Drie lagen (raw / wiki / schema) — exact dezelfde structuur die in dit repo's CLAUDE.md staat. Karpathy's framing: *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."* Memex-referentie (Vannevar Bush 1945): "The part he couldn't solve was who does the maintenance. The LLM handles that." → De wiki is geen statische database, het is een **gecompiled, self-maintaining artefact** dat per ingest 10–15 bestanden raakt.

### Niveau-2 vragen

Niet meer geformuleerd — bronnen voor deze specifieke relatie-vraag zijn uitgeput. Zie Niveau 3.

## Niveau 3 — verkort

**Verkort uitgevoerd.** De drie pagina's op Niveau 2 leverden de architectonische volledigheid die nodig was om de relatie te beantwoorden. Verder volgen van links zou herhaling opleveren — bijvoorbeeld het volgen van [[2026-05-07-chatterjee-anatomy-of-agent-harness]] zou opnieuw de Compounding-laag bespreken die al in Niveau 1 is uitgewerkt; volgen van [[2026-05-04-rethinking-agents-harness-is-all-you-need]] zou de OS-analogie herhalen die al in Niveau 1 / `agent-harness.md` is opgenomen.

De vraag is een **architectuur-relatie**, niet een empirische vraag — er is een verzadigingspunt waarbij verdere pagina's geen nieuwe relatie-claims meer toevoegen, alleen extra evidence voor reeds gevonden claims. Dat punt is hier bereikt na 7 pagina's (4 op N1 + 3 op N2).

## Synthese — kern-elementen verwerkt in antwoord

1. **Architecturale stapel (verticale relatie)**: Wiki ÍS een Software 3.0-programma; harness is wat het uitvoert. Karpathy noemt wiki's expliciet als named-voorbeeld van een Software 3.0-productklasse.
2. **Compounding-laag (horizontale verbinding)**: Chatterjee's 4e laag = Kiron-Schrage's flywheel = wat dit repo concreet doet via CLAUDE.md + log + lifecycle-frontmatter.
3. **Session-equivalent (durability-relatie)**: Anthropic's session-buiten-context-window heeft als organisationele tegenhanger de wiki — kennis die *elke individuele context window overleeft*.
4. **Karpathy's projectie-frasering**: "synthetic data generation over fixed data" en "different projections" leggen de 4 wiki-operaties (ingest/query/lint/synthesize) bloot als verschillende lees-modi op dezelfde fixed data.
5. **Concrete repo-instantiatie**: dit repo IS de relatie — de wiki content is het programma, Claude Code is de harness, CLAUDE.md is de stabiele Context-laag, hooks in `.claude/settings.json` is de Constraints-laag, lifecycle frontmatter is de Contracts-laag, de log + supersession-protocol is de Compounding-laag.
6. **Eigendoms-asymmetrie**: *"The model is rented; the harness is owned."* + *"the wiki is a persistent, compounding artifact"* = beide zijn modelonafhankelijke eigendomslagen. Modellen veranderen; harness en wiki blijven en worden waardevoller.

## Bronnenmatrix

| Wiki-pagina | Gebruikte claim |
| --- | --- |
| [[agent-harness]] | 4-laags taxonomie; OS-analogie; "model rented, harness owned"; Compounding-laag operationeel = Kiron-Schrage flywheel |
| [[software-3.0]] | Wiki = Software 3.0-product klasse; harness = runtime voor Software 3.0-programma's; mapping-tabel CPU/RAM/disk/OS naar Software 3.0 |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] | Karpathy 29 april 2026 bevestigt eigen wiki-workflow; "synthetic data generation over fixed data"; "different projection onto information" |
| [[2026-05-07-kiron-schrage-compound-benefits]] | CLAUDE.md letterlijk genoemd als voorbeeld van learning-capture; "version control for organizational judgment"; Boris Cherny pattern |
| [[agentic-engineering]] | "Agentic engineering is to the harness what software engineering is to the IDE"; spec-first; CLAUDE.md continu verfijnen |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]] | Brain/Hands/Session decompositie; "session is a context object that lives outside the context window"; "harnesses encode assumptions that go stale" |
| `llm-wiki.md` (repo root, upstream spec) | Drie-lagen architectuur; "wiki is the codebase"; Memex-erfgoed; LLM doet maintenance |
