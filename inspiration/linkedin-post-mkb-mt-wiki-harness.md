# Plan: LinkedIn-post over robuustere AI met een wiki in de agent harness

## Context

Je hebt een AI research-agent gebouwd die kennis ophaalt uit een persoonlijke wiki (architectuur uit `inspiration/Agent Memory Systems and Decision Tree.md`). Voor LinkedIn wil je MKB-MT's overtuigen dat een wiki-laag in de agent harness AI **robuuster** maakt — minder hallucinatie, meer institutioneel geheugen, betere reproduceerbaarheid.

CTA staat vast: *"Nodig me uit voor een kop koffie en laat me je helpen bij je AI groei!"* Drie totaal verschillende versies, SCQA-flow impliciet (geen letterlijke labels), en de inhoud verdiept met cijfers/quotes uit de wiki via een methodische zoektocht (4 niveaus diep).

## Persona

**"Mark / Maaike de Vries — Algemeen of Operationeel Directeur, MKB"**

- 42–55 jaar, MKB met 20–200 medewerkers (zakelijke dienstverlening, productie, of gespecialiseerde handel)
- Heeft Microsoft Copilot of ChatGPT Enterprise uitgerold óf overweegt het serieus
- Pijnpunten op LinkedIn-tijd (07:30 of 17:00):
  - "Mijn mensen gebruiken AI, maar elk antwoord is anders — kan ik hier processen op bouwen?"
  - "Onze senior collega gaat met pensioen — al haar kennis loopt mee de deur uit"
  - "Wat doe ik als de hype voorbij is en ik nog steeds geen ROI heb?"
- Leest geen technische jargon — wel: concrete voorbeelden, een verhaal, en iemand die het zelf heeft gedaan

## Methodologie van de wiki-query

Voor elke versie (V1/V2/V3) is dezelfde 4-niveau iteratie gevolgd:

```
Level 0:  3 startvragen formuleren over het onderwerp
   ↓
Level 1:  uit wiki/index.md de 3 meest waarschijnlijke pagina's selecteren
          → openen, lezen, antwoorden onthouden
          → per pagina 3 nieuwe vragen genereren
   ↓
Level 2:  per vraag de meest waarschijnlijke link kiezen
          → openen, lezen, antwoorden onthouden
          → 3 nieuwe vragen genereren
   ↓
Level 3:  laatste keer links volgen, antwoorden onthouden
   ↓
Synthese: alle verzamelde antwoorden → contentversie
```

---

# DEEL A — RESEARCH LOG (apart opgeslagen)

## A1 — Versie 1 (Hallucinatie / Risico)

### Level 0 — 3 startvragen

1. **Waarom geven AI-modellen inconsistente of onjuiste antwoorden in productie?**
2. **Hoe groot is het probleem (cijfers, incidenten, frequentie)?**
3. **Welke architectonische ingreep maakt AI demonstreerbaar betrouwbaarder?**

### Level 1 — geselecteerde pagina's en antwoorden

Pagina's gekozen uit `wiki/index.md`:
- `wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md` — voor Q1 + Q3
- `wiki/sources/2026-04-30-ai-index-report-2026.md` — voor Q2
- `wiki/concepts/agent-harness.md` — voor Q1 + Q3

**Antwoorden:**

- **Q1** (Chatterjee): AI-fouten in productie zijn meestal **harness-fouten, geen modelfouten**. De Friday-in-March-casus: prompt was *"clean things up before the board review"*; agent archiveerde stale documenten, verwijderde duplicaten, ruimde "ongebruikte" bronnen op — en verloor 2 weken aan onderzoek 40 minuten voor een boardmeeting. Quote: *"The model was not the problem... The problem lived in the layer around the model — the layer that should have recognized 'clean up' as a destructive intent."*
- **Q2** (AI Index 2026): organisatie-adoptie 88% (van 78% in 2024). Gedocumenteerde AI-incidenten **233 (2024) → 362 (2025) — +55,4% YoY**. SWE-bench 60% → ~100% in één jaar; OSWorld agents 12% → 66%. Maar: agent-deployment in **enkele cijfers per bedrijfsfunctie**.
- **Q3** (agent-harness concept): 4-laagse anatomy van Chatterjee — Context / Constraints / Contracts / Compounding. Quote: *"The model is rented; the harness is owned."*

### Level 1 — 3 nieuwe vragen per pagina

Van Chatterjee:
- 1.1 Wat doen pre-tool en post-tool hooks precies?
- 1.2 Hoe werkt "intent validation" technisch?
- 1.3 Waarom werken agents in demo's en breken ze in productie?

Van AI Index 2026:
- 2.1 Welke incident-types zijn gedocumenteerd?
- 2.2 Hoe vaak rapporteren leveranciers RAI-benchmarks?
- 2.3 Wat is de tegenstrijdigheid tussen RAI-dimensies?

Van agent-harness:
- 3.1 Wat is "context rot"?
- 3.2 Wat is het verschil tussen frameworks (Layer 2) en runtime (Layer 3)?
- 3.3 Wat is "security as structural unreachability"?

### Level 2 — gevolgde links en antwoorden

Geselecteerde pagina's:
- `wiki/concepts/responsible-ai.md` — voor 1.3 + 2.1 + 2.2 + 2.3
- `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` — voor 1.2 + 3.3
- `wiki/sources/2026-05-07-kokane-agent-harness-vs-systems-design.md` — voor 3.1 + 3.2

**Antwoorden:**

