## Redactierapport — linkedin-post-mt-vier-mechanismen-ai-geheugen.md

**Datum redactie:** 2026-05-11

### Taalwijzigingen

| # | Locatie | Origineel | Gecorrigeerd | Reden |
|:--|:--------|:----------|:-------------|:------|
| 1 | §Pijler 2, alinea Medewerker 2 (regel 86) | …wat ze de afgelopen maanden **gelééd** heeft over hoe ú die documenten gebruikt… | …wat ze de afgelopen maanden **geleerd** heeft over hoe ú die documenten gebruikt… | Spelling — *"gelééd"* is geen Nederlands woord; de bedoelde vorm is *"geleerd"*. Geïsoleerde tikfout, geen patroon |
| 2 | §Wat is "AI" eigenlijk (regel 46) | Zodra een sessie eindigt, is wat het systeem net wist**,** weg. | Zodra een sessie eindigt, is **alles** wat het systeem net wist weg. | Zinsstructuur — de twee komma's framen een onderwerp-bijzin maar laten het zinseinde stoten ("…wist, weg"). De toevoeging *"alles"* maakt het onderwerp expliciet en haalt de tweede komma weg; de zin valt vloeiend uit zonder verlies van betekenis |
| 3 | §Pijler 2, openingsalinea (regel 82) | hoe groot zijn de **overdrachts-risico's** bij uitstroom? | hoe groot zijn de **overdrachtsrisico's** bij uitstroom? | Spelling — gangbaar Nederlands schrijft samenstellingen tussen twee zelfstandige naamwoorden zonder koppelteken (*overdrachtsrisico*, één woord). Koppelteken alleen wanneer leesbaarheid daadwerkelijk verbetert; hier niet |
| 4 | §Twee lagen, alinea Karpathy Sequoia (regel 124) | Iedere keer dat hij dezelfde informatie van een andere kant bekijkt, **schrijft hij**: *"I always feel like I gain insight."* | Iedere keer dat hij dezelfde informatie van een andere kant bekijkt, **voegt hij toe**: *"I always feel like I gain insight."* | Zinsstructuur — beide aanhalingen komen uit Karpathy's gesproken keynote op Sequoia AI Ascent; *"schrijft hij"* suggereert ten onrechte een geschreven bron. *"Voegt hij toe"* blijft binnen de gesproken context |
| 5 | §Twee lagen, brug-alinea (regel 126) | …twee afzonderlijke lagen die u in **deze post** allebei in actie ziet… | …twee afzonderlijke lagen die u in **dit stuk** allebei in actie ziet… | Anglicisme — *"post"* (uit *post* / *blogpost*) is in social-media-context ingeburgerd, maar in een lopende zin van een zakelijk LinkedIn-artikel is *"dit stuk"* of *"dit artikel"* natuurlijker en consistent met het gebruik elders in de tekst |
| 6 | §Twee lagen, Laag 1-alinea (regel 128) | …die voor een **MT-koper** relevant zijn: | …die voor een **MT** relevant zijn: | Zinsstructuur / consistentie — de samenstelling *"MT-koper"* introduceert een koop-frame dat eerder in deze redactieronde juist uit de tekst is gehaald (architectuur-reframe). *"MT"* volstaat en past bij de architectuur-positionering |
| 7 | §Pijler 1 GIF-onderschrift (regel 78); §Twee lagen kop (regel 118); Laag 1 (regel 128); Laag 2 (regel 132); §Wat dit bewijst (regel 134); §B-closer GIF-onderschrift (regel 141) | **artifact** / **Artifact** / **artifacts** (8 vermeldingen totaal) | **laag** / **Laag** / **lagen** | Anglicisme — *"artifact"* is een Engels leenwoord; het Nederlandse *"artefact"* draagt in het algemene taalgebruik vaak de bijbetekenis van *ongewenst bijproduct*. De auteur introduceert het concept zelf al als *"twee afzonderlijke lagen"* (regel 126); het label *"Laag 1 / Laag 2"* sluit aan op die zelfgeformuleerde framing en op architectuur-vocabulaire dat een MT-publiek herkent |
| 8 | §Maandagochtend-vraag, voorlaatste zin (regel 149) | Drie van de vier architecturen kunnen daar geen eerlijk ***ja-en-ja*** op leveren. Bij de vierde is het antwoord triviaal: ***ja* en *ja***. | Drie van de vier architecturen kunnen daar geen eerlijk ***ja* en *ja*** op leveren. Bij de vierde is het antwoord triviaal: ***ja* en *ja***. | Zinsstructuur — binnen dezelfde alinea kwam de uitdrukking *"ja en ja"* in twee verschillende cursiveringen voor (één gekoppeld met verbindingsstreepjes, één met losse italics). Geharmoniseerd op de tweede vorm; ritme van de slotzin verbetert en typografische consistentie hersteld |
| 9 | §Pijler 2, vier slotvragen onder Medewerker 1–4 (regels 84, 86, 88, 90) | **Meenbaar?** | **Mee te nemen?** | Niet-gangbaar woord — *"meenbaar"* staat niet in Van Dale; *"meeneembaar"* wél, maar wordt door de auteur als geforceerd ervaren in zakelijk-Nederlandse publicatietoon. *"Mee te nemen?"* (drie woorden, één geheel) sluit aan op het werkwoord *"meenemen"* dat door pijler 2 heen wordt gebruikt en blijft punchy genoeg voor het slotvraag-patroon. Vier vervangingen, één logische correctie. (Geconstateerd in een tweede leesronde — gemist in de eerste pass omdat het patroon zich herhaalt en consistent leek.) |

