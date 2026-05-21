---
title: 'Stanford CS153 Frontier Systems | The AI Native Company: How One Founder Becomes a 1000x Engineer'
video_id: Lri2LNYtERM
url: https://www.youtube.com/watch?v=Lri2LNYtERM
channel: Stanford Online
channel_id: UCBa5G_ESCn8Yd4vw5U-gIcg
channel_url: https://www.youtube.com/channel/UCBa5G_ESCn8Yd4vw5U-gIcg
publish_date: '2026-05-20T10:36:41-07:00'
upload_date: '2026-05-20T10:36:41-07:00'
category: Education
duration: '47:14'
length_seconds: 2834
view_count: 3238
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi/Lri2LNYtERM/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGHIgXyg9MA8=&rs=AOn4CLDh03RicmyzqZBYGSVQH6VC5m6BGg
keywords:
- Stanford
- Stanford Online
- Artificial Intelligence
- AI
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "For more information about Stanford's online Artificial Intelligence programs, visit: https://stanford.io/ai\n\nFollow along with the course schedule and syllabus, visit: https://cs153.stanford.edu/\n\nIn a CS153 Frontier Systems lecture, the class shifts from upstream bottlenecks like power and compute to the capital and company-formation layer, framing YC's 2010s introduction of the SAFE as a standardization moment for venture capital comparable to the buildout of the electrical grid. \n\nGuests Garry Tan, CEO of Y Combinator, and General Partner Diana Hu argue that agentic coding, unlocked by Claude 4.5 in late 2025, has collapsed the unit of production: Tan recounts rebuilding his old startup Posterous in five days on a $200 Claude Max plan and shipping his open-source GStack and GBrain projects to over 100,000 GitHub stars. They walk through agentic primitives — skills, resolvers, Skillify, evals, and a three-layer memory system — and map them onto company structure, with skills as employees, resolvers as the org chart, and CheckResolvable as audit and compliance. Hu closes by arguing AI-native companies run as closed-loop systems with one or two million dollars in revenue per employee, citing YC portfolio companies Salient, Happy Robot, and Reducto as forward-deployed examples and pointing to white space across back office, finance, and customer service for one-person frontier companies.\n\nGarry Tan is president and CEO of Y Combinator and a General Partner. He was a partner at Y Combinator from 2011 to 2015, where he built key parts of the YC experience for founders including Bookface and the Demo Day website. Garry is the co-founder of Initialized Capital and Posterous (YC S08), a blog platform acquired by Twitter, and prior to that, he was an early designer and engineering manager at Palantir (NYSE:PLTR), where he designed the company logo. Garry holds a BS in Computer Systems Engineering from Stanford.\n\nDiana Hu is a General Partner at YC. She was co-founder and CTO of Escher Reality (YC S17), an Augmented Reality Backend company that was acquired by Niantic (makers of Pokémon Go). At Niantic, she was the head of the AR platform. Previously, she led data science at OnCue TV that was sold to Verizon. Originally from Chile, Diana graduated from Carnegie Mellon University with a BS and MS in Electrical and Computer Engineering with a focus in computer vision and machine learning.\n\nFollow the playlist: https://youtube.com/playlist?list=PLoROMvodv4rN447WKQ5oz_YdYbS74M5IA&si=DOJ5amlyRdyMJBhG"
notes: ASR transcript fetched via youtube-transcript-skill (Playwright path).
---

## Transcript

[0:09] We are super lucky to have with us today Gary Tan and Diana from YC.

[0:15] [applause]

[0:19] Um before we dive in, I'm going to do a couple minutes of in uh sort of warm up.

[0:28] This is a really special lecture because for for a couple reasons one um this class

[0:37] CS 153 which as you know Mike and I started teaching four years ago which was security at scale uh small group 50

[0:46] people was inspired by is sort of a composite of several different classes that have been taught at Stanford by Silicon Valley leaders and when I was an

[0:55] undergrad sophomore year Peter taught um Peter Thiels taught the first version of uh how to start 0ero to one that it was

[1:04] 1 minute, 4 seconds CS 183 how to start a startup and that became the book 0ero to1. The following year, YC taught a a version of that

[1:12] 1 minute, 12 seconds class uh that Sam put together and Gary was at YC at the time or I think it just started initialized, right?

[1:21] 1 minute, 21 seconds And uh and so those are the spiritual descendants of this class. And then there's CS43N which was Terry Windows class we've talked about. That was computers in the open society which was

[1:30] 1 minute, 30 seconds the first freshman seminar I took. And so over the years, we've tried to, you know, sort of take the best parts of all those classes and and bring it together

[1:38] 1 minute, 38 seconds in 153. But I think it's just really poetic to have Gary back because based on many of the, you know, things Gary

[1:45] 1 minute, 45 seconds learned here at Stamford, he went out and sort of took the spirit of Stamford out to Silicon Valley. um and to have him back and be able to talk about, you

[1:54] 1 minute, 54 seconds know, um all of his work and and now with Diana helping to update some of the the the sort of YC philosophy that I

[2:03] 2 minutes, 3 seconds want to we're going to talk about. It's sort of a close the loop moment. So, thank you guys for coming back. It's really appreciated. Yeah, thanks for having us.

[2:11] 2 minutes, 11 seconds Oh, no. This is this is the fun part. So um I'm going to let you be before we sort of dive in. I'd like to give a

[2:18] 2 minutes, 18 seconds couple minutes of sort of context on why I think this is an important lecture for you guys. So as you know 153 is a systems class. You know you've heard up

[2:27] 2 minutes, 27 seconds and down the stack from uh land power shell and energy like Scott Nolan at General Matter to the chip layer. We had

[2:35] 2 minutes, 35 seconds Jensen last week. Um there's a full rewrite of systems going on to unblock bottlenecks on frontier progress right

[2:42] 2 minutes, 42 seconds in the world. Um one of those things that you need that we need to unblock bottlenecks on is capital. And uh as you

[2:50] 2 minutes, 50 seconds heard from Ben Horowitz a few weeks ago, you know, Mark and Ben came up with a system to try and scale that deployment of capital in Silicon Valley over 10 years ago and are now thinking through how to update that system.

[3:01] 3 minutes, 1 second And and YC is very similar. And I'd like to connect the dots between lecture one where we talked about the compute

[3:08] 3 minutes, 8 seconds bottleneck, right? And if you remember, one of the reasons I I talked about how bottleneck is uh compute is a bottleneck today is because we're in the

[3:16] 3 minutes, 16 seconds pre-standardization of compute era. And if you zoom back to the industrial revolution, one of the things that allowed this very important

[3:24] 3 minutes, 24 seconds thing called electricity to become a stable sort of resource uh a piece of infrastructure that lots of people could

[3:31] 3 minutes, 31 seconds develop on and access was the development of standards, right? One of them was ACDC and then we had institutions enforce those standards.

