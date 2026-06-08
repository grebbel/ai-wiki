---
type: prd-input
topic: "Concept-input voor PRD Kwaliteitsmanagementsysteem HBO Bedrijfskunde"
date: 2026-05-26
language: nl
prd_under_revision: "https://hanbedrijfskunde.github.io/prd-kwaliteit/PRD-Kwaliteitsmanagementsysteem-HBO.html"
research_log: "2026-05-26-hbo-bk-kwaliteitssysteem-research-log.md"
related_prior: "2026-05-20-visienotitie-han-bk-kwaliteitsmanagement-ai-native.md"
note: |
  Dit document is geen volledige PRD. Het levert PRD-secties op basis van wiki-evidentie, in te bouwen in de bestaande PRD-draft. Elke claim is herleidbaar tot het bijbehorende onderzoekslog; daar staat ook welk citaat uit welke wiki-pagina komt. Waar de wiki geen bewijs heeft, staat dat expliciet.
---

# PRD-input: Kwaliteitsmanagementsysteem HBO Bedrijfskunde

Een synthese op basis van bewijs uit de `ai-wiki` (131 bronnen, 32 concepten, 4 syntheses) — bedoeld als concept-input voor de bestaande PRD. Bevat zes secties die direct in een PRD passen, plus een lijst open vragen waarop de wiki geen antwoord biedt.

---

## 1. Probleemstelling

De huidige situatie van de opleiding combineert vier symptomen die in de wiki herkenbaar zijn als één onderliggend patroon:

1. **Studenttevredenheid is laag, slagingspercentages zijn hoog (> 90%) — studenten ervaren het curriculum als te makkelijk.** Het wiki-canonieke signaal van *kwantiteit boven kwaliteit* in het AI-tijdperk. Mithu Storoni (HBR IdeaCast, mei 2026, geciteerd in `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md`): *"de productiviteit van een organisatie is niet langer evenredig met de kwantiteit van menselijke output, omdat het domein van kwantiteit door AI wordt overgenomen. Mensen beïnvloeden productiviteit door de kwaliteit van hun output."* Een meetwaarde die het aantal geslaagden beloont in plaats van leerdiepte, meet in 2026 het verkeerde.
2. **Lage moraal bij docenten plus hoog ziekteverzuim.** De wiki duidt deze combinatie als een signaal van *systeem-ontwerp-mismatch*, niet van zwakke mensen. De peer-reviewed RCT van Krakowski e.a. (Management Science, 2025, N=72 Noord-Europese farma-experts; `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md`) toont dat *untailored* interventies, ook goedbedoelde, *negatieve* prestaties opleveren ten opzichte van géén interventie. Mechanisme: rolconflict, motivatie-instorting, terugtrekking. De *prison quote* van een Deense innovator: *"We kregen deze geweldige tool, en tegelijkertijd voelde ik me in de gevangenis... dit niveau van controle doodde mijn interne motivatie!"*
3. **Geen strategie.** *Plannen ≠ strategie*. Roger Martin (HBR 2022, `wiki/concepts/strategy.md`): *"Strategie specificeert een competitieve uitkomst (studenten willen jouw aanbod genoeg om er voldoende van af te nemen om je in staat te stellen waarde te creëren) — je beheerst dat niet; klanten beslissen."* Plannen vormen de comfortzone — een lijst van kostenkant-activiteiten die je beheerst. Strategie is wat moet worden waargemaakt.
4. **Een curriculum-innovatie faalde in productie.** Het wiki-canonieke *Friday-in-March pattern* (`wiki/concepts/agent-harness.md`): een systeem dat *"competent, hulpvaardig, werkt zoals ontworpen"* is, faalt omdat de *laag eromheen* — de checkpoint-laag, de intentie-validatielaag, de kwaliteitsscore-laag — niet bestaat. De praktijkvingerafdruk van zo'n ontbrekende checkpoint-laag bij curriculumontwerp is slagingspercentages > 90% bij ontevreden studenten.

**De onderliggende these.** De vier symptomen zijn *uitingen van één architectonisch tekort*: er is geen onafhankelijke kwaliteitslaag rond het onderwijsproces — geen *kwaliteits-harness* die toetsmateriaal scoort, intentie valideert, vroege faalsignalen opvangt, telemetrie aggregeert en leerervaring over cohorten laat cumuleren. Het doel van de PRD: *deze harness bouwen*.

---

## 2. Vijf principes voor het kwaliteitsmanagementsysteem

Vijf ontwerpprincipes op basis van bewijs, elk gebaseerd op een convergentie van ten minste twee wiki-bronnen.

### Principe 1 — Kwaliteit is een harness-laag, geen model-laag

De *"model"-laag* van een opleiding — lesinhoud, individuele vakken, individuele toetsen, en in administratieve zin de individuele rolvervullers — is op termijn vernieuwbaar. De *"harness"* — de architectuur die intake, toetsing, feedback, cohortmonitoring en jaar-op-jaar bijstelling met elkaar verbindt — is wat de instelling bezit en wat in waarde toeneemt door gebruik. Bron: `wiki/concepts/agent-harness.md` (Chatterjee 2026): *"the model is what you rent. The harness is what you own."* De analogie is meer dan een metafoor; zij is een structureel inzicht over waar institutioneel kapitaal naartoe moet stromen. Eén waarschuwing vooraf: de analogie komt uit AI-engineering en breekt op één punt zodra zij de mens-laag raakt — die breuk wordt expliciet behandeld in 1.7 voordat zij tot beleidsuitspraken wordt verheven.

#### 1.1 De analogie: wat een harness eigenlijk is

In de AI-engineering-literatuur (Prompt Engineering, mei 2026, in `wiki/concepts/agent-harness.md`) wordt de relatie tussen een groot taalmodel en zijn omringende infrastructuur uitgelegd via een OS-analogie:

| Computer | AI-systeem | Onderwijs (deze vertaling) |
|---|---|---|
| CPU — krachtig maar inert | Het ruwe LLM | De individuele docent + lesinhoud |
| RAM — snel maar beperkt | Het context window | Wat een lesgroep binnen één lesweek aankan |
| Disk | Externe databases | Toetsbank, leerlingdossier, alumni-data |
| Device drivers | Tool integrations | LMS, peer-review-software, plagiaatdetectie |
| **Besturingssysteem** | **De harness** | **Het kwaliteitssysteem zelf** |

Een CPU produceert niets bruikbaars zonder een besturingssysteem dat plant wat hij ziet, wanneer en met welke geheugenstaat. Goede docenten en goede lesinhoud produceren zonder een kwaliteits-harness eromheen een onverbonden reeks individuele ervaringen — geen accumulerende opleidingskwaliteit.

Vivek Trivedy (LangChain, maart 2026) drukt het korter uit: **Agent = Model + Harness**, vertaling *Opleidingsuitkomst = Lesinhoud (model) + Kwaliteitssysteem (harness)*. En zijn corollarium: *"if you're not the model, you're the harness."* Voor de management-taakverdeling: wie geen les geeft, is de harness aan het bouwen — of zou dat moeten zijn.

#### 1.2 *Model rented, harness owned* — een investeringsfilosofie

Wat *roteert* in een opleiding? Lesinhoud (die meebeweegt met het vakgebied), individuele vakken (per cyclus herzien), individuele toetsen (jaarlijks bijgesteld). Allemaal model-laag — administratief vernieuwbaar, niet vanzelf compounderend. Docenten zijn de tussencategorie waarin de analogie het zwakst is; die zwakte wordt apart behandeld in 1.7.

Wat *bezit* je dan? De architectuur die intake → toetsing → feedback → cohortmonitoring → jaar-op-jaar bijstelling samenhangend laat draaien. Dat is de harness, en zij compoundeert in waarde door gebruik.

