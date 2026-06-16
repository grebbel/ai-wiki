---
type: narrative
title: "Latent Value in the Intersections: Translating Fung from Engineering to Business"
date_generated: 2026-05-09
based_on: "[[2026-05-08-running-an-ai-native-engineering-org]]"
prompt: "Extract broader business wisdom from Fiona Fung's talk on running an AI-native engineering org — particularly the intuition that today's workers are 'running the shop' and that AI could free human capacity to meet across functional intersections, where latent value is locked."
seed_observation: "today a lot of workers are just busy running the shop. When someone suggests an improvement or a new value proposition or even a new business model, it gets blocked because everyone is busy. A lot of latent value is locked in the intersection between two or more functions, departments, processes, product groups, client categories, products and services. AI could free up human capacity and allow people to meet across these boundaries."
---

# Latent Value in the Intersections

## The translation move

Fiona Fung's *Running an AI-native engineering org* (Code with Claude, May 2026) is a talk about a software-engineering team. Her examples are PRs, code reviews, JIT planning, *"Claude handles style and lint, I keep the human for legal review."* For the casual viewer, it's a niche talk: how Anthropic runs the team that builds Claude Code.

That reading misses what the talk actually is. Fung's specific claims about engineering practice are instances of a much broader pattern — one that applies to any organization in 2026 where some load-bearing capability has just gotten cheap. Translated out of the engineering frame, the talk is a guide to *what an organization should look like when the constraint that defined its old shape no longer binds.*

The translation key is the slide-12 question Fung leaves the audience with: *"if it only exists because engineering used to be expensive, it probably doesn't."* In her frame, the constraint that's lifted is engineering bandwidth. In any other organization, substitute your own historical-scarce-resource: case-handling capacity in a law firm, hours of analyst time in a research group, designer attention in a product company, content-moderation throughput in a platform company, advisor time in financial services, frontline-staff bandwidth in retail. **Whatever was the bottleneck in your industry's last era is now changing, and whatever bureaucracy was built to ration that scarce resource is now vestigial.**

That observation carries a generative implication that's bigger than the talk states explicitly. Because the workers in those organizations are *currently running the shop* — busy with the very processes built around the old scarcity — they have no capacity to notice what changes when the scarcity lifts. The latent value sits exactly in the places they cannot reach: the intersections between functions, between departments, between client categories, between product groups. Those intersections are where the new value lives, and in the old shop you didn't need them, and in the new one you do.

## Running the shop — the problem named

A lot of work in 2026 organizations is *maintenance work*. Re-running last quarter's report. Reformatting last week's deck. Reconciling last month's invoices. Filling the same forms with the same fields for the same regulators. Fung's framing — *"rarely do processes kill themselves"*, *"processes pile on"* — names the accumulation pattern. Every gap that someone noticed at some point became a process. The processes outlived the gaps. The work outlived the work's reason for existing.

Most workers can articulate this. Almost none of them have the slack to act on it. *That's the trap.* The workers who could reform the system are the workers most consumed by running it. The freedom to ask Fung's diagnostic question — *"is this still serving us?"* — requires a margin of attention that the system itself doesn't provide.

This is what [[2026-04-28-reitz-higgins-spacious-thinking|Reitz and Higgins]] called "advantage blindness." Their 3,000-employee survey found that 73% of executives recognized curiosity as critical, but only 9% of employees felt their leaders supported it. That gap isn't ill will — it's structural. Leaders running the shop preach the kind of thinking the shop's processes systematically suppress.

## Why the intersections are where the value lives

What is "the intersection," concretely? Three flavours, all of which the wiki's 2026 corpus engages:

**Between functions.** The work that doesn't fit any one team's mandate. Customer-success knows the product is hard for new users in a specific way; product-engineering owns the fix; marketing owns the messaging. The fix lives in the intersection of all three. In the old shop, this work waits in queues — exactly the [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]] *quoting workflow at FabricationCo* that required coordination across sales, design, and operations and consequently took hours per quote. After workflow redesign, 20 minutes by non-designers. The intersection got resolved, and most of the value resolution captured was simply the value that had been waiting on the queue.