[3:41] 3 minutes, 41 seconds Um, one of those institutions was would utility companies that developed a grid to coordinate the production, demand and

[3:48] 3 minutes, 48 seconds supply of electricity in the capital world. Um, when I was uh getting showing up when I showed up in

[3:56] 3 minutes, 56 seconds Silicon Valley 20 in 2011, we were in the pre-standardization of capital of venture capital. It was a complete mess.

[4:03] 4 minutes, 3 seconds You know, there were a bunch of VC firms who were all trying to do their own deals and figure out how to negotiate with founders and so on. And into that

[4:10] 4 minutes, 10 seconds mess stepped um Paul Graham and Jessica Livingston and introduced a new standard for how capital should be allocated. And

[4:19] 4 minutes, 19 seconds that was called the safe. How many people have heard of the safe? There we go. Okay. So, this is living proof. The at the time it wasn't legible to me how

[4:27] 4 minutes, 27 seconds profound the safe was. It was basically a two-page legal document that YC put up online and said, "Here's how we're going

[4:34] 4 minutes, 34 seconds to fund startups. It's called a safe simple agreement for future equity." And at the time I was like I was a founder uh sorry stu student here and I saw it I

[4:42] 4 minutes, 42 seconds was like okay whatever legal document in hindsight now it's so obvious to many of us in the ecosystem that that was a pivotal moment in the history of Silicon

[4:50] 4 minutes, 50 seconds Valley where you know the YC team saw what was going on and realized at that

[4:57] 4 minutes, 57 seconds point there was another um we we were living through the rise of the cloud and SAS era right AWS and GCP and so on had

[5:04] 5 minutes, 4 seconds started to make compute uh quite accessible And that had reduced the marginal cost of innovation in the valley. But but

[5:12] 5 minutes, 12 seconds venture capital was still hadn't caught up with that era. You know, it didn't cost much to produce software. And so there was a sort of moment of abundance we knew we were going to go through back

[5:21] 5 minutes, 21 seconds then. But to get capital out to innovators like you guys, there was so much there was a there was sort of a

[5:28] 5 minutes, 28 seconds venture capital bottleneck at that time, which now seems cute given the numbers we're living through today. But at that time, it really did feel like it was hard to get time with VCs and get good

[5:38] 5 minutes, 38 seconds deals and so on. And so when into that mess stepped YC and published the safe, it became a standard for how early stage

[5:46] 5 minutes, 46 seconds startups um you know were going to be funded. And then by enforcing it, YC became an institution that standardized

[5:52] 5 minutes, 52 seconds seedstage funding. Um, and and I think you know the the arc of Silicon Valley would have looked very different without

[5:59] 5 minutes, 59 seconds that one document. Okay. And so as you as we it's very obvious to me as at AMP

[6:07] 6 minutes, 7 seconds we you know we live through this every day on the compute side. We might even at some point open source a standard agreement for future compute um

[6:14] 6 minutes, 14 seconds something like that. But you know, we look to what YC has done as a somewhat of a spiritual uh ancestor for the work

[6:22] 6 minutes, 22 seconds we're doing. And so it's very cool to have you guys back within that context.

[6:26] 6 minutes, 26 seconds I hope you know this this gives you a little bit of you know connect the dots moment for why lecture one and and this lecture are parallels and systems design

[6:34] 6 minutes, 34 seconds is not just something you do in engineering. You you can do it in any uh domain you're in to try and accelerate the pace of progress and unblock

[6:42] 6 minutes, 42 seconds bottlenecks. Is this making sense to people? Can I get a yes?

[6:48] 6 minutes, 48 seconds Come on. It's spring quarter, guys. Can I get a yes?

[6:51] 6 minutes, 51 seconds Yes. Okay. Thank you. All right. With that, over to you guys. Thank you so much for coming. Why don't we start with, you know, introductions about yourself, how you got here, and then you can dive in.

[7:00] Absolutely. Hey. Hey, everyone. I'm Gary Tan. Uh, I was uh Stanford class of 03.

[7:05] 7 minutes, 5 seconds I took a lot of classes in here. I fell asleep in this lecture hall a great many times. Thank you so much for bringing me back. This is it's great to be back to

[7:13] 7 minutes, 13 seconds the farm and uh any every time I come back to the farm I'm like you know uh sort of shocked that I get to be up here

[7:20] 7 minutes, 20 seconds uh because like I feel like I just blinked and I was in your seat and uh you know zooming out that's actually desperately what I want for every single

[7:27] 7 minutes, 27 seconds one of you is like how do we like you you know what we're talking about here is there's a grand shift like all those historical things like literally the new

[7:36] 7 minutes, 36 seconds standards are being established right now and there are people in this room who are actually going to be the people who establish those things and then

[7:43] 7 minutes, 43 seconds Diana and I and the team at YC were hoping that we're uh you know the safe was a legal instrument uh what we're going to talk about today is actually

[7:51] 7 minutes, 51 seconds code and not just code markdown is code like literally the new and you know we're going to link it all the way over

[8:00] to uh what a startup is what people in this room are going to be spending your entire lives uh building the railroad

[8:07] 8 minutes, 7 seconds for the rest of society over like you know for our our generation uh we were building the internet and we were building mobile phones and we're

[8:15] 8 minutes, 15 seconds building social networks and your generation is going to create the cognitive layer for all of society and this I mean

[8:24] 8 minutes, 24 seconds what we're talking about is just like stuff that we're like these are our hunches even like you guys are going to go and actually build it and so you know

[8:32] 8 minutes, 32 seconds thank you for bringing us back I mean Diana do you want to introduce yourself uh thank you for having us I'm Diana I'm one of the general partners at YC and we

[8:42] 8 minutes, 42 seconds are living through an exciting time as you all know with what all the capabilities with AI is unlocking and we

[8:50] 8 minutes, 50 seconds have a lot of interesting things to share for all of you in this lecture.

[8:54] 8 minutes, 54 seconds We've seen unprecedented growth from a lot of the companies in our portfolio that gone from zero to tens of millions

[9:01] 9 minutes, 1 second and dollars in revenue in one year, which is impossible before. Within a year, it would have taken four or five years to get to basically series B level

[9:10] 9 minutes, 10 seconds traction and like hundreds of millions of dollars in capital. I mean, it's just a different moment right now, different world. And we're going to tell you how these founders have done it. and

[9:19] 9 minutes, 19 seconds we're going to go through really what it means to build a company now to be AI native.

[9:24] 9 minutes, 24 seconds So with that, um I mean it's a pretty packed lecture. So we're going to just get right in. I mean AI is going to change the unit of production. Like you

[9:32] 9 minutes, 32 seconds know when I was sitting in your seat uh I knew that I needed to raise money. I needed to hire a lot of people. This was about me learning how to like you know

[9:40] 9 minutes, 40 seconds uh create a new cult like you know Palunteer was like that. Um YC you know ultimately it's a religion right? like this something that we believe that

