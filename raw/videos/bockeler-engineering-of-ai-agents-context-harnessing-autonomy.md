---
title: 'The Engineering of AI Agents: Context, Harnessing, and Autonomy'
video_id: _R83pFpUWyM
url: https://www.youtube.com/watch?v=_R83pFpUWyM
channel: InfoQ
channel_id: UCkQX1tChV7Z7l1LFF4L9j_g
channel_url: https://www.youtube.com/channel/UCkQX1tChV7Z7l1LFF4L9j_g
publish_date: '2026-05-06T21:09:45-07:00'
upload_date: '2026-05-06T21:09:45-07:00'
category: Science & Technology
duration: '42:01'
length_seconds: 2521
view_count: 12917
is_live: false
thumbnail: https://i.ytimg.com/vi/_R83pFpUWyM/maxresdefault.jpg
keywords:
- QCon London
- InfoQ
- Transcript
- Artificial Intelligence
- AI
- AI Agents
- Software Architecture
- Generative AI
- Software Engineering
- Claude Code
- GitHub Copilot
- Context Engineering
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: 'The Evolution: From Autocomplete to Agents'
  start: 0:00
  start_ms: 0
- title: What is Context Engineering? (Rules, MCP, and Skills)
  start: '2:15'
  start_ms: 135000
- title: Modularizing Context with Anthropic Skills
  start: '5:30'
  start_ms: 330000
- title: 'The Cost Reality: $380/day per Developer?'
  start: '8:45'
  start_ms: 525000
- title: Subagents and Research Workflows
  start: '11:20'
  start_ms: 680000
- title: The "Lethal Trifecta" of AI Security Risks
  start: '14:05'
  start_ms: 845000
- title: 'Harness Engineering: Building Deterministic Safety Nets'
  start: '17:50'
  start_ms: 1070000
- title: 'Maintaining Quality: Structural Tests as Feedback Loops'
  start: '21:10'
  start_ms: 1270000
- title: 'The "Goldilocks Speed": How much velocity do we actually need?'
  start: '24:40'
  start_ms: 1480000
- title: 'Final Thoughts: Scaling AI Autonomy Safely'
  start: '28:15'
  start_ms: 1695000
