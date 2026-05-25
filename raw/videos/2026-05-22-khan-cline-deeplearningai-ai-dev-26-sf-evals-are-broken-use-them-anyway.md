---
title: "AI Dev 26 x SF | Ara Khan: Evals Are Broken Use Them Anyway"
video_id: fAfuQN0WwFE
url: https://www.youtube.com/watch?v=fAfuQN0WwFE
channel: "DeepLearningAI"
channel_id: UCcIXc5mJsHVYTZR1maL5l9w
channel_url: https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w
publish_date: '2026-05-22T16:14:59-07:00'
upload_date: '2026-05-22T16:14:59-07:00'
category: Education
duration: '24:36'
length_seconds: 1476
view_count: 1187
default_language: None
is_live: False
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  This talk by Cline's Ara Khan explains why they went from "evals are useless" to using them as a core part of my agent improvement loop. I share practical heuristics for interpreting, running, and creating evals, and why doing them anyway is better than pure "vibes".
notes: |
  Acquired 2026-05-25 via youtube-transcript-skill (Playwright path; succeeded
  on first attempt with `--timeout 60000`). 699 ASR segments. Stage cues and
  audience interjections retained.
---

## Transcript

[0:07] I'm Era. I'm going to be talking about
[0:10] eval uh specifically u AI evals like
[0:14] coding agent evals and stuff. And I'm
[0:17] going to talk about how they're broken
[0:18] and how you could still use them.
[0:20] Anyway, uh before I start, I just I want
[0:22] to say one thing. It's just like it
[0:24] boggles my mind when when you're like
[0:26] when you're working on something and
[0:27] you're like cooped up in a room for so
[0:29] long and you just like you think that
[0:31] like in your head you think that there's
[0:32] like no one cares and then when you talk
[0:34] about it and there's like so many people
[0:35] here. It makes me very happy. I'm very
[0:37] thankful that you guys showed up. Um it
[0:40] it makes you feel like you like it means
[0:42] something and I'm very thankful that you
[0:45] guys came over. So thank you so much. Um
[0:48] all right so speaking of uh evals like
[0:50] my claim my fundamental claim of this
[0:53] entire conversation is that eval are
[0:55] people are wrong about evals
[0:58] most people know a lot of things about
[0:59] eval claims they'll say things but
[1:01] they're wrong about eval
[1:06] to be right about eval do you do that
[1:09] like how do how do we how do we become
[1:11] from wrong about eval to right about
[1:12] eval
[1:14] to do able to do that basically what I
[1:16] want you to do is like I want you to be
[1:17] able to build them. I want you to be
[1:19] able to interpret them and I want you to
[1:21] be able to use them in your agent flows.
[1:22] Your agent flows could be anything. It
[1:24] could be a coding agent. It could be
[1:26] like a shopping agent. It could be an
[1:27] agent for anything. It could be
[1:28] something very trivial or it could be
[1:30] something super complex that's like a
[1:31] production workflow that's used by
[1:33] millions of people. And in all those
[1:36] cases, you can learn from EVLs. And
[1:39] regardless of like whichever direction
[1:41] you tend to go to in your agent building
[1:44] experience, I think Ewells are like one
[1:45] of the most critical aspects um of my
[1:49] years of spending uh working with AI
[1:51] agents. So let's kind of reverse it,
[1:56] right? Let's reverse it. Like how do we
[1:57] know like how do we know if people are
[1:59] wrong about them? Like why why do I
[2:00] claim that people are wrong about them?
[2:02] And there's two ways. The first there's
[2:04] two camps of wrong. And the first camp
[2:06] of wrong is the objective metrics camp.
[2:09] What does that mean? Objective metrics
[2:11] camp is like basically like it's like
[2:13] basically people who believe that like
[2:16] everything you just take it as face
[2:18] value. So if you look at an EOL, you
[2:20] look at artificial intelligence, you
[2:21] look at epoch AI, you look at all these
[2:23] companies and they're all doing great
[2:25] work and they'll come up with these
[2:26] objective numbers of like whenever a
[2:29] model comes out, you just post these
[2:30] benchmark scores and all your Twitter
[2:32] feed is just filled with like this score
[2:35] on evalu
[2:41] uh array of information coming at you
[2:42] and it's it's supposed to be real
[2:44] numbers so you're supposed to believe it
[2:46] and it that's what a number came out and
[2:48] it's like I don't think that's the
[2:50] answer. I don't think that there's like
[2:52] these exact numbers or how precisely one
[2:55] model is better than the other. To be
[2:57] very very precise, if you notice like
[2:59] there's like you would notice sonnet 4.6
[3:02] at 52 and then you'll notice like a few
[3:04] other models quite close to it. And it's
[3:07] very difficult to make the claim that
[3:09] like the models which are close to each
[3:10] other in the score here are actually
[3:12] equally as good because they're not. And
[3:14] if you spent like half an hour using any
[3:17] of these models, you'll know very
[3:18] quickly that these scores don't
[3:20] necessarily mean much. Um, so this was
[3:23] like a tweet from um Francis and he made
[3:26] a claim that Meta came out with a new
[3:29] model. It was a it was a huge
[3:31] disappointment because it was benchmark
[3:32] max. Tons and tons of models these days,
[3:35] tons and tons of lab these days are just
[3:37] doing this like game where just like get
[3:39] the highest score on Eval. Doesn't
[3:40] matter how good the model is, it will
[3:42] get it will get the tweets in, it will
[3:43] get a clout in and then you pull people
[3:45] in and then who knows maybe the model's
[3:47] good, maybe not. So that's one end of
[3:49] the spectrum. But how are the others end
[3:51] of the spectrum? The other end of the
[3:52] spectrum is taste. So taste is king
[3:55] people are basically like who don't
[3:56] believe in the numbers at all. Who think
[3:58] that these numbers are completely
[3:59] pointless. They don't believe in
[4:00] anything. It's just it's just uh made
[4:02] up. So this is basically like the taste
[4:04] and king people. But basically like um
[4:08] the the argument of taste is king people
[4:10] is basically like it it it's it's all
[4:12] about wibes man. It's all about wibes.
[4:14] Like it does it don't matter what the
[4:16] numbers say. So they'll like if you talk
[4:19] to them they'll say things like oh why
[4:21] do I like why do you like cloud models?
[4:23] And they'll say oh I like talking to
[4:25] her. She sounds nice. They'll talk
[4:27] they'll talk about an AI model like it's
[4:28] like an actual person. And it's it's
[4:31] just at this point it's like it's like I
[4:32] don't even know where to start. And I
[4:34] think both of those like both of those
[4:36] uh groups are wrong. And I think the
[4:37] truth is somewhere in the middle that
[4:39] like eelss are not the end all and be
[4:41] all. They're not completely useless.
[4:43] There are right ways to use them and
[4:44] there are wrong ways to use them. So the
[4:46] purpose of this conversation is that I
[4:48] want you to like I want you to take
[4:50] through take you through a few levels
[4:52] and with as I walk you through these
[4:54] levels like you you'll have a much
[4:56] better understanding of how to work with
[4:57] emails. So the first one, this is a very
[5:01] rudimentary one, is like I want you to
[5:02] be able to be like how can you use other
[5:04] people's evals? How can you use eval
[5:06] from like if it comes out from the model
[5:08] labs, it comes out from cursor, it comes
[5:09] out from cloud code, whatever, how do
[5:11] you interpret them? Level two is like
[5:13] how do you use eval to improve your own
[5:15] agents? And level three, if you have a
[5:17] lot of money and a lot of time, you can
[5:19] even build your own eval. Um, but yeah,
[5:21] so these are these this is basically the
[5:23] point of this uh conversation here
[5:25] today. Um so instead of like instead of
[5:28] just like giving you like you know how
[5:30] to interpret eval like some hard rules
[5:32] I'm just going to give you some
[5:33] heruristics and if you follow these
[5:35] heruristics I think you have a much
[5:36] better understanding of somebody else's
[5:38] eval. So when you get these numbers
[5:40] you'll you'll be like much more
[5:41] confident of like here's what it is and
[5:43] here's what it means for me. So first
[5:45] thing the rule number one don't ever
[5:48] believe model lab eval just don't just
[5:50] like the whenever the numbers come out
[5:52] whenever labs come out with like
[5:54] whatever eval numbers come out for
[5:55] mythos preview or gb 5.5 or whatever
[5:59] they're great and they're probably
[6:01] accurate and those models are I'm sure
[6:03] they're very decent. I'm just saying
[6:04] don't take those those numbers as a word
[6:06] of god. You you have to use your own
[6:09] discernment. They're close
[6:10] approximations but they're not perfect.
[6:13] Um so this is like one of the tweets
[6:16] which is like very profound where this
[6:18] guy he makes the claim that has any
[6:20] engineer actually made a decision based
[6:22] on a benchmark result and basically the
[6:26] claim is that like a lot of people they
[6:28] will like routinely dismiss like eval
[6:30] results they will routinely say thing
[6:31] they like they'll run evals they'll get
[6:33] the numbers they'll get those things but
[6:35] like they'll actually dismiss it and a
[6:37] lot of times like real AI researchers
[6:39] would like kind of take them with a
[6:40] grain of salt and I think that's like
[6:42] the right way to think of uh of eval. Um
[6:45] the heristics too of how to interpret
[6:47] eval is that you got to stay current but
[6:50] you don't have to be the earliest
[6:52] adopter and a lot of you who work for
[6:54] like very big companies and and you you
[6:57] guys this matters more for you guys than
[6:59] for the rest of us. So what what do I
[7:01] mean by this? So this is a chart of EPO
[7:05] AI which shows like how good the models
[7:07] have been scoring in the last couple of
[7:09] years. Uh well I guess like from 2024 to
[7:13] now it's like 2 years but in AI that's
[7:15] like 27 years. It's it's moves so fast.
[7:18] What you'll notice is that if you look
[7:19] at the soda score every couple of months
[7:22] the sort of model changes and it changes
[7:25] very quickly. Like if I time travel to a
[7:28] couple months ago it was like sonnet 4.6
[7:31] or oppus was the best model. Not so much
[7:33] anymore right? And if you if you keep
[7:36] playing this game of like, hey, I want
[7:37] the best thing all the time. Like you
[7:39] you'll just like the mental bandwidth
[7:42] that you'll spend trying to always be on
[7:44] top is just not worth it. I think what
[7:46] you want to do is you want new models to
[7:48] come out. You want new things to come
[7:49] out. You got to wait out for a couple
[7:51] weeks and then you got to be like,
[7:53] "Okay, let the dust settle." And that's
[7:55] when you try your own thing. There are
[7:57] people like me who will spend all their
[7:58] time trying to find out what the new
[8:00] thing is, what's the best frontier thing
[8:02] at any point of time. and that is what I
[8:04] do for a living. So sure, I'll do that.
[8:06] But I don't think you should do that. I
[8:07] think you should stay current, but you
[8:09] don't necessarily have to pick the most
[8:11] urgent thing. And the third heristic
[8:14] which is a very important one is that
[8:16] when you're working on a problem, so I'm
[8:19] personally because I work at client, I
[8:20] work on the problem of coding agents.
[8:23] Coding agents have a very specific kind
[8:24] of eval. So these are called terminal
[8:26] bench. Um some evolve version like
[8:29] Frontier SWE um some other kind of like
[8:32] coding benchmarks. Those are very
[8:33] specific and pertaining to me. I think
[8:36] maybe you work on a different problem.
[8:37] Maybe you work for some kind of shopping
[8:40] company. Maybe you work for
[8:41] infrastructure company and maybe the
[8:43] eval applicable for you are very
[8:45] different. When a lot of these models
[8:48] apps come up with a score, they're just
[8:49] like generic general purpose eval. They
[8:51] may not necessarily apply to you. I
[8:53] think as a problem solver, you should
[8:55] always look for eval
[8:58] to your problem or as close as you can
[9:00] get. I think that's a much better
[9:01] measure. Um so to give a very precise
[9:04] example like S swb bench was a very
[9:07] standard eval marker for coding agents
[9:10] for so long and then openai came along
[9:12] and they said yeah this this benchmark
[9:13] is like so saturated we can't use it
[9:16] anymore. If you've been in this space
[9:17] you would have known that this this this
[9:19] eval was like saturated so hard that
[9:21] like right now model apps come out they
[9:22] they don't even mention the score
[9:24] because that's how saturated some of
[9:26] those eval are and they're not
[9:27] applicable to your problems.
[9:30] Okay, so that was the first part. The
[9:33] first part was figuring out what are the
[9:34] huristics that you can use to like
[9:37] improve like understand and interpret
[9:39] other people's emails but like how do
[9:41] you use eval to improve your agent upon
[9:42] them and this is where I come in with
[9:44] like my own like experience of uh
[9:47] working at client and working on this
[9:49] like very very hard problem which is a
[9:51] problem of both engineering and
[9:53] philosophy and the way you want to think
[9:56] of this is that like
[9:59] because like because AI has like such a
[10:02] high variance of response. It could like
[10:04] it could give you an answer. Uh it's not
[10:07] very deterministic. The answer space is
[10:09] basically infinite, right? And if you
[10:10] let an agent run, if you let an agent
[10:12] run for you know 10 minutes at every
[10:17] step of the way, it could take a
[10:18] different turn. And then if you let the
[10:20] tree go this way, like it's like it's an
[10:22] infinite space of what are the things an
[10:23] agent could do. So like when you want to
[10:25] solve this kind of problem like it's
[10:27] it's very hard for to measure like is an
[10:29] agent actually doing the thing you
[10:31] wanted it to do and that's why the way I
[10:33] think of eval is like I think eval are
[10:35] like kind of an engineering but they're
[10:37] also a philosophy problem and when we
[10:40] were working with coding agents for like
[10:42] we've been doing this for a couple years
[10:43] um we found last year that like there
[10:46] were all these eval but like they were
[10:48] just like so different from day-to-day
[10:50] problems that we just didn't bother
[10:52] using them. I talked to like open I
[10:54] talked to Enthropic last year and they
[10:56] were basically like yeah eval are great
[10:58] but bro it's just about the vibes it's
[11:00] just about the vibes and um at the time
[11:02] it was part of the reason was that like
[11:03] the evals were just like measuring
[11:05] something completely wrong. So to give
[11:06] an example to give a very precise
[11:08] example a lot of eval would have things
[11:09] like Fibonacci sequence like implement
[11:11] the Fibonacci sequence implement the
[11:13] unit test right um they would have like
[11:15] this algorithms problem that you solved
[11:17] in your sophomore year of university and
[11:19] it's like doesn't apply at all to your
[11:21] real world coding experience. So um with
[11:25] time what happened was uh client wanted
[11:27] to build our own eval which were like
[11:29] more applicable more accurate more
[11:31] pertaining to real world software
[11:33] problems and as we were working on them
[11:36] uh we found this incredible group from
[11:38] Stanford u institute and they were came
[11:41] out simultaneously with this benchmark
[11:43] called terminal bench and the best part
[11:46] of terminal bench was that it had like
[11:49] this small set of problems well 89
[11:52] problems which very applicable to very
[11:54] real world software engineering task.
[11:57] And these could include database issues,
[12:00] uh race conditions, um front-end bugs,
[12:03] um just real actual problems that like
[12:06] real software engineers such as yourself
[12:08] face dayto-day. And we realized halfway
[12:11] through working on building on our eval
[12:12] like hey they they've built this like
[12:14] great ecosystem of like good set of
[12:16] problems. It's easy to run them. It's
[12:18] easy to replicate them. It's easy to
[12:19] make these eval work with any of the
[12:21] coding agents whether it's codex cloud
[12:23] code client whatever and work with them.
[12:26] So we adopted
[12:29] u we adopted um their their evals
[12:32] basically. Now the hardest part the
[12:34] hardest part about them was like when
[12:37] you measure when you're measuring like
[12:39] an AI system if you measure something
[12:41] very trivial. So if you measure
[12:42] something like how many Rs there are in
[12:44] a strawberry or if you're measuring like
[12:46] how many toes does a cat have those
[12:48] things have like somewhat of a
[12:50] deterministic answer or you know what's
[12:53] the weather somewhere those things are
[12:54] like single turn I think where agents go
[12:57] off is that like if you ask an agent
[12:59] like hey like write an MCP server to
[13:02] connect to my app using this O what the
[13:05] agent will do is like the agent will do
[13:07] a ton of different things. It will like
[13:09] use a web search tool. It will maybe
[13:11] install a Python library. Maybe it will
[13:13] access like some kind of sandbox. Maybe
[13:15] it will read a few files. Maybe it will
[13:16] edit a few files. And the whole process
[13:19] could take like 5 to 10 minutes. So what
[13:22] you want to be able to do in this kind
[13:23] of eval is like you do all those steps.
[13:25] You really let the agent run for 5 10 20
[13:27] 30 40 minutes. Let it do the whole
[13:30] thing. And then once it's done there are
[13:32] like these deterministic unit tests
[13:34] which check like did I make the file?
[13:36] Does it run? Does it pass the test? And
[13:38] that's what that's what terminal bench
[13:40] does. It's like agentic eval which take
[13:42] a while. They'll take like some of those
[13:44] uh problems easily take like 30 45
[13:46] minutes of like continuous agent just
[13:48] running turning on different attempts to
[13:50] solve the problem and then once it's all
[13:52] done then it grades um the problem. Um
[13:56] so this is bench and this I'm very
[13:59] thankful for the team. So shout out to
[14:01] them. Um, so yeah. So I guess like I
[14:05] guess when you have like an evaluation
[14:07] suit, right, you you want to be able to
[14:10] like you want to be able to like how do
[14:12] you define like a problem? Like how do
[14:14] you like what do you learn from this?
[14:16] Like I'm just talking about my thing,
[14:18] but how can you interpret from this? So
[14:20] there's a couple of things you want to
[14:22] track when you're working on agentic
[14:23] evals, right? The first thing you want
[14:25] to track is like just like how many
[14:27] turns is it taking? How many tool calls
[14:30] is it taking? How many tokens is it
[14:32] using? How long does the whole run take?
[14:34] The run could take like sometimes there
[14:36] are models which are like very very good
[14:38] at performance but they'll take like 45
[14:40] minutes because the inference is so
[14:42] slow, right? as you tweak these
[14:44] parameters of like what exactly you're
[14:46] looking for and you run it on different
[14:48] models, I think you you get much much
[14:50] closer to like, hey, this is what I
[14:52] really want and this is what I'm okay
[14:53] with and this is how much of money I'm
[14:55] willing to spend on this much quality.
[14:58] And once you track all these things, I
[15:00] think that that is like what you really
[15:02] need because I think that as much as I
[15:04] would love for everyone to use the most
[15:06] expensive frontier model for every
[15:08] problem, I don't think that's how the
[15:09] world works. Like we don't have infinite
[15:11] amount of money. Sometimes it just makes
[15:12] more sense to use like Deep Seek V4 for
[15:14] Flash, which is like 150th the cost of
[15:17] another model. And I think that this is
[15:19] like if you track these things in EVAL,
[15:22] um they'll tell you like how to how to
[15:23] how to figure out and what to choose
[15:25] from. Um so specifically for terminal
[15:29] bench, the way the eval work is that I
[15:32] told you that there were like 89 tasks,
[15:33] right? So these 89 tasks could be task
[15:35] of like caching bugs, latency issues, uh
[15:39] reg x bugs, front end bugs, race
[15:41] conditions, whatever, uh implementation
[15:43] aspects of things. What terminal bench
[15:46] does with Harbor is that if you have
[15:49] problems you want to be able to solve,
[15:51] what you do is you make isolated
[15:53] containerized environments where you set
[15:55] up the whole thing. You set up the
[15:57] machine, you set up the environment, you
[15:59] install the dependencies, you install
[16:01] everything that you need in that
[16:03] specific machine in an isolated
[16:04] container and then you run the agent on
[16:06] it, right? So if you run any agent with
[16:09] like the same starting point of like it
[16:11] already has, you know, whatever version
[16:13] of Python and JavaScript that you
[16:15] needed, it's got this all all thing
[16:17] working and then from that point on the
[16:19] agent starts. So the benefit of using
[16:21] harbor which was also it's tied to the
[16:23] terminal bench team. The benefit of
[16:24] using that is that like usually back in
[16:27] the day the way eval would work is that
[16:29] they would work sequentially. So they'll
[16:31] run like one after the other and it will
[16:32] take like six seven hours for the eval
[16:36] to finish because problems would run
[16:37] sequentially and they will like
[16:38] interfere with each other's code. They
[16:40] will interfere with each other's like
[16:41] environments and system. What Harbor
[16:43] does is that like it just like lets you
[16:45] split out all of them in different
[16:46] environments and then you could run um
[16:49] Ewells on them. So I think that when you
[16:51] run your own emails, when you build your
[16:52] own EVs, I would strongly encourage you
[16:54] that like really containerize them,
[16:56] really isolate them from each other.
[16:58] That's why they won't interfere with
[16:59] each other's problems. And for us, uh we
[17:02] use model. model is like the
[17:04] infrastructure layer that helps us build
[17:07] like these parallelized containerized uh
[17:09] environments so that like whenever our
[17:12] eval task would run they would run in
[17:14] like different uh different containers
[17:16] um the the in the way that I've shown
[17:18] here so shout out to modal um all right
[17:22] so how's the process like what do you do
[17:25] like what do you what do you do here so
[17:27] the process is very simple you run the
[17:29] UL with your agent coding agent um any
[17:33] other kind of agent you get an original
[17:35] score you figure out like what what went
[17:38] wrong. So to give I I'll give you a very
[17:40] precise example. Have you ever used like
[17:42] say sometimes you use like say clock
[17:45] code or sometimes you use like say um
[17:48] codeex like what would happen is that
[17:50] like it will try to read a file or it
[17:52] will try to install something and it
[17:53] will just go in circles that it can't
[17:55] install this it can't read this or it's
[17:56] just it goes into the same error and it
[17:58] just keeps going in circles of like I
[18:01] can't run this command I can't do this
[18:03] and I'm sure you've experienced this
[18:05] before what happens is when you run
[18:07] evals on like a larger scale those
[18:10] problems become very obvious. So what
[18:12] would happen is that like if there are
[18:15] 89 tasks on 20 of the task the model
[18:17] just went in like complete circles and
[18:19] did nothing just like was trying to read
[18:21] a file couldn't read a file was trying
[18:23] to edit a file couldn't edit a file or
[18:25] has was having installation issues. When
[18:28] you run the eval you get this like
[18:29] portfolio allocation of your failures.
[18:32] So if you're failing on like being able
[18:34] to read files, if you're failing on
[18:35] inference, if you're failing on
[18:36] something, you're able to figure out
[18:38] like okay, what are the broad buckets in
[18:40] which my successes and failures could be
[18:42] bucketed? And once you figure that out
[18:45] once you figure out like your tiny like
[18:46] like these large buckets of like your
[18:48] successes and failures, you can like
[18:50] iteratively improve on figuring out and
[18:52] point to the exact specific problem. So
[18:54] one of the the examples that we found in
[18:56] our testing was that like sometimes we
[18:58] would have a model that just doesn't
[18:59] work well with editing certain files. So
[19:01] we would change the edit file tool.
[19:03] Sometimes it couldn't use the web
[19:04] browser pretty well. So we'll we'll
[19:05] change that tool. And I think that that
[19:08] like having the manifestation of your
[19:10] problems reflected in like an aggregate
[19:11] way is like a much easier way to
[19:13] simulate what the user experience would
[19:15] be because how else are you going to
[19:16] like figure out like what went wrong? Um
[19:19] so there's actually three things you're
[19:20] testing. What are the three things
[19:22] you're testing? You're testing the
[19:23] model. Obviously you're testing the
[19:25] model whether or not it's good, but
[19:27] you're testing the harness as well. The
[19:29] harness is your agent scaffolding. So
[19:31] like when you write the agent like it's
[19:33] possible that there's a model that's
[19:34] like really really good but you just
[19:36] wrote it the wrong way. The best
[19:38] explanation is that if a new model from
[19:41] anthropic comes out I guarantee you you
[19:43] would have noticed that it works better
[19:44] in cloud code compared to say Droid or
[19:47] cursor sometimes and it's like it's if
[19:50] it's the same model why is it that it's
[19:51] much better in cloud code than some
[19:53] other agent? Why is that? And that's
[19:56] basically what you're testing here. that
[19:57] like sometimes it's a great model and
[19:59] your harness hasn't just just done the
[20:01] justice that that the model needs to be
[20:04] able to make sense of it. And then the
[20:06] last thing you're testing is the problem
[20:08] same because you could be solving like a
[20:09] stupid problem that just doesn't apply
[20:11] to that just doesn't apply to your eval.
[20:13] So you need all three to be in alignment
[20:15] and you need to be very honest with
[20:16] yourself like hey this is what I'm
[20:17] trying to do and this is what works for
[20:19] me. So in our case it was something like
[20:22] this like uh we ran the eval the first
[20:25] time and yeah so we ran the eval the
[20:28] first time we got an original score um
[20:30] then we made some changes to like CPU
[20:32] memory layer uh we raised some timeouts
[20:35] we improved the thinking behavior and as
[20:38] we made those changes iteratively our
[20:40] scores just improved and then eventually
[20:42] we were able to beat clock code in uh
[20:44] for oppus 4.5 eels and what we found
[20:48] over time is that like we're able to
[20:49] beat clock code in other emails as well.
[20:51] Um because we we just figured out some
[20:54] tiny knobs that they they couldn't
[20:55] figure out or they didn't optimize for.
[20:58] Um so I think that if you're you're
[21:00] working on an interesting problem, you
[21:02] can just be like, "Hey, let me figure
[21:04] out what I'm doing. Let me figure out
[21:05] what my competitor is doing, let me
[21:07] build some great evaluators
[21:09] doing, I'm just going to beat them. I'm
[21:11] just going to do it so much better than
[21:12] them." Um so there are um three zones of
[21:17] improvements. The first one is like the
[21:19] most obvious flaws, right? Like the
[21:21] obvious flaws of like okay like what is
[21:25] like obviously wrong with like your
[21:28] agent. So it could be like your read
[21:30] file tool is wrong. It could be that
[21:32] your you know agent turns are broken.
[21:35] Maybe your checkpoints are broken. Maybe
[21:36] something obvious is broken. Right?
[21:39] Those things are just like it basically
[21:40] tells you that your agent is like broken
[21:43] on like a fundamental level. So once you
[21:45] fix like once you fix like those basic
[21:47] things I think your agent starts to work
[21:50] it it makes it look like okay it's
[21:51] actually working it's actually
[21:52] functioning and that's a good zone one
[21:54] of when you're working with evals
[21:56] because you want to fix the obvious
[21:57] flaws. The second zone and I think this
[22:00] is where you really do the real hill
[22:01] climbing is that at that point you're
[22:04] just like um how do we like how do we
[22:06] actually figure out the philosophical
[22:08] aspects of like how to make my agent
[22:10] better. A lot of times you'll find that
[22:12] like it's like you have all kinds of
[22:14] like stuff in the prompt in the tool
[22:16] call in the tool call definitions
[22:19] um in the logic of like retries or
[22:22] whatever that like your agent is just
[22:25] not doing well. And I think to some
[22:26] extent it's your fault of like prompt
[22:28] engineering. Maybe it's a fault of like
[22:30] using too many tools. Maybe you're using
[22:31] too few tools. Maybe you're using the
[22:33] wrong tools. And I think that is where
[22:35] the like real gift of eals is that like
[22:38] you instead of like sitting around and
[22:40] pontificating philosophically whether or
[22:43] not your agent is good, you can have
[22:45] like very nuanced judgments of whether
[22:47] or not your agent is actually good by
[22:49] giving it real problems to solve. And
[22:51] then the zone 3 is like the danger zone.
[22:53] So the the reason I call zone 3 as the
[22:55] danger zone is that like sometimes
[22:58] people have this thing that once so as
[23:00] soon as you give them a metric as soon
[23:01] as you give them a number to optimize
[23:02] for all they do is just optimize for the
[23:05] number. So they don't they don't really
[23:06] care what the problem at hand is right
[23:08] give if you give someone a number all
[23:09] they'll do is like optimize for that
[23:11] number. So they'll like they'll just
[23:12] like uh overfitit the model. They'll
[23:15] like they'll like change the prompt such
[23:17] a way that they only pass this like
[23:19] specific task. They'll add like weird
[23:21] skills and stuff. So that that's not
[23:22] nice. So you want to be cautious that
[23:24] like you're improving but like not
[23:26] overfitting or doing something wrong. So
[23:30] basically if I could give you a final
[23:31] word it is that like find a benchmark
[23:34] that works for you. Build some eval if
[23:37] you can. You should hill climb. Honestly
[23:38] hill climb means just like improving
[23:40] your score on the eval. And then even if
[23:43] you get a good score you always need to
[23:44] make sure you're passing the vibe check.
[23:46] Like you need to know on some emotional
[23:48] level that like yes my agent makes
[23:50] sense. Like it's it's you know it's not
[23:51] just about benchmarks. like is this a
[23:53] sensible agent? Is it making sense? Is
[23:54] it actually solving our problems? And
[23:56] you got to start somewhere. You got to
[23:58] start somewhere. I think this is a great
[23:59] discipline. Uh we spent a couple months
[24:02] working on it at client. We're still
[24:03] working on it. Every time a new model
[24:05] comes out, we try eval. We improve the
[24:07] new model experiences with it. Uh we're
[24:09] using like a lot of open source models
[24:11] now. So we're we're trying to support
[24:13] and improve eval. Um, and I think that
[24:16] we never would have figured out all
[24:17] these beautiful nuances of these like um
[24:21] these open source models which are
[24:23] incredible much cheaper had we not run
[24:25] eval because we just we would have
[24:26] completely ignored them and just worked
[24:28] on wibbes.
