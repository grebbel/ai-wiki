---
type: interview-answers
date: 2026-05-20
topic: "PRD Validatie Interview — AI-adviseur voor MKB"
interviewer: Nathan (student Bedrijfskunde)
respondent: AI-adviseur (gebaseerd op ai-wiki)
status: completed
---

# PRD Validatie Interview — Antwoorden

> **Methode:** elk antwoord is gebaseerd op de ai-wiki (`node scripts/wiki-query.mjs`).
> Waar de wiki direct evidence levert: antwoord met citaten naar wiki-pagina's.
> Waar de wiki indirect raakt: antwoord met expliciete *"de wiki spreekt hier indirect over..."*.
> Waar de wiki stil is: expliciet *"de wiki bevat hier geen materiaal over"*.
>
> **Belangrijke caveat vooraf:** de wiki is gefocust op AI-strategie, agent-harness,
> dynamic capabilities en grootbedrijf/customer-story content — **niet specifiek
> Nederlands MKB-automatisering**. Veel antwoorden zullen daarom indirect of partieel zijn.
>
> **Definities** (uit Nathans vragenset):
> - MKB = bedrijven met <250 fte
> - Lokaal = binnen Nederland, regionaal opererend
> - Simpele automatisering = workflows met <5 processtappen, zonder maatwerk ML
> - Oude systemen = legacy software, on-premise databases, niet-API-toegankelijke tools

---

## 1. Markt & kans

**Hoofdvraag:** Beschrijf de laatste drie keer dat je een MKB-bedrijf hebt zien werken met handmatige, repetitieve processen.

**Antwoord:**

De wiki bevat geen Nederlandse MKB-cases — alle voorbeelden komen uit grootbedrijf-deployments — maar drie patronen zijn goed gedocumenteerd en raken jouw vraag direct.

**Eerste voorbeeld: customer support bij Lyft.** Tot 2023 liepen de wachtrijen vol met handmatige, repetitieve ticketafhandeling — bestuurders en passagiers die vastliepen in dezelfde categorie problemen, support-agents die *"30+ minuten"* per case kwijt waren. Na inzet van een Claude-gebaseerde assistent daalde de oplostijd met **87%** ("soms in seconden"); de bespaarde miljoenen werden niet omgezet in ontslagen maar in upskilling van agents en een nieuwe high-touch dienst ("Lyft Silver"). Zie [[2026-02-18-lyft-customer-support-with-claude]].

**Tweede voorbeeld: customer success bij HubSpot.** CSM's deden voorheen handmatig calltranscripties uitwerken, follow-ups schrijven en knowledge base-artikelen erbij zoeken — uren werk per klant. Met Claude gaat het van transcript-plus-artikelen naar een eerste analyse waarin de CSM ineens *revenue-analyse* doet voor een hospitality-klant ("dat ligt ver buiten mijn normale rol"). Engineering claimt 40% productiviteitswinst (testimonial, geen meting). Zie [[2026-02-09-hubspot-customer-success-with-claude]].

**Derde voorbeeld: changeover bij Heineken Mexico.** Een 6-uur durende productie-changeover die feitelijk *"maar vijftien minuten aan informatie bevatte"* — de rest was wachten op data. Een relatief simpele AI-agent die machine-, cloud- en onderhoudsdata on-demand ophaalde, comprimeerde 6 uur naar 15 minuten en leverde **een miljoen extra kratten bier per maand** op. Zie [[concepts/industrial-ai-agents]] en [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success]].

Het canonieke empirische anker hierachter is [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (QJE 2025)]]: **+15% productiviteit** in customer support, met een sterk gelijkmakend effect (laagopgeleide agents +30%, ervaren agents ~0%).

**Belangrijke caveat:** dit zijn allemaal *grootbedrijf-cases* (Fortune 500, beursfondsen, een internationale brouwerij) — niet Nederlands MKB. De wiki noemt MKB-beperkingen alleen indirect, bijvoorbeeld in [[concepts/lean-4-0]] dat expliciet flagt dat Lean 4.0-frameworks "vooral voor grote fabrikanten geschreven zijn; kosteneffectieve SME-paden blijven onderontwikkeld." Voor échte Nederlandse MKB-validatie heb je primaire bronnen nodig die de wiki nu niet bevat.

---

## 2. Probleem-oplossing fit

**Hoofdvraag:** Wanneer een MKB-eigenaar voor het eerst over een procesprobleem vertelt — wat zegt hij of zij dan letterlijk?

**Antwoord:**

De wiki bevat **geen letterlijke MKB-quotes** — er is geen etnografisch materiaal over hoe een Nederlandse MKB-eigenaar voor het eerst over een procesprobleem vertelt. De ai-wiki documenteert leiderschapsdynamiek bij grotere organisaties (Heineken, Google, Amazon, Lowe's, Fortune-1000) en bij consultants/academici die *over* leiders schrijven. Met die beperking expliciet: de wiki suggereert dat eerste-articulatie zelden in proces-taal gebeurt — het begint vaker bij een **capaciteitssymptoom** of een **financieel symptoom**.

Het scherpste voorbeeld zit in [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier (MIT Sloan, 2026)]]: bij Heineken Mexico kwam het probleem eerst op tafel als *"we hebben twee nieuwe bottellijnen nodig"* — een **capex-vraag**, niet een procesvraag. Pas na time-delay-analyse bleek het werkelijke probleem: *"het duurde zes uur om een changeover te doen, maar er was maar vijftien minuten aan informatie."* Carrier veralgemeent dit: leiders kopen capaciteit in plaats van het systeem te repareren. [[2022-06-29-martin-hbr-a-plan-is-not-a-strategy|Martin (HBR, 2022)]] noemt dit de *planning-trap* — leiders defaulten naar kostenkant-keuzes die ze controleren, niet naar de strategische diagnose.