**Aantal wijzigingen:** 9 logische correcties (regels 7 en 9 dekken elk meerdere individuele tekstvervangingen)
**Oordeel:** Kleine correcties (twee tikfouten/niet-gangbare woorden, één compoundvorm, drie zinsstructuur-verbeteringen, twee anglicismen, één consistentie-correctie). Geen structurele heroverweging van inhoud, claims of argumentatie

### Inhoudelijke revisie pijler 2 — auteursrevisie, geen redactionele correctie

Buiten de taalkundige correcties hierboven heeft de auteur in een vervolgsessie besloten de inhoudelijke claims van pijler 2 te nuanceren. De aanleiding: de antwoorden *"Nee"* (medewerker 2) en *"Met moeite"* (medewerker 3) waren architectonisch te scherp gesteld. Een RAG-implementatie op open componenten en een knowledge graph op een open standaard *kunnen* portable zijn — alleen niet by default in de gangbare commerciële implementaties.

De herziene pijler 2 onderscheidt nu twee verschillende eigenschappen:
- *By default meeneembaar* (medewerker 4 — eigenschap van haar architectuur);
- *Meeneembaar mits engineering-keuze* (medewerker 2 en 3 — eigenschap van uw inkoopkeuze);
- *Architectonisch onmogelijk* (medewerker 1 — sessies leven per definitie lokaal).

Concrete wijzigingen die hieruit voortvloeien (niet als redactie geteld omdat het auteursrevisie van de claims betreft, niet correctie van taal):
- M1 slotantwoord: *"Nee"* → *"Architectonisch onmogelijk"*
- M2 paragraaf-body: herschreven om het *"mits open componenten"*-pad expliciet te benoemen
- M3 paragraaf-body: herschreven om het *"mits open standaard"*-pad expliciet te benoemen
- M4 slotantwoord: *"Ja, triviaal"* → *"Ja, triviaal — uit zichzelf, niet na een migratieproject"*
- Nieuwe alinea toegevoegd tussen medewerker-paragrafen en de Bratanic-quote, die de as *by default meeneembaar / mits engineering-discipline / architectonisch onmogelijk* expliciet maakt
- Slotzin pijler 2 ("…laten u die ommuurde tuin niet uit. Eén wel.") herschreven naar *"Bij drie van de vier kost het u een engineering-keuze of -project om uit die ommuurde tuin te komen. Bij één is de tuin er nooit geweest."*
- Audit-trail-zin in pijler 2 herschreven om dezelfde nuance op te nemen.