- **1.3** (responsible-ai): Demo's gebruiken brave inputs; productie heeft destructieve verbs ("clean up", "consolideer", "schoon op") die de Constraints-laag moet onderscheppen. Drie-laagse RAI-runtime-taxonomie: architecturaal (brain/hands/session) + middleware (intent + isolatie + loop-detectie) + output-evaluatie (contracts).
- **2.1** (responsible-ai): Pakistan deepfake (Imran Khan), VS spamouflage-campagne, ZA potholed-roads-deepfake (DA), Uruguay AI-hologram debat. AI-misinformatie in **>12 landen / >10 platformen** in 2024. McKinsey RAI-survey: top-risico's *inaccuracy 64% / regulatory 63% / cybersecurity 60%* — maar mitigatie blijft achter.
- **2.2** (responsible-ai): Major frontier developers publiceren zelden gestandaardiseerde RAI-benchmarks. Foundation Model Transparency Index steeg van 37% (okt 2023) → 58% (mei 2024).
- **2.3** (responsible-ai): AI Index 2026 nieuwe finding: *"improving one RAI dimension (e.g., safety) can degrade another (e.g., accuracy)"* — multi-objective tradeoff, geen additieve verbetering.
- **1.2** (Anthropic Managed Agents): Brain/hands/session decoupling. Brain emit alleen tool-call **requests**; executor beslist of die wordt uitgevoerd. Auth bundled with resource óf in vault buiten sandbox. Quote: *"narrow scoping is mitigation; making credentials structurally unreachable is the fix."*
- **3.3** (Anthropic Managed Agents): "Structural unreachability" = de architectuur maakt gevaarlijke acties **deterministisch onbereikbaar** in plaats van te vertrouwen op het model dat hem weigert (probabilistic). Per-tool sandboxing; session ≠ context window; out-of-band oversight.
- **3.1** (Kokane): **Context rot** = werkgeheugen dat actief slechter wordt naarmate het langer loopt. *"Garbage collection is not the same thing as semantic drift correction."* Een van de twee echt nieuwe primitieven in agent harness werk.
- **3.2** (Kokane): Layer 2 = frameworks (LangChain, Microsoft Agent Framework v1.0, Google ADK, LlamaIndex, CrewAI). Layer 3 = runtime zelf (context manager, permission, state, tool executor, retry, HITL, observability). Frameworks zijn pre-assembled harness-kits.

### Level 2 — 3 nieuwe vragen per pagina

Van responsible-ai:
- A1. Wat is "intent validation" als RAI-control?
- A2. Hoeveel landen reguleren AI inmiddels?
- A3. Wat is "learn responsibly" als 5e RAI-dimensie?

Van Anthropic Managed Agents:
- B1. Wat is het pet-vs-cattle probleem in containers?
- B2. Wat is "context anxiety" in Sonnet 4.5?
- B3. Hoe spaart decoupling tijd (TTFT)?

Van Kokane:
- C1. Welke 7 building blocks heeft de Layer 3 runtime?
- C2. Wat is Microsoft Agent Framework v1.0?
- C3. Wat zijn de twee redenen voor de rebrand "agent harness"?

### Level 3 — laatste links en antwoorden

Geselecteerde pagina's (zonder nieuwe reads — dieper in eerder gelezen materiaal):
- Anthropic Managed Agents § "Why the team rebuilt the architecture" — voor B1, B2, B3
- Kokane § "The 4-layer architecture" + "The rename, mapped out" — voor C1, C2, C3
- responsible-ai § "Governance frameworks proliferating" — voor A2

**Antwoorden:**

- **A2**: AI-mentions in wetgeving in 75 landen, +21,3% sinds 2023, 9× meer dan 2016. VS: 59 federale AI-regelingen in 2024 (2× t.o.v. 2023, van 2× zoveel agencies). Frameworks van OECD / EU / VN / AU.
- **B1**: Containers werden "huisdieren" — als één faalde was de sessie verloren; engineers moesten ze "verzorgen". Decoupling maakt ze "vee" (cattle): vervangbaar.
- **B2**: Sonnet 4.5 rondde taken voortijdig af bij naderende contextlimiet ("context anxiety"). Patch met context-resets in harness. Dezelfde harness op Opus 4.5 had het niet meer nodig — model-binnen-familie variatie is reëel.
- **B3**: TTFT p50 -60%, p95 -90% omdat containers alleen worden geprovisioneerd wanneer ze nodig zijn (niet bij elke sessie-start).
- **C1**: Context manager / Permission & guardrails / State & memory / Agentic loop (LLM, Tool Executor, Retry, HITL) / Observability.
- **C2**: Microsoft Agent Framework v1.0 — opvolger van Semantic Kernel + AutoGen, GA april 2026. Agents, graph workflows, HITL, state, A2A, MCP.
- **C3**: Drie redenen — (1) **genuinely**: non-determinisme op core logic layer; (2) **cynisch**: companies need a category to sell; (3) **cynisch**: SEO + vocabulary capture voor mindshare.

### Synthese voor V1

Kern-elementen voor de tekst:
- **Hook**: Friday-in-March casus (vivid, feitelijk)
- **Schaal**: AI Index 2026 cijfer 233→362 incidenten (+55%), 88% adoptie, agent-deployment in single digits
- **Diagnose**: het probleem zit in de laag rond het model, niet in het model
- **Oplossing**: harness met wiki-laag voor intent-validatie en Constraints
- **Bewijs**: "validate intent, not just output format" (Anthropic + Chatterjee + Kokane convergeren)
- **MKB-vertaling**: jij hoeft Anthropic niet te zijn — een gestructureerde wiki + checks bouwt al 80% van het verschil

---

## A2 — Versie 2 (Kennisbehoud / Tacit kennis)

### Level 0 — 3 startvragen