Bij [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels (McKinsey, 2026)]] articuleert de CEO het probleem juist **financieel-spanning-tussen-rollen**: *"My CFO is in my ear that we're spending a lot of money on technology, but we're not yet seeing enterprise-level value. CIO's saying: this is one of those moments."* De aanleiding is hier een rapportage-meeting, niet een procesinzicht.

Over **wie het eerst benoemt**: meerdere bronnen convergeren op het tegenovergestelde van wat leiders aannemen. [[2026-05-07-carucci-resistance-as-data|Carucci (HBR, 2026)]] stelt dat *"de mensen die het meest weerstand bieden tegen de verandering juist het dichtst bij de risico's staan die het kunnen laten ontsporen"* — operationele medewerkers zien procesproblemen die leiders missen of wegredeneren als kennis-/loyaliteitskwestie. [[concepts/micro-productivity-trap|micro-productivity-trap]] noemt dit een **luister-falen, geen technologiefalen**: vijf onafhankelijke bronnen wijzen op de patroon dat *operators see problems leaders dismiss*.

[[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work|Sterman (MIT Sloan, 2026)]] voegt de diepere diagnose toe: leiders denken in open-lus (probleem → data → besluit → klaar), terwijl de werkelijkheid feedback is. De eerste verwoording is daarom bijna altijd een symptoom, niet de feedback-lus die het symptoom produceert — vandaar de waarde van het Forrester-achtige diagnose-gesprek dat áchter de eerste klacht graaft. Voor Nederlands-MKB-specifieke quotes is aanvullende bronvergaring (Kamer van Koophandel, MKB-Nederland, etnografisch onderzoek) noodzakelijk; die zit niet in deze wiki.

---

## 3. Implementatie realiteit

**Hoofdvraag:** Beschrijf een geval waarin een automatiseringsproject vastliep op de bestaande IT-omgeving. Wat gebeurde er precies?

**Antwoord:**

Een van de scherpste cases in de wiki is het Klarna-verhaal, gerapporteerd door [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni op de E-commerce Berlin Expo]]: Klarna ontsloeg in 2023 zijn klantenserviceteam omdat een AI-agent het werk zou overnemen. Zes maanden later werd dat team opnieuw aangenomen. De pilot werkte uitstekend in demo-omstandigheden, maar in productie liepen edge-cases vast — gevallen die juist de bestaande systemen (CRM, betalingsbackends, regelgevingslogica) raakten en waar de agent geen grip op kreeg. Het project liep dus niet vast op de modellaag, maar op het orkestratievlak: integratie en operationeel beheer van uitzonderingen. Ognibeni vat dit samen als de *demo-to-deployment chasm* — een patroon dat hij toeschrijft aan de bredere BCG/PwC/McKinsey-bevinding dat "elk bedrijf iets met AI doet, maar zelden zien we daar economische waarde uit komen op schaal."

Een tweede, fysieker voorbeeld komt uit [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier (MIT Sloan)]]: een raffinaderij waar hij vijftien jaar geleden werkte, kreeg te maken met *alarm-fatigue* — het veiligheidssysteem werd zó overspoeld met meldingen dat de informatiestroom feitelijk stilviel. Eén onset-mail leidde mede tot een tragedie met twee doden. Hier was de technologie zelf operationeel; het probleem zat in de integratie met menselijke besluitvorming en in de cultuur van "verzamel alle data". Carrier's diagnose is organisatorisch: men optimaliseert op datavolume in plaats van op leading indicators.

De [[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work|Sterman-webinar (MIT Sloan, mei 2026)]] tilt deze observaties naar een algemener principe: *policy resistance*. Goed onderzochte, expert-gevalideerde oplossingen — M&A's op synergie-logica, TQM-, Six Sigma- en BPR-trajecten — werken op korte termijn of niet, waarna het probleem elders weer opduikt. Sterman noemt dit "extreem gewoon en extreem ontmoedigend"; de oorzaak is een mismatch tussen het open-loop-mentale model van managers en het feedback-rijke systeem dat de werkelijkheid is. Het is dus zelden puur technisch en zelden puur organisatorisch — het is een systeemkwestie waarin de IT-omgeving slechts het oppervlak is waar de mismatch zichtbaar wordt.

Een eerlijk voorbehoud: de wiki's evidence zit overwegend op grootbedrijfsschaal (Klarna, Heineken, raffinaderijen, Lowe's). Concrete MKB-cases waarin een AI-project vastliep op legacy on-prem databases of fragmentarische IT-omgevingen ontbreken in het corpus. De [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]-pagina noemt wel de bredere *micro-productivity-trap* (task-level winst die niet doorstroomt naar firm-level waarde) als het patroon waaronder deze faalwijzen schuilen.

