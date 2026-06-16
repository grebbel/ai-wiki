---
title: Inside YC's AI Playbook
video_id: B246K_G7mHU
url: https://www.youtube.com/watch?v=B246K_G7mHU
channel: Y Combinator
channel_id: UCcefcZRL2oaA_uBNeo5UOWg
channel_url: https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg
publish_date: '2026-05-27T07:00:26-07:00'
upload_date: '2026-05-27T07:00:26-07:00'
category: Science & Technology
duration: '46:30'
length_seconds: 2790
view_count: 30430
is_live: false
thumbnail: https://i.ytimg.com/vi/B246K_G7mHU/maxresdefault.jpg
keywords:
- YC
- Y Combinator
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "Building superintelligence inside a company isn't about adding AI as a feature. It's about making it the operating system the whole organization runs on. In this episode of the Lightcone, we sat down with YC's Pete Koomen to talk for the first time about how he led the effort to build YC's internal agent infrastructure from the ground up. We cover how giving agents unrestricted access to one database changed everything, the self-improving skill loops that get smarter overnight and why he thinks we've arrived at the personal computer moment for AI.\n\nChapters:\n00:00 — Intro\n00:39 — YC's AI Stack\n02:15 — The Finance Team Problem That Started It All\n05:07 — SQL Access Changes Everything\n07:20 — One Database to Rule Them All\n09:14 — Jevons Paradox \n10:07 — Denormalizing for Agents (GBrain)\n12:15 — The Single-Player Era of Agents\n14:16 — 350 Tools and a Shared Registry\n16:24 — Skillify, DRY, and MECE Resolvers\n18:23 — The Self-Improving Dream Cycle\n20:26 — The Two-Sentence Pitch Skill\n23:06 — How Super Intelligence Compounds\n25:10 — Recording Everything as a Building Layer\n27:10 — The Shared Organizational Brain\n29:18 — Trust-Default Culture as a Requirement\n30:44 — Raising the Floor for New Employees\n32:35 — Horseless Carriages\n34:24 — Why Chat Is the Best Interface for Agents\n38:50 — Just-in-Time Software\n40:49 — Centralizing vs. Decentralizing AI\n43:32 — The Personal AI Revolution\n\nApply to Y Combinator: https://www.ycombinator.com/apply\nWork at a startup: https://www.ycombinator.com/jobs"
notes: 'Auto-generated ASR cleaned: skill-fetched metadata via Playwright; transcript fetched separately via yt-dlp WebVTT fallback because the engagement panel timed out after 180s (recurring failure for ≥20-min talks per youtube-transcript-skill failure modes). VTT rolling-window dedup applied: second-line-of-each-cue content kept, inline <c>/<t> timing tags stripped, ~5-second buckets, HTML entities unescaped.'
---

## Transcript

[0:00] How do you build super intelligence inside a company? >> Part of the key thing is not to just use

[0:05] AI as a copilot. This is the the thing where you use it as the building layer

[0:10] for everything. And you need to start recording all the artifacts. >> It's like a shared organizational brain.

[0:15] It's like the closest thing to us being able to like connect our brains. If you

[0:20] frame this as a way for everyone in an organization to get better at what they do using the like collective skill and

[0:25] instinct of the people they work with,

[0:30] it's incredibly powerful.

[0:40] Today we have a real treat. Uh we have a special guest, general partner at YC, our partner Pete Kumman. He created

[0:45] Optimizely which was one of the first

[0:50] and one of the best ways to do AB testing for apps and websites. And since

[0:55] then he has gone on to create all of our agent infrastructure at YC. So literally

[1:00] all of our harnesses and how we use AI internal to YC. Pete, welcome to the

[1:05] light code. >> Thanks Gary. for the last few years since ChatgBTYC has been funding mainly

[1:10] AI companies and we've been we've gone

[1:15] through like many different like versions of advice for them about how to build AI native companies that build

[1:20] like mainly AI products and we've gone on a crazy journey with them learning

[1:25] all of this. I think a lot of people don't realize that internally YC is

[1:30] actually building and using a lot of the same stuff that we're helping our

[1:35] startups build and use themselves. And it's been I think a very powerful

[1:40] symbiotic relationship for us to actually be adopting these tools and like transforming our own organization

[1:45] which was started way way pre- AI into a super AI native organization ourselves

[1:50] and Pete has really been leading the charge for that. And so I'm really

[1:55] excited about this episode because I've actually been wanting to talk publicly about all the stuff that we've built

[2:00] internally and this is the first time that we're doing it. So Pete perhaps to start off you sort of go back to the

[2:05] beginning and like talk about like there was a particular like moment when we

[2:10] really started adopting these AI tools internally. It was really you who got us started down that path.

[2:15] >> Sure. uh happy to happy to tell the story here and it's I I like framing it

[2:20] that way because it was a project that I and and a few engineers got started about a year ago, maybe a little more,

[2:25] but that has since snowballed into just a whole infrastructure layer that's made

[2:30] it possible for us to use AI internally at YC in lots of different ways. And

[2:35] that's actually been one of the neatest parts about this is watching the whole engineering team and and many partners

[2:40] also just dive in and contribute to this this infrastructure layer. We started

[2:45] building our own harness inside of YC or

[2:50] kind of YC specific agents about a year ago and uh the original impetus for the

[2:55] project was some of the work that I and

[3:00] and a few of the software engineers at YC were doing with our finance team. Just for a bit a bit of backstory. So YC

[3:05] has for as long as it's existed, as far as I'm aware, run mostly on our own

[3:10] software in this era just given us a huge advantage, right? And so with that

[3:15] context, back to this this moment maybe a year ago, we were sitting down with