Deze revisie versterkt de governing thought (*drie kostenposten, één kapitaalinvestering*) in plaats van haar te ondergraven — het inzicht *"by default vs mits engineering"* is precies waarom medewerker 4 architectonisch onderscheid maakt.

### Inhoudelijke uitbreiding §8 — didactische slotsectie (auteursrevisie, geen redactionele correctie)

De auteur heeft daarnaast besloten dat het stuk uiteindelijk wel de vaktermen moet uitleggen die er in de hoofdtekst opzettelijk uit zijn gelaten — *contextvenster*, *RAG*, *knowledge graph*, *LLM Wiki* — zodat MT-lezers ze in vendor-pitches, rapporten en strategie-documenten kunnen herkennen.

Concrete wijziging: §8 is vervangen. De voormalige sidebar *"Voor de vakgenoot-curieus: het *RAG is dead*-debat in één alinea"* (~140 woorden) is vervangen door een volwaardige didactische sectie *"De namen onder elke medewerker — voor wie de termen in pitches en rapporten wil herkennen"* (~500 woorden). De RAG-is-dead-noot is niet weggehaald maar geïntegreerd onder de uitleg van Medewerker 2, op de plek waar ze functioneel het beste landt.

De vier vaktermen worden per medewerker geïntroduceerd met (1) de Nederlandse en Engelse term, (2) een korte werkings-uitleg in MT-taal, (3) gangbare marketing-frasen waaraan de lezer ze kan herkennen, en (4) waar relevant: vermeldingen van rebranding-bewegingen in het vakveld. De v2-implementatieplan-verwijzing uit de oude §8 is bewaard als afsluitende noot voor wie nog dieper wil.

Effect op het stuk:
- Lengte volledig artikel groeit van ~2.000 naar ~2.350 woorden;
- De frontmatter-omschrijving van het publiek is aangescherpt: *"jargon-vrij in de hoofdargumentatie, vaktermen opzettelijk geïntroduceerd in de didactische slotsectie"*;
- De governing thought + twee pijlers + medewerker-metafoor blijven onaangetast — de didactische sectie zit *na* de eerlijke kanttekening en *vóór* de B-closer, op een plek waar de inhoudelijke argumentatie al is geland en de lezer ruimte heeft voor service-materiaal.

### Structuuranalyse (advies)

Bevindingen tegen het McKinsey Pyramid Principle. Geen wijzigingen aangebracht in de tekst — de auteur beslist of en hoe hij deze observaties verwerkt.

**SCQA-opening:** Herkenbaar en correct uitgespeeld.
- **Situation**: *"U bent de afgelopen maanden op verschillende plekken de belofte 'AI met geheugen' tegengekomen — in een productbeschrijving, in een rapport, in een strategie-document."* — een onbetwistbare context die de doellezer (MT/CEO) deelt.
- **Complication**: *"De belofte klinkt overal hetzelfde. De architectuur eronder is dat niet. Onder hetzelfde label werken op dit moment vier compleet andere architecturen…"* — de spanning is helder en wordt direct verbonden aan de twee KPI's die de lezer al volgt (compounding + portabiliteit).
- **Question** (impliciet, niet uitgespeld): welke van de vier architecturen draait er bij mij, en past die bij wat ik nodig heb? De lezer kan die vraag zelfstandig formuleren — zoals de skill voorschrijft voor zakelijke publicatieformaten.
- **Answer / governing thought**: *"Drie van die vier zijn een kostenpost. Eén is een kapitaalinvestering. Twee eenvoudige sollicitatievragen zijn voldoende om te onderscheiden welke u eigenlijk koopt."* — uitgespeld in de tweede alinea, niet verstopt in een latere bullet of slotzin.

Dit is precies de SCQA-discipline die de skill noemt als ideaal voor publicatieformaten en die ontbrak in eerdere drafts uit dezelfde lijn.

