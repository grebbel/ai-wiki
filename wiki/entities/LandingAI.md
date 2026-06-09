---
type: entity
kind: organization
aliases: ["LandingAI", "Landing AI", "landing.ai"]
tags: [landing-ai, andrew-ng-founded, document-intelligence, agentic-document-extraction, ade, dpt, document-pre-trained-transformer, vision-first-ai, visual-grounding, computer-vision, enterprise-ai, document-ai, vendor]
founded: 2018
website: "https://landing.ai"
confidence: 0.75
last_confirmed: "2026-06-09"
accessed_at: "2026-06-09"
source_count: 1
relationships:
  - type: employs
    target: Andrew-Ng
    via: "Founder / CEO"
  - type: published-by
    target: 2026-05-26-landingai-touchpoint-to-outcome-front-office-processes
    via: "LandingAI's own webinar on Agentic Document Extraction (ADE) + partner TCG's OCTO orchestration (26 May 2026)"
---

# LandingAI

**LandingAI** is the computer-vision / document-AI company **[[Andrew Ng]] founded** (described in the webinar as *"about seven years ago"*; ~2018). It is the wiki's first **document-intelligence vendor** entity, promoted on 9 June 2026 from a Dangling mention (long referenced on the [[Andrew Ng]] entity as his company) to its own page when the wiki ingested its **first LandingAI-channel source** — the [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|*Touchpoint to Outcome* webinar (26 May 2026)]].

The company self-describes as **"vision-first AI"** — distinct from the *"OCR + LLM"* approach it positions against — and notes a history of *"hundreds of projects to many enterprises"* on visual / unstructured data before pivoting to its current flagship product about a year before the webinar.

## Role in the wiki

LandingAI anchors the **[[document-intelligence|document-intelligence]] vendor altitude** — the technical-and-commercial vantage on extracting high-accuracy, grounded structured data from unstructured enterprise documents. Where [[Google]]'s Gemini File Search ([[2026-05-05-google-gemini-file-search-multimodal|multimodal RAG]]) approaches verifiable document retrieval from a *RAG / hyperscaler-API* angle, LandingAI approaches it from a *vision-first structured-extraction* angle. It is also the commercial instantiation of [[Andrew Ng]]'s *"unbig in AI"* / fit-for-purpose-beats-generality thesis at the document-AI altitude.

### Agentic Document Extraction (ADE)

LandingAI's flagship product. Stated differentiators from the webinar:

- **Vision-first.** Reads a page *as an image* — identifying blocks, structures, and human reading-order — then extracts in that sequence, rather than treating the page as pixels + text. Pitched as the reason competitors *"stuck in pilot form"* on complex documents (nested tables, handwriting, signatures, graphs, mixed formats) succeed with ADE.
- **Visually grounded.** Every extracted value references back to the source cell / word / figure / page, giving a programmatic + UI **audit trail** that suppresses hallucination — *"financial services and life sciences love that type of technology... auditability of data is paramount."*
- **Zero-shot.** *"No training needed, no fine-tuning needed"* — point documents at the API and receive structured output. API primitives include *parse*, *extract*, *classify*, plus schema-driven selective extraction and document splitting.
- **Built for developers** as part of an enterprise-grade agentic stack.

### DPT — Document Pre-trained Transformer

LandingAI's **proprietary model family** underpinning ADE. **DPT2** is shipping; **DPT3** was described as *"just about to be launched"* (as of 26 May 2026). The company cites an *"independent benchmark"* (not shown in the webinar) placing ADE at *"the top of the 99s plus accuracy... even above human performance"* — a **vendor-reported, uncorroborated** claim. (Currently a Dangling concept/product mention; promote DPT to its own page on a second source.)

### Deployment options

- **ADE Cloud** — multi-tenant SaaS, hosted in the **US or EU**, optional **zero-data-retention**.
- **ADE VPC** — virtual private cloud, deployed into the customer's own AWS / Azure hyperscaler tenancy.
- **On-prem / air-gapped** — for government and high-control financial organisations requiring data in their own data centre. More prerequisites; available on request.

### Customer evidence (vendor-reported)

- A **global bank** adopted ADE for KYC / client due-diligence / fraud detection across diverse unstructured documents, moving from *"hundreds of analysts... thousands of hours"* of manual review toward production automation; LandingAI claims it is *"adding two or three [banks]"* to its portfolio monthly.
- Applicable verticals named: insurance, pharmaceutical / life sciences, engineering, manufacturing.
- Trust posture: `trust.landing.ai`; customers across North America, Europe, and Asia.

## Partner ecosystem

- **TCG / OCTO** (Dangling) — TCG (est. 1996) embeds ADE inside its **OCTO** no-code process-automation platform, orchestrating extraction with the *"before and after"* (input normalisation, validation, grounding, downstream-system connection) to reach *"100% accuracy"* before systems of record are touched. The webinar's insurance / car-rental demos are OCTO-driven. See the [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|source page]].

## Open questions

- **DPT benchmark provenance.** The *"independent benchmark"* and *"above human performance"* claims are vendor-reported and unshown; corroboration (the cited blog, a third-party eval) would lift `document-intelligence` confidence above the vendor cap.
- **Founding date.** Webinar says *"about seven years ago"* (→ ~2019) but LandingAI is generally dated to 2017–2018; pin against a primary source.
- **ADE vs LandingLens.** LandingAI's older industrial-vision product (LandingLens) is not mentioned in this webinar; the relationship between the visual-inspection lineage and the document-AI product line is untracked.
- **TCG / OCTO promotion.** Promote TCG, OCTO, and Neil Walker on a second source.

## Mentioned in

- [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes]] — the founding source: LandingAI's own ADE webinar with partner TCG/OCTO.
- [[Andrew Ng]] — founder entity; LandingAI listed in his affiliations and the *"unbig in AI"* / industrial-vision lineage.
