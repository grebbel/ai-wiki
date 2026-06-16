---
title: 'AI Dev 26 x SF | Anush Elangovan: Impact of AI on Software'
video_id: FMpgh2QfX_g
url: https://www.youtube.com/watch?v=FMpgh2QfX_g
channel: DeepLearningAI
channel_id: UCcIXc5mJsHVYTZR1maL5l9w
channel_url: https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w
publish_date: '2026-05-19T13:59:14-07:00'
upload_date: '2026-05-19T13:59:14-07:00'
category: Education
duration: '14:24'
length_seconds: 864
view_count: 532
is_live: false
thumbnail: https://i.ytimg.com/vi/FMpgh2QfX_g/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgVShBMA8=&rs=AOn4CLBAtO7vEQRzpl6iGaTClzp0gyq7yg
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "Anush Elangovan from AMD, explored the transformative impact of AI on software engineering and development at AI Dev 26 x San Francisco. \n\nHe described a \"K-shaped\" divergence where higher-level skills like systems thinking, judgment, and problem framing are accelerating, while lower-level tasks like specific language syntax and formatting are becoming less critical.\n\nAnush introduced the concept of \"intent velocity\"—the speed at which an idea can move from conception to production—as the new primary measure of success, rather than traditional metrics like lines of code.\n\nThe talk concluded by urging leaders to lean into agentic AI, noting that agents now monitor bugs, file pull requests, and validate code autonomously in his daily workflow."
notes: Auto-generated ASR. Skill engagement-panel route succeeded on 180-second retry (initial 30s timeout failed; recurring failure mode for AI Dev 26 SF talks). No further ASR cleanup applied.
---

## Transcript

[0:07] Good morning, San Francisco. I was told

[0:10] to yell in here, so I hope you can hear

[0:12] me. Okay, good. At the back. Okay. Um,

[0:16] this is great to be here in the city uh

[0:18] where every wave of software innovation

[0:22] has either started or has come to reckon

[0:25] itself here.

[0:27] Starting from mainframes,

[0:29] client server. I know these all like you

[0:31] know some of you know these words but

[0:34] mainframe client server the web mobile

[0:39] cloud and now AI. But I will tell you

[0:43] this AI is coming at you so much faster

[0:47] than each of those other transitions.

[0:50] And I've been able to live through those

[0:52] transitions. this is happening in the

[0:54] order of months and weeks compared to

[0:56] things that took um decades or or years.

[1:01] So before I get started on talking about

[1:04] the impact of AI on software, I do want

[1:06] to spend a minute uh acknowledging

[1:09] Andrew uh thanking I want to thank him

[1:12] for something he did about like 12 years

[1:14] ago. uh we were a small startup working

[1:17] on gesture recognition and and u you

[1:21] know uh this was pre-AII right before

[1:24] the the term AI was popular and he

[1:27] awarded us the uh best AI startup award

[1:30] in 2014 and that team now runs most of

[1:34] AMD's software uh AI software team so

[1:37] just a legendary like visionary that can

[1:39] see things 10 12 years ahead so it's

[1:41] great to be here with partnering with

[1:44] deep learning AI and you know um looking

[1:47] forward to learning from him on what is

[1:49] like 10 12 years from now. So

[1:53] before I get started, I do want to um

[1:57] you know preface this with you know this

[1:59] there there's a there's a slide that I

[2:01] cannot unsee or something that came up

[2:03] on social uh and it's attributed there.

[2:06] You can go check it out. It was called

[2:07] the K-shaped future of software

[2:09] engineering and I completely agree with

[2:13] what this assessment looks like and it

[2:17] is a uh a way to frame your thought on

[2:20] AI and how AI can be consumed and

[2:24] processed. So what we will look for in

[2:28] this and this I think is backed by a a a

[2:31] paper that came out of Harvard that did

[2:33] this analysis. Um what rises in the top

[2:37] arm of the K-shaped future is systems

[2:41] level thinking uh judgment and taste,

[2:44] intuition, uh problem framing, how how's

[2:47] your harness set up? So all of these are

[2:49] like higher level constructs and that is

[2:52] what is going to be accelerating. So

[2:55] you'll have a a section of your team

[2:58] that is just supercharged with that,

[3:01] right? and they'll be generating

[3:03] monstrous amounts of code but they have

[3:05] the framing of the problem. They know

[3:08] they know how how to solve the problem

[3:10] and they're thinking at it still the

[3:12] first principles thinking um is still a

[3:16] a big part of it. What falls is whether

[3:20] you know how to code in a specific

[3:23] language, right? Whether you know how to

[3:25] uh format your uh Python or syntax. And

[3:29] yes, that's still important when you if

[3:31] if you need to go look at it, but

[3:35] increasingly um you do not need to know

[3:37] any of that, right? And that is just

[3:40] intermediate language for your AI agents

[3:42] to consume. Um so it it is very uh you

[3:46] know um important to acknowledge this

[3:49] transition and we do see this in the

[3:53] industry. We are seeing, you know, teams

[3:55] that just suddenly become 100x more

[3:57] productive. And there are people that

[3:59] the wingspan of what they're working on

