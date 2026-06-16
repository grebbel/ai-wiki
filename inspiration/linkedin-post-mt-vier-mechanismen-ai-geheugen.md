---
type: linkedin-post
language: nl
title: "Stel u huurt vier nieuwe medewerkers — en één van hen heeft een trucje dat de andere drie niet hebben"
based_on: "[[concepts/llm-wiki]], [[concepts/knowledge-graphs]], [[concepts/agent-harness]], [[2026-05-11-huber-chroma-rag-is-dead-agentic-search]], [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained]], [[2026-05-08-bratanic-unified-agentic-memory-hooks]]"
audience: "Mid-market CEO's / MT's — architectuur-bewust, KPI-gedreven, geen AI-engineering achtergrond verondersteld; jargon-vrij in de hoofdargumentatie, vaktermen opzettelijk geïntroduceerd in de didactische slotsectie zodat de lezer ze in pitches en rapporten kan herkennen"
narrative_structure: "SCQA + Pyramid Principle (twee MECE-pijlers — compounding en portabiliteit — onder één governing thought)"
storyline: "hybride — architectuur-reframe + twee pijlers (compounding + portabiliteit) + repo-CTA; medewerker-metafoor als didactische laag; geen vendor-critique"
target_length: "feed-post ~1.000 chars + volledig artikel ~2.000 woorden"
research_log: "[[2026-05-11-vier-mechanismen-ai-geheugen-research-log]]"
gifs:
  - inspiration/search-wiki.gif — onder pijler 1 (handboek-zoals-mens-hem-ziet)
  - inspiration/agent-wiki.gif — als climax onder de B-closer (handboek-zoals-agent-hem-gebruikt)
---

# Feed-post (~1.000 tekens) — aankondiging

**Stel u huurt vier nieuwe medewerkers. Allemaal slim. Allemaal met "AI-geheugen" op hun CV. Eén wordt elke week beter in haar werk. De andere drie niet.**

Onder het label "AI met geheugen" werken op dit moment vier compleet verschillende architecturen. De meeste MKB-directies kunnen het verschil niet zien — totdat hun systeem zes maanden later nog steeds dezelfde fouten maakt.

Drie observaties:

- Vier architecturen, één label, vier compleet andere uitkomsten onder de motorkap.
- Slechts één van de vier wordt beter naarmate u haar inhuurt; de andere drie staan stil.
- Slechts één van de vier kunt u meenemen als u het systeem vervangt; de andere drie laten hun kennis achter.

Drie kostenposten. Eén kapitaalinvestering.

In het volledige artikel: de vier medewerkers in detail, twee sollicitatievragen waarmee u onderscheidt wie u eigenlijk gekocht heeft, en een werkende implementatie waar u zelf doorheen kunt klikken. Stuk staat in de eerste reactie.

#AINative #Strategie #Leiderschap #MKB

---

# Volledig artikel — *Stel u huurt vier nieuwe medewerkers*

## Eén label, vier compleet andere medewerkers

U bent de afgelopen maanden op verschillende plekken de belofte *"AI met geheugen"* tegengekomen — in een productbeschrijving, in een rapport, in een strategie-document. De belofte klinkt overal hetzelfde. De architectuur eronder is dat niet. Onder hetzelfde label werken op dit moment **vier compleet andere architecturen**, en die gedragen zich op de twee KPI's die u écht volgt totaal verschillend: *wordt het systeem beter naarmate we het gebruiken*, en *kunnen we het meenemen als we het systeem ooit vervangen?*

Drie van die vier zijn een kostenpost. U koopt ze opnieuw en opnieuw, ze stapelen geen waarde op, en u kunt ze niet meenemen. **Eén is een kapitaalinvestering.** Ze wordt beter, ze blijft van u, en haar waarde groeit met elke maand dat ze bij u werkt. Twee eenvoudige sollicitatievragen zijn voldoende om te onderscheiden welke u eigenlijk koopt.

## Even voor de helderheid — wat is "AI" hier eigenlijk?

Een AI-model — denkt u aan ChatGPT, Copilot, Gemini, of de AI-assistent in uw CRM — is in essentie statistische tekstgeneratie. Erg slim met taal, maar geen werknemer die *uit zichzelf* leert of onthoudt. Zodra een sessie eindigt, is alles wat het systeem net wist weg.