[3:20] the finance team, talking through a set of tools that we were going to build for

[3:25] them, uh, just to help them run through some of their finance workflows, booking

[3:30] journal entries, uh, logging priced rounds, like all the sorts of things

[3:35] that that make YC run really. I was seeing kind of two things at once. Like

[3:40] on one hand uh we you know we had this sort of loop going internally right

[3:45] where we'd sit down with the finance team. The finance team would describe to

[3:50] our software engineers how you know this complicated financial workflow worked and then the software engineers would go

[3:55] and build some purpose-built software where there was a deterministic workflow

[4:00] encapsulating everything that they had been told and then hand it back to the finance team and so on. And it felt

[4:05] really inefficient. And then at the same time, this was right around the time when agentic tools were really agentic

[4:10] coding tools were really catching hold, right? And so you had uh kind of the

[4:15] first generation uh windsurf and cursor that were well established by this point. I think this right around when

[4:20] cloud code was was introduced. I felt like this was giving me superpowers,

[4:25] right? Um and then kind of watching this sort of old classical way of building software in YC and then watching how I

[4:30] was doing things on my own machine. this it just felt like a bigger and bigger

[4:35] divide between those things. And so the original impetus was why don't we try to

[4:40] build some tools at YC that we could use to run agents that would give the finance team control over their own

[4:45] software, right? like remove the

[4:50] software engineers from this crazy loop where they have to sort of understand these complicated workflows and give the

[4:55] finance team the tools that they could use to encode their own workflows not not as you know not as Ruby uh but as as

[5:00] English with prompts right >> I mean what's interesting is like uh we

[5:05] all funded companies like maybe even like two or three years ago when LLMs

[5:10] were out but like agent coding wasn't a thing yet and so the first thing actually was not a coding it was LLMs

[5:15] for writing SQL queries. Yes. >> So that's what I remember from like the

[5:20] first versions of what you built was uh how like good it was and how basically

[5:25] it rhymed with like these other failed startups that we had funded like each of

[5:30] us probably funded one at some point. You know here it was it was working and

[5:35] it worked so well that non-technical people uh granted very smart people from

[5:40] finance but with no engineering background could use these tools to ask real questions. I was really surprised

[5:45] too to be honest and and so that we started with this kind of purpose-built

[5:50] thing for finance and then rewrote it to even more of a general agent loop right

[5:55] and it and it's this is now you see these all over the place now but um I the first kind of magical moment that I

[6:00] had was we had this agent loop and we had a tool registry a shared tool

[6:05] registry for kind of YC specific tools and the first tool that really was an

[6:10] unlock for me was I think a tool looking back that you actually built Jared. It

[6:15] gave these agents the ability to run readonly SQL queries against our

[6:20] database. Yes. >> Right. Um it was two tools actually. One was was running queries against our

[6:25] database and the other one was the ability to read our model files. I remember I built those tools and I felt

[6:30] a little bit like I was breaking the rules because initially we started with

[6:35] very limited tools that had very

[6:40] narrowly scoped domains and I kept getting frustrated because they weren't powerful enough to do the things that I

[6:45] wanted and so I was like what if we just gave the thing like access complete access to the production database where

[6:50] it could just like trample on anything and I sort of like surreptitiously

[6:55] pushed it out maybe late at Right. >> And it worked.

[7:00] >> It worked. >> It worked extremely well, right? >> Yeah. Perhaps foreshadowing, you know, subsequent things like OpenClaw where it

[7:05] turns out that like the thing that was hampering the world was being worried

[7:10] about security and privacy and all the things that could go wrong. And when you like worry a bit less, you're like, "Oh

[7:15] my god, these things are unbelievably powerful." It's it's another really good example of this weird split between I'm

[7:20] at work and I'm kind of operating in this really >> narrow box and I'm at home using clawed

[7:25] code or or or whatever like open claw her and I can do anything right um and

[7:30] and and trying to trying to narrow that gap. So why was this so useful? This

[7:35] ability to run SQL queries against our database. Sounds really simple. Well, I

[7:40] think this is where it's important to talk about one of the big advantages that I think YC had coming into this

[7:45] experiment. Uh which is that we run on our own software and all of that

[7:50] software sits on one Postgress database that has everything that's important to

[7:55] YC's world in it. You know, every company that we funded, there's a company's table, there's a there's a

[8:00] founders table, right? There's tables for our financial transactions. There's

[8:05] tables for the notes that I leave in our little internal CRM. Right? All of these

[8:10] functions that I think a lot of other companies farm out to third party SAS tools, we've built our own. And as a

[8:15] result, we have this database with every important piece of context that I can

[8:20] now ask questions like, hey, show me all of the investors who invested in a space

[8:25] related company in the last four batches. Right? It just turns out when

[8:30] when all of that context is in one place with a little bit of additional uh information about how the schema is laid

[8:35] out, an agent can go and ask any or answer arbitrary questions about about

[8:40] our business. >> That was a magic moment for sure when I first saw that. >> Yeah. >> The cool thing for me is that it didn't

[8:45] just make it easier to answer questions. It dramatically increased the number of

[8:50] questions that we would ask and dramatically increased the the scale and complexity of the questions that we

[8:55] would dare to ask where like you know in the in the old days back when we were using like BI tools to ask to ask a

[9:00] question like that you know like what investors have invested like in space

[9:05] related companies that would be like several hours of writing SQL and so like unless it was really important you just

[9:10] wouldn't bother. It's just another example of the you know this instance of Gvon's paradox that you get when you

[9:15] remove the amount of back and forth uh

[9:20] between different teams in order to get a thing done right if if in order to answer ask some kind of complex question

[9:25] about YC I have to go and knock on on you know the data science team's door