[4:02] moves from like higher levels of the

[4:04] stack, lower levels of the stack. And so

[4:06] how you measure the outcome is not

[4:08] necessarily uh necessarily lines of

[4:11] code. It is outcomes for your business.

[4:13] Right? So can we can we unlock a

[4:16] specific um use case? Can we do

[4:18] something that we just thought is not

[4:20] possible? And we have been um at AMD

[4:24] trying to do this quite a bit. And I'll

[4:26] I'll hit a few samples of what we

[4:29] thought was not possible like 6 months

[4:31] ago and now it's just like an overnight

[4:33] project that someone sits down, you

[4:35] know, with a cup of coffee and and they

[4:37] have it done, right? Okay.

[4:41] Um when when that K divergence happens,

[4:44] what is your mode? And I keep repeating

[4:47] this. Um I I think speed is the mode and

[4:50] your I'll call it intent velocity is

[4:55] what you want to measure. So you you

[4:58] know how fast can you take an idea that

[5:00] you're thinking about to actual

[5:02] production and everything else in

[5:04] between is just it's just a means to get

[5:08] to the end right um so intent velocity

[5:10] just internalize that it's like okay I

[5:13] need to go do this and how fast can I do

[5:16] that right and if you uplevel that it

[5:19] all comes back to how fast you move

[5:21] because what was cool and new last week

[5:25] isn't that today, right? And so what you

[5:28] want to do is try to adapt and and be

[5:32] ready for change. Um, so you know,

[5:36] winners operate in parallel. This is

[5:37] another one that I I think you want to

[5:40] internalize. It is not necessarily about

[5:43] singular throughput. It's about how much

[5:45] your um your agent span

[5:50] u you know uh can cover, right? And so,

[5:52] for example, at night, I have like four

[5:54] or six agents that are crunching away

[5:56] and they're doing something in parallel.

[5:58] So, you want these things to just be

[6:01] running autonomously at night or when

[6:04] when when I'm doing this keynote, you

[6:06] know, my agents are crunching away. This

[6:08] is something that you couldn't do in the

[6:10] past. And you want to set the intent and

[6:12] then unlock them to start running,

[6:14] right? Um, and this is going to be a

[6:18] flywheel. the faster you move, the

[6:20] faster you're going to go up that K

[6:22] curve and the divergence is going to be

[6:24] stark, right? And and as leaders who

[6:26] have large uh organizations, I think the

[6:29] responsibility will lie on us to see how

[6:32] you reduce the divergence but not

[6:34] necessarily slow down the upper arm of

[6:36] the um you know um uh output of the uh

[6:40] upper arm.

[6:42] So um let's talk about rockom uh for a

[6:45] second. This is just uh an AMD

[6:47] portfolio. AMD has traditionally had a

[6:51] very very strong uh hardware portfolio.

[6:53] We we have a pervasive hardware strategy

[6:56] starting from laptops, desktops,

[6:58] workstations, um edge AI, cloud and data

[7:01] center. But what we wanted to do next

[7:04] was try to make sure that we brought in

[7:07] the software layer and AMD has always

[7:10] had a open ethos and open software

[7:13] mindset. Um and so that was our founding

[7:17] like you know pillar in terms of how we

[7:19] approach software and then the second

[7:22] one was how we brought up abstractions

[7:24] right like you didn't have to program

[7:26] deep in the details of GPUs but the cool

[7:29] thing is what's happening now with AI we

[7:32] layer all of this with AI and we're now

[7:34] able to unlock software acceleration

[7:36] that has not been possible in the past

[7:39] um in the order of days and I'm going to

[7:41] go through a few of the examples that I

[7:43] have here um that we'll we'll talk

[7:45] about. But the acceleration is just

[7:49] huge. And what I would take away for

[7:51] each of your efforts is how you apply at

[7:54] apply AI at every layer of the stack. Uh

[7:57] and luckily for AMD, it's fully open

[7:59] source. So all of the frontier models

[8:03] understand our stack end to end. And so

[8:05] it's really really easy to program on

[8:08] AMD with AI.

[8:11] So I'm going to uh touch on three

[8:13] different um you know project three or

[8:15] four projects. Uh I I'm not going to

[8:17] keep it too long and I can chat about

[8:18] this after the keynote. Uh so we did

[8:20] something called geek which is one of

[8:23] the the big pain points we had which was

[8:25] performance on you know uh the software

[8:27] and how we achieve it. So now we have an

[8:30] agent loop that just understands what

[8:32] the customer is running and it

[8:34] autonomously just optimizes the software

[8:38] non-stop. Um and this has shown us like

[8:41] immense amount of uh outcome right like

[8:44] and customers actually see the value

[8:46] they are able to serve tokens much

[8:48] faster and and this is uh this is what I

[8:50] mean by you want to aim for your like

[8:53] outcome we wanted faster time to

[8:56] performance and geek was one of those

[8:58] projects that provided us that

[9:02] um we did another one again this is uh

[9:05] uh it's like Rosetta um which is like we

[9:08] can we can translate machine ISA from

[9:12] one GPU to another on the fly. Years