Het empirische ankerpunt staat in `wiki/concepts/agent-harness.md` (Lee e.a. *Meta-Harness*, maart 2026): een harness die op één model is geoptimaliseerd, verbeterde vijf andere modellen zonder hertraining (+4,7 punten gemiddeld op math reasoning). Vertaald naar onderwijs: een kwaliteitssysteem dat goed werkt voor cohort A behoedt de opleiding wanneer lesinhoud, vakken of toetsen veranderen — *mits de institutionele intelligentie als systematisch geheel is gestold in de harness en niet uitsluitend in de hoofden van individuele docenten.*

Implicatie voor budget. Een opleiding die jaarlijks 80 % van haar institutionele aandacht aan model-laag besteedt (betere docenten zoeken, nieuwe vakken ontwerpen) en 20 % aan harness-laag, vertoont dezelfde failure mode die AI-organisaties nu leren ontwijken. Geen verkeerde investering — een verkeerde *verhouding*. De model-laag is zichtbaar; de harness-laag compoundeert.

#### 1.3 De vier lagen, vertaald naar HBO Bedrijfskunde

Chatterjee's vier-laagsmodel (`wiki/concepts/agent-harness.md`) leent zich voor een directe vertaling. Per laag een concrete onderwijs-invulling plus een test-vraag die het management voor zichzelf kan beantwoorden.

**Context-laag — wat de student, docent of lesgroep meebrengt.**
- LLM-vergelijking: het *system prompt* per cohort (intake-data, vooropleiding, leerstijl-meting, beroepscontext, leerdoelen, eerdere ervaringen) plus de *running context* (waar staan we in het curriculum, individuele leervoortgang, peer-feedback-geschiedenis).
- Onderwijs-invulling: een one-pager per cohort die op donderdagochtend, vóór de les, voor elke docent beschikbaar is — *"dit is wat dit cohort kan, hier zaten ze vorige week vast, dit zijn de gevoelige individuele situaties."*
- **Test:** kan een docent die one-pager nu opvragen? Zo nee, dan ontbreekt de Context-laag in operationele vorm.

**Constraints-laag — pre- en post-checkpoints rond elke onderwijsstap.**
- LLM-vergelijking: middleware vóór en na elke tool call die intentie valideert, scope bewaakt, output scoort.
- Onderwijs-invulling: pre-hook *vóór* een toets — een statistische slaagkans-voorspelling op basis van historische cohorten en toetsstructuur. Post-hook *na* elke toets — niet alleen pass/fail per student, maar geaggregeerde itemanalyse plus een automatische evaluatie-trigger naar de onderwijsinterventie zodra een drempel over- of onderschreden wordt.
- **De 90 %-slagingspercentage als verloren intent-validatie:** een pre-hook had moeten waarschuwen dat een verwachte slaagkans > 80 % expliciete kwaliteitscriteria én een go/no-go-besluit uitlokt voordat de toets wordt afgenomen. Dat ontbrak.
- **Test:** is er per kwartaal een 'kwaliteitsbord' dat zichtbaar maakt welke checkpoints draaien, welke triggeren en welke worden genegeerd? Zo nee, dan zijn er geen Constraints — er zijn alleen procedures.

**Contracts-laag — wat is "geslaagd" eigenlijk?**
- LLM-vergelijking: een formele, evalueerbare specificatie van *wat goede output is voor deze taak*, geformuleerd als functie van de input — geen checklist.
- Onderwijs-invulling: Dublin-descriptoren en het HBO-kwalificatieraamwerk leveren standaardcontracten op het bovenste niveau. De Contracts-laag in concrete vorm is de programma-specifieke operationalisatie: wat onderscheidt een 6 van een 8 in *dit* beroepsproduct, gegeven *deze* leerfase?
- **Test:** kan elke kerncompetentie in één paragraaf worden vastgelegd als *"dit zijn de zes signalen die we erin verwachten, dit zijn de drie failure modes, dit onderscheidt een 6 van een 8"*? Zo nee, dan is de competentie een aspiratie, geen Contract.

**Compounding-laag — telemetrie die de harness zelf verbetert.**
- LLM-vergelijking: gestructureerde records per uitvoering die een nachtelijke leerlus voeden welke harness-aanpassingen voorstelt; mensen reviewen, goedgekeurde aanpassingen worden workspace-overrides.
- Onderwijs-invulling: per cohort, per les, per toets emitteren *structured records* — hoe scoorde het cohort, waar zaten de uitschieters, wat correleerde met later succes (alumni-data), wat met later uitval. Geen logging, maar *trainingsdata voor het kwaliteitssysteem zelf*.
- De jaarlijkse meta-reflectie vraagt dan niet *"hoe gaat het met de opleiding?"* maar *"welke checkpoints van vorig jaar hadden moeten waarschuwen, welke regels uit de Contracts-laag moeten worden verfijnd?"*
- **Test:** zijn er minstens drie expliciete compound-loops gedefinieerd — bijvoorbeeld alumni-uitstroom → curriculum-update, toetsincidenten → assessment-design-update, docent-feedback → context-laag-update — met een datum waarop de update wordt verwerkt? Zo nee, dan vergeet de opleiding wat ze leert.

#### 1.4 Harnessen krimpen niet, ze verschuiven

Een waarschuwing tegen de neiging om kwaliteit te zien als een stapel regels die altijd groeit. Bron: `wiki/concepts/agent-harness.md` (Anthropic via Osmani, mei 2026): *"every component in a harness encodes an assumption about what the model can't do on its own."*

Vertaling: elke check, elke regel, elke procedure in het kwaliteitssysteem codeert een aanname over wat docenten of studenten *niet alleen* aankunnen. Wanneer omstandigheden veranderen — nieuwe AI-tools in handen van studenten, betere intake-data, beter onderbouwde inzichten in leerstijl — vervalt de noodzaak van bepaalde regels terwijl elders nieuwe behoeften ontstaan. De totale harness-omvang verandert nauwelijks; haar *vorm* schuift mee. Dit sluit aan op Principe 3 (ratchet) en het *subtraction principle*: het kwaliteitssysteem moet snoei toelaten, niet alleen aangroei. Een kwaliteitssysteem dat alleen maar dikker wordt, codeert geen nieuwe situaties — het codeert oude angsten.

#### 1.5 Werken vanuit gedrag (working-backward-from-behavior)

Bron: `wiki/concepts/agent-harness.md` (Trivedy via Osmani): *"behavior we want (or want to fix) → harness design to help the model achieve this"*, en de operationele test: *"if you can't name the behavior a component exists to deliver, it probably shouldn't be there."*

Voor elk procedure-document in het kwaliteitssysteem — toetsbeleid, herkansingsregels, deeltijd-curriculum-richtlijnen, evaluatieformulieren, OER-paragrafen — is de testvraag: kan je in één zin benoemen welk specifiek gedrag het beoogt te bewerkstelligen of te voorkomen, en welk incident of welke geobserveerde failure die regel rechtvaardigt? Zo nee, dan is het document een brainstorm-artefact, geen ratchet-artefact (zie Principe 3). Deze test is goedkoper dan een audit en harder dan een tevredenheidsonderzoek: een snelle inventarisatie *"wat doet dit document, en welke gebeurtenis bracht het tot stand?"* maakt zichtbaar welke delen van het kwaliteitssysteem geërfd zijn zonder dat iemand nog weet waarom.

#### 1.6 Twee disciplines, één machinerie

Bron: `wiki/concepts/micro-productivity-trap.md` sectie 4-5, met een directe convergentietabel. Kiron-Schrage 2026 (MIT Sloan Management Review) beschrijft op *organisationeel* niveau een flywheel — **verificatie → evaluatie → leerregistratie** — als de machinerie die organisaties laat compounderen op AI-interacties. Chatterjee 2026 (Medium) beschrijft op *runtime-engineering*-niveau de Constraints-, Contracts- en Compounding-lagen. De twee zijn operationeel identiek: dezelfde architectuur, op twee verschillende lagen, onafhankelijk gevonden door twee verschillende vakgemeenschappen.