**Between products and customer categories.** Value propositions that combine offerings the firm already has but never bundled because the bundling required cross-team negotiation no one had time for. [[Lowe's]]'s Mylow Companion isn't a product the company didn't have access to in 2024; it's the bundling of stock retail product knowledge × associate floor presence × AI conversational ability that nobody at Lowe's had bandwidth to build before. The result is a 200-bp customer-satisfaction lift across 1,700 stores. The value sat in the intersection waiting to be picked up.

**Between an existing process and the question of whether the process should still exist.** Fung's 50-person weekly meeting that she canceled by asking *"why are we having it?"* — and her broader Monday-morning diagnostic — this is the intersection of *the work* and *the work's purpose*. In a busy shop, no one stands at this intersection. There is no time. AI changes the cost of standing there.

The common pattern: latent value lives where two or more streams of work meet, where a synthesis is possible but expensive in human terms, and where the cost of attempting the synthesis (in negotiation, translation, coordination, scheduling) used to exceed the value of finding it.

## What Fung's engineering rewrite tells the rest of the business

Fung names six operational moves that, translated out of engineering, work for any function:

### 1. Old processes don't die. Name the ones that can go.

The third of Fung's three priorities — *"people don't delete processes on their own; they pile new ones on top; name the ones that can go"* — is the universally true version of organizational housekeeping. In a finance team, a marketing team, a customer-success team, a regulatory-affairs team, the same accumulation has happened. The cost-balance has shifted (in many domains AI changed what's cheap and what's not) and the processes built around the old balance are now overhead. The work to surface them is the work no one has time for; making that work explicit and ritualized is the move. Fung gives it a name on her slides: *"explicit permission to kill old processes"*. As a forcing function for a non-engineering team, this single principle would unlock more capacity than most AI-tooling rollouts.

### 2. The cost of asking a "dumb" question went to zero.

Fung's framing for onboarding in the AI-native team. Translated: in any organization where AI is now ambient, the cost of looking up what something means, finding precedent, understanding what a colleague's slide is referring to, is collapsed. *That changes who can participate in cross-functional conversations.* The barrier to a marketing manager understanding a manufacturing team's quoting workflow used to be hours of explanation; now it's a five-minute prompt. The intersection becomes traversable. The functionally-narrow specialist of the 2010s — invaluable in their domain, useless outside it — gives way to the synthesis-capable generalist whose domain is *picking which intersections matter*.

### 3. Build cheap, argue expensive.

Fung's *generate-three-PRs* anecdote translates: when prototyping any artifact — a marketing brief, a financial model, a process map, a customer journey — is suddenly fast, the *deliberation* about which approach to take is more expensive than just trying them. This breaks the meeting culture of organizations whose last era required deliberation because building was slow. It also implies a culture-of-alignment requirement that Fung specifically calls out: when "the last person who checked in wins" is a real risk, alignment has to do more work than it used to. The cheap-build era doesn't reward consensus theatre; it rewards explicit shared spec-design.

### 4. Roles blur. Intersections become real estate.

Fung's slide-6 framing — *"the XFN gap stops being a bottleneck and becomes a collaborator. Humans still decide, they just aren't the first draft anymore"* — is the central translation point for this entire note. In the old shop the cross-functional gap was where work *waited*. In the AI-native shop the gap is where work *gets done*. Whoever can stand at the gap and direct the synthesis is the new high-leverage role. *That's where the latent value gets unlocked.*

This generalizes a finding the wiki holds at the engineering-discipline layer: Karpathy's *agentic engineering* is the discipline that *preserves the quality bar of professional work while going much faster*. Translated outward: in every function, the new high-leverage discipline is the one that uses AI to ship faster *across* functional boundaries while preserving the standards each function held alone. The cross-functional translation is now a discipline, not a job description.

### 5. The 6-month adoption test.

Fung's slide-10 framing — *"if these don't shift in six months, adoption isn't working"* — is a stronger formulation than most AI-strategy talks deliver. Pick three direction-of-travel signals appropriate to your function (cycle time on a key workflow, time-to-productivity for new staff, share of work that has AI in the loop) and commit to a six-month checkpoint. If the signals haven't moved, **the firm has bought a license, not adopted a technology.** That's the operational interpretation of the [[2026-05-07-ransbotham-augmented-learners|Augmented Learners]] gap: the 15% who actually adopt vs. the 59% who buy and stall.

### 6. Leaders stay close to the work.

Fung's *every manager starts as an IC* rule and her broader dogfooding insistence translate: in fast-moving substrate-shifted environments, the leader who hasn't done recent hands-on work is operating with stale models. This is true for the marketing director who hasn't briefed an AI agent themselves, the legal head who hasn't tried the contract-review prompt, the CFO who hasn't asked the model to forecast — same dynamic as the engineering manager who hasn't shipped a PR. *The model of leadership that delegates execution is incompatible with the speed of substrate change.* Werner-Le-Brun warned about this in the [[2026-04-28-werner-lebrun-octopus-organization|Octopus framing]]; Fung shows what enforcing it looks like as a hiring policy.

## What gets in the way

Three forces an honest read of the talk has to acknowledge.

**Resistance read as deviance, not data.** [[2026-05-07-carucci-resistance-as-data|Carucci]]'s framework for treating organizational pushback as feedback about the change rather than friction to manage away — most leaders don't yet do this. When a team resists the new workflow, the default is to push harder. The information-rich move is to ask which of Carucci's four signals is firing (Loss / Anxiety / Lack of control / Flaws in change). *Flaws in change* is the one that contains the actual latent-value information: the team is telling you something about why your reform won't work in this domain. It is also the signal leaders most often suppress, because operator pushback under deadline pressure feels like obstruction.

**The micro-productivity trap.** [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]]'s name for the failure mode where individual task gains don't translate to firm-level value because the surrounding workflow still depends on tacit knowledge, manual handoffs, or legacy systems. The intersection-unlocking work *is exactly* the workflow-redesign work the trap eats. A firm that buys AI tools but doesn't redesign workflows around them never reaches the intersections — the AI just speeds up the running of the old shop.

**Theatre that calls itself work.** Fung's sharpest slide line — *"for most work it [the design doc] was theater"* — generalizes. A great deal of office work in 2026 is theatre: the appearance of value-producing activity that consumes attention but produces no value the organization could not produce without it. The maintenance of theatre is the most expensive form of "running the shop." Any honest audit of where the workforce's time goes would find significant theatre. Most organizations don't conduct that audit because the theatre serves status, not just task — and you cannot ask a team to disclose its own theatre without offering a replacement source of legitimacy. (This is, incidentally, why the Octopus org's "do less to achieve more" pattern is harder than it sounds: removing theatre requires the leader to provide what the theatre was performing for.)