Het "geheugen" dat in al die producten en strategieën wordt beloofd zit dus nooit in het model zelf. Het zit altijd in iets dat *eromheen* is gebouwd. En daar valt te kiezen — uit vier architectuur-varianten. De rest van dit artikel bespreekt die varianten als vier nieuwe medewerkers die u zou kunnen aannemen. AI is geen medewerker; voor de discussie hier werkt het beeld.

## De vier medewerkers — even kennismaken

Vier kandidaten, vier verschillende werkwijzen, één label op hun CV.

**Medewerker 1 — De stagiair met geweldig kort-termijngeheugen.** Tijdens een gesprek onthoudt ze elk detail. Ze leest mee, ze stelt scherpe vervolgvragen, ze houdt twintig openstaande draadjes uit elkaar. Zodra het gesprek eindigt, is alles weg. Morgen begint ze blanco.

**Medewerker 2 — De stagiair met een uitstekend doorzoekbaar archief.** Ze beschikt over een grote kast met alle bedrijfsdocumenten en kan binnen seconden het juiste stuk vinden. Maar ze leest dat stuk *bij elke vraag opnieuw*. Wat ze gisteren las, is morgen geen kennis — alleen een vindplaats.

**Medewerker 3 — De medewerker met een organogram in haar hoofd.** Ze weet wie wat doet, hoe processen op elkaar aansluiten, welke leverancier bij welk product hoort, welke klant bij welk contract. U vraagt iets over een proces, ze kan de keten volgen. Voorvereiste: ú heeft haar eerst dat organogram geleerd.

**Medewerker 4 — De medewerker die haar eigen handboek bijhoudt.** Ze leest dezelfde stukken die medewerker 2 leest, maar ze schrijft conclusies uit, koppelt feiten aan elkaar, markeert tegenstrijdigheden tussen wat ze vorige maand las en wat ze deze week leest. Volgende keer dat hetzelfde onderwerp ter sprake komt, hoeft ze niet meer het archief in — ze pakt haar handboek.

Deze cast loopt door de rest van het artikel. We bekijken ze twee keer, telkens vanuit één van de twee sollicitatievragen.

## Pijler 1: slechts één van de vier wordt béter naarmate u haar inhuurt

Dit is de eerste vraag die u in elk regulier sollicitatiegesprek stelt: *wordt deze persoon na drie maanden sneller, preciezer, goedkoper?* Of doet ze op dag 90 nog exact hetzelfde werk als op dag 1, met hetzelfde tempo?

**Medewerker 1**: na vrijdag is ze alles vergeten. Maandag begint ze blanco aan een nieuwe week. Beter na drie maanden? Nee. Er ís geen drie maanden — alleen een serie losse vrijdagen.

**Medewerker 2**: leest deze week dezelfde stukken als zes maanden geleden, net zo langzaam, met net zoveel kans om de samenhang te missen. Haar archief groeit — haar kennis niet. Een vakgenoot in deze hoek (de bekende AI-ingenieur Andrej Karpathy) verwoordde het zo: *"medewerker 2 leest voor elk tentamen het hele boek opnieuw door."* Beter? Nee.

**Medewerker 3**: ze wordt beter, mits ú haar organogram blijft bijwerken. Komt er een nieuwe afdeling bij, een nieuwe leverancier, een gewijzigd proces — dan moet u haar dat leren. Het organogram leert *zichzelf* niet bij. Beter uit zichzelf? Nee.

**Medewerker 4**: haar handboek wordt elke week dikker, beter doorzoekbaar, en — cruciaal — beter *gekoppeld*. Een nieuw document raakt vijftien bestaande hoofdstukken; ze werkt al die hoofdstukken bij, markeert wat afwijkt van wat ze eerder schreef, en sluit het in. Op dag 90 antwoordt ze sneller en met meer onderbouwing dan op dag 1. Karpathy's analogie weer, ditmaal omgekeerd: *"medewerker 4 maakt na elk boek een hoofdstuk in haar handboek."* Beter? **Ja.**

