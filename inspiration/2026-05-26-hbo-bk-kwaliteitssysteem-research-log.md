---
type: research-log
topic: "Wiki-grounded answers voor HBO Bedrijfskunde PRD over een nieuw kwaliteitsmanagementsysteem"
date: 2026-05-26
output_target: "PRD-input voor HAN Bedrijfskunde kwaliteitsmanagementsysteem (vier vragen, evidence-only)"
related_output: "2026-05-26-hbo-bk-kwaliteitssysteem-prd-input.md"
related_prior: "2026-05-20-visienotitie-han-bk-kwaliteitsmanagement-ai-native.md"
prd_under_revision: "https://hanbedrijfskunde.github.io/prd-kwaliteit/PRD-Kwaliteitsmanagementsysteem-HBO.html"
---

# Research log — HBO Bedrijfskunde kwaliteitsmanagementsysteem

Vier-niveau iteratieve wiki-query (`iterative-wiki-query` skill) op vier door de gebruiker geformuleerde vragen rond een nieuw kwaliteitsmanagementsysteem voor een Nederlandse HBO Bedrijfskunde-opleiding. Gebruiker leverde de feitelijke situatie:

- Kwaliteit is laag; studenten zijn ontevreden.
- Een recente curriculum-innovatie *"faalde in productie"* — student-evidentie: examenslagingspercentages > 90%, dus te makkelijk.
- Moraal van docenten is laag; verzuim is hoog.
- Er is geen strategie.

Gebruiker-instructie was expliciet: ***evidence-only, niets aannemen, als de wiki geen volledig antwoord biedt: dat zeggen***. Daarom sluit elk antwoord af met een *"Wat de wiki niet zegt"*-blok.

---

## Niveau 0 — drie startvragen

De gebruiker leverde *vier* vragen. Per de skill-conventie *drie startvragen* werken niet als rigide regel hier — de vier vragen worden behandeld als vier parallelle research-threads die een gedeelde bewijsbasis hebben:

1. Wat kan onderwijs leren van AI-native bedrijven op kwaliteitsmanagement?
2. Welke stappen zijn nodig om de organisatie te transformeren en in welke volgorde?
3. Welke signalen moet het management in dit proces zien?
4. Welke rol gaat AI spelen in de toekomstige kwaliteit van onderwijs?

---

## Niveau 1 — pagina's uit `wiki/index.md`

Gelezen (gedeeltelijk waar bestanden > 25k tokens):

- `wiki/concepts/warner-wager-process-model.md` — antwoordt vooral Q2 (transformatie-skeleton)
- `wiki/concepts/dynamic-capabilities.md` — Q2 (sense/seize/transform; Erginbilgić als non-digital control case)
- `wiki/concepts/strategy.md` — Q2 (strategie-als-participatie doctrine van Erginbilgić; Martin's *theory of winning*; Oberholzer-Gee's value-stick)
- `wiki/concepts/agent-harness.md` — Q1 (vier-laagsmodel Context/Constraints/Contracts/Compounding); Q4 (model rented / harness owned)
- `wiki/concepts/enterprise-ai-adoption.md` — Q1, Q4 (52-bron concept; tien framework-vantages)
- `wiki/concepts/micro-productivity-trap.md` — Q3 (failure-modes; 11-bron convergentie)
- `wiki/concepts/automation-vs-augmentation.md` — Q1, Q4 (15 sub-claims; Krakowski als de scherpste empirische ankerpunt)
- `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` — Q1 (de tien-frameworks-decision-tree)
- `wiki/index.md` — partial (te groot voor volledige read; gescand op structuur)

Kernantwoorden per startvraag:

- **Q1**: AI-native bedrijven scheiden *model* (wat output produceert) van *harness* (wat scoort, corrigeert, leert, compoundeert). De harness is wat compoundeert in waarde; het model is gehuurd en vervangbaar. Vier-laagsmodel: Context, Constraints, Contracts, Compounding.
- **Q2**: Erginbilgić's Rolls-Royce playbook (wiki's enige pure non-digital industriële transformatie-anker, McKinsey-genoemd *"a case study in the art of corporate transformation"*) levert een chronologische sequentie van zeven stappen — diagnose-vóór-dag-één → burning-platform-met-visie → semantiek (transformatie ≠ herstructurering) → strategie-als-participatie → vier pijlers → laagafbouw → veerkracht-als-procescapaciteit.
- **Q3**: Drie categorieën signalen: (a) transformatie-wordt-gehoord (Carucci's vier weerstand-categorieën), (b) transformatie-faalt-in-productie (Friday-in-March pattern, Krakowski's *gradual decline*-finding), (c) het meetsysteem-zelf-is-misleidend (micro-macro-divergentie, Goodhart-correlaat in Martin).
- **Q4**: De wiki bevat slechts één direct feit over AI in onderwijs (AI Index 2026: >80% van Amerikaanse middelbare- en universiteitsstudenten gebruikt AI voor schoolwerk; 6% van docenten zegt dat AI-beleid duidelijk is). De rest is *transfer* uit AI-native enterprise-quality patronen.

### Niveau-1 vervolgvragen

Van `warner-wager-process-model`:
- 1.1 Hoe operationaliseert Erginbilgić concreet `strategic-renewal/organizational-culture` zonder digital-mindset-element?
- 1.2 Welke W&W-cellen *zouden* een onderwijstransformatie raken die deze bron niet raakt?
- 1.3 Welke rol-mapping uit `role_defaults:` past op een HBO-context (CEO ↔ instituutsdirecteur, CHRO ↔ HR-directeur, etc.)?

Van `agent-harness`:
- 2.1 Wat is de Friday-in-March worked example precies, en hoe vertaalt dat naar onderwijs?
- 2.2 Wat zegt de Khattab et al. transferability-finding over de educatieve toepasbaarheid?
- 2.3 Is er een educatief equivalent van de subtraction principle?

Van `strategy`:
- 3.1 Wat is de operationele uitwerking van Erginbilgić's 25-30 workshops met 500+ medewerkers?
- 3.2 Hoe verhouden Martin's *theory of winning* en Erginbilgić's *strategy-as-participation* zich tot elkaar?
- 3.3 Wat zou een "value-stick" analyse voor onderwijs concreet inhouden?

---

## Niveau 2 — links gevolgd

Vier bronpagina's gelezen:

- `2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` — antwoordt 1.1, 3.1, en levert het volledige zeven-stappen-playbook.
- `2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` — antwoordt op de *waarom* van de 90%-slagingspercentage-paradox: kwantiteit-over-kwaliteit metric in AI-tijdperk; gear-3 reactive work is wat AI overneemt.
- `2026-05-07-carucci-resistance-as-data.md` — antwoordt op Q3 (weerstand-categorisering); reframeert "legitiem vs irrationeel" als foute vraag.
- `2025-06-09-krakowski-human-centered-ai-field-experiment.md` — antwoordt op Q4 (peer-reviewed RCT: untailored AI deployment veroorzaakt *gradual decline*, niet zero gain — *worse than no intervention*).

Kernantwoorden gekoppeld aan Niveau-1 vragen:

- **1.1**: Erginbilgić past `strategic-renewal/organizational-culture` toe als *non-compromise-on-mediocrity* + *demanding-with-fairness-and-transparency* + *fast-and-flexible cadence*; de *digital-mindset*-clausule blijft optioneel.
- **3.1**: CEO-attendance bij 25–30 workshops; 500+ medewerkers door het strategievormingsproces; twee protocolregels (*"no hierarchy in the room"* + *"this is going to be chaotic"*); alignment is de *output van participatie*, niet de output van communicatie. Expliciet contrast met *"strategy in a dark room with consultants."*
- **Q3 verdieping (Carucci)**: drie leider-traps (personalize / moralize / rush to resolution); vier signaal-categorieën (Loss / Anxiety / Lack of control / Flaws in change); de stilte in de kamer is geen alignment maar *people stopped speaking up*.
- **Q4 verdieping (Krakowski)**: vier interactie-design parameters (work procedure / decision authority / training / incentives), getailleerd op Kirton 1976 cognitieve stijl (adaptor/innovator). Work procedure is de meest kritieke parameter. De *"prison quote"* van een Deense innovator onder untailored conditie is de kwalitatieve mechanisme-evidentie.