[9:48] 9 minutes, 48 seconds nobody else believes yet, right? Um that is still true. Um all the things we're going to talk about like a team is still valuable, human beings are still

[9:56] 9 minutes, 56 seconds valuable, but it's not going to be just humans. It's going to be humans in concert with agents with memory and evalu. So by the by by the end of this

[10:05] 10 minutes, 5 seconds talk, you're going to understand what we're talking about right now. It sounds like a bunch of buzzwords. We don't want this to be a bunch of buzzwords. We want you to take these ideas and actually

[10:13] 10 minutes, 13 seconds implement them and remake society. and we think you will do that. Um, let's see. Yeah, in 2010 like uh I mean I'll

[10:22] 10 minutes, 22 seconds tell you my personal story. Uh, in 2008 I got into YC. We raised about $4 million. I hired you know 10 people. We created Posterous which is a dead simple

[10:30] 10 minutes, 30 seconds blog platform. And uh, you know, we sold that to Twitter uh, three years later for $20 million. And uh honestly like I

[10:39] 10 minutes, 39 seconds was able to create like everything all the software we made over two years with 10 people and all that capital but me with a $200 a month uh cloud code max

[10:49] 10 minutes, 49 seconds plan and anyone in this room could do that and it it didn't take like two years it took about uh 5 days right so I

[10:56] 10 minutes, 56 seconds experienced that speed up recently um you know I created Gary's List and then it uh that caused me to create Gstack.

[11:02] 11 minutes, 2 seconds We're going to talk about what those things are, but you know, as Diana said, like we're in 2026 now. And so a sixperson team can hit 10 million in

[11:11] 11 minutes, 11 seconds revenue uh with just just the things that we're talking about today. And a lot of you already know this, so it might be review, but for some of you, this is like some astonishing good news.

[11:21] 11 minutes, 21 seconds Um you know, so let's talk about GStack.

[11:24] 11 minutes, 24 seconds This is something that uh I discovered, you know, la late last year, I saw Steve Yaggi, a famous blogger and engineer. uh

[11:31] 11 minutes, 31 seconds I believe he was an early Googler. He wrote that you know people using AI coding agents are 10x to 100x more productive as engineers using cursor and

[11:40] 11 minutes, 40 seconds chat today. And then at anthropic they're about a thousandx as productive as googers were in 2005. And I was like

[11:48] 11 minutes, 48 seconds what is going on? And so I had to try it. I opened cloud code and of course I ended up writing uh I'm around like a

[11:55] 11 minutes, 55 seconds million lines of code in um which is really really crazy. um everything.

[12:00] Let's see. You know, let's just talk about the things that you might read on the internet. These are all wrong. Um it's not just AI slop actually. You

[12:09] 12 minutes, 9 seconds know, yes, LLMs are very verbose and some of it is boilerplate, but like uh when you create your own software factory, this is actually what you're

[12:18] 12 minutes, 18 seconds fighting. This is actually what you're preventing from happening by default. Um yes, there are hallucinations. Yes, those are actually the things that we're

[12:25] 12 minutes, 25 seconds trying to control. uh you know can you make demo code very quickly? Yes. But like how do you get it to production?

[12:32] 12 minutes, 32 seconds Well, you actually have to get to 100% or 80 to 90% test coverage. That's actually one of the main reasons why uh

[12:40] 12 minutes, 40 seconds plan-ge review as a skill exists. Like that's the one that that's the number one with a bullet skill that I use about 20 times

[12:47] 12 minutes, 47 seconds a day to get to 80 90% test coverage so that I am not shipping slop. I'm something I'm shipping something that is actually literally usable and that I

[12:56] 12 minutes, 56 seconds rely on every day in production. Um, this is very controversial. I've gotten in trouble over this. I apologize to people for, you know, who who like, you

[13:04] 13 minutes, 4 seconds know, took my trolling as serious. Like, you know, is Lok gameable and uh something that might be, you know, not

[13:11] 13 minutes, 11 seconds usable. Like actually, yes. Like LO on its own can be wrong. But on the other hand, like if you have tests, if you

[13:18] 13 minutes, 18 seconds know the real measure of whether or not these things work is actually look down and does it work for you, does it work for your customers? Are people actually paying? That's actually the true metric.

[13:28] 13 minutes, 28 seconds Uh, you know, look might be a garbage metric, but I might argue that in the age of there's nothing in cloud code or the model or the harness or any or

[13:36] 13 minutes, 36 seconds GStack or any of these things that tell the model to write as many lines as code as possible. Like if anything, the reverse is probably true. like we're

[13:44] 13 minutes, 44 seconds trying to write as dense and concise code as possible to serve the purpose and you know I think that that's something that's quite important to talk

[13:52] 13 minutes, 52 seconds about. Um this is my experience like I got to 87,000 stars. Um my other project GBrain is 13,000 stars. So I mean

[14:00] basically for someone who was not coding at all in December of last year I have more than 100,000 GitHub stars and about 15,000 people use it every single day.

[14:11] 14 minutes, 11 seconds um you it's hundreds of thousands of skill invocations and so I don't know this is sort of what I'm learning um you

[14:18] 14 minutes, 18 seconds know last year uh probably before Claude uh 4.5 Opus 4.5 came out we were talking about co-pilots uh today I think we're

[14:27] 14 minutes, 27 seconds really talking about a software factory and so if you use GStack you'll understand this is actually what's happening um what I discovered is that

[14:36] 14 minutes, 36 seconds um and this is mo more or less by accident as I was writing half a million lines of code or uh recreating my startup that I created like two other

[14:44] 14 minutes, 44 seconds times previously but doing it in about 5 days or you know during the course of like several months creating GStack I

[14:52] 14 minutes, 52 seconds realized that it's actually really useful to pull out specific uh personas of what is already in the

[15:01] 15 minutes, 1 second latent space and so um the most famous skill that a lot of people use that I you know it's actually interestingly a

[15:08] 15 minutes, 8 seconds distillation of what we already do at Y Combinator when YC we have 15 partners 16 partners at YC when you have an idea

[15:16] 15 minutes, 16 seconds and you're doing office hours with us we're mainly asking questions about what's the problem who's the customer how do you know that and then what are

[15:24] 15 minutes, 24 seconds we building right and so that's what the office hours skill is we basically took uh actually three four months of like transcripts across like thousands of

[15:33] 15 minutes, 33 seconds conversations distilled that into something very very potent and then I had to distill that down by 90% % and then that's what is shipped in open source in SLOF office hours in GStack.

[15:44] 15 minutes, 44 seconds Um but you know as I went like uh it turns out there are lots of different things that I like to use um to actually

[15:52] 15 minutes, 52 seconds make it easier and you know far better to the product that you can create uh with coding agents can be better if

