---
title: "AI-Native Software Engineering: Enduring Principles, New Pace"
video_id: sANRC65z6EQ
url: https://www.youtube.com/watch?v=sANRC65z6EQ
channel: "Software Engineering Institute | Carnegie Mellon University"
channel_id: UCrmnnE3yzpAyAuX_hRqyLdg
channel_url: https://www.youtube.com/channel/UCrmnnE3yzpAyAuX_hRqyLdg
publish_date: '2026-05-21T11:46:47-07:00'
upload_date: '2026-05-21T11:46:47-07:00'
category: Science & Technology
duration: '01:01:14'
length_seconds: 3674
view_count: 624
default_language: None
is_live: True
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  AI is rapidly changing how software is produced but not the need to engineer software to meet business and mission goals. AI is enabling developers to move from idea to implementation at incredible speeds. However, this fast pace has implications that teams must manage. Product quality does not come for free, and there is some tendency for AI to accelerate the accumulation of technical debt. In addition, what works well on small code bases doesn't always work as well on large code bases. So, what's a good software engineer to do?
  Software engineering principles and practices are essential in guiding software engineers to use AI to achieve production-ready outcomes. In this webcast, experienced software engineers discuss their observations and lessons from applying AI-native software engineering and studying its use across multiple projects. 
  
  What Will Attendees Learn?
  • Distinguish between “vibe coding” and software engineering
  • Understand how software engineering principles improve the use of AI and where these principles need to be adapted to be used with AI
  • Recognize the different criteria that can be used to assess the benefits of AI-native software engineering (e.g., productivity and software quality) and their potential tradeoffs
  
  Speakers: Scott Sinclair, James Ivers, and Mario Benitez 
  
  #artificialintelligence  #ainative #softwareengineering 
  
   ⁨@TheSEICMU⁩
notes: |
  Acquired 2026-05-22 via youtube-transcript-skill (Playwright path, succeeded
  on second attempt with `--timeout 60000`; first attempt at 30s hit the
  panel-render timeout — long-format ASR-only videos often need the longer
  timeout). 581 ASR segments. Light cleanup: speaker name "Mario Bonitez"
  (ASR) standardised to "Mario Benitez" per the description's spelling.
  ASR also has a fragmentary final segment "Heat. Heat. N." which is
  background music/intro audio bleed — retained verbatim per acquire-time
  policy. The talk was a SEI webcast originally streamed live (is_live: True).
---

## Transcript