1. **Hoe verandert AI de waarde van menselijke (tacit) kennis in organisaties?**
2. **Welke organisaties scoren beter met AI en waarom (cijfers)?**
3. **Wat is het mechanisme dat kennisbehoud bij AI-inzet mogelijk maakt?**

### Level 1 — geselecteerde pagina's en antwoorden

Pagina's gekozen uit `wiki/index.md`:
- `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` — voor Q1 + Q3
- `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` — voor Q2
- `wiki/concepts/durable-skills.md` — voor Q1

**Antwoorden:**

- **Q1** (Kiron-Schrage): **Polanyi tacit-dimension breach** — *"Humans know more than they can articulate."* Tacit kennis was decennia een moat voor kenniswerkers, want wat niet expliciet kon worden beschreven, kon niet worden geautomatiseerd. LLMs lezen patronen uit miljarden gedragstraces en infereren tacit kennis die experts nooit hebben geformuleerd. *"Tacit expertise was a moat. It is no longer."*
- **Q2** (Ransbotham et al.): MIT SMR × BCG 8th annual survey, **3.467 respondenten / 21+ industries / 136 landen**. 2×2 op organisatie-leren × AI-leren. Distributie: **Limited Learners 59%**, Org Learners 14%, AI-specific 12%, **Augmented Learners 15%**. Augmented Learners zijn **1,6× beter voorbereid op industrie-onzekerheid**, **2,2× op talent-disrupties**, **1,4× hogere kans op extra businesswaarde**, en **99% rapporteert structurele omzetgroei**.
- **Q3** (durable-skills): "The expert as evaluator is not a transitional role." Mechanisme: waar verificatie checkt tegen bestaande standaarden, **genereert evaluatie nieuwe standaarden**. Dat vereist domeinexpertise. Implicatie: zet AI eerst in waar je mensen al diepe expertise hebben.

### Level 1 — 3 nieuwe vragen per pagina

Van Kiron-Schrage:
- 1.1 Wat is precies de "verification → evaluation → learning capture"-flywheel?
- 1.2 Wat doet een CLAUDE.md bestand operationeel?
- 1.3 Wat is "consumption dressed up as adoption"?

Van Ransbotham et al.:
- 2.1 Hoe meet je organisatorisch leren (5 vragen) en AI-leren (4 vragen)?
- 2.2 Hoe lopen Augmented Learners voor op talent-disrupties (2,2×)?
- 2.3 Welke 3 gebieden waar AI organisatie-leren versterkt?

Van durable-skills:
- 3.1 Welke vaardigheden zijn duurzaam tegen AI-substitutie?
- 3.2 Wat is de "Vantage" measurement methodology?
- 3.3 Wat zegt OECD over 21st-century skills?

### Level 2 — gevolgde links en antwoorden

Geselecteerde pagina's:
- Kiron-Schrage § "The three-step compounding flywheel" — voor 1.1
- Kiron-Schrage § "Worked example 1: Anthropic's Claude Code" — voor 1.2
- Kiron-Schrage § "Worked example 2: Google's Jaana Dogan" — voor 1.3
- Ransbotham et al. § "Methodology summary" + § "Three areas..." — voor 2.1 + 2.3
- Ransbotham et al. § "Headline outcomes" — voor 2.2
- `wiki/concepts/micro-productivity-trap.md` — secundair voor de hele cluster

**Antwoorden:**