[16:00] you're literally pulling out the latent space for a particular vibe and like thing that you're trying to go for. So plan CEO review for instance my favorite

[16:08] 16 minutes, 8 seconds thing about that is uh it asks the question okay well it has context it knows what you're trying to build uh what is the 10x version of that what is

[16:16] 16 minutes, 16 seconds the platonic ideal of that and so you know when I was a product manager at uh both Palunteer and Microsoft and like a founder for my startups like that was

[16:24] 16 minutes, 24 seconds what that when I thought about product that's what I wanted to do I wanted to figure out like what is the perfect manifestation of the thing that we could

[16:32] 16 minutes, 32 seconds build and then when I build a um what what I'm building right now needs to be on a road map that is a straight line

[16:39] 16 minutes, 39 seconds from where we want to go from where we are now. And then the other thing that I discovered as we were doing this stuff is that you can boil the ocean. You know

[16:47] 16 minutes, 47 seconds who here remembers that term boil the ocean. Like if you go and work someplace, you're going to go into a meeting where people start saying things

[16:56] 16 minutes, 56 seconds that are a little too scary and then immediately people in that room are going to say, "Whoa, whoa, whoa. Let's not boil the ocean." And my response to

[17:03] 17 minutes, 3 seconds that based on my experience with uh coding agents and what's happening right now is actually let's boil the ocean.

[17:09] 17 minutes, 9 seconds You know the the things that you can do like uh basically you sitting in front of one of these terminals can you can do the work of about 500 to a thousand

[17:18] 17 minutes, 18 seconds people. And if that's true, then like all of the expectations that we currently have in society around what a

[17:25] 17 minutes, 25 seconds founder can do, what a company can do, what a small team can do, what you can do sitting in front of a computer, they're actually a thousandx wrong,

[17:33] 17 minutes, 33 seconds right? And actually what's funny is that's baked into the model weights.

[17:36] 17 minutes, 36 seconds Like who here has asked claude code before like how long is this going to take? And it'll give you, oh, it's going to take about three weeks to code all of

[17:45] 17 minutes, 45 seconds this stuff. and then you press approve on the plan and then literally it's done in about an hour. So I mean all of us have experienced that like the models

[17:54] 17 minutes, 54 seconds themselves have not caught up to this new reality that we can actually boil the ocean. So anyway use GStack like there's a lot of stuff in there. Uh we

[18:02] 18 minutes, 2 seconds have very little time so I feel like I need to skip ahead like you know GStack was basically my understanding of building open source and putting it out

[18:10] 18 minutes, 10 seconds there and I'm still working on it. Um, but the new thing that I've been working that like everyone at YC has been uh, you know, just completely immersed in is

[18:19] 18 minutes, 19 seconds OpenClaw and Hermes agent. And they're actually teaching us brand new primitives on how to think about code,

[18:26] 18 minutes, 26 seconds how to think about markdown, and how those things work together to do real work. Um, and so this is like somewhat

[18:36] 18 minutes, 36 seconds obvious, but I have to say it because I keep like anytime I would build an agentic system and it broke, it would

[18:44] 18 minutes, 44 seconds every single time break because something was wrong about what I was trying to do. like I was either trying

[18:52] 18 minutes, 52 seconds to do deterministic work like things that should be in code in my markdown skill or I was trying to do uh latent

[19:01] 19 minutes, 1 second stuff like actually that things that like my agent should be doing using the LLM in the code. Uh and like a concrete

[19:09] 19 minutes, 9 seconds example for instance is you know uh we spend a lot of time trying to curate the experience of people at YC events. I

[19:16] 19 minutes, 16 seconds have um you know anyone actually you can just use uh claude you don't even need cloud code you could use chat GPT put in

[19:24] 19 minutes, 24 seconds uh you know bios of like eight people coming to your dinner party and you can have it go and you know Google that person run a dossier and then like figure out who should sit next to who.

[19:34] 19 minutes, 34 seconds That's very easy to do in latent space.

[19:37] 19 minutes, 37 seconds But try to do that with an 800 person dinner party or with uh the 6,000 people that are coming to startup school. you

[19:45] 19 minutes, 45 seconds can't do it. Like the model's not big enough. Like it it hallucinates. It doesn't work. And so what do you do?

[19:51] 19 minutes, 51 seconds Well, that's the perfect example of like we you know you need to make the latent space work with the deterministic space.

[19:58] 19 minutes, 58 seconds Um and so you know what how do you actually do that? Um here's a toy. The toy example here is like well what is a

[20:06] 20 minutes, 6 seconds skill? Who here has like played with a skill or used a skill file? So skill file is actually I mean it sounds fasil.

[20:13] 20 minutes, 13 seconds I mean, if you go on Twitter and believe like the haters, they're going to say like, "Haha, it's just a bunch of markdown files. Who cares, right?" But

[20:20] 20 minutes, 20 seconds the big difference now with LLMs is like l like you can actually do real work with this stuff. Um, you know, the thing

[20:28] 20 minutes, 28 seconds that keeps coming back over and over again is that you can do real investigations about it. And so, you

[20:35] 20 minutes, 35 seconds know, basically what is a skill? It's basically just a runbook. Like you know even you know if if you've ever thrown

[20:42] 20 minutes, 42 seconds an event and you need to throw that event over and over again what do you do? you go into your notebook and you just write down well one we need to do

[20:49] 20 minutes, 49 seconds this secure a venue two like let's figure out who should come like it's just this any human being or agent should be able to look at it and say

[20:57] 20 minutes, 57 seconds okay like after I read like 1 2 3 4 5 6 like however many steps it is maybe it's branching it could be very complicated

[21:04] 21 minutes, 4 seconds actually um you know do I know how to do that thing right you know this is a very simple concept but the really cool thing

[21:11] 21 minutes, 11 seconds is that you can actually make it call code and that's what I find myself doing inside of OpenClaw and Hermes all the

[21:20] 21 minutes, 20 seconds time and this this is where it links to what you guys are doing as founders and this is the pattern that we're seeing inside every YC founder or inside every

[21:28] 21 minutes, 28 seconds YC startup now like we're not picking up the phone and doing it ourselves just like we're not opening VS code and writing code ourselves like every like

[21:37] 21 minutes, 37 seconds claude code revolutionized how we write code and we don't open like I you know me karpathy and tons of other people in this room probably don't open the editor

[21:46] 21 minutes, 46 seconds at all. Right? Um the same thing is happening with OpenClaw and Hermes agent. So all non-technical or

[21:53] 21 minutes, 53 seconds processoriented things in knowledge work are now you can do it in openclaw like you can have twilio call someone. You

[22:02] 22 minutes, 2 seconds can use Gemini live to actually like book a thing or like buy a thing or here's my credit card like all of these things you know like that. Do who here

[22:09] 22 minutes, 9 seconds remembers that Google demo where like they stood up on one of their conferences and they're like so proud like you know Gemini can now call and

