# Plan — LinkedIn-reeks "Harness Engineering" voor MKB-directies

## Context

Witek wil een LinkedIn-reeks over **harness engineering** schrijven, gericht op managers/directie van MKB-bedrijven (50–500 fte) die:

- **óf** met AI willen starten maar nog geen besluit hebben genomen hoe;
- **óf** een besluit genomen hebben en nu merken dat het moeilijker is dan gedacht.

Doel: positie nemen als data/AI engineer die helpt waar directies vastlopen — zónder dat de reeks als pitch leest. Bestaande HTML-visualisaties (`inspiration/architecture-of-scale-nl.html` en `inspiration/harness-is-os-nl.html`) vormen het visuele anker. De wiki (`/Users/witoldtenhove/Projects/ai-wiki/wiki/`) levert de autoriteit — met name `concepts/agent-harness.md` (conf 0,95, 20 bronnen) en de syntheses in `is-rag-dead.md` en `knowledge-architectures-for-llm-agents.md`.

**Hoofdboodschap:**

> **Werken met AI is een nieuw soort samenwerking. Niet jij + een tool, maar jij + een collega die elke nacht vervangen wordt door een nieuwe versie van zichzelf — sneller maar zonder herinnering. De *harness* — geheugen, wiki, contextarchitectuur — is hoe je organisatie zorgt dat wat jullie samen leren bij jullie blijft. Wie alleen op het model investeert, verliest die kennis elke release. Wie in de harness investeert, bouwt institutioneel geheugen dat modelwisselingen overleeft.**

**Reeksbeslissingen** (vastgelegd 2026-05-12 via brainstorm, herzien na pivot 2026-05-12, structuuradviezen verwerkt 2026-05-13):
- Toon: **feitelijk en analytisch** — Witeks stem direct; bronnen uit de wiki dragen de claims. (*Pivot: oorspronkelijk verhaalgedreven via fictieve personages; nu zonder fictieve verteller.*)
- Persona's Marieke + Stefan: **interne toetslens** vóór publicatie, niet in de content.
- Omvang: **9 stukken** — 3 pijler-artikelen (~1500 woorden) + 6 ondersteunende posts (~400 woorden).
- Lead-gen: **provocatie + open invitatie** aan het einde van elk stuk.
- Redactie: persona-toetslens + `taalredactie-publicatie` skill vóór publicatie van elk stuk.
- Cadans: wekelijks, dinsdag 8:00.

Wiki-anker voor de hoofdboodschap: [`wiki/concepts/agent-harness.md`](../wiki/concepts/agent-harness.md).

---

## Ondersteunende provocaties

Vier provocaties, parallel-gestructureerd, verspreid over de reeks:

1. *Je AI is je nieuwste collega — maar elke nacht wordt hij vervangen door een vreemde.*
2. *Dezelfde problemen als 1969, dezelfde architectuur in 2026 — maar nu werk je ermee samen.*
3. *Eén vraag, vier antwoordwegen — drie wissen wat je organisatie leert; één laat het doorgroeien.*
4. *Hetzelfde benchmark, hetzelfde plafond — maar productie-agents stijgen door als de harness er staat.*

Patroon: concrete openings-image + dash-twist die het tegen-intuïtieve kernpunt levert.

---

## Persona's als interne toetslens (niet als verteller)

Marieke en Stefan blijven beschikbaar als **review-paneel** vóór publicatie. Ze worden niet in de content opgevoerd; ze testen of de content de juiste lezer raakt.

### Marieke (45) — commercieel directeur / mede-eigenaar

Profiel: MKB-installatiebedrijf, 80 fte, denkt in €/KPI/eigenaarschap, geen jargon-tolerantie. Variant op de persona uit [`linkedin-post-mkb-mt.md`](linkedin-post-mkb-mt.md).

**Toetsvragen per draft:**
- Kan ik in 30 seconden zien wat dit voor mijn bedrijf betekent?
- Staat er één concreet getal, voorbeeld of beslissing in?
- Wordt de prijs van het probleem genoemd, niet alleen de oplossing?
- Word ik niet behandeld als technologisch leek?

### Stefan (38) — IT-manager / "de IT-man"

Profiel: MKB 60–150 fte, tweemansafdeling, rapporteert aan COO. Technische precisie, hekel aan oversimplificatie, eerlijk over wat hij niet weet. Bestaande persona uit [`linkedin-post-mkb-ict.md`](linkedin-post-mkb-ict.md).