Voor een onderwijsbestuurder: de analogie is geen modeterm uit één veld, maar een *transformation primitive* die boven AI-context uitstijgt en in organisatie-onderzoek even legitiem is. Investeren in een kwaliteits-harness is geen IT-keuze; het is een organisatorische investering die toevallig in AI-engineering haar scherpste vocabulaire heeft gevonden.

#### 1.7 Waar de analogie breekt: docenten leren, modellen niet

De *model-rented / harness-owned*-framing komt uit AI-engineering, waar het model letterlijk bevroren is na training. `wiki/concepts/agent-harness.md` (Chatterjee 2026) is hier expliciet: *"the model is frozen; you cannot fine-tune Claude in production. They mean the infrastructure around the model is learning, and the surface area where learning lives is the harness."* In die context is alle compounding-capaciteit per definitie in de harness gelokaliseerd, juist omdat het model zichzelf niet kan verbeteren. In onderwijs breekt die scheidslijn op twee punten — en beide breuken zijn informatief voor het ontwerp van het kwaliteitssysteem.

**Breuk 1 — Constraint: arbeidsrelaties zijn geen commodity-rotatie.** Een AI-organisatie kan vandaag van GPT-5 naar Claude Opus 4.7 wisselen zonder ontslagvergoeding, OR-traject of cohort-disruptie. Een opleiding kan dat niet. Arbeidsrechtelijke en relationele continuïteit (cao, vaste aanstellingen, OR-instemming, vertrouwen tussen collega's, studentbinding aan vertrouwde gezichten) begrenzen *waar en hoe snel* de model-laag verschuift. De transferability-claim uit Lee e.a. — een harness draagt over vijf modellen heen zonder hertraining — wordt daarom in onderwijs op een andere manier waardevol: niet omdat de model-wissel kosteloos is (dat is zij beslist niet), maar omdat een harness die robuust is tegen rotatie de opleiding *behoedt* voor de schokken van zo'n rotatie wanneer zij toch onvermijdelijk wordt.

**Breuk 2 — Potentie: docenten zijn niet bevroren.** Hier ligt het belangrijkste verschil tussen onderwijs en AI-engineering, en het verschil loopt in het voordeel van onderwijs. Anders dan een LLM kan een docent zich ontwikkelen — via professionalisering, peer-feedback, vakdidactisch onderzoek, cohort-evaluaties, leerlijnreflectie. Dat is een *tweede compounderende laag* waar AI-engineering simpelweg niet over beschikt. Een opleiding die haar docenten expliciet onderdeel maakt van de Compounding-laag (zie 1.3) — docent-leertrajecten gevoed door dezelfde telemetrie die het curriculum voedt — heeft een asymmetrisch voordeel ten opzichte van de bron-analogie.

De juiste herformulering van de investeringsfilosofie uit 1.2: *investeer in de harness omdat zij compoundeert, **en** investeer in docent-ontwikkeling omdat zij — anders dan in AI — óók compoundeert.* De twee investeringen zijn complementair, geen substituten. Een opleiding die op docent-ontwikkeling bezuinigt onder het motto *"de intelligentie zit in de harness"* maakt een keuze die AI-engineering niet hoeft te maken, omdat zij die keuze niet *kán* maken — daar is het model bevroren, hier niet. Het kwaliteitssysteem moet beide compounding-bronnen orchestreren, niet kiezen tussen de twee.

#### Operationele implicaties

- **Investeer disproportioneel in de harness-laag**, juist omdat zij minder zichtbaar is dan investeringen in lesinhoud, nieuwe vakken of nieuwe toetsen. Disproportioneel is hier een herverdeling ten opzichte van die model-laag-categorieën, niet ten opzichte van docent-ontwikkeling.
- **Behandel docent-ontwikkeling als tweede compounding-bron** (zie 1.7), niet als model-laag-investering: plan professionalisering, peer-feedback en vakdidactisch onderzoek als integraal onderdeel van de Compounding-cyclus, gevoed door dezelfde telemetrie die het curriculum voedt.
- **Maak elke regel in het kwaliteitssysteem herleidbaar tot een gewenst gedrag plus een datum of incident.** Een jaarlijkse opschoning op deze test verwijdert meer dood gewicht dan een volledige herziening.
- **Bouw vanaf dag één een compounding-cyclus in.** Gestructureerde telemetrie plus een jaarlijkse meta-reflectie-vraag (*"welke checkpoints hadden moeten waarschuwen?"*) zijn goedkoper dan een audit-rapport en informatiever dan een tevredenheidsonderzoek.
- **Waarschuwing tegen verwarring.** De Examencommissie is *één checkpoint*, niet de harness. De Onderwijs- en Examenregeling (OER) is *één Contract*, niet de Contracts-laag. De harness is de bredere architectuur waarbinnen deze instrumenten op elkaar aansluiten — en haar afwezigheid is precies waarom afzonderlijk goed werkende instrumenten kunnen samenkomen in een opleiding die het toch niet rond krijgt.

### Principe 2 — Verificatie ≠ evaluatie. Vraag: *"wat ging interessant fout?"*

Kiron-Schrage 2026 (`wiki/concepts/micro-productivity-trap.md`): de meeste organisaties beoefenen *"verificatie vermomd als evaluatie"* — ze behandelen output als oordeel dat moet worden bevestigd, niet als startpunt dat moet worden bevraagd. *Consumptie verkleed als adoptie.*

Drie stappen, op het niveau van de **onderwijsinterventie** (een module, een vak, een toetsvorm, een herontwerp), bevraagd via de **cohortuitkomsten** die zij produceert:

- **Verificatie** — *"hebben we met deze onderwijsinterventie de gewenste uitkomst bereikt?"* — binaire check tegen bestaande criteria, gemeten via aggregaten van cohortuitkomsten.
- **Evaluatie** — *"wat onthullen deze cohortuitkomsten over het ontwerp van de onderwijsinterventie?"* — *kan nieuwe ontwerpkeuzes voortbrengen.* Vereist domeinexpertise.
- **Leerregistratie** — *"hoe leggen we dat inzicht vast in het kwaliteitsraamwerk zodat cohort N+1 het oogst?"* — versiebeheer voor onderwijskundige oordelen op interventieniveau.

De dragende vraag is Kiron-Schrage's derde: ***"Wat was *interessant* fout?"***

**Operationele implicatie.** Geen toetsanalysesysteem kan zonder een evaluatielaag boven de verificatielaag. Wat *interessant fout* ging in cohort N moet zich laten codificeren en cohort N+1 voeden. Zonder die registratiestap is elke evaluatie een eenmalige gebeurtenis.

### Principe 3 — Ratchet, niet brainstorm

`wiki/concepts/agent-harness.md` (Osmani, mei 2026, naar Trivedy): ***"Elke fout wordt een regel. Je voegt alleen constraints toe als je een echte failure hebt gezien. Je verwijdert ze als een capabel model ze redundant heeft gemaakt. Elke regel in een goede AGENTS.md moet herleidbaar zijn naar iets dat fout ging — ratchet, niet brainstorm."***

Dit is *geen* bureaucratie. Bureaucratie groeit door regels die vooraf zijn bedacht; de ratchet groeit door regels na een geobserveerde failure, in scope beperkt tot die failure, en met verwijdering zodra het probleem opgelost is (het *subtraction principle*: ***"volwassen harness-werk lijkt minder op opbouw, meer op snoei"***).

#### 3.1 De software-engineering-parallel: ratchet als git-discipline

De ratchet-discipline is geen onderwijsuitvinding. Software-engineering werkt al decennia volgens exact dit patroon en heeft er een infrastructuur omheen gebouwd waarvan de operationele blauwdruk vrijwel direct overdraagbaar is. Een professioneel ontwikkelteam voegt geen regel code toe zonder een spoor terug naar een gebeurtenis: een **issue** (datum, melder, reproductie) wordt opgepakt via een **commit** met een herkenbare boodschap (*"fix(auth): reject empty tokens — closes #423"*); de commit gaat als **pull request** door een reviewlaag van collega's plus automatische tests; bij elke bug-fix wordt expliciet een **regressietest** toegevoegd die *die specifieke failure* voor altijd vastlegt; pas dan volgt de **merge** naar de hoofdtak. Na merge toont `git blame` voor elke regel code de bijbehorende commit, datum, auteur en rationale. Een regel verwijderen (**revert**, **refactor**, **dead-code-removal**) is een gelijkwaardige operatie zonder sociale kosten — de historie bewaart het waarom voor zover dat ooit relevant blijkt.

De vertaling naar de kwaliteits-harness is één-op-één:

| Software-praktijk | Kwaliteits-harness-praktijk |
|---|---|
| **Issue** (datum, melder, reproductie) | **Incident** in een cohort, vak of beoordelingsmoment, met datum en omstandigheden |
| **YAGNI** — geen speculatieve code | Geen procedure-documenten omdat ze *zouden kunnen* helpen |
| **Commit-message** *"fix(X): Y — closes incident-N"* | Nieuwe regel met expliciete verwijzing naar incident-datum en -beschrijving |
| **Pull request** + code review | Examen- of curriculumcommissie als reviewer-laag — niet als bron van regels |
| **Regressietest** | Telemetrie-checkpoint dat de specifieke failure-conditie in volgende cohorten meet |
| **`git blame`** | Gedateerd register dat per regel toont welk incident hem introduceerde, welke commissie, welke versie |
| **Revert / refactor** | Het *subtraction principle*: een regel verwijderen zodra het probleem op een andere manier is opgelost |
| **Postmortem** | Kiron-Schrage's *"wat was interessant fout?"*, gevolgd door *"welke checkpoints hadden moeten waarschuwen?"* (Principe 2) |

**Het ene mechanisme dat het verschil maakt.** Software-engineering steunt op één afdwingbaar contract: alles wat in `main` staat is herleidbaar tot zijn introductie. Niet vrijwillig, niet aspirationeel — *technisch afgedwongen*. Git registreert het automatisch. De kwaliteits-harness mist in vrijwel elke onderwijsinstelling die afdwinging: een handboek, een OER-paragraaf of een toetsbeleid bestaat *nu*, maar zelden bestaat het gedateerde register dat voor elke regel zegt *"deze regel is op 14 maart 2023 toegevoegd door commissie X, naar aanleiding van incident Y, met als beoogde gedragsverandering W."* Zonder dat register is opschoning onmogelijk — niemand durft een regel weg te halen waarvan niemand meer weet waarom hij ooit nodig was. Het systeem stapelt regels op; het kan alleen omhoog, nooit omlaag. Dit is exact wat 1.5 (*working-backward-from-behavior*) test, en wat het *subtraction principle* uit 1.4 vereist.

**Waar de analogie eindigt.** Twee plekken waar de mapping niet schoon doorloopt. *Eerste:* een softwarebug is meestal binair (de test slaagt of niet); een onderwijs-failure is een interpretatief oordeel dat domeinexpertise vraagt. Dat is precies waarom Principe 2's onderscheid tussen verificatie en evaluatie zo zwaar weegt — de ratchet werkt nog steeds, maar elke schakel (*"dit was een failure"*, *"dit is een passende regel"*, *"deze regel is nu redundant"*) is een evaluatieve, geen verificatieve stap. *Tweede:* code verwijderen heeft geen sociale kosten; een commissie is wél eigenaar van een procedure. Het *subtraction principle* botst daarom harder op organisatie-politiek dan op een refactor-pull-request, wat pleit voor een verplicht **jaarlijks snoeiritueel** waarin elke regel tegen zijn incident-registratie wordt gehouden — niet als optie, maar als cyclus die anders niet vanzelf gebeurt.

**Operationele implicatie.** Start de kwaliteits-harness *klein*. Voeg constraints toe wanneer een specifieke failure is geobserveerd. Verwijder constraints zodra ze redundant zijn geworden. Elke constraint moet herleidbaar zijn tot een datum en een incident — concreet: een **gedateerd regel-register** (de organisatorische tegenhanger van `git blame`) plus een **jaarlijks snoeiritueel** waarin regels zonder actueel rechtvaardigend incident worden ingetrokken.

### Principe 4 — Maatwerk in interaction design, geen uniforme uitrol

Krakowski e.a. 2025 (peer-reviewed Management Science, `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md`) — sterkste empirische ankerpunt: een *untailored* uitrol van AI veroorzaakt *geleidelijke prestatiedaling* ten opzichte van de legacy-IT-controlegroep. Een *tailored* uitrol (afgestemd op cognitieve stijl volgens Kirton 1976 — adaptor versus innovator) levert positieve effecten ten opzichte van beide.

Vier interactieparameters worden gevarieerd:

1. **Werkprocedure** (opgelegd versus flexibel) — *de meest kritieke parameter.*
2. **Beslissingsbevoegdheid** (beperkt versus hoog).
3. **Training** (verplicht versus op aanvraag).
4. **Prikkels** (extrinsiek versus intrinsiek).

**Operationele implicatie.** Een uniform kwaliteitssysteem dat aan alle docenten en alle studentengroepen dezelfde procedures, bevoegdheidsgrenzen, training en prikkels oplegt, levert volgens Krakowski slechtere uitkomsten op dan géén systeem. Het systeem moet *gevarieerd* zijn op deze vier assen, afgestemd op de cognitieve stijl van docenten *én* studenten. Dit conflicteert met het bureaucratische instinct om uniformiteit te eisen omwille van *fairness*.

### Principe 5 — Momentum slaat perfectie. Lever op in maanden, niet in jaren.

`wiki/concepts/enterprise-ai-adoption.md` (via Brooklyn Solutions / Allen, AWS, mei 2026): een engagement met een gereguleerde klant (Danske Bank, MoD) leverde **5× output bij ≤ 25 % opex-toename** op, onder de operationele leus *"momentum beats perfection."* Convergent met `wiki/concepts/strategy.md` (Roger Martin): *"strategie is een reis — een mechanisme om te tweaken, te verfijnen, te verbeteren naarmate je voortgaat."*

**Operationele implicatie.** Een v1 die in zes maanden live gaat en op basis van geobserveerde failures ratchet, levert in drie jaar betere kwaliteit op dan een perfect systeem dat na drie jaar live gaat. De PRD moet expliciet de v1-scope kleiner houden dan een volledig kwaliteitsmodel, met een ratchet-cyclus voor de uitbreiding naar v2 en v3.

---

## 3. Transformatie-sequentie

Zeven stappen, in volgorde, gebaseerd op het turnaround-playbook van Rolls-Royce onder Tufan Erginbilgić (door McKinsey betiteld als *"a case study in the art of corporate transformation"*). Bron: `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md`.

### Stap 1 — Externe diagnose vóór de officiële start

Erginbilgić gaf opdracht voor externe benchmarking *vanaf september '22, vier maanden vóór zijn aanvangsdatum*. Citaat: *"Je kunt deze dingen niet zeggen zonder data, want anders klinkt het alsof je hen alleen maar bekritiseert. Met data demonstreerde ik waar het bedrijf staat."*

**Voor HBO Bedrijfskunde:** het diagnose-substraat moet bestaan uit data die het management *niet zelf heeft geschreven*:

- Vergelijkende verdelingen van slagingspercentages over peer-HBO-opleidingen.
- Werkgeversenquêtes onder alumni (eerste drie jaar na afstuderen).
- Externe accreditatiebevindingen (NVAO).
- Een onafhankelijke peer review van de toetsmoeilijkheid (bijvoorbeeld anonieme beoordeling door externe docenten).

Het slagingspercentage van 90 % is *één* zo'n datapunt; het heeft drie tot vier naburige datapunten nodig voordat het *burning platform*-gesprek eerlijk gevoerd kan worden.

### Stap 2 — Burning-platform-speech: diagnose plus visie in één artefact

De town-hall van Erginbilgić in januari 2023 duurde anderhalf uur en koppelde de diagnose (*"elke investering die we doen, vernietigt waarde"*) aan de visie binnen dezelfde toespraak. Wiki-citaat: *"Burning-platform zonder visie is paniek; visie zonder burning-platform is wishful thinking; samen is dat transformatie."*

Tweede voorwaarde: *"aandeelhouders waren al gefrustreerd"* — de speech was *publicatie* van een al gedeelde kritiek, geen unilaterale aanval. **Voor HBO Bedrijfskunde:** stem het CvB en het managementteam af *vóór* de town-hall met docenten en studenten. De town-hall zelf bevestigt een al gevormde consensus, niet de eerste keer dat iemand iets hoort.

*Wiki-honesty.* De specifieke burning-platform-methodologie van Erginbilgić — extern gecommissioneerde benchmarking vóór dag één, plus diagnose en visie gekoppeld in één artefact — rust binnen de huidige wiki op één primaire bron. Kandidaten die op keyword-niveau verwant lijken (Ries over *force-that-destroys-from-within*, Ross-Schneider over adaptability, Sternfels over consulting-transformatie) bleken bij lezing geen substantieel mechanisme-overlap te hebben. Dit is een legitiem wiki-singleton; toekomstige ingest van Kotter's *Leading Change* (HBR 1995 / boek 1996) of vergelijkbare change-narrative-literatuur zou de leuning verstevigen.

### Stap 3 — Restructuring ≠ transformation: een bewuste semantische distinctie

Erginbilgić *"staat erop"* dat de term *transformation* gebruikt wordt, niet *restructuring*. Reden: in het decennium daarvoor waren er meerdere *restructurings* die geen stand hielden. Een nieuwe term met een verdedigbaar andere change theory is geen marketing — het is een signaal dat de aanpak structureel anders is.

**Voor HBO Bedrijfskunde:** als eerdere kwaliteitsinterventies *kwaliteitsverbetering* of *herstructurering* heetten en niet beklijfden, voer de nieuwe interventie dan onder een nieuwe naam *én* een verdedigbaar andere change theory. Niet de oude theorie in nieuwe verpakking.

Convergent met Dutt en Chatterji 2026 (Bain/OpenAI, [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]]): organisaties die in het *experimentation*-stadium blijven hangen — incrementele initiatieven onder een transformation-label — leveren minder dan 40 % meetbare gains; alleen *wholesale* transformatie (organization-wide, outcome-oriented) levert de 10 tot 25 % EBITDA-verbetering op die Bain bij zijn klanten meet. Dezelfde change-theory-distinctie, andere woordenschat — twee bronnen die de single-source-leuning verlichten.