---

## 4. Waarde van simpel vs complex

**Hoofdvraag:** Noem een automatisering die heeft gewerkt in een MKB-bedrijf, waarbij de oplossing eenvoudig was. Wat leverde het op?

**Antwoord:**

Een sterke en concrete case uit de wiki is de **Heineken-brouwerij in Mexico**, beschreven door MIT Sloan-docent John Carrier ([[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier, MIT Sloan 2026]]). Carriers studenten ontdekten dat een changeover op de bottelarij zes uur duurde, terwijl er feitelijk maar **vijftien minuten aan informatie** in zat — de rest was wachten op data. Ze bouwden geen geavanceerd ML-systeem, maar *"een relatief simpele AI-agent die machine-, cloud- en onderhoudsdata kon ophalen op het moment dat dat nodig was"*. De changeover ging van zes uur naar vijftien minuten. **Opbrengst: ongeveer één miljoen extra kratten bier per maand.**

Wat dit voorbeeld zo bruikbaar maakt voor het PRD-gesprek, is *waarom* deze oplossing simpel was: één agent die bestaande data uit drie systemen bij elkaar haalde op het juiste moment. Geen LLM-stack, geen vector database, geen agent-orchestrator. Carrier formuleert dit als een heuristiek: *"there's no reason to jump to a level five agent when a simple rule-based agent will do"* — eerst het probleem vinden, dán het juiste agent-niveau kiezen ([[concepts/industrial-ai-agents|industrial-ai-agents]]).

**Hoe meet je de opbrengst?** Heineken meet operationeel, niet financieel: kratten per maand (volumemaat), changeover-tijd in uren, machine-utilisatie. Carriers checklist voor industrial-AI-waarde noemt drie diagnostische plekken: kapitaalallocatie (waar wil men investeren terwijl het probleem informatie is?), informatiestromen die tot lage utilisatie leiden (*"twintig procent extra capaciteit als de informatie beter was"*), en variatie in taakduur. Voor MKB vertaalt dit naar: changeover-tijd, doorlooptijd per order, defect-rate, foutmarges in offertes — concrete operationele uren of stuks, niet abstracte ROI-percentages.

**Wat had het bedrijf gedaan zonder deze automatisering?** Carrier vertelt dit expliciet: Heineken stond op het punt **twee nieuwe bottellijnen te kopen**. Dat is de klassieke planningsval — capaciteit kopen in plaats van het systeem repareren. Andrew Ng en Rodney Brooks worden in dezelfde context geciteerd voor het bredere principe *"we need to unbig in AI"*: Brooks ging van de complexe Sawyer-robot (2012) naar simpele, specialistische material-handlers (2024) — *"industry just needs something very simple robot designed to do one specific task over and over again; that's the one having the impact"*.

Eerlijke kanttekening: Heineken Mexico is geen MKB. Maar het onderliggende principe schaalt expliciet naar kleinere context — een simpele rule-based agent die bestaande data uit drie systemen koppelt, levert vaak meer op dan een ambitieus L5-platform. Carriers les: *scope eerst naar één gemiste feedback-loop, meet in operationele eenheden, en kies de simpelste agent die die loop sluit.*

---

## 5. Verdienmodel

**Hoofdvraag:** Wat zeggen MKB-bedrijven wanneer zij voor het eerst de prijs van een softwareabonnement zien?

**Antwoord:**

De wiki bevat geen onderzoek naar MKB-reacties op softwareprijzen specifiek. Wat hij wel biedt:

**Het sterkste prijspunt-anker** komt uit de Emergent-customer-story van Mukund Jha op het Claude-kanaal ([[2026-05-13-jha-emergent-democratizing-app-building-with-claude]]). De headline-anekdote: **Christy**, een klinisch psycholoog en paardencoach in Alaska, betaalde **$50K aan een Nova Scotia dev shop** voor een app die niet werkte — daarna stapte ze over naar Emergent en lanceerde *Equ* op de App Store met "hundreds of users". Jha noemt expliciet het vergelijkingsanker: gebruikers vergelijken Emergent's output met **"a $250,000 price point that they would have paid if they had gone and hired a dev shop"**. Dit verschuift het hele referentiekader: niet *"is een abonnement duur?"* maar *"hoeveel goedkoper dan $250K?"*.

Belangrijke implicatie voor het verdienmodel: Jha stelt dat zijn gebruikers **"not price sensitive, not latency sensitive — they're comparing us to a 3-months project that would have been executed outside"** (~8:00). Het *prijs-anker* dat de klant in het hoofd heeft, bepaalt of een abonnement "redelijk" of "te duur" voelt — niet het abonnementsbedrag zelf.

De *"price doesn't matter as much as personality/taste/voice"*-lijn uit het Claude-channel cluster (Lyft, HubSpot, Figma Make, Emergent) gaat over **modelselectie door bouwende teams**, niet over MKB-bereidheid-tot-betalen voor SaaS. Niet rechtstreeks bruikbaar voor PRD-vraag 5.