Drie van de vier staan stil. Eén stapelt op. Dat is geen detail van de techniek — dat is een fundamenteel verschil in *welk soort medewerker* u in huis haalt.

> *[search-wiki.gif hier — onderschrift: "Dit is laag 1 — het handboek zelf. Een map met markdown-bestanden, geopend in een browser, doorzoekbaar door een mens. Zo zien uw mensen het. Onderaan dit artikel ziet u laag 2: een tweede AI die hetzelfde handboek op vraag raadpleegt en met antwoord plús bronnen terugkomt."]*

## Pijler 2: slechts één van de vier kunt u méénemen als u het systeem ooit vervangt

De tweede sollicitatievraag stelt elke directie vroeg of laat: *als u opzegt, neemt u uw kennis dan mee — of blijft die bij ons?* In HR-termen: hoe groot zijn de overdrachtsrisico's bij uitstroom? In architectuur-termen: hoe vrij staat u om dit systeem ooit te vervangen?

**Medewerker 1**: u kunt haar gesprek niet eens meenemen naar morgen, laat staan naar een ander systeem. Het gesprek leeft tijdens het gesprek — er is niets om mee te nemen. Mee te nemen? Architectonisch onmogelijk.

**Medewerker 2**: haar archief en haar embeddings kunt u in principe meenemen — *mits* ze op open componenten draait die u zelf host. In de turnkey-implementaties die u het vaakst krijgt aangeboden, draait de retrieval-laag bij een derde partij. Wat ze daar geleerd heeft over hoe ú zoekt — welke vragen u stelt, welke prioriteiten u heeft — blijft achter. Mee te nemen? Mits u 'm zelf op open componenten heeft gebouwd.

**Medewerker 3**: haar organogram kan op een open standaard draaien — dan is een overstap probleemloos. Maar de meeste implementaties draaien op platform-eigen formaten en query-talen; migratie wordt dan een project. Mee te nemen? Mits u voor een open standaard heeft gekozen.

**Medewerker 4**: haar handboek is een map met platte tekstbestanden. Geen database, geen platform-eigen formaat, geen abonnement op iets dat nodig is om de tekst te lezen. U kunt 'm meenemen op een USB-stick — en dat is geen engineering-keuze die u nog moet maken; het is wat ze *is*. Mee te nemen? **Ja, triviaal — uit zichzelf, niet na een migratieproject.**

Het verschil zit dus niet in *of* u haar mee kunt nemen — alle drie middelste opties kunnen worden meegenomen, mits u de juiste open componenten kiest. Het verschil zit in *wat u ervoor moet doen*: bij medewerker 4 hoeft u niets te doen, bij medewerker 2 en 3 is het een actieve engineering-keuze, en bij medewerker 1 is het architectonisch onmogelijk. Onder medewerker 4 is portabiliteit een eigenschap van haar architectuur; onder medewerker 2 en 3 is het een eigenschap van uw inkoopkeuze.

Een vakgenoot bij een specialistisch bedrijf in deze hoek (Tomaz Bratanic, werkzaam bij Neo4j) schreef het deze maand in één zin op: *"als u uw geheugen niet bezit, bezit u uw AI niet. Elke AI-omgeving bouwt zijn eigen ommuurde tuin."* Bij drie van de vier architecturen kost het u een engineering-keuze of -project om uit die ommuurde tuin te komen. Bij één is de tuin er nooit geweest.

En één detail dat hierbij hoort: wat u meeneemt is niet alleen *waar ze nu staat*, maar ook *hoe ze daar gekomen is*. Elke wijziging in haar handboek is gedateerd, gemotiveerd, en — als ze van mening veranderd is — gekoppeld aan de oudere conclusie die ze heeft vervangen. U kunt haar vragen *waarom* ze nu iets anders zegt dan in maart, en ze laat het u zien. Een audit trail die u by default krijgt — bij de andere drie moet u 'm zelf opbouwen, áls het architectonisch al kan.

## Twee pijlers, één conclusie

Twee sollicitatievragen. Vier medewerkers. Drie keer twee keer *nee*. Eén keer twee keer *ja*.