[9:16] ago, this would this was literally like

[9:18] I know of implementations that took four

[9:20] five years and

[9:22] I know like 200 300 people to implement

[9:25] because each ISO you have to like each

[9:28] instruction you have to make sure it's

[9:30] mapped correctly. It's it tests well. It

[9:32] was a real software engineering project.

[9:35] The first prototype of this took about

[9:37] like 48 hours and I think it's about

[9:39] like a few billion tokens of uh um I I

[9:43] forget it was cloud cloud code or Opus

[9:45] 4.6 and now we are shipping it in

[9:48] production. You can actually take an old

[9:52] um older generation hardware, run it on

[9:54] newer generation hardware or vice versa.

[9:56] Like we're doing code design of hardware

[9:58] that's coming out in 2 3 years running

[10:00] on current generation GPUs seamlessly at

[10:03] native speed. And this would have been

[10:06] just like something that we we we can't

[10:09] we couldn't even plan right like

[10:10] software engineering our thing is like

[10:12] we were limited by oh why would you do

[10:14] something like that? You're you're doing

[10:16] something too hard, right? Now there is

[10:18] no such thing as too hard. You just have

[10:20] to have an intent saying I'm going to

[10:22] attempt that too hard thing. Don't tell

[10:24] me not what not to do and just go

[10:27] attempt it. Right? You you have to frame

[10:29] the problem. You have to guide it. You

[10:31] have to understand where are the

[10:32] pitfalls so you don't get lost. But the

[10:35] you you are now limited by your ability

[10:37] to like think forward and not by what

[10:40] you're like churning out in terms of

[10:42] lines of code.

[10:44] Um, another one that we we we've been

[10:47] like, you know, beat up on a little bit

[10:48] was like Llama CPP and and how it

[10:51] integrates with AMD GPUs. There was a

[10:54] little hard problem to make sure that

[10:56] you could seamlessly move tensors

[10:58] between CPU, GPU, NPU. And again, we did

[11:02] a new runtime that has like zero cost

[11:05] overhead to move tensors seamlessly and

[11:08] partition data and and compute across

[11:11] CPU, GPU, NPU. the first integration is

[11:13] going to come out on Llama CPP so that

[11:15] you can now use your laptops and use all

[11:17] of the silicon that's available. I do

[11:19] believe that um the ability to consume

[11:24] AI is going to shift to wherever there

[11:28] is compute AI will consume it and and we

[11:31] want to enable that on your laptops too.

[11:33] So that that was another uh uh good um

[11:36] outcome that we had. Um we also built a

[11:40] tokenizer. One of the uh you know

[11:43] bottlenecks of uh LLM inferencing is the

[11:46] first part of it which is token which is

[11:48] the tokenizer. And there had been a area

[11:51] that not a lot of people had focused. Uh

[11:54] it was one guy and 200,000 lines of code

[11:57] generated and we have like the world's

[11:59] fastest tokenizer now. Again it's all

[12:01] open source. It's it's more tokens for

[12:04] the future tokens to learn from. And

[12:06] that's why it's a flywheel effect

[12:08] because all what we created now you have

[12:10] a reference your your models will learn

[12:13] from it and know that hey there's a

[12:15] tokenizer that works fast, right? So the

[12:17] next time you ask for building

[12:19] something, it's going to have this in

[12:21] its pre-training data and know how to

[12:22] execute and move faster. And that's why

[12:24] it's a compounding flywheel effect of um

[12:28] of impact.

[12:30] I will um I I will you know uh finish

[12:35] with a few thoughts. Uh one is you know

[12:38] um obviously the K shape is real. Uh

[12:41] it's moving really fast. In December I

[12:44] thought um agents were um prompts in a

[12:48] cron job. I I don't know how many got

[12:51] that but but it literally is like you

[12:53] know it's just a yeah sure it's a it's

[12:55] an agent. Um but now there is no way I I

[12:59] think I can do my job um without having

[13:03] the agents running continuously and they

[13:06] are like off the bugs that we have on

[13:09] those models and those uh those projects

[13:12] there are agents that are monitoring

[13:13] them for issues that are filed PRs that

[13:15] are filed and they're going to respond

[13:17] to that automatically and I'm not even

[13:19] even involved. All I've told the agent

[13:21] is that make sure every bug is

[13:24] recreated. Every bug is fixed with

[13:26] another is fixed and then there's

[13:28] another test that validates all of it

[13:31] and then commit it if the CI is green.

[13:33] And those projects that I showed you are

[13:36] actively being, you know, um monitored

[13:39] and and worked on. So the change is

[13:41] real, the change is fast. And what I

[13:44] would recommend is or what what based on

[13:47] what I've seen is one it it is changing

[13:50] our trade and and the skills that we

[13:53] have to um you know to operate. And so

[13:57] it's uh the analogy I'll use is like

[14:00] oxygen masks. First put one on yourself

[14:02] and then help the person next to you. Uh

[14:04] make sure you bring them along too. But

[14:06] you do need to put that oxygen mask on

[14:09] and start like you know just really

[14:11] leaning into agentic AI because uh the

[14:14] future is coming very fast. Thank you.