**Wat de wiki niet heeft**: geen Nederlandse MKB-prijspunten, geen onderzoek naar opzegtermijnen of minimumduur-dealbreakers, geen kwalitatief onderzoek naar eerste-reactie op abonnementsprijzen. Dit is een echt wiki-gat — voor vraag 5 zijn primaire klantgesprekken of extern marktonderzoek nodig. De wiki biedt alleen het *anker-effect* als hypothese: positioneer prijs tegen een duurder alternatief (dev shop, consultant, fulltime medewerker), niet als losse SaaS-fee.

---

## 6. Positionering & niche

**Hoofdvraag:** Bedrijven die succesvol zijn geworden met automatiseringsdiensten voor het MKB — wat hadden zij in hun eerste 12 maanden gemeen?

**Antwoord:**

De wiki bevat geen Nederlandse MKB-dienstverleners als bronnen, dus dit antwoord is gebaseerd op analoge cases — vooral Amerikaanse natural-language-to-app-platforms (Emergent, Replit), Chinese agentic-commerce (Alibaba, JD.com via Ognibeni) en de strategie-canon (Martin, Oberholzer-Gee). Lees het dus als patroonherkenning, niet als directe benchmark.

**Wat doorbrekers in hun eerste 12 maanden gemeen hadden.** De scherpste case is [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Emergent]]: $100M ARR in 8 maanden, 7M gebruikers in 190 landen, 70–80% nooit een regel code geschreven. Vier patronen vallen op. *Eén:* een **enterprise→SMB pivot** nadat ze merkten dat enterprise-adoptie traag was — ze kozen bewust de long-tail waar het kostvergelijk extreem is (Christy, psycholoog in Alaska, betaalde eerst $50K aan een dev-shop, bouwde uiteindelijk haar app *Equ* op Emergent). *Twee:* **index-op-hoogste-redeneerkwaliteit, niet snelheid of prijs** — gebruikers vergelijken met een 3-maanden $250K-traject, dus latency en token-kosten zijn niet de bindende constraint. *Drie:* een **delete-and-reimagine-discipline** — *"we hebben onze systemen vier keer herschreven in 9 maanden"* (Jha). Bij elke nieuwe modelgeneratie het hele systeem opnieuw bouwen vanuit het lens van het nieuwe model. *Vier:* harness-as-product — de differentiatie zit in het hele agentic-engineering-stack (container-tech, multi-agent, long-term memory, pre/post-deploy security agents), niet in het model. [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Replit]] vertelt hetzelfde verhaal vanuit dezelfde categorie.

**Wat niet-doorbrekers gemeen hadden.** [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni]] geeft vier failure modes: *Klarna-patroon* (te vroeg uitschalen — service-team ontslagen, zes maanden later weer aangenomen omdat edge cases de pilot deden falen); *demos-to-deployment chasm* (BCG/PwC/McKinsey constateren dat bijna iedereen iets met AI doet maar weinigen economische waarde realiseren); *silo's denken in plaats van ecosystemen*; en *trust-deficit*. Achter al deze symptomen zit het patroon dat [[2022-06-29-martin-hbr-a-plan-is-not-a-strategy|Martin]] beschrijft als *playing to play* — een lijst activiteiten zonder coherente *theory of winning*. Geen scherpe keuze waar te spelen, geen expliciete logica over hoe je wint. Pair dit met de [[concepts/micro-productivity-trap|micro-productivity-trap]]: bedrijven die AI inzetten voor kostenbesparing op individuele taken zonder business-modelvernieuwing.