[9:30] and wait for them to get it through you know their backlog uh I'm just going to

[9:35] ask far fewer questions. I mean, there are people out there watching this who work in places that still use it. The

[9:40] majority of people live in that world still, and it's 2026, which is a little

[9:45] unfathomable, actually. >> There's a long way to go, >> I think, which is which is really

[9:50] exciting. >> I guess one question is how do companies that live in that old world could get

[9:55] sort of wings to move so quickly? Because our the magic for us was as you said, everything was the context was in

[10:00] one place that made it easy. You know, if you think about um data science

[10:05] historically, one of the first things that the Googlers had to figure out was a big table, right? And big table was,

[10:10] you know, instead of schema you and

[10:15] joins, you have one big table that um can be map produced.

[10:20] >> Yes. >> And so I think that that's happening again. And I would argue that that's happening now with um Karpathy style

[10:25] knowledge LLM wikis uh with Gbrain.

[10:30] I mean, that's what I'm seeing anyway. Like, you know, obviously I have I have

[10:35] an open claw. It has access to lots of lots of systems and then I'm normalizing

[10:40] it to my own schema that's relevant to me and the things that I care about. And

[10:45] it is like denormalization. It's you're taking data and you're putting it into a format that uh is more or less optimized

[10:50] for openclaw or Hermes agent like that particular type of harness to be able to

[10:55] ask questions. It needs retrieval, it needs rag, it needs graph rag, it needs

[11:00] uh you know hybrid RRF like there's re-ranking in there like you know all the things that everyone has learned

[11:05] about retrieval uh is now inside Gbrain. And then when you give the agents a soul

[11:10] and it and you give it uh the data and

[11:15] it knows you and what you care about like suddenly these things have insane wings. like I just kind of can't believe

[11:20] how it sees around corners and you might ask a question and it'll even you sort

[11:25] of interpret what your question was about and like give you a thing that

[11:30] frankly like it would take a human who really knows you well

[11:35] >> to answer um all that's possible now and so you know your question is like all

[11:40] the data is everywhere my answer from like the openclaw Hermes experience with Gbrain is like yeah you basically have

[11:45] to take that you're going to denormalize it and you're going to put it in in a format that is optimized for agent

[11:50] retrieval and understanding. You could wrap it in an MCP, but for whatever

[11:55] reason, I just like intuitively I'd be worried like it's still sort, you know,

[12:00] these things are really good at working with MCP and C like they're a little even better with CLI. It seems like you

[12:05] have to denormalize and do the big table thing, but you know, specifically for

[12:10] the agent. Looking back over the last year and a half, uh it feels like we're

[12:15] still kind of in the single player era of agents where the harnesses that have

[12:20] gotten really popular, right? Uh Claude Code, Codeex, Pi, OpenClaw, Hermes,

[12:25] they're all designed to be used by a single human running on a single

[12:30] machine. And it makes a lot of sense, right? Because in that environment,

[12:35] these these agents can do just about anything, right? And they they make you

[12:40] incredibly powerful. It's it's they're a lot of fun to use. I think one of the big problems uh that I don't think has

[12:45] been solved well yet by anybody is the multiplayer

[12:50] >> harness, right? It's it's enabling that kind of superpower, but on a team or an organizational level, right? And and and

[12:55] that's I think been the interesting thing to explore with the infrastructure

[13:00] that we've built at YC is watching which primitives that we've created that have

[13:05] enabled individuals and teams to use agents. you asked the question about if

[13:10] you're working inside of a kind of a legacy organization which is like anyone

[13:15] who's more than two years old uh uh what are the things that you can focus on uh

[13:20] in order to to help enable everybody at your org to use AI to to do more uh and

[13:25] we talked about kind of this common context layer right and so a data

[13:30] warehouse where just as much of your internal important context lives it just

[13:35] turns out is extremely useful there are many tools for connecting

[13:40] individual agent harnesses to uh you know other MCP tools, other other

[13:45] sources of truth. But just like a coding agent inside a monor repo just tends to

[13:50] be much more efficient, watching our agents operating on our single database

[13:55] that has everything in one schema tells

[14:00] me that there's a lot of value at least in getting all of the context into one place. Having an internal tool registry.

[14:05] This is I think the other really important thing that we've built. So in the beginning like we were talking about

[14:10] it was just the whole system was really simple. It was like an agent loop and a

[14:15] simple tool registry and you know a few other pieces right like a model router

[14:20] underneath. The tool registry is where most of the like YC specific stuff lives

[14:25] right. The tool registry is what turns these agents into something that's

[14:30] useful at work. and we had like 20 tools at the beginning, including this magical ability to query our our SQL database.

[14:35] But over time, teams have added more and more tools. Every time we kind of come

[14:40] upon some piece of work at YC uh that we think could be improved with an agent,

[14:45] we can just add tools. And there's more than 350 today. I just checked, right?

[14:50] Every team is adding their own tools. You know, I can do things like manage my office hours. Our finance team can uh

[14:55] you know, can book journal entries, right? we can help manage the events

[15:00] that we run. Uh there's tools for all of the important work that we do at YC. And now once these all exist in in in in one

[15:05] place, you can make them available to

[15:10] these internal agents that we've built, but you can also make them available to cloud code, you know, running on on on

[15:15] our individual machines. So those things above all I think were the important

[15:20] pieces that we built that if I were working in any other organization, I

[15:25] would focus on building. I mean honestly inspired by what you guys would did with tools like this idea of skillify in

[15:30] openclaw and then actually the most important the last part of skillify.

[15:35] Skillify is like this meta skill that I made in openclaw where it's like you just do anything in uh openclaw on

[15:40] Hermes. Hermes actually already has skillify. They call it something. It's like it makes skills automatically. But

