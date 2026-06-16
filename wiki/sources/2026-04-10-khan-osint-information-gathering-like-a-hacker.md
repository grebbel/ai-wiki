---
type: source
kind: article
title: "How I Used OSINT to Gather Information Like a Hacker"
subtitle: "I found my company's exposed secrets in two hours. No hacking required."
author: ["Hania Khan"]
publisher: "[[OSINT Team]]"
section: "OSINT Team (Medium publication)"
url: ""
date_published: 2026-04-10
date_ingested: 2026-05-18
length: "~3 min Medium read; full body ingested"
raw: "../../raw/articles/2026-04-10-khan-osint-information-gathering-like-a-hacker.md"
tags: [osint, cybersecurity, infosec, privacy, security, defensive-osint, attack-surface, shadow-it, github-secrets, google-dorks, social-engineering-recon]
roles: [tech-lead]
relationships:
  - type: supports
    target: 2026-05-12-techlatest-hacker-search-engines-osint-tools-2026
    via: "narrative walkthrough complementing TechLatest's platform taxonomy — Khan shows what 2 hours of OSINT looks like against a real organisation; TechLatest catalogues the ~18 platforms that industrialise the same workflow"
  - type: instance-of
    target: osint
  - type: supports
    target: attack-surface-management
    via: "first-person worked example of a one-off attack-surface audit using only free, public sources — concrete evidence for the *unmanaged-known-set* failure mode (3-year-old public GitHub repo with internal credentials)"
---

# Khan — How I Used OSINT to Gather Information Like a Hacker

## TL;DR

A short first-person Medium piece by **Hania Khan** in the [[OSINT Team]] publication (Apr 2026). Khan describes auditing her own organisation using *only a browser and public search engines*, finding within two hours: a list of employee emails, internal server names, and a forgotten PDF containing network diagrams.

The article is the wiki's **canonical narrative anchor for defensive [[osint|OSINT]]** — a *show, don't tell* demonstration that the entire attacker reconnaissance playbook works on data the target organisation has chosen, accidentally, to publish. Seven vectors are walked through end-to-end with the defensive remediation for each. The closing call is operational: *"Run a simple OSINT audit on your own organization. […] The attackers are already doing this. Now you can too — defensively."*

Paired with [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] (the platform-taxonomy companion piece landing in the same week): Khan is the *narrative walkthrough*; TechLatest is the *tool catalogue*. They form the wiki's initial two-source frame on OSINT and [[attack-surface-management]].

## What was actually ingested

Full ~3-min Medium article body, converted via `pdftotext -layout` from a Medium PDF print. No appendices, no methodology section (it's a narrative piece, not a research paper). The source URL was not embedded in the PDF and is left blank rather than guessed; the canonical raw file (with content) is at [`raw/articles/2026-04-10-khan-osint-information-gathering-like-a-hacker.md`](../../raw/articles/2026-04-10-khan-osint-information-gathering-like-a-hacker.md). The original Medium PDF is preserved at `raw/articles/How I Used OSINT to Gather Information Like a Hacker _ by Hania Khan _ Apr, 2026 _ OSINT Team.pdf`.

## Key claims

### Seven OSINT vectors Khan walked end-to-end on her own organisation

1. **Company-website source code.** View-source revealed developer comments with internal file paths, staging-server URLs, and a `<!—remove debug=true before launch →` comment *"still there after two years."* Defensive lesson: scrub developer comments and dev-mode flags before publishing.
2. **Image metadata.** A team-offsite photo contained GPS coordinates and the camera model — sufficient to tell an attacker *where employees gather and what devices they use.* Defensive lesson: strip EXIF before publishing.
3. **Email harvesting via LinkedIn + password-reset enumeration.** Names + titles collected from LinkedIn, the company's email format guessed (`first.last@company.com`), and account existence confirmed via a password-reset form that returned a different message for valid vs invalid accounts. Defensive lesson: password-reset responses must not reveal account existence.
4. **GitHub goldmine.** A public repo containing a configuration file with internal API endpoints and a commented-out admin credential, public for three years. Khan downloaded it, verified the endpoints, escalated to leadership; credentials were rotated and automated public-repo secret scanning was set up. *"Search for your company name on GitHub right now."*
5. **Job postings as tech-stack disclosure.** Five job descriptions stitched into a tech-stack map; named tools cross-referenced against known vulnerabilities. Defensive lesson: use generic descriptions; do not name specific software versions.
6. **Social media physical-context clues.** A LinkedIn photo with an employee badge in frame disclosed the access-control system in use (format, colour, logo placement, card type). Another photo had a whiteboard with a partial network diagram visible. Defensive lesson: policy against photographing internal spaces, or routine blurring before posting.
7. **Google dorks for defenders.** Operators like `site:ourcompany.com ext:pdf` surfaced an internal security policy with server names; `intitle:"index of"` revealed an open directory of log files from an old server. Defensive lesson: these techniques are legal — *Google indexes everything* — so the defender's job is to find what is public and remove it.

### The defensive thesis is "do this to yourself first"

The article does not gate-keep. Every technique is described in enough detail for a reader to replicate the audit on their own organisation. The framing is consistently defensive: *"This is not hacking. It is how web forms work."* The unifying mechanism Khan returns to is that organisations *don't audit what they themselves publish* — every vector exploits the gap between intended and actual disclosure.

### Human-perimeter exposure as an under-attended category

Beyond technical vectors, Khan flags employees' public social-media disclosure of travel and conference attendance as sufficient for targeted phishing or physical pretexting. Defensive lesson: train teams to limit public sharing of work-related locations, schedules, and internal projects.

## Linked entities and concepts

- New concept pages created on this ingest: [[osint]] (this article's defining topic), [[attack-surface-management]] (the management discipline this audit operationalises).
- Bridge into existing wiki: none directly — Khan stays squarely on traditional defensive OSINT; no AI / agent / harness content. The bridge into [[ai-agents]] / [[agent-harness]] sits with the paired TechLatest piece.
- **Dangling** (single-source mention, deferred per author-entity rule):
  - **Hania Khan** (author) — Medium author, "Exploring the evolving world of cybersecurity and emerging technologies."
  - **[[OSINT Team]]** (publisher) — Medium publication, 19.6K followers; *"We teach OSINT from multiple perspectives. Cybersecurity experts, investigators, law enforcement, and intelligence specialists read us to grow skills faster."*

## Source-quality flag

Personal-experience Medium piece, single-author, no peer review, no quantitative data. Confidence calibrated at **0.65** — the techniques and defensive lessons are well-known industry practice (so the *factual* content is reliable), but the article carries no quantitative or replicable claims. It functions as a **narrative anchor**, not an empirical anchor.

The "two hours" headline is unverifiable but consistent with practitioner consensus on how fast a one-off defensive OSINT audit yields material findings against an unprepared organisation.

## Why this matters to this wiki

- **Widens scope.** First wiki source on [[osint]] / [[attack-surface-management]] — alongside [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] as the companion piece.
- **Narrative-to-taxonomy pairing.** Khan's walkthrough is the show-don't-tell complement to TechLatest's tool catalogue — together they form the two-source frame the new concept pages sit on.
- **Tech-lead role-relevance.** Defensive-OSINT auditing belongs to engineering-leadership operational hygiene — hence the explicit `roles: [tech-lead]` tag overriding the (absent) W&W cell defaults.