**Wat is "succesvol"?** De wiki gebruikt impliciete signalen — ARR-groei, retention, en duurzame *defensibility* (Carly Ryan's triplet: *deep user understanding, proprietary infrastructure, human trust*). Eerlijk: dat is een Silicon Valley-meetlat. Voor Nederlandse MKB-automatisering past mogelijk beter een combinatie van klantbehoud >12 maanden, herhaalbare leverdiscipline, en de Oberholzer-Gee-test ([[concepts/strategy]]): is de *willingness-to-pay minus willingness-to-sell* meetbaar verbreed? Dat is een vraag die het PRD-onderzoek zelf moet beantwoorden — de wiki levert hier het frame, niet de Nederlandse data.

---

## 7. Grootste fouten / risico's

**Hoofdvraag:** Beschrijf een ondernemer die is gestart met een automatiseringsdienst voor MKB en daarmee is gestopt of vastgelopen. Wat ging er mis?

**Antwoord:**

De wiki bevat geen Nederlands-MKB-dienstverlener die met een automatiseringsdienst is vastgelopen, dus ik gebruik proxy-cases — vooral de Nova Scotia dev shop uit het Emergent-verhaal en de Klarna-rehire — om het mechanisme zichtbaar te maken. Eerlijk gezegd: dit zijn de zijdelingse signalen, niet de directe Nederlandse markt.

De meest concrete faalcase is die van **Christy**, een psychologe annex paardentrainer in Alaska, beschreven door Mukund Jha (CEO Emergent). Zij betaalde **$50K aan een dev shop in Nova Scotia** voor een custom app die haar twee vakgebieden moest verbinden — en kreeg een product dat *niet werkte*. Pas toen ze later naar Emergent overstapte, kon ze haar app *Equ* op de App Store krijgen ([[2026-05-13-jha-emergent-democratizing-app-building-with-claude]]). Dit is de schaduwzijde van de MKB-automatiseringsdienst: een dienstverlener belooft maatwerk, scope groeit, het MKB-bedrijf betaalt vooruit, en het moment-van-duidelijkheid komt pas bij oplevering — als er niets bruikbaars staat. De dienstverlener is dan al weg of failliet; de klant blijft met de rekening.

De tweede case is **Klarna**, gerapporteerd door Björn Ognibeni: Klarna ontsloeg het hele customer-serviceteam omdat AI het zou overnemen, en moest ze **zes maanden later terughalen** — *"the pilot worked great but edge cases make it extremely difficult to actually do this"* ([[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]]). Het moment-van-duidelijkheid was de eerste echte edge case in productie, niet de demo.

Wat ging er mis, terugkerend over de cases:

- **Demo-tot-deployment-kloof**: BCG, PwC en McKinsey rapporteren allemaal dat *bijna elk bedrijf iets met AI doet, maar zeer weinigen er economische waarde uit halen* ([[concepts/enterprise-ai-adoption]]). De pilot werkt; productie breekt.
- **Geen iteratiediscipline**: Jha vertelt dat Emergent zijn **systeem 4× in 9 maanden** herschreef bij elke nieuwe modelklasse. Wie dat niet doet, levert verouderde architectuur op.
- **Verkeerde maat van automatisering**: een full-stack agent inzetten waar een simpele workflow volstaat — bouwt complexiteit die niemand kan onderhouden.
- **Geen ecosysteem-denken, alleen silo's**: Ognibeni's diagnose — *"we think in silos and these silos are not interconnected"* — past direct op MKB-automatisering die één proces optimaliseert maar geen aansluiting heeft met de rest van het bedrijf.
- **Verkeerde framing**: kostenbesparing als doel in plaats van groei. Klarna stuurde op kostenreductie; Emergent klanten vergelijken met *"a $250K, 3-month dev-shop project"* en sturen op uitkomstkwaliteit.

Achteraf had anders gemoeten: **klein starten met één gemeten feedback-loop**, niet beloven wat nog niet bewezen werkt in productie, en *outcome-first* ontwerpen — eerst de bewezen gedragsverandering, dan pas de architectuur eromheen. Vertrouwen wordt verloren bij de eerste edge case; pas terug te winnen door eerlijke scope.

---

## 8a. Standaardisatie

**Hoofdvraag:** Welke onderdelen van automatiseringsoplossingen komen tussen verschillende MKB-bedrijven terug in vrijwel dezelfde vorm?

**Antwoord:**

De wiki heeft hier ongewoon sterke evidence: zowel bij agent-engineering primitieven als bij customer-facing patronen blijken automatiseringsoplossingen voor MKB-bedrijven op een herkenbaar fundament te rusten dat in vrijwel identieke vorm terugkomt.

**De zes Trivedy-primitieven als universeel skelet.** In [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness]] formuleert Vivek Trivedy (LangChain) de equation *Agent = Model + Harness* en leidt zes herbruikbare primitieven af die elke serieuze agent-oplossing nodig heeft: (1) **filesystem** voor doorgaande staat en multi-agent samenwerking, (2) **bash + code als generieke tool** zodat het model zijn eigen tools on-the-fly ontwerpt, (3) **sandbox + verifier defaults** (test runners, logs, screenshots), (4) **memory & search** — concreet via een `AGENTS.md` config-bestand dat bij sessie-start in context wordt geïnjecteerd, plus Context7 MCP voor documentatie-lookup, (5) **context-rot mitigatie** via compaction, tool-call offloading en Skills (progressieve disclosure), en (6) **long-horizon execution** via Ralph-loops, planning en self-verification. Trivedy laat zien dat *enkel de harness wisselen* zijn Terminal-Bench-team van Top 30 naar Top 5 bracht — de primitieven dragen zwaar, ongeacht het onderliggende model.

**Anthropic's blueprint is bijna 1-op-1 herbruikbaar.** In [[2025-11-26-anthropic-effective-harnesses-long-running-agents]] documenteert Justin Young de canonieke initializer-agent + coding-agent vorm: een `init.sh` script, een `claude-progress.txt` log, een initiële git-commit, en een `feature_list.json` met alle features (initieel `"passes": false`). Elke nieuwe sessie begint met `pwd` → git-log → progress-file → feature-list. Anthropic ontdekte zelfs dat JSON robuuster is dan Markdown voor agent-bewerkte staat. Voor een MKB-leverancier is dit een template dat per klant nauwelijks hoeft te wijzigen — alleen de feature-inhoud.

**Customer-facing patronen tonen identieke mechaniek.** [[2026-02-18-lyft-customer-support-with-claude]] en [[2026-02-09-hubspot-customer-success-with-claude]] gebruiken op een ander niveau exact hetzelfde recept: domeinkennis injecteren (knowledge-base artikelen + historische data), een herkenbare persoonlijkheid/tone-of-voice afdwingen, en een escalatie-route naar mensen voor complexe gevallen. Vertaald naar Nederlands MKB werkt dezelfde harness voor factuurvragen, leveringsstatus, FAQ-routering en CSM-follow-ups.