[15:45] the most important thing I I think is actually like plugging it into the

[15:50] resolver which is like your agents.mmd with like the list of things that the agents can do and then like it links to

[15:55] the markdown entry point that like lets

[16:00] you use a tool basically. And so like this thing keeps coming up in all these different contexts like cloud code has a

[16:05] skill the skill registry in cloud code is actually a resolver. Our tool

[16:10] registry is actually a resolver. And then the weird thing that you have to do

[16:15] on top of that is actually um I have a meta skill called check resolvable that

[16:20] I call all the time. So I'm always like I do something that's new or different in uh in my agent and then after it does

[16:25] it and I like it I say skillify it and

[16:30] then it becomes basically like a tool call or method call and then I run check resolvable which is like you know look

[16:35] at all of the other skills and uh tools that exist and is it you know dry don't

[16:40] don't repeat yourself and is it uh mece

[16:45] which is you know I'm embarrassed to say a McKenzie term or um the consultants

[16:50] use for uh making really good slide decks. Mutually exclusive, collectively

[16:55] ex exhaustive. That's like how you're supposed to do slides if you're a Mackenzie consultant. But it's useful

[17:00] because it's like an additional layer on top of don't repeat yourself dry.

[17:05] >> And like the models just seem to know what those things are. And so if you have a dry and MECE

[17:10] resolver table anywhere, it's actually

[17:15] like the optimal resolver. Like it's bad to have 10 skills that do all the same

[17:20] thing. It's good to have one skill or one tool that has parameters that then

[17:25] let you call them. So I don't know. I think it's like this is like the wildest time to be alive as like an applied

[17:30] computer scientist because it's like simultaneous like discovery of the same

[17:35] useful applied concepts over and over again. And I wonder if like when people

[17:40] are, you know, developing the first versions of Unix or something, it's like discovering a stack and a heap. It feels

[17:45] like we're right at that moment today. Like we're just coming up with the new primitives for what an agentic system

[17:50] actually is. And you can see it in the parallel sort of development of like

[17:55] we're just trying to do a thing and it might be in Claude code or it might be in our own internal harness or it might

[18:00] be in OpenClaw, it might be in Hermes. Like these things just keep coming back over and over again. YC Startup School

[18:05] is back. We're hand selecting the most promising builders in the world and

[18:10] flying them out to San Francisco for July 25th and 26th to discuss the

[18:15] cutting edge of tech and startups. Apply now for your spot. Yeah, it's really

[18:20] interesting to look at how some of the other companies that are building this

[18:25] stuff uh have built their infrastructure because you see a lot of these same primitives in in each of them, right?

[18:30] Like there's the agent loops, there's tool registries, there's skill registries. looking at at at the way

[18:35] that we're using skills now at YC. So if you think of skill as a simple

[18:40] abstraction layer over tools, we have a handful of sort of shared skills uh that

[18:45] that we all have access to uh through this through this agent system. And it's

[18:50] been interesting to watch. I think you've talked about this where this progression of like in the beginning you

[18:55] were kind of writing your own system prompts and then skills emerged and so you started writing your own skills and

[19:00] then you would start uh metaprompting where you where you know you'd have the agent write a skill. Exactly.

[19:05] >> Improve the prompt. >> Yes. Automatically. >> Yes. Seeing us kind of do the same progression internally where we have a

[19:10] couple skills and now we've gotten to the point where we have these sort of

[19:15] autonomous self-improving loops, right? uh you know and so uh

[19:20] >> auto research from Karpathy again you know yeah or SLG goal now in codeex like

[19:25] they've they've incorporated it too >> we have this general agent that every night will go and read through all of

[19:30] the agent conversations that employees have had and look for uh things it could

[19:35] have done better and pieces of context that if it had up front it would have

[19:40] done more efficiently. >> This is open claw's dream cycle and GBrain also has a dream cycle. This is a

[19:45] um a skill improvement dream cycle, but it could also potentially um read all

[19:50] the transcripts and then write them back

[19:55] into the internal uh DB into the internal CRM on like what we know about

[20:00] people in companies. >> Indeed. And we we there are cool

[20:05] examples of using transcripts actually to make these skills more effective as

[20:10] well. One of the shared skills that we have uh is a skill that that partners at

[20:15] YC use to help our companies uh write what we call two sentence descriptions.

[20:20] Right? Everybody here has written hundreds of these. >> We should probably explain what a two two sentence description actually is.

[20:25] >> Sure. So, a two sentence description is a concise way of explaining what your

[20:30] company does in natural language that anyone will understand and why it's

[20:35] interesting. >> Sounds easy, but it's surprisingly hard for founders to actually >> and also no one does it. Weirdly, weirdly like even the most experienced

[20:40] founders like forget because they have perfect context. Interestingly, uh I now

[20:45] realize YC itself is a a context

[20:50] engineering uh sort of process in that like people we're frequently teaching

[20:55] people you have perfect context about what's going on in your brain, but great communication is replicating that same

[21:00] context in someone else's brain. And that's what a two sentence pitch is.

[21:05] Like what is it? Like I don't even know what the heck this is. And then second part is like is it interesting or

[21:10] valuable? What you know is it worth my time? And so that you know when I when I

[21:15] teach two sentence pitches that's my favorite way to do it is like do I even

[21:20] know what the heck this is? >> Yes >> because if you don't know what it is you can't even ask a question about it. It's like something about computers I guess

[21:25] whatever what time is lunch again. And then the second part is equally

[21:30] important which is like if I've heard that you know there are like 20 companies like there are five other

[21:35] companies in this room that do X like and then I don't understand like why

[21:40] this is noteworthy like again I'm like thinking about my pastrami sandwich again right so so the two sentence pitch

