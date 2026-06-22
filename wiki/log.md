---
title: Log
---

## [2026-06-22] ingest | zot-003-nbra-backlog-process

- Executed trigger: "Update ghs-wiki from NBRA collection using ZOT_003 workflow".
- Acquire check found 23 NBRA Zotero items and 0 newly fetchable additions; all collection items were already present in `raw/`.
- Processed 6 previously unindexed NBRA raw stubs into `wiki/sources/`:
  - [[sources/2010-12-03-biosafety-and-biosecurity-as-essential-pillars-of-international-health-security|Biosafety and biosecurity as essential pillars of international health security and cross-cutting elements of biological nonproliferation]]
  - [[sources/2016-national-laboratory-planning-developing-sustainable-biocontainment-laboratories|National Laboratory Planning: Developing Sustainable Biocontainment Laboratories in Limited Resource Areas]]
  - [[sources/2019-establishment-of-a-national-inventory-of-dangerous-pathogens-in-uganda|Establishment of a National Inventory of Dangerous Pathogens in the Republic of Uganda]]
  - [[sources/2021-01-01-ghs-index-report-and-data|GHS Index Report and Data]]
  - [[sources/2023-ar6-synthesis-report-climate-change-2023-ipcc-portal|AR6 Synthesis Report: Climate Change 2023 — IPCC]]
  - [[sources/2024-06-01-learning-from-history-of-natural-disasters-in-the-sahel|Learning from history of natural disasters in the Sahel: a comprehensive analysis and lessons for future resilience]]
- Updated [[index|wiki index]] to include the new sources in chronological order.
- Notes: two of the new sources are web or portal entries; two are abstract-only because Zotero did not provide attachment full text.

## [2026-06-18] ingest | zot-003-nbra-refresh-execution

- Executed trigger: "Update ghs-wiki from NBRA collection using ZOT_003 workflow".
- Acquire step processed 17 NBRA top-level items and refreshed raw stubs (including webpage URL fallback extraction where needed).
- Process step generated 86 source templates and 4 new raw stubs; after manual relevance cleanup, 3 NBRA source templates were retained.
- Fixed template-generation robustness issues encountered during run:
  - empty `date_published` no longer crashes generation;
  - collection filtering now skips non-requested Zotero collections.
- Build validation succeeded: 112 markdown files parsed, 306 files emitted.

## [2026-06-18] ingest | prep-016-zotero-web-url-fetch-fallback

- Implemented website-content fallback in Zotero acquire flow for URL-only web entries.
- Updated `.claude/skills/zotero-acquire/fetch_zotero.py` so web-like items (`webpage`, `blogPost`, `document`, etc.) attempt direct URL fetch when attachment/fulltext extraction returns empty.
- Added lightweight HTML-to-text extraction (remove script/style/HTML tags, normalize whitespace, cap output length) and write result into raw stub body.
- New provenance marker: `fulltext_source: url-fetched` for successful URL fallback extraction.
- Added CLI option `--url-timeout` (default: 20s) to control website fetch timeout.
- Validation: dry-run on NBRA confirmed mixed behavior (`zotero-extracted` when available, `url-fetched` when fallback used).

## [2026-06-18] ingest | zot-004-ipcc-ar6-orphan-attachment

- **Discovery**: IPCC_AR6_SYR_FullVolume.pdf exists in NBRA Zotero collection (key: ANSAH9AN) but was not auto-acquired by fetch_zotero.py.
- **Root cause**: Item is an orphan attachment (itemType: "attachment", parentItem: null) not linked to any top-level item (journalArticle, book, report). The fetch script only processes top-level items with binary attachments.
- **Manual ingest**: Created wiki source page [[sources/2023-03-21-ipcc-ar6-synthesis-report-climate-change|IPCC AR6 Synthesis Report: Climate Change 2023]] with full frontmatter, findings, and implementation implications.
- **Rationale**: IPCC AR6 is critical context for understanding biosecurity and health security in climate-altered landscapes; informs risk assessment and preparedness under climate change scenarios.
- **Status**: Now indexed in [[index|wiki index]] with concepts linking to biosecurity-capacity-building and one-health-operationalization.
- **Process improvement**: Identified need to handle orphan attachments in fetch script (future enhancement).

## [2026-06-18] ingest | zot-002-nbra-update-new-items

