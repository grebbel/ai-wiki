---
title: "The Q/A Layer for the AI Coding Era"
video_id: UpWNdSVWA7M
url: https://www.youtube.com/watch?v=UpWNdSVWA7M
channel: YC Root Access
channel_id: UCxIJaCMEptJjxmmQgGFsnCg
channel_url: https://www.youtube.com/channel/UCxIJaCMEptJjxmmQgGFsnCg
publish_date: '2026-03-23T07:00:45-07:00'
upload_date: '2026-03-23T07:00:45-07:00'
category: Entertainment
duration: '33:54'
length_seconds: 2034
view_count: 6998
default_language: en
is_live: false
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  In this episode of Founder Firesides, YC Managing Partner Harj Taggar talks to Weiwei Wu and Jeff An, co-founders of Momentic (W24), who just raised a $15M Series A. Momentic is the verification layer for software — an AI-powered testing platform that impersonates end users to catch bugs before they ship. Powering companies like Notion, Quora, and Built with over a million test runs a day, they discuss why the explosion of AI-generated code makes testing more critical than ever and their vision for a future where engineers write specs, not code.

  https://momentic.ai

  Apply to Y Combinator: https://www.ycombinator.com/apply
  Work at a startup: https://www.ycombinator.com/jobs
notes: |
  Acquired 2026-05-22 via youtube-transcript-skill (Playwright path, first-attempt success, 328 ASR segs). Light cleanup: "Weiwayi"/"way"/"ways" → "Weiwei" or "Wei" by context; "Mantic" → "Momentic"; "llinters" → "linters"; "customerf facing" → "customer-facing"; "PC process" → "POC process"; "SES" → "SEVs"; "agentto agent" → "agent-to-agent"; "playright" → "Playwright" (the test framework); "Kora" → "Quora" (per description); "claw MD" → "CLAUDE.md"; "codeex" → "Codex"; "Standard Capital" preserved verbatim from ASR (lead investor). NOTE: speakers say "$50 million Series A" but channel description says "$15M Series A"; channel description used as canonical figure in body since author is authoritative. Stage cues retained.
---

## Transcript

[0:00] [music] Hey everyone. I'm excited to be joined here today by Weiwei and Jeff. They're the co-founders of Momentic. Momentic went through YC in winter 2024 and just raised their $15 million Series A round. Wei and Jeff, why don't you tell us what Momentic does?

[0:20] Yeah. Momentic is the verification layer for software. We power awesome companies like Notion, Built, Quora, Zero, and we're processing over a million test runs a day.

[0:32] And you just raised $15 million in your Series A from Standard Capital. Maybe tell us a bit about why did you raise the round now?

Yeah. So for us, we were at a place where we had a repeatable sales motion and we wanted to raise to scale both our engineering and go-to-market team so we could build more and get more customers.

[0:55] And then why Standard Capital — why did you choose them as your lead?

Yeah, for us, the decision came down — it was pretty simple. Standard was a very quick process. We applied through online, you know, not too unlike the application for YC. And I think one of the big standouts for us is, like, instead of having a board member on our board, we have a peer group of other similar-stage Series A companies to do our board meetings with. It's a peer group where we're learning and helping each other.

[1:31] For people who aren't technical, maybe who aren't developers, explain sort of what testing even is, and then what does Momentic actually do for developers?

[1:38] Yeah, for sure. So the quick 101 on testing is — if I'm shipping code, how do I make sure my app isn't broken? And especially as my app is getting larger and larger, there's multiple people, multiple teams working on it, there's different product lines, and how do I make sure it's not broken? And testing is the solution to that. You have teams manually testing, which is incredibly inefficient. And you have teams also dipping their toes into automations — like, how do we make this process faster, more efficient, without taking as much valuable engineering time? But the end goal is always: how do I make sure my product is working as I expect?

[2:20] One thing that developers are known for traditionally is not wanting to write tests, not enjoying testing. Like, is that true for both of you in your careers as engineers? And so if so, why? Why has there always been this reluctance to write tests?