[21:45] like viscerally is important for

[21:50] founders >> and it's it's a it's a simple kind of atomic thing that every partner at YC

[21:55] has practiced over and over and over again I I think Tom, uh, one of one of

[22:00] the partners here wrote a skill that teaches an agent how to, uh, take some

[22:05] context about a company and can and condense that into a two- sentence

[22:10] description. And so that was his sort of handwritten prompt or skill about how

[22:15] that was done. And one of the cool things that happened in the last month or two was that a couple of the other

[22:20] partners took a meeting that they had with a a group office hours they had

[22:25] with a bunch of the companies in the spring batch and just went through and had every founder try uh their hand at

[22:30] at a two cents description and kind of gave them feedback and input. And so

[22:35] kind of the knowledge that lives in a partner's head about how to do this effectively was exchanged back and

[22:40] forth, right? and and and now lived in

[22:45] the context of of that meeting transcript and handing that back to the agent and saying given you know what

[22:50] you've learned by reading through this context improve the two sentence

[22:55] description skill and they got noticeably better after that like this

[23:00] thing is now better than I am I would I would argue at writing those >> this is how super intelligence happens inside organizations I mean this two

[23:05] sentence pitch thing sounds like something kind of small but uh embedded

[23:10] in it is actually something very powerful I'm sure you guys have heard um Jack

[23:15] Dorsey talk about what he's doing with block. He basically is trying to turn block into a mini AGI around helping

[23:20] people in the world make payments to one another, right? Uh and then this is

[23:25] actually the micro mechanism by which

[23:30] he's going to do that, right? like you can look at the operation of any

[23:35] organization as uh the aggregate of you know I mean the two sentence pitch at YC

[23:40] is that's sort of one of like thousands of things that I would argue we do for

[23:45] founders but you know we just walked through a very concrete way where

[23:50] someone wrote a prompt used it used a bunch more other people used it uh a

[23:55] bunch of artifacts came off of that around literally like the transcript of using it becomes a thing that can be

[24:00] used to metaprompt and improve in an automated fashion on a daily basis the

[24:05] operation of that one skill and then suddenly that one skill you just said it

[24:10] that skill is now better than any of us individually than be you know when

[24:15] before we actually had access to that and so this is like a particular like

[24:20] needle pin prick in the fabric of like how any organization does things and

[24:25] then how do you build super intelligence inside a company you do that on

[24:30] everything you do. And it's not more complicated than that. Like you literally just compose everything that

[24:35] you do and any given thing that any given person can do, you combine that in

[24:40] aggregate and in this particular process

[24:45] and like you have a super organization. It's possible now like every single person watching this can do this at any

[24:50] company at their own company. They can do it at their job. I mean, the interesting thing is that's why you

[24:55] should start a startup because people are going to be trapped in organizations

[25:00] with people running organizations that are very powerful and have all these resources and all this capital that do

[25:05] not believe what we just said >> because they keep all the context locked down, >> right? Because it's unsafe.

[25:10] >> It's unsafe. This is one of those things that we talk about um how to build an AI

[25:15] native organization, right? Part of the key thing is not to just use AI as a

[25:20] copilot. I think that's very 2023 4, right? This is the the thing where

[25:25] you use it as a really the the building

[25:30] layer for everything and you need to start recording all the artifacts like

[25:35] people wouldn't have thought of uh meeting recordings and I think it's one of those reasons why all these uh

[25:40] meeting recorders have been taking off. People have been finding them with coaching them on the meetings. But it's

[25:45] not just that. You could take that and improve all the output for you that you

[25:50] do like writing emails, communication, planning. You have the whole context of

[25:55] everything. >> It's funny. I remember the Dario essay where it's like there's some of the blockers and just the rate of

[26:00] progression of AI are not technical. They're just sort of like social cultural things. I think it's kind of

[26:05] like a really interesting example. two years ago it would have seemed I just remember it felt odd to just like record

[26:10] a meeting or like there was just like people trying to figure out what the like social etiquette around it was and

[26:15] like how intrusive it was and today I just feel like it's almost like default

[26:20] assumed that like most beings are being record especially if they're on Zoom but just in general like everyone started

[26:25] recording things now >> it's a little scary but I think if you frame this as a way for everyone in an

[26:30] organization to get better at what they do using the like collective skill

[26:35] and instinct of of the people they work with. It's incredibly powerful. Having a

[26:40] canonical two sentence description skill

[26:45] is not just a way to like generate a snippet of text for a founder. It's a

[26:50] way to help me get better at understanding what makes for effective

[26:55] founder communication. Right? because now I can tap into everything that Diana and Harge and you two have learned over

[27:00] the many years you've done this job which are now kind of baked into this skill through the conversations that

[27:05] you've had. >> It's like a shared organizational brain. >> Yes. >> The closest thing to us being able to

[27:10] like connect our brains, right? Yeah. >> It it it totally is right. And I I can have an agent now come and I can do

[27:15] practice sessions with it, right? and I can have it critique my like there there

[27:20] are so many possibilities once you get all of this knowledge into a place where

[27:25] an agent can can work with it. Uh it's a it's a it's a very empowering thing for

[27:30] every human in the organization. >> There's some subtle interesting things around here that like you know other

[27:35] people might get wrong that like I feel like we've gotten right. I mean one of them is by default the agent

[27:40] conversation is actually um globally viewable by any full-time employee at

[27:45] YC. you know, we sort of weren't sure about that decision. I mean, it felt

[27:50] right and it felt like living in the future, but it did not come easily. I

[27:55] feel like we had a lot of conversations about like, >> well, then everyone sees everything. Is