[0:32] Hi everyone, welcome to today's SEI webcast, AI native software engineering, enduring principles, new pace. My name
[0:40] is Scott Sinclair and I'm a software architect here at the SEI and I wanted to thank you for joining us. Today's
[0:47] topic, it's getting a lot of attention and for good reason. AI is transforming how quickly teams can move from idea to
[0:53] implementation and many teams are currently exploring what that means for their day-to-day development work. It's
[0:59] opening up new ways of building, experimenting, and collaborating. But it also raises important questions about
[1:04] how these tools fit into established practices. Today, we're going to talk about that balance. How AI is changing
[1:11] the pace of software development, what it enables, and what teams still need to do to produce software that meet that
[1:17] meets business and mission needs. And we're also going to ground some of the uh terminology that often comes up when
[1:24] discussing AI terms like AI native, AI augmented, uh agentic, and vibe coding.
[1:31] These are all floating around and they're often used in different ways by different people. So we'll try to get a few working definitions uh to ground our
[1:38] common frame of reference here. And most importantly, we want to hear from you. We already have some audience questions
[1:44] in hand, but please continue to submit questions to the YouTube chat, and we'll try to get as many as we can.
[1:51] Now, let's meet our panelists. Uh, first, James Ivers, a principal engineer with over 30 years experience spanning
[1:57] research and application and software architecture. And to my right, Mario Benitez, a software architect with over
[2:04] 20 years experience in software engineering. Welcome, guys. Thank you.
[2:11] So, this first question, let's just get started with James. Um, I'm hearing a lot about AI's ability to generate code
[2:18] and with the field moving as quickly as it is. What are some of the different ways that you're seeing that teams are
[2:23] using AI in software engineering? So AI's taken off in a really big way and there have been a lot of changes in
[2:29] the last couple of years. What we were doing two years ago with chat GBT is nothing compared to what we're doing
[2:34] right now with tools. What we're usually talking about are AI coding agents or even our own custom agentic frameworks.
[2:40] And the big gamecher here is these tools can now access your data. They can access your repository, your databases
[2:47] within permissions of course, but they can also take actions. They can run your tests. They can run your tools. They can
[2:52] help you with debugging. And it's really tightening the loop in terms of what AI can do in terms of gathering information
[2:57] to give better responses, but also act on those responses and start to execute some strategies. So what this means is
[3:04] where we started initially with using uh chat GPT or something like this for some
[3:10] some thoughtful exercises like uh brainstorming requirements or design options or doing some product research.
[3:17] Now we can go way beyond that and generate code in fact even ask for implement this feature in my user
[3:23] interface come back a little bit and you've got tests working code something you can run. So this really changes the
[3:29] pace that we can do things, but there are upsides and downsides to that as we're going to talk about today.
[3:34] Yeah, definitely. Uh it's it's exciting. I I'm just over the moon with the whole AI. Obviously, there's some caveats
[3:41] there. We have to to consider uh you know, even running experiments at home.
[3:48] If you let this thing just loose, you may come back after that half hour lunch and find that it didn't do what you
[3:54] wanted to do, right? It's possible. So great. Uh that segus us right into the next question. Mario, uh what are some real world ways that you've seen
[4:00] personally uh used AI agents and assistants? And so what stood out about this?
[4:05] Yeah. Yeah. So it's a you know like James was saying right. So the thing is the the field is changing. We started
[4:12] with that chat GPT. Right now we're seeing a lot of our customers they want to implement their own agentic
[4:19] workflows. They want to use this technology to modernize their application. Right? I mean there's a lot
[4:25] of software out there. There is cobble applications that date back before I was
[4:31] even around. Uh so you know it's time to modernize that. So people are using AI
[4:37] to see how can I move how can I make that faster right? Um even in our own research we're doing
[4:44] code translation. Sometimes you want to go from one language to another. How can I do that faster? Uh so lots lots of
[4:52] applications like that. Obviously the you know implementing code implementing little scripts here and there that's a
[4:58] very easy one. Uh personally I use it in every way I can. uh sometimes it may be
[5:04] just brainstorming right but let's let's think about this idea we're trying to do and just get some help there uh at home
[5:12] my home lab is all maintained with AI uh I you know I let this thing loose and
[5:17] you know make me some docker compose files so that I don't have to do that myself you know so lot lots of different
[5:24] ways lots of different applications it that changes right one thing I'd like to build on with that is there is a
[5:29] difference between using an off-the-shelf coding agent like a claw code or uh codecs and building your own
[5:34] agentic frameworks and yes both have really important use cases and in fact my personal perspective my
[5:41] learning perspective is starting with the coding agents get gives me more of a feel for AI is good at what it's bad at where I need to help it along and a lot
[5:48] of what we do and what we'll talk about today is how we help AI along to a better outcome yeah how do we agentic space just uh the
[5:55] agentic space is where we get into customization this way we can come up with our own agents that can enforce our own standards more easily our own
[6:01] safeguards compensate for organization specific policies or extra hoops we have to go through.
[6:06] That's that's the more more advanced case, right? So you start with your coding agents and you get a taste for
[6:11] what it what it means to have a AI do some work for you. Absolutely.
[6:17] And overall, what would you rate your experience with some of these AI agents at home? Oh, okay. So, I mean I I so I'm on a
[6:27] quest not to write any code at home if I can avoid it. And so far so good. Now,
[6:32] that doesn't mean the internet doesn't go down every once in a while. Uh but overall, it's it's it's very
[6:38] useful, right? Especially if your task is bounded, right? And and I think that's what we see a lot with our with
[6:45] our customers. If you can manage to define your task and make it as clear as possible, then
[6:51] your results tend to be a little bit more much better. more deterministic which is a little bit of a challenge uh
[6:58] sometimes. Okay, great. Uh continuing on with you Mario. Yeah.
[7:04] How was your use of how has your use of AI changed the way that you develop software and what you consider to be a good outcome?
[7:09] Oh yeah, so you know I think the one thing about AI is it's really easy to
[7:15] produce code, right? you you you pull up your codeex, you you pull up claw and uh
[7:21] you say, "Hey, you know, write me a script that parses this Excel file or you know, write me a feature and next
[7:28] thing you know, you got, you know, thousands of lines of code, lots of markdown and lots of test and you're
[7:34] like, wow, that's it. Uh ship it, right? We can just, you know, ship that out."
[7:40] Uh and so it's it's kind of tempting, right? Uh and and you know, I'll be honest, I find myself sometimes, you
[7:47] know, wait a second. I I got to think a little bit about what this is actually is it doing what it's supposed to be
[7:53] doing, right? Uh because at the end of the day, you know, we want this software to
[7:58] actually deliver some value. Uh so there is a little bit of tension there that I
[8:03] that I observe. It could be, you know, I think of it as that siren song, right?
[8:09] you know, kind of, you know, enticing you to just ah, you know, hit commit, push it, you know, open that pull
[8:15] request and that's it. Uh, but, you know, there's some some caution there, I think, definitely.
[8:21] And following that question up, James, that sounds a lot like vibe coding a little bit of the home activities. Yeah.
[8:26] Is that enough to realize great and successful outcomes? So, so vibe coding was introduced with a
[8:32] particular meaning. Uh the idea was to stay in the flow to interact with AI to tell it what you want to respond to what
[8:39] it produces and stay out of the code right and there are a lot of ways in which this is a really exciting thing.
[8:45] This is fantastic for prototyping for for home use hobbyist work time uh
[8:50] these kinds of things any scenario where you have low risk of errors coding is a really good way to go
[8:56] and it can bring subject matter experts into software in a way that they haven't before. They can mock up an idea and talk to a production
[9:02] team, but five coding is not enough for production. At least not in my experience. Um,
[9:07] one of the issues that I've seen over and over again is incomplete specifications. As Mario says, well, AI is going to fill in that gap
[9:14] for you. It will invent something. Sometimes that's good, sometimes it's bad. Uh, but if we really want to get the
[9:19] most out of AI, we can't just vibe our way through it. We've got to be respond, we have to respond to the risk that
[9:26] matters to our organizations and to our users. And typically that means introducing some software engineering discipline. Yes.
[9:31] Right. One of the things that I noticed really on with my own uh coding effort is I had to slow AI down. It just had
[9:38] this propensity to run and generate as much as possible and just flood the zone with information. But it was missing
[9:44] tight feedback loops. And so in my interaction I moved more and more towards putting the brakes on activity, asking for checkpoints, asking AI to ask
[9:51] questions and really working on that clarity up front so that I could get better outcomes from AI. It it just
[9:57] wants to code, right? It just it's a generator. It's a generator. So, you know, you say something, I'm like, "Yeah, here's a
[10:04] plan. You want me to implement it yet?" And you may not even know that stuff to ask that. It may not even ask. That's right.
[10:10] So, uh this is a great little point from u a question from Paulo. Some say vibe coding output should not go into
[10:16] production. Uh vibe coding means you don't need to read or write any code. Do you agree with that?
[10:21] Uh so again, I'll come back to risk tolerance, right? If production means it's going to negatively impact your
[10:27] organization or your user, I would agree. I wouldn't put it into production. But there was a survey just uh a year or so ago that says that uh
[10:34] 25% of IT professionals were pushing pro code into production for yet reviewing.
[10:39] They weren't even testing it. So there's some of these tendencies we've had as engineers. Some people go the
[10:44] extra mile and embed that quality into their software. Those are the software engineers of the world as I think about it. The coders who are just churning
[10:51] code and spitting it into production. I think they need to raise their game because it's easier to do those kinds of
[10:56] things now. I I think it goes towards the risk tolerance, right? And so depending on,
[11:01] you know, if I'm if I'm doing a simple app where the the impact of it failing is well, nobody gets to use the app and
[11:08] they switch to another app and they play with another game. Well, maybe it's not a problem. Maybe you can push your V code to production. If you're going to
[11:16] implement safety critical code, something that goes in an airplane, well, you know, there is already even
[11:22] processes in place that help you make sure that whatever code you produce, however you produced it, meets whatever
[11:29] uh risk tolerance uh you're willing to accept. And there's a great parallel from from more than a decade ago with Netflix.
[11:35] Netflix has some really advanced engineering cultures, things like the the Simeon army, Chaos Monkey, things like this. What they would do is they
[11:41] would recognize that they have a relatively low risk if an individual user doesn't get a recommendation in 60
[11:47] seconds and they could fall back. So they could actually exercise some strategies where they could push code into production and maybe it wasn't
[11:52] ready but they understood the risk and they had a fallback strategy in plants. So it was it was intentionally how they
[11:58] would hit. Yes. So Mario uh in your mind what does it mean to be AI native? Is it vibe coding?
[12:05] Is it agentic? Is it something else together? Yeah. So I think so I I think you know
[12:11] I'm I'm with James here. I I tie it back to the risk and and it means understanding what that is. It means
[12:17] understanding where my use of AI is going to derive the most value in line
[12:23] with what I'm trying to accomplish as a company, as a business, as an individual, right? And so that may mean
[12:29] sometimes like I was mentioning, I use it to brainstorm, right? Hey, maybe I got to write some requirements for an
[12:34] application. So let's think about this and and and try to to hone in on the
[12:40] idea and and give it some shape, right? So maybe it's good use. Uh but then afterwards, maybe I want somebody else
[12:46] to take a look at that. Give me give me a different perspective, right? So AI gets me perhaps, you know, 80% there,
[12:53] 70% there, generates a set of requirements or use cases really quick for me. Uh but then I still have to do
[13:00] that extra extra work because it matters to my to my goal. It matters to my mission. It also means in my mind for
[13:07] example not just abandoning the things that we know are good, right? Uh think
[13:13] about static tool uh static analyzers. They've been around forever. You can
[13:20] absolutely use them. You can put them in with your AI. You should use them. Uh and you can make the output of your
[13:27] AI better, right? you can just ask the agent, hey, oh, by the way, before you
[13:33] give me any code, I want you to run this tool for me and fix the the issues by
[13:38] the way. Right? So, it means recognizing that it's not just all about I'm just
[13:44] going to go full full throttle on just prompts and that's that. There are other
[13:49] mechanisms that we have to understand and aligning all of that uh with our mission. Yeah. And in my mind too uh along with
[13:56] those prompts goes a lot of that 20 years of software engineering expertise and domain uh understanding uh that's
[14:03] more than just the prompting more than just the questions that you can initially ask. You know you're looking at these a lot from a system engineering
[14:09] perspective which might be different for different people. That's right. Yeah. So I think it's important to recognize AI native is not AI only.
[14:16] Right. AI is a tool, right? It's a tool that can help us more effectively at some tasks than in others. But what
[14:21] we've seen in our own experience is combining AI with nonAI techniques really gives you more leverage than using either alone, right? Using static
[14:28] an analysis tools. It's great to check the output. It's also great as a source of input to these tools because there's
[14:33] so much that we can do. Um I think of AI native is is essentially a state of mind where we're
[14:38] not thinking about it as this new thing or trying to figure out how to use it. It's this future state in which it's just something we use. We learn how to
[14:44] do it. We need to know how to integrate into our engineering processes because at the end of the day, we're not going
[14:50] to trust AI fully any more than we trust developers fully. The history of software engineering is layering on
[14:55] additional tools and practices and training so that we can trust the process even if we don't trust every
[15:01] individual element throughout it. And that's the goal we want to get to especially in uh scenarios where risk is
[15:06] a really big factor. Yeah, it's you know it may be risk from a you know people's lives. It may be financial risk. It may be all the above,
[15:15] right? Yeah. And there's lots of history there. All right. Uh, so we've been talking a
[15:20] lot about software development, but software is more than just development, right? Uh, let's talk about AI and the
[15:25] whole software development life cycle. So, Mario, where have you seen AI fit most naturally into existing workflows
[15:32] and why do they work well there? Yeah. So um when I think about the software development life cycle, you can
[15:39] uh you can think about early activities, you know, middle middle activities and and later activities. And so let me let
[15:46] me start with the early activities. Those tend to be where you're you you're starting to think about what it is that
[15:52] we're trying to build, right? So think about requirements. How are we going to build it? Think about your design. Uh AI
[15:59] is good in terms of providing you input there. Hey, you know, these are some typical requirements you see in these
[16:06] types of applications. Uh, or here are some design patterns you can choose from. Um, so it fits really well there.
[16:13] Right now, we still need to take a look at those and understand uh how do they fit with our overall context. If I have
[16:21] a a sixmonth deadline, I may not be able to do everything that the AI is
[16:26] proposing, right? uh or I may need to consider some of the constraints that my
[16:32] uh customers have uh you know budget resources etc right so um AI is really
[16:40] helpful in in providing you that additional almost perspective almost option in that early stages right in the
[16:46] middle well obviously that's where we see it shine a lot right it's really good at implementing code uh really good
[16:52] at implementing tests maybe uh etc uh
[16:57] where it's a little bit more iffy is on on on the later side from a validation
[17:03] perspective, right? Making sure is this the right solution. Is is this the right
[17:08] approach? Have we handled all of our corner cases, all of our edge cases? Uh
[17:13] that's where AI can be a little bit shortsighted, if you will, if you can call it that. Um but I think you've seen
[17:19] the same uh occasional shortcoming I've seen in that when AI is struggling to get a test working sometimes just drop
[17:25] the It just deletes it. I I think in all of this I there's an important role in vigilance for the user. We've got to
[17:30] watch what's going on and not just blindly. We can't you can't just accept you know recently I I was developing a a
[17:38] test augmentation agent right and over five days I had 15,000 lines of code 700
[17:43] tests and it still didn't do what I wanted it to do you know but it was really easy to produce the code right uh
[17:51] so but yeah so I think about it like that right so there is that that v vigilance that you have to have
[17:57] throughout the process uh but it can be very helpful all All right, we heard a lot of things
[18:03] about software development uh early in the life cycle with the uh discovery and and ideation and downright you know
[18:10] development and test generation. Um does this mean we can't use AI very well
[18:16] when we're developing or maintaining ex existing systems James? No, it doesn't mean that, but it is a harder problem.
[18:21] And I think um most people who experiment with these tools start with a blank piece of paper, if you will. They
[18:26] have an idea, they want to go to prototype, and it it shines. And there's a couple of reasons why it shines. There
[18:32] it gets a little bit harder with existing code. It's a simpler problem. There are fewer constraints to work with. There are fewer artifacts to to
[18:38] deal with. There are fewer behaviors that you have to avoid breaking. And these are are real problems. Context
[18:44] management is something you will hear a lot about as you get in more and more into using agents or creating your own
[18:50] agents. Two years ago, everything was prompt engineering. Now, it's context management. There's really good reasons for that. If you stop and think about a
[18:58] 10-year-old, 20-year-old project, the amount of context, shared memory among the team, documents, requirements, code,
[19:05] test, logs, the volume of information that is available is huge. All of that
[19:11] can be effective for AI. AI is pointed in the right direction. If it knows what's there, it knows how to use it.
[19:16] But there's a little bit of a a trade-off there because the more context it's slurping in, the more tokens it's
[19:21] using. That's expense. Yes. Uh there's also some propensity to overwhelm the context and start to lose the
[19:27] information that matters. So trying to figure out the right data, the right information that informs a given task is
[19:32] an important problem. But on the other side, there's the breaking things, right? So if I have an existing system,
[19:38] we've all done this. we made a change over here and inadvertently broken something over there. Right? Good tests protect us from that.
[19:45] That's an enabler for using this technology effectively. If you're working in an existing system and it doesn't have good tests, AI is going to
[19:51] be more we're enabled maybe to make unfortunate changes and not realize that it's wrong because it's have the
[19:57] feedback loop to detect that. Yeah. So as we work in these spaces with big entrenched legacy code bases,
[20:03] especially the really older ones, we have to give some thought ahead of time to what gaps do we need to fill so that we can take better advantage of AI.
[20:10] All right, great. And that brings up a audience question from Martin. I you partially answered it, but I want to hear some additional uh insights here.
[20:17] Can we harvest the relevant knowledge from all stakeholders of a piece of software or system completely and
[20:22] precisely and then just let AI combine those gems? Why or why not? So I'll start this. Um it's it's a
[20:29] wonderful goal. Uh and we can make some steps there, but I've been doing this long enough that if I talk to three
[20:35] different developers on a project, I might get conflicting answers, right? So there's an adjudication that needs to happen there.
[20:40] Uh but the ability to, you know, I've heard of some teams recording team meetings and conversations and piping
[20:46] that into AI to develop more of a corpus. Um there is a lot of information we can gather, but I am reluctant to
[20:54] call it a solve problem. uh we're all architects here and one of the things that we do is look at the architectures
[20:59] of older systems trying to discover the asimplemented architecture not the the thing that was written in PowerPoint and
[21:06] years ago that's a hard problem there's a semantic gap we have to close the more information we can gather the more we
[21:12] can do that but in my experience that's best as an interactive activity not a handoff to AI so I can ask questions of
[21:18] AI I can have AI help me build scripts to gather data and these are fantastic things to help assemble information But
[21:25] I'm not yet convinced we get it for free. Uh I don't know Mari maybe you want to talk about what we're seeing with some of the the markdown files that
[21:31] generation now that complicates it's it's really that that's right. So we've been seeing from you know some of
[21:37] our engagements with some organizations it's really easy to you know take some legacy codebase and produce thousands
[21:43] and thousands of lines of markdown. You as a human can't consume that easily at
[21:49] least even the AI can't consume it easily right because there's the context problem again
[21:54] and consistency problem and consistency problem and so you end up with h is this the right markdown is
[22:01] this some markdown that just got generated in the process of trying to refactor this piece of code uh so it is
[22:09] not uh that straightforward I'm not sure there's a solution yet I think the the encouraging thing is we
[22:15] can assemble this information. Yeah, I think what we as engineers can do is what's the right information that I'm looking for? Let's make targeted
[22:21] requests that we have higher confidence in as opposed to uh I think that's where you get more value, right? If you're explicit and and and uh
[22:29] what's the word I'm looking for here? Direct in terms of what type of permission you're going to see. Goal driven. You know, what are the
[22:35] things that you really want to know about this project? And yeah, sure, document those, put those, and maybe feed them to your agents as you're
[22:42] making changes. And just one more audience question because I'm I'm liking this line of uh discussion here. This is from George uh
[22:50] talking about maintenance again but you know these large code bases that have
[22:55] existed for a long time or battle tested a lot of times they don't have tests or they don't have unit test or integration tests. How do you successfully um
[23:03] maintain these in perpetuity with AI? [laughter] So you know I have a couple of thoughts
[23:08] there. One thought is a lot of these legacy systems and I think about the legacy systems I used to work with don't
[23:15] have tests right so maybe one way you could leverage AI is let's build some
[23:21] tests that's that's a starting point uh before you go and say well let's convert it
[23:26] from ADA to C++ right so maybe yeah we want to do that uh but let's
[23:33] let's be uh thoughtful about the way we want to do that right and let's use the AI where it can it and help us out.
[23:39] Yeah, setting up those enablers to enablers. So, maintenance is tough, right? Oftent
[23:44] times the requirements don't exist. There's been some good examples at trying to infer requirements from code
[23:50] and and as far as that gets you, that's great, but it doesn't replace subject matter experts because oftent times what
[23:56] this system does is just what it does, not sort of what you really want. So, if you if your idea of maintenance
[24:01] is status quo, then that puts you down a particular path. Automated test generation is really strong on that
[24:06] path. But if you actually want to really modernize and reflect on how can we use technology better, how can we connect
[24:11] systems differently, got to involve the subject matter experts and understand the flow of information. And maybe one
[24:18] thing you can do with AI is quickly mock up some user interfaces. Hey, if it worked this way, what would you think?
[24:23] That's not necessarily getting all of the engineering through productization, but it furthers a conversation in a very different way
[24:28] because you're now getting into the organizational aspect. Exactly. Um not necessarily much of the code, right?
[24:34] You're changing the business. They both matter, but what are your real goals and how does the tech industry help you with
[24:39] those goals? Yeah. And just one more question. I know you've touched on this a little bit, but this one's from Vince. Do you have any
[24:45] experience using AIS to develop, assess, revise, and validate requirements before anyone or anything starts designing
[24:51] systems and writing code? Good idea or a bad idea? So, so the history of software
[24:57] engineering tells us the earlier we find a mistake, the cheaper it is to fix it. Right? If we validate our requirements
[25:03] before we go off and do design and test, there are fewer decisions we have to unwind later if we got something wrong.
[25:08] So the software engineer says, "Yeah, of course you want to validate requirements." That's that's good. You don't want to get into analysis
[25:14] paralysis, right? Is a good innovation for lots of reasons. So there's that that usual balance to walk. We we don't
[25:19] go away from that with AI. Um where we get to is the cost of making changes is maybe a little bit more
[25:25] beneficial than it's been in the past. So maybe some requirements mistakes are easier to unwind, easier to change. Yeah. But in terms of
[25:31] uh of requirements work, I I've done a lot of what Mario was talking about earlier. I start with requirements. I ask AI the
[25:37] critique, fill in some gaps, ask some questions, look for ambiguity. It's not perfect and I don't expect it to be
[25:43] perfect, but it does save me time. It gets me to a more polished state before I present it to a colleague. Yeah. Oh, that that's that's the key,
[25:48] right? So one way to think about it is if it took you before I don't know two days to draft a set of requirements and
[25:54] you can now get AI to help you get there in one hour with some back and forth you
[26:00] know whether that means standing up an agent that is going to critique your your requirements chat simple chat
[26:06] simple chat that's already savings right that's and and so when you go to the review you know when we used to you know
[26:12] work and say hey Scott can you can you review my requirements what you think I bring a better product
[26:18] that's already savings uh even if it doesn't look like it sometimes because it's and maybe that's a really important to
[26:23] realize is savings don't always come from full automation. Yes. Sometimes it's that that intellectual
[26:29] step that filling in a gap early on that lets you keep working that gives you that uh that over the shoulder that pair
[26:35] programmerl like perspective as you're working on demand. These little things add up to a lot. They do.
[26:41] So now at this point we're all using AI and we're getting this warm fuzzy from using it, right? Um, so now that we're
[26:48] adopting it and we're embedding it in our development process, how do you know if we're actually getting better at developing code when you introduce AI
[26:55] into your workflows? Go ahead, James. Okay, so this is a really important question and I don't think we've got
[27:00] consistent answers yet. Uh, I've been looking at lots of studies, talking to organizations, and the data is all over
[27:06] the map. Uh, but as you hear me say data, you know the answer is already measurement, right? So we see some studies that show
[27:12] AI is a 10 to 30% improvement. We see other people talking about 10x improvements. There was also a really
[27:18] interesting study last year that showed under certain circumstances AI made you go slower. What was really important
[27:23] about that last study is the difference between perception and reality. The developers thought they were going
[27:29] faster but measurement showed they were going slower. So we got to measure and that means a lot of different things.
[27:34] There are different dimensions we need to measure. Lines of code as a productivity measure has always been a little shaky. something like function
[27:40] points a little more normalized is more helpful especially with AI's propensity to uh duplicate code.
[27:46] Oh yeah. But we also need to look at cost right token cost is is smaller than human cost right now. So
[27:51] that's a good thing and that's a an asset we can leverage. Quality matters a lot. Uh in particular uh there was a
[27:58] quote I heard in the talk earlier this week that that really connected with me. No one has maintained code that was AI
[28:04] generated for 5 years. It hasn't been around that long. we don't know what it's going to be to maintain this code in five years. So in terms of
[28:10] productivity, we have short-term and long-term perspectives. One other thing I want to touch on uh with regard to
[28:16] measurement is we've got to measure the right thing. Right? So there have been too many people who say I can generate code
[28:22] faster. Fantastic. I believe that that doesn't mean another phase didn't get longer. If your code is a lot faster,
[28:28] your test time is an order of magnitude larger, you may not be seeing quite the measure of the magnitude of savings that
[28:34] you expect. So we have wide enough aperture that we're doing even comparisons, apples to apples kinds of
[28:39] things. Uh and we recognize that while some activities will go faster, others won't. If we measure that, we can learn from it
[28:45] and we can keep making it better. And Mario, what's your take on this? Well, yeah. So, you know, I I always
[28:52] keep taking it back to my ultimate goal, the mission, right? Um even when we did
[28:58] traditional software engineering, we didn't do it because we like it. Nobody likes writing requirements, right? Well,
[29:05] maybe maybe some of us do, but excuse me. In general, you know, we did
[29:10] it because we recognized there was a value to our mission and taking those extra steps matter. It's the same with
[29:18] AI, right? I don't want to burn tokens just to burn tokens. That, you know, what's the point of that? I want the the
[29:24] ultimate uh result to be beneficial. Yes, I want to measure so that I know am
[29:30] I really going faster? I'm just burning tokens. Uh, and so you you have to tie
[29:35] it to that business case, to that mission, so that you know that it's actually helping you and not just
[29:40] generating tons and tons of code that you won't know what to do later on that you don't even know if it's right, if
[29:46] it's going to help you uh in the end. I mean, what one of the things that that I've I've noted for a while is yeah, we
[29:51] can generate code at rates we've never thought of before. My goodness. We can also generate technical debt at rates that we've never thought of
[29:57] before. Yes. And I think that's not meant to be a scary thing. It's it should be an empowering thing
[30:02] because we as users of the technology have a lot of influence over the direction that we go, the the safeguards, the guardrails that we put
[30:08] in place, the practices we put in place. We can steer this in a good direction. Yeah, absolutely. I mean, don't take me
[30:14] wrong. I I want to get to the point where I don't have to write the code. I'm not sure we're quite there yet. There is a lot of uh goodness. We need
[30:21] to be careful. Just make sure we we're conscious about what we're doing, right? Yeah. Writing code is fun, but it's also fun developing products, you know,
[30:28] quicker and quicker with AI, right? Uh let's shift the conversation a little bit towards development. It's hard to
[30:34] keep up. You were talking about the markdown files. Uh AI output is just prolific sometimes. Uh [snorts] so how
[30:40] has the pace and nature of development changed when using AI tools and what are some of these challenges and
[30:46] opportunities? Yeah. So you know as you can imagine I've been living it a little bit with
[30:51] some of uh the code we're seeing. It's like all of a sudden you generate thousands of lines of code and then
[30:58] what? Yeah. you know, how does this gonna go to production? Think think about a legacy application that uh you
[31:04] know, you're trying to replace. Okay, here's here's uh the new modernized version. How do I know it meets
[31:11] everything my legacy application did before? How, you know, how do I did it handle all the failure cases, all the
[31:18] edge cases? And so to me, there is um and goes back to to the measurement,
[31:25] right? It's it's really nice to generate a lot of code but let's not forget that that other stage of the process which is
[31:32] understanding what the business needs what the context for the business is
[31:37] right what kinds of constraints do we have that we need to be aware of oh you can't uh you can't change that interface
[31:44] to that subsystem because we don't own that subsystem we can't change it right so you know your new REST API
[31:52] I'm sorry but it's not going to work or rather maybe maybe your your gRPC API. We can't do that. It's got to be REST or
[31:58] it's got to be UDP or whatever it was. Uh so those are the those are the hard
[32:04] things uh that AI is not really giving you yet. Even if it's speeding up the
[32:10] code production, which is all fantastic, we just have to be aware of those, right? think about those ahead of time
[32:15] so that we tell the AI don't change that API leave it because I need to interface
[32:20] or create a mock um you know some some sort of facade that I can that I can use
[32:26] to integrate my system right that's the engineering part that's the thing that we got to pay attention to I think
[32:33] and uh development doesn't stop when we ship it right so how does the ability to
[32:39] generate code so quickly uh influence how you think about maintainability and long-term system help James
[32:45] so so this is a tough question this is one you know coming to that quote five years no one's maintained this for five
[32:50] years we don't really know yet but we have some clues uh so I I did a vibe
[32:55] coding experiment I produced an application soup to nuts 25,000 lines of code in language I never written before
[33:02] that was impressive I got a very slick application but under the hood it was structured terribly the architecture was
[33:08] bad it wasn't very maintainable and this this points out a trade-off that we have to wrestle with right so we
[33:15] know the economics of software engineering is changing right we can write code faster we don't know what the downstream effects are we don't what
[33:21] those quality implications are we have some hints right we know from software engineering that finding defects earlier
[33:26] is usually cheaper that's as true with AI as it is outside of AI and [clears throat] avoiding burning tokens avoiding human
[33:33] review loops it's sort of taking waste out of the system that's something we can and should continue to do but in
[33:39] terms of this this technology and what it means for for maintenance There's a debate, right? So there is a
[33:45] debate uh isn't one as far as I'm aware or I believe uh that says maybe we don't
[33:51] have to maintain anymore. Maybe we can just regenerate. Maybe AI can do all of this for us. Maybe the quality of the
[33:56] code doesn't really matter. I'm not sold on that one. And and my reasoning is this. Uh the kinds of
[34:02] principles we've developed in software train think dry solid yagney. These are all principles that make code cleaner,
[34:09] easier to understand. Those benefits aren't just for people. Cleaner, easier
[34:14] code is easier for static analysis tools to work with. It's easier to test. It's easier for AI to work with. A lot of
[34:20] those things that we've developed make code more self commenting, [clears throat] right? Make it easy to understand. We don't want to give that
[34:27] up. If we give that up, AI has to work harder to do anything. That's more waste in the system. So, if we do it right the
[34:33] first time, the same things that make it easier for us in the traditional ways to maintain, it's going to make it easier for AI as well. That's my belief. It may
[34:40] be cheaper, right? So you may not be burning those. It may be an economic question rather than a person's time,
[34:47] which was still all about money anyways, right? And that's a great point. So in the old days that the cost factors of of defect
[34:53] escape was like 10x per page, right? That's come down as we get to techniques like agile and whatnot. AI might lower those factors even
[35:00] further. Instead of it being 10 times more expensive, I think it's two times or one and a half times. We don't know those numbers yet, but I do believe that
[35:06] the the numbers are changing in a favorable direction. I think so. Yeah. So, you know, some of these enduring
[35:12] principles are just that enduring whether it happens to be traditional software engineering or now, you know,
[35:17] AI native software engineering. Um, so you don't get anything for free, right? You need
[35:22] to maintain those those principles. Yeah. All right. Uh, Mario, so what are some of the
[35:28] practical considerations in AI assisted development? Uh, for example, AI given
[35:33] the same prompt uh multiple times will produce multiple results. How do you manage this non-determinism in
[35:40] day-to-day work? Yeah. So, uh, you know, that's an interesting thing, right? I see a lot of people trying to get at managing the
[35:47] non-determinism of of AI. Uh, we we're in luck, I think, because think about
[35:53] it, we as people are non-deterministic, right? And we've been producing code for a long time. You give the same
[36:00] requirement specification to two developers, you end up with two different pieces of code. In fact, that's safety systems do that very
[36:07] often. They have two people intentionally. Yeah. Uh and so, you know, these techniques
[36:13] that we have in software engineering like reviews, like testing, like static
[36:19] analyzers, they're all about helping us manage that non-determinism, right? We
[36:25] we create our specification or our use cases so that we know that we understand
[36:30] the problem, right? We again, we don't do it for fun. We do it so that we have a clear picture. What are we trying to
[36:36] do? Well, you can do that with AI and not let the AI fill in the blanks, right? Uh you can do
[36:44] re, you know, have review agents that increase that quality output for you so that you don't have a lot of cycles
[36:51] with, you know, your peers or whomever is reviewing that that output. Uh so all
[36:56] of those things I think we can borrow from from the traditional practices. is we just have to be a little bit
[37:02] creative, right? It may mean, you know what, I'm going to have a a skill or an agent that that does this for me, a
[37:09] review or, you know, adds tests. Like one of the agents that I recently wrote,
[37:15] one of the things that I had to do was not just create the design, but call a different agent that reviews the design.
[37:21] And the same thing for the the guy that does the refactoring. My agent that does refactoring, it's not about just
[37:27] changing the code. he's gotta invoke another agent that reviews that code before I even get to look at it, right?
[37:34] You know, things like that. I think what's what's great about this is none of these are new ideas. No, right? The history of software engineering is how
[37:40] do we account for the fact that people make mistakes and is going to make mistakes, too. We that's not an excuse to avoid it. That's that's silly. That's
[37:46] okay. We have to we have to create engineering processes that we trust that have imperfect actors in the middle. All of
[37:52] this practices, tools, llinters, unit test frameworks, agile, uh shortening the the open rules, all of this, all of
[37:59] this has an equivalent with AI. Some of it translates very directly. Some it requires a little bit of tweaking, but
[38:05] if we remember why those practices and tools exist and we translate to them to this new world, we're going to be good.
[38:11] I think so. Now, back to the topic of non-determinism. James, uh what I know
[38:17] you're dealing with that that process a lot and the work that we're doing. What practices have you found helpful to avoid accumulating technical debt?
[38:23] So I I appeal to the basics, right? They're the principles that we've learned. Short feedback loops are very
[38:29] powerful, right? Keeper validation techniques are more
[38:34] powerful, right? That's why we have unit tests over exhaustive human inspection. We find the right combination to meet
[38:40] our risk tolerance, but we keep adopting those principles of getting feedback earlier, getting feedback from the right
[38:45] parties, whether it's tools or people. All of that is really important. Now the one thing that I think where we still
[38:51] have some room to grow is we've talked a lot about the code and we know we can test code and we can llinters at it. We
[38:58] can do all this great stuff that we absolutely need to do. We haven't talked about architecture. Yeah. And architecture is where I see AI a
[39:04] little bit weaker right now. Um architecture is we know is about the qualities of the code and we can't
[39:10] always test for how maintainable is this thing. There are other metrics that are good proxies for that. But we also know
[39:15] we have to make trade-offs. We need to make heristic decisions. I'm going to favor this over that in my business context for this reason. And so
[39:23] architecture involves a lot of subjective assessment, understanding these stakeholders. And not all this
[39:29] context is readily available. More often what what I've seen from AI so far is is what I think of the wisdom
[39:34] of the masses. Yeah. This is the solution that most people use. It may or may not fit your need, but I as a user have to make that
[39:40] judgment. Whatever the LLM was trained on, right? Exactly. Yeah. Which maybe is the wisdom of the masses.
[39:46] So in terms of technical debt right all the stuff that we do we got to keep doing we also have to recognize where AI
[39:52] might be a little bit weaker maybe it'll get better in a few months always possible but we have to compensate for
[39:57] those with other practices we have to inject that wisdom that that engineering discipline where it's not coming for
[40:02] free and especially for those for for those systems where that risk tolerance is you
[40:09] know much more important much more important right I I think we're not talking about doing you know fullblown specific ification design for
[40:17] a small That's right. Right. I mean, we're talking about like a, you know, big industrial system.
[40:23] Great point. We're not talking big upfront design heavy kind of stuff. It's always you use what you need to to get the
[40:30] outcome you need that you need. That's right. We just got the comment that humans are also non-deterministic, which I I can
[40:35] appreciate. U But you touched briefly on risk. I mean, we that's kind of the theme of what we've been talking about quite a
[40:41] bit, and we're getting some audience questions right now about risk. um how would you go about applying some of
[40:47] these tools and techniques in a safety world? I know you come from the safety industry. You've had a lot of experience
[40:53] with it, James. Um you know, what can a developer do here? Well, uh so you know, like I I know the
[41:00] way I would approach this, right? So developers wrote the code, that code never made it to production after it was
[41:07] written. There was the whole process in place that had to happen. If AI wrote the code, that same process still has to
[41:13] happen, right? Now, can I write that code faster? Yeah, absolutely. Can I write now? You know, before I had to
[41:20] write the unit tests, right? Or somebody had to write some tests. Well, maybe now I can use AI to do that. Heck, I'm going
[41:27] to add more uh more unit tests now. Uh I can assemble the package for review much
[41:32] more quickly. Much more on certification bodies, we can produce evidence more quickly. That's right.
[41:38] I agree with all of that. I think the unknown for me is in any individual
[41:43] organization process how much importance they put on human review. And one of the things that we've talked
[41:49] about in passing is the pace is changing that that that equation very badly.
[41:55] We can generate so much more code than we can review in a day. And review fatigue,
[42:00] take take it from me, is a very real thing. I've been living over this last year. You actually want to review all of
[42:05] this code. Scott's smiling because he's experiencing it with me, right? um it takes a lot out of you and I
[42:11] remember some old research saying that the limit is around two hours and then you need a break. Yep. You just cannot
[42:17] keep up at that same pace. So I think this is something we're still figuring out. There is a lot of merit in an
[42:22] independent review. Humans are go-to. That's what we're used to doing. There are some experiments using a different
[42:28] AI model than the one you generate code with as another reviewer. um we got to get smarter in that space because the
[42:34] the pace of production is going to outpace the pace of traditional review and that's a real challenge coming
[42:41] but you know one thing one I guess one little caveat in my mind even if uh you
[42:46] know yes we are becoming a bottleneck we are absolutely becoming a bottleneck but we always were
[42:51] but we were always the bottleneck right so so you know we're just before it used
[42:57] to be a much slower pace before we had code now it's like both. Okay. Well, now
[43:02] let's maybe put more emphasis on that review, right? Where we save this, maybe we can actually do a better job over
[43:07] here. And this is a great connection back to measurement. What does your entire development workflow look like? Which stages are getting faster? And
[43:13] from queuing your perspective, where is that creating new bottlenecks in the process? How do you attack that based on
[43:19] the data to do good work? All right. Uh these are all great discussions so far. Let's take a couple
[43:25] questions from the audience. Yes. Uh this one is uh is Genai the elusive
[43:31] silver bullet that we all think it is and can it give us the 10 times 10x developer that we're all hoping for. So
[43:39] reflexively I don't believe in silver bullets, right? I think engineering discipline still matters. I think what
[43:45] we see in these frontier models is is really impressive, but it's not everything, right? I think
[43:50] one of the things that I'm looking at is what do the coding agents add beyond the the frontier model? What do our agentic
[43:57] frameworks add beyond the frontier model? How much of what we know of good engineering disciplines can we embed in
[44:03] AI plus static analysis plus people these integrated workflows to get us to
[44:08] something that's closer to that silver bullet solution. But it's not uh it's not a one-stop shop. Yeah, there there's I don't I don't
[44:14] believe in silver bullets either. I' I've seen enough software out there that just there is no silver bullet. But
[44:20] that's okay. We can still have really good processes. It can still be great. Can still be still be great. It can be better. And so
[44:27] let's take a look at our agents. Can we make better use of those agents like having additional LLMs to get better
[44:33] quality output, right? Uh so that you know in your reviews you're not finding silly things in in
[44:40] the code, right? Uh so how can we put all those pieces together to get uh you
[44:46] know the most quality? And that leads into our next question. Uh you know we've been talking a lot about AI workflows, AI native software
[44:53] engineering. We've been talking about agents and agentic uh different things. How does the role of the software
[44:59] architect evolve? James, you want to start? So, I I think I've been using AI to help
[45:05] me uh with ideation, right? So, help me understand what are some my options on the tech stack. Help me brainstorm some
[45:10] some requirements. Uh I brainstorm a bunch of quality attributes scenarios. What am I missing from this list?
[45:16] I don't accept everything, but I'm getting input more quickly. Uh so, that kind of background, I'm getting good
[45:22] results. I'm also seeing much better results in terms of finding the references to why a given recommendation
[45:28] is being made. That's useful rationale for me to consider because then I can consider okay this is the recommendation
[45:34] here's why the why doesn't really match my setting so I need to look elsewhere. It's that additional step that is really
[45:40] saving me a lot of time where I'm not using it is to come up with complex bespoke architectures for uh for systems
[45:47] you don't typically find on GitHub that are much less likely to be in the training corpus. there's still more
[45:52] judgment in these special purpose uh usually very demanding systems.
[45:57] And Mario, what's your take on that? Um so the the way I look at it is uh I I think I've made this analogy before,
[46:03] right? Before we used to write assembly code and then compilers came along and you no longer needed to do that. I know
[46:10] this is still non-deterministic. I know because James is going to say, well, you know, those are nondeterministic,
[46:17] you know, so we're elevating a little bit. I'm not sure how much, right? Uh and so what that tells me is that we
[46:23] have to be uh thinking more in terms of the system we're building understanding
[46:29] the business the the domain we're applying this system right because there we can guide our AI to a much better
[46:37] output giving it better content giving it better context what's the right context that's right right and and
[46:43] determining what the right context is in my mind is still a human activity right
[46:49] it's still something that the human has to do. I if I'm doing a business uh application that was written in cobalt,
[46:56] I need to understand what my users did before, how they used it so that I can
[47:01] determine what the right stages for a replacement maybe and so then I can guide my AI to maybe start with these
[47:09] forms or maybe start with that other module. Right? But that's that's the level I think where we are going from an
[47:15] architecture point of view, from a systems point of view. So system engineering thinking um in my mind or at
[47:21] least replaying that what I'm hearing is not a big change from what software architects typically do right just the
[47:27] new tools that are available to them. So there there are a lot of people out there who are using this technology who are saying that architects are more
[47:33] important than ever because it's those big picture decisions that guide everything else and those are the upstream things that tend to be
[47:39] historically more expensive to to change. Uh and that insight really is tied to
[47:44] the organization's goals. All right, great. That leads into a question from Eduardo. What are the
[47:50] major challenges regarding the management of large amounts of AI generated code, but specifically what
[47:55] about managing architectural decisions? Uh, so to some extent those are two
[48:01] different questions, right? So, so managing architecture decisions, uh, AI
[48:06] currently is better with text. So, things like ADRs are a way to capture that, but ADRs can proliferate quickly
[48:12] if you're not careful. and managing for a human managing a context spread
[48:17] across 20 ADRs can be daunting and so that's something we have to be mindful of but another thing that uh I don't
[48:24] think we've mentioned yet is AI generates all these artifacts along the way if you ask it to lots of markdown
[48:29] files uh ADRs being one example without careful attention those files
[48:35] become dated very quickly right as AI is able to iterate very quickly and make changes
[48:40] it may not always go back and update that information which leads leads to if you will an accelerated pace at which
[48:45] the documentation is out of date. So managing that takes some again some vigilance some some a responsible party
[48:52] to remind the AI to keep those artifacts up to date to check the code that it produced actually conforms to that
[48:58] because it doesn't always again if AI doesn't have the right context for a feature change it will neglect something
[49:04] that is there and available and so we have to bring that discipline and that's still that's not a new problem right that's an enduring
[49:10] challenge no but maybe it's a faster one a faster one yeah it's coming at us quick yeah all right a question from Jim
[49:16] What's your recommendation for teams from the business side and also on the software developer side and even quality
[49:22] assurance to balance this accelerated flow of work using AI? Well,
[49:29] yeah, it's a hard one. So, you know, be mindful, right? Understand that you're
[49:35] going to produce a lot of code really quickly. And so if your downstream processes that help you look at this
[49:42] code are not ready for that, you're going to very quickly see either a decrease in the quality or you're going
[49:48] to see a slowdown in the process, right? You're going to push things that aren't reviewed or you're just going to say, you know
[49:53] what, I'm just going to push the the code to production, which little side note, the Octoverse 2025, right? 20%
[50:01] increase in PRs, but the discussions, they're pretty much flat. So that means we're pretty good at generating code but
[50:08] looking at it h not so much. So so we we have to be mindful right that means you got to talk to your developers. You got
[50:14] to say look guys you can't just let claude go and uh throw the code over the
[50:20] fence. We got to think about what does this mean to our organization. More code is also not necessarily
[50:26] better. Yeah. Right. In some of the work that we've seen that I've seen in my own code that I've generated there's a huge propensity to duplicate code instead of
[50:32] reuse code. Right. So this is missing context that AI can handle better. Point it to the shared libraries, the moodles
[50:39] that we've created. Ask it to refactor code to produce those. More code just is not a good thing for the sake of more
[50:45] code. But that's what we get if we're not careful. Well, there's a reason we had things like product lines, right? Because
[50:51] people got tired of reviewing the exact same code over and over again. And if I just let the AI duplicate whatever code,
[50:58] right, I'm going to do twice the work. We'll get the same configuration management problems. the issues a fix
[51:03] here is a slide there. We've been here before. We know the principles. We just got to embed them in. How are we using
[51:08] that? Yes. So, with this uh prolific generation of code that you guys are both talking about, uh this leads into a question
[51:14] from Cindy. [snorts] Uh and this one goes to you, James, but recent analysis shows that AI code has more security
[51:20] issues than human generated code. Given that it's projected to exceed 50% of all global code by 2027,
[51:27] how do we mitigate this? So, first off, we we fall back on what we do already. I mean, all of our code should be going
[51:33] through a vulnerability scanner, right? That no kidding, got to do it. Some organizations have been really proactive
[51:39] in training our staff to look for security issues. If AI is not going to have similar training, though I think it
[51:44] does, uh we need to make sure that our code reviewers have that kind of thing. We don't let go of the safeguards that
[51:50] we have now just because there's more code. We might scale it differently. That's a different thing. Uh although
[51:55] there are some some new things that are creeping up that uh I'll talk about slop squatting which is this funny phenomena
[52:00] that that came to my attention last year. Um there's kind of a new attack vector in that AI generative AI
[52:07] generates code for us. Sometimes it'll generate an include or a width of a package that that doesn't really exist.
[52:13] The name sounds good but doesn't really exist. This has actually become an attack vector where adversaries can create a
[52:19] dummy repository with that bogus name. So, seems like a new problem, but if
[52:25] we're doing good supply chain management, if we're looking at sbombs or other ways to take a look at what we
[52:30] do before we integrate third party code, then we should have a handle on this as well. But the same lesson applies to
[52:36] both. We've got to exercise the discipline that we know, the safeguards that we know, and we'll get better results. Yeah.
[52:42] And I think it might touch directly on that answer, but uh just another question for Michael. It's been stated
[52:48] that AI magnifies both good and bad practices. What are some of these uh bad practices that should be uh immediately
[52:54] addressed to allow AI and the SDLC to work? The the big one I would start with is
[53:00] under specification, right? AI I mean I noticed this right away when I started using cursor. If I gave it a loose
[53:05] requirement, fine. It would just go generate code and it would fill in all the blanks. It would decide what corner
[53:11] cases worth handling, what weren't, what I really meant by that requirement. Terrible idea. Uh but then again, you
[53:19] know, we wouldn't do this with our interns. We wouldn't give them a fuzzy problem and expect them to go off for 6 weeks and come back with code that's
[53:24] done. No, we we have feedback loops and we know to do that and that's really important. I think that feedback loop is is the
[53:30] key, right? We can't just uh assume that hey AI write me my new application. And
[53:36] even if if ourselves don't understand what we needed to do, you really can't expect the AI
[53:42] Yeah. to to do it for you. That work is still there. But the other thing I'll touch on is is
[53:48] something Mario mentioned earlier. And he and I have chatted about this. There's tremendous temptation with this technology.
[53:53] Yes. It generates something, it shows up, I run it, that looks right. It's so tempting to just run with it and
[54:00] keep going and and produce more and more and more. We've got to put the brakes on ourselves and exercise that discipline if we want
[54:06] to avoid some of those downstream consequences. Guilty. I know what I'm saying. [laughter]
[54:12] Now, uh, one question, Mario, on the implementation side. Yeah. How does speckit compare to options for AIdriven
[54:54] tolerance and recognize what gap they're trying to fill with these things. That's right. And then then pick and
[54:59] choose, right? Uh and so, you know, try them all just like you should try all
[55:06] the LLMs. just be mindful of of what gap you're filling, what are you trying to do, and make sure it it does that.
[55:13] Great. And um maybe one last question from the audience, but this one's from Sean uh to James. What kind of speed
[55:19] increases are you seeing when you're using AI? It depends. I mean, I I as I said
[55:25] earlier, the data is all over the map. In some cases, it's a little bit slower, some cases a little bit faster. Um
[55:33] so much depends on the organization's maturity. I really don't think we know. I think what we need to do is to gather
[55:38] that data and learn why organizations perform differently. Do they have a better test infrastructure? Are they using better models? Are they providing
[55:45] clearer specifications? What are these key factors that are leading us to better outcomes in some cases than others? That's what we got to share as a
[55:51] community. I mean, especially within your organization, right? If you're going to go and implement,
[55:56] you know, get all your developers to use AI, you got to start having some effort
[56:03] dedicated to making sure that you're just not spending a lot of money on on your LLMs or your claws or whatever
[56:10] tools you're choosing, right? And um one last one, we got a couple
[56:16] comments in the audience from it, but it's a question along the lines of, "All right, AI's here. I'm a little bit
[56:22] worried about my job. Is AI going to replace developers? So, let me start this one. So,
[56:28] for me, I have this mental model. I've always had a difference between a coder and a software engineer. A coder in a in
[56:36] an abstract sense is someone who just grabs a jar ticket, implements a feature, checks it in, moves on to the next ticket. Not a lot of big picture
[56:42] thinking, right? Software engineers go beyond that. We think about the overall design, how our code fits with the
[56:48] design. Is the design appropriate? How do we get this through quality assurance? How do we convince our certifying bodies that things are
[56:54] correct? There's a much broader perspective in terms of it's not about the line of code and and many software
[57:00] don't care about the language really because it's just not that big a deal to them. It's the higher level questions.
[57:05] What I think we're seeing may see is that that narrow interpretation of coding might be fading, right? That
[57:11] might be where we're more likely to see job impact. But those people who can bring engineering judgment, point AI in
[57:17] the right direction, connect it to the business, connect it to the users, that's an incredibly valuable skill
[57:22] that's never resided solely in a programming language that I think is more enduring and will survive and be
[57:27] more critical than ever. Yeah, I think that's the key, right? So that that understanding what's the
[57:32] system to do like when we used to do trains, you know, it's got to meet the company's needs. It's got to meet the
[57:38] customer needs and whether you do it with C, C sharp, it's a language.
[57:44] It's a language, right? Or whether you use this tool or that tool, whether you don't know the language anymore.
[57:49] Yeah. Well, that's right. Or I may not even know the language anymore, right? You got to get that systems thinking, that business mentality, understanding
[57:56] the constraints. And so if if I'm starting, you know, or if I'm worry about my job, where do I go? I go there,
[58:03] right? I go, you know, I want to learn more about the business, you know. Uh, all right. Great thoughts so far, but I
[58:09] want to give you each a chance to leave the audience with one final thought. So, in 30 seconds or less, James, what's
[58:15] your perspective on AI and software engineering? I think it's a really exciting time. It's a faster change than we've seen and
[58:21] there's a ton of potential. However, there's a lot of risk as well. I think we have not just an opportunity, but a
[58:28] responsibility to point AI in the right direction and to bring that discipline to bear. If we do that, we've got a
[58:33] great future. Mario, uh, well, you know, I love it, of course. Uh, can't help myself. Uh, but,
[58:40] you know, we got to adopt it. We got to embrace it. Understanding its implications, understanding how do we
[58:48] derive the most benefit from it. Uh, because again, we don't do this for
[58:53] fun. Sometimes we do. Uh, but you know, there's a reason, right? The business model, the mission, that's that's the
[59:00] goal, right? stay focused on that and use this as your tool to to get there.
[59:05] All right, guys. Big thank you to James and Mario for sharing your perspectives today. And thanks to all of you for
[59:11] joining and submitting all those questions. Uh if you have interest in collaboration on this topic with us at
[59:16] SEI, please reach out at info@sei.cmu.edu.
[59:21] And also, we ask that you complete our survey. The link is posted in the YouTube chat area now. um your feedback
[59:28] is always appreciated and help can help guide these talks in the future. And lastly, our next webcast will be June
[59:34] 9th and our topic will be about rethinking AI adoption where we'll discuss the upcoming AI adoption
[59:41] maturity model. Uh registration information will be added to the SEI website and emailed out. And remember,
[59:48] like and share the video.
[1:00:22] Heat. Heat. N. [music]
[1:00:46] [music]