### Stap 4 — Strategie als participatie, niet als document

Bronnen: [[strategy|concepts/strategy]] (aggregeert Martin, Oberholzer-Gee en Erginbilgić in één concept-pagina) plus `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md`. De doctrine van Erginbilgić:

> *"Ik doe geen strategie in een dark room met consultants. Ik bezocht persoonlijk 25 tot 30 workshops toen we strategieën ontwikkelden... ongeveer 500-plus medewerkers deden mee. Wanneer je klaar bent, is de hele organisatie aligned omdat ze in de kamer waren toen je de beslissing nam."*

Twee protocolregels per workshop:

- ***"Geen hiërarchie in de kamer"*** — zodat junior stemmen senior aannames mogen uitdagen tijdens vorming.
- ***"Dit wordt chaotisch"*** — expliciet toegestane divergentie: *"veel strategische gesprekken openen niet, ze sluiten. Je moet het openen zodat alle onverwachte ideeën in de kamer komen, ook als je ze niet uitvoert: ze zijn in de kamer geweest."*

**Granulariteit als validatiecriterium** (de tweede pijler): *"een strategie is granulair als iedereen in het bedrijf zijn rol in de strategie-uitvoering kent. Heb je geen granulaire strategie, dan weten alleen tien mensen ervan en zijn diezelfde tien mensen verrast als de strategie niet wordt uitgevoerd."*