[28:00] that okay? And like, you know, what is not okay? And then I'm glad we made the choice to keep it open actually cuz I

[28:05] agree. >> People learned how to use it from watching how other people used it.

[28:10] >> Yes, we used that transparency to solve several problems at the same time.

[28:15] one, every agent conversation, as you mentioned, was broadcast internally to a

[28:20] Slack channel and anybody could join that Slack channel and look and learn,

[28:25] right? And I remember this is another kind of big unlock moment was when you started using it really heavily. You

[28:30] were like super creative with with the things you were doing with it. And a lot of us watch that was like, "Oh, wow. I

[28:35] didn't even to to use it that way." Right? It allows

[28:40] you to be a little more lenient on internal security, right? One of the things we talked about earlier was this

[28:45] trade-off where these agents are at their most powerful when they are given

[28:50] unrestricted access to lots of context which runs counter to the way more most

[28:55] organizations work. It turns out that by defaulting to public broadcast for these

[29:00] conversations, you kind of institute a bit of a social control on what people can do with it. uh that as we learned I

[29:05] think has been like reasonably effective

[29:10] uh inside of this high trust environment at keeping private information private.

[29:15] >> Yeah. What's interesting is um it it betrays two traits of uh truly agentic

[29:20] like 1000x super intelligent organizations that I would not have necessarily guessed would exist but are

[29:25] now like must exist if you want to create this type of organization. You

[29:30] have to be relatively egalitarian and you also have to be trust by default.

[29:35] And then neither of those things uh actually are most organizations in the world. If you're the founder of an

[29:40] organization, you actually have to have those at the core of what you're doing. >> And I think like that kind of

[29:45] environment honestly works best at startups, right? When it's a small group of people that are all aligned and and

[29:50] and and operating in a high trust environment. >> The other thing you have to do is be

[29:55] willing to spend like $10 to $100,000 a year on tokens. But if you're willing to

[30:00] do it and you invest in the skills and you like actually do everything in an

[30:05] open way with your team that way, like basically what I realized is it allows you to live in 2028, right? Like what

[30:10] you spend a h 100,000 or a million dollars a year on now it will be

[30:15] commonplace like in in two years, right? It'll it won't cost a h 100,000 in a

[30:20] year. It'll cost 10,000 and the year after that it'll be like a couple

[30:25] hundred bucks, right? and everyone will do it and we'll call it like this is how companies are now. So basically there's

[30:30] a one-time time warp where you can leapfrog every incumbent, all Fortune

[30:35] 500s, all startups that exist

[30:40] by doing this. >> Like I'm imagining in the '9s, I wonder if it felt similarly when companies

[30:45] started buying computers for their employees. Yeah, >> they were probably very expensive and probably only certain companies really

[30:50] invested in buying these like expensive flaky computer systems for their

[30:55] employees. But like what a superpower to have a computer when your competitors like don't have computers.

[31:00] >> I think more tactically how I've seen this affect uh YC has been raising the

[31:05] the floor >> floor >> the floor in a sense. What I mean by that is that you could have a new employee joining and maybe it would have

[31:10] taken them six months to ramp up. But with this, it's sort of like they

[31:15] automatically get a lot of the context from the company working and they know how the best people and the star players

[31:20] in the organization do things by apprenticeship automatically with AI

[31:25] instead of uh because partner time is expensive or sometimes the best people

[31:30] in an or they're very busy, right? And you get to kind of run the simulation of what it's like to be like Pete when he

[31:35] does like an awesome job coaching founders on sales or like Gary when he's

[31:40] like talking to founders and giving very specific advice. I think it helps all

[31:45] the new new entrance in the organization just be a mini version of you a lot

[31:50] faster. One of the first things that I appreciated about being able to use a

[31:55] coding agent was that all of the dumb questions I was too embarrassed to ask.

[32:00] I had no trouble asking asking the agent. And it this is kind of that same thing but at an organizational level,

[32:05] right? You're a brand new employee. You're embarrassed to ask. You don't want to bug hard with a with a question.

[32:10] And now you don't have to, right? And which onet means a lot more questions

[32:15] get asked and answered and people ramp up much more quickly. after you had

[32:20] built all of this agent infrastructure at YC, it inspired you to write this essay, Horseless Carriages, that went

[32:25] like pretty viral on the internet. Maybe you can like explain the ideas behind

[32:30] horseless carriages. I think is still very relevant now. >> It was a critique of a lot of the the AI

[32:35] software that I saw being built at the time. And to be totally honest, I think a lot of it still falls into

[32:40] >> It's still like that. Yeah. It didn't change. >> Yes. I just saw a lot of examples of uh

[32:45] companies building software and adding

[32:50] AI features by sort of slotting a little bit of AI inside of a lot of software,

[32:55] right? And and the example that I used at the time was the the kind of email writer that uh the the Gmail uh team had

[33:00] had shipped. But the the real idea underneath was just kind of that that

[33:05] the potential for AI is to shift control of software from the developer to the

[33:10] user, right? And and the the simple example I started with was basically

[33:15] that all of these kind of like AI as a little feature kept a bunch of prompt

[33:20] context about how the AI should do a job

[33:25] locked away and hidden from the user which was just this classic example of like well it's the developer's job to

[33:30] figure out how all of this stuff should work. So the developer should write that and we should protect the user from that

[33:35] kind of complexity. >> Safetyism. I hate it. >> Right. and and you know and and it's

[33:40] just again going back to this contrast between watching the way that some of these tools work and what it was like to

[33:45] use a coding agent on my computer that

[33:50] could do anything right and feeling feeling like I I had superpowers. I think the conclusion that this essay

[33:55] points to is that as we get better at

[34:00] building AI native software, it's going to look a lot more like the agent