Medewerker 4 is de enige die op beide vragen positief scoort. De andere drie zijn — in MT-taal — een **kostenpost**: u koopt ze opnieuw en opnieuw, ze stapelen geen waarde op, u kunt ze niet meenemen. Medewerker 4 is een **kapitaalinvestering**: ze wordt elke maand meer waard, en haar waarde blijft van u.

Dit is wat *"AI met geheugen"* zou móéten betekenen. In drie van de vier architecturen op de markt betekent het iets anders.

## Eerlijk over waar medewerker 4 stukbreekt

Medewerker 4 klinkt — terecht — als de duidelijke winnaar. Maar geen architectuur is perfect, en we tonen hier ook eerlijk de zwakke kanten. Drie kanttekeningen, in MT-taal:

- **Plafond bij ongeveer honderd onderwerpen.** Daarboven past haar handboek niet meer in haar werkgeheugen. Voor de grootste corpora heeft u dan medewerker 2 onder haar nodig — geen vervanging, een samenwerking. Bij MKB-schaal komt u dit plafond zelden tegen; bij enterprise-schaal wel.
- **Een verkeerde conclusie wordt door iedereen klakkeloos overgenomen.** Schrijft ze op woensdag iets fouts in haar handboek? Maandag, woensdag, en de drie maanden erna citeert ze die conclusie als feit. Een AI-architect die dit patroon onlangs nuchter beschreef: *"georganiseerde, hardnekkige fouten zijn moeilijker te zien dan losse fouten."* Periodieke controle is dus geen luxe; het is haar onderhoud. De gangbare aanpak: medewerker 4 leest maandelijks haar eigen handboek door, markeert tegenstrijdigheden tussen pagina's, signaleert claims die door één bron worden gedragen waar er ondertussen meerdere bestaan, en stelt voor — niet uitvoert — welke conclusies herzien moeten worden. *Voorstelt*. De beslissing blijft bij u.
- **Inwerken is duur.** Elk nieuw document kost haar significant meer tijd dan medewerker 2 erover doet — medewerker 4 doet immers méér: lezen, samenvatten, koppelen, tegenstrijdigheden zoeken, vijftien hoofdstukken bijwerken. Bij snel veranderende data (een live-prijslijst, een dagelijkse voorraadstand) kiest u medewerker 2.

Geen van die drie ondergraaft de keuze. Ze kalibreren 'm. Medewerker 4 is een investering, en u kent de onderhoudsplicht die bij elke investering hoort.

## De namen onder elke medewerker — voor wie de termen in pitches en rapporten wil herkennen

U heeft nu de vier medewerkers en hun twee sollicitatievragen gezien. Voor wie zometeen in een vendor-rapport, een LinkedIn-post of een strategie-document de échte vaktermen tegenkomt — hier is de naam onder elke medewerker, plus wat marketing-taal die u erbij kunt horen.

