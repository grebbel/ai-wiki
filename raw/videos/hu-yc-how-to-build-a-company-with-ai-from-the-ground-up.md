---
title: How To Build A Company With AI From The Ground Up
video_id: EN7frwQIbKc
url: https://www.youtube.com/watch?v=EN7frwQIbKc
channel: Y Combinator
channel_id: UCcefcZRL2oaA_uBNeo5UOWg
channel_url: https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg
publish_date: '2026-04-24T07:00:21-07:00'
upload_date: '2026-04-24T07:00:21-07:00'
category: Science & Technology
duration: '10:27'
length_seconds: 627
view_count: 164854
is_live: false
thumbnail: https://i.ytimg.com/vi/EN7frwQIbKc/maxresdefault.jpg
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: AI as your company’s operating system
  start: 0:58
  start_ms: 58000
- title: Open vs closed loop companies
  start: '1:57'
  start_ms: 117000
- title: Making your company fully queryable
  start: '3:00'
  start_ms: 180000
- title: The rise of the 1,000x engineer
  start: '5:00'
  start_ms: 300000
- title: Why middle management disappears
  start: '7:12'
  start_ms: 432000
- title: Startups will win this shift
  start: '9:12'
  start_ms: 552000
description: "AI isn't just making teams more productive. It's changing how companies should be built.\n\nIn this episode of Startup School, YC Partner Diana Hu explains what it means to build an AI-native company, where AI isn't just a tool but the operating system your company runs on.\n\nShe breaks down how to make your company queryable so agents can improve across every function, why management hierarchies break down when an intelligence layer replaces human middleware, and why early-stage founders have a massive edge in building this way from day one.   \n\n00:58 - AI as your company’s operating system\n01:57 - Open vs closed loop companies\n03:00 - Making your company fully queryable\n05:00 - The rise of the 1,000x engineer\n07:12 - Why middle management disappears\n09:12 - Startups will win this shift\n\nApply to Y Combinator: https://www.ycombinator.com/apply\nWork at a startup: https://www.ycombinator.com/jobs"
notes: |-
  Transcript fetched via youtube-transcript-api fallback after the Playwright path hit 'transcript panel did not render' timeout (GH #2). Caption track is ASR (auto-generated, kind=asr). Light cleanup: dropped [music]/[applause] non-speech markers, grouped consecutive segments into ~12-second windows with [mm:ss] timestamps, preserved YouTube's chapter list as ## headings. The skill's chapter records returned start_ms=0 (parser bug recurs); recomputed at ingest from the 'start' mm:ss string. 252 raw segments -> ~52 grouped windows.
---

## Transcript
[0:09] Hi, I'm Diana and I'm a partner at YC. Over the past few months, it's become clear to me that AI is not just going to change how quickly software gets built or what workflows get automated. It's going to fundamentally change the way
[0:23] startup should be run from what roles will exist to what products are possible to build. In this episode, I'm going to discuss how founders should think about building an AI native company, what roles their team should have, and what
[0:36] concrete internal practices they can adopt right now to move much faster. Currently, most people talk about AI in terms of productivity. They'll talk at length about how it can make engineers more productive or say we need to add
[0:49] copilot to existing workflows and ship more features. This framing misses the shift we're currently seeing, which is less about productivity boosts than

## [0:58] AI as your company’s operating system
[0:59] entirely new capabilities. The right person with AI tools can now build features that used to require an entire team or were just impossible. Thinking about AI in terms of new capabilities
[1:11] has several implications for how founders should run their companies. At a high level, the way to think about AI is that it should not be a tool your company just uses. It should be the operating system your company runs on.
[1:26] Every workflow, every decision and every process should flow through an intelligent layer that is constantly learning and improving. What this means concretely is every important process in your company should be captured by an
[1:39] intelligent close loop. A close loop captures information, feeds it back into an intelligent systems, and improves the process over time. If you've ever studied control systems, you'll be familiar with the difference between an
[1:51] open loop and a closed loop system. Open loops are controlled systems without feedback loops. In the old world,

## [1:57] Open vs closed loop companies
[1:57] companies basically ran as open loops. You made a decision, executed it, and didn't always systematically measure the outcome and adjust the process. Open loops are inherently lossy. A closed
[2:10] loop, on the other hand, is self-regulating. It continuously monitors its output and adjusts its process to better meet the stated goal. Closed loops are extremely powerful for correctness and stability. With
[2:23] self-improving agents, your company should run as a closed loop. To build these closed loops, you will need to make your entire company queryable. In other words, the whole organization should be legible to AI. Every important
[2:36] action should produce an artifact that the intelligence at the center of the company can learn from and use to self-improve. This means recording your meetings with the AI notetaker, minimizing DMs and emails, and embedding
[2:49] agents throughout communication of all channels. It also means building custom dashboards with everything in the company, revenue, sales, engineering, hiring, ops, everything. Here's a

## [3:00] Making your company fully queryable
[3:00] concrete example of how it could work. Take engineering, management, and sprint planning. If you have an agent that has access to your linear tickets, all your Slack engineering channels, all customer feedback from emails or tools like Pylon
[3:14] and GitHub, highle plans in a notion or Google doc, sales calls and recordings from daily standups, then the agent can analyze what was actually shipped in your previous sprint and how well they
[3:26] met customers needs for real. From there, you can go a step further with full visibility into what shipped, what worked, and what didn't. Agents can start looking ahead. They can propose sprint plans for engineers that are way
[3:40] more predictable and accurate and on track. The days of anch manager status rollups that are super lossy are gone. Having managed engineering teams myself and now seeing this across multiple YC companies, this is a gamecher. What used
[3:55] to require constant coordination becomes legible and querable by default. I've seen teams that do this cut their engineering sprint time in half and get close to 10x more done in that time. The
[4:09] overarching principle here is that to get their full capabilities, you need to provide models with as much context as you would provide an employee. When you do this, your company stops operating as a open loop where information is
[4:22] fragmented and manually interpreted. It becomes instead a closed loop system. Status, decisions, and outcomes are continuously captured and fed back into this intelligence layer. The result is a
[4:34] system that always has an upto-date view of what's actually happening. There's also a new paradigm emerging for how the highest velocity companies build product AI software factories. If you're
[4:48] familiar with the testdriven development or TDD, this is the next evolution of that. With software factories, humans write a spec and a set of tests that define success and then AI agents

## [5:00] The rise of the 1,000x engineer
[5:02] generate the implementation and code and iterate until the test pass. The human defines what to build and judges the output. The actual code is the agent's job. Some companies have
[5:15] already pushed this to the point where their repos contain no handwritten code, just specs and test harnesses. Strong DM's AI team is an example of how to do this. Their end goal was a system that
[5:30] essentially eliminated the need for a human to write or review code. And so they built their own software factory where specs and a scenario based validations drive agents to write tests and iterate on code until it meets a
[5:44] probabilistic satisfaction threshold and it works. This is how you achieve the thousandx engineer that Steve Jay talks about by surrounding a single engineer with a system of agents that enable them
[5:58] to build things they would have never been able to build before. The era of the thousand or even 10,000 X engineer is here. One implication of building your company this way with AI loops
[6:10] everywhere, a queryable organization and software factories is that the classic management hierarchy no longer makes sense. In the old world, you needed middle managers and coordinators to route information inefficiently up and
[6:25] down an organization. In the new world, the intelligence layer serves that purpose. If your company is queryable, artifactrich, and legible to an AI, you
[6:37] should have almost no human middleware. This matters because your company's velocities is only as fast as its information flow. Every layer of human routing you can remove is the direct
[6:50] speed gain. A great example is what Jack Dorsey is doing over at Block. After going deep on the tools, he's come to the same conclusion many have. This is about more than just incremental
[7:04] productivity gains. His view is that if you keep the same org chart and management structure, you've missed the shift entirely. The company itself has

## [7:12] Why middle management disappears
[7:13] to be rebuilt as an intelligence layer with humans at the edge guiding it rather than routing information through it. Going forward, Jack suggests every company will have three employee archetypes. The first is the individual
[7:25] contributor or IC basically the builder operator. This is someone who directly makes and runs things in an AI native company. This is not limited to engineers. Everyone builds and ops
[7:38] support sales. Everyone comes to meetings with working prototypes not pitch decks. Second is the DRRI the directly responsible individual focused on strategy and customer outcomes. This
[7:51] is not a classic manager is the person with a clear responsibility for the result. One person, one outcome, no hiding. The third is the AI founder type. This person still builds, still
[8:05] coaches and leads by example. If you're the founder, this needs to be you at the forefront, showing your team what massive capability gains look like, not delegating your AI strategy to someone else. With this structure, companies
[8:19] will be able to get outsized results with much smaller teams. Maximizing token usage, not headcount, will be the critical shift. The best companies will be the ones that are token maxing. Think of the trade-off this way. One person
[8:32] with AI tools can be the equivalent of what used to take a large engineering team at a preAI company. That means dramatically leaner engineering, design, HR, and admin teams. And so you should
[8:46] be willing to run an uncomfortably high API bill because it's replacing what would have taken a far more expensive and inflated headcount. But don't just take my word for any of this. You cannot
[9:00] outsource your conviction on the power of these tools. You need to develop it yourself by actually sitting with coding agents and using them until you start to break your own priors about what is now possible to build. If you are an early

## [9:12] Startups will win this shift
[9:13] stage founder, you have a huge advantage in getting ahead on this. You don't have legacy systems in orchards or thousands of people to retrain. You are small enough to build your company right from day one. The opposite is the case for
[9:27] existing companies. They have to maintain and grow a live product while unwinding years of standard operating procedures and core assumptions about how software gets built. Some companies
[9:39] can achieve this by spinning up small internal skunk work teams that can build AI native systems from scratch separate from the core business. Mutiny is a great example of this. But for most, every change to their core processes
[9:53] risk breaking something that already works. So by their nature, these large companies will have a much harder time going AI native. Startups don't have that constraint and that's a major edge
[10:06] to take advantage of. You can design your systems, workflows and culture around AI from the start and as a result operate thousand times faster than the incumbents.
[10:22] Same