[34:05] wrapping software deterministic tools rather than deterministic software

[34:10] wrapping AI, right? And we've done our best to expose that to internal

[34:15] employees with some of these primitives that we built. U but we have a lot we

[34:20] have a long way to go. the chat as the interface. I just feel something there's like things going around right now about

[34:25] how there's a need to build a new interface for like AI and what does that look like and I think that just comes

[34:30] from people who haven't like touched and felt it yet. Chat is actually pretty good because like you trust the agent.

[34:35] You increasingly trust the agent to do more of the work and you trust its decisions and you don't actually need to

[34:40] like have too much of a UI to go in and like review the things it's it's doing

[34:45] time for just in time software. Yeah, basically right like yes, occasionally you want it to present you like maybe

[34:50] like a specific view of something, but >> and it could make the software and build

[34:55] it as a single page JavaScript just purposely built for you at that moment.

[35:00] Yeah. >> And it could be a skill file that could be like called anytime you want. >> I was thinking a lot about this because

[35:05] I used to be in the camp that oh perhaps

[35:10] chat was not going to be the UI for all these AI applications.

[35:15] And I've definitely changed my mind. Part of it is after experiencing all these tools and I think the more I

[35:20] reflect upon it why chat is probably the better interface is because it's the

[35:25] closest thing to human language and human language and writing is basically the closest thing to expression of

[35:30] thinking. >> So chat is the closest stepping stone to

[35:35] clear intelligence. >> Yeah. >> So you can't just put it in a box. I

[35:40] think it just constrain us too much to have a very specific box. So that's why I thought it's like okay all in with

[35:45] chat interfaces. I used to be in the other camp and it's like >> it's multimodal. I know we've talked

[35:50] about like Telegram is not ideal but I actually Yeah, it's pretty good.

[35:55] >> I mean the voice memos sometimes when I don't want to type you just do the voice memo and it's it feels like I'm talking

[36:00] to >> I can give my claw like I can give it text. I can give it voice. I can give it pictures of things like I can give it

[36:05] files. Like it's like pretty good. >> Yeah. I just experienced this. So like

[36:10] January, I think the last episode we did, I just talked about this. It's like I spent January and through February

[36:15] building a half a million lines of code for a Rails app, which was Gary's list.

[36:20] And it was like, you know, I know people make fun of me for like it was a blog, but it was like I built the blog in like

[36:25] the first week. Like I spent a month and a half building a full agentic framework

[36:30] that did like my own version of deep research and like fact-checking. But the

[36:35] thing is I built it the way I would have built software in 2013. The last time I wrote code, it was like the web 2.0

[36:40] version of this. And Cloud Code lets you do that. And uh what's crazy to connect

[36:45] is like I'm working like I don't know, I think I wrote like 40,000 lines of code

[36:50] the last 3 days just for Gbrain. And Gbrain is basically Gary's list 2.0,

[36:55] but it's totally open source, right? So

[37:00] everything I had to write for uh agentic retrieval, everything I had to do for

[37:05] voice extraction, everything I had to do for factchecking, all of that now exists

[37:10] inside Gbrain. And I just gave it to my, you know, Gary's list team yesterday as

[37:15] their own openclaw instance. And they're flying now, right? like they were

[37:20] complaining about like I had made you know this monolithic writer chat interface and it was like full of bugs

[37:25] because I was like reimplementing things that openclaw and telegram already do

[37:30] and now they just use open andclaw telegram and my retrieval system with

[37:35] like all the same data that I extracted it out and with our MCP and it's working

[37:40] great like basically you know Gary's list 2.0 know the next rewrite

[37:45] thankfully is not half a million lines of uh Rails code that is like insane to

[37:50] actually you it's rigid it's uh takes a long time it like takes like 10 times

[37:55] long you know even though it was 1/100th the amount of time to do it like by hand

[38:00] you don't have to do it by hand like that half a million lines of code in Rails is easily like 10,000 lines of

[38:05] like TypeScript and like maybe 2,000 lines of markdown and all of that is way

[38:10] more dynamic like you you could just say like actually for the second paragraph

[38:15] uh I really like including a biography of like the politician we're focusing on

[38:20] and it's like I don't have to code that in Rails. I don't even have to write

[38:25] that into um a Ruby file that then gets evaled in like you know my complex eval

[38:30] infrastructure like OpenClaw just knows that and I have an eval skill. my

[38:35] editor-inchief can just change it on the fly and I didn't touch it. Yes.

[38:40] >> And it's like this is insane actually. Like this is actually the dawn of just in time software and I can see it right

[38:45] now. The best AI software that I've used whether it's inside of YC or or tools

[38:50] that others have built tend to be very

[38:55] small and just add kind of the smallest amount of code ahead of time that you

[39:00] need in order to let the model shine. >> Mhm. And you can build an awful lot with

[39:05] that, right? I can write tens of thousands of lines of code uh like like

[39:10] you're saying, but the ability to start at this like extremely simple thing that

[39:15] I need to to understand very little in order to use is incredibly powerful. And

[39:20] I think that's I think most software in the future is going to look. >> We were talking about this earlier, but I think that is what open core did

[39:25] really well. Like there were like a few things that you want. You wanted like

[39:30] some ability to give it a bit of personality. you wanted it to like persist and last for a long time and

[39:35] have some concept of memory and it's not like perfect but that's like actually like good enough as like for that use

[39:40] case >> claude code too every time Boris comes and speaks at he spoke with Diana

[39:45] earlier this week one of one of the things that really stands out is how

[39:50] obsessed he is with simplicity with just like making the product as small as

[39:55] possible >> my favorite example of this is is uh the this open source harness called Pi which