**Eerlijke afbakening.** Dit is *generieke agent-engineering*, geen Nederlandse MKB-bedrijfsproces-template. De wiki bevat geen sector-specifieke modules (groothandel-orderpicking, accountancy-workflows, etc.). Wat universeel is, is het **skelet** — filesystem, AGENTS.md, hooks, init.sh/progress/feature-list, escalatie-route — niet de domein-invulling daarbinnen.

---

## 8b. Maatwerk

**Hoofdvraag:** Welke onderdelen moeten per bedrijf opnieuw worden ontworpen of ingericht?

**Antwoord:**

De wiki is hier ongewoon expliciet: een agent-implementatie kent een *generieke laag* (model, harness-primitieven, tools, evaluatie-discipline) en een *bedrijfs-specifieke laag* die per organisatie van de grond af aan wordt ingericht. Hergebruik werkt voor de eerste, niet voor de tweede. Vijf onderdelen vallen consistent in die tweede categorie.

**1. Werkdefinitie en succes-criteria.** Wolfe's *Agent Evaluation* roadmap zet *"Define success — outcome goals (final state) + process goals (transcript components)"* als stap 1 van zeven, vóór alles ([[2026-05-18-wolfe-agent-evaluation-detailed-guide]]). Trivedy formuleert hetzelfde principe vanuit de bouw-kant: *"Behavior we want (or want to fix) → Harness Design to help the model achieve this"* — werkt achterwaarts vanuit gewenst gedrag naar harness-primitieven ([[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness]]). Wat "klaar" en "goed" betekent is in een orderverwerker-MKB iets fundamenteel anders dan in een advocatenkantoor; geen template levert die definitie.

**2. Feedback-loops mapping.** Carrier is hier op zijn scherpst: *"a key insight from Jay Forrester — there were some missing feedback loops here. So it's not simply about building AI agents. It's about using them to replace long, slow feedback loops with very fast ones"* ([[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success]]). De Heineken-changeover (6 uur → 15 minuten) was géén generieke loop — het was *die specifieke* loop in *die* brouwerij. Een loodgietersbedrijf, een retailer of een gemeentelijke balie heeft andere trage loops. Eerst in kaart brengen, dan pas een agent ontwerpen.

**3. Domein-vocabulaire, data-toegang en tool-koppelingen.** Wolfe's evaluation harness moet *"the same scaffold, tools, and environment that are used in production"* spiegelen. Dat betekent: welke systemen (Exact, AFAS, Snelstart, SAP, Excel-tabbladen) heeft dít bedrijf, en hoe komt de agent erbij? De tool-laag uit Trivedy's anatomie (filesystems, sandboxes, MCPs) is generiek; de *invulling* — welke tools, welke schema's, welke API-rechten — is per organisatie uniek.

**4. Beslissingsbevoegdheid en escalatie.** Wie mag wat goedkeuren? Welke acties vereisen menselijke review? Dit is governance-werk dat tegen de organisatiestructuur aan zit en niet uit een sjabloon komt.

**5. Calibratie aan medewerker-niveau.** Brynjolfsson's variantie (laagopgeleide agents +30%, ervaren ≈0%) impliceert dat een agent gebouwd voor juniors anders moet zijn dan voor seniors ([[concepts/ai-employment-effects]]). Per team afstemmen, niet één-maat-iedereen.

**Eerlijk caveat:** de wiki spreekt over deze maatwerk-laag in generieke termen. Een Nederlandse MKB-template-anatomie — *"voor een installatiebedrijf van 20 fte met AFAS ziet de harness er zó uit"* — bestaat hier niet. Dat is precies waarom dit per bedrijf opnieuw moet.

---

## 9. Concurrentie & onderscheid

**Hoofdvraag:** Welke vragen van MKB-bedrijven over procesautomatisering blijven op dit moment onbeantwoord door bestaande aanbieders?

**Antwoord:**

In de wiki tekenen zich drie witte vlekken af die bestaande aanbieders structureel laten liggen bij MKB-vragen over procesautomatisering.

**Witte vlek 1 — kosteneffectieve SME-paden.** [[concepts/lean-4-0|Lean 4.0]] erkent dit expliciet als open onderzoeksgat: de bestaande Lean-4.0-frameworks zijn "mostly written for large manufacturers; cost-effective SME paths remain underdeveloped" (Gomaa 2025, research gap-tabel). Hetzelfde geldt voor de bredere implementatiekosten, integratiecomplexiteit en skills-gaps die specifiek SME-schaal raken. Voor het MKB betekent dit: de Lean-tool-naar-Industry-4.0-mapping bestaat wél, maar de geprijsde, modulaire, niet-consultant-zware route ernaartoe niet.

**Witte vlek 2 — feedback-loop diagnose vóór tooling.** [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier (MIT, 2026)]] stelt dat winnaars worden bepaald door *adoptiesnelheid en system-fit*, niet door technologietoegang — en dat AI-agenten dienen om "lange, trage feedback-loops te vervangen door snelle". De bestaande aanbiederslogica is omgekeerd: tooling eerst, loops nooit. Sterman's group-modeling-traditie en de MIT-systems-dynamics-lijn die Carrier mobiliseert zijn in de Nederlandse MKB-adviesmarkt nauwelijks vertegenwoordigd; consultants verkopen *implementatie*, geen *loop-diagnose*. Het gevolg is wat Carrier "buy two bottling lines" noemt — capaciteitsoverspend zonder dat de bindende beperking ooit is geïdentificeerd.