[22:17] 22 minutes, 17 seconds like get you an appointment and then they never shipped that thing. You don't need to wait for them to ship that anymore because you can have that yourself and that's like the most

[22:23] 22 minutes, 23 seconds empowering thing. So code is code. I mean the concrete example I have is like who here uses open claw and uh it always

[22:31] 22 minutes, 31 seconds for some reason thinks that you're in Greenwich uh in the UK like it's always and so this is a perfect example of like

[22:39] 22 minutes, 39 seconds uh I had to write code in Typescript it's context-now.mmjs and I have tests for it and then I have

[22:47] 22 minutes, 47 seconds it built into my system so that I don't rely on the latent space to do it. It just tells me here's the time and then

[22:54] 22 minutes, 54 seconds actually here's the things that are coming up. And if I don't do that, like left to its own devices, the latent space will be like, "Oh yeah, it's 3:00

[23:02] 23 minutes, 2 seconds a.m. like why are you still up?" And it's like, "What are you talking about?

[23:05] 23 minutes, 5 seconds It's the afternoon right now." Um, the next important thing that we discovered, like anyone who has used Claude code a lot has probably seen this

[23:13] 23 minutes, 13 seconds uh error message at the top of Claude saying your claw.md is 40,000 tokens or 40,000 lines or something like that. Um,

[23:21] 23 minutes, 21 seconds and then you Google around, you're like, "Okay, well, how do I fix that?" Well, how you fix it is actually a resolver.

[23:27] 23 minutes, 27 seconds So, resolver is actually really important because, uh, it's amazing how much you have to spend time getting this

[23:33] 23 minutes, 33 seconds right. Um, you claude is a whole bunch of in cloud. MD is a whole bunch of instructions of on how to do things that

[23:41] 23 minutes, 41 seconds you developed like you got mad that claude code did this or that or wrote the change log in a certain way. You say, "Hey, I don't want it like that.

[23:47] 23 minutes, 47 seconds Don't do it like that anymore." Well, turning it into a proper resolver means that you take that instruction and it's like anytime you have to write to the

[23:55] 23 minutes, 55 seconds change log, load changeel log.mmd and so suddenly you don't need that in your context. Uh like the agent itself knows,

[24:03] 24 minutes, 3 seconds oh okay, here's this master directory of all the things I know how to do and I need to I need to load the instruction

[24:11] 24 minutes, 11 seconds only when I actually need it. Uh it sounds so simple but it's kind of obvious but like this is actually the core of having a really great agent

[24:19] 24 minutes, 19 seconds actually. It's having a resolver. When I when I need to check signatures, I want it to actually go to my executive assistance skill. Um, who is a

[24:28] 24 minutes, 28 seconds particular person like well I needed to look up in my brain repo how to do that and I have a skill a specific code path and it's not a code path. It's like a

[24:36] 24 minutes, 36 seconds markdown code path, right? It's a I call it a skill pack. Um I have a skill pack specifically for that thing. I did it

[24:43] 24 minutes, 43 seconds once and then that's where um here's another primitive that I discovered that I I find myself doing about 20 times a

[24:50] 24 minutes, 50 seconds day when I'm using open claw or Hermes agent. Uh it's called skillify. So it's you know you're sort of going up one

[24:57] 24 minutes, 57 seconds level in abstraction. So let's use one of these examples. Um you know save this article. Well I do that once I'm you

[25:05] 25 minutes, 5 seconds know I look at the input I look at the output. I get the agent to do exactly what I want. And then once I have it in a position where I like it, I actually

[25:13] 25 minutes, 13 seconds tell it skillify. And then on the right, that's actually what the skill says. And in, you know, this is a summarized version of it. I have a article on X

[25:22] 25 minutes, 22 seconds about it if you want to see like all the full details. But long story short, you write the skill, you write the code, and then here's the part that is actually

[25:30] 25 minutes, 30 seconds broken in Hermes agent. I think they're about to fix this actually, but um it's not enough to do it once. You actually

[25:38] 25 minutes, 38 seconds need to test it. Um you have to it's like kind of like uh if you work in a finance organization like think about all the people like 10 or 20% of people

[25:46] 25 minutes, 46 seconds who work in some of these organizations just do compliance and you're like what are all these people doing actually like in an agentic system this is exactly the

[25:54] 25 minutes, 54 seconds illustration of that like look at all these steps writing the skill and writing the code is only two out of the 10 steps all of the rest of it is making

[26:01] 26 minutes, 1 second sure that this messy system that is kind of more like a human system than perfect beautiful beam of light code can still work and do work that you want, right?

[26:12] 26 minutes, 12 seconds Okay. So, you want you did it some you did something in cloud code, you or sorry, you did something in open cloud, you made it work, then you say skillify.

[26:19] 26 minutes, 19 seconds What does it actually do? Well, you have to write unit tests for the actual code.

[26:22] 26 minutes, 22 seconds You have to write LLM evals for the skill file. Then you have to write an integration test. Then you have to make sure that there's a resolver trigger in

[26:30] 26 minutes, 30 seconds agents.mmd. And then you have to test that. you need an LLM as judge eval to make sure that when that thing comes up,

[26:38] 26 minutes, 38 seconds it's broad enough that it actually gets triggered. And then uh there's this other concept that you can look up in Gbrain called check resolvable that is

[26:45] 26 minutes, 45 seconds very important. You want it to be dry, don't repeat yourself, otherwise you end up with like a thousand skills that do all the same thing. Um you need an end

[26:53] 26 minutes, 53 seconds toend smoke test and then you know ultimately you need a schema. You need to figure out where does this live in my memory and my repo. Um, so we're going

[27:00] really fast, but you know, that's why memory is actually really important. And so my next project uh that is out now that I'm working on is called Gbrain.

[27:09] 27 minutes, 9 seconds It's actually a three layer memory system built on top of what Karpathy already talked about with his knowledge wiki. So I started with a knowledge wiki

[27:16] 27 minutes, 16 seconds as well and then it started falling over because it just uses GP. Um, and so I had to add uh, you know, vector search

[27:24] 27 minutes, 24 seconds um, you know, RRF fusion backlinks. I added a graph database. It's a type knowledge graph. I'm about to add uh an

[27:32] 27 minutes, 32 seconds ep epistemology um system so that we know that things are take they're like hunches or um

[27:39] 27 minutes, 39 seconds beliefs by specific people or world knowledge and I want to track when things sort of you know what's funny about maybe this is very specific to me

[27:47] 27 minutes, 47 seconds like I'm super fascinated with the idea that people in this room are going to go on to like your your journey as a

[27:54] 27 minutes, 54 seconds founder literally is that you have a hunch you think that like the world needs X Nobody believes that yet. But, you know, I want my knowledge system to

[28:03] 28 minutes, 3 seconds be able to track like, oh, well, I heard so and so, this person in this room, this person in red shirt right here, he tweeted this and nobody else believed