**Voor HBO Bedrijfskunde:** de absolute aantallen uit Erginbilgić's quote (25 tot 30 workshops, 500-plus medewerkers) gelden voor een aerospace-concern van ~50.000 medewerkers; voor een opleiding met ongeveer veertig docenten plus de ondersteunende collega's rondom haar schaalt dit terug naar enkele workshops met de volledige docentenstaf en de relevante ondersteuners. Het *aantal* doet er minder toe dan het *principe*: als de docenten en de ondersteunende staf rond de opleiding niet *in de kamer* zijn wanneer de kwaliteitsstrategie wordt gevormd, levert de uitrol dezelfde failure mode op als de mislukte curriculum-innovatie. *Alignment is de uitkomst van participatie, niet van communicatie.* Convergent met Carucci (`wiki/sources/2026-05-07-carucci-resistance-as-data.md`): *"faux-inclusie — input vragen nadat de belangrijke beslissingen al zijn genomen. Mensen leren dat hun stem er niet toe doet en bieden hem niet meer aan."*

*Wiki-honesty.* De open-strategy-doctrine zelf (25 tot 30 workshops, 500-plus medewerkers, het *no-hierarchy-in-the-room*-protocol, granulariteit als alignment-uitkomst) rust binnen de wiki op één primaire bron — Erginbilgić. De concept-pagina [[strategy|concepts/strategy]] markeert dit zelf als structureel gat: *"de dichtstbijzijnde wiki-buur op deze doctrine is nog niet aanwezig — er is geen concept-pagina voor open strategy of strategy-as-conversation."* Whittington's *Opening Strategy* (Oxford 2019) of vergelijkbare empirische open-strategy-literatuur zou de leuning verstevigen (zie ook §8 open vragen).

### Stap 5 — Vier pijlers

Erginbilgić noemt er expliciet twee; de wiki reconstrueert de andere twee uit context (`wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md`):

1. **Mensen** — *"leiderschap, visie, engagement."* Convergent met Allen 2026 (AWS, [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]]): het *hourglass-organization*-model als operationele invulling — bescherming van het junior-leerpad als onmisbaar onderdeel van de people-pijler in een agentic-AI-context.
2. **Granulaire strategie** — zie stap 4.
3. **Commerciële discipline** (gereconstrueerd) — bij Rolls-Royce: heronderhandeling van contracten. Bij HBO Bedrijfskunde: *waardecreatie-discipline*. `wiki/concepts/strategy.md` citeert Oberholzer-Gee 2022: *"waardecreatie gaat aan waarde-vangst vooraf."* Operationeel: verlaag de *willingness to serve* van de staf niet met *meer geld* (*"waarde is geredistribueerd, niet gecreëerd"*), maar door *de baan beter te maken* — opleiding, royale promotieregels, thuiswerk, interessanter werk. **Dit pakt het moraal- en verzuimprobleem aan bij het mechanisme, niet bij het symptoom.**
4. **Performance culture en 360-management** — *"360-performancemanagement. Altijd. Wil je de cirkel sluiten, dan eindigt het met beloning en erkenning, en daarna laat je het bedrijf groeien, want dat schept allerlei carrièrekansen. Krimpende bedrijven hebben minder kansen om te groeien."* En de talentbelofte: *"Je wilt mensen in je organisatie die in trek zijn op de arbeidsmarkt, maar bij je willen blijven. Dat is de geheime saus."* Convergent met Storoni 2026 (HBR IdeaCast, [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai]]): in het AI-tijdperk is kwaliteit de menselijke bijdrage — *"humans now influence productivity by the quality of their output."* Storoni's neuroscience-mechanisme (gear-3 reactive-work onderdrukt prefrontale-cortex-betrokkenheid, *"the equivalent to a mental sprinting"*) onderbouwt waarom getolereerde middelmatigheid niet alleen het werk maar ook de goede werknemers schaadt — de organisatie zit collectief vast in een werkmodus waarin waardevolle cognitie onmogelijk is.

### Stap 6 — Elimineer lagen, niet operationele mensen