**Witte vlek 3 — de [[concepts/micro-productivity-trap|micro-productivity-trap]] doorbreken.** Taakwinst (de developer die 20× sneller een feature levert) loopt niet door naar firm-level resultaat (Google: ~10% versnelling totaal) zolang de omliggende workflow nog op tacit knowledge, handmatige overdrachten en legacy-systemen leunt. Bain/OpenAI, Nishar-Nohria, Kiron-Schrage en zeven andere bronnen convergeren: *process redesign creates most of the value* — en dat is precies wat niemand verkoopt aan een installatiebedrijf met 40 man personeel.

**Concreet voorbeeld.** Christy's case (paardencoach in Alaska, $50K kwijt aan een dev shop voor iets dat uiteindelijk een SaaS-agent-build bleek) is het paradigma. Het MKB-equivalent: een Nederlands installatiebedrijf dat een offerte-agent zoekt en alleen "ERP-implementaties" of "AI-strategie-trajecten van €80K" krijgt aangeboden — terwijl de werkelijke vraag een afgebakende workflow-agent is van enkele duizenden euro's per jaar.

**Waarom geen enkele aanbieder hier op inspeelt.** Carrier's adoptie-asymmetrie favoriseert long-tail bedrijven langzaam — vendors mikken op enterprise-deals waar marge zit. Consultants prijzen zichzelf uit het MKB-segment. Dev shops bouwen custom waar SaaS volstaat omdat hun verdienmodel uurtarief is, niet outcome. SaaS-vendors mikken hun ICP naar boven (mid-market en up). Het gat dat ontstaat — *diagnose + lichte tooling + workflow-herontwerp tegen MKB-budget* — is structureel, niet conjunctureel.

Eerlijke beperking: de wiki spreekt vooral over US/global cases (Lowe's, FabricationCo, Amazon, Google); concrete Nederlandse MKB-niches zijn hier niet empirisch gevalideerd — die invulling vergt eigen veldonderzoek bovenop de wiki-evidence.

---

## 10. Eerste stap

**Hoofdvraag:** Wanneer een ervaren ondernemer morgen zou starten met een automatiseringsdienst voor MKB, en advies vraagt over de eerste 30 dagen — wat zou je hem of haar vertellen?

**Antwoord:**

Een ervaren ondernemer die morgen start met een automatiseringsdienst voor MKB heeft in de eerste 30 dagen één opdracht: voorkomen dat je in de planning-val van [[2022-06-29-martin-hbr-a-plan-is-not-a-strategy|Roger Martin]] trapt. Een lijst met diensten en doelen is *geen* strategie. Volg deze fasering.

**Dag 1-7 — Theory of winning op één pagina.** Schrijf, in Martins vorm, één A4: *where to play* (welke procesklasse bij welk type MKB — denk aan Carriers Heineken-voorbeeld in [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Industrial AI that works]]: ergens waar een traag feedback-loop bestaat die je radicaal kunt verkorten), *how to win* (snelheid van uitlevering? betrouwbaarheid? domeinkennis? trust?), *capabilities* (welke harness, welke evals, welke proces-kennis), *management systems* (hoe meet je deployment-success-rate à la [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Emergent]]) en *aspiration* (waar wil je over 18 maanden staan). Accepteer Martins angst-clausule: je kunt vooraf niet bewijzen dat dit werkt.