## A Monday-morning version of Fung's question

Fung leaves engineers with: *"pick your noisiest workflow. Ask if it still earns its place. If it only exists because engineering used to be expensive, it probably doesn't."*

The general-business version:

> **Pick your most expensive recurring activity — the one that consumes the most attention from people you cannot replace. Ask whether it exists because some specific historical resource was scarce. If the answer is yes, ask whether that scarcity still binds. If the answer is no, you have just identified an intersection.**

The intersection is where two streams of work meet that the activity was preventing from meeting. Standing at the intersection is the work that's worth doing this quarter. The freedom to stand there is what the AI-native organization buys you.

That's the talk's deepest claim, and it's the one Fung doesn't quite say but everything in the deck implies. **Not that AI makes the organization more productive — though it does. Not that AI shrinks the workforce — though it might. That AI can free human capacity to stand at intersections that the old workflow design forbade.** Whether any specific organization actually directs that freed capacity toward intersection work, or merely toward more of the old shop running, is the choice that determines whether the firm compounds or stalls in the 2030s.

Fung is showing — through PRs and code reviews and team norms — what it looks like when an organization makes that choice deliberately. The substantive insight isn't about engineering. It's about what every function gets to do once the scarcity that defined its old shape lifts.

---

**Anchors used:** [[2026-05-08-running-an-ai-native-engineering-org]] (Fung talk + 12-slide canon); [[2026-04-28-reitz-higgins-spacious-thinking]] (advantage blindness); [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] (FabricationCo, Lowe's, micro-productivity trap); [[2026-04-28-werner-lebrun-octopus-organization]] (Tin Man / Octopus); [[2026-05-07-carucci-resistance-as-data]] (resistance signals); [[2026-05-07-ransbotham-augmented-learners]] (the 15% / 59% adoption gap); [[agentic-engineering]] (Fung's engineering-discipline analogue at the team-norms layer).