Erginbilgić: *"We elimineerden lagen in de organisatie. Als je kijkt naar wat we hebben gedaan, zijn er geen operationele mensen vertrokken."* De morele basis: *"als we het niet doen, worden waarschijnlijk 50.000 levens beïnvloed, want het bedrijf gaat naar slechte plekken."* *Risk-of-keeping > pain-of-cutting.*

Convergent met Allen 2026 (AWS, [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]]): het *hourglass-organization*-model — elimineer managementlagen, bescherm het junior-leerpad. Allen's empirische anker: 73 % entry-hiring collapse (Ravio, Europese tech), terwijl seniorgroei 9 % bedraagt en nieuwe afgestudeerden slechts 7 % vormen; Jeff Bezos elimineerde L9 bij Amazon onder hetzelfde principe. Convergent met Yee et al. 2025 (MGI, [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships]], Exhibit 20): leiderschapsvaardigheden zoals coaching en mentorship zijn *low-SCI-exposure* en blijven menselijk, terwijl prioritization en decision-making — precies het managementlaag-werk — *high-SCI-exposure* zijn. Drie bronnen, drie industrieën (aerospace, cloud, ~800 BLS-occupaties), dezelfde structurele claim: layer-eliminate ≠ people-eliminate.

**Voor HBO Bedrijfskunde:** is er een laag van administratieve of coördinerende functies die werk absorbeert zonder waarde aan student of staf te leveren? De wiki noemt geen onderwijsspecifieke lagen, maar het *principe* — lagen elimineren, operationele capaciteit beschermen — is overdraagbaar. Dit moet via de medezeggenschapsraad of ondernemingsraad — een proces dat de wiki niet behandelt.

### Stap 7 — Bouw veerkracht als procescapaciteit, niet als voorspelling

Het veerkracht-playbook van Erginbilgić (vier ingrediënten, in volgorde):

1. **Mindset** — *"belangrijker dan al het andere."*
2. **Reactievermogen** — *"je moet dat ontwikkelen vóór je in de problemen zit, want het kost tijd."*
3. **Agility** — *"je moet die capaciteit behendig kunnen inzetten."*
4. **Actie-oriëntatie** — *"actie-georiënteerd, niet uitleg-georiënteerd."*

De diskwalificatie: ***"Het gaat niet om het voorspellen van de wereld, het gaat erom hoe jouw bedrijf nu denkt over het omgaan met externe schokken."***

Dit conflicteert expliciet met de foresight-traditie zoals beschreven door Webb 2024 ([[2026-04-28-webb-strategic-foresight]]): *"a scenario is a form of prediction — a deeply researched preview of how the world might unfold."* Twee strategische tradities staan hier op een kernkwestie tegenover elkaar — proces-capability versus scenario-as-prediction. Voor de PRD blijft Erginbilgić de leuning: process-capability ontwikkelen is operationeel haalbaar voor een opleiding, terwijl een volwaardige foresight-methodologie buiten de huidige institutionele capaciteit ligt. Maar de spanning is reëel en verdient erkenning.

**Voor HBO Bedrijfskunde:** bouw de *gewoonte* van het omgaan met schokken (curriculumveranderingen, accreditatiebevindingen, marktvraag-verschuivingen, AI-disruptie), niet de *voorspelling* van welke schok komt. Numerieke claim van Erginbilgić, ongeveer drie jaar na zijn aantreden bij Rolls-Royce in januari 2023: *"We reageren nu op actuele schokken. Drie jaar geleden konden we nog niet de helft van wat we nu doen — waarschijnlijk maar 10 %."* Dat wil zeggen: wat in 2023 hun volledige capaciteit was, is nu nog maar 10 tot 50 % van wat zij in 2026 leveren — een capability-multiplier van ongeveer 5 tot 10× in drie jaar.

---

## 4. Succesindicatoren — wat het management moet zien

Drie categorieën, elk met meerdere signalen die in de wiki zijn geattesteerd. Een toezichthouder die deze signalen kan lezen, weet of de transformatie werkt — *los van de KPI's*.

### (a) Signalen dat de transformatie goed wordt gehoord

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 1 | Weerstand verschijnt, in een van vier categorieën: **Verlies / Angst / Gebrek aan controle / Gebreken in de verandering** | Carucci 2026 | *Diagnostiseer*, onderdruk niet. *"Alle weerstand is betekenisvolle data."* |
| 2 | Junior medewerkers dagen senior aannames uit zonder gevolgen | Erginbilgić | Het protocol *"no hierarchy in the room"* werkt. |
| 3 | Docenten *kunnen articuleren wat hun rol is in de strategie-uitvoering* | Erginbilgić (granulariteit) | Een granulaire strategie is geland; een aspiratiedeck niet. |

### (b) Signalen dat de transformatie faalt in productie

Vier sub-clusters, MECE-geordend van architectuur via meetwaarde en staf naar externe stakeholders. De clusters dekken samen de hoofdcategorieën van productie-falen; binnen elk cluster zijn de signalen geënt op verschillende observatiekanalen zodat dezelfde root-cause via meerdere routes detecteerbaar blijft.

#### b1 — Architectuur-falen

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 4 | Pilot werkt, productie faalt | Friday-in-March pattern (`agent-harness`) + MIT NANDA: 95 % zero-return | Het systeem werkt in demo, maar de harness-laag eromheen ontbreekt. |

#### b2 — Meetwaarde-falen *(wat we meten verbergt wat we zien)*

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 5 | Hoge slagingspercentages bij studenten die het curriculum als te makkelijk ervaren — gerapporteerd via formele én informele kanalen | Storoni: kwaliteit boven kwantiteit + DORA, *amplifier and mirror* (`agent-harness`) | Kwantiteitsmeetwaarde in plaats van kwaliteitsmeetwaarde. Observeerbaar via **formele kanalen** (slaagcijfer + Nationale Studenten Enquête + tevredenheidsonderzoek) én **informele kanalen** (directe student-uiting in de klas, studentevaluatieformulieren). *Wat onder AI-blootstelling wordt versterkt: AI in handen van studenten legt de zwakte van de toets versneld bloot.* |

#### b3 — Staf-falen *(zichtbaar op drie observatieniveaus)*

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 6 | Geleidelijke prestatiedaling na een uniform uitgerolde interventie | Krakowski e.a., RCT | **Macro-uitkomst.** Untailored design — *erger dan geen interventie*. |
| 7 | Psychologische onveiligheid bij stafleden — als subjectief gevoel én als collectief vergadergedrag | Krakowski e.a., *prison quote* + Carucci 2026 | **Ervaring én groepsgedrag.** Stafleden ervaren rolconflict, ambiguïteit en motivatie-instorting (*"we kregen deze geweldige tool, en tegelijkertijd voelde ik me in de gevangenis"*). In vergaderingen vertaalt zich dat naar stilte: *"Mensen houden op met spreken — dat betekent niet dat ze aligned zijn, maar dat het niet langer veilig of nuttig is om je te vertellen wat ze echt denken."* De tegenpool van signaal 1: niet meer weerstand ≠ alignment; het betekent dat de feedback-kanalen gesloten zijn. |
| 8 | Stijgend ziekteverzuim onder de beste docenten | Erginbilgić: *"niet-compromisloze middelmatigheid... doodt organisaties en goede mensen"* + Storoni 2026 ([[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai]]) | **Individueel gedrag (observeerbaar in HR-cijfers).** Het systeem tolereert middelmatigheid die de goede mensen uitput. Storoni levert het mechanisme: gear-3 reactive-work design produceert middelmatige output die wel meetbaar 'productief' aanvoelt, en put goede werknemers systematisch uit. |

#### b4 — Externe stakeholder-signalen *(buiten ai-wiki-evidentie; toegevoegd op basis van algemeen onderwijsbestuurlijk kader — zie open vraag 8.3)*