[2:38] Yeah, I think so. When I was at Robinhood, I saw the team grow from 300 engineers to over 1,000. And then my entire job was basically managing eight people and trying to get those eight people to convince the other thousand people to write and maintain tests. And our goal was to cover 80% of the code that we wrote and maintain a 90% pass rate. And it was basically impossible to do that. Basically like — no one cared about this. And I think it just boils down to the fact that it doesn't feel like productive work. Like, it's not work that your customer sees. It's not work that you get to show someone in a flashy demo. It's not work that shows up on your performance evaluation, right? And so because of that, it always feels like a drag, like a secondary afterthought. And that's when there's really a risk to quality and reliability.

[3:26] Now, as we're entering this era of codegen, it's so fast-moving — one day it's Cursor, the next day it's Claude Code, maybe the next day it's Codex. One thing that's clearly staying constant is just the amount of code — like lines of code being written per day — is growing exponentially. How is that going to impact the need for Momentic and testing? Where have you seen that affect your business?

[3:51] Yeah, for sure. I think as the amount of code output is increasing, we see massive bottlenecks where there may not be before in terms of just: how do I actually verify the work? There's linters, you have code review, but then how do you actually make sure this works when this is deployed to production?

[4:09] Again, explain for people who aren't engineers themselves, kind of conceptually — what are linters, and what's code review, and how does that fit in under the umbrella of testing and shipping?

[4:26] Yeah. So when you're shipping a high volume of code, there's certain tools you can use to verify that the code follows good patterns — like you can have linters that scan through your code, make sure you're following the right patterns, following the right best practices. You can also have a code review where it can be a human — another engineer review your code that you're about to merge — or recently there's been a lot of AI code reviewers helping to take some of that burden off humans. And I think an important part that Momentic solves is, beyond all these different checks that you already have today, how do you actually make sure it's actually working live? And the status quo for a lot of teams is, I'm going to go in as a human and log in and manually click around and do like a bug-bash every time before a release. And that's just not scalable when your product is growing — you have a lot of engineers — and it's also very slow and very expensive.

[5:31] And so then where exactly does Momentic fit into that flow? Like, you have engineers writing the code, you have linters looking for, does it conform to the right patterns or not, you have humans reviewing code. Where does Momentic fit in there?

[5:46] Yeah. So the type of testing that Momentic does is what we call **functional testing**. It's acting — impersonating one of your users — actually going through your app and clicking through and making sure all of the user flows that I can achieve are actually working. And how we fit in is: as an engineer makes a code change, their change is going to impact production in some way. We just make sure that everything that they care about doesn't break, from an end user's perspective.