[28:10] 28 minutes, 10 seconds that yet, right? But he's going to go and spend like a year, two years, 5 years proving it correct. And then if my Gbrain is actually working properly,

[28:19] 28 minutes, 19 seconds it's going to spot that. It's going to be like, oh, actually, like here's at Stanford, there was this one person who believed X and then they manifested it.

[28:27] 28 minutes, 27 seconds And so, I don't know. I for me like philosophically I'm I'm fascinated by knowledge systems like truly capturing what's going on and that's sort of what

[28:35] 28 minutes, 35 seconds we you know I think about this like I'm just building software for myself like this is the stuff that we have to think about and um I don't know I if you spot

[28:43] 28 minutes, 43 seconds in my in my um voice like I'm excited about this because I'm building again and I'm building for myself and then

[28:51] 28 minutes, 51 seconds we're open sourcing the stuff because we want all of you to actually be able to do it. Um, I feel like I need to expand on like, you know, one of the things

[28:59] 28 minutes, 59 seconds that GBrain does is like it's a very specific schema for my use case, but you know, one of the last things I need to do before I go to V1, hopefully in the

[29:08] 29 minutes, 8 seconds next couple weeks, is I actually need to make uh fully dynamic ontology, which is a great buzzword from that I've learned

[29:16] 29 minutes, 16 seconds from Palunteer back in the day. I mean that's what you know right now it's built it's the schema is built for me but there's no reason why it can't be built for you whether you're a

[29:24] 29 minutes, 24 seconds researcher whether you're a journalist whether you're a politician like each person's going to have a different schema we need to support all of those things so zooming out I'm about to pass

[29:32] 29 minutes, 32 seconds it over to Diana to take it all the way home like I sort of gave you the primitives that we're learning literally like week by week like I didn't even

[29:40] 29 minutes, 40 seconds know about sk uh skillify until it flew out of my hands at like 3:00 a.m. using open claw and then I put it on X and

[29:48] 29 minutes, 48 seconds that went viral and I mean I'm just learning as I go. I'm not an expert. You know, some sometimes it's like uh my favorite line from Alan Watts who if you

[29:57] 29 minutes, 57 seconds guys know Alan Watts is uh he walks he goes to a room like this. He get he used to give lectures and he would say I am not a guru. I am just an entertainer. So

[30:06] 30 minutes, 6 seconds uh you know that's uh I want to pass this over. I mean we're talking about the Agentic company.

[30:13] 30 minutes, 13 seconds Diana's going to tell you a lot more about it. like the the concepts that I just talked about like one of the weirder things we realized is these

[30:20] 30 minutes, 20 seconds actually map to the company. So a skill is you know sort of a squishy human being who's an employee who has a

[30:27] 30 minutes, 27 seconds capability. A resolver is the org chart like who handles what like how does it happen like it's you know the filing

[30:34] 30 minutes, 34 seconds rules where it goes in the brain is the internal process where's the information live check resolvable is this thing that makes sure that the resolver works for

[30:43] 30 minutes, 43 seconds like the set of things that you want to get done and that's like audit and compliance like I you know when I was sitting in your seat I had no idea why

[30:50] 30 minutes, 50 seconds so many people in so many human organizations had to spend so much time on audit and compliance but now at age 45 building a lot agentic systems and

[30:59] 30 minutes, 59 seconds looking at skillify and how much time I spend just trying to make the things like faking work you know uh I actually

[31:06] 31 minutes, 6 seconds understand now like human systems are very messy and that's what check resolvable is and in the end like you know the funniest thing is what a trigger eval is like you would think

[31:14] 31 minutes, 14 seconds like oh well of course it's in the trigger it's in the resol you know in in agents it should just work right but no you even have to check that like that

[31:21] 31 minutes, 21 seconds itself is its own latent space squishy operation that you have to check and that's you know in an org those are

[31:28] 31 minutes, 28 seconds performance reviews. So um with that I want to hand this over to Diana to take us to the actual applied portion that will actually help you.

[31:39] 31 minutes, 39 seconds So I think uh couple of things that Gary went over are a lot of the details on how you could implement it with a lot of

[31:47] 31 minutes, 47 seconds the building blocks and if we really backtrack and step now a couple layers up. One of the key concepts of building

[31:55] 31 minutes, 55 seconds a AI native company is you need to change fundamentally how companies are run. I think normally today preAI

[32:02] 32 minutes, 2 seconds companies are basically run as a open loop. People make decisions and a lot of those um decisions take a while to come

[32:12] 32 minutes, 12 seconds back and is basically lossy. There's no concrete tight feedback loop. If a lot of you have studied control systems, how many of you have taken control systems

[32:20] 32 minutes, 20 seconds and know the difference between open loops and closed loops. uh the problem with openloop systems is as error accumulates the systems become more

[32:29] 32 minutes, 29 seconds erroneous and then it goes off the rails as opposed to let's say closed loop zipsson very famous closed loop systems

[32:36] 32 minutes, 36 seconds could be like P controllers you have a tight feedback loop into the controller so that a lot of the error stays within

[32:44] 32 minutes, 44 seconds check and this is how a lot of uh robotic systems work a lot better so we're basically now with AI have the capability to take a lot of these lossy

[32:53] 32 minutes, 53 seconds information of how companies run into becoming a closed loop system. So what that means fundamentally today for old

[33:02] 33 minutes, 2 seconds school companies information lives in people's in people's head in an or they have a lot of side conversations DMs and

[33:11] 33 minutes, 11 seconds slack they have a lot of meeting notes that are not written they have just vibes how they feel about a particular

[33:17] 33 minutes, 17 seconds decision and all very lossy this is basically how decision in companies are made and now the ability is to change

[33:26] 33 minutes, 26 seconds all of that into a closed loop system where you tie these agents that Gary described and how to implement it into

[33:33] 33 minutes, 33 seconds basically the fabric of how you make decisions for a company. So the idea is that you would have a agent like a Hermes or Open Claw embedded into all

[33:42] 33 minutes, 42 seconds the decision making and what it means the agent needs to have read access to every single artifact that the company produces. So for some of you that might

[33:50] 33 minutes, 50 seconds be working on some projects in school, you could have a small version of this.

[33:54] 33 minutes, 54 seconds You could have an agent that basically connects to your GitHub codebase, connects to your Discord, and even start recording all the meetings you have with

[34:02] 34 minutes, 2 seconds your teammates as you make progress. And as you get all this context, the agent can then suggest what are the best next

[34:12] 34 minutes, 12 seconds items to work on or bug fixes and put it in your D brain.

[34:16] 34 minutes, 16 seconds Put it in your D brain and the memory context. And this is how you start embedding this agentic system that starts building the system and self-healing. So that's one of the

[34:24] 34 minutes, 24 seconds things that we're seeing companies do where they can pull this crazy stats of one employee making in the revenue per