- **Medewerker 1 = Contextvenster** (Engels: *context window*). Het werkgeheugen waar een AI-model in werkt tijdens één gesprek. ChatGPT, Copilot en Claude hebben allemaal een contextvenster. Marketing noemt dit vaak *"200K tokens context"* of *"1M tokens context"* — het is een werkgeheugen, geen kennislaag. Bij elke nieuwe sessie weer leeg.
- **Medewerker 2 = RAG** (Engels: *Retrieval-Augmented Generation*, soms: *"agentic search"* of *"semantic search"*). Het patroon waarin een AI-model bij elke vraag eerst documenten ophaalt uit een zoekindex en daarna een antwoord schrijft op basis van die documenten. Onder de motorkap: tekst wordt in stukken geknipt, omgezet in numerieke vectoren, en opgeslagen in een *vector-database* (een ander vakterm waar u dezelfde techniek mee benoemd ziet). Bij een vraag worden de stukken met de meest *vergelijkbare* vector teruggegeven. Verreweg het meest verkochte *"AI met geheugen"*-patroon. **Eén opmerking over jargon-bewegingen**: in het vakveld klinkt sinds april–mei 2026 dat *"RAG dead is"*. Drie deskundigen (Karpathy, Sathish Raju, en Jeff Huber — de CEO van Chroma, een leverancier van vector-databases) zijn het erover eens dat het **de term** is die op sterven ligt, niet de techniek. Huber: *"if you ask 25 people to define RAG, they'll all define it a slightly different way — banned."* De voorgestelde vervang-term is *context engineering*. U bent dus voor de tweede keer in een jaar bezig getuige te zijn van een rebranding van dezelfde techniek.
- **Medewerker 3 = Knowledge graph** (soms ook: *kennisgraaf*, *enterprise knowledge fabric*, *semantische datalaag*). Een gestructureerde "kaart" van entiteiten (mensen, producten, klanten, processen) en de getypeerde relaties tussen die entiteiten — *werkt-voor*, *onderdeel-van*, *geleverd-door*, *contract-met*, enzovoort. Een AI-model gebruikt zo'n kaart om feiten en relaties op te zoeken zonder ze te hoeven verzinnen. Vereist een *ontologie* — uw team moet eerst formeel definiëren wie-wat is en hoe alles samenhangt. Zonder die discipline vooraf wordt het organogram inconsistent en raken antwoorden vaag.
- **Medewerker 4 = LLM Wiki** (ook: *compiled wiki*, *agent memory*, *knowledge compilation*). Een markdown-wiki die door een AI-model wordt geschreven en onderhouden — de synthese gebeurt bij het opnemen van een nieuwe bron, niet bij elke vraag. Op dit moment vooral indie-built; zelden vendor-aangeboden. Het patroon is op 4 april 2026 benoemd door Andrej Karpathy in een GitHub-notitie die 17 miljoen lezers trok. Onder de motorkap: een map tekstbestanden, version control, een AI die ze bijwerkt en kruislinks legt, en een tweede AI die ze op vraag raadpleegt — precies de twee lagen die u in §B-closer hieronder in actie ziet.

Drie van deze termen zult u vaker zien in aanbiedingen; de vierde (LLM Wiki) is op dit moment vooral indie-built en zelden vendor-aangeboden. **Welke term in een aanbieding aan u staat, zegt iets over welke medewerker u in feite krijgt.** En welke aanbieder een nieuwe term verzint voor een bestaande techniek, vertelt u iets over hoe nieuw die techniek écht is.

Voor wie nog dieper wil: het implementatieplan van het LLM Wiki-patroon onder dit artikel noemt negen feature-clusters die boven Karpathy's basale notitie uitstijgen — onder andere lifecycle-metadata, automation-hooks, kwaliteitscontrole met een tweede AI als beoordelaar, en scope/privacy per pagina. De volledige spec staat in de repository hieronder.

## Twee lagen: het handboek én de collega-AI die het op vraag raadpleegt

Op 4 april 2026 plaatste Andrej Karpathy — voormalig hoofd AI bij Tesla, mede-oprichter van OpenAI — een notitie op GitHub. Geen product, geen paper. Een notitie van een paar pagina's. **17 miljoen mensen** lazen die notitie in de eerste week, 5.000 maakten 'm tot favoriet, 4.282 kopieerden 'm naar hun eigen account.

Het idee: laat de AI haar eigen handboek bijhouden in plaats van elk document opnieuw lezen. Medewerker 4 in plaats van medewerker 2.

Karpathy gebruikt het zelf nog steeds. Eind april stond hij op het podium van Sequoia AI Ascent (een belangrijke industrie-conferentie) en bevestigde dat hij elke ochtend zijn eigen leeswerk door zo'n handboek laat verwerken: *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles, and I love asking questions about things."* Iedere keer dat hij dezelfde informatie van een andere kant bekijkt, voegt hij toe: *"I always feel like I gain insight."*

Zes weken geleden ben ik er voor mezelf mee begonnen. En het is belangrijk te zien dat dit eigenlijk niet één gebouwd ding is, maar twee — twee afzonderlijke lagen die u in dit stuk allebei in actie ziet:

- **Laag 1: het handboek zelf.** Een map met markdown-tekstbestanden. Geen database, geen platform-eigen formaat, geen abonnement nodig om de tekst te kunnen lezen. U opent 'm in elke teksteditor, doorzoekt 'm in elke browser, en version-controleert 'm met dezelfde tools waar uw ontwikkelaars al mee werken. Dit is wat u onder pijler 1 in het eerste filmpje zag. Drie eigenschappen die u in de pijler-discussie nog niet zag maar die voor een MT relevant zijn:
   - *Audit trail per claim.* Elke pagina draagt een datum van laatste bevestiging, een telling van de onderbouwende bronnen, en een betrouwbaarheidsscore. Vervangen claims blijven bestaan met een verwijzing naar wat ze opvolgt — niets wordt stilletjes weggegooid.
   - *Scope per pagina.* Eén markering bovenaan elke pagina zegt: deze is intern, die mag publiek. De publieke uitgave laat de interne pagina's niet zien; medewerker 4 zelf kan ze nog wel raadplegen. Compliance-vriendelijk zonder dubbel werk.
   - *Zelfreview op afroep.* Medewerker 4 kan op aanvraag haar eigen handboek doorscannen op contradicties, verouderde claims, en pagina's waar niemand meer naar verwijst. Ze stelt herzieningen voor; u keurt goed.
- **Laag 2: een collega-AI die het handboek op vraag raadpleegt.** Een afzonderlijke agent — *niet* dezelfde AI als degene die het handboek schreef. Deze tweede AI neemt mijn vraag aan, zoekt de relevante hoofdstukken op, schrijft een antwoord, en levert daarbij **de pagina's uit het handboek waarop het antwoord is gebaseerd** — klikbaar, controleerbaar, traceerbaar tot op de bron.

Deze tweede laag is meer dan een sfeer-demo. Het bewijst twee dingen die elders in dit artikel alleen als belofte stonden:

- **De portabiliteits-claim wordt hardgemaakt.** Het handboek is niet alleen *theoretisch* meenbaar (platte tekst, open formaat). Het wordt *al feitelijk* gelezen door een tweede AI op een ander platform dan degene die het schreef. Lock-in is afwezig in een werkende keten, niet alleen op papier.
- **Auditbaarheid wordt zichtbaar.** Vraag het iedere andere AI-assistent op de markt — u krijgt een antwoord. Vraag het deze tweede AI — u krijgt een antwoord plús de drie wiki-pagina's waar het antwoord op gebaseerd is. *Dat* is wat een MT zou moeten verwachten als hij voor "AI met geheugen" betaalt.

Open formaat, geen abonnement, geen lock-in. Open source. Repo: [businessdatasolutions.github.io/ai-wiki](https://businessdatasolutions.github.io/ai-wiki). Klik door, lees mee, of vraag uw eigen ontwikkelaar er een kwartier naar te kijken.

> *[agent-wiki.gif hier — onderschrift: "Dit is laag 2 in actie. Links de vraag van de gebruiker. Rechts het antwoord van de tweede AI. Eronder de wiki-pagina's waaruit het antwoord is opgebouwd — klikbaar, controleerbaar. Een collega-AI raadpleegt laag 1 (het handboek) op vraag en komt terug met synthese plús bronnen."]*

## Maandagochtend-vraag

Als u één architectuurvraag stelt over uw AI-systeem deze week, stel deze:

> *"Wordt het 'geheugen' van dit systeem beter naarmate we het gebruiken — en als we het systeem over twaalf maanden vervangen, kunnen we het geheugen meenemen?"*

Drie van de vier architecturen kunnen daar geen eerlijk *ja* en *ja* op leveren. Bij de vierde is het antwoord triviaal: *ja* en *ja*. Want het zit in een map met tekstbestanden waar u zelf bij kan.

Welke van de vier architecturen draait er bij u eigenlijk?

---

**Bronnen voor wie verder wil lezen.** De geconsolideerde wiki-versie van dit artikel staat op de open-source repository hierboven, met getypeerde citaten naar de oorspronkelijke bronnen: Karpathy's GitHub-notitie van 4 april 2026; Sathish Raju's *RAG Isn't Dead* op Medium (16 april); Yanli Liu's vergelijkende architectuur-analyse op AI Advances (27 april); Tobias Martin van SurrealDB over knowledge graphs (27 april); Jeff Huber van Chroma op Mastra over RAG-de-term-niet-de-techniek (11 mei); Tomaz Bratanic op Towards Data Science over harness-portabele geheugen (8 mei); Karpathy's keynote op Sequoia AI Ascent (29 april).