[40:00] is a >> that's what technical uses out of the box coding agent. >> It's this beautiful piece of software

[40:05] which is just like the smallest possible coding agent. You can use PI to ex

[40:10] modify and extend PI, right? And it's this kind of idea of like self-extending

[40:15] and self-referential software. It's really fascinating and you're right, OpenClaw was built on top of that. One

[40:20] of the things I'm very curious to see is how many other sort of pieces of classic software emerge in this form as this

[40:25] kind of minimal thing that you start with uh and then use an agent to extend

[40:30] over time. I think more and more I mean looking at honestly the benefits that

[40:35] we've gotten from having our own customizable software. I suspect that a

[40:40] lot of commercial software uh will come with this capability uh out of the box

[40:45] in the future. There's a really interesting subtle thing that I wanted to talk about around like what I learned

[40:50] from your essay uh which is like AI can either be centralizing or decentralizing

[40:55] and um the Google Gmail like I can't change the prompt thing is like the

[41:00] perfect example of that. We basically have a choice to be made over the next I don't think it's even that long. I think

[41:05] it's like 18 to 24 months. It might take five years, but um there are sort of two

[41:10] scenarios and uh what comes to mind is literally like the uh 1984 Macintosh

[41:15] commercial by Apple >> where it's like is 2034 going to be like

[41:20] 1984? And you know the 1984 case would be we have centralized control. Like

[41:25] there are five kings. There's only you

[41:30] know one of them maybe wins. They have the most advanced AI. They have uh end run around all compute and power. They

[41:35] have all the space data centers cuz they could you can't build any terrestrial

[41:40] data centers in America anyway. There's this like centralization of control. And

[41:45] not only that, they don't let you run your own prompts. like they literally do

[41:50] the Gmail thing but like for your whole computing existence, right? And this

[41:55] would be as if like personal computers never existed and there were only mainframes and mini computers. Like this

[42:00] is sort of lost to the sands of time. But you know in the 1960s and '7s when

[42:05] computers first came out like you couldn't go to the store like you can today. You couldn't go to an Apple store

[42:10] and just buy an iPhone let alone uh a Mac. you had to get access to like this

[42:15] thing that was worth like hundreds of

[42:20] thousands of dollars to millions of dollars and >> it was like and it was like tightly locked down by corporate policies.

[42:25] You're right. And the and the thing that really spurred the computing revolution was when people started having personal

[42:30] computers that they could experiment on. >> Yeah. And there's like the priesthood, right? There was a small priesthood and

[42:35] an institutional base that controlled capital, literally the means of

[42:40] production. And so, you know, this is like a coherent future that we could

[42:45] live in that I don't want to live in. And the alternative to that is actually

[42:50] uh embedded in the homebrew computer club. It's embedded in the revolution

[42:55] that Steve Jobs and Steve Waznjak gave us when they were in the garage in Mountain View literally soldering

[43:00] together breadboards and they like sold 500 of these Apple Ones. And I think

[43:05] we're at the Apple 1 moment right now. We are coming up with the primitives. We're learning how do these things work

[43:10] and how do we sell it and how do we package it. Uh but then there's like a

[43:15] lot of choices right now right like most people the mass you know a billion users

[43:20] use chat GPT and chatpt like gives you a

[43:25] little access but MCP is really locked down. You actually you know can't hook

[43:30] things up to your own databases that easily. Um, and you know, for what

[43:35] safety, like I would argue Claude is like a little bit more open, but not really. Perplexity Computer is probably

[43:40] the best version of it, but it's still like, you know, pretty limited compared

[43:45] to what you could do with OpenClaw and Hermes agent. And so, what does the uh

[43:50] revolution look like? That is like the true personal AI moment. And that's what

[43:55] I hope that we are building with things like Gbrain and you know Hermes agent

[44:00] and openclaw like the ability to run your own software to change your own

[44:05] prompts to test all of it to have your

[44:10] own private repo that like you know is only yours um to be able to choose which

[44:15] model to use and maybe it's an openweight model like to me that's sort

[44:20] of the white pill for AI is uh we could have corporate control, no control of

[44:25] your own prompts and like literally the AI happens to you. You know, you're

[44:30] under the API line or like there's this other alternative where I want like a

[44:35] billion people to actually control and program for themselves. What are these

[44:40] things? This should be an extension of yourself and what you care about, not

[44:45] what you know, Meta or Alphabet or even OpenAI or Anthropic care about. I always

[44:50] really bristle when I see AI framed as a

[44:55] way to replace people because it just doesn't match the way that I have experienced it and the way that so many

[45:00] of the people around me have experienced it not as a replacement for humans but

[45:05] as a thing that empowers. If you look at at at kind of how tech has developed since the era of of mainframes to PCs to

[45:10] the internet which gave everyone like a publishing platform to like it's it's a

[45:15] story overall above all of individual empowerment and I think AI uh is going

[45:20] to play out the same way. I think it is going to enable us to do more uh than we

[45:25] could before. I think it's going to eliminate kind of the drudgery style

[45:30] work that like made a lot of my job painful in the past. To me it's like we have to make choices to do so. By

[45:35] default like a company is not open by default. A company is uh command and

[45:40] control by default. Maybe the leadership gets access to these tools but like the

[45:45] you know line level people the staff people don't right and like we need like

[45:50] a radically different type of organization and we need to actually offer computing in a different way and

[45:55] um these are all choices and the people who are watching are going to be the

[46:00] people who build all these things in society. So, we better choose well.

[46:05] Well, that's all the time we have for today. I mean, I think we covered some pretty heavy stuff, but Pete, thanks for

[46:10] joining us. >> Thanks. >> Thank you. >> Thanks for watching, guys. We'll see you

[46:15] guys on the next one.