**Dag 8-15 — Value stick voor één klantgroep.** Pas [[2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick|Oberholzer-Gee's value stick]] toe op precies één segment. Wat verhoogt WTP — kwaliteit, complements (integratie in bestaande tooling), netwerk-effecten? Wat verlaagt WTS aan jouw kostenkant — niet door simpelweg meer te betalen, maar door de *job better* te maken? Oberholzer-Gee's load-bearing inzicht: begin altijd met *value creation*, niet *value capture*.

**Dag 16-23 — Eén klant, werkende harness.** Werk *backwards from behavior* zoals [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy]] voorschrijft: welk concreet gedrag moet de klant na 14 dagen vertonen? Bouw de simpelst mogelijke harness die dát realiseert — niet meer. Volg [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's 7-stappen eval-roadmap]]: definieer succes (outcome + proces), verzamel 10-20 realistische taken, voeg ground-truth toe, configureer eerst code-based graders, dan pas model-based. Geen eval = geen product.

**Dag 24-30 — Meten en pivot-signaal.** Carriers asymmetrie is hier leidend: *"winners will be determined not by who has access to the technology, but whose organization adopts it faster."* Adoptiesnelheid bij de pilotklant is je leading indicator. Werkt-of-niet-signalen na 30 dagen: (a) geen tekenbevoegde gebruiker geactiveerd, (b) geen werkende uitlevering in productie, (c) de klant kan niet in één zin articuleren wát hij heeft gekregen — alle drie zijn direction-change-signalen.

**Stop-signalen, niet pivot-signalen.** Drie harde stops: ten eerste het Klarna-patroon van premature scaling — schaal nooit voor je deployment-success-rate stabiel boven de 90% zit zoals bij Emergent (84% → 98%). Ten tweede: als je harness na drie iteraties nog *illegal moves* genereert die niet via prompt, tools of context te repareren zijn — het probleem zit dieper dan de harness, stop. Ten derde, [[2026-05-07-carucci-resistance-as-data|Carucci's resistance-as-data]]: als belanghebbenden je oplossing wél begrijpen maar afwijzen, is de weerstand signaal — niet weerstand om te overwinnen, maar om te diagnosticeren. Vaak betekent dat: herontwerp, niet harder duwen.

Het verschil tussen mislukken en winnen in maand één zit niet in de tech. Het zit in de discipline om één pagina te schrijven, één klant te dienen, en één feedback-loop te sluiten.

---

## Bronnenmatrix

| Wiki-pagina | Gebruikt voor vraag | Kern-claim |
| ----------- | ------------------- | ---------- |
| [[2026-02-18-lyft-customer-support-with-claude]] | 1 | 87% reductie customer-resolution time; bespaard geld in upskilling i.p.v. ontslagen |
| [[2026-02-09-hubspot-customer-success-with-claude]] | 1 | CSM doet revenue-analyse "ver buiten typische rol"; 40% productiviteit (vendor-claim) |
| [[concepts/industrial-ai-agents]] | 1, 4 | Heineken Mexico — simpele agent versnelt 6u→15min changeover; ~1M extra kratten/maand |
| [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success]] | 1, 2, 3, 4, 9, 10 | Adoptie-asymmetrie; "unbig in AI"; feedback-loop diagnose vs tooling; capex-eerst is fout antwoord |
| [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work]] | 1, 8b | QJE 2025: +15% RPH; laagopgeleide agents +30%, ervaren ≈0% |
| [[concepts/lean-4-0]] | 1, 9 | Lean 4.0 frameworks "underdeveloped for SMEs" — open onderzoeksgat |
| [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting]] | 2 | CEO articuleert probleem financieel: "CFO in my ear, CIO says this is the moment" |
| [[2026-05-07-carucci-resistance-as-data]] | 2, 10 | "Resistance is data" — wie weerstand biedt staat dichtst bij faalrisico |
| [[concepts/micro-productivity-trap]] | 2, 3, 6, 9 | Task-level winst loopt niet door naar firm-level resultaat |
| [[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work]] | 2, 3 | Policy resistance; open-loop denken bij leiders; groep-modeling vereist |
| [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] | 3, 6, 7 | Klarna-rehire; demo-to-deployment chasm; silo's vs ecosystemen |
| [[concepts/enterprise-ai-adoption]] | 3, 7, 9 | BCG/PwC/McKinsey: bijna iedereen doet iets, weinig waarde |
| [[2026-05-13-jha-emergent-democratizing-app-building-with-claude]] | 5, 6, 7, 10 | $50K Nova Scotia dev shop; $250K vergelijkings-anker; 4× rewrite/9mnd; deployment-success 84→98% |
| [[2022-06-29-martin-hbr-a-plan-is-not-a-strategy]] | 2, 6, 10 | Theory of winning; planning-trap; where-to-play/how-to-win; Southwest case |
| [[2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick]] | 6, 10 | Value stick: WTP/WTS; value creation eerst, value capture daarna |
| [[2026-04-25-masad-replit-ceo-only-two-jobs-left]] | 6 | Paired natural-language-to-app categorie-anker met Emergent |
| [[concepts/strategy]] | 6 | Frame: WTP-WTS-test als waardecreatie-meetlat |
| [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness]] | 8a, 8b, 10 | Zes harness-primitieven; "Agent = Model + Harness"; working-backward-from-behavior |
| [[2025-11-26-anthropic-effective-harnesses-long-running-agents]] | 8a | init.sh + progress.txt + feature_list.json blueprint; JSON > Markdown voor agent-state |
| [[concepts/agent-harness]] | 8a | Cluster-anker voor harness-engineering als discipline |
| [[2026-05-18-wolfe-agent-evaluation-detailed-guide]] | 8b, 10 | 7-stappen eval-roadmap; "define success" als eerste stap |
| [[concepts/ai-employment-effects]] | 8b | Brynjolfsson-variantie als kalibratie-argument per medewerker-niveau |

## Onderliggende caveat — wat de wiki níét bevat

- **Geen Nederlandse MKB-cases** (geen veldwerk, geen ondernemers-interviews, geen Nederlandse aanbieders).
- **Geen letterlijke MKB-quotes** (alle bronnen zijn academisch, executive, of grootbedrijf-customer-story).
- **Geen prijsonderzoek** voor SaaS-abonnementen bij MKB (geen prijspunten, geen contractvoorwaarden-dealbreakers).
- **Geen sector-specifieke automatiseringstemplates** (groothandel, accountancy, installatie, retail).

Voor een PRD-validatie die op deze antwoorden voortbouwt, zijn dus primaire bronnen nodig: ondernemers-interviews, MKB-Nederland data, Kamer-van-Koophandel cijfers, of etnografisch veldwerk. De wiki levert het *frame* (harness-engineering, theory of winning, value stick, feedback-loop diagnose, micro-productivity-trap), niet de *Nederlandse data*.
