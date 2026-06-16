---
title: How to Make Claude Code Your AI Engineering Team
video_id: wkv2ifxPpF8
url: https://www.youtube.com/watch?v=wkv2ifxPpF8
channel: Y Combinator
channel_id: UCcefcZRL2oaA_uBNeo5UOWg
channel_url: https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg
publish_date: '2026-04-23T07:30:49-07:00'
upload_date: '2026-04-23T07:30:49-07:00'
category: Science & Technology
duration: '21:49'
length_seconds: 1309
view_count: 158172
is_live: false
thumbnail: https://i.ytimg.com/vi_webp/wkv2ifxPpF8/maxresdefault.webp
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: AI Just Changed Coding Forever
  start: 0:00
  start_ms: 0
- title: From YC to Building With AI
  start: 0:09
  start_ms: 9000
- title: Why AI Coding Feels So Different
  start: '1:07'
  start_ms: 67000
- title: Turning AI Into a Real Team (GStack)
  start: '2:45'
  start_ms: 165000
- title: Let’s Build an App Live
  start: '3:45'
  start_ms: 225000
- title: The Question That Kills Most Ideas
  start: '5:23'
  start_ms: 323000
- title: This Idea Just Got Way Bigger
  start: '7:13'
  start_ms: 433000
- title: The “Feels Illegal” AI Hack
  start: '8:38'
  start_ms: 518000
- title: Upgrading the Idea in Real Time
  start: '10:50'
  start_ms: 650000
- title: Breaking + Fixing the Plan
  start: '12:44'
  start_ms: 764000
- title: AI Designs the App
  start: '14:25'
  start_ms: 865000
- title: The Full System Explained
  start: '16:59'
  start_ms: 1019000
- title: Running Multiple AI Engineers
  start: '18:00'
  start_ms: 1080000
- title: Shipping 10x Faster
  start: '20:00'
  start_ms: 1200000
- title: The Only Thing That Matters Now
  start: '21:20'
  start_ms: 1280000
