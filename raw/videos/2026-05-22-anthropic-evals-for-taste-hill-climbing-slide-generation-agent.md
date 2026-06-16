---
title: "Evals for taste: Hill-climbing a slide-generation agent"
video_id: v9FTCvkV_a0
url: https://www.youtube.com/watch?v=v9FTCvkV_a0
channel: "Claude"
channel_id: UCV03SRZXJEz-hchIAogeJOg
channel_url: https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg
publish_date: '2026-05-22T22:39:25-07:00'
upload_date: '2026-05-22T22:39:25-07:00'
category: Science & Technology
duration: '39:16'
length_seconds: 2356
view_count: 1872
default_language: None
is_live: False
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  Built rubric-driven replayable eval system from real user projects giving quality, cost, latency, error, token signals in under 6 hours per model change. Evolved into dev flywheel powered by real user dissatisfaction signals.
notes: |
  Acquired 2026-05-25 via yt-dlp fallback (youtube-transcript-skill Playwright path
  failed at 60s timeout — the recurring panel-render failure mode). Custom VTT
  dedupe with hour-aware `<\d\d:\d\d:` regex (same parser from the Caldwell + Ng
  ingests). 1053 deduped ASR segments spanning the full 39:09 runtime.
  Stage cues and audience interjections retained.
---

## Transcript