[34:32] 34 minutes, 32 seconds company at at least like one or$2 million which now the public comps is I don't know take like a like a salesforce maybe the employee comps of how much

[34:41] 34 minutes, 41 seconds revenue they bring in is under six figures. So this is this is huge is at least a 10x based on what we're seeing on the startups.

[34:48] 34 minutes, 48 seconds And what does this look specifically is when agents are able to read the full state. In practice, we actually implemented this also at YC with our

[34:57] 34 minutes, 57 seconds engineering team. We're basically able to cut the sprint time in half and produce 10x the amount of work. And some

[35:04] 35 minutes, 4 seconds of you may have read this uh blog post from Jack Dorsey about the agent organization. How many of you have read that post?

[35:12] 35 minutes, 12 seconds Some of you are familiar with this concept. And I think it talks a lot about now making an organization very

[35:18] 35 minutes, 18 seconds flat and basically getting less need for middle management because middle management used to be just all about this lossy information routing.

[35:28] 35 minutes, 28 seconds You end up basically having three roles in a company. One is uh everyone starts building. So everyone becomes effectively an individual contributor

[35:37] 35 minutes, 37 seconds that ships something and even people that are nontechnical you now have the power to build with all these tools. So even a salesperson could be building

[35:46] 35 minutes, 46 seconds their whole pipeline of uh calls and meetings and automate all of that. And then the other person is the DRRi who

[35:54] 35 minutes, 54 seconds tends to be some of you are familiar with this term from Apple. How many of you know DRRi? The concept of a direct responsible individual that every

[36:01] 36 minutes, 1 second outcome in a company trace down to a particular owner that owns the outcome.

[36:07] 36 minutes, 7 seconds And the way it works is that the DRRI orchestrates with the IC to make sure something gets done. For example, a goal for a company might be we need to

[36:14] 36 minutes, 14 seconds increase the revenue by 3x the end of the week. They're responsible to orchestrate all the things that need to happen to get there. They work with the

[36:23] 36 minutes, 23 seconds sales team to get all the calls booked with the engineering team to ship all of these and that tends to be oftent time the founder. Now the new role that comes

[36:30] 36 minutes, 30 seconds into this AI native uh organization is sort of a we call it AI founder. I mean

[36:36] 36 minutes, 36 seconds this is kind of the if if you hear Gary he be really much embodies this is you're living at the edge of the future

[36:43] 36 minutes, 43 seconds with all the tools in order to get your company to run fast you've got to be trying all the tools everything is changing and moving so quickly I mean

[36:51] 36 minutes, 51 seconds literally we had this big revolution with agentic coding that just happened end of last year with uh claw 4.5 when

[36:59] 36 minutes, 59 seconds it came out that's when things started to work but if you were not building if you were not at the edge you would not be able to bring all those innovations

[37:06] 37 minutes, 6 seconds into your company. So that's one of the things that we're seeing the best founders at YC do.

[37:12] 37 minutes, 12 seconds Yeah, there are people who are still uh operating like co-pilot level from last year and it's like not going to make it, bro.

[37:18] 37 minutes, 18 seconds They're not going to make it. Now the other thing that gets talked a lot about is in order to build all these agentic

[37:26] 37 minutes, 26 seconds systems to avoid quote unquote the AI slop is you what cannot be delegated is really this

[37:33] 37 minutes, 33 seconds concept of a taste. How many of you have been hearing a lot in the taste is what's going to be durable. I think that

[37:40] 37 minutes, 40 seconds and a lot of you agree with this right coding let's just call it shipping code is going to zero the cost of it but what

[37:48] 37 minutes, 48 seconds is not going to zero is the taste to build something good the taste to discern was good or bad and as part of that that really manifests in terms of

[37:57] 37 minutes, 57 seconds evals into the systems for how you build all these agents and what that means is that generic benchmarks won't make it

[38:06] 38 minutes, 6 seconds whether your product works I know sometimes people are trying to just It's um generic public benchmark MLU doesn't

[38:13] 38 minutes, 13 seconds tell you whether your product or or agents are really working or upsetting the user.

[38:19] 38 minutes, 19 seconds A lot of uh the product that a lot of you if some of you want to hopefully start companies raise your hand maybe. Yeah. All right.

[38:27] 38 minutes, 27 seconds Great. So part of it the actual judge ultimately of whether something is good is whether users really want it. And

[38:35] 38 minutes, 35 seconds with that is going to be different in every single domain. There's no way to automate that. And how can you tell? I

[38:42] 38 minutes, 42 seconds think the agent, you will have to go into all the details deep. Did it follow the instructions?

[38:48] 38 minutes, 48 seconds Was the answer correct? Did it preserve the customer trust? Was this something that was spewing correctly or incorrectly? Did it actually hit the

[38:57] 38 minutes, 57 seconds business goals? Did it comply with the domain rules? So, a lot of these things that Gary talked about in terms of uh resolvers and skillifying it and

[39:06] 39 minutes, 6 seconds improving the system apply here. But in order to do that, you still need the human in the loop to tell when something

[39:13] 39 minutes, 13 seconds goes wrong and to basically label a particular interaction or pipeline or workflow that is incorrect. And that is

[39:20] 39 minutes, 20 seconds something that is that you're going to have to own and do and painstakingly actually look through all the traces. I

[39:28] 39 minutes, 28 seconds mean, this is how Gary, you go through a lot of the system, too. You read through the traces and click when it's wrong or right and decide to skillify it, right?

[39:37] 39 minutes, 37 seconds Yeah.

[39:38] 39 minutes, 38 seconds Well, what's cool though is like uh once you get like the basics going, my favorite thing that I haven't released yet, but I will release is a crossmodal

[39:46] 39 minutes, 46 seconds evolve. So you I'm about to add to skillify where you can actually have the frontier models of Opus GPT 5.5 and

[39:54] 39 minutes, 54 seconds Deepseek V4 uh all evaluate the inputs and the outputs and then rate it and then feed it back to the original sub

[40:03] 40 minutes, 3 seconds agent saying you know this is the rating and here's what you need to do for the next try and then you actually iterate and so you can metaprompt to get

[40:11] 40 minutes, 11 seconds something that is 10 times better than the first version of what it is. I mean this what's weird is like these abstractions are basically stacking because that's what I learned that from

[40:19] 40 minutes, 19 seconds Gstack. A lot of YC founders said well I I like claude code but that's like my ADHD CEO and then codeex is my uh you

[40:27] 40 minutes, 27 seconds know nearly non-verbal 200 IQ uh CTO and I need both of them to do crossmodal analysis and then it ships with zero

[40:35] 40 minutes, 35 seconds bugs. So these are all things that are like stacking like we're just discovering these things like week to week right now and this is effectively this section on