- **1.1** (Kiron-Schrage): Drie stappen, **alle drie nodig**: (1) **Verification** — binair: voldoet output aan een bestaande norm? Zonder dit is AI-output "noise with a confident tone." (2) **Evaluation** — "wat onthult dit?" Genereert mogelijk nieuwe standaarden. Vereist expertise. (3) **Learning capture** — "hoe zorgen we dat dit inzicht blijft?" *Version control voor organisatorisch oordeel.* Wanneer één stap ontbreekt, **consumeert** de organisatie alleen AI-output zonder te compounden.
- **1.2** (Kiron-Schrage / Boris Cherny): Boris Cherny (Anthropic, Claude Code) gebruikt 10–15 concurrent Claude-instanties + een `CLAUDE.md` bestand dat tijdens de workflow fouten, correcties en designprincipes verzamelt. *"Each new session inherits what every prior session learned."* Elke business functie kan zijn eigen versie maken.
- **1.3** (Kiron-Schrage / Jaana Dogan): Dogan (Google, Gemini API) richtte Claude Code op een probleem waar haar team maanden aan had gewerkt. Output was *vergelijkbaar*. De meeste managers zouden alleen verifiëren (accept/reject). Dogan: *"It's not perfect and I'm iterating on it."* Verschil: evaluatie interrogeert wat de output onthult — over het probleem, over je aannames. *"Most organizations treat AI outputs as verdicts to be confirmed rather than starting points to be interrogated."*
- **2.1** (Ransbotham): Org learning (5): leren door experimenten / fout-tolerantie / postmortems / kennis-codificatie / kennis-deling. AI-leren (4): AI leidt tot nieuw leren / AI leert van performance / human-feedback-loops / werknemers leren ván AI. Median splits → 4 quadranten.
- **2.2** (Ransbotham): Augmented Learners op talent-disruptie 83% prepared vs 39% Limited Learners (2,2×). Tech 86% vs 49% (1,8×). Legal 79% vs 48% (1,6×). 95% AL rapporteert extra businesswaarde vs 66% Limited (1,4×).
- **2.3** (Ransbotham): Drie gebieden — (a) **knowledge capture**: NASA Mars 2020 (rover leert "interesting terrain" zonder definitie); LG Nova AR-glasses (factory workers' tacit kennis live); Capital One; Expedia (fraude-simulatie). (b) **knowledge synthesis**: Stitch Fix (jaren Fixes-historie); Expedia (1,26 quadriljoen combinaties). (c) **knowledge dissemination**: Slack daily channel recaps (>700M messages/dag); cloud services TikTok-style learning.
- **LG Nova quote** (Shilpa Prasad): *"60% of the workforce will likely hit the age of 65 by the year 2028 or 2030, which means that a lot of knowledge will go out from the workforce."*
- **micro-productivity-trap**: 6× meer financieel voordeel met systematic feedback loops; 73% meer financiële impact bij learning-with-AI; 70% AI-adoptie maar slechts 15% gebruikt het voor org-leren.

### Level 2 — 3 nieuwe vragen per pagina

Van Kiron-Schrage flywheel:
- A1. Welke 5 concrete moves moet een organisatie maken?
- A2. Wat is "minimally viable verification"?
- A3. Hoe meet je "the cycle, not just the output"?

Van Ransbotham:
- B1. Wat zijn de 5 stappen om Augmented Learning te ontwikkelen?
- B2. Wat is de paradox van adoption (84% hope / 20% fear)?
- B3. Hoe definieert MIT SMR/BCG "explore vs exploit"?

Van micro-productivity-trap:
- C1. Wat is het verschil tussen verification en evaluation in deze context?
- C2. Hoe maakt Lowe's de 4 stappen concreet?
- C3. Welke EBITDA-cijfers gelden bij transformatie-mindset?

### Level 3 — laatste links en antwoorden

Geselecteerde pagina's (zonder nieuwe reads):
- Kiron-Schrage § "Five concrete moves" — voor A1, A2, A3
- Ransbotham § "Five practical steps" + § "Hopes vs fears" + § "Explore" — voor B1, B2, B3
- `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` — voor C1, C2, C3

**Antwoorden:**

- **A1**: (1) Preserve evaluation expertise; (2) Build minimally viable verification; (3) Institute evaluation practices ("what was *interestingly* wrong?"); (4) Create capture systems (decision journals / prompt repositories / evaluation logs); (5) Measure the cycle, not just the output.
- **A2**: Multijudge systems die disagreement surfacen + consistency checks die output vergelijken over verschillende formuleringen van hetzelfde probleem. Begin de cyclus zelfs als volledige verificatie duur is.
- **A3**: Tellen — hoeveel interacties geverifieerd? geëvalueerd? hoeveel learning gecaptured? hoe snel verandert gecapturede learning de praktijk? *"Did your team leaders learn things from AI interactions last week that changed how they worked this week? If not, the cycle is not running."*
- **B1**: (1) Verbeter beide leren tegelijk; (2) Leer **explore** met AI (niet alleen exploit) — Limited Learners zijn 2× vaker bezig met procesoptimalisatie; (3) Kies leerprojecten (>5 jaar / hoog risico, AL is 1,9× resp 2,4× vaker); (4) Leer verantwoord; (5) Versnel leren met AI.
- **B2**: 84% **hoopt** AI helpt met taken (vs 70% in 2017); slechts 20% **vreest** AI vervangt taken (vs 31% in 2017). *Hopes outpacing fears.*
- **B3**: Augmented Learners zijn 2× vaker bezig met *exploration* van nieuwe waarde-creatie via traditionele AI; 1,6× via generatieve AI. Limited Learners verbeteren vooral bestaande processen.
- **C1**: Verificatie kijkt of output voldoet aan **bestaande** standaarden. Evaluatie kijkt wat output **onthult** over het probleem zelf. Process lock-in = AI automatiseert *huidige* processen zonder herontwerp.
- **C2**: Lowe's: prioritisatie-framework op tech maturity / use-case size / readiness / dimensional risk. Vision = "democratiseren van expertise". Twee interfaces (Mylow / Mylow Companion) maart 2025. SMEs maakten prompt + expert-validated response sets ("hoe Mylow zou moeten antwoorden"). Multi-model evaluation. Associates auditen output én tussenstappen.
- **C3**: Bain client EBITDA gains **10–25%** voor transformation-mindset deployments. Lowe's: >2× online conversie; +200 bps CSAT; uitgerold over 1.700+ winkels. FabricationCo: ~$30M winst; 15× sneller offertes; +10pp win-rate in 3 maanden.

### Synthese voor V2

Kern-elementen voor de tekst:
- **Hook**: LG Nova 60% pensioen-quote + Polanyi tacit-breach
- **Empirisch anker**: 59% Limited / 15% Augmented / 6× meer financieel succes
- **Mechanisme**: drie-staps flywheel (verify → evaluate → capture)
- **Concreet voorbeeld**: CLAUDE.md als "version control voor organisatorisch oordeel"; Jaana Dogan's *"not perfect and I'm iterating"*
- **MKB-vertaling**: een wiki ís jouw CLAUDE.md — daar wordt tacit kennis stap voor stap expliciet
- **CTA-bridge**: jij wil bij die 15% horen — laten we kijken hoe

---

## A3 — Versie 3 (Build / Architectuur / Rent vs Own)

### Level 0 — 3 startvragen

1. **Wat is het concrete bedrijfsresultaat van AI-transformatie vs. AI-experimentatie?**
2. **Hoe is een agent harness opgebouwd (architectuur)?**
3. **Wat betekent "rent vs own" en waarom is dat strategisch?**

### Level 1 — geselecteerde pagina's en antwoorden

Pagina's gekozen uit `wiki/index.md`:
- `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` — voor Q1
- `wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md` — voor Q2 + Q3
- `wiki/concepts/agent-harness.md` — voor Q2 + Q3

**Antwoorden:**

- **Q1** (Dutt et al.): **Micro-productivity-trap**. Individuele werknemers boeken winst op één taak; firm-level gebeurt er niets — want werkstroom rondom is niet veranderd. Twee lock-ins: **offering lock-in** (AI optimaliseert bestaand product i.p.v. waardepositie te herzien) en **process lock-in** (AI automatiseert huidige processen i.p.v. uit te outcomes te herontwerpen). Bain client EBITDA gains: **10–25%** voor wie wel transformeert.
- **Q2** (Chatterjee): 4 lagen in build-volgorde:
  1. **Context** — system prompt als *document, niet string*; stable parts (KV-cached) + dynamic parts (user memory + workspace + delta + persona). *"Het is de kamer waar de agent binnenloopt."*
  2. **Constraints** — pre-tool en post-tool middleware; destructive-verb detection, workspace-isolation, loop-detection, output-scoring.
  3. **Contracts** — formele evalueerbare specificaties van "geslaagde output", **geijkt op de inputs**.
  4. **Compounding** — gestructureerde telemetrie als trainingsdata voor de **harness** (niet het model).
- **Q3** (agent-harness concept): *"The model is rented from a vendor whose competitor will outperform them within the year; the harness — our memory architecture, our quality contracts, our learned per-customer overrides, our telemetry — is what we own and what compounds."* Plan for swap, not for marriage.

### Level 1 — 3 nieuwe vragen per pagina

Van Dutt et al.:
- 1.1 Welke 4 stappen om uit de trap te komen?
- 1.2 Wat is FabricationCo en wat zijn hun resultaten?
- 1.3 Welke "evals" gebruikt Lowe's?

Van Chatterjee:
- 2.1 Wat zijn de "stable" vs "dynamic" delen van de Context?
- 2.2 Wat is het verschil tussen verification, contract en compounding?
- 2.3 Wat is de roadmap-implicatie ("permanent allocation")?

Van agent-harness:
- 3.1 Hoe verhoudt dit zich tot Anthropic's brain/hands/session?
- 3.2 Wat is "the under-resourced role" in AI-teams?
- 3.3 Wat is Kokane's 90/10-thesis?

### Level 2 — gevolgde links en antwoorden

Geselecteerde pagina's:
- Dutt et al. § "Four steps" + § "Headline numbers" — voor 1.1, 1.2, 1.3
- Chatterjee § "The four layers — full treatment" + § "What this means on a roadmap" — voor 2.1, 2.2, 2.3
- `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` — voor 3.1
- `wiki/sources/2026-05-07-kokane-agent-harness-vs-systems-design.md` — voor 3.2 + 3.3

**Antwoorden:**

- **1.1**: (1) Narrow possibilities strategically — 4 of 5 kritieke domeinen. (2) Reimagine workflows across the org — *"It's the process redesign — not the technology — that is the most challenging part... and creates most of the value."* (3) Engage those closest to today's process — top-down + bottom-up. (4) Measure what matters — concrete business outcomes + continuous **evals**.
- **1.2**: FabricationCo (geanonimiseerd Fortune 1000 manufacturer, Bain client). Week-lange cross-functional workshop → 14 use cases → ~$30M extra winst. Quote-workflow: oude design-engineers spendeerden uren aan elke offerte; nieuw: 20-min cost estimates door non-designers voor early-stage bids; **15× sneller**, +10pp win-rate in 3 maanden.
- **1.3**: SMEs creëerden prompt + expert-validated response sets ("hoe Mylow Companion zou moeten antwoorden"). Multi-model vergelijking. Iteratief prompting. Associates auditen output én tussenstappen. Outcome metrics: basket size, conversion rate, incremental sales, associate knowledge, customer satisfaction, ease of check-out. **>2× conversie online; +200 bps CSAT in-store. Uitrol over 1.700+ Lowe's-winkels.**
- **2.1**: Stable parts (top, KV-cached): identity, workspace, rules. Dynamic parts (rebuilt per turn): user memory, workspace knowledge, delta summary, behavioral persona. *"At scale this is the difference between a sustainable cost curve and one that bankrupts you."* De duurste fout: statische prompt + lazy context retrieval midden in een gesprek.
- **2.2**: Verification = binaire check tegen bestaande criteria. Contracts = formele specs van geslaagde output, **geijkt op inputs** (5 sources ≠ 50 sources). Compounding = telemetrie waaruit harness adjustments worden voorgesteld; menselijke review; goedgekeurde adjustments worden workspace overrides die compounden.
- **2.3**: *"There is no version of this where you finish the harness."* Eerste 3 lagen in jaar 1; vierde laag (Compounding) in jaar 2; elke kwartaal kalibreren-uitbreiden-harden. Permanent allocation, niet een fase.
- **3.1** (Anthropic): Brain (Claude + harness loop) / Hands (sandbox + tools) / Session (durable event log). Elk independently replaceable, isolated failure, reachable across infrastructure boundaries. Mapping: Kokane's "inference-only model" = brain; "execution-only tool executor" = hands; "State & memory + Context" = session. *Zelfde architectuur, twee vocabulaires.*
- **3.2** (Chatterjee): de meest under-resourced rol op AI-teams is *niet* de model researcher en *niet* de prompt engineer, maar de engineer *"who thinks about agents the way SREs think about distributed systems: in terms of failure modes, observability, graceful degradation, and the long tail of edge cases that only emerge at production scale. Hire for this taste. It is rare and it compounds."*
- **3.3** (Kokane): 90% mature systems engineering rebranded (cache management, database + job queue, API middleware, approval workflows, summarization + offload, process lifecycle); 10% genuinely nieuw (non-determinism + context as degrading resource). *"If you've shipped real backend systems, you're already 80% of the way there."*

### Level 2 — 3 nieuwe vragen per pagina

Van Dutt 4-stappen:
- A1. Welke 4–5 critical domains zijn typisch?
- A2. Wat is "FabricationCo quoting workflow" precies?
- A3. Wat is de "boardroom imperative"?

Van Chatterjee 4 lagen:
- B1. Wat is een pre-tool hook concreet?
- B2. Hoe scoort een post-tool hook output?
- B3. Wat is "the most expensive mistake" in Context?

Van Anthropic / Kokane:
- C1. Wat is "context anxiety" en hoe los je het op?
- C2. Welke 7 building blocks zitten in Layer 3?
- C3. Wat zijn de drie redenen voor de term-rebrand?

### Level 3 — laatste links en antwoorden

Geselecteerde pagina's (zonder nieuwe reads):
- Dutt § "Step 1" + § "Step 4" + § "The boardroom imperative" — voor A1, A2, A3
- Chatterjee § "Constraints" + § "Context most expensive mistake" — voor B1, B2, B3
- Anthropic § "Why the team rebuilt" + Kokane § "Building blocks" + § "Why the new term exists" — voor C1, C2, C3

**Antwoorden:**

- **A1**: Top-4 domeinen op basis van Bain's portfolio: **software development, customer support, knowledge worker efficiency, marketing**. Diagnostic: waar profiteert het bedrijf vandaag én morgen? Waar is hoogste concentratie van repeatable work? Hoge waarde, lage effort? Buy vs build? In-house vs partner?
- **A2**: Oud: design engineers spendeerden uren aan élke offerte (>50% niet gewonnen). Nieuw: 20-min cost estimates door non-designers voor early-stage bids; full engineered designs alleen voor higher-probability opportunities. Resultaat: ~15× sneller, minder verspilde inspanning, betere win rates.
- **A3**: *"AI transformation must be prioritized at the very top levels of the company, with all executives and functions participating."* Falling firms: leadership erkent AI als belangrijk maar **delegeert** naar tech-groepen zonder concrete doelen of metrics. *Lagging firms recognize AI as important but delegate it... From that delegation, initiatives often fail.*
- **B1**: Pre-tool: destructive-verb recognition (route to soft alternatives) — **Friday-in-March remediation**. Workspace-isolation: Customer A's agent kan niet bij Customer B's data. Loop-detection: agent heeft 6× dezelfde search gedaan → exhaustion warning in plaats van $0,20 aan tokens te verbranden.
- **B2**: Output gescoord op **citation coverage, source triangulation, severity distribution, density, thematic diversity**. Onder threshold? *Inject corrective context*: *"your last synthesis scored a C, here is why, try again with these specific corrections."* De harness wordt een actieve editor.
- **B3**: De duurste fout = statische system prompt doorgeven en context-retrieval mid-conversation laten gebeuren. Het verschil tussen useful-first-draft en drie-turns-naar-baseline-competentie zit in *het juiste context, samengesteld vóór het eerste token*.
- **C1**: "Context anxiety" — Sonnet 4.5 rondde taken voortijdig af bij naderende contextlimiet. Patch: context-resets in harness. Op Opus 4.5 was het probleem weg → resets werden dood gewicht. Les: harness moet replaceable zijn als modellen veranderen.
- **C2**: Layer 3 building blocks: (1) Context manager; (2) Permission & guardrails; (3) State & memory; (4) Agentic loop / Orchestrator (LLM, Tool Executor, Retry, HITL); (5) Observability.
- **C3**: (a) Genuinely — non-determinisme op core logic layer vereist intent-validation. (b) Cynisch #1 — bedrijven hebben een categorie nodig om te verkopen. (c) Cynisch #2 — SEO + vocabulary capture; nieuwkomers in AI engineering hebben vocabulaire nodig.

### Synthese voor V3

Kern-elementen voor de tekst:
- **Hook**: "The model is rented; the harness is owned" (Chatterjee)
- **Trap**: micro-productivity-trap + EBITDA-cijfers (10–25%) als business case
- **Architectuur**: 4 lagen Context/Constraints/Contracts/Compounding
- **Sceptische realiteit**: Kokane's 90/10-thesis — 90% gewone systems engineering
- **MKB-vertaling**: jij hoeft Anthropic niet te zijn; een wiki + checks dragen al die 4 lagen
- **Concrete bewijslast**: Lowe's >2× conversie, FabricationCo 15× sneller offertes, Bain 10–25% EBITDA

---

# DEEL B — UITEINDELIJKE LINKEDIN-VERSIES

> **Stijlnoot:** SCQA blijft de ruggengraat. De labels staan níet in de tekst.

## Versie 1 — De "Friday-in-March-versie" (risico-georiënteerd, cinematisch)

**Doelpersona binnen MT:** CFO / COO / risico-eigenaar.

---

🎯 *Op een vrijdag in maart wiste een AI-agent twee weken aan klantonderzoek — 40 minuten voor de boardmeeting begon.*

De prompt? Eén zin: *"Ruim de boel op voor de board review."* De agent vond dat redelijk: archiveer oude documenten, verwijder duplicaten, schoon stale bronnen op. Elke afzonderlijke handeling was logisch. Het totaal: een klein drama. *(Bron: Chatterjee, "The Anatomy of an Agent Harness", mei 2026.)*

Inmiddels gebruikt 88% van de organisaties AI in minstens één functie (Stanford AI Index 2026). En het aantal gedocumenteerde AI-incidenten? **Van 233 in 2024 naar 362 in 2025 — +55%.** Maar slechts **enkele procenten** van de bedrijfsfuncties zet AI-agents écht in.

Dat hiaat heeft één oorzaak die in zes wiki-bronnen tegelijk terugkomt: **het probleem zit niet in het model, maar in de laag eromheen.** Anthropic, Google en onafhankelijke practitioners (Chatterjee, Kokane) noemen die laag de **harness**. Wat hij doet:

- *Intent-validatie*: snapt "opruimen" als destructieve actie en vraagt eerst om bevestiging
- *Workspace-isolatie*: Klant A's agent kan niet bij Klant B's data — gebouwd als architectuur, niet als belofte
- *Loop-detectie*: agent zoekt 6× hetzelfde → meldt het, verbrandt niet voor twintig cent aan tokens

In mijn eigen build is die harness gekoppeld aan een **wiki**: een gestructureerde, bronvermelde kennisbank die per vraag wordt geraadpleegd. Geen hallucinatie over interne afspraken. Geen agent die "opruimen" interpreteert als "wissen". Bewijs gaat boven belofte.

Voor MKB: je hoeft Anthropic niet te zijn. *"Build constraints before you build cleverness"* (Chatterjee). Die uitspraak is goedkoper dan de excuus-mails achteraf.

👉 **Nodig me uit voor een kop koffie en laat me je helpen bij je AI groei!**

#AI #MKB #Digitalisering

---

## Versie 2 — De "Tacit-breach-versie" (HR/strategisch, narratief)

**Doelpersona binnen MT:** HR-directeur / People & Culture / AD met focus op kennis.

---

📚 *"60% van onze werknemers bereikt de pensioenleeftijd in 2028 of 2030. Een hoop kennis loopt straks gewoon de deur uit."* — Shilpa Prasad, LG Nova, in MIT SMR/BCG-onderzoek (2024).

In ieder MKB zit de waardevolste kennis in mensen, niet in handboeken. Hoe een offerte écht wordt opgebouwd. Welke leverancier je nooit op vrijdag belt. Waarom een specifieke installatie altijd dezelfde rare storing geeft. Dit heet **tacit kennis** — kennis die niet is opgeschreven maar die in elke handeling zichtbaar wordt.

Filosoof Polanyi formuleerde het al in 1966: *"Humans know more than they can articulate."* Decennialang was dat tacit-kennis een moat — wat niet expliciet kon worden beschreven, kon ook niet worden geautomatiseerd. **Die moat is gebroken.** Grote taalmodellen lezen patronen uit miljarden gedragstraces en infereren expertise die experts nooit hebben geformuleerd (Kiron & Schrage, MIT SMR, april 2026).

Wat onderscheidt de bedrijven die hier slim mee omgaan? Het MIT SMR/BCG-onderzoek onder 3.467 organisaties geeft het cijfer: **slechts 15% combineert organisatorisch leren met AI-leren** ("Augmented Learners"). Die 15% is **6× vaker** financieel succesvol met AI dan de **59% die slechts consumeert**. **99% van hen** rapporteert structurele omzetgroei.

Hoe doen ze dat? Met een drie-staps cyclus die elke AI-interactie productiever maakt:

1. **Verifiëren** — voldoet deze output aan de norm? (vaak doen organisaties alleen dít)
2. **Evalueren** — *wat onthult deze output?* Anthropic's Boris Cherny laat AI tests draaien voordat een mens iets ziet; Google's Jaana Dogan zegt: *"It's not perfect and I'm iterating on it."* Dát is evaluatie.
3. **Vastleggen** — Anthropic-engineers gebruiken `CLAUDE.md`-bestanden — *versie-controle voor organisatorisch oordeel*. Elke nieuwe sessie erft wat eerdere sessies leerden.

Voor jouw MKB werkt hetzelfde principe: een **wiki** in het hart van je AI-systeem waarin tacit kennis stap voor stap expliciet wordt. Mens als regisseur, AI als verlengstuk. Ik bouwde zoiets voor mijn onderzoekswerk — ik begin nooit meer bij nul.

👉 **Nodig me uit voor een kop koffie en laat me je helpen bij je AI groei!**

#AI #MKB #Kennisbehoud

---

## Versie 3 — De "Rent-vs-Own-versie" (founder-tone, architectonisch)

**Doelpersona binnen MT:** Algemeen directeur / vernieuwer / IT-strateeg.

---

⚙️ *"Het model is wat je huurt. De harness is wat je bezit."* (Chatterjee, mei 2026)

In april 2026 publiceerden Bain & OpenAI een diagnose voor de AI-stagnatie in het MKB: de **micro-productivity-trap**. Individuele werknemers boeken winst op één taak — sneller mailen, sneller offerte — maar firm-level gebeurt er niets. De reden? De werkstroom rondom die taak is niet veranderd.

De bedrijven die wél transformeren? **10–25% EBITDA-stijging** (Bain client data). Lowe's verdubbelde de online conversie en lifte klanttevredenheid +200 basispunten met hun Mylow-systeem. Een Bain-klant ("FabricationCo"): **15× sneller** offertes, +10pp win-rate in 3 maanden, ~$30M extra winst.

Het verschil zit niet in welk AI-model ze gebruikten. Het zit in de **harness** — de runtime-laag tussen het model en het werk. Vier lagen, in build-volgorde (Chatterjee 2026):

1. **Context** — assembleer de juiste kennis vóór de eerste token, niet midden in het gesprek. Stable parts (cached) + dynamic parts (per vraag opnieuw opgebouwd).
2. **Constraints** — controleer **intentie**, niet alleen output-formaat. *"Authorize whether the model is allowed to want what it wants"* (Kokane).
3. **Contracts** — formele criteria voor "geslaagd" werk, geijkt op de input. Een synthese over 5 bronnen heeft niet dezelfde norm als één over 50.
4. **Compounding** — telemetrie als trainingsdata voor de **harness** (niet het model — *dat is bevroren*). De infrastructuur leert. Daar zit waarde-opbouw.

In mijn eigen build is een **wiki** de drager van die 4 lagen. Bronnen, entiteiten en concepten gestructureerd opgeslagen. Bij elke vraag haalt de agent precies de relevante stukken op, citeert de bron, en valt terug op een mens als de zekerheid laag is.

Akshay Kokane (ex-Microsoft, ex-AWS) is sceptisch en heeft gelijk: **90% van dit werk is gewone systems engineering**. *"If you've shipped real backend systems, you're already 80% of the way there."* De resterende 10% — non-determinisme, context als degraderende resource — is waar de discipline zit.

Voor MKB: plan voor swap, niet voor huwelijk. Het model is huurmateriaal. De harness en wiki bouw je zelf.

👉 **Nodig me uit voor een kop koffie en laat me je helpen bij je AI groei!**

#AI #MKB #Innovatie

---

# DEEL C — ONDERSTEUNENDE ARTEFACTEN

## Bronnenmatrix (wiki-citaten per versie)

| Wiki-pagina | V1 | V2 | V3 |
| ----------- | -- | -- | -- |
| `wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md` | Friday-in-March; "build constraints before cleverness" | — | "model rented, harness owned"; 4-laagse anatomy |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | 88% adoptie; 233→362 incidenten (+55%); single-digit agent-deployment | — | — |
| `wiki/concepts/agent-harness.md` | 3-laagse RAI-runtime taxonomy | — | Conceptueel anker |
| `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` | "structural unreachability"; brain/hands/session | — | brain/hands/session decoupling |
| `wiki/sources/2026-05-07-kokane-agent-harness-vs-systems-design.md` | "validate intent, not just output format"; context rot | — | 90/10-thesis; "80% of the way there" |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | — | LG Nova quote; 15% AL / 59% Limited; 99% rev gain | — |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | — | Polanyi tacit-breach; 6×-feedback-loop; CLAUDE.md; verify→evaluate→capture; Cherny + Dogan | — |
| `wiki/concepts/durable-skills.md` | — | "expert as evaluator is not transitional" | — |
| `wiki/concepts/responsible-ai.md` | RAI runtime taxonomy; incident-types; AI-regulering 75 landen | — | — |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | — | — | Micro-productivity-trap; 4 stappen; 10–25% EBITDA; Lowe's >2× conversie; FabricationCo 15× / +10pp |
| `wiki/concepts/micro-productivity-trap.md` | — | 6× / 73% / 70% adoptie cijfers | Anker voor trap-diagnose |

## Verschillen tussen de drie versies

| Aspect | V1 (Friday-in-March) | V2 (Tacit-breach) | V3 (Rent-vs-Own) |
| ------ | -------------------- | ----------------- | ---------------- |
| **Pijnpunt** | Onbetrouwbaarheid → risico/incidenten | Tacit-kennis-erosie + pensioneringsgolf | Stagnerende ROI ondanks AI-uitrol |
| **Tone** | Cinematisch, urgent | Reflectief, narratief, filosofisch | Founder, architectonisch-bouwend |
| **Hook** | Verhaal van een verloren boardmeeting | LG Nova 60%-quote + Polanyi | Chatterjee aphorism |
| **Bewijs** | Casus + AI Index incidentcijfers | Survey-data + filosofie + 2 named cases | Consultancy-cijfers + 4-laagse architectuur + sceptische tegenstem |
| **Vakjargon** | "harness" (uitgelegd) | "tacit kennis" (uitgelegd via Polanyi) | 4 lagen + "rent vs own" (uitgelegd) |
| **MT-aanspreker** | CFO / COO / risico-eigenaar | HR / People & Culture / AD | AD / vernieuwer / IT-strateeg |
| **Lengte** | ~290 woorden | ~310 woorden | ~330 woorden |
| **Hashtags** | #Digitalisering | #Kennisbehoud | #Innovatie |

## Verificatie

- [ ] Versie 1 opent met de Friday-in-March case (Chatterjee 2026) en gebruikt AI-Index-cijfers
- [ ] Versie 2 verwerkt de Polanyi tacit-breach + LG Nova 60%-quote + 15%-Augmented-Learners + 6× feedback-loop
- [ ] Versie 3 noemt expliciet de 4 lagen Context/Constraints/Contracts/Compounding én de Bain 10–25% EBITDA + Lowe's 2× + FabricationCo 15×
- [ ] Alle drie eindigen op exact: *"Nodig me uit voor een kop koffie en laat me je helpen bij je AI groei!"*
- [ ] SCQA-structuur is impliciet (geen letterlijke labels)
- [ ] Jargon wordt direct uitgelegd óf is in de doelgroep gangbaar
- [ ] Bronnen worden lichtgewicht geattribueerd (auteur + jaar + publicatie), niet als formele citaties
- [ ] Lengte 280–340 woorden — passend voor LinkedIn long-form
- [ ] Research log (Deel A) is per versie traceerbaar en kan apart worden gepubliceerd of in de wiki gefiled

## Volgende stap

Bij goedkeuring kunnen de drie versies in dit plan worden gepubliceerd zoals ze zijn. Het research log (Deel A) kan optioneel:

- Als losse wiki-pagina worden opgenomen (in `wiki/syntheses/` als query-gedreven synthese, of in een nieuw `wiki/queries/`-pad)
- Of bij elke versie als "bronnen-bijlage" worden meegestuurd in DM-conversaties die uit de post voortkomen

Niets wordt zonder expliciete goedkeuring naar de wiki zelf geschreven — dit plan is een communicatiestuk.