[0:19] Hello, hello, hello. Good afternoon,
[0:21] everyone. I hope you all had a wonderful
[0:24] lunch. Um, there's so many of you as
[0:26] well. I'm actually kind of surprised by
[0:28] this. Um happy to see that there's that
[0:31] much interest in talking about uh evals.
[0:34] Um I personally am a big fan of anything
[0:36] evals related but I know not everyone's
[0:39] that's not everyone's cup of tea, right?
[0:41] Um so very happy to see this many people
[0:43] of you. Um so yeah this so today's
[0:46] session is really going to be about
[0:48] evals. Um, and I guess my goal for this
[0:51] session is for you all to be afterwards
[0:54] to be inspired to build evals to be
[0:57] like, okay, evals are actually really
[0:58] useful. Um, and how you can act on them,
[1:01] right? Like we're going to be building
[1:03] evals. I want you to get a better sense
[1:06] of like, okay, how should I be thinking
[1:08] about building evals? What are useful
[1:10] type of evals? And then also, how can we
[1:13] use and take these evals to then make
[1:16] better agents, right? So that's the main
[1:19] goal of this session. Um, and the way
[1:21] we're going to do this is by building a
[1:24] slide generation agent and then finding
[1:26] out like, okay, what are some good
[1:28] evals? What do we want to measure? And
[1:30] then how can we build now better agents
[1:33] based on the feedback that we're getting
[1:35] from our evals. And the first thing that
[1:39] we all need to set the stage on is what
[1:42] are evals, right? So, evals are
[1:46] systematic tests that measure how well
[1:48] an AI system performs on a specific
[1:50] domain or use case, right? So, they give
[1:53] you information about like what's the
[1:55] quality of the results? Um, what did you
[1:58] do well, what was it not good at, how
[2:00] can we improve, right? And evals, they
[2:03] are made up of tasks that define certain
[2:05] scenarios um that then encode certain
[2:09] expectations through the grading logic.
[2:11] So one way that we're thinking about
[2:13] evals is if you for example are building
[2:17] an AI system, an AI agent and you want
[2:20] to make sure that the output adheres to
[2:22] like a certain type of quality or you
[2:25] want need to make sure like this must
[2:27] always be present. Evals are a way to
[2:30] kind of encode this behavior in a way
[2:32] where then afterwards if your evals fail
[2:34] you know like okay my agent is not doing
[2:38] or behaving the way it is intended.
[2:40] Right? So that's the way how we can use
[2:42] these evals and then evals is also the
[2:45] bridge between things like it seems to
[2:48] work or like um we know it works or
[2:50] maybe you saw like ah it kind of feels a
[2:52] little bit worse today for some reason.
[2:55] It's always very hard to act on these
[2:58] types of vibes, right? Like I think
[2:59] vibes definitely have their own place. I
[3:02] think they're useful just to get like a
[3:03] general sense check of like how people
[3:05] are feeling, but they're not very
[3:07] actionable, right? And that's kind of
[3:10] what we want to get out of EVAs. We want
[3:12] to have something that's actionable.
[3:15] So then
[3:18] we always ship EVA or like we always
[3:20] once we release like a model, we always
[3:22] have this accompanying benchmark card,
[3:25] right? And we always list like oh these
[3:26] are like a bunch of EVAs. This is what
[3:29] we achieved, what our models achieve. We
[3:31] compare them to other models. We compare
[3:32] them to competitor models, right? Um and
[3:35] there's like always a few usual
[3:36] suspects, right? Like for example um SWE
[3:40] bench is a very famous one which
[3:42] measures agentic coding abilities.
[3:45] Terminal bench is one that's also quite
[3:47] popular. But we also have other types of
[3:48] evals right we have like tool use and
[3:50] agents like for example like tbench
[3:52] browse bump os world which are some
[3:54] other evals that measure different
[3:55] things and then we also have like
[3:57] reasoning and knowledge um like arc agi
[4:00] too. Um now this is all fine and dandy
[4:03] right and then you look at these evals
[4:04] and we always every time a new model
[4:06] releases like oh it's top of the
[4:07] benchmark for these and these um evals
[4:10] right um and they give us like a gen
[4:13] general sense of like how well is the
[4:16] model and how much did we improve upon
[4:18] previous versions right but for you guys
[4:22] if you're like building something if
[4:23] you're building an agentic system this
[4:26] doesn't really say much usually right
[4:28] like because like we we don't measure
[4:30] for example like a very specific use
[4:33] case that you guys are building on right
[4:36] we measure these gen generic general
[4:38] benchmark that measure a lot of
[4:39] capabilities but they might not be
[4:41] applicable to your specific use case
[4:43] right so that's why we always say build
[4:46] your own evals
[4:48] benchmark the different models benchmark
[4:50] your AI agent and make sure that you get
[4:52] the most out of the models and make sure
[4:54] that you're also using the right model
[4:55] for the job right
[4:59] and so why are these Evals specifically
[5:01] important. So this is my pitch to you of
[5:03] start using evals, right? So without
[5:06] evals, suppose you don't have evas. I
[5:07] think we've all been into the scenario
[5:10] where you have like this agent and it's
[5:12] working fine and then you get like this
[5:14] feedback of like a customer who's like
[5:17] saying like uh it's it's not really up
[5:20] to par of like this new model switch.
[5:22] It's something is off, right? It's very
[5:25] hard like to do anything with that
[5:27] information, right? It's just like okay
[5:29] um do you have some logs maybe that we
[5:31] can take a look at some specific
[5:32] instances right and then you try to like
[5:35] debug it manually right but in a way
[5:37] you're still flying blind right you're
[5:40] always in a reactive loop so you wait
[5:42] for the feedback and then you're like
[5:43] okay let's see what we can do about this
[5:44] right so you basically only catch issues
[5:46] in production you you can fix for
[5:49] example like one issue which then might
[5:51] for example create multiple more down
[5:52] the line by making I don't know a prompt
[5:55] change tweak that suddenly degrades the
[5:57] cap capabilities on like other tasks
[5:59] that you haven't even considered. Um
[6:01] it's it's also quite annoying to
[6:04] distinguish like genuine feedback from
[6:05] noise, right? Um which is always you
[6:08] don't want to act on every single thing
[6:09] that you see because people have also
[6:11] some um biases in the way they perceive
[6:14] these things, right? Um and then finally
[6:17] I think which is the most important one
[6:18] is there's no way to verify improvements
[6:20] or regressions on anything that you're
[6:22] building or that you've done, right? So
[6:24] you like need a way to make sure that
[6:26] the changes that you are making to your
[6:27] agent are actually impacting the quality
[6:30] and making sure that you improve upon
[6:31] your previous versions, right? And so
[6:33] this is basically what evals do give
[6:35] you. If you add evals, you have clarity.
[6:38] You need to define what does success
[6:40] look like, right? Because like if let's
[6:43] say you don't have evals, right? And
[6:44] you're not even able to articulate like
[6:46] this is how the agent should behave.
[6:48] This is what a successful end product
[6:50] would look like from an agent. then how
[6:52] can you make sure that your agent is
[6:54] actually behaving properly because you
[6:55] can't even vocalize it to yourself like
[6:57] this is what it should be. So building
[6:59] these emails forces you to define
[7:02] formalize in a way what you expect your
[7:04] agent to do. Um it also allows you as I
[7:08] said to iterate on optimal agent
[7:09] configs. Um you can also adopt new
[7:12] models faster right instead of like
[7:14] saying like oh we might test out this
[7:17] new model and then see if it's like okay
[7:19] you now have like some clarity to say
[7:21] like okay this is better on this and
[7:22] this is not better on this and this is
[7:25] why we should or should not migrate to a
[7:26] new model which especially I think is
[7:28] quite relevant with the pace of new
[7:31] models coming out I think is also like
[7:34] just taking this load of your back of
[7:36] always constantly having to find like
[7:38] okay what is the new frontier Right. Um
[7:41] and then finally making problems visible
[7:43] before launch. Right? So you know like
[7:45] oh if there's like a few um cases that
[7:47] you have that we always do well or that
[7:49] you trust to provide a lot of insight
[7:52] that's where you get the most value out
[7:54] of evals.
[7:57] And so h how do evals really fit in? So
[7:59] originally um when we were thinking
[8:02] about like prompt engineering we had
[8:04] this basically this flow of like how you
[8:07] should optimize your prompts right? So
[8:09] first you develop your test cases which
[8:11] are the evals in the end. Then you write
[8:13] like a prompt, you test out the prompt
[8:15] against the tasks, you refine the prompt
[8:18] a little bit and then it goes back. You
[8:20] run the prompt again. You refine it
[8:21] until you've like okay I'm doing good
[8:24] great on my evals. I'm confident that my
[8:26] system is working properly and then
[8:28] finally you can like ship the polish
[8:29] polish prompt right. Um over time
[8:31] systems have gotten a little little oh
[8:34] can I go back? Can we go back one slide
[8:39] Thank you. Um, so over time it has
[8:41] gotten a little bit more complex with
[8:42] now agents coming into the loop with
[8:44] like tool calls, skills, all the
[8:46] different ways to optimize your context
[8:48] and all that stuff. So over time these
[8:50] systems get more and more complex. So
[8:52] it's also way more levers that you can
[8:54] pull to make changes to your agents
[8:57] which makes it once again then more
[8:59] important to have evals that forces you
[9:02] to have a concrete way of identifying
[9:05] these are the things that we can change
[9:07] and these are the things that impact the
[9:09] system in a positive way. So once again
[9:12] like with agents it's the same flow
[9:14] right um except now we test way more and
[9:17] way more complex things
[9:22] evals when you create them there's
[9:23] basically a few graders a grader is what
[9:25] we consider basically a way how we can
[9:28] judge the output right and like one of
[9:31] those ways is for example a codebased
[9:33] grader which is pretty similar to for
[9:35] example a unit test as you might know in
[9:37] like software engineering right um it's
[9:39] can be like a string match rejax, maybe
[9:42] a fuzzy fuzzy match. Um, but it's like a
[9:44] strict analysis, right? Um, it finds
[9:47] static uh and tool call checks. And the
[9:49] advantages of this one is it's fast,
[9:51] cheap, deterministic,
[9:53] but it has a big drawback which is that
[9:55] it's brittle and it also lacks in
[9:58] nuance, right? Um, and with this we mean
[10:01] like especially brittle is quite an
[10:02] interesting one in my opinion because
[10:06] these deterministic checks, they force a
[10:08] certain deterministic behavior, right?
[10:10] But with and sometimes this is
[10:12] absolutely the way we want um an agent
[10:15] to behave right like for example let's
[10:16] say you have an agent that creates a
[10:18] slide deck for example you want to make
[10:20] sure that in the end there is a slide
[10:22] deck present deterministic check but
[10:25] then if you want to have like a check on
[10:27] what's the quality of this slide deck
[10:29] this is way more nuanced right like you
[10:31] cannot easily encode this in like some
[10:33] deterministic checks right and that's
[10:35] why we also have this second type of
[10:37] graders which is the model based graders
[10:39] Right? And this is like rubric based
[10:41] reasoning. Um so you for example say
[10:46] is this slide high quality very generic
[10:50] but that might be for example a rubric
[10:52] or like for example is this text
[10:54] coherent also a way to get some intel on
[10:58] how well your agent is performing. Um
[11:00] you can do some interesting things with
[11:02] this as well. Um pair wise comparison is
[11:04] in my opinion quite underrated. Let's
[11:06] say you have two examples two outputs.
[11:09] Um, and then you basically OS model
[11:10] which one of the two do you prefer and
[11:13] why? That's also quite interesting to
[11:15] get some information out of especi
[11:16] especially for these scenarios where you
[11:19] don't really have a clear way of of
[11:21] defining what makes a better one, right?
[11:24] Um, and and then another one is the
[11:27] multi-judge consensus which is just for
[11:30] example you take like best of three and
[11:31] you say like three judges score
[11:33] independently and say like majority wins
[11:36] for example, right? Once again that this
[11:38] multi-judge consensus is interesting
[11:40] because it allows you to introduce some
[11:42] more determinism in a way um where if
[11:45] you have like we know that an LLM is
[11:47] undeterministic right and the same would
[11:50] be happening for these model based
[11:51] graders right like if you run them like
[11:53] 100 times a few times it might say oh
[11:55] this is great and a few other times
[11:57] might say ah it's not that great if you
[11:59] have like this multi-judge consensus you
[12:01] basically are assuming let's put more
[12:03] compute into this and let's see what the
[12:04] majority of our greatest consensus It is
[12:07] right and this is unlocks a lot of
[12:09] things right like this is flexible this
[12:11] is scalable this is nuanced
[12:13] but as I said it's nondeterministic it
[12:16] costs more money and also it requires
[12:18] some calibration which we will see is
[12:20] not easy at all and then finally the
[12:24] most expensive one are the human graders
[12:26] and these are probably the graders that
[12:29] when you building these agentic systems
[12:31] you will be using the least right
[12:33] because they're like incredibly
[12:36] um you have like a whole subject matter
[12:38] expert that will do like a whole review
[12:39] of the system. It will it's expensive.
[12:41] It's slow as well, but it is more it's
[12:44] the highest quality. It is very nuanced.
[12:47] Um and yeah, it's like really good for
[12:49] like some AB testing and some spot
[12:50] checking, right? So, I'm not sure like
[12:54] how many of you were able to clone the
[12:55] repo beforehand and have this all set
[12:57] up. Um, I actually wanted to do this
[12:59] session a little bit differently, but
[13:01] given the amount of people, I will
[13:02] probably do a little bit more um myself
[13:06] uh instead of like letting you um think
[13:08] about all of the things. Um, but I'll
[13:10] quickly give you an overview of of
[13:11] what's in the wrapper, right? Um, let me
[13:13] make this a little bit bigger. Um, I
[13:15] have made some pre-made uh slides that I
[13:18] will show you in a bit. Um,
[13:21] the resources is the main thing where
[13:23] you guys would be working in. So, you
[13:25] have the let me actually close this
[13:26] session for now. Um so you have like the
[13:28] agent. ML and this is basically where
[13:30] you would define your agent, right? Like
[13:32] um I think before we did a session. So
[13:34] this is basically what we're going to do
[13:36] use like the manage agent. So for the
[13:38] people who attended that session um
[13:40] before lunch, it's basically the same
[13:42] thing. We define here like an an agent
[13:44] in this case. Um and we have given this
[13:47] uh the system prompt, right? So this is
[13:48] a system prompt that we're giving. So
[13:49] basically you are a slide generation
[13:51] agent and when the user gives you a
[13:52] topic create a powerpoint file at this
[13:55] location and then also we tell it you
[13:56] have a shell um with bid pptx uh
[14:00] pre-installed right um so that's all we
[14:02] give it for now and then we also have
[14:04] like an environment which we've defined
[14:06] um with like a few packages um and what
[14:08] is it what it needs to complete this
[14:10] session um and then basically that's it
[14:13] we also have some other things defined
[14:15] but I will get to that I think maybe the
[14:17] first question that I have for the
[14:18] audience Today's we want to make a
[14:21] slight generation agent, right? What do
[14:24] you guys think is a good eval? What are
[14:27] you trying to measure? What would be
[14:29] some good information that you want to
[14:30] get out of evals?
[14:38] &gt;&gt; Number of words on slides isn't really
[14:40] useful uh thing to track.
[14:43] Any anyone else with some ideas?
[14:50] Yeah, absolutely valid. Absolutely
[14:52] valid. Yeah. Yeah. Yeah. Um and and this
[14:55] actually I like these two examples
[14:57] because they immediately give you like a
[14:58] different sense of um how you can use a
[15:01] type of graders like for example the
[15:02] number of words on a slide is
[15:04] quantifiable right it's like easy say
[15:06] you can count the number of words with
[15:07] like a deterministic grader with like a
[15:09] code grader. the one if it's like
[15:11] overlapping or if it's overspilling that
[15:13] one is harder to um um encode in code
[15:16] right so for this one you might for
[15:18] example use a model grader and that's
[15:20] exactly what we did right so we have
[15:22] actually defined for you guys already a
[15:24] few graders beforehand two specific uh
[15:27] uh directories we have the code and we
[15:29] have judge so the code one is as I said
[15:31] it's like these these code graders are
[15:33] quite derministic like for example if we
[15:35] take a look at emoji count for example
[15:37] is one um that we have defined where We
[15:40] basically just count the number of
[15:42] emojis present in the slide deck. Um
[15:45] because we we just noticed that it's
[15:47] quite prevalent. Like for example, if I
[15:49] open the slide deck, um let me go with
[15:53] environment one in this case. Um so
[15:55] these are the slides that I it's
[15:57] basically the agent running. Um it's
[15:59] it's done beforehand just because it
[16:00] takes can take quite a while um to get
[16:03] the agents running. Um but this is for
[16:05] example the results of the initial
[16:07] agents, right? So this is slide number
[16:09] one. Um slide number two. Slide number
[16:13] three. Um with some
[16:17] weird things on the bottom left. Um
[16:20] slide four and slide five. Now I think
[16:23] we can all agree like this is not the
[16:25] best slide deck you guys have ever seen.
[16:28] Um but it's a good start. At least it
[16:29] there's a slide deck. Um there's five
[16:32] slides. I think that's exactly the
[16:34] prompt that we send it. Um so we have a
[16:36] few slides. There's a few content on
[16:38] here. There's like a few boxes. It's,
[16:40] you know, it's a slide deck. Um, given
[16:42] these slides, is there anything else
[16:44] that you guys are seeing that like this
[16:46] is something that we would never want in
[16:47] our slide deck?
[16:58] &gt;&gt; What was that?
[17:00] &gt;&gt; No teal. We can if you absolutely want
[17:02] to avoid teal, that's absolutely right.
[17:04] I think in this it doesn't do that for
[17:06] every single slide like let me see for
[17:07] the career one. Um let me see what this
[17:10] Oh okay maybe it does always use you
[17:11] still actually but for example in this
[17:13] one we see like this
[17:15] overlap of like words and and and this
[17:18] this horizontal um what else do we have
[17:21] some weird coloring?
[17:23] Um yeah there there's a few weird things
[17:26] happening generally right. Um so yeah
[17:29] based on this we take you take a look at
[17:31] what it is what the results are and
[17:33] you're like hm what type of graders do I
[17:35] want to define for this specifically
[17:36] right and so we did that and we noticed
[17:40] for example emoji count is one that's
[17:42] quite prevalent we want to check how
[17:45] many times do we see an emoji popping up
[17:47] another one is for example cluttered
[17:49] slides like how many shapes do we see on
[17:51] these slides like if there's just so too
[17:53] many things it becomes cluttered um
[17:56] counting the number of slides for
[17:57] example We always ask for five slides.
[18:00] Making sure that you have five slides.
[18:01] Um do we have slides with image, small
[18:04] fonts, text heavy slides? Now this is
[18:06] this is in this case it's quite
[18:08] arbitrarily chosen, right? These were
[18:10] just like things that were like thought
[18:11] were like this is quite representative
[18:13] of what a slide deck might have for
[18:18] graders, right? It really depends like I
[18:20] want really want to stress this like it
[18:22] really depends from use case to use case
[18:24] what makes a good grader, right? I think
[18:26] generally the way I think about this
[18:28] thing is if you have a grader that you
[18:31] get no useful out of information out of
[18:34] then you should not have that part of
[18:36] your eval right like each thing you
[18:38] should be able to tell like for each
[18:39] single scenario that you're testing you
[18:41] should be able to say like this is the
[18:42] information that I want to get out of
[18:44] this this is the type of this is the
[18:47] part of the system that I'm testing and
[18:48] this is how I can act on if it's being
[18:51] degrading right um so those were just
[18:54] like a few codes once and then we also
[18:56] have a few judge ones. For example, the
[18:58] color judge, which basically judge
[18:59] what's the color contrast and then it
[19:01] gives a score from like zero to five. Um
[19:04] same with image um the layout text and
[19:08] this is the prompt that we give. Um let
[19:11] me close this one real quick.
[19:14] Oh, actually let me keep it like this.
[19:16] So this is basically the system prompt
[19:18] um that we give it. Um, oh, so it's
[19:22] saying, "Please evaluate the slide based
[19:24] on each of the following criteria. Text,
[19:27] the title should be simple and clear to
[19:28] indicate the main points. For main
[19:30] content, avoid too many text and keep
[19:32] words concise. Use a consistent and
[19:34] readable font size, style, and color."
[19:36] And I mean it it goes on and on, right?
[19:38] So we give like for each of the
[19:39] different things that you want to
[19:39] measure, we give like a little
[19:40] information of like this is what you
[19:43] should be focusing on when you want to
[19:44] measure this, right? Okay, cool. So we
[19:49] have these evals.
[19:51] Let's say you have now created a slide
[19:53] deck and you now want to see like okay
[19:55] what are the results right and how can
[19:57] we act on these results. So in this
[19:59] wpper we also have created this nice
[20:02] little script that will automatically
[20:03] score your slide deck for you. And so at
[20:06] the top here we basically have it all um
[20:08] listed out. So we have like the slide
[20:10] count which is being counted the slides
[20:12] the number of slides with image text
[20:14] heavy slides cluttered slides small font
[20:16] slides and so on. We also have our
[20:19] judges over here which are saying like
[20:20] they give a score from like zero to five
[20:23] based on like how good is the text, how
[20:25] good is the image, the layout and the
[20:26] color right. Um
[20:29] honestly like these scores you can
[20:31] immediately note that these scores are
[20:32] quite high. So as we said like we
[20:33] calibrated between zero and five and as
[20:35] we see like the scores you've been
[20:36] giving here like between 2.8 date and
[20:38] four which honestly I think are quite
[20:40] high given the slide deck that we have
[20:44] seen right so that's like a part of the
[20:47] calibration that needs to happen as well
[20:48] right I think this also like one thing
[20:50] that I maybe want to stress it's not
[20:51] because you have set up your evals once
[20:54] that they are now like the ground truth
[20:56] you know um evals over time they can
[21:00] evolve they need to be a living artifact
[21:02] it's not like something you make once
[21:03] and then forget and then use this like
[21:04] to make all of your future decisions on
[21:06] right because like we will see over time
[21:08] like as I go through all of the
[21:10] different examples that we have we will
[21:11] see like there needs to be a way also
[21:13] how we can see how we can make sure that
[21:15] the evals that we create are actually
[21:18] still measuring something useful for us
[21:19] right um if you ever hear people talk
[21:22] about saturation of evals that's
[21:23] basically what they mean in the way that
[21:25] like the eval is not giving any more
[21:28] relevant information that we can act on
[21:30] due to several reasons cool so we see
[21:34] this and I guess maybe the first thing
[21:36] that we want to do in this case is we
[21:38] want to make an agent that is a little
[21:40] bit more polished, right? And so for
[21:42] this we actually just update our system
[21:45] prompts. So in instead of just having
[21:48] like oh you are a slide generation agent
[21:50] make a slide deck we now give it a
[21:52] little bit more information of like what
[21:53] are the expectations that we have of you
[21:55] in terms of typography right um because
[21:58] as we noticed we said like oh the font
[22:00] is too small there's too many words on
[22:01] there it's not readable or it's too big
[22:03] right so we give it a little bit more
[22:04] information so we say like slide title
[22:06] should be this size section header
[22:09] should be this size body this size
[22:11] caption this size right um and we also
[22:13] give it some information on the layout
[22:14] and density like here are the things
[22:16] that we expect from the layout and
[22:17] density point of view. For example, we
[22:19] say keep the body text concise, leave
[22:22] braiding room and left aligned
[22:23] paragraphs, right? And then also we I
[22:27] think everyone kind of I mean I am at
[22:29] least getting like ticked off like if I
[22:31] read something that's clearly AI
[22:32] written, I'm always a little bit
[22:34] skeptical of if I can completely trust
[22:37] the content and if the p person sending
[22:38] me these texts is like has like read it
[22:40] himself or themselves and is standing
[22:43] behind that content. Right? So we also
[22:45] say like avoid these AI generated tells
[22:46] as well. So never use a thin accent
[22:48] lines in the titles and don't pepper
[22:50] slides with emojis as decorative icons.
[22:53] Right? So this is based on the things
[22:55] that we have seen in our EVA. Right? So
[22:57] we have seen as let's go back a little
[22:59] bit. We've looked at the slide deck um
[23:02] and we're like oh this is not properly
[23:05] done. These fonts are a little bit off.
[23:08] Um there's some emoji used in here. It's
[23:10] like a little bit all over the place.
[23:12] And then based on the score we were like
[23:13] okay these are the things they were
[23:14] clearly failing at right so we have like
[23:16] emoji counts four in this case small
[23:18] font slides also four as well cluttered
[23:20] slides too and text heavy slides right
[23:23] so based on the information that we have
[23:24] gotten from the eval that we have run we
[23:26] have made these changes to our new agent
[23:31] let me now pull up the result of the new
[23:33] agent that we have created in this case
[23:35] right um so this is slide one which I
[23:38] think is immediately way more enjoyable
[23:40] to look at like there's no overlapping
[23:41] stuff. Um, there's no dollar sign.
[23:44] That's just generally it's cleaner.
[23:47] This once again, I think this one still
[23:48] has like quite small text, but at least
[23:51] once again, we're like getting a little
[23:52] bit more consistent with the coloring as
[23:54] well. Um, once again, like the whole
[23:56] slide deck is more consistent. The third
[23:58] slide, the fourth slide, and the fifth
[24:02] slide, right? And this is just by
[24:04] basically identifying here's a few
[24:07] failure modes of our original one.
[24:08] Here's how we now make changes based on
[24:11] these things that we found in the system
[24:12] prompt. And now we run it back. And now
[24:15] once again we can do the same thing. So
[24:16] this we're now basically in this loop of
[24:19] finding what's wrong, iterating, finding
[24:21] what's wrong, running it again, and
[24:23] making improvements over time. So now we
[24:25] can take a look back at what we find
[24:27] over here. Oh, and this is actually way
[24:29] worse. Suddenly we see like emoji count
[24:30] 20. I'm wondering where they are. I
[24:32] haven't seen them actually.
[24:34] Wondering where that is at. Hm.
[24:39] Wonder if this like a mistake in this
[24:41] case. Um but generally we see like okay
[24:43] small font slides we've seen that but
[24:45] we've we've improved upon the
[24:46] cluttering. Um and let's see text heavy.
[24:49] Is that still the case? Um
[24:53] I think I think that's fine. I mean
[24:54] those are a little bit text heavy but I
[24:56] think it's acceptable. Right. So now
[24:59] we're like so this once again shows the
[25:02] value of like human review as well,
[25:03] right? Because now we see, oh, these
[25:06] things that we have defined in our evals
[25:08] are maybe not as well defined as we hope
[25:10] them to be, right? Because now I'm here
[25:11] arguing like, oh, this is not as text
[25:13] heavy as I expected it to be, right? So
[25:16] that means that something is actually
[25:17] wrong with the way we're grading. So now
[25:19] we go back then we would go back, go to
[25:21] our grader, change the grader, update
[25:23] it, and make sure that it better
[25:25] reflects the actual thing that we want
[25:26] to measure, right? And this is also not
[25:28] something to be underestimated like this
[25:30] calibration of how your agent should
[25:32] behave um and how your judges should
[25:34] judge the specific a output is really
[25:37] something very fickle right like you
[25:39] should spend like proper time trying to
[25:41] find the ways on how you should make
[25:43] this happen. Um let's say now that we
[25:47] want to have an agent like I I think
[25:48] with this one I mean it's fun. I think
[25:50] it's nice um but it's still quite text
[25:53] heavy and it's only text right. Um,
[25:56] let's say now that we want to have an
[25:57] agent. Let's say that's one of our
[25:58] requirements, right? That we have an
[26:00] agent that we always want to have
[26:02] includes diagrams. Once again, we go
[26:05] back to our system prompt, we update it,
[26:07] and we now say every slide must include
[26:09] at least one generated diagram or chart
[26:11] inserted as an actual image, right? Um
[26:15] so once again we update the system
[26:17] prompt or any part of the agent that you
[26:20] can tune and then we go again and we
[26:23] check what do we get.
[26:26] Okay so this one is quite interesting.
[26:28] Um I guess personally I'm not a fan of
[26:30] having an image on the opening slide but
[26:34] once again it is what we defined that it
[26:36] should do right. So I'm going to let
[26:37] that slide but it's a nice nice graph
[26:39] what it's saying it's like no
[26:40] negotiation and active negotiation. So
[26:42] it's arguing that if you do active
[26:44] negotiation for your salary, you can see
[26:46] over time the gap widens between no
[26:48] negotiation and yes neg negotiation some
[26:51] extra benchmarks. I I think this looks
[26:53] immediately way better just in the way
[26:56] that like kind of grounded into some
[26:58] actual facts right now instead of just
[27:00] waffling its way through the slide deck.
[27:04] Yeah. This one I'm not a big fan of. I
[27:06] feel like it's a little bit stretched,
[27:08] but that might also just be the
[27:10] screenshot. Um, yeah. And this one also
[27:13] not the best one either, right? Let me
[27:17] see like let's see what the score.json
[27:19] now says. Okay. No emojis. Great. No
[27:21] cluttered slides. Still quite text heavy
[27:23] slides surprisingly. Um, still small
[27:26] font slides. I think that's fine. I
[27:27] think we just say like with images. I
[27:29] think yeah, I think we we accept like
[27:33] these types of things are fine. Um so
[27:36] once again shows you some um questions
[27:38] regarding the creator that we have set
[27:40] up but now we can also take a look at
[27:42] like the judges right like for example
[27:43] because now we have images that we have
[27:44] created so now we can also consider how
[27:46] does the image judge uh think this is
[27:48] and it says it's 3.8 eight out of five.
[27:51] Um, doesn't say give us a lot to go off,
[27:54] right? It just gives us a random number.
[27:57] What does it mean? How can we improve
[27:58] upon this? But that's fine for now.
[28:02] Now, one thing that we always see that
[28:04] works just generally quite well. And
[28:05] that's like it's transversal over every
[28:07] single use case is adding a QA loop,
[28:11] right? Um, for coding, this is quite
[28:13] intuitive. That's basically saying like
[28:14] you create an agent that actually is
[28:17] writing the code, right? And then you
[28:19] add a second agent that is then looking
[28:21] at the code that has been written and
[28:22] just criticizes it. So it's basically
[28:24] saying this is bad, this is bad, this is
[28:26] bad, this introduced a bug, this
[28:28] introduced a bug, this is not according
[28:29] to standards, whatever. Right? So it
[28:31] basically is criticizing the the thing
[28:33] that has been created and then that part
[28:35] of the feedback you give back to your
[28:37] original agent, the creation agent. The
[28:39] creation agent goes off again, does the
[28:41] creation, does the finetuning, makes the
[28:43] changes that were informed by the
[28:45] criticizing and then once again after
[28:47] that is done, it goes back to the
[28:49] criticizing agent. And that loop
[28:50] basically goes on and on and on until
[28:52] both sides are like, okay, this is fine,
[28:54] we can ship this. And that's basically
[28:56] what we now do in this uh next step.
[29:00] Um, so we basically say like, okay,
[29:02] required QA loop. Um, assume there are
[29:05] no problems. Um, I assume there are
[29:08] problems and then your job is to find
[29:09] them. Approach QA as a bug hunt, not a
[29:12] confirmation step. And this is quite
[29:13] interesting because we're like actively
[29:15] instructing the agent to behave in a way
[29:18] adversar adversely, right? Like we're
[29:20] saying like there are issues, you need
[29:22] to find them. It's not it's not like oh
[29:24] there might be something you might be
[29:25] interested in finding something. No,
[29:26] it's actively saying there are issues go
[29:28] find them. Um, and then we say like we
[29:31] instruct after writing the deck, okay,
[29:32] convert it to images. Inspect every
[29:34] slide image yourself. fix issues,
[29:36] rerender, reinspect, and then do not
[29:38] stop until you've completed at least one
[29:40] fix and verify cycle. Cool. Now, as I
[29:44] said, I think for coding, this is quite
[29:46] intuitive, but I think it's also quite
[29:48] intuitive if you take a look at like um
[29:51] the the slides that we have created,
[29:52] right? Because that's basically what we
[29:53] did. We have looked at the slides and
[29:55] we're like, "Ah, this is not good. This
[29:57] is not good. Let's take that feedback,
[29:59] update our creators, update our system
[30:01] prompt, and let's run it back again,
[30:03] right? So let's now see if we can
[30:04] actually if this is actually showing
[30:06] some improvements. Um I think this is
[30:10] immediately a lot better. So the the the
[30:12] image is way bigger now. I think it's
[30:14] way more readable even from a further
[30:16] distance away. Um still the slides are
[30:18] small but like for example it's source
[30:20] now. There's a source over here as well
[30:21] which is quite good. Um I think this is
[30:24] also way better. It is more cleanly
[30:26] structured. I think the image is also a
[30:28] little bit better as well. Right. a
[30:31] quite interesting graph in this case. Uh
[30:33] your value profile versus team average.
[30:37] This one is still a little off in my
[30:39] opinion. Also, we now have like a little
[30:41] introduction of like these weird ticks.
[30:45] and this one is also a little bit
[30:47] better, I would say, but I think like
[30:48] the just the image taking is um kind of
[30:50] messing with the slide here. And so then
[30:53] we kind of know the drill by now. We
[30:55] take a look at the score. We see like
[30:57] has it improved? Why do we see still
[30:59] gaps? And now we see like for all of the
[31:01] judges that we have created, it is
[31:02] higher than uh the ones before, right?
[31:04] We're now all good in the 4.2 to 4.4
[31:08] now. Um so we're on a we're on a good
[31:10] track, right?
[31:12] And um you can keep on doing this. You
[31:14] can keep on doing this. Um
[31:17] and you will always make like this
[31:18] little changes. But sometimes and this
[31:20] is I guess where it gets quite
[31:22] interesting and more like more like
[31:24] nuanced is you can also just go to a
[31:28] smarter model right because like now
[31:30] you're like defining oh this is what a
[31:32] good slide should look like this is what
[31:33] it should do this what what it should
[31:35] not do but with these models getting
[31:38] smarter and better over time you kind of
[31:40] expect them to be like able to figure
[31:42] that out on their own right um I mean
[31:45] that would at least be nice so that's
[31:47] what we tried out as So now in the last
[31:50] one we basically just changed our model
[31:52] to opus 47 instead of sonnet 47 which we
[31:56] have used up to this point if you can
[31:58] 46. Um so now we have switched to opus
[32:01] 47 and we have basically just given it a
[32:03] simple prompt again like you are a slide
[32:05] generation agent and then when the user
[32:07] gives you a topic create a powerpoint
[32:09] file at whatever and then you have a
[32:11] shell. So it's basically just the
[32:12] initial prompt that we gave to our
[32:14] sonnet model in the beginning, right?
[32:16] And then once again, let's now consider
[32:20] taking a look at the results of those
[32:24] and this is just a base prompt, right?
[32:26] Like you can immediately see like it's
[32:28] significantly better than the sonnet
[32:29] one, right? I think there's still clear
[32:31] issues that we can iron out, but
[32:34] generally like it's way more structured,
[32:36] right? And then we can take a look at
[32:38] the score as well. And I think this is
[32:40] quite interesting and quite telling.
[32:41] Like for example,
[32:44] Opus just does not use any emojis. Like
[32:46] it kind of knows like if you want to
[32:48] make a slide deck about salary increase,
[32:51] emojis are probably not right place to
[32:53] put them, right? Um it also has like
[32:55] fewer small font slides because it's
[32:57] kind of has like this innate knowledge
[32:59] of okay, it should be readable. This is
[33:01] how a slide deck should function. This
[33:02] is what people expect out of a slide
[33:04] deck, right? And then we get to these
[33:06] judge graders, right? Um, we see a 4.4.
[33:10] We see a five for the image. Do we even
[33:12] have an image in this one? I don't think
[33:13] we do, actually.
[33:16] No, we don't. Okay. But, so once again,
[33:17] we got a five in this one. Layout judge
[33:19] 4.2 and then a color judge 4.8 and title
[33:23] body coherence 4.4. So, this is like
[33:25] immediately giving like extremely high
[33:26] scores as well, right? Which I think is
[33:28] quite interesting because like this is
[33:29] once again showing that we might not be
[33:32] measuring the right thing.
[33:34] And this is not too unexpected for these
[33:36] types of um graders right or for these
[33:39] judge graders. I think one of these
[33:42] things with like I okay let's go to the
[33:45] code gra I think those are quite
[33:46] straightforward I think most people in
[33:48] the room would have understood by now
[33:49] like how they work and how what we can
[33:51] do them like for example emoji count
[33:53] it's quite simple just count the number
[33:55] of emojis and that's it but with this
[33:58] judging what we have done here is
[34:00] actually quite problematic we basically
[34:04] say like give a score from 0 to five and
[34:07] for text well the text should the title
[34:09] should be simple and clear to indicate
[34:10] the main point for main content, avoid
[34:11] too many text and keywords,
[34:14] but it has nothing to anchor on, right?
[34:16] Like it doesn't really know what good
[34:17] looks like in this case. It doesn't know
[34:19] what bad looks like. So there's still
[34:21] like this trade-off between like what
[34:23] does a model actually know and what do
[34:26] we need to give more information on to
[34:29] the model to make sure that it can give
[34:31] like a proper um proper judging of what
[34:34] we actually have produced. Right? So for
[34:37] example in this case um I would for
[34:39] example say what could help is say like
[34:42] oh this is a bad example like let's say
[34:44] you have a zero like everything is just
[34:46] awful these are some telltale signs that
[34:48] you're dealing with an extremely badly
[34:49] formatted um um slide deck and then like
[34:53] over time the different ranges you can
[34:55] kind of express um and then once over
[34:59] time uh once again like that doesn't
[35:01] mean it will still be able to give like
[35:02] a good answer because
[35:05] we now have these results. We have this
[35:08] number that our LLM decided to
[35:12] output for some reason. Like for
[35:13] example, in this in this case, image
[35:15] just put out five.
[35:17] Okay, what do we do with that number
[35:18] now? Okay, it's a five. We we we just
[35:20] said there was no not a single image in
[35:22] that slide deck, right? Um so how can we
[35:25] interpret this five? One way of doing
[35:28] this is just basically always asking
[35:29] your judge graders to give reasons why
[35:33] it came to that conclusion, right? And
[35:36] one thing that should be very like um
[35:38] cautious about is the ordering, right?
[35:41] Um I've had it happen where I was like
[35:42] setting this up and I did like this
[35:45] exact thing. So I had like the number
[35:46] and then I said like, "Okay, give me
[35:47] also the reasons why you did that." And
[35:49] so then it said like, "Oh, it's a four
[35:51] and the reasons for this are this, this,
[35:52] and this." But we know that an LLM it
[35:55] works auto reggressively, right? So if
[35:57] it is anchored on like this four, it
[35:59] will do anything it can to argue why it
[36:01] should be a four, right? Anything. And
[36:04] even if it's like extremely bad, if it's
[36:05] like if it should be like a one, it will
[36:07] still say, "Oh, it is good for these and
[36:09] these reasons because it needs to
[36:11] justify the four that it put out."
[36:14] So once how you do it is you actually
[36:16] turn it around. So first you say like,
[36:18] "Give me a bunch of reasons. Give me
[36:20] pros, give me cons, give me reasons why
[36:21] it should be high, give me reasons why
[36:22] it should be bad." And then based on all
[36:24] of those reasons together, then you need
[36:27] to make a final decision on the output,
[36:29] right? And that's also that goes also
[36:31] back to like this QA loop as well. Um
[36:33] because then once again you can get a
[36:35] little bit tricky here where you have
[36:36] like multiple agents also doing the
[36:38] verification part where you have like
[36:40] one agent that is like finding all of
[36:42] the issues and then the other one is
[36:44] like refuting those. For example, one
[36:46] example that I can give which I think is
[36:48] quite interesting. Let's say you want to
[36:49] make um a document for um where you need
[36:54] to like some analysis. You first need to
[36:55] get a lot of context from the internet
[36:57] for example like on a legal document for
[36:59] example right um and you ask the you ask
[37:02] a model to like make a summary of um a
[37:05] certain case what was decided what does
[37:07] this have for legal implications for
[37:09] other cases right you need to be very
[37:11] careful with like all of these things
[37:12] that like legal cases are generally
[37:14] quite tricky and like an agent would
[37:16] love to create like oh this and this and
[37:17] jump to conclusions like this is the
[37:18] reason and that's it right and then the
[37:21] creator might be like oh this is unclear
[37:23] this is um maybe not as this is maybe in
[37:27] uh untrue. This is maybe uh maybe like
[37:30] glossing over the actual facts all of
[37:32] those type things, right? But then once
[37:34] again you can like apply these multiple
[37:36] techniques. You can have like multiple
[37:38] graders for example seeing like um
[37:40] evaluating those and seeing like what
[37:42] are the main ones popping up um because
[37:44] once again a grader might still
[37:46] elucinate things as well, right?
[37:47] Especially in like these very nuanced
[37:49] scenarios, right? So there's like
[37:51] different ways of how you then can work
[37:53] with these judges to make sure that you
[37:55] actually get like good consistent output
[37:57] that is actionable, right? And what I've
[38:01] shown you here today is basically just a
[38:03] small introduction to how eval can help
[38:05] you, but it's definitely not the end. I
[38:08] think 45 minutes for a session on evals
[38:10] is in my opinion quite short because it
[38:13] can get really deep, right? Because like
[38:16] I started this off this session with
[38:17] talking about benchmarks which are in
[38:20] the end just eval
[38:23] why would every single model provider
[38:25] care so much about benchmarks so much
[38:27] about evals if it wasn't one of the main
[38:29] important things when we are building
[38:31] new models right
[38:36] &gt;&gt; exactly we need to find the things that
[38:37] we are failing at exactly we need to
[38:39] find things what are we good at what are
[38:41] we bad at how can we make the model
[38:43] better in future generations and That's
[38:45] the same thing when building
[38:47] applications that are consisting that's
[38:49] using AI agents, right? It's the same
[38:51] thing. It's just finding what works,
[38:54] finding what doesn't, iterating, and
[38:56] making sure that the changes that you're
[38:58] making that you're informed on the
[38:59] decisions that you are making and making
[39:01] sure that the changes you make have
[39:02] actually positive influence on your
[39:05] final output. Okay, thank you guys so
[39:08] much. This is all the time that I have.
[39:09] Thank you guys.