De wiki bevat geen onderwijsspecifieke evidentie voor deze drie signalen. Ze zijn opgenomen omdat zij in een Nederlandse HBO-context dezelfde diagnostische functie vervullen als de interne signalen hierboven, en ze in een MECE-volledige tabel niet kunnen ontbreken. De brontype-aanduiding markeert hun status expliciet.

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 9 | NVAO-accreditatie-uitkomst onder de norm of opleiding in herstelfase | *(buiten ai-wiki-evidentie; Nederlands kwaliteitsregime)* | **Onafhankelijk extern oordeel.** Het Nederlandse kwaliteitsregime registreert de transformatie-uitkomst los van het management. Een voorwaardelijke of niet-positieve accreditatie is een laat maar onmiskenbaar signaal — als dit aan komt is intern bijsturen al duur. |
| 10 | Werkgevers en alumni melden afname van starterscompetenties bij recent afgestudeerden | *(buiten ai-wiki-evidentie; te triangleren via werkgeversenquête + alumni-onderzoek eerste drie jaar)* | **Post-graduation outcome-signaal.** Het externe beoordelingssubstraat dat het management *niet zelf heeft geschreven* (zie stap 1). Vertraagd (twee tot vier jaar na curriculumwijziging), maar de meest objectieve test van wat de opleiding feitelijk levert. |
| 11 | Praktijkbegeleiders melden inhoudelijke gaten in beroepsvaardigheden bij stagiairs | *(buiten ai-wiki-evidentie; te triangleren via stage-coördinator + werkveldcommissie)* | **Vroeg extern diagnostisch signaal.** Observeerbaar tijdens de opleiding, niet pas na afstuderen. Vult de stage-feedback-loop die in de Compounding-laag (1.3) als compound-loop moet aansluiten. |

### (c) Signalen dat het meetsysteem zelf misleidt

| # | Signaal | Bron | Interpretatie |
|---|---------|------|---------------|
| 12 | Individuele KPI's stijgen, maar collectieve uitkomsten verslechteren | DORA via `micro-productivity-trap`: *"verhoogde AI-adoptie kan leiden tot individuele productiviteits­voordelen, terwijl team-niveau-voordelen afnemen."* | Micro-macro-divergentie. De harness-laag ontbreekt of is verkeerd. |
| 13 | De meetwaarde voelt comfortabel | Roger Martin via `strategy`: *"Het is veel makkelijker om te zeggen 'ik bouw een fabriek' dan 'ik zorg dat klanten ons aanbod meer waarderen dan dat van concurrenten.'"* | Een meetwaarde die het management comfort geeft, is een *plan*-artefact, geen *strategie*-artefact. |
| 14 | Het management duwt niet hard genoeg | Erginbilgić: *"Ik ben veeleisend... ik wil dat je verbetert."* Maar **niet** tough love: *"veeleisend, met eerlijkheid en transparantie."* | Een management dat ongemakkelijke prestatiedata niet aan het licht brengt, levert structureel het patroon op van hoge slagingspercentages, lage kwaliteit en lage moraal. |

---

## 5. Risicoregister

Vijf risico's die de wiki specifiek benoemt, elk met een wiki-citaat als onderbouwing plus een mitigatie.

### Risico 1 — Untailored uitrol veroorzaakt *erger dan geen interventie*

**Bewijs.** Krakowski e.a. 2025 (peer-reviewed RCT): in de untailored conditie *daalt* het marktaandeel geleidelijk ten opzichte van de stabiele legacy-IT-baseline. Mechanisme: rolconflicten, ambiguïteit, motivatie-instorting. *"Felt like in prison."*

**Mitigatie.** Geen uniforme uitrol. Stem af op vier parameters (werkprocedure, beslissingsbevoegdheid, training, prikkels), met *werkprocedure* als meest kritieke. Begin met een gevarieerde rolpilot om interactiepatronen te leren *voordat* je institutionaliseert.

### Risico 2 — Friday-in-March: de pilot werkt, productie faalt

**Bewijs.** Chatterjee 2026 in `agent-harness`: een AI-agent verwijderde de werkruimte van een klant 40 minuten voor een board meeting omdat de harness geen intentie-validatielaag had. *"Het model was niet het probleem. Het probleem zat in de laag rondom het model."*

**Mitigatie.** Bouw constraints *vóór* slimheid. Voor elke kwaliteitscheck een pre-hook (*wat is de intentie?*) en een post-hook (*wat scoort dit op de kwaliteitscriteria?*). Geen curriculum-innovatie zonder uitvoerbare kwaliteitscheckpoint vóór livegang.

### Risico 3 — De kamer wordt stil

**Bewijs.** Carucci 2026: *"Hoe harder leiders pushen om weerstand te elimineren, hoe meer ze die versterken of ondergronds drijven. Mensen houden op met spreken, maar dat betekent niet dat ze aligned zijn — het betekent dat het niet langer veilig of nuttig is om je te vertellen wat ze echt denken."*

**Mitigatie.** Maak rapporteren van weerstand *makkelijker*, niet moeilijker. Anonieme kanalen, no-hierarchy-protocollen zoals dat van Erginbilgić: *"no hierarchy in the room."* Een kwaliteitssysteem zonder weerstand als invoer is een kwaliteitssysteem zonder feedback.

### Risico 4 — Antropomorfisering van AI

**Bewijs.** Kropp e.a. 2026, RCT (N=1.261, BCG/HBR): de framing *AI-as-employee* veroorzaakt een daling van 9 pp in accountability, 44 % meer escalatie-aanvragen en 18 % minder gedetecteerde fouten — zonder dat de adoptie-intentie significant stijgt. Bron: `wiki/concepts/automation-vs-augmentation.md`, sectie 13.

**Mitigatie.** Frame AI in de PRD en dagelijkse communicatie als een *tool die docenten en studenten gebruiken*, niet als *AI-tutor* of *AI-teaching-assistant* met employee-achtige agency. Accountability blijft expliciet en persoonlijk — *"decision rights, escalation triggers, consequences"* — niet diffuus gemaakt door antropomorfiserende taal.

### Risico 5 — Verificatie vermomd als evaluatie

**Bewijs.** Kiron-Schrage 2026: *"De meeste organisaties behandelen AI-outputs als oordelen die bevestigd moeten worden, niet als startpunten om te bevragen. Het resultaat is consumptie verkleed als adoptie — verificatie aangezien voor het hele werk."*

**Mitigatie.** Een evaluatielaag *boven* de verificatielaag (zie Principe 2). Vraag bij elke significante AI-interactie en bij elke significante curriculum-feedbackloop: *Wat werkte? Wat faalde? Wat was **interessant** fout?* Codificeer het derde antwoord — dáár neemt de waarde toe.

---

## 6. Wat er expliciet *niet* in mag

Antipatronen die de wiki specifiek identificeert als failure modes:

1. **AI antropomorfiseren** in beleid of communicatie. Geen *"AI-docent"* of *"AI-assistent"* met employee-framing. Wel: tools, ondersteuning, instrumenten.
2. **Pilot-purgatorium.** Allen / AWS, in `wiki/concepts/micro-productivity-trap.md`: *"pilots blijven gedemoed, nooit verbonden met daadwerkelijke business-decision-flows."* Pilots moeten binnen één semester een go/no-go-gate hebben — geïntegreerd of stoppen.
3. **Verificatie aangenomen als evaluatie.** Geen kwaliteitssysteem dat alleen slagen of zakken meet zonder *"wat ging interessant fout?"* te coderen.
4. **Restructuring herverpakt als transformation.** Een naamsverandering is kosmetisch als de change theory dezelfde is als bij eerdere mislukte interventies.
5. **Strategie geschreven door consultants in een dark room.** Het expliciete contrast van Erginbilgić. Een PRD zonder workshop-traject met de docentenstaf en de ondersteunende collega's rond de opleiding — proportioneel naar Erginbilgić's volume, niet in absolute aantallen — slaat het strategievormingsproces over dat alignment oplevert.
6. **De *willingness to serve* verlagen door meer geld.** Oberholzer-Gee 2022: *"waarde is geredistribueerd, niet gecreëerd."* Pak het moreel van de staf aan door de baan beter te maken (opleiding, autonomie, interessanter werk), niet door salaris.
7. **Uniforme uitrol over heterogene populaties.** Het bewijs uit Krakowski: dat veroorzaakt prestatiedaling, geen nulwinst. Stem af.