- Fetched newly added NBRA items via Zotero local API (NBRA collection: 15 total items, 13 previously processed, 2 new).
- Acquired 2 new items into `raw/papers/`:
  - `preparedness-impacts-and-responses-of-public-health-emergencies-towards-health-s.md` (PDF + fulltext)
  - `natural-hazards-and-climate-change-are-not-drivers-of-disasters.md` (PDF + fulltext)
- Processed the 2 new stubs into `wiki/sources/`:
  - [[sources/2023-11-30-preparedness-impacts-and-responses-of-public-health-emergencies-towards-health-security|Preparedness, impacts, and responses of public health emergencies towards health security]] (Khatri et al., 2023)
  - [[sources/2022-03-01-natural-hazards-and-climate-change-are-not-drivers-of-disasters|Natural hazards and climate change are not drivers of disasters]] (Ismail-Zadeh, 2022)
- Updated [[index|wiki index]] with new sources in chronological order.
- Related topics: health-systems preparedness, disaster risk governance, vulnerability-vs-hazard drivers.

## [2026-06-16] ingest | cont-001-seed-graph-structure

- Seeded previously empty wiki sections with linked pages:
- Added entities: [[entities/rivm|RIVM]], [[entities/who|World Health Organization]], [[entities/biological-weapons-convention|Biological Weapons Convention]].
- Added concepts: [[concepts/pathogen-inventory-systems|pathogen-inventory-systems]], [[concepts/one-health-operationalization|one-health-operationalization]], [[concepts/biosecurity-capacity-building|biosecurity-capacity-building]].
- Added thread: [[threads/one-health-implementation-gap-closure|one-health-implementation-gap-closure]].
- Added synthesis: [[syntheses/nbra-initial-operational-baseline|nbra-initial-operational-baseline]].
- Updated [[index|wiki index]] so Entities, Concepts, Threads, and Syntheses sections are now populated.

## [2026-06-16] ingest | nbra-rivm-web-sources-update

- Acquired 4 newly added NBRA items from Zotero into `raw/articles/`.
- Added raw file `raw/articles/global-health-security-rivm.md`.
- Added raw file `raw/articles/capacity-training-materials-rivm.md`.
- Added raw file `raw/articles/tools-rivm.md`.
- Added raw file `raw/articles/ghs-world-map-rivm.md`.
- Processed the 4 acquired stubs into `wiki/sources/`.
- Added source page [[sources/2026-06-16-global-health-security-rivm|Global Health Security | RIVM]].
- Added source page [[sources/2026-06-16-capacity-training-materials-rivm|Capacity Training Materials | RIVM]].
- Added source page [[sources/2026-06-16-tools-rivm|Tools | RIVM]].
- Added source page [[sources/2026-06-16-ghs-world-map-rivm|GHS world map | RIVM]].
- Updated [[index|wiki index]] with the new sources.

## [2026-06-16] ingest | nbra-batch-process-remaining-sources

- Processed 7 additional NBRA-acquired raw sources into `wiki/sources/`:
  - [[sources/2022-05-27-complementarity-of-international-instruments-in-biosecurity|Complementarity of International Instruments in the Field of Biosecurity]]
  - [[sources/2024-02-20-we-have-to-join-forces-european-one-health-policies|We have to join forces - Current status and future European policies as discussed at the One Health EJP conference]]
  - [[sources/2024-06-22-an-integrated-inventory-of-one-health-tools|An integrated inventory of One Health tools]]
  - [[sources/2025-07-10-one-health-policy-communities-perspectives-on-zoonoses-risk-factors-and-management|One Health policy communities' perspectives on zoonoses risk factors and management]]
  - [[sources/2025-08-08-application-of-the-one-health-approach-to-zoonotic-diseases-in-bhutan|Application of the One Health approach to zoonotic diseases in Bhutan]]
  - [[sources/2025-11-12-a-haccp-one-health-framework-for-game-meat-supply-chains-zambia|A HACCP-One Health framework for game meat supply chains in Zambia]]
  - [[sources/2026-03-16-horizon-scanning-of-invasive-plant-pests-in-zimbabwe|Horizon scanning of invasive plant pests endangering Zimbabwe's agricultural sector]]
- Updated [[index|wiki index]] with all eight processed NBRA sources.

## [2026-06-16] ingest | systematic-approach-towards-establishing-a-national-inventory-of-dangerous-pathogens

- Processed first NBRA-acquired raw source into [[sources/2021-09-08-systematic-approach-towards-establishing-a-national-inventory-of-dangerous-pathogens|wiki source page]].
- Updated [[index|wiki index]] to include the first source entry.