description: "GStack is an open-source toolkit built by YC President & CEO Garry Tan that turns Claude Code into an AI engineering team — with skills for office hours, design, code review, QA, and browser testing. \n\nUse it with Claude Code or Codex or Cursor. It's free and open source: https://github.com/garrytan/gstack\n\nIn this video, Garry walks through how GStack works, starting with Office Hours, a skill modeled after real YC partner sessions that pressure-tests your idea before you write a line of code. He demos it live, going from idea through adversarial review, design mockups, and automated QA in a single session.\n\n00:00 – AI Just Changed Coding Forever\n00:09 – From YC to Building With AI\n01:07 – Why AI Coding Feels So Different\n02:45 – Turning AI Into a Real Team (GStack)\n03:45 – Let’s Build an App Live\n05:23 – The Question That Kills Most Ideas\n07:13 – This Idea Just Got Way Bigger\n08:38 – The “Feels Illegal” AI Hack\n10:50 – Upgrading the Idea in Real Time\n12:44 – Breaking + Fixing the Plan\n14:25 – AI Designs the App\n16:59 – The Full System Explained\n18:00 – Running Multiple AI Engineers\n20:00 – Shipping 10x Faster\n21:20 – The Only Thing That Matters Now\n\nApply to Y Combinator: https://www.ycombinator.com/apply\nWork at a startup: https://www.ycombinator.com/jobs\n\nhttps://www.conductor.build/"
notes: |-
  Transcript fetched via youtube-transcript-api fallback after the Playwright path hit 'transcript panel did not render' timeout (GH #2). ASR caption track only (kind=asr). Light cleanup: dropped [music]/[applause]/[beeping] non-speech markers, grouped consecutive segments into ~12-second windows with [mm:ss] timestamps. 521 raw segments -> N grouped windows (replace N after run).
---

## [0:09] From YC to Building With AI
[0:09] Hi, I'm Gary, president and CEO of Y Combinator. I'm also an engineer who spent the first decade of my career building software full-time. I studied computer systems engineering at Stanford, then was employee number 10 at
[0:23] Palunteer, where I was an engineer, designer, and product manager all at once. I co-founded Posterous, a micro blogging platform that sold to Twitter, and I also built the first version of
[0:36] Bookface, YC's internal social platform and knowledge base. Basically, I've written a lot of code in my career, and I'm here to tell you we are in a completely new era of building software, the agent era. It turns out the way to
[0:50] get agents to do real work is the same way humans have always done it as a team with roles with process with review. I built GStack to encode this 3 weeks ago
[1:03] and now it has more GitHub stars than Ruby on Rails. In this video I want to

## [1:07] Why AI Coding Feels So Different
[1:08] explain how it can help you build with agents. I've coded more in the past two months than I did in all of 2013, which is the last time I worked really, really
[1:20] hard as an engineer. I started playing with Claude Code back in January after hearing people like Andre Karpathy and Boris Churnney say they weren't manually writing any code anymore. And I got
[1:33] completely hooked. Along the way, I've essentially built all of Posterus, which took 2 years to build with a co-founder and a team of 10 engineers. I've essentially built all of my startup
[1:45] Posterus, which took 2 years, $10 million, and 10 engineers to build. Out of the box, the model wanders. It doesn't know your data well. So, it guesses. And guessing at that scale is
[1:58] how you get plausible looking code that silently breaks. The bottleneck here is not the model's intelligence. As long as you set the models upright, they are already smart enough to do extraordinary
[2:10] work on your codebase. This is backwards. The scaffolding should be trivially thin. GStack is my implementation of the thin harness fat skills approach. It's an open-source
[2:22] repo that I built that turns clawed code into an AI engineering team for you. skills that act like a team of specialists. Office hours is one of those skills. It's actually modeled
[2:35] exactly after what we go through at YC as a partner doing office hours with startups. It starts by asking six forcing questions for you to reframe

## [2:45] Turning AI Into a Real Team (GStack)
[2:46] your product before you start building. Let me show you how it works. The best way to get started with GStack is uh actually conductor. And so we're going to go in quick start. And GStack is actually built into Conductor right now.
[3:00] You just click GStack. And today we're going to make a tax app. Uh it's going to go into your Gmail and fish out all of your 1099s cuz it's tax day as of today. Gstack is actually a set of
[3:14] skills. And the first one that we're actually going to use is called office hours. This is actually the distilled version of what is thousands and tens of thousands of hours that the 16 YC
[3:28] partners have spent many many years honing and perfecting. And uh this is a distilled down 10% strength version of what we do at YC every day. So as you
[3:41] can see uh conductor actually just drops you right in there. We're in YC office

## [3:45] Let’s Build an App Live
[3:46] hours now and I'm trying to do a startup to create to help people get all their 1099 ins
[3:58] out of their Gmail and financial institutions. Many banks will email you with uh new tax documents, but some won't. So, we
[4:14] need to both search the user's inbox and accept URLs to go and search and download the 1099 int PDFs.
[4:29] Cool. That's our startup idea. It's just uh something to help people with their taxes and it's something that I had to deal with just yesterday. So, the user wants to do office hours about a startup idea. um and it's starting on office
[4:42] hours. So, one of the things you'll notice is um we have Gary mode on and uh what that does is it actually shows you all of the reasoning traces. So, that's one of the things I really like about um using GStack. It actually with conductor
[4:58] you actually get to see exactly what um the model is thinking as it does it. Uh right now it's just sort of getting started but now it's starting to do some context. Okay, this is a fresh project with an initial commit. No prior design
[5:12] docs. We're in startup mode. Oh, and here this is uh this is sort of the first thing that happens. You know, your model with the skill uh of office hours does a lot of thinking. It searches the

## [5:23] The Question That Kills Most Ideas
[5:24] web sometimes and figures out well what what are you trying to do? Here's the question that determines everything else. What's the strongest evidence that you have that someone actually wants this? This is actually one of the most important questions to ask yourself when
[5:37] you're trying to decide, should I work on project X or work on that startup? I actually just experienced this recently. So, I'm going to click that. I have this experience uh just the other day.
[5:50] So, what happened exactly? How many bank accounts do we have and which one sent uh 1099? Well, I have a few and then the process of hunting down is actually quite painful. Okay, the pain is real,
[6:03] but the consequence is friction and annoyance, not actual penalties. Well, I mean, frankly, my accountant uh sends me annoyed emails, and sometimes they get a phone call because they're just trying to do my their job, and uh I'm supposed
[6:16] to be there to help them. And so, I do have more than five accounts. This is actually a really interesting thing. It points out, Turboax and HR Block actually have 1099 import features, and Plaid connects to
[6:28] banks. Why aren't those solving it for you? So, I answered and it said, "Well, the user's thinking bigger than a document act creator. They're seeing this as a funnel. The hook is we'll find all your 1099 ins for you, solving an immediate pain. But the expansion is now
[6:42] that you have your docs, let's actually get your taxes prepared, which is matchmaking and lead genen for tax preparers. And it's a classic wedge strategy. It's actually a more interesting business model than just the document aggregation alone, which is
[6:55] right. You could probably charge $2 or $5 a month or $2 or $5 maybe an entire year for $1099 in aggregation, but you can actually charge um a percentage of the transaction that ends up happening
[7:09] with a tax preparer, which uh might be 10x more. This is actually a very cool

## [7:13] This Idea Just Got Way Bigger
[7:14] part of office hours. I might just build this for myself just for fun because I do have to do this every single year. And this is actually one of the most fun parts about using office hours and GStack is it's not this sort of on rails
[7:26] thing. It's more like a conversation with your model. And so if you just came in and gave instructions to the model as it is, if I just typed the original thing, which is I need to go and find my
[7:38] 1099s, it'll go do that. It will just literally do it, but it won't think about who's the user, what is this, what is the business model, who wants this, what's the pain point, how does it work, right? Like this is the kind of stuff
[7:51] that we get to do every day with lots and lots of founders in office hours and we're pretty good at it, but so is this skill. Revised AI browser automation GStack browser style lets the user log in then AI navigates to tax docs and
[8:04] downloads PDFs. The user watches it happen. I think that's correct. Let's see. I mean this is a very interesting thing for me. I mean I feel like I learn about the process of building a little bit even though I do office hours with
[8:16] people all the time. This is sharp push back on premise 3. You're right. I do have GStack browser and the approach you're describing is genuinely clever. The model would be user logs in AI takes over, navigates to tax docs, finds the 1099 ins, downloads it. No plaid, no
[8:31] stored credentials. The user watches the whole thing happen in the visible browser. I mean, what I like about it is it can happen on their actual browser.

## [8:38] The “Feels Illegal” AI Hack
[8:38] It's not happening in the cloud. The cloud is just someone else's computer. One of the cool things that GStack does increasingly is it lets you use codecs to actually sort out all of the crazy bugs that might be in here. I'm not
[8:52] going to do it right now, but it is something that you can do when you're at home working on it yourself. The way to think about Claude code is that by default it uses Claude. And I think Opus 4.6 is sort of ADHD CEO. He's the guy
[9:06] you want to get a beer with and he's got a billion ideas, but when the going gets tough, you got to call in your autistic CTO and that's Codex. All right, we're going to skip for now because we're actually pretty close. I feel like
[9:19] basically we're in plan mode and office hours helps us start off with a plan that has a lot of the things thought through. So, here's actually a really cool uh example. It actually thinks through and here's three different
[9:33] approaches. The first approach is Gmail off then search for tax doc not notification then output a checklist of banks which issue 1099s. There's no browser automation initially. The effort
[9:45] is small and the risk is small. You know when I look at that it's like that sounds interesting but it doesn't sound big enough for me to actually even work on this. Like I could do that myself. Next is full stack Gmail and AI browser
[9:58] automation using uh and a CPA marketplace. This sounds like what I want actually. And then uh it sort of thinks out of the box. It says, "Oh, okay. What about approach C? CPA first flip the go to
[10:11] market. You know, I would say B sounds right." And then actually I sometimes I like to add this extra thing which like when I have an idea when I one of the approaches speaks to me, but then I think about something else. I'm like, "Okay, well, I like B, but actually we
[10:25] could use the browser interaction to skip Google OOTH entirely and just have the user open Gmail and a version
[10:40] of GStack browser could just use Gmail to find the 1099s to search for automatically."

## [10:50] Upgrading the Idea in Real Time
[10:51] Simultaneous to that, it could also ask the user what other banks they have. Also, and this is what happens for me. If they already have a CPA, you can find
[11:05] out from the email. And if you're me, you probably already have a bunch of emails from your CPA bugging you for the specific accounts.
[11:19] We're sort of at the end of office hours, but as you can see, we already went from sort of a halfbaked rough idea for something that we might want to do. I'm not saying this is actually a good startup idea, but you can see how this
[11:32] got farther along. We started with something that might start with OOTH and then CPA's nagging emails, but in the end we realized, well, we have a browser and the browser could be used with
[11:46] browser automation to search the inbox, find all of the 1099s that you need to download. It can also using LLM ask you which bank portals you need to add to and it can go log in with your account
[12:00] and actually download the PDFs for you and then send an email to the CPA. So I really like this browser automation is a very outofpocket sort of unusual way to solve this problem. And the wild thing
[12:12] about coding models is, you know, a year ago, two years ago, even like 3 months ago, it's not clear to me that anyone would even try this. I think that's the most interesting thing about uh our time
[12:26] right now. You're able to have an idea and then get farther along with it than you ever would be. Frankly, sometimes I use office hours and maybe one in three times I get to the end of it and I say, "You know what? This isn't something
[12:39] that makes sense." You'll notice that there's actually a feasibility aspect of office hours and that's one thing I

## [12:44] Breaking + Fixing the Plan
[12:45] really pride myself on in office hours working with startups. I have a very strong opinion about how the world works and what might work and um it's just very interesting to see Opus 4.6 mirror
[12:57] that in trying to help you figure out what your startup or product idea might be. Now, what it's doing is a multi-step adversarial review. It's trying to put your idea through the paces. And as you can see, it's already found a bunch of
[13:10] things and it's going to try to autofix it. There's no failure handling. There's no privacy section. 2FA handoff has no proposed solution. It actually tries to auto fill out these things. And it if it
[13:23] can, it does. And so our doc survived two rounds of adversarial review. And it automatically caught and fixed 16 issues. Um so we're going to approve this design doc. So, as you can see, the
[13:36] adversarial review improved the score from 6 out of 10 to 8 out of 10 with three remaining issues that we can worry about later. Now that we've locked in the adversarial review and addressed all these issues, uh, normally what I would
[13:49] do is run plan CEO review, but instead I think what we're going to do is jump directly to design shotgun, which is one of my most fun uh, ways to use this. And this is just one of a bunch of different
[14:03] design tools that are in the bag. So, it figured out here's a bunch of different views. What do you want to actually design? And let's just do the main checklist dashboard. Design checks my
[14:15] visual brainstorming tool. So, it'll actually generate multiple AI versions and then ask us questions about it. These are three directions. It takes about 60 seconds. it actually farms it

## [14:25] AI Designs the App
[14:26] out to uh OpenAI codecs which um is able to use image gen. So all right let's there's three versions command center friendly progress and split view. Let's take a look. All right so let's let the agents cook and we'll be back in about 5
[14:39] minutes. Great. The agents are done cooking. And this is what we we got back. We got three different options for the actual page that shows up in the command center for tracking down our tax
[14:53] documents. So let's look at them one by one. There's option A, B, and C. All right, here's one command center. There's a dashboard. Here's all the specific. I mean, this looks pretty good. If you can extract here are all
[15:06] the banks and here are all the 1099s and where are they coming from? Um, and what their status is, that's pretty good. I like that. I'm I'm going to give that a four out of five stars. Option B is like
[15:18] much more friendly. Um, so option A is sort of like if you're a Linux hacker, I bet you would really like this. But option B, I think it's more friendly for just normal people. So I kind of like I I I might put that as a five. That might
[15:32] be a pick. And then let's see. Option C. This makes it way more complicated than it needs to. So I really wouldn't do that. Let's go with option B. Uh, and then the cool thing is if you
[15:44] don't like it, you can enter uh, you know, any of your feedback. You can click regenerate. But in this case, we're just going to run with option B and continue. So that comes back in. And you know, as you can see, we're going to
[15:57] go ahead and select option B. And there it is. So a friendly card-based approach with progress and the progress ring. Good instinct. Variant B is locked in. So while I have you, I mean, that is just two of 28 different commands. We've
[16:13] got more than 70,000 uh stars now. And some of the people who use it like they they actually talk about how when they're using cloud code they spend 80 to 90% of their time in office hours
[16:26] plan CEO review and auto plan. Um this is sort of a rough view of how that sprint process actually works. We already talked about office space, but if you don't want to do a lot of back
[16:39] and forth, if you don't want to be in the weeds, I did create auto plan, which gets you through CEO, engineering, design, and developer experience review using basically my default recommendations. Like these are sort of
[16:52] programmed to be what I would do if I were you. There are a bunch of design skills that you can use after the code is actually done. Cloud code will

## [16:59] The Full System Explained
[17:00] actually build when you click approve on the plan and then after it's done writing the code you can run review which does a staff level uh bug catching service that goes through puts the work
[17:14] through the paces full code review uh finding bugs that might not have been in the plan mode and then the coolest part I think that um is actually an incredible amount of code is I wrote a CLI around playrite and chromium
[17:29] So there's actually an entire headed and headless browser in there. And that was a real magic moment for me as I was using cloud code as I sped up. Um there's this idea of trying to get a to
[17:42] a level 8 software factory and GSAC does not get you to level 8, but I do think it gets you to level seven. And that's where I can run multiple conductor windows on different projects and
[17:56] sometimes three or four all on the same project all at the same time. These are

## [18:00] Running Multiple AI Engineers
[18:01] parallel PRs with parallel branches and parallel different features that all can land more or less simultaneously. And one of the bottlenecks I ran into was that, you know, once the agent was doing
[18:14] all the work of planning and design and coding it, I found myself sitting there doing QA, probably the least fun part of software development. So that made it very, very important for me to try to
[18:27] automate that. And when I did, Claude in Chrome MCP is one of the worst pieces of software I've ever used. You know, every time it would try to do an action, it would think and think and think. There
[18:39] was crazy context bloat. Often it wouldn't even do anything, but it would take two to three seconds even when it was working to be able to take an action. And I was amazed that I could use all of my other skills in GStack to
[18:54] create the SLQA and SL browse tool. I basically wrapped Playright at the CLI level. And now your cloud code and any agent now can actually just use the
[19:07] browser. And so you know, not only could it use the browser, it can take screenshots. It can do complex interactions. It can click on things. It can fill things out. Now it can even download media, run eventually full
[19:20] regression tests and update CSS and assess real browser bug issues, whether it's JavaScript or CSS. And finally, there's a ship tool. So, it's sort of the last step before to make sure that
[19:33] your PR is ready to land on main. And this is actually how I work. I run 10 to 15 parallel cla code sessions all at the same time. I might in one session be running office hours on a brand new
[19:46] idea. And I actually now have multiple open- source projects with tens of thousands of stars. And I'm probably sitting on about 400 uh PRs to review
[19:59] right now. And so I almost always have

## [20:00] Shipping 10x Faster
[20:01] one or two sessions active for each project just evaluating and bringing in all the open- source fixes that I'm getting from the community. Uh and I evaluate it in waves. Um one of the things that's been really scary in AI
[20:16] coding right now is supply chain attacks. So I'm really really paranoid about it. But the great thing is I have GStack that has my back. So I don't have a to-do list anymore. One of the things that has emerged is I actually click on
[20:28] whenever I have an idea or I get a bug report from a user or I see something on X where someone's frustrated with what GStack or GBrain does, I just click the plus icon in Conductor. It creates a new
[20:40] work tree and each one of these things is a new work item. And all I have to do is run office hours, CEO review, end review, uh adversarial review, and then I just run my normal process. when it's
[20:54] ready to land, it lands and I can do 10, 15, 20, sometimes 50 PRs in any given day, depending on the number of meetings I have in that day. So that's it. Uh, GStack is available right now. Just go
[21:08] to github.com/gritan/GStack. When you run/off hours, you're getting a version of the real product thinking we do at YC with founders. similar push

## [21:20] The Only Thing That Matters Now
[21:20] back and similar reframing before you ever meet us. Give it a try and let me know what you think. This is the most incredible time in history to build software. The barrier to building just
[21:32] collapsed. The only question left is what are you going to build? It's time to let it rip. Go make something people want.