**Toetsvragen per draft:**
- Klopt de architectuur-claim ook op detailniveau?
- Worden RAG / KG / contextvenster correct uitgelegd of vereenvoudigd tot onjuist?
- Wordt een leverancier of methode niet zonder bewijs aangevallen?
- Krijg ik een bron of citaat voor de hardste claims?

### Werkwijze

Elk concept-stuk wordt vóór publicatie tweemaal gelezen — eenmaal met Marieke-lens, eenmaal met Stefan-lens. Punten waar de twee oneens zijn (Marieke wil eenvoud; Stefan precisie) vormen productieve spanning — los op door **bron-citaten** te gebruiken zodat Marieke kort kan lezen en Stefan dieper kan klikken via de wiki-link.

Wenselijk eindbeeld per stuk: een Marieke-lezer komt na 60 seconden eruit met één bruikbaar inzicht; een Stefan-lezer komt na 5 minuten eruit met genoeg bronnen om zelf verder te graven.

Na de persona-toetslens volgt de **taalredactie-stap** (zie [Productie-volgorde](#cadans--productie-volgorde)) — de `taalredactie-publicatie` skill wordt op elk gepubliceerd stuk toegepast.

---

## Reeks-ruggengraat (9 stuks)

| # | Format | Werktitel | Centrale visual | Wiki-anker |
|---|---|---|---|---|
| 1 | POST | *"Wat investeer je eigenlijk in, als je investeert in AI?"* | nieuwe tegel: verouderd vs. groeit door | `concepts/agent-harness.md` sectie Definitie |
| 2 | **ART** | *"Dezelfde problemen, dezelfde architectuur — wat AI-systemen in 2026 van Unix in 1969 erven."* | **harness-is-os-nl.html** | `concepts/agent-harness.md` sectie OS-analogie |
| 3 | POST | *"Waarom productie-AI elke maandag opnieuw begint — en hoe teams dat oplossen."* | agent-wiki.gif | Bratanic geheugenstuk; `syntheses/knowledge-architectures…` |
| 4 | POST | *"RAG is niet dood. De term is dood."* | RAG-kolom uit visual #1 | `syntheses/is-rag-dead.md` |
| 5 | **ART** | *"Vier manieren om één vraag te beantwoorden — en wanneer welke werkt."* | **architecture-of-scale-nl.html** | `syntheses/knowledge-architectures-for-llm-agents.md` |
| 6 | POST | *"Een LLM-wiki is geen tool. Het is een vorm van eigendom."* | search-wiki.gif | `concepts/llm-wiki.md` + Karpathy-thread |
| 7 | POST | *"Het model is gehuurd. De harness is van jou."* | nieuwe: rent-vs-own-tegel | `concepts/agent-harness.md` sectie Model is gehuurd |
| 8 | POST | *"Vijf vragen die elke MKB-directeur aan zijn AI-leverancier moet stellen."* | nieuwe: vragen-tegel | Chase/LangChain ADL + `concepts/agent-harness.md` |
| 9 | **ART** | *"Hoe AI-investering compoundt: een bouwplan voor MKB-directies."* | compositie + echte wiki-screenshot | alle drie syntheses + `agent-harness.md` |

**Logica van de volgorde:**

- Stuk 1 stelt de **hoofdvraag** waar de reeks omheen draait. Geen verteller; één scherpe formulering die de lezer aanzet tot positionering.
- Stuk 2 zet het **mentale model** (OS-analogie) — de zwaarste conceptlaag op een breukpunt zodat lezers er met scherpe aandacht in komen.
- Posts 3–4 hangen *concrete herkenningen* aan dat model: geheugen, en de RAG-misverstanden.
- Stuk 5 zet de **beslismatrix** (vier architecturen) op het tweede breukpunt — de meest pragmatische bijdrage.
- Posts 6–7 hangen *eigendoms-implicaties* aan die matrix: wiki als bezit, model als huur.
- Post 8 maakt het **doe-baar** — vijf concrete vragen die elke directeur morgen kan stellen.
- Stuk 9 maakt het **commercieel** — synthese + bouwplan, met open invitatie zonder pitch.

---

## Verificatie — wanneer is de reeks geslaagd?

Geen testsuite; deze signalen kijken we naar. (Deze sectie staat bewust vroeg in het document, zodat tijdens het schrijven van elk stuk meteen helder is wat "succes" betekent.)

**Kwantitatief (per stuk, eerste 7 dagen):**
- Impressies > 5.000 (post) / > 1.500 (artikel-views).
- Engagement-rate > 3% (LinkedIn-mediaan B2B is ~1,5%).
- Reposts door minimaal één directielid uit de doelgroep per artikel.

**Kwalitatief (over de hele reeks):**
- Minimaal 3 DM-conversaties die starten met herkenning van een specifiek probleem uit een artikel ("dit met geheugen herken ik letterlijk", "die vijf vragen ga ik morgen stellen").
- Minimaal 1 inkomende vraag om kennismaking voor concreet werk.
- Reacties die over de *inhoud* gaan (architectuur, samenwerken-met-AI) in plaats van compliment-reacties ("mooi geschreven!").
- Geen reacties die de reeks lezen als pitch.

**Reeks-niveau:**
- Stuk 9 trekt aantoonbaar de meeste DM's van de reeks (terwijl het de enige duidelijke invitatie heeft).
- Tegen week 10: minstens één professioneel contact reageert met *"ik wist niet dat dit werk een naam had — kunnen we praten?"*

**Anti-signalen (in dit geval moet bijgestuurd worden):**
- Reacties als "interessante theorie maar onpraktisch" — vragen om stuk 8 (vijf vragen) eerder te publiceren of vooruit te duwen.
- Stuk 2 (OS-analogie) krijgt 30%+ minder views dan stuk 5 — opener moet concreter in plaats van conceptueler.
- DM's zijn vooral van consultants/concullega's, niet directies — toon te jargon-zwaar; persona-toetslens Marieke is niet streng genoeg toegepast.
- Reacties markeren claims als ongefundeerd — Stefan-toetslens niet streng genoeg toegepast; bronnen ontbreken of zijn te indirect.

---

## Per-stuk-uitwerking

### Stuk 1 · POST · *"Wat investeer je eigenlijk in, als je investeert in AI?"*

- **Hoofdboodschap:** AI-investering bestaat uit twee verschillende soorten uitgaven die zelden gescheiden worden gerapporteerd: (a) gehuurde modelcapaciteit (per token, per maand, verdampt bij elke modelwissel); (b) eigen harness-laag (stapelt zich op, blijft, is overdraagbaar). Zonder dit onderscheid weet je niet wat je over drie jaar nog bezit.
- **Lengte:** ~400 woorden.
- **Visual:** nieuwe tegel **"Wat verouderd / Wat groeit door"** — twee kolommen, brutalist-blueprint stijl. Vooruitwijzing naar stuk 7.
- **Wiki-anker:** [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie Definitie + sectie De vier C's (Context, Constraints, Contracts, Compounding).
- **Bronnen om naar te wijzen:** het cijfer uit het AI Index Report 2026 over AI-volwassenheid (1% van de directies noemt de implementatie volwassen); Sternfels (McKinsey) HBR-interview over AI-strategie.
- **Provocatie:** *Negen van de tien MKB-AI-investeringen kopen een gehuurd model — en boeken het op alsof het een eigen capaciteit is.*
- **Invitatie:** "Welk type investering doet jouw bedrijf op dit moment — gehuurd of eigen? Reageer of DM me."

### Stuk 2 · ART · *"Dezelfde problemen, dezelfde architectuur — wat AI-systemen in 2026 van Unix in 1969 erven."*

- **Hoofdboodschap:** De OS-analogie is geen retorische vondst maar een ontwerp-identiteit. Vijf vraagstukken die Bell Labs in 1969 oploste (geheugenbeheer, planning, IO, isolatie, exception-afhandeling) keren in 2026 één-op-één terug bij agent-harnessen. De term "harness engineering" komt rechtstreeks uit OpenAI's eigen engineering-blog (Lopopolo, februari 2026).
- **Lengte:** ~1500 woorden.
- **Visual hero:** [`inspiration/harness-is-os-nl.html`](harness-is-os-nl.html) als ingebedde statische export. De vier takeaways uit die visual (Mapping, Inversie, Economie, Trajectorie) structureren de tweede helft van het artikel.
- **Wiki-anker:** [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie OS-analogie + sectie Empirische verankering.
- **Primaire bronnen:** Lopopolo (OpenAI) *Harness engineering: leveraging Codex in an agent-first world* — herkomst van de term; Böckeler (Thoughtworks) *The Engineering of AI Agents — Context, Harnessing, and Autonomy* (QCon London 2026) — onafhankelijke bevestiging.
- **Structuur:** (1) Waar de term "harness" vandaan komt en waarom hij in februari 2026 plotseling overal opduikt. (2) Vijf parallellen: geheugen / planning / IO / isolatie / exception. (3) Wat dit voor MKB-bedrijven betekent: je koopt geen model, je bouwt een laag. (4) Hoe je in een leveranciersgesprek hoort op welke laag iemand werkt.
- **Provocatie:** *Als je leverancier "het beste model" verkoopt, verkoopt hij een CPU. Vraag waar het OS zit.*
- **Invitatie:** "Welke van de vijf vraagstukken is in jullie opstelling al opgelost — en welke gokken op het model? DM me als je hier wilt sparren."

### Stuk 3 · POST · *"Waarom productie-AI elke maandag opnieuw begint — en hoe teams dat oplossen."*

- **Hoofdboodschap:** Het contextvenster is RAM, niet schijf. Wat in sessie X gebeurt, is in sessie Y weg tenzij er een geheugenlaag tussen zit. Drie patronen die in 2026 productie bereikt hebben: hooks (Bratanic), agentic memory frameworks, harness-niveau context engineering.
- **Lengte:** ~400 woorden.
- **Visual:** bestaande `agent-wiki.gif` (toont accumulatie) of nieuwe variant van het maandag-begin-fenomeen.
- **Wiki-anker:** [`syntheses/knowledge-architectures-for-llm-agents.md`](../wiki/syntheses/knowledge-architectures-for-llm-agents.md).
- **Primaire bron:** Bratanic — *Unified Agentic Memory Across Harnesses Using Hooks* (Towards Data Science, 8 mei 2026). Secundair: Chase (LangChain) *Agent Development Lifecycle*.
- **Provocatie:** *Als je nieuwe medewerker elke maandag het dossier kwijt was, zou je dat geen drie weken pikken. Een AI die hetzelfde doet, accepteren bedrijven negen maanden.*
- **Invitatie:** "Hoe houdt jouw AI-opstelling kennis tussen sessies vast? Benieuwd."

### Stuk 4 · POST · *"RAG is niet dood. De term is dood."*

- **Hoofdboodschap:** De RAG-architectuur (zoeken in vectoren, daarna context-injectie) werkt nog steeds voor de juiste vraagsoorten. Wat verandert is het marketingvocabulaire — "context engineering", "agentic search". MKB-directies horen "RAG is achterhaald" en interpreteren dat verkeerd: de techniek leeft, de term is uit de mode.
- **Lengte:** ~400 woorden.
- **Visual:** statische uitsnede van kolom 02 (RAG) uit [`architecture-of-scale-nl.html`](architecture-of-scale-nl.html).
- **Wiki-anker:** [`syntheses/is-rag-dead.md`](../wiki/syntheses/is-rag-dead.md) — headline finding: *term retired, technique persists* (5 bronnen converge, conf 0,90).
- **Primaire bron:** Huber (Chroma) video *RAG is dead, the term is dead* (mei 2026).
- **Provocatie:** *Als je leverancier zegt "wij doen geen RAG, wij doen iets beters", vraag dan welk pad ze door de vector store maken. Negen van de tien keer: vector store, daarna cosinus, daarna top-K. Dat heet RAG.*
- **Invitatie:** "Welke termen uit jouw AI-offerte zijn marketing, welke architectuur? Reageer."

### Stuk 5 · ART · *"Vier manieren om één vraag te beantwoorden — en wanneer welke werkt."*

- **Hoofdboodschap:** Contextvenster, RAG, knowledge graph, LLM-wiki. Vier substraten, vier kostenstructuren, vier soorten vragen waarvoor ze geschikt zijn. De fout die MKB-directies systematisch maken: *één* architectuur kopen voor *alle* vragen.
- **Lengte:** ~1500 woorden.
- **Visual hero:** [`inspiration/architecture-of-scale-nl.html`](architecture-of-scale-nl.html) als ingebedde export.
- **Wiki-anker:** [`syntheses/knowledge-architectures-for-llm-agents.md`](../wiki/syntheses/knowledge-architectures-for-llm-agents.md) — drie-architectuur-beslisraamwerk (7 bronnen, conf 0,90).
- **Primaire bronnen:** Huber (Chroma) over vector-stream-limieten; Karpathy-thread (Towards AI, april 2026) over het LLM-wiki-patroon; Manditereza (HiveMQ) *Ontology-Driven Intelligence for Industrial AI Agents* over KG-substraat; artikelenseries van Adi Insights, Raju en Liu over wiki-implementaties.
- **Structuur:** (1) Drie soorten vragen die MKB-bedrijven aan AI stellen — specifiek-feitelijk ("wat is de levertijd van product X?"), brede overzicht ("welke trends spelen in markt Y?"), multi-hop-verbinding ("welke klant past bij welke installateur?"). (2) Per substraat: voor welke vraag is dit *minimaal voldoende* en voor welke *overkill*. (3) De voorinvestering-as uit de visualisatie: wat krijg je terug per geïnvesteerde dag. (4) Hybride als regel, monolithisch als veelvoorkomende fout.
- **Provocatie:** *De duurste architectuur is degene die het meest vertrouwd voelt — niet degene die het hardst werkt voor jouw vragen.*
- **Invitatie:** "Welke van de vier kolommen lijkt op jouw eigen AI-investering? DM me — ik teken graag mee."

### Stuk 6 · POST · *"Een LLM-wiki is geen tool. Het is een vorm van eigendom."*

- **Hoofdboodschap:** De LLM-wiki — een door agents bijgehouden, voor LLM-leesbare kennisbasis — is geen software-product maar een laag van permanent eigendom. Karpathy formuleerde het patroon in april 2026; sindsdien implementeren meerdere teams het. Witek bouwt het zelf — deze reeks staat er gedeeltelijk op.
- **Lengte:** ~450 woorden.
- **Visual:** [`inspiration/search-wiki.gif`](search-wiki.gif) (toont accumulatie) of nieuwe variant.
- **Wiki-anker:** [`concepts/llm-wiki.md`](../wiki/concepts/llm-wiki.md) (conf 0,91, 5 bronnen).
- **Primaire bronnen:** Karpathy-thread (originele bron); Adi Insights *I Used Karpathy's LLM Wiki to Build a Research Brain That Updates Itself* (Towards AI, april 2026); OceanBase ex-brain artikel; Raju explainer; Liu comparative-architecture (alle vier ingelezen op 2026-05-12).
- **Provocatie:** *Jouw bedrijf produceert al elke dag tien wiki-pagina's. Ze heten alleen "e-mail", "Notion", "PDF". De vraag is wie ze leest — een mens of ook een agent.*
- **Invitatie:** "Waar sterft institutionele kennis in jouw bedrijf? Reageer."

### Stuk 7 · POST · *"Het model is gehuurd. De harness is van jou."*

- **Hoofdboodschap:** Modelaanbieders brengen nu per kwartaal een nieuwe versie uit. Wat in het model zit, vervangt zichzelf. Wat in de harness zit, blijft. Economische implicatie voor MKB: investering in harness groeit door op zichzelf, investering in model verliest waarde per release.
- **Lengte:** ~400 woorden.
- **Visual:** nieuwe tegel **"Rent vs. Own"** — twee kolommen. Links: model (gehuurd, kwartaalcyclus, vervangt zichzelf). Rechts: harness (eigendom, accumuleert, draagt over).
- **Wiki-anker:** [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie Model is gehuurd, sectie Empirische verankering.
- **Bronnen:** rauwe releasecadens (Claude 4.5, dan 4.6, dan 4.7 in 12 maanden; GPT-4, dan 4o, dan 5, dan de o-serie); Sternfels (McKinsey) over modelobsolescentie-economie.
- **Provocatie:** *Wat je vandaag in het model investeert, draagt jouw bedrijf in 2027 niet. Wat je in de harness investeert, wel.*
- **Invitatie:** "Welke kolom krijgt deze maand jouw budget? Eerlijk antwoord, geen oordeel."

### Stuk 8 · POST · *"Vijf vragen die elke MKB-directeur aan zijn AI-leverancier moet stellen."*

- **Hoofdboodschap:** Vijf vragen waarmee je in tien minuten ziet of een leverancier op CPU-laag of OS-laag werkt. Concreet, geen jargon, scherpe antwoorden-of-afhaken-test.
- **De vragen:**
  1. *Hoe houdt jullie systeem kennis vast tussen sessies — toon de architectuur.*
  2. *Welk model gebruiken jullie, en hoe wisselen we het over een jaar uit?*
  3. *Voor welk vraag-type is jullie architectuur ontworpen — en voor welk niet?*
  4. *Wat blijft van ons als we morgen overstappen — welke artefacten zijn overdraagbaar?*
  5. *Toon een geval waar het systeem fout zat. Wat hebben jullie aangepast en op welke laag?*
- **Lengte:** ~500 woorden.
- **Visual:** nieuwe tegel **"Vijf vragen"** — vertical roadmap-stijl, blueprint look.
- **Wiki-anker:** [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) + [`concepts/agent-development-lifecycle.md`](../wiki/concepts/agent-development-lifecycle.md).
- **Primaire bronnen:** Chase (LangChain) *Agent Development Lifecycle*; Sternfels (McKinsey) over leverancier-doorlichting; Böckeler (Thoughtworks) over overdraagbaarheid.
- **Provocatie:** *Een leverancier die geen van de vijf vragen scherp kan beantwoorden, verkoopt je een CPU en noemt het een systeem.*
- **Invitatie:** "Welke vraag denk je dat jouw huidige leverancier het slechtst kan beantwoorden? Reageer."

### Stuk 9 · ART · *"Hoe AI-investering compoundt: een bouwplan voor MKB-directies."*

- **Hoofdboodschap:** De synthese van de hele reeks. Drie lagen: (a) substraat — wat is je bron-kennis, hoe blijft die leesbaar voor LLM's en mensen; (b) harness — geheugen, contracts, context engineering; (c) samenwerking — hoe directie, IT en operatie samen het systeem onderhouden. Wat in maand 1, 3, 6 en 12 zichtbaar wordt. Eén concreet artefact: live screenshot van Witeks eigen wiki + een agent-trace die de wiki gebruikt. **Open invitatie**: niet "huur mij" maar "ik kan dit pad doorlopen met je".
- **Lengte:** ~1700 woorden.
- **Visual hero:** compositie van beide visualisaties + screenshot van de echte wiki (`/Users/witoldtenhove/Projects/ai-wiki/wiki/`).
- **Wiki-anker:** alle drie syntheses + [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) als spine.
- **Bronnen:** Sternfels (McKinsey) over AI-strategie; Jassy (Amazon) over de veranderende rol van managers; Witeks eigen wiki als gedemonstreerd artefact.
- **Provocatie:** *MKB-bedrijven die nu hun harness opzetten bouwen in vijf jaar een onvergelijkbare voorsprong op MKB-bedrijven die wachten tot het model "rijp" is. Het model wordt nooit rijp. De harness wel.*
- **Invitatie (explicieter dan eerdere stukken):** "Ik ben Witek ten Hove. Ik bouw harness-laag voor MKB-bedrijven die met AI willen werken zonder dat hun kennis bij Big Tech eindigt. Mail mij op witek@businessdatasolutions.nl als je wilt verkennen wat voor jouw bedrijf passend zou zijn."

---

## Provocatie + invitatie — patroon

Elke aflevering eindigt met twee zinnen, in Witeks stem:

- **Provocatie:** scherp, niet onbeleefd. Concreet, niet ideologisch. Variatie per stuk — niet recyclen.
- **Invitatie:** open, niet verkopend. Variatie tussen "DM staat open", "reageer hieronder", "benieuwd hoe jij hierover denkt". Stuk 9 is de enige expliciete dienstverlenings-vermelding.

**Anti-patronen om te vermijden:**
- Geen "klik hier voor een gratis consult".
- Geen lange opsomming van wat Witek kan.
- Geen verkapte leveranciers-kritiek zonder onderbouwing (de softere thesis-keuze maakt dit expliciet ongewenst).
- Geen fictieve voorbeelden of bedrijfscases — alleen geanonimiseerde echte observaties of expliciet geciteerd bron-materiaal.

---

## Visuele identiteit + nieuw te maken visuals

**Stijl-anker (consistent met bestaande HTML's):**
- Font: Inter + JetBrains Mono + Instrument Serif.
- Palet: papier `#FCFBF6`, ink `#2A2722`, blauw `#2540C8`, oranje `#E54B2B`.
- Brutalist-blueprint als secundaire stijl voor tegels (bron: [`inspiration/A3 _ Brutalist blueprint.html`](A3%20_%20Brutalist%20blueprint.html)).

**Hergebruik bestaand:**
- [`harness-is-os-nl.html`](harness-is-os-nl.html) — hero stuk 2.
- [`architecture-of-scale-nl.html`](architecture-of-scale-nl.html) — hero stuk 5; uitsnede voor stuk 4.
- [`agent-wiki.gif`](agent-wiki.gif) — stuk 3.
- [`search-wiki.gif`](search-wiki.gif) — stuk 6.

**Nieuw te maken (in volgorde van urgentie):**

| Voor | Naam | Specs |
|---|---|---|
| Stuk 1 | `verouderd-vs-groeit-door.html` | Tegel 1080×1080, brutalist-blueprint. Twee kolommen: links wat verouderd (token-credits, modelversies), rechts wat doorgroeit (wiki, harness-laag, schema). |
| Stuk 7 | `rent-vs-own.html` | Tweekoloms-tegel 1200×675. Links CPU/gehuurd met kwartaalcyclus visueel, rechts OS/eigendom met accumulerende curve. |
| Stuk 8 | `vijf-vragen.html` | Vertical 1080×1350. Vijf genummerde vragen in blueprint-stijl. |
| Stuk 9 | `bouwplan-hero.html` | Compositie. Mini-versies van beide HTML-visualisaties links/rechts, daartussen een derde paneel met live screenshot van de echte wiki. |
| Optioneel stuk 5 | `drie-vragen-matrix.html` | Drie generieke vraagsoorten × vier architecturen = matrix. Inline in stuk 5. |

Alle nieuwe visuals: HTML met inline JS/CSS in dezelfde stijl als de bestaande inspiratie-bestanden, zodat ze als statisch beeld kunnen worden geëxporteerd voor LinkedIn én als interactief artefact op een eigen domein kunnen blijven leven.

---

## Wiki-referenties om naar te citeren

| Stuk | Primair anker | Secundaire bronnen (uit wiki) |
|---|---|---|
| 1 | [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie Definitie | AI Index Report 2026; Sternfels (McKinsey) |
| 2 | [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie OS-analogie | Lopopolo (OpenAI); Böckeler (Thoughtworks) |
| 3 | [`syntheses/knowledge-architectures-for-llm-agents.md`](../wiki/syntheses/knowledge-architectures-for-llm-agents.md) | Bratanic (Towards Data Science); Chase (LangChain) |
| 4 | [`syntheses/is-rag-dead.md`](../wiki/syntheses/is-rag-dead.md) | Huber (Chroma) |
| 5 | [`syntheses/knowledge-architectures-for-llm-agents.md`](../wiki/syntheses/knowledge-architectures-for-llm-agents.md) | Huber (Chroma); Karpathy-thread; Manditereza (HiveMQ); Adi-, Raju- en Liu-wiki-artikelen |
| 6 | [`concepts/llm-wiki.md`](../wiki/concepts/llm-wiki.md) | Karpathy-thread; Adi Insights; OceanBase ex-brain; Raju; Liu |
| 7 | [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) sectie Model is gehuurd | Sternfels (McKinsey) |
| 8 | [`concepts/agent-harness.md`](../wiki/concepts/agent-harness.md) + [`concepts/agent-development-lifecycle.md`](../wiki/concepts/agent-development-lifecycle.md) | Chase (LangChain); Böckeler (Thoughtworks) |
| 9 | Alle drie syntheses + `agent-harness.md` | Sternfels; Jassy (Amazon); eigen wiki |

**Citatie-conventie:** waar passend wikilink-naar-eigen-publicatie (https://wiki.witek.nl/…) als bewijs van de doorgroeiende harness die Witek zelf bouwt. Maakt de meta-laag zichtbaar zonder erover te praten.

---

## Hergebruik uit bestaande LinkedIn-drafts

Niet vanaf nul beginnen — recycle gericht. De personage-drafts leveren *toon en standpunt*, niet langer een plot.

| Bestaande draft | Recycle naar |
|---|---|
| [`linkedin-post-mkb-mt.md`](linkedin-post-mkb-mt.md) — Marieke-persona, mini-case versie | Persona-toetslens Marieke; toon-referentie voor stuk 1 en stuk 8 |
| [`linkedin-post-mkb-mt-wiki-harness.md`](linkedin-post-mkb-mt-wiki-harness.md) — wiki-in-harness | Argumenten voor stuk 6; provocatie-stijl |
| [`linkedin-post-mt-vier-mechanismen-ai-geheugen.md`](linkedin-post-mt-vier-mechanismen-ai-geheugen.md) — vier architecturen | Stuk 5 (artikel) — directe structuurbasis |
| [`linkedin-article-nl-latent-value-intersections.md`](linkedin-article-nl-latent-value-intersections.md) — latent value | Eventueel standalone teaser vóór stuk 1, of off-series follow-up na stuk 9 |
| [`linkedin-post-mkb-ict.md`](linkedin-post-mkb-ict.md) — Stefan-persona | Persona-toetslens Stefan; toon-referentie voor stuk 2 en stuk 4 |

---

## Cadans + productie-volgorde

**Cadans:** wekelijks, dinsdag 8:00 NL-tijd (LinkedIn-piek voor B2B).

**Tijdslijn:** week 0 = startweek. Reeks loopt week 1–10 (artikelen krijgen een extra week voor diepte).

| Week | Stuk | Voorbereiding-deadline |
|---|---|---|
| 1 | 1 (post) | T-3d |
| 2 | 2 (artikel) | T-7d |
| 3 | 3 (post) | T-3d |
| 4 | 4 (post) | T-3d |
| 5 | 5 (artikel) | T-7d |
| 6 | 6 (post) | T-3d |
| 7 | 7 (post) | T-3d |
| 8 | 8 (post) | T-3d |
| 9 | (week buffer voor artikel 9) | — |
| 10 | 9 (artikel) | T-10d |

**Productie-volgorde** (afwijkend van publicatie-volgorde):

1. **Eerst:** stukken 1, 2, 7, 9 schrijven — die bepalen de toon van de hele reeks.
2. **Daarna:** stuk 5 (zwaarste tussenartikel).
3. **Dan:** stukken 3, 4, 6, 8 — relatief lichte posts, makkelijker te schrijven als toon vaststaat.
4. **Per concept-stuk:** persona-toetslens-ronde (Marieke + Stefan) — twee leesrondes, één per persona.
5. **Taalredactie vóór publicatie:** elke definitieve tekst (post of artikel) wordt vóór publicatie gecontroleerd met de [`taalredactie-publicatie`](../.claude/skills/taalredactie-publicatie/SKILL.md) skill. De skill behandelt spelling, lidwoorden, niet-bestaande woorden, anglicismen, speciale tekens, aanspreekvorm-consistentie en zinsstructuur — en signaleert daarnaast (adviserend, niet corrigerend) structuurpunten volgens SCQA / Pyramid Principle. Het redactierapport en de gecorrigeerde versie worden naast de brontekst opgeslagen volgens skill-conventie (`taalrapport-<bestandsnaam>` in dezelfde map). De auteur beslist of structuuradviezen worden verwerkt.

**Visuals-productie loopt parallel:**
- `verouderd-vs-groeit-door.html` + `rent-vs-own.html` vóór week 1.
- `vijf-vragen.html` vóór week 8.
- `bouwplan-hero.html` + eventueel `drie-vragen-matrix.html` vóór week 10.

---

## Kritieke bestanden (overzicht)

**Lezen (bestaande context):**
- [`inspiration/architecture-of-scale-nl.html`](architecture-of-scale-nl.html)
- [`inspiration/harness-is-os-nl.html`](harness-is-os-nl.html)
- [`wiki/concepts/agent-harness.md`](../wiki/concepts/agent-harness.md)
- [`wiki/concepts/llm-wiki.md`](../wiki/concepts/llm-wiki.md)
- [`wiki/concepts/agent-development-lifecycle.md`](../wiki/concepts/agent-development-lifecycle.md)
- [`wiki/syntheses/is-rag-dead.md`](../wiki/syntheses/is-rag-dead.md)
- [`wiki/syntheses/knowledge-architectures-for-llm-agents.md`](../wiki/syntheses/knowledge-architectures-for-llm-agents.md)
- Bestaande LinkedIn-drafts in `inspiration/linkedin-*.md`.

**Te produceren (nieuwe content):**
- 9 LinkedIn-tekst-bestanden in `inspiration/linkedin-harness-reeks/` (bv. `01-wat-investeer-je.md`, `02-os-analogie.md`, …).
- Per stuk: één taalredactie-rapport `taalrapport-<bestandsnaam>` naast de brontekst (output van de `taalredactie-publicatie` skill).
- 4–5 nieuwe HTML-visuals in `inspiration/visuals-harness-reeks/`.
- Bij elk gepubliceerd stuk: log-entry in [`wiki/log.md`](../wiki/log.md) onder een nieuwe op `publish` (afstemmen vóór eerste publicatie).

**Niet aanraken:**
- Wiki content-pagina's (alleen citeren) — geen edits door deze reeks behalve via reguliere ingest-flow als de reeks zelf later als source wordt opgenomen.

---

## Open punten (te beslissen tijdens uitvoering)

1. **Domein voor interactieve visuals:** publiceren we de HTML-visualisaties op `wiki.witek.nl` of een apart subdomein (`harness.witek.nl`)? Beïnvloedt linking-strategie in de stukken.
2. **Stuk 1 timing:** publiceren in eerste week, of eerst latent-value-intersections-artikel als warming-up?
3. **Optioneel stuk 10 — "drie maanden na de reeks":** korte post met geanonimiseerde geleerde lessen uit drie maanden DM-conversaties die de reeks heeft opgeleverd. Beslissen op basis van engagement.
4. **Engelse versie:** alle bestaande visuals hebben EN-tegenhangers (`*-en.html`). Reeks in EN parallel publiceren of NL-first met EN-bundel later? Standaard: NL-first.
5. **Geanonimiseerde voorbeelden:** stukken 3, 5 en 9 winnen aan kracht met één concreet (geanonimiseerd) voorbeeld uit eerder werk. Welke klantcontext mag/kan publiek?

Deze punten zijn niet blokkerend voor week 1 — beslissen kan tijdens uitvoering.
