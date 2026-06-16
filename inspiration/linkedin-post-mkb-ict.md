---
persona: "Stefan (38) — IT-manager / 'de IT-man', MKB 60-150 fte, één- of tweemansafdeling, rapporteert aan COO/eigenaar"
audience: MKB-ICT (IT-managers, system engineers, hoofd ICT)
versions:
  - A — vakinhoudelijk paradigma-essay
  - B — open brief / hot take
  - C — stap-voor-stap micro-tutorial
cta: live wiki in eerste comment (https://businessdatasolutions.github.io/ai-wiki/)
---

# MKB-ICT (persona: Stefan) — drie versies

---

## Versie A — Vakinhoudelijk paradigma-essay

**Het is geen RAG. Het is geen low-code. Het is iets waarvoor we nog geen goede naam hebben.**

Andrej Karpathy publiceerde zijn nieuwste "project" niet als code, maar als één markdown-bestand. Daarin staan het ontwerp, de architectuur en de werking. Geen repo. Geen demo. Eén specificatie.

Wat opvalt vanuit architectuurperspectief:

De specificatie is dé bron van waarheid. Niet de code. Refactoren betekent: specificatie aanpassen, opnieuw genereren. Code-review verschuift naar specificatie-review. Drie heldere lagen: schema (de specificatie) → wiki/output (gegenereerd, regenereerbaar) → bron (immutable). Eén verantwoordelijkheid per laag.

Voor MKB-ICT met één hoofdleverancier verandert dit de machtsbalans. Wie de specificatie bezit, bezit het systeem. De leverancier wordt uitvoerder, geen kennishouder. Onderschat die uitspraak niet.

Ik heb het patroon dit weekend uitgeprobeerd. Karpathy's specificatie gekopieerd, Claude er een onderzoekswiki uit laten opbouwen. 4,5 uur van eerste commit tot live op GitHub Pages, acht bronnen verwerkt, cross-references onderhouden zichzelf.

De interessante vraag is niet "wordt code achterhaald?" Die vraag stelden mensen ook over assembler.

De vraag is: welke laag van ons werk wordt straks de specificatie, en welke laten we genereren?

Live wiki in de eerste comment. Repo erbij — de specificatie staat letterlijk in CLAUDE.md.

Wie bij jullie schrijft op dit moment feitelijk de specificatie — jij, of de leverancier?

#ITArchitectuur #AI #MKB

---

## Versie B — Open brief / hot take

**Aan elke IT-manager in een MKB die volgend kwartaal weer "iets met AI" voorgeschoteld krijgt:**

Ik weet hoe het loopt.

Het MT komt met een vage opdracht. Geen budget, geen richting, wel een deadline. Marketing gebruikt al ChatGPT, sales draait Notion AI, niemand vraagt jou. Je hoofdleverancier komt langs met een "AI-module" op de offerte. Tussendoor staat NIS2 op je radar en moet je wéér uitleggen waarom je geen "AI-firewall" kunt kopen.

Lees deze week één ding: hoe Andrej Karpathy zijn nieuwste werk deelt. Niet als code. Eén markdown-bestand. Iedere AI-agent genereert daaruit een werkende implementatie.

Wat dat voor jou betekent: jij kunt dit weekend, zonder budget, zonder leveranciersgesprek, zonder Jira-ticket, een proof-of-concept neerzetten dat groot genoeg is om je MT tot concrete keuzes te dwingen.

Ik deed het zaterdag. Karpathy's bestand gekopieerd, Claude erop gezet, 4,5 uur later stond er een live, zelfonderhoudende kennisbank op het web met acht onderzoeksbronnen erin.

De specificatie staat in CLAUDE.md. Een paar honderd regels. Dát is het hele "product". De implementatie is volgende maand misschien anders gegenereerd. Het idee blijft.

Live in de eerste comment. Repo open.

Welke specificatie ga jij dit weekend schrijven om volgend kwartaal niet meer in dezelfde vergadering te zitten?

#MKB #ITManagement #AI

---

## Versie C — Stap-voor-stap micro-tutorial

**16:03 — `git init`. 20:36 — live op GitHub Pages. Dit is wat ik tussendoor deed.**

Karpathy's `llm-wiki.md` gekopieerd. Geen aanpassingen. Het is een idee-bestand, geen code.

- **16:03** — repo aangemaakt, Karpathy's specificatie erin.
- **16:11** — scaffold met Claude Code: `raw/` voor bronnen (immutable), `wiki/` voor gegenereerde pagina's, `index.md`, `log.md`.
- **16:51** — eerste bron erin: Stanford AI Index 2025. Claude maakt entiteit-pagina's, concept-pagina's, log-entry en cross-references — automatisch.
- **17:02** — tweede bron: MIT Sloan over AI-volwassenheid in organisaties.
- **18:09** — derde tot zesde bron in één batch: MITTRI/Cisco, twee HBR-artikelen en een Lean 4.0-paper. Eén commit, twaalf wiki-pagina's geraakt.
- **18:32** — zevende bron: Brynjolfsson, "Canaries in the Coal Mine".
- **19:42** — achtste bron: Brynjolfsson, Li & Raymond in QJE.
- **20:31** — Quartz v4 toegevoegd. GitHub Actions workflow. Eén commit.
- **20:36** — live: https://businessdatasolutions.github.io/ai-wiki/

Acht bronnen, 4,5 uur, geen leverancier, geen aanbesteding, geen budget. Wel een werkende, zelfonderhoudende kennisbank die zichzelf bijhoudt zodra ik een nieuwe bron toevoeg.

Het volledige "product" is een specificatie van een paar honderd regels in CLAUDE.md. Iedereen die dat bestand heeft, heeft de tekening.

Link in de eerste comment. Repo erbij — neem hem mee als je vandaag wilt beginnen.

Welke 4,5 uur heb jij dit weekend?

#AI #ClaudeCode #SelfHosted