### Niveau-2 vervolgvragen

A1. Welke parallel bestaat er tussen Erginbilgić's *layer elimination without losing operational people* en HBO-context?
A2. Hoe kan de Krakowski-vier-parameter framework vertaald worden naar lerar-AI-interactie?
A3. Wat is de exacte operationalisatie van Storoni's gear-2-protection in een HBO-werkweek?

B1. Hoe past Carucci's *"flaws-in-change"* categorie op de docenten die de 90%-slagingspercentage-curriculum-innovatie ervoeren?
B2. Welke wiki-bron behandelt het verschil tussen *pilots-as-stage* (MIT CISR) en *pilots-as-trap* (Bain/OpenAI) — relevant voor curriculum-innovatie?
B3. Wat zegt de wiki over evalueren *wat interessant fout ging*, versus alleen pass/fail meten?

---

## Niveau 3 — verkort (zoals de skill toestaat)

Niveau 3 is bewust verkort gehouden — de bronnenruimte is na Niveau 2 voor de vier specifieke gebruikersvragen *uitgeput voor zover de wiki er evidence op heeft*. De wiki bevat geen onderwijs-specifieke bronnen die een vierde diepteslag zouden opleveren; verdere reads zouden steeds dezelfde patronen herhalen. Wat wel gelezen werd op Niveau 3, in passages binnen de Niveau-2 bronnen:

- Het *Friday-in-March pattern* uit `agent-harness` (passage in concept-page, niet aparte bron) — antwoord op A2/B1.
- De *Kiron-Schrage verification → evaluation → learning capture flywheel* uit `micro-productivity-trap` section 4–5 — antwoord op B3.
- De *Augmented Learners 2×2 (15% cohort)* uit `enterprise-ai-adoption` en de tien-frameworks-decision-tree — context voor de cross-cutting synthese.

---

## Synthese — de antwoorden per vraag

> De volgende secties zijn een directe mirror van het plan-bestand (`~/.claude/plans/i-am-consulting-the-keen-wigderson.md`). De gestructureerde *bronnenmatrix* aan het eind van dit document maakt elke claim traceerbaar.

### Q1 — Wat kan onderwijs leren van AI-native bedrijven op kwaliteitsmanagement?

**Headline.** AI-native bedrijven scheiden de *output-producerende laag* (model; voor onderwijs: lesgevers en curriculum-units) van de *kwaliteits-laag* die scoort, corrigeert, leert, compoundeert. **De kwaliteitslaag is wat in waarde compoundeert; de output-laag is huurbaar.** Citaat uit `agent-harness` (Chatterjee 2026): *"the model is what you rent. The harness is what you own."*

Zeven evidence-claims (samengevat; volledige uitwerking in plan-bestand):

1. **Kwaliteit is een harness-laag** — Context / Constraints / Contracts / Compounding (Chatterjee in `agent-harness`).
2. **Build constraints before cleverness** — de *Friday-in-March story* is de canonical failure (`agent-harness`).
3. **The ratchet** — *"every line in a good AGENTS.md should be traceable back to a specific thing that went wrong"* (Osmani in `agent-harness`).
4. **Verification ≠ evaluation** — Kiron-Schrage flywheel uit `micro-productivity-trap`: *"What was **interestingly** wrong?"*
5. **A decent model with a great harness beats a great model with a bad harness** (Osmani, met Khattab et al. transferability empirisch anker).
6. **Augmentation is contingent on interaction-design** — Krakowski et al. 2025: untailored = gradual decline; tailored = positief.
7. **Momentum beats perfection / 5× expectation** — Brooklyn Solutions via Allen / AWS, in `enterprise-ai-adoption`.