[40:43] 40 minutes, 43 seconds all the founders here would be the ones building the evals and exactly that as part of uh doing this cross model evaluation you have to start with being

[40:52] 40 minutes, 52 seconds able to capture a lot of the traces and the way you capture the traces is going to be very context dependent on the product you build and uh if you're

[41:00] building a let's say a video application is very different than a speech application, consumer model, B2B SAS,

[41:08] 41 minutes, 8 seconds all very different. And then you need to convert a lot of the failure cases and you have to detect when they fail into actually evals that you use. And then

[41:17] 41 minutes, 17 seconds the step three is to be able to replay this constantly into the system to in order to self-heal and improve the system and improve the prompts

[41:25] 41 minutes, 25 seconds automatically, which is exactly what Gary's describing that he's going to shift. He's doing like a general version, but for each of you, you can build all of these. These are still the same principles.

[41:35] 41 minutes, 35 seconds Can we metapar prompt here for a second?

[41:37] 41 minutes, 37 seconds Like you're sitting here listening to a lecture about this stuff, but the lecture is totally useless if you don't go and open your own Hermes agent and

[41:44] 41 minutes, 44 seconds OpenClaw and like load up your own GBrain and like actually use the like there are 40 skills that you can test

[41:51] 41 minutes, 51 seconds out and try inside Gbrain. And some of it is like make your own like basically have do stuff and then skillify your own

[41:58] 41 minutes, 58 seconds stuff and then release it open source too and see what other people want, you know, like that's we're we're sort of like getting there together. And so the

[42:07] 42 minutes, 7 seconds exhortation is like not only are we metaprompting um the machines themselves, we we need to metaprompt one another to be better

[42:15] 42 minutes, 15 seconds and to be able to fuse with the machines in a new and more profound way every single day.

[42:21] 42 minutes, 21 seconds Now, the last section we're going to go over is that for some of you here in the audience that are excited to start a

[42:28] 42 minutes, 28 seconds company, this is probably one of the best times in history ever to start a company. And this is not an overstatement. You might have heard this from other lectures that came here. Is

[42:37] 42 minutes, 37 seconds that right? The times right now are unprecedented.

[42:42] 42 minutes, 42 seconds And part of it is we're seeing this a lot of the wedge in practice is you pick a painful workflow. You go inside deep

[42:50] 42 minutes, 50 seconds into the customers and you basically become the four deploy engineer. And what that looks like, we've seen it across many industries. And these are

[42:57] 42 minutes, 57 seconds examples of companies that done this crazy growth that I'm telling you that gone zero to eight figures in revenue within a year. For example, Salient is

[43:06] 43 minutes, 6 seconds this company that's doing uh voice agents for loan servicing. They closed some of the top banks in the US. And the

[43:13] 43 minutes, 13 seconds way they did it is they built agents how Gary described it. Other companies, Happy Robot as well that closed the

[43:20] 43 minutes, 20 seconds series B recently last year and 10x the revenue in a year. Same thing. I think they embedded themselves with freight forwarders and built the best agents to

[43:29] 43 minutes, 29 seconds automate a lot of that cruddy work with truckers and coordinating timelines. And then the other one is u reductum. I don't know how many of you might have

[43:37] 43 minutes, 37 seconds heard of this company that's uh doing document processing. The other opportunity is there's just so much tooling that needs to be built for all

[43:45] 43 minutes, 45 seconds these tools. Just the fact of doing better document processing is making all of the other agents better because they

[43:52] 43 minutes, 52 seconds all need to now read documents. But if you increase it, it improves rag and memory and brain to be a lot better. So

[43:59] 43 minutes, 59 seconds Redux is another of these teams that are growing. So what what this means is that a lot of these companies are seeing all

[44:06] 44 minutes, 6 seconds these impressive growth is they're they're just demoing like AI or or some sort of side project. They're actually

[44:14] 44 minutes, 14 seconds deploying full solutions. And part of it if you want to start a company in this fashion you basically go undercover

[44:23] 44 minutes, 23 seconds because some of you a lot of you probably don't have necessarily a background like the founders of salient or happy robot did not come from a finance background or logistics

[44:32] 44 minutes, 32 seconds not in the training set not in the training set but the way they became experts is they actually shadow or took a job and learned the depths of

[44:40] 44 minutes, 40 seconds everything that had to be done with it and then they were able to automate a lot of the repetitive labor

[44:46] 44 minutes, 46 seconds and handle a lot of messy domains into this latent space that Gary described.

[44:52] 44 minutes, 52 seconds And all these workflows before were just done by like phone or email spreadsheets and all very random places where agent

[45:01] 45 minutes, 1 second embedded into all the system could just create a solution that would just work.

[45:07] 45 minutes, 7 seconds And I guess the other thing is we want to show you this this graph that Anthropic posted in terms of the

[45:14] 45 minutes, 14 seconds deployment in different industries. And we're seeing that right now I think a lot of you I don't know if a lot of you

[45:22] 45 minutes, 22 seconds in computer science how many of you are a little bit afraid of the CS jobs after you graduate.

[45:27] 45 minutes, 27 seconds I mean it's a real fear because yeah for this chart taken by anthropic 50% penetration into the usage of these

[45:35] 45 minutes, 35 seconds tools but what is interesting there's this giant white space in all these other domains in terms of like back

[45:43] 45 minutes, 43 seconds office finance data academics cyber security customer service this is like a huge white space there's room for

[45:50] 45 minutes, 50 seconds hundreds and hundreds of AI unicorns that are waiting to be started perhaps by some of you in the room I guarantee it

[45:57] 45 minutes, 57 seconds because some of you may feel it's like all the ideas are done, but what we're seeing is that is not the case.

[46:02] 46 minutes, 2 seconds Yeah, we're at like the first pitch of the first inning on the revolution and you guys are the shock troops.

[46:08] 46 minutes, 8 seconds And one other stat I want to give you from the last batches at YC is that in the past only the best top 1% of the

[46:16] 46 minutes, 16 seconds companies grew 10% week overw week. That was the metric that PG set and in the past perhap only maybe Airbnb and another company

[46:24] 46 minutes, 24 seconds hit it. But now what we're seeing things have dramatically changed where on average this is the growth of companies that within three months they basically 3x.

[46:34] 46 minutes, 34 seconds Yeah. In the history of YC this has never happened before. So we get to live in this moment where like people in this room can create something that actually

[46:43] 46 minutes, 43 seconds has a real impact and you can see it and you can tell because uh your customers are going to say I can't believe this exists and thank you and they'll pay you

[46:51] 46 minutes, 51 seconds and then every week 10% more people will be paying you.

[46:55] 46 minutes, 55 seconds And what we want to close off here, I know a lot of the lecture theme has been about how you could build a oneperson frontier lab. This whole lecture was

[47:02] 47 minutes, 2 seconds about that lab can become a oneperson company and that could be you. We just gave you all the secrets here. Thank you everyone.