**Governing thought en supporting arguments:** Helder gestructureerd.
- De governing thought (*"drie kostenposten, één kapitaalinvestering — twee eigenschappen onderscheiden welke u koopt"*) staat **boven** de twee supporting arguments, niet erin verstopt.
- Twee supporting arguments (pijler 1: *"slechts één wordt beter naarmate u haar inhuurt"* en pijler 2: *"slechts één kunt u meenemen als u het systeem vervangt"*) zijn MECE op de governing thought: compounding en portabiliteit zijn de twee onafhankelijke eigenschappen die *"kapitaalinvestering"* van *"kostenpost"* onderscheiden. Geen overlap, geen leemte.
- Het aantal (twee) is bewust kleiner dan de McKinsey-richtlijn van drie; in dit geval is dat correct omdat de kapitaalinvestering-claim precies twee onafhankelijke dimensies kent. Een derde pijler zou de structuur dilueren.

**Horizontale en verticale logica:** Beide lagen kloppen.
- **Verticale logica**: onder elke pijler staan vier medewerker-paragrafen die elk de pijler-claim erboven beantwoorden ("wordt deze medewerker beter?" / "kunt u haar meenemen?"). Onder de B-closer staan twee bewijzen (portabiliteit + auditbaarheid) die de pijler-claims daarboven hardmaken. De vraag-en-antwoord-dialoog klopt op elk niveau.
- **Horizontale logica**: de vier medewerker-paragrafen binnen elke pijler hebben identieke openings-grammatica (*"Medewerker N: [evidence]. Beter / Meenbaar? [Ja/Nee]"*). Pijler 1 en pijler 2 zijn parallel-gestructureerd ("Slechts één van de vier… de andere drie…"). Binnen §9 zijn Laag 1 en Laag 2 als pendanten gepresenteerd. Het stuk wisselt niet tussen inductief en deductief halverwege.

**Concrete suggesties** — twee observaties, geen interventies. De redacteur signaleert; de auteur beslist:

- **§Vakgenoot-curieus (de "RAG is dead"-sidebar) onderbreekt het ritme licht.** Het stuk loopt van §Twee pijlers, één conclusie (§6, de brug terug naar de governing thought) naar §Eerlijk over waar medewerker 4 stukbreekt (§7, de eerlijke kanttekening) — beide functioneel voor de pyramid. Daarna komt §8 als jargon-rijke sidebar voor een ander publiek dan de hoofdtekst bedient, en pas dan §9 met de B-closer. Een lezer in *"MT-modus"* die de governing thought heeft opgenomen, kan in §8 even verloren raken voordat de demonstratie volgt. Twee opties die de auteur kan overwegen:
  - *Optie A — laten staan.* De sidebar is bewust gemarkeerd als optioneel-voor-de-vakgenoot; lezers die haar overslaan verliezen niets van de hoofdargumentatie.
  - *Optie B — schrappen of verplaatsen naar onderaan, na de Bronnenlijst.* Houdt de hoofdlijn (SCQA → pijlers → brug → eerlijke kanttekening → B-closer → maandagochtend-vraag) ononderbroken en bedient de vakgenoot in een aparte voettekst.
- **§9 B-closer is substantieel** (~400 woorden, met Karpathy-lineage + Laag 1 + Laag 2 + bewijs-bullets + repo-link + GIF-onderschrift). Sommige lezers ervaren dit als een tweede argumentatie-passage naast de pijlers, niet als afsluitende demonstratie. Mogelijk te overwegen:
  - Splits §9 in twee: één korte sectie *"Twee lagen — wat ik bouwde"* (Karpathy-lineage + Laag 1 + Laag 2 + GIF) en één korte sectie *"Wat dit tweede laag bewijst"* (portabiliteit + auditbaarheid + repo-CTA). Twee korte secties lezen vaak lichter dan één lange.
  - Of behoud zoals het is — de huidige opzet honoreert de feedback-ronde die de tweedeling tussen wiki-als-substraat en agent-als-koppeling expliciet vroeg, en de lezer krijgt het bewijs op de plek waar hij de claims net heeft gehoord.

**Structureel oordeel:** Volgt herkenbaar het Pyramid Principle. SCQA-opening klopt, governing thought staat boven de structuur, twee MECE-pijlers met parallel-grammar evidence, verticale en horizontale logica intact. De twee structurele observaties hierboven zijn ritmische optimalisaties, geen substantiële heroverwegingen.