description: "As we move from simple autocompletion to autonomous AI agents, \"vibe coding\" isn't enough for enterprise-grade software. \n\nBirgitta Böckeler (Thoughtworks) explores the shift from prompt engineering to \"Harness Engineering\"—the practice of building deterministic safety nets around non-deterministic models. \n \n⏱️ Video Timestamps (For Navigation)\n0:00 – The Evolution: From Autocomplete to Agents\n2:15 – What is Context Engineering? (Rules, MCP, and Skills)\n5:30 – Modularizing Context with Anthropic Skills\n8:45 – The Cost Reality: $380/day per Developer?\n11:20 – Subagents and Research Workflows\n14:05 – The \"Lethal Trifecta\" of AI Security Risks\n17:50 – Harness Engineering: Building Deterministic Safety Nets\n21:10 – Maintaining Quality: Structural Tests as Feedback Loops\n24:40 – The \"Goldilocks Speed\": How much velocity do we actually need?\n28:15 – Final Thoughts: Scaling AI Autonomy Safely\n\n\U0001F517 Transcript available on InfoQ:   https://bit.ly/4we3odZ      \n   \n#SoftwareArchitecture #AIAgents #GenerativeAI #SoftwareEngineering #ClaudeCode #GitHubCopilot #ContextEngineering"
notes: |-
  Transcript fetched via youtube-transcript-api fallback after the Playwright path hit 'transcript panel did not render' timeout (GH #2 known failure on videos >=20 min). Caption track is ASR (auto-generated, kind=asr). The fetched chapter records had start_ms=0 for every chapter (parser bug on this channel's description format); start_ms was recomputed at ingest time from the 'start' mm:ss string so chapter-based grouping works. Light cleanup applied: dropped [music]/[applause] non-speech markers, normalised '>>' / '>' speaker turn markers, preserved YouTube's chapter list as ## headings, grouped consecutive segments into ~12-second windows with [mm:ss] timestamps.
---

## [0:00] The Evolution: From Autocomplete to Agents
[0:11] Yes, I was here last year at QCon, so about a year ago, and I gave a talk over with the title from autocomplete to agents, and I tried to just give a bit of the lay of the land of where we are in terms of AI coding, because as Blanca
[0:24] said, everybody's a bit overwhelmed, including me, even though I can I have time to look into this topic full-time. And I'm try I'm going to try and do something like that again today. And so, a year ago, I was mainly talking about
[0:38] the new agentic modes that at the time everybody was starting to pay attention to. The term vibe coding was about 2 months old at the time, I think. MCP was all the rage, and
[0:52] Claude Code was still in diapers, I think. Like, it was already kind of there, but not generally available yet. So, that's kind of where we were about a year ago. And so, I try to kind of reflect on the high-level kind of things that that
[1:06] happened over the past year. And one of the things is that context engineering evolved. So, this is also a term that wasn't even around last year at QCon London.
[1:18] This started being a term that it started floating around around June. And it basically the simplest definition of it is you want to curate the information that your model or your agent sees to get better results. So, that's the
[1:31] simple definition. Means different things, like when you're building an agent or you know, using a coding agent, which is what I'll be talking about right now. And again, a year ago, I
[1:43] had a slide that was similar to this one, that was talking about the kind of the state of context engineering at the time for coding agents, which was rules files. So, you just have like an agents.md, a cloud.md file in your
[1:55] workspace, and every time you start a session with an agent, the agent gets sent this file. So, you can kind of put typical pitfalls, repeated errors in there. So, I had a thing like my agent kept forgetting to activate the Python virtual environment every time it ran a
[2:08] Python process, so you would put stuff like that in there. And MCP servers were also around at the time, as I said, which which help you

## [2:15] What is Context Engineering? (Rules, MCP, and Skills)
[2:16] get help an agent get more dynamically get get data. And so, since then, there've been all of these things, right? Not just rules and MCP servers, also commands and skills
[2:28] and subagents and plugins and specs and, you know, so there's been a lot of activity in that in that space. Um and I just want to like zoom in on one of those things because it's been confusing
[2:41] to quite a lot of people, I think. I took a sabbatical the end of last year, and when I came back, skills had come out, and I was very confused at the beginning what exactly it is. So, I'll try to zoom in a little bit on that. So,
[2:54] um one thing that skills help you do So, first of all, this was this was a new concept introduced by Anthropic based on a lot of different things that had already been going on. And so, what it basically is, one, it
[3:08] helps you modularize [clears throat] those rules that I was talking about. So, you don't just have to have one big file in your workspace that always gets sent to the agent, but you can have like little subfolders that yeah, that modularize the different
[3:21] things you want to tell the agent. So, it can be from like here's how we usually build a React component all the way to here's how you get logs from our AWS test environment. Um And so, these
[3:34] modules can then be loaded by an LLM just in time. So, that's another big thing. So, this kind of progressive kind of lazy loading of context. And the the agent or the the large language model
[3:46] will just get a description of the skill. So, here it's just like a get log skill, and the description says get from our test environment for example for debugging incidents. And then when the large language model realizes oh that seems to
[3:58] be what we're doing there is more information on that then it's just going to load that so it's not filling up your context window from the start. Um then the next thing with skills is that they can include more files than
[4:10] just this markdown file. So you can have additional documentation in this folder. You can have a you can have scripts in this folder that you want the the agent to to execute. So you can have like it's a folder it's not just one markdown
[4:23] file. And then as I mentioned um so you can have scripts in here as well or you can refer so that I mean this you you could do this before but it's been a thing that more people have caught on to now that you can just
[4:37] tell the agent in the markdown file to use the CLI that is installed on your machine. And this is kind of like the realization that has had a lot of people shift a lot of their use cases away from MCP in agent coding and just like
[4:52] paid more attention to what CLIs do we already have on our machine what scripts can I write to have my agent do that because you know it's a lot more straightforward than having yet another different type of process running on your machine.
[5:06] So in a nutshell context engineering is a combination of the following things. So one it's of course as always reusable instructions and conventions right? So it's it's you know how do you write a react
[5:18] component? How do you um how do you bootstrap a new project stuff like that but also just like coding conventions and stuff like that. And that is combined with kind of like context interfaces right?

## [5:30] Modularizing Context with Anthropic Skills
[5:31] Things like the description of the skill or things like the the list of tools that an MCP server has or the list of tools that are built into the coding agent. So all things that the LLM can then take and say oh in this situation I
[5:44] want to call this tool I want to load that skill I want to call this MCP server tool. So, it's all about how can you get this to be intelligently loaded just in time?
[5:56] There's always non-determinism is always involved with this, right? So, you never have a guarantee that the LLM will actually decide to load your skill. Um and as a human then my job becomes a lot to manage that context and also to
[6:09] manage and monitor the context size. Because even though context windows are of course a lot bigger now technically than they used to be a year ago or especially 2 years ago, still when they kind of
[6:22] get full, you can kind of feel the the performance the like the effectiveness of the agent degrade and also of course like it starts costing a lot more money, right? Because every time you go back and forth
[6:35] with the with the model, you send like the full context window. So, there are now encoding agents, there are different features to help you monitor what's actually in your context. And it's actually quite interesting to also see all of the things that take up space,
[6:48] right? So, on the left here is a session that I started with Claude Code and it was actually very shortly after I started the session, so I hadn't even typed a lot and already the context window is 15% full because there's Claude Code system prompt, there's all
[7:01] of these context interfaces like skills that I have and stuff like that and so that will be um you know, that's also part of you know, how you have to balance your skills and all of the things that you give to a coding agent.
[7:15] On the right is also like yeah, GitHub Copilot also has that feature. So, at the moment it's basically um Claude the Claude Code team is leading the pack and then everybody else copies what they're doing. It's a little
[7:28] bit the high-level summary. Um And then finally a really powerful feature that I would also see as part of context engineering which started becoming more popular last year as well
[7:42] is sub agents. So, a lot of the coding agents have that built in now. So, it's this idea that the domain agent can spawn off sub agents, right? And the most common use case of that that, you
[7:55] know, we don't even control but that the the agents often decide to do is that when you start a session and the agent wants to research what's in your code base, it often spawns a sub agent to do that. Like, I don't know if you could Some of
[8:07] you might be able to read that. On the bottom right, there's a cloud code screenshot that shows this agent. So, then because like research often takes up a lot of tokens because it has to read a lot of files and stuff like that and find the ones that are relevant to the task. And then it just reports back
[8:20] the result to the main session and the main session doesn't have all of the potentially like over um you know, overload of like some stuff that it doesn't have to know. Um but you can also use this yourself.
[8:32] So, a very common uh use case for sub agents that we as users try to do is like a code review agent, right? A lot of people like to have a kind of a separate context window that doesn't know about all of the history in the

## [8:45] The Cost Reality: $380/day per Developer?
[8:45] session do a code review or maybe also uh have that use a different model and so on. So, this feature has like unlocked a lot of other stuff that I'll also be talking about in a few minutes.
[8:58] So, in the context engineering area like uh ask yourself like what coding conventions do you want to amplify because all of this is like is is a way to amplify things with AI, right? Good stuff and bad stuff. Right? So, it's
[9:10] also you have to be careful. What workflows can you maybe build for our modernization initiatives? Like migration is a super good use case for generative AI. And now with some of these uh um these uh options in the
[9:23] coding agents, it's becomes uh easier to build something like that. I just recently talked to a colleague who was uh working with the client who had thousands of uh CICD pipelines in an older tool that they wanted to migrate to GitHub
[9:36] Actions. And she was building kind of like a workflow, uh you know, a human supervised workflow with different sub agents and skills and MCP service and stuff like that.
[9:49] What tools should be available in your organization to make it easier for an agent to take certain actions or to get information. So, that can be CLIs, it can be MCP servers, maybe also language servers.
[10:02] I'll I'll get a little bit back to that later, but like if you have um yeah, maybe more unusual languages where you can give the agent more uh um information and tools that actually
[10:14] understand how the language works. Um yeah, and not only like coding conventions, but also what are practices you want to amplify. Like my favorite examples that I always mention are things like improving an architecture decision record or how do you do threat
[10:27] modeling, stuff like that, right? So, you can have those and skills as well to help um help people actually understand those. There are a few lots of open questions as well. So, context engineering is a little bit engineering in quotes, right?
[10:40] So, like how do you version and distribute these? So, there's like first ideas, there's now these plugin marketplaces, some of you might have heard of them. Also again introduced by by Anthropic and the Cloud Code team. Um but it's still not quite mature, it's
[10:54] all a kind of like evolving. And also a big question of course is is the context that you have is it making things better or worse, right? And this is all about evals, evaluation of the skills. So, again Anthropic just released something
[11:08] to make it easier to to do something like evals, the skills registry Tessell also released something recently. So, that's kind of like in the early stages as well. So, with all the model improvements that

## [11:20] Subagents and Research Workflows
[11:21] have that of course have also been happening, right? And this more powerful context engineering, there's been this like trend towards more giving agents more autonomy and like reducing human supervision, right?
[11:35] I guess that's what all the hype is always about like when can I just, you know, have AI build all of my code, right? So, supervised kind of like me as developer I sit in front of the computer in front of the session and I still kind
[11:47] of like look what it's doing and I steer and there's a lot of back and forth versus unsupervised. This is a screenshot from like mid of last year when OpenAI's Codex first came out where
[11:59] you basically have these cloud agents, right? You send you just send it off in the cloud maybe for 20 minutes or something to do to do something for you. And at this point like a lot of the big
[12:11] coding agent products have this ability for you to not only have agents work locally in the IDE, but also in the cloud. So, top left here is cursor, bottom right is cloud code. I think Copilot has this as well. So,
[12:26] and of course now you can also do this from your mobile phone, right? So, people starting to code on their commute to work if they have one, I guess. And then and but another option to do this like you can use these
[12:39] cloud agent coding agent platforms, but another way to do this is also that because there's been this rise of CLI based coding assistance. So,
[12:51] again every one of the big products now also have a has a command line based version of it. So, there's a cursor CLI, there's a Copilot CLI. The first first one that got a lot of attention of course again is cloud code and because
[13:05] you can run them in headless mode, you can also put them into your existing pipeline systems, right? So, for example, there are GitHub actions for cloud code and and and Copilot and so on.
[13:17] So, as part of this familiar beast rears its head, right? Which is we have to sandbox this somehow, right? Or we have to give the uh the agent uh a proper environment. So, we have to uh figure out how to give it all of the
[13:30] tools that it needs, all of the compilers, all of the dev tools, and so on. Uh out of memory error is just like an uh representation of like uh you know, we have to we have to give these the right amount of resources and stuff
[13:43] like that. Um internet access is in in our um CSD pipelines with uh dev sandboxes is already a big question, like how much internet access do we give it or not. And there's like new concerns now with agents uh with like prompt
[13:55] injection, right? When they when they uh load maybe untrusted content um on the web. So, there's like a few new question, but some of it is also is also like existing challenge that we have,

## [14:05] The "Lethal Trifecta" of AI Security Risks
[14:06] right? And not just in the cloud, but there's also a trend to less supervision locally. So, this is a um this is a a visual from um Steve Yegge's uh Gas Town
[14:18] blog post, which maybe a lot of you have read, where he's saying, you know, kind of like the it says the uh the eight stages of dev evolution to AI, and stage six here is having three cloud code instances in parallel on your machine, and stage uh
[14:32] seven is 10 instances in parallel. I tried the three instances, and it's a lot. Like I kept typing the wrong thing into the wrong session and stuff like that. So, it's like but it is something that uh in some teams out there is is um
[14:48] actually happening, right? And so, that last picture there, the stage eight, is like a short intermezzo for the the hype du jour, when I call it, which is um agent swarms.
[15:04] And Gas Town is an example of that. And there's this project Cloud Flow that has been around for quite a while. I think it was recently renamed. Um I unfortunately forget the new name. And there were these um two experiments recently by Cursor and Anthropic as well
[15:17] that got a lot of attention. So, by agent swarms, I basically mean you send out a lot of agents, like dozens or a hundreds, right? So, you kind of like throw as many agents as you can at the wall and you see what sticks and maybe
[15:29] are they going to be like emerging new behaviors, how do we coordinate those and so on. And those experiments by Cursor and Anthropic made a lot of people nervous, I think. So, Cursor basically had a bunch of agents run for I think the
[15:43] longest run was for a week to build a browser and Anthropic had them build a C compiler. And so, then people were like, "Oh my god, this does mean now, you know, AI is already there. It can build these things." Like one thing to keep in mind with these two
[15:56] is that both of those use cases, and they were probably also specifically picked for that. Cursor actually also say they specifically picked the use case. Both browser browsers and C compilers are very, very well-specified problem.
[16:09] So, and the specification is all over the internet. And also, especially in the case of the C compiler, there's even a very, very elaborate test suite that the agent can use to get feedback on if it works or not. So, that's and that's often like
[16:23] what we don't have when we build like enterprise software, right? We don't have it to to that level. So, I don't think you necessarily have to go and try like Gastown for like the
[16:35] context of probably what a lot of y'alls work environments are, but if you want to still like dip your toes into this, a good way to do that is also Claude Code released a feature. This is like in in preview, so you have to like switch
[16:49] preview flag, I think, which is called agent teams. Some people use agent teams and swarms as like the same thing. I kind of like to think of them conceptually as as two different things, right? You either send out like
[17:03] dozens and hundreds of agents that AI even decides which ones to use or maybe you can also do it in like a smaller context, right? Here I was trying this with five agents, I think. And so, the the key is that there needs to be a lot
[17:16] of orchestration, right? So, the main agent kind of decides what can be paralyzed. Um they can also talk to each other and stuff like that. But, this is all like still um early days, I would say. So, um
[17:30] let's go back. Let's uh back to the present in the less supervision like some things that you should be asking yourselves like, "What do you want to experiment with those cloud agents or with like less supervised agents, right?" Um depending on your
[17:42] environment, you might not want to take like large risks, but you can uh experiment with um things like cleaning up feature toggles or like lots of

## [17:50] Harness Engineering: Building Deterministic Safety Nets
[17:50] people again use like code review agents and stuff like that. Um and then how do you gauge the appropriate level of supervision for a task? And also how do you help people in the organization gauge that that level of
[18:03] supervision that you should choose? And so, I found myself um doing a lot of like micro, sometimes macro, but like lots of little risk assessments when I use AI. Should I use it for this? Should I not use it? How
[18:16] much review should I uh apply? And uh so, risk assessment is always in in any uh situation a combination of three things: probability, impact, and detectability. And in this context for
[18:29] me that is first uh I think about the probability that AI might get something wrong. And that probability uh depends like I assess that by my knowledge of the context I've given it, by my
[18:42] knowledge of how good the tool works, by my experience of using it for similar things before. So, it's something that, you know, like an intuition you have to build up over time using these tools. And uh it's also about stuff like how confident am I
[18:55] even in my requirements? So, how well can I even specify what I want? Impact of course is if impact if AI gets something wrong is all about the use case criticality, right? Is this uh proof of concept or a spike? Or is this
[19:08] something that will get me out of bed at 2:00 a.m. in the morning on the weekend because it's a critical workflow and I'm on call. And then the detectability is about it's the detectability that AI got something
[19:21] wrong. So, this is all about me knowing my feedback loops. And then by assessing that, I make a decision about like which type of workflow I use. Like do I use a very super elaborate one
[19:33] with like lots of planning in the beginning and stuff like that or do I just like start with the quick prompt? Uh it also determines how much I review. So, I don't do I just like fully vibe code and not look at anything or do I look at every single line of code or
[19:47] something in between? And also how long do I let it go off without supervision, right? Because the longer it goes off without supervision, um the more I'm I have to review afterwards and actually
[19:59] see what happened. And if you look at these things, actually only the thing that I have highlighted in yellow here now, like knowing the context and knowing how how good the AI is at this type of task, that's the new thing, right? All of the
[20:12] other things an experienced developer at least should already be be good at, right? But this is kind of like the skill that we have to hone. And it's also about like you have to be this tall to to ride the roller coaster.
[20:25] You have to be this tall to reduce supervision, right? So, the probability that AI gets something wrong can increase with like a bad code base, right? Because it will pick up on existing patterns. It can increase with
[20:39] like you have like a very you have a system where things are in lots of different places. So, it has like a lower chance to actually get all the information. Detectability is also something like if you don't have feedback loops, if you don't have good test automation and stuff like that,
[20:53] then you have fewer ways to both yourself verify what happened but also give the agent the ability to verify that. And there's more things to be cautious about, of course.
[21:08] Um

## [21:10] Maintaining Quality: Structural Tests as Feedback Loops
[21:10] So I talk I also talk a bit about security and cost. Also two things that have uh changed over the past year, but maybe not in a in a direction that we like. First of all, security, like almost every week now there's some like report
[21:24] of something happening, right? Like so one of the So it's usually all related to prompt injection. So this idea that an agent gets content from an untrusted source that might give it instructions that you
[21:36] weren't aware of, right? So uh and one thing that can happen with that is unwanted command execution. So all of the agents have like these allow list uh features in them that let you you can also configure them to say with this
[21:50] pattern or for these commands I usually, you know, you don't have to bother and ask me if you may execute that, but for other ones you maybe always want to say yes, you're allowed to yes, you're allowed to. But there are like some weaknesses in the implementations of these and that combined with like other
[22:03] stuff still not being quite figured out and with AI being non-deterministic is like a risk. Um another security risk is the extraction of secrets. This was just from What is it today? This is from 11 days ago, I think. Um there was like uh
[22:17] um so this is like a big risk is especially for um open source projects that uh are open for GitHub issues by anybody, but then immediately trigger like an agent without much supervision. And so
[22:30] this one actually managed through like some prompt injection in a GitHub issue to extract the secrets that allowed the attacker to push to the NPM registry for this particular uh tool.
[22:42] So it's like not all of this is relevant for what we're doing inside of an enterprise for example, but it's like shows us uh much increased risk again in like the dependencies that we're using and how
[22:55] careful we have to be about the the the ecosystem that we're pulling into our um application. And um a really great model for like thinking through this, I hope a lot of you have already heard about this. If
[23:08] not, then please look it up. Um, Simon Willison wrote about this in June 25, uh, this idea of the lethal trifecta. So, when you have an agent that has, um, exposure to untrusted content and access
[23:22] to private data and can externally communicate, then you have a high risk of, uh, uh, yeah, getting getting data problems, getting security problems with this agent, right? And this is like even
[23:34] more relevant for business use cases of agents, by the way, because as soon as you, uh, integrate like email, for example, with read and send, uh, rights, uh, permissions into an agent, you already have the lethal trifecta.
[23:49] So, it's not it's not a technical problem. It's a conceptual problem and it will be interesting to see in the bus- on the business side of things how all of those use cases with agents that were promised to us will even be able to get around this.
[24:02] So, with less human supervision, security, so, uh, think about, uh, are you making it easy to sandbox coding agents also locally, not just in the cloud, right? So, both with like, uh, pre-existing,
[24:14] uh, things like dev containers, for example, that I've been using a lot for this recently, but also there's like a bunch of new products popping up that have interesting ideas about this. Um, yeah, so just like sandboxing your agents even when you run them locally to
[24:27] reduce the supervision. And, uh, what is the AI security literacy among the engineers in the organization, right? Like, um, do they even know what's happening under the hood? Uh, you know, don't use this Yolo, you know, Yolo mode where you

## [24:40] The "Goldilocks Speed": How much velocity do we actually need?
[24:41] don't, uh, um, you don't even have to allow any of the commands, it just does what it wants, right? Stuff like that. And then secondly, for costs, the honeymoon is definitely also over, right? So, in the beginning of '24, I
[24:55] heard a keynote where the keynote speaker said, "Generating 100 lines of code only costs about 12 cents. Compare that to a developer salary." Um I mean, leaving aside that lines of code is of course not a good measure of value,
[25:09] right? Let's leave that aside, but it's not even like 12 cents anymore, right? So, this is if this is from summer 2025, there's some websites where people post their uh token usage, right? And there
[25:21] was this one person who was using on average $380 um a day, which if you extrapolate that to 20 work days a month, 12 months, would be a developer salary of 9,100 uh 91,200
[25:37] dollars, which is not a bad developer salary in Germany, to be honest. Uh And of course, this was summer, like this has like exploded even more, right? So, we've gone from like $20 flat rates in the beginning. I think Copilot might
[25:50] have even been $10 in the very beginning, right? I'm not sure. To more like $200 flat rates that are not really flat rates because you get request limiting, and then you see people on Reddit saying, "Oh, it's only the middle of the month, and I'm out of tokens, and
[26:04] what do I do?" You know, because we can't work without them anymore. That's a whole other topic. Um so, why is the cost ballpark for a change far from 12 cents now?
[26:17] So, now we don't just like Remember like when the the keynote speaker, this was like early 2024, so we were mainly doing autocomplete, right? Maybe asking in a chat for a few lines of code, right? But now we uh have the agent research the
[26:30] existing code, then make a plan, then we review and adjust the plan, then we start implementation, we have it run the tests and fix the tests and check the lint errors and fix the lint errors, maybe check the browser if it's a if
[26:44] it's a visual uh UI feature, fix that again, have a code review agent running, uh react to that, have a summarization. So, it's all of this back and forth, and it might even just be two lines of code
[26:57] afterwards, right? Um, so, yeah. So, where are we then after these last 12 months? So, context engineering, I talked about
[27:10] in the beginning, is like becoming a very powerful lever now of amplification both for good and bad, but you can actually do a lot of stuff now to make make it uh, more probable that the agent does what
[27:23] you want. And then, again, model improvements I haven't even explicitly mentioned here. That has definitely also happened, but I find I find that actually less interesting than all the other stuff that's happening around that. And so, as a result of these things, like there are strong forces tempting us
[27:37] out of the loop, right? So, we have to think about like where in a given organization or given use case can we give into that pull and where is it treacherous, right? So, kind of this like, oh, this feels really good and
[27:50] gives me like quick results, but like what will this mean in a in a year maybe? Because um, yeah, so there's kind of like this need for need for speed, right? Everybody just wants to be faster and
[28:02] more throughput and look how many PRs we merged this week, right? But with this like more autonomy and less supervision, there's also not just a question of security and cost, but also what happens to maintainability of the code, right?

## [28:15] Final Thoughts: Scaling AI Autonomy Safely
[28:16] Um, and there was an interesting article recently by team at OpenAI that uh, says they have been working on a code base for the last 5 months. It started as a greenfield code base,
[28:30] um, and their kind of rule for themselves was we um, we don't want to touch the code directly. We just want to interact with the agent and then continuously improve the um,
[28:42] all the setup around it to make it easier for the agent to maintain this uh And it was a mix of these things, so it was like a lot of that context engineering stuff, right? Like skills and stuff like that. Um they also put in more deterministic checks like uh
[28:57] custom linters and structural tests and stuff like that. And then they still said they kind of had like entropy increasing and like drift happening. So they had what they called garbage collection. So like agents uh
[29:10] continuously kind of running against the code base and cleaning up uh over time. And um this architectural constraints with more deterministic tools as well, this is something that has been popping up in a lot of uh stories that teams that use
[29:25] agents like this a lot uh recently. So I also experimented a little bit with it. So it's this idea of having, yeah, structural tests as agent feedback. So think stuff like uh ArchUnit or Spring Modulith or um in my case I was working
[29:40] on a TypeScript code base, so I used something called Dependency Cruiser, which I had actually never heard of before. And I think the reason is that we've had these tools for quite a while, but I think a lot of people haven't used them because we think we were still
[29:52] working on the code, right? And in a lot of cases, of course, they are. But we're like, "Yeah, yeah, I know how to modularize. I can say I don't need a tool like to to help me with these constraints." But now they're becoming like really interesting feedback tool
[30:04] for the agents, right? So here in this case, in my application, I kind of like And again, I I worked on this together with AI, uh defined like the different layers that I wanted in the application, and then set up uh a bunch of different rules. So there was one, for example,
[30:18] that um that said that external SDKs may only be imported by files in this client's folder that had lots of clients for other APIs. You don't want to do that in the domain folder, right? And so then this was like additional feedback um for
[30:32] the agent. And what's also interesting about these linters and uh um structural tests and so on is our ability to to go and um enhance and extend the the messages now, right? And
[30:47] make the It's kind of like a good type of prompt injection, right? So, you adjust the messages so that they the that they also contain instructions or hints for the agent how to react to those. So, let's say you have maybe like
[31:00] a linting rule, every file may only have 500 lines of code. And if you want to avoid that the agent just makes every line multiple statements so that it stays in the 500 lines of code, you could put into that error message that
[31:14] is a smell for a design problem, so you should consider refactoring, right? So, like just give it more context on what that message means to us. And this is
[31:28] So, this is basically all about how can we increase our trust in the agents ultimately, right? A building up a harness like this, right? So, the team called this harness engineering because ultimately,
[31:42] like let's think like a few years from now, I think we're not aiming for perfection that we want the agents to build perfect code, right? We certainly aren't building perfect code, but how do we get enough confidence and trust for
[31:55] our particular situation? Because we want to safely and quickly in a sustainable way deliver um our software, right? And so, I just want to share like a mental model of how I have recently been
[32:11] thinking about this. So, again, I talked a lot about the context engineering, the skills, and so on. And all of those things are kind of like feed forward into the agent, right? So, we're anticipating what the agent might do wrong, and we're trying to give it all
[32:24] the tools and instructions to increase the probability that it does what we want, right? So, those would be like giving it principles, coding conventions, maybe reference documentation, how-tos, and so on and so on.
[32:37] And then after the agent does its first generation of code, uh very often it's not immediately perfect, so then we give it feedback, right? So, static analysis, we have like
[32:49] maybe give it access to logs and start the application and see if it actually works the browser and so on. So, that all lets the agent like do some of the road correction the road work of corrections before we even look at what it's doing. And this can actually be a
[33:02] mix of like CPU and GPU-based things, right? So, I I took this framing from this company called Modern who recently started using that as framing for the CPU-based tools
[33:16] that they use. So, we you know, we can have a code review agent, but that is still like based on GPU inference, right? Like what if we enhance that with a lot more CPU-based more deterministic things.
[33:29] And we can actually have the same thing in the feed forward as well. So, all the things that I mentioned here before were kind of GPU inference-based, but if we give the agent access to CLIs, to maybe like bootstrap scripts, to code
[33:42] mods like open rewrite recipes and stuff like that, then again we can like feed it the things that make it more probable that it does the right thing. And that also comes back here like to the language servers that I mentioned
[33:54] before. So, for example, you can now give an agent access to something like IntelliJ's refactoring capabilities, right? So, it can actually use the rename symbol functionality to do a refactoring instead of doing
[34:07] text diffs all over the place. Again, makes it more probable that it does the right thing in the first place. So, and then that all of those things together, I would call a harness. So, some of those
[34:19] things are built into the coding agents themselves, right? So, like the way they do code editing, the way they do code search, they can improve all of those things. It's all part of the feed forward harness, but then there's like a bunch of things that we can control ourselves
[34:32] and like make it specific to our situation. And then as humans, we're kind of like the in the the steerers of this, right? So um and that's what that opening eye team was trying to do. They were trying to
[34:45] like um continuously like improve uh this harness around the agent. And of course for that, we can also use AI, right? And so that's the new potential of these structural tests and uh and and
[34:59] that I mentioned before and and linting that previously we wouldn't have built custom tooling for that. It was too much work, right? But now actually for the that experiment that I was doing, I did all of that with AI. I didn't I didn't write that myself.
[35:12] And that's like a lot lower uh risk factor than some of the production software we write, right? And I also wonder if that's kind of like one of the new abstraction layers
[35:25] actually, right? So will we maybe at some point in the future just have these like let's say topologies, right? That cover 80% of what we do. Like we build data dashboards a lot that just collect data
[35:38] uh from from other APIs and show it or there's maybe a crowd business service or event processors or just like typical types of applications that we write and then we have a definition of how they're supposed to be structured and what the tech stack is and then maybe have
[35:52] instead of a service template, we have a harness template for that that we can instantiate to then work on our code base. And then we might not even care anymore if it's React or Vue, right? As but one of our um decision metrics might
[36:05] actually be do is there an existing harness for that so I don't have to worry about that and I don't have to build that up initially. But all the examples I just gave for everything I just talked about with this
[36:19] harness were all about maintainability and internal code quality. I still have lots of questions about uh verifying functionality and of course, that's that's ultimately the key, right? We still want our software to work. We
[36:31] don't only want safety-critical systems to work, we want all software to work, right? So, um I think we need ideas how to harness different aspects of our application. So, I just talked I would say a lot
[36:44] about maintainability. Um maybe there's also something architecture fitness, so how can we have a harness for operability, performance, and so on. Um and then there's like I said, behavior. So, right now, what most
[36:57] people do is they feed forward a description of the functionality, and then the feedback part is mostly like, "Oh, the test suite is green." But the test suite was generated by AI, and then you do some manual testing, and
[37:10] then that's it, right? So, that's the approach right now that I see. Some people say they do more review of the tests and all of that, but I'm sometimes a little bit skeptical. Um so, and that's not good enough, right? Like, we have to come up with um
[37:23] better ways to do this. So, how does all of this change my trust level? So, improved models have definitely increased uh some of my trust level. Much more sophisticated context engineering, so the progressive loading of context, more tool integrations,
[37:36] sub-agents, uh all of those also um offer a lot of new ways to increase my trust level. New food for thought for like, how far can we push static analysis and stuff like that.
[37:49] But in terms of the question marks, I still see models do stupid things all the time. There's just this post on Reddit that went viral uh this week or last week where uh the agent was saying, "Oh, yeah, you said no, but I I thought
[38:03] you said no to me asking you for permission, so I just went ahead." Something like that, like a teenager kind of like, you know, "Yeah, you said no, but I thought you meant something else, right?" So, I still see that happen all
[38:15] the time. Um there's like this cognitive overload in the loop, right? So, there's more and more anecdotes now of people like talking about burnout or just being overwhelmed either by like doing all of the review or like trying this like
[38:28] multiple sessions at the same time. And so, and also mostly when I hear this done dialed up to 11 with like a lot of AI autonomy, it's done by quite experienced engineers, right? Who have
[38:42] the capacity for more more load because they have so much experience. And yeah, then there's just this like pressure for speed from from up above as well, right? So, and then if you put pressure on people to be faster with AI,
[38:55] they will cut corners and become more sloppy, right? And interestingly, there was like an article about Amazon reflecting recently on like some outages that supposedly were
[39:08] related to AI-generated code, and one of their reactions to it is now to have more gateways where senior engineers have to review what's going into production, which seems kind of like, weren't we supposed to like be faster
[39:22] going into production and now we're just putting in more gateways, right? So, um yeah, that's probably also isn't the solution. So, I've recently been asking myself more and more with this like speed, how much speed do we actually
[39:34] need, right? Is that what is the Goldilocks speed that is fast enough but not too fast, right? So, just imagine Homer falling off that fast treadmill. I didn't want to have an actual GIF of a human falling off the treadmill because
[39:49] um So, um yeah, what are the risks of all of this speed, but also how does the speed actually help the organization, right? Isn't there like uh aren't there other things that we should
[40:01] be looking into? So, to wrap up, I talked a lot about reducing human supervision and increasing the ability to use AI as like as an automation tool, right? Like building a lot more for us because that
[40:13] is definitely the through line of everything that's happening, and that's what a lot of people see in the future, right? But AI is a Swiss Army knife with lots and lots of potential use cases and of course plenty of them are useful with
[40:27] supervision and they don't necessarily overload you, but they're actually like a good extension of what you otherwise would have to be manually for and it would take a really long time, right? So so many things have developed over the past year
[40:40] that also make you more effective make the use of AI more effective and a better developer experience when you're using it as an enhancement of yourself, right? And over the next 12 months we're
[40:52] going to learn a bunch more again. There will be new good ideas, but we'll also discover more about all the worries and concerns that we have, right? About overload, about skills atrophy and stuff like that.
[41:06] So these were just like some of the things that I was posing to you as questions to to reflect on and that's I think the the least you have to do is is reflect on these questions and it's like a good
[41:18] kind of like um how do you say thought experiment, right? How ready would you be if you wanted to give AI more autonomy with in your delivery, right? What's your automated safety net? What's your security stance? What's people's AI
[41:32] literacy at this point in time and improving those things is always worth it. It's also worth it for the humans and AI can even help you improve that safety net already today if you want to be prepared in the future.
[41:47] And that's it.