[6:22] How should engineers think about where you fit into the dev stack? Like I've certainly noticed this on our own engineering team at YC — like as Claude Code usage has ramped up, we've now set up sort of a pipeline (it's in the CLAUDE.md file actually) to just like make sure you run your own tests and make sure they all pass before you submit any PRs or MRs. Where should an engineer who currently doesn't have Momentic in their dev stack think about inserting you?

[6:51] Yeah. So I think there's a couple places. One is within your developer loop. We are seeing a lot of customers actually use our MCP integration to have Cursor or Claude Code write and run Momentic tests while they're developing. So actually while they're creating a new feature or editing an existing feature, they'll make sure that these coding agents also verify that that change is functionally correct by calling out to Momentic — starting a real browser, verifying that the flow actually works — like a tool. It's basically a tool-call for one of the agents.

[7:26] And so — why is that better than the agent just sort of writing its own tests from scratch?

[7:29] Yeah. So one thing that we've seen is, like, first of all, the agent often thinks that it doesn't have to do that, or whatever it's done is just correct, even though it's not. And secondly, these agents aren't optimized for browser use, especially in a testing capacity. So some of our customers have incredibly complex sites that are actually incredibly hard to interact with — right, like rich text editors, drag-and-drop editors, things that have canvases. And these types of applications are just relatively difficult to verify. But we've specialized our agents to deal with that.

[8:01] It's also really slow. Like, I've used this for just like side projects where you have the like Chrome browser extension — you can tell Claude Code to like use the browser extension to figure out what's going on with this bug, but it's just so slow. I presume your agents are optimized for speed and actually being able to test a complex app?

[8:22] Yeah. So the average step for us runs in under 300 milliseconds. And to your point, we've also optimized the debuggability UX part of it. So it's really hard to know what went wrong if you use a traditional browser agent. You know, it's hard to debug exactly what element was interacted with or what the state of the page was. We've essentially built the whole platform around that type of user experience, and we have agents that help with that as well — like, they automatically diagnose these issues for you.

[8:51] Yeah, because I find the existing agents — like, it works okay-ish if, you know, you've got some like file-upload button is not working, like "open web browser and figure out why a file upload is not working." Whereas you guys are like, I don't have to specify that at all — like, yeah, I just give you the app and you will just figure out all the various things to test and what the correct tests are.

[9:08] Yeah, exactly. Any user flow you can describe — whether it's to a manual tester or to an AI or to Cursor or Claude Code — when you're building it, just give it to Momentic and we'll validate it.

[9:24] And then, so then go back — you mentioned code review, and you certainly like code review tools like Cursor BugBot, Greptile — these things are very popular. Again, like the YC engineering pipeline, we have these integrated in. So what does a future dev stack look like? Are people using you and code review tools? Are you sort of competing for developer mindshare? Or are they sort of like totally orthogonal to each other?

[9:53] Yeah. Yeah. I think that's a great question. And I think, taking a step back, I would be disappointed in three to six months if I'm still reviewing TypeScript or React code. And I think the future of software is moving towards a world where I, as an engineer, can provide a plain-English spec to some AI agent, it's going to build it, verify, make sure it all works according to the success criteria, all the different edge cases I've spec'd out. I see code as an implementation detail. It's a commodity. Some frontier model out there or frontier AI coding tool is going to be incredibly good at generating code. It's just the implementation detail.

[10:34] And today I think we have code review because we still care very much about the code that's being generated. But I don't think that's necessarily going to be true in the next three to six to nine months.

[10:46] What do you — let's assume the models are going to keep getting better and better, and just like the quality of the code they output is going to get better and better — again, how does that impact your outlook for Momentic over the next X months?

[11:00] I think it impacts user behavior more than anything. Today, engineers are still very much focused on what code is being generated. But I think as these models get better, that will be less and less of the focus. And humans will be more like requirements-gatherers, or they'll be sort of like **truth-finders**, right? Like, their goal is basically to figure out: what should be written, what should be built in the first place? What are the requirements from the end user? Or, I have a thousand feature requests from various customers — which ones are actually the ones that I'm supposed to build? And so they kind of become like the input to the code generator black box, and then we're this sort of step that actually validates that whatever the black box generates is functional.

[11:48] That certainly lines up with my own experience as a developer, because I feel like — yeah, you can — the quality of the model is getting better and better, but they will still confidently go off in the wrong direction. And then you're sort of doing this patchwork of like adding things to your CLAUDE.md file and trying to make sure it steers, and like it consults you before it — I mean, plan mode's the obvious example. But even sometimes plan mode's not enough — if you have to sort of like, before you go off and assume that this hypothesis for debugging is correct, like, run it by me first. But yeah, the dream would be to just have like an external source of truth that just knows everything about how my users are using my app, and it can consult that and figure out — okay, no, I should — like, this is, of these three hypotheses, this is kind of where I should go. Is that the way that you imagine Momentic interacts with the coding agents?

[12:41] Yeah. The coding agents are going to be informed on what to build by the spec, and the spec would have details about what the different user flows it needs to build, what different features, how it's supposed to work. And that spec is also the guardrails of how do you verify these requirements are met. And that's completely going to be done through Momentic.

[13:06] In a sense, it's like we're **closing the loop for feedback for the coding agents**.

[13:11] And why — what's the reason that that's always going to be a better product sort of as a standalone product, outside of like the coding agent itself? [snorts]

[13:22] One of the things that's pretty interesting is — today, the coding agents are generating code. It can prompt you for feedback. It can access third-party tools, different dependencies through MCP servers or CLI. And I think one of the things that's incredibly important is, how do you make sure — the always the open question at the end of the day is — how do I make sure Cursor or Claude Code actually built what I told it to build, in exactly the way I told it to build it? And for me, I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth for verifying that. This is why I have unit tests, I have integration tests at different parts of the stack.

[14:18] And I think that's an incredibly important part, because at the end of the day, if something breaks, I can't really tell our customer, "Hey, we vibe-coded this with Claude Code, our SLA got breached because of that, sorry about that, we're going to revert their pull request." I think that doesn't really work on like that, because the responsibility ultimately is on the product owner — on the human who was delegating to these different AI agents.

[14:48] I think the other interesting part about this is that Cursor or these coding agents in general aren't maintaining your source of truth over time. It's similar to the question of: why don't you use Cursor to generate Playwright code, right? And the answer is, well, you can right now, you have 100,000 lines of Playwright code, and whenever you change your feature in a meaningful way, now you have 50K lines that you have to find and update.

[15:11] I think what we've done is, like, essentially we have encapsulated that whole system, and so we've built a mechanism for automatically maintaining that source of truth over time for you — and even going as far as suggesting changes to what your source of truth should be. Like, you've added this new UI component. Was that intentional? And if so, I can automatically actually update the test for you without you having to go through another 200,000 tokens — or your Cursor credits in one session.

[15:41] Cool. Um, so let's — okay, so then let's talk about one of your biggest customers, Notion. Like me. I would love to learn a little bit about — how were they thinking about testing before Momentic? How did they hear about you? Then how did you convince them to use you, and what's sort of been the difference in their workflow post-Momentic?

[16:05] Yeah, for sure. So I think it's a really funny story on how we started working with Notion. Simon from Notion actually was posting on Twitter — like, "It'd be great if I could just describe this and test it for me." And, you know, a lot of people were commenting on the Twitter thread. A lot of people recommended Momentic. I was in San Francisco actually that evening at 10 p.m. I DM'd Simon — Simon Last — and I was like, "I think we've built exactly what you want. I can onboard you tonight." I sent him a Loom of me testing on my own personal Notion workspace. And we onboarded him that night.

[16:45] And then it turns out it was a good enough experience where we decided to do a more official POC process with the broader Notion team. They were coming from a mix of manual testing, a really big suite of Selenium that the team was maintaining, and that was just taking a lot of effort, because Selenium is notoriously prone to flakiness — whether it's like XPaths or selectors which is how you target elements on the page, it would frequently break. Especially since Notion is such a very flexible product — it's a rich text editor, everything's a database — but all of those things are also very difficult to test with Selenium. And we were able to handle that with Momentic quite easily through just like plain-English instructions. And now today they execute almost like half a million test runs a day. Momentic tests must pass before one of Notion's engineers can merge their PR.

[17:53] How does Notion sort of quantify the value they've gotten from working with Momentic?

We can think about ROI in a few different lenses. One could be developer hours saved with Momentic compared to Selenium. That's the easiest, especially if you're coming from a legacy tool like Selenium or Cypress or Playwright. But I think the north-star is, how many regressions or SEVs are Momentic tests preventing from reaching your end customers? Because that is the end goal. Tests are just a way for you to prevent these types of regressions and incidents. And that's how we would track ROI for our customers and Notion.

[18:37] I've heard you all mention this idea of like **truth-driven development**. What does that mean, and where does Momentic fit into that?

[18:49] I would say like the two main schools of thought are: one is, **your code is the source of truth**. Whatever is in prod is what you've specified it to be. That's a direct reflection of your codebase. And that has a few gaps. It's not necessarily entirely incorrect, but code has bugs, and are these bugs also part of your source? Is that how your product is supposed to behave?

[19:15] And then the other one is what I would consider **truth-driven development**, or **spec-driven development**. This is where someone, typically a human in collaboration with AI, is specking out in detail different user journeys, user flows, success criteria, edge cases within your application. And this is the source of truth for how your product is supposed to work. Your code is just an implementation of that source of truth. Because, you know, since engineers are humans, we make mistakes, AI makes mistakes — we're all contributing to this codebase. It doesn't really make sense for that codebase, production, to be the source of truth for how my product is supposed to work.

[20:06] So one of the things — especially as all of these different AI coding tools — how we interact with AI is increasingly through plain-English text. I'm chatting with Cursor, I'm chatting with Claude Code, I'm chatting with ChatGPT. Our bet is that in the future — in the near future, I would imagine — instead of writing code and reviewing code, I would actually just be writing specs and detailing edge cases, success criteria, that's for these AI agents to build. I don't really care if they're using TypeScript or Rust or anything like that. They're just implementation details to me. All I care about is the end user journey, the end success criteria that I've spec'd out. In the future, that's like my source of truth.

[20:54] Do you think the role of being an engineer then moves away from sort of starting with the code, looking at the code, really deeply understanding the code, and eventually engineering is just going to mean reviewing the specs? Will you need any appreciation of the code and thinking about that as a source of anything?

[21:05] Uh, I mean, I think so, in so much that I think there are still many technical aspects of being a software engineer that are not based in the code, right — like thinking about how this integrates with other systems or third-party dependencies, or the scalability aspects, or even just thinking about taste, right? I think models are not particularly good right now at producing tasteful UX, for example, and that's the difference between ChatGPT generating a Figma lookalike and actual Figma, right? The devil's very much in the details. So I do think the technical expertise still matters. But at the same time, I feel like good engineers were always sort of their own PMs in a way — they always had a strong product intuition and a sense of what the vision for their product should be. And I think that's going to be more and more true as the sort of truth-driven development idea becomes more prevalent.

[22:04] What's sort of on the roadmap for you guys, maybe especially this year and then maybe even further afield?

Some of the things that we've been working hard on, for example, is Android, iOS, desktop app support. And I think if anything our focus this year has narrowed. We've seen firsthand how fast engineers are moving, and we're always thinking about how can we accelerate them, how can we be faster, how can we be more integrated with their existing tools and workflows, and how do we make the barrier-to-entry zero or negative — like, they just fall into this pit of success with Momentic. A big focus this year is definitely on developer experience, developer productivity for our customers, beyond just the core primitives that we support as a platform.

[23:00] And then maybe as a company — kind of as you start adding people and you grow the company — how do you think about that? What are the skills, maybe especially for engineering, what skills do you look for and how do you think that's changed from sort of the pre-AI world?

[23:19] I think, to be honest, a good engineer is still a really good engineer. I actually wrote a LinkedIn post about this — but, like, **Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with.** And I think that underscores the fact that if you're adaptable, if you can navigate ambiguity, if you're curious and passionate, then that continues to be an asset. And that's still what we're looking for.

[23:45] I think now that the industry is moving at this incredibly fast pace, it's even more important to be able to adapt to new trends, to be able to take in that there's a new level of tooling that you can adopt that dramatically accelerates your code output. And, you know, as always, like we need folks with strong product intuition. As people at Momentic, I think effectively own entire domains and are given a lot of ownership and responsibility.

[24:14] Have you thought about just the company culture? Anything? How would you describe your culture as being sort of unique to you guys at Momentic?

[24:25] Yeah, I think we're still a pretty small team. We're a team of 13. And I'll say our culture is still budding, early early stages. But I think one of the things that we care a lot about is **radical candor** — clear direct feedback, you know, don't be a dick, don't be an [expletive] to your co-workers and people that you're working with day-to-day, but also being able to give and receive feedback so everyone can be the best version of themselves. And we want to hear everyone's voice. Everyone has a say in our product roadmap. We want to hear all of your feedback, all of our customers' feedback. And I think that's kind of the basis driving how we think about culture. Just be a pleasure to work with and learn from.

[25:16] How did you both get into engineering and tech and startups? Love to hear the quick overview of that.

When I graduated high school, I was actually planning to be a pharmacist. I was going to go to a PharmD program. And then the summer before college I went to a pharmacy camp with a friend and it was the most boring experience of my life. After that camp I decided to change my major. I actually got into University of Minnesota — they had a like, in pharmacy, what is it called — like, two years undergrad, four-year PharmD program. I was like, I'm going to change my major to computer science. Can't get into the science and engineering college, and they let me. So that's how I got into computer science and software engineering.

[26:04] So I was going to study chemistry at Cambridge, actually. And then, similar to your experience, I did a summer internship and the day-to-day lab work was incredibly grueling. Essentially each researcher does their own work in a fairly isolated way. And I realized that while it was technically interesting, and I think the problems solved are some of the most important problems in the world, that type of work didn't sort of challenge all of me as a person. There was a part of me that really wanted to build products and work with other people and rally a team — and I think that interpersonal side of things just was missing from that day-to-day life. And I think that's like what pushed me towards founding ultimately — I think it's like the one role that really pushes you in every aspect of your life.

[26:56] Cool. And then how did the two of you team up and work on this specific idea?

So we actually got introduced end of 2023 through a mutual friend, Dan Robinson, the old CTO of Heap. I was actually beta-testing Dan's startup at the time, which was called like QQ Bot. It was using AI to — it was like Cursor for unit tests before Cursor existed. And then I was sharing — I was building a few prototypes on the side, and I was sharing with Dan, and actually Dan introduced me to Jeff, who was building his own product in the same space I was. So we met, we had a quick Zoom call. I was in Seattle and Jeff was in San Francisco. And I actually flew down, I stayed on Jeff's couch for like a week or so, before we decided to join forces and build Momentic together.

[27:50] And what prompted you to apply to YC, and what was that process like?

I think it was your idea actually. I was incredibly unconvinced we would get in. At that time we had a little more than a prototype. AI agents were really bad at that point. Models still had like 16K in token limits — which meant that most websites wouldn't actually fit within the context window — and we barely had any market traction. So I thought there's no way they would take us. But I think Wei convinced me — it was like, you know, we've been jamming on this, I see the potential, and we might as well throw in an application. So we did that, and here we are.

[28:30] Yeah. For what it's worth, we had I think like six or seven pilot customers at the time that we were hopeful would convert. So we had good quality of customer feedback and interactions.

[28:49] As founders now and your journey, what have been some of the most challenging moments running and growing the company, and how have you handled them?

For me, I would say building the company early on in terms of headcount was really challenging. Especially at the seed stage, there's a ton of seed-stage startups now building a lot of cool stuff. And when people say "AI seed-stage startup," I think there's a lot of thrash right now — people don't know what to choose from. And, you know, especially given how popular and strong the foundational-model companies are, there's a strong draw away from the startup market. So I think we had a really tough time with just early talent and convincing people that we were going to win.

[29:33] I think we had to really double-down on proving that our culture was solid. We invested a ton in our interview process — where we would talk to people multiple times before they ever did a single interview. We would be really intentional about the on-site. We ended up building a sort of rather unique one-day work-trial process. And we double-down on the culture when they joined as well. So we do really in-depth team retros and discussions, retreats as well.

[30:05] I think for me, the main thing would be: how do we — the landscape within AI is shifting so much. How do we adapt on the fly to different workflows, to different trends we're seeing — new tools, new models, things like that — but at the same time also look ahead: what is the actual problem we're trying to solve, rather than creating a solution trying to fit a problem into it the opposite way around? And making sure the whole team is aligned on the direction that we're going and is very excited about it.

[30:45] And then I think secondary is, learning how to sell as an engineer. How do I — what's a POC, what's a pilot, what's the difference? What are the things I should say on these sales calls? Over the past two years, I'm still a new seller, but I think I've gotten a decent amount better at selling and pitching and solving customer pain.

[31:10] What's your best advice to engineers who are sort of where you were a couple of years ago, starting out, need to learn to sell? What's your best advice?

Yeah, you just have to do it. You have to be comfortable with that. I think about it as like you have different cohorts, and every cohort you're going to burn — and some of them will probably never come back. But this is a great learning experience for you. As you learn and evolve in your sales process — how you talk to customers, how you communicate, how your product solves their problems — at the end of the day, you have to get your reps in. You can't learn just by watching someone else sell. Everyone has their own unique way of communicating and selling and chatting with customers, and you just have to get the reps in.

[32:00] What keeps you both motivated to want to keep working on this problem and build this into a huge company, through the inevitable challenges you have?

I think a lot about the impact that we could have if we fully solve the problem of code validation. I think a lot of product development, feature development is blocked on how fast you can verify code right now. And so I think about the global productivity improvement that we can make if we change this very fundamental aspect of how software engineering works. It's a fairly utilitarian mindset, almost. But as someone who's always been really passionate about DevEx, it feels incredibly force-multiplying to be able to make everyone else around you be able to deliver a higher-quality product with a few bucks.

[32:54] For me, Momentic is disrupting a massive industry. The QA industry is massive — but that's actually not the market we're specifically targeting. We're targeting all software. Every software that's ever going to be built — now and in the future — will need to be verified. And how do you do that? It's going to be with Momentic. And then I think like secondary is, I just — I want to win, but not just win. I want to kill all of our competitors. Like we will win and destroy them all. It is inevitable. We will make that happen.

[33:27] Nice. All right. Well, on that note, that's all we have time for today. Congrats so much on the round, and I'm really excited to see where you guys take things. Looking forward to seeing Momentic continue to grow this year and the years beyond.

Yeah, thanks, thanks for having us, Harj.