---

## 7. Bronnen ter triangulatie

De voorgaande analyse leunt op meerdere plekken zwaar op Erginbilgić 2026 als primaire bron. Per claim is hieronder genoteerd welke andere wiki-bronnen de claim onafhankelijk ondersteunen, nuanceren of contradicteren — en welke claims binnen de huidige wiki single-source blijven. De inventaris is opgesteld na een gerichte buurscan over `wiki/sources/` en `wiki/concepts/`, met leesvalidatie per kandidaat (geen pure keyword-match).

| Claim | Status | Bronnen |
|---|---|---|
| Restructuring vs transformation (semantisch onderscheid) | **Getrianguleerd** | Erginbilgić 2026 + [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] (Bain/OpenAI — dezelfde change-theory-distinctie in andere woordenschat) |
| Lagen elimineren zonder operationele mensen te ontslaan | **Getrianguleerd (3 bronnen, 3 industrieën)** | Erginbilgić 2026 + [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] (hourglass-organization, 73 % entry-hiring collapse) + [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships]] (Exhibit 20: coaching/mentorship low-SCI, prioritization/decision-making high-SCI) |
| Performance culture / mediocrity kills good people | **Getrianguleerd (neuroscience-onderbouwing)** | Erginbilgić 2026 + [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai]] (gear-3 reactive-work onderdrukt prefrontale cortex) |
| Resilience playbook (process-capability over voorspelling) | **Productieve tension** | Erginbilgić 2026 vs. [[2026-04-28-webb-strategic-foresight]] — twee strategische tradities op een kernkwestie tegenover elkaar; de PRD kiest expliciet Erginbilgić's positie en motiveert dit. |
| People-pijler (junior-leerpad bescherming) | **Getrianguleerd op deelaspect** | Erginbilgić 2026 + [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] (hourglass als operationele invulling) |
| Tailored-leadership + culture-refresh | **Reeds getrianguleerd** (op de source-pagina van Erginbilgić zelf) | Erginbilgić 2026 + [[2025-06-09-krakowski-human-centered-ai-field-experiment]] (Nordic pharma DiD, tailored beats untailored across Kirton-cognitive-style parameters) |
| Burning-platform speech (extern benchmarken vóór dag 1 + diagnose+visie in één artefact) | **Singleton** | Alleen Erginbilgić 2026. Geen substantieve wiki-buur op het mechanisme. Toekomstige ingest: Kotter, *Leading Change* (HBR 1995 / boek 1996) of vergelijkbare change-narrative literatuur. |
| Open strategy / 25-30 workshops / *no-hierarchy-in-the-room* / granulariteit | **Singleton (bekend gat)** | Alleen Erginbilgić 2026. De concept-pagina [[strategy|concepts/strategy]] markeert dit zelf als structureel gat. Toekomstige ingest: Whittington, *Opening Strategy* (Oxford 2019). |
| Vier-pijlers-framework (als frame) | **Singleton** | Alleen Erginbilgić 2026. Afzonderlijke pijlers (Mensen, Performance) zijn getrianguleerd; het frame zelf niet. |
| Demanding ≠ tough love (precieze formulering) | **Singleton** | Alleen Erginbilgić 2026. Het onderscheid (demanding-met-fairness-en-transparantie binds high bar to trust contract) is bron-specifiek; geen wiki-tweede-bron. |

**Resultaat.** De 22 single-source-Erginbilgić-vermeldingen in dit document worden door bovenstaande triangulatie effectief teruggebracht naar circa 12 tot 14 *écht* single-source claims, waarvan 4 (burning-platform-methodologie, open-strategy-doctrine, vier-pijlers-frame, demanding-niet-tough-love-onderscheid) expliciet als legitiem singleton of als bekend wiki-gat zijn gemarkeerd. De andere claims hebben minstens één onafhankelijke wiki-buur — in één geval (resilience) zelfs een productieve tension, die de geargumenteerde keuze in de PRD positioneert binnen een echt strategisch debat in plaats van consensus te suggereren waar die er niet is.

**Wat er nog niet getrianguleerd is.** De vier singletons hierboven, plus alle HBO/NL-context-specifieke claims (NVAO-cyclus, OR/MR-dynamiek, NSE-signalen) staan los van de wiki — zie §8 voor de open vragen.

---

## 8. Open vragen waarop de wiki geen antwoord biedt

De wiki bevat geen onderwijsspecifieke evidentie. De volgende vragen vereisen aanvullend onderzoek buiten het ai-wiki-corpus:

1. **NVAO-tijdsbeperkingen.** Hoe verhouden de zeven Erginbilgić-stappen zich tot de NVAO-accreditatiecyclus? Wat moet binnen welke termijn aanwezig zijn?
2. **OR- en medezeggenschapsraad-dynamiek.** Erginbilgić elimineerde lagen in een Britse aerospace-context. De Nederlandse HBO-context vereist OR-instemming bij organisatorische ingrepen. De wiki behandelt dit niet.
3. **Specifieke onderwijssignalen.** Geen inspectiesignalen van de NVAO, geen signalen uit de Nationale Studenten Enquête, geen kaders van de Inspectie van het Onderwijs in de wiki.
4. **Kwantitatieve drempelwaarden.** De wiki levert patronen, geen drempels (*"als ziekteverzuim > X % dan signaalstatus Y"*).
5. **AI-in-pedagogiek-literatuur.** De wiki bevat één feit over AI-gebruik door studenten (AI Index 2026) en is verder stil over ChatGPT in de klas, AI-detectie in essays, AI-beleid bij universiteiten en curricula voor AI-geletterdheid. Een volledig antwoord op Q4 vereist aanvulling uit onderwijspedagogische bronnen.
6. **Open-strategy academische literatuur.** De doctrine van *strategie als participatie* rust op één wiki-bron (Erginbilgić). De wiki-pagina `strategy.md` markeert dit als een gat: *"de dichtstbijzijnde wiki-buur op deze doctrine is nog niet aanwezig — er is geen concept-pagina voor open strategy of strategy-as-conversation."* Whittington's *Opening Strategy* of vergelijkbaar zou de aanbeveling steviger maken.

---

## 9. Voorgestelde volgende stappen (buiten dit document)

1. **Lees de bestaande PRD-draft naast de zevenstappenreeks in sectie 3.** Identificeer waar de huidige draft een stap overslaat (waarschijnlijk: externe diagnose vóór dag één, en het workshop-traject met de docentenstaf — schaal-proportioneel naar Erginbilgić's 25 tot 30 workshops bij Rolls-Royce, niet letterlijk overgenomen).
2. **Identificeer twee tot drie externe diagnose-datapunten** naast het slagingspercentage van 90 %. Zonder die context is stap 2 (burning-platform-speech) niet eerlijk te voeren.
3. **Plan een eerste reeks workshops** voor de strategievorming volgens stap 4. Drie tot vijf workshops met de volledige docentenstaf (ongeveer veertig docenten) plus de ondersteunende collega's rond de opleiding, met de protocols *"no hierarchy in the room"* en *"this is going to be chaotic."*
4. **Definieer de v1-scope van het kwaliteitssysteem** zo klein mogelijk, volgens principe 5 (momentum). Eén of twee jaargroepen, één faculteit, één semester data verzamelen *voordat* je institutionaliseert.
5. **Schrijf een interne afspraak (norm)** dat AI in communicatie nooit als employee of tutor wordt geframed, alleen als tool. Mitigatie van risico 4.
6. **Plan voor risico 6 (open strategy):** vraag een onafhankelijke onderzoeker (of Whittington's *Opening Strategy*) om de doctrine van *strategie als participatie* een tweede empirische bron te geven voor de PRD.

---

*Volledige bronnenmatrix en onderzoekslog: `2026-05-26-hbo-bk-kwaliteitssysteem-research-log.md` (dezelfde map).*