**Wat de wiki niet zegt over Q1**: geen bron over NVAO / EFQM / AACSB / EQUIS / ISO 21001 / ESG / Inspectie van het Onderwijs; geen bron over student-as-customer vs co-creator framings; de harness-analogie behandelt studenten als *outputs* — een vereenvoudiging.

### Q2 — Welke stappen, in welke volgorde?

**Headline.** Erginbilgić's Rolls-Royce-playbook (`2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook`) levert de wiki's enige non-digital transformatie-sequentie, met McKinsey-validatie. De zeven stappen:

1. **Externe benchmark BEFORE day-one** (Erginbilgić commissioneerde diagnose vanaf Sept '22, vier maanden vóór startdatum).
2. **Burning platform = diagnose + visie in één artefact** (1.5 uur Jan '23 town-hall, externally-benchmarked, met visie gepaard).
3. **Restructuring ≠ transformation** als semantische distinctie — niet alleen herbenaming, ander change-theory.
4. **Strategie-als-participatie** (25–30 workshops, 500+ medewerkers, *"no hierarchy in the room"* + *"this is going to be chaotic"*); granulariteit als validatiecriterium.
5. **Vier pijlers**: People + Granular Strategy + Commercial Discipline (= value-creation; Oberholzer-Gee's WTS-lowering via *making the job a better job*) + Performance Culture (360 management).
6. **Eliminate layers, niet operational capability** — risk-of-keeping > pain-of-cutting.
7. **Bouw veerkracht als procescapaciteit, niet als forecast** — mindset → response capability → agility → action orientation.

**Warner-Wäger overlay**: drie cellen worden actief in de Erginbilgić-mapping (`strategic-renewal/organizational-culture`, `digital-seizing/strategic-agility`, `contextual/internal-barriers`); de wiki houdt deze cellen als *transformation primitives* die buiten de digital lens werken (`warner-wager-process-model`).

**Wat de wiki niet zegt over Q2**: geen onderwijs-specifieke transformatie-sequence; geen evidence over OR/medezeggenschapsdynamiek; geen NVAO-timing-constraints.

### Q3 — Welke signalen?

**Headline.** Drie categorieën signalen:

**(a) Transformatie wordt gehoord:**
1. Weerstand verschijnt — *interpreteer, onderdruk niet*. Carucci's drie traps (personalize / moralize / rush) + vier categorieën (Loss / Anxiety / Lack of control / Flaws in change).
2. De kamer wordt stil — dat is *geen* alignment. *"It means it's no longer safe or useful to tell the leader what they really think"* (Carucci).

**(b) Transformatie faalt in productie:**
3. Pilot slaagt, productie faalt — *Friday-in-March pattern* + MIT NANDA 95%-zero-return-finding.
4. 90% slagingspercentage = *gear-3 reactive-work* signaal, geen kwaliteitssignaal (Storoni). Quantity-over-quality in AI-tijdperk meet het verkeerde.
5. Untailored interventie veroorzaakt *decline*, niet zero gain (Krakowski) — de *"prison"* quote.
6. Ziekteverzuim, terugtrekking, motivatie-collaps als staff-side correlaat — wiki houdt dit als *systeem-mismatch* signaal, niet als *zwakke mensen* signaal.

**(c) Meetsysteem zelf misleidt:**
7. Micro-macro divergentie (DORA) — individuele winsten compoundeert niet naar firm-level value.
8. Wat geGoodhart-isd wordt is geen metric meer — Martin's *plan ≠ strategy* in `strategy`.
9. Leiderschap dat niet hard genoeg duwt — non-compromise on mediocrity (Erginbilgić); *demanding-with-fairness-and-transparency*, niet tough love.

**Wat de wiki niet zegt over Q3**: geen onderwijs-specifieke signalen-taxonomie; geen kwantitatieve drempelwaarden; geen student-mental-health-collaps signaal.

### Q4 — Welke rol gaat AI spelen?

**Headline.** Wiki bevat één direct AI-in-onderwijs feit. Zes evidence-claims op basis van transferbare patronen:

1. **AI neemt kwantiteit, mensen nemen kwaliteit** — Storoni's definitionele reframe.
2. **Antropomorfiseer AI niet** — Kropp et al. 2026 RCT (N=1,261): AI-as-employee framing veroorzaakt 9pp accountability-drop, 44% meer escalaties, 18% minder errors caught.
3. **Augmentation is contingent on interaction-design** — Krakowski et al. (zie ook Q1 claim 6).
4. **Bescherm de gear-2 cognitieve toestanden** (Storoni's drie-gear-framework).
5. **AI is amplifier en mirror** (DORA via `agent-harness`) — AI exposes en accelerates bestaande kwaliteit, creëert geen nieuwe.
6. **Models commoditize; what's owned compounds** — drie onafhankelijke vantages: Chatterjee (engineering), Nishar-Nohria (firm-boundary), Kiron-Schrage (organizational learning).

**Wat de wiki niet zegt over Q4**: geen bron over AI in hoger onderwijs specifiek; geen academic-integrity beleid onder AI; geen AI-literacy-curricula; geen Nederlandse-context.

### Cross-cutting synthese

***Kwaliteit is een harness-laag, geen model-laag.*** Eén architectonische claim verenigt de antwoorden op alle vier vragen — operationeel identiek op drie onafhankelijke lagen:

1. **Engineering** — Chatterjee's vier-laagsmodel.
2. **Organisationeel leren** — Kiron-Schrage flywheel.
3. **Transformatie-playbook** — Erginbilgić's strategie-als-participatie + granulariteit + 360-performance + non-compromise-on-mediocrity, ratchetend tegen externally-benchmarked diagnose.

De convergentie is de sterkste single transfer van de wiki naar de HBO Bedrijfskunde context.

---

## Bronnenmatrix

Elke load-bearing claim in de synthese is in deze tabel traceerbaar naar een wiki-pagina, met verbatim citaat waar gebruikt.

| Wiki-pagina | Vraag | Gebruikte claim | Verbatim citaat (waar gebruikt) |
| --- | --- | --- | --- |
| `concepts/agent-harness.md` | Q1, Q3, Q4 | Vier-laagsmodel (Context/Constraints/Contracts/Compounding); model rented / harness owned; Friday-in-March story; the ratchet; subtraction principle; transferability (Khattab et al.); *"AI is an amplifier and a mirror"* (DORA citatie) | *"the model is what you rent. The harness is what you own."* / *"It is cheaper to build the layer than to write the apology emails."* / *"Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong — ratchet, don't brainstorm."* / *"AI is an amplifier and a mirror. It magnifies the existing strengths and it holds up a mirror to those weaknesses."* |
| `concepts/micro-productivity-trap.md` | Q1, Q3 | Verification ≠ evaluation; Kiron-Schrage flywheel; *"What was interestingly wrong?"*; MIT NANDA 95%-zero-return; *operators see problems leaders dismiss*; eleven-source convergence | *"Most organizations practice verification masquerading as evaluation — treating AI outputs as verdicts to confirm rather than starting points to interrogate. The result is consumption dressed up as adoption."* / *"95% of organizations are getting zero return."* / *"The very people resisting the change are the ones closest to the risks that could derail it."* |
| `concepts/warner-wager-process-model.md` | Q2 | Twaalf-cell vocabulary; *transformation primitives* hypothese; Erginbilgić als eerste non-digital test case; drie cellen actief in Rolls-Royce mapping | *"the cells are transformation primitives whose digital-flavour reflects the original sample, not a load-bearing scope restriction."* |
| `concepts/dynamic-capabilities.md` | Q2 | Teece sense/seize/transform; Rolls-Royce non-AI control case; convergentie tussen AI-era en pre-AI transformatie-literatuur | *"the AI-era literature ... is best read as digital-flavoured variations on transformation primitives that the non-AI literature has been articulating for decades."* |
| `concepts/strategy.md` | Q2, Q3 | Strategy-as-participation doctrine (Erginbilgić); planning ≠ strategy (Martin); value-stick (Oberholzer-Gee); WTS-lowering via *making the job a better job*; *"strategy is a journey"*; granulariteit als validatiecriterium | *"I don't do strategy in the dark room with consultants. I personally attended 25–30 workshops … every like 500-plus people joined. When you are done, whole organisation is aligned because they were in the room when you were making the decision."* / *"no hierarchy in the room"* / *"this is going to be chaotic"* / *"It's much easier to say, 'I'll build a factory, I will hire more people, et cetera' than 'I will have customers end up liking our offering more than those of competitors.'"* / *"value creation precedes value capture."* |
| `concepts/enterprise-ai-adoption.md` | Q1, Q4 | Tien framework-vantages; 88% adoption / 1% mature; Brooklyn Solutions 5× / momentum-beats-perfection; AI Index 2026 student-AI-use feit; models commoditize | *"durable advantage in AI comes from what the firm owns and accumulates, not from which model it rents."* / *">80% of U.S. high school and college students use AI for school-related tasks; only half of middle/high schools have AI policies and just 6% of teachers say those policies are clear."* |
| `concepts/automation-vs-augmentation.md` | Q1, Q4 | *"Put humans on judgment work, agents on execution work"* (Allen); *"human starts the work, human ends the work"* (Brooklyn); anti-anthropomorphizing finding (Kropp); Storoni quality-over-quantity reframe; tailored vs untailored augmentation (Krakowski) | *"put humans on judgment work, agents on execution work."* / *"we essentially always have a human start the work and a human end the work."* / *"the productivity of a company is no longer proportional to the quantity of output of its human workers, because the realm of quantity is being taken over by AI and technology. Humans now influence the productivity of their organization by the quality of their output."* |
| `syntheses/organizational-frameworks-for-ai-adoption.md` | Q1, Q2 | Tien-frameworks-decision-tree; *pick a framework by the executive's question, not the framework's brand*; convergence around process-redesign-is-main-cost (zeven bronnen) | *"Pick a framework by the executive's question, not the framework's brand. Each framework names a different layer; mismatched layers explain most 'why didn't this work' stories."* |
| `sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | Q2, Q3 | Volledig zeven-stappen playbook; vier-pijlers (twee expliciet, twee gereconstrueerd); demanding ≠ tough love; *"non-compromising mediocrity"*; *"marketable but staying"*; resilience playbook (mindset → response → agility → action) | *"You cannot say the things you just said without data because it will just learn like you are criticising them effectively. With data, I demonstrated where the company is."* / *"non-compromising mediocrity at that level kills the organisations but also good people"* / *"You want people in your organisation who are highly marketable, but they want to stay with you. That's the secret sauce."* / *"It's not about actually predicting the world, it is about how your company now thinks about dealing with external shocks."* / *"I am demanding... I want you to improve... pace and intensity is for a purpose."* |
| `sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | Q3, Q4 | Definitional reframe quality-over-quantity; three-gear framework; gear-3 als micro-productivity-trap mechanisme op individueel niveau; gear-2 als beschermwaardige cognitieve toestand; intrinsic motivation via learning-progress-mechanism | *"It's a trade-off between speed and accuracy. Your speed becomes faster, but your accuracy goes down. ... You will make mistakes, errors, and you will miss nuances."* / *"workers trapped in gear-3 are producing the kind of output that gets automated next."* |
| `sources/2026-05-07-carucci-resistance-as-data.md` | Q3 | Resistance-as-data reframing; drie leider-traps; vier signaal-categorieën; *the room goes quiet ≠ alignment*; *flaws-in-change* als load-bearing categorie | *"All resistance is meaningful data. The leader's job isn't to determine whether pushback is valid; it's to diagnose what it's signalling."* / *"the more leaders push to eliminate resistance, the more they amplify it or drive it underground. People stop speaking up but that doesn't mean they've aligned."* / *"The 'legitimate concern' vs 'resistance' distinction is most dangerous here because it encourages leaders to filter feedback rather than listen to it."* |
| `sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | Q1, Q4 | Peer-reviewed RCT; vier interactie-design parameters (work procedure / decision authority / training / incentives); work procedure is meest kritieke parameter; *untailored produces decline*; *prison quote* als mechanisme-evidentie; mediation analysis via login-data | *"untailored augmentation results in negative treatment effects compared with both the tailored and control conditions."* / *"We got this super tool, and at the same time, I felt like in prison. There was no freedom to work the way I wanted to work. … This level of controlling killed my internal drive!"* / *"Work procedure emerged as the most critical parameter, shaping daily operational interactions."* |

## Wiki-pagina's NIET geraadpleegd (en waarom)

Volledigheidshalve — pagina's die thematisch raken maar bewust niet zijn ingelezen in deze sessie:

- `concepts/ai-deskilling.md` — relevant voor lange-termijn AI-in-onderwijs implicatie, maar zwakker dan Storoni/Krakowski als bron voor Q4.
- `concepts/jagged-frontier.md` — over per-taak AI-fit; zou Q4 verdiepen maar voegt geen kern-claim toe.
- `concepts/durable-skills.md` — Storoni's *self-regulation-under-uncertainty meta-skill* zit hier; reeds gecit via Storoni-bron.
- `syntheses/strategy-finite-vs-infinite-game.md` — interessant voor strategie-framing maar geen direct antwoord op de vier vragen.
- `concepts/infinite-game.md` — idem.
- Bronnen van onder andere Allen/AWS, Forsgren/Macvean, Kiron-Schrage, Kropp et al. — *secondair geraadpleegd via cita ties in de gelezen concept-pagina's*, niet als primair bestand. De citaten daarin zijn niet onafhankelijk geverifieerd in deze sessie.

## Disclaimers

- Synthese is *interpretatief* (de gebruiker vroeg expliciet om antwoorden op vragen). Cross-source-neutraliteit (per de [feedback_cross_source_neutrality memory](../../.claude/projects/-Users-witoldtenhove-Projects-ai-wiki/memory/feedback_cross_source_neutrality.md)) geldt voor wiki-ingest-time hygiene, niet voor synthese-output naar de gebruiker.
- De Khattab et al. *transferability-finding* (één-harness werkt op vijf andere modellen) is in `agent-harness` ingelezen als second-hand citaat van een Tsinghua/DSPy-team paper via een May 2026 YouTube-synthese. De wiki vermeldt: *"the two underlying papers are not separately ingested. Treat the specific numbers as second-hand until primary-source ingest confirms them — but the direction is durable independent of the specific magnitudes."* Dit is in de synthese geneutraliseerd door alleen de *richting* (transferability) te claimen, niet de specifieke magnitudes.
- De vier *"Wat de wiki niet zegt"*-blokken zijn voor de eerlijkheid van de research load-bearing. Negeer of overschrijf ze niet bij verdere bewerking.

## Verwijzing naar PRD-input

Het bijbehorende PRD-input-bestand `2026-05-26-hbo-bk-kwaliteitssysteem-prd-input.md` snijdt deze synthese tot PRD-secties (probleemstelling, vijf principes, transformatie-sequence, success signals, risk register, wat er niet in mag, open vragen) — in het Nederlands, ready to integrate in de bestaande PRD-draft op `hanbedrijfskunde.github.io/prd-kwaliteit/PRD-Kwaliteitsmanagementsysteem-HBO.html`.
