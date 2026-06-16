---
title: "AI Dev 26 x SF: Andrew Ng: The Future of Software Engineering"
video_id: g8um2AEf5ZA
url: https://www.youtube.com/watch?v=g8um2AEf5ZA
channel: "DeepLearningAI"
channel_id: UCcIXc5mJsHVYTZR1maL5l9w
channel_url: https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w
publish_date: '2026-05-20T11:30:55-07:00'
upload_date: '2026-05-20T11:30:55-07:00'
category: Education
duration: '19:21'
length_seconds: 1161
view_count: 10095
default_language: None
is_live: False
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
  - language_code: en-orig
    name: English (Original)
    kind: asr
    is_translatable: true
description: |
  At AI Dev 26 x San Francisco, Andrew Ng discussed the rapid evolution of software engineering driven by AI coding agents and introduced new tools to support this shift:
  
  - The Shift in Software Development
  - New Bottlenecks and Generalist Skills
  - Job Market Perspective
  
  Andrew also announced:
  
  Context Hub: A tool designed to provide AI agents with up-to-date documentation to prevent hallucinations and the use of deprecated APIs.
  Code Dream: An interactive learning environment featuring AI-driven video conversations and a browser-based terminal for practicing with modern coding agents.
notes: |
  Acquired 2026-05-24 via yt-dlp fallback (youtube-transcript-skill Playwright path
  failed at 60s timeout — the documented panel-render failure mode for some
  long-format videos; this is a 19-min talk so panel-render-fail was unexpected
  but reproducible). Custom VTT dedupe applied: kept only the *new content* line
  per cue with hour-aware `<\d\d:\d\d:` timing-tag detection (the same parser
  built during the Caldwell ingest on 2026-05-22). 502 deduped ASR segments
  spanning the full 19:10 runtime. Stage cues and audience reactions retained.
---

## Transcript

[0:07] It's really nice to see all of you here.
[0:10] In addition to the AI prompting for
[0:12] everyone course announcement, there's
[0:14] one other significant announcement I
[0:16] want to make in this presentation today,
[0:18] and you'll be the first people in the
[0:20] world to hear about this. And I'll do
[0:22] that toward the end of this
[0:25] What I want to do today is share with
[0:27] you what I'm seeing with the future of
[0:29] software engineering as it relates to AI
[0:31] coding, and touch on context up, and a
[0:34] new thing that I'll announce a little
[0:35] bit to share with you more I think how
[0:38] we can hopefully help developers
[0:40] navigate to this future.
[0:43] A year ago at the first AI dev,
[0:46] I presented a slide like this, where I
[0:49] talked about thinking of software as
[0:52] assembling many building blocks to
[0:54] create these wonderful things.
[0:56] So, it turns out that I often think of
[0:59] software, tools, frameworks, APIs,
[1:03] as akin to LEGO bricks. And if all I
[1:06] have is one type of white colored LEGO
[1:09] bricks, I can build some stuff, but not
[1:12] that interesting.
[1:13] If you mix in some black LEGO bricks,
[1:15] you can build more interesting things.
[1:17] Mix in some blue ones, mix in some red
[1:20] and yellow ones, and so on. And as the
[1:23] number of disparate building blocks you
[1:25] have grows, the way you can combine them
[1:28] to create interesting software grows
[1:29] exponentially or grows combinatorially.
[1:32] Over the last year, the rise of AI
[1:35] coding agents has made it far more
[1:37] effective for all of us to quickly put
[1:40] these building blocks together to create
[1:42] amazingly cool stuff. And this includes
[1:45] both AI building blocks, like large
[1:47] language models you can prompt, rag
[1:49] agentic workflows, and many more, as
[1:51] well as non-AI building blocks like UI
[1:53] components, persistence of databases,
[1:56] identity or off managers, and so on. And
[1:59] it turns out because of AI coding,
[2:02] these building blocks are proliferating
[2:04] at a speed like we've never seen. There
[2:06] are more and more building blocks every
[2:07] single day, both AI and non-AI, for all
[2:10] of us to use.
[2:12] And this is wonderful, especially when
[2:14] AI coding lets us
[2:17] get AI agents to assemble these building
[2:20] blocks for us.
[2:21] Now, when I speak to different teams in
[2:24] startups, academia, also very large
[2:26] companies, one question that's often
[2:28] discussed and debated is how much should
[2:30] we use AI coding agents? And there's
[2:33] actually one popular poll question,
[2:34] which is I'm not going to ask this
[2:36] question, but I see many people ask how
[2:38] much of your coding is AI versus human?
[2:41] And, you know, there'll be some teams
[2:43] that'll say, "Oh, yes, my team does 80%
[2:46] of our coding by AI." And, you know,
[2:48] that's pretty good. Um, my own coding is
[2:52] not 80% AI, it's actually pretty much
[2:55] 100% AI. And I want to share with you
[2:57] why I think this even last gap makes a
[3:01] big difference. Oh, by the way, in case
[3:03] there's anyone here that's 0% AI, it's
[3:05] okay too, but I encourage you to
[3:07] increase that percentage, right?
[3:10] Um, but what I see among teams is if 80%
[3:13] of your code is AI, then in terms of
[3:15] time spent, it actually looks like this,
[3:18] right? AI coding is time, human to
[3:21] review that 2% of code just takes
[3:22] forever. Whereas a team that's 100% AI
[3:25] coding just gets a lot more done in a
[3:27] short time.
[3:30] I find that this is true not just for
[3:32] writing code, but also reviewing code.
[3:35] And I know that a lot of teams that
[3:36] still have AI write code, but have a
[3:37] human review every single line of code.
[3:39] But for myself and a lot of my teams, we
[3:41] find that if I got to review the code,
[3:44] then I become the bottleneck, and it
[3:46] also doesn't work. And I'm not saying,
[3:49] you know, if you're if you're working
[3:50] for NASA building and you need to write
[3:52] 50 lines of code for a spaceship,
[3:55] go ahead, write it by hand. It's totally
[3:57] fine. So, this is not a religion where
[3:59] we should never be allowed to write code
[4:00] by hand. But, what I'm seeing is um many
[4:03] of the frontier teams are trending
[4:05] toward 100% almost 100% of code written
[4:08] by AI. And this creates a real
[4:11] acceleration that getting only 80% of
[4:13] the way there feels very different from
[4:16] um both for writing and reviewing code.
[4:20] as coding is done by AI, there are
[4:22] fascinating second-order effects.
[4:25] I think um last July in the batch um
[4:28] newsletter, I wrote about the product
[4:30] management bottleneck. And was this
[4:33] observation that um when I'm trying to
[4:36] build stuff,
[4:37] you know, we'll often have an idea,
[4:39] build the prototype, that's software
[4:41] engineering, and then go to users, get
[4:44] feedback, that's PM or product
[4:45] management work, use those ideas to come
[4:48] and refine the software.
[4:50] So, AI coding has made that 10 or 100
[4:52] times faster.
[4:54] And so, this means that deciding what to
[4:56] build or the product management work
[4:58] becomes the new bottleneck rather the
[5:00] actual building. So, what I started to
[5:03] see, like starting a year and a half
[5:05] ago, was this very strange trend where
[5:08] we used to have product manager to
[5:10] engineering ratios of, you know, one PM
[5:12] would keep eight engineers busy, right?
[5:15] These ratios typically vary in a small
[5:16] but one to eight PM to engineer, one to
[5:19] seven common in many companies. But, the
[5:21] ratio started to trend toward, you know,
[5:23] one to two was really weird, and then
[5:25] one to one, which is even more weird.
[5:28] And what I'm seeing is rather than one
[5:31] engineer and one PM, the only thing that
[5:33] can move even faster is you take those
[5:35] two people and collapse them into a
[5:38] single human. And I find that engineers
[5:40] who shape products or product managers
[5:42] that can code can move really fast. And
[5:45] that speed is a huge advantage.
[5:47] But not everything can be done by a
[5:49] single person team. And so I find that
[5:52] for more and more AI natives, the trend
[5:54] is that very small teams, they're all
[5:56] kind of generalists where the engineers
[5:58] can do some PM work, the PMs can do some
[6:00] engineering work, and everyone kind of
[6:02] knows almost everything, and the small
[6:04] team can move really fast.
[6:07] I know that in some Silicon Valley
[6:09] circles, it's trendy to talk about the
[6:11] job apocalypse. This idea that AI would
[6:13] take all jobs almost all jobs and the
[6:16] rewriting in this phase.
[6:18] Um, frankly, I'm not really seeing that.
[6:20] And in fact, with this profile of
[6:22] engineer, the future AI engineer has a
[6:26] very bright future.
[6:27] When my teams are hiring for AI
[6:29] engineers, these are these are what we
[6:31] look for, right? First, have to be able
[6:33] to use coding agents uh effectively, be
[6:35] it Cloud Code, Gemini's AI, or Codex,
[6:38] open code, or something else. Um, and
[6:42] I find that having a robust knowledge of
[6:44] the amazing building blocks out there,
[6:46] which is a challenge because there's so
[6:48] many of them. So many and they change so
[6:50] quickly. That is a challenge, but
[6:52] knowing these building blocks lets you
[6:53] assemble things very quickly. I'll come
[6:55] back to the building blocks a few times
[6:57] in this presentation.
[6:58] And then lastly, I find that people with
[7:01] generalist skills, be it basic product
[7:02] management or other things as well, can
[7:04] build much faster. So there's a
[7:06] combination of skills on the ability to
[7:09] how to build things as well as the
[7:10] ability to know what to build. And um,
[7:14] I'm seeing massive
[7:16] unmet demand for a lot more engineers
[7:19] with anywhere near this mix of skills.
[7:21] Frankly, even my teams, we can't find
[7:23] enough of these people.
[7:25] and this is why
[7:27] um, and and maybe going beyond the
[7:30] product management bottleneck, I want to
[7:31] take that one step further, which is
[7:35] when software engineering speeds up 10
[7:36] or 100 times X, everything else seems
[7:38] slow in comparison. So in addition to
[7:40] the product management bottleneck, I'm
[7:43] seeing that um
[7:44] there's often a design bottleneck cuz
[7:46] you design something and she implements
[7:48] it or even better, maybe the designer
[7:49] just implements it in code without going
[7:52] through a design tool like, you know,
[7:53] Figma, and that even speeds it up. And
[7:56] one thing that used to be painful, but
[7:58] is even more painful now, is the legal
[8:00] compliance bottleneck, right? If you
[8:02] spend 3 months writing code and legal
[8:05] takes a month to sign off, it's okay,
[8:08] but if you take a day writing code,
[8:09] you're going to wait a month for legal,
[8:11] it's like, boy.
[8:13] Um and even marketing bottleneck. For
[8:15] many of our teams, we write code and
[8:17] ship products so fast that marketing has
[8:19] a hard time scrambling to keep up with
[8:21] what these engineers are doing to figure
[8:22] out how to tell people about it. So, I'm
[8:24] seeing design bottlenecks, legal
[8:26] compliance bottlenecks, marketing
[8:27] bottlenecks, sales bottlenecks, a whole
[8:29] whole bunch of other things.
[8:31] And this is why I find it increasingly
[8:34] small teams of people that includes
[8:36] engineers, but also generalists, can
[8:38] move really fast. And a piece of good
[8:40] news is, it turns out that an engineer
[8:43] that's not a marketer,
[8:45] but that knows how to prompt AI well,
[8:48] maybe they're not an amazing marketer,
[8:50] AI actually makes really weird marketing
[8:51] decisions, but, you know, they could do
[8:53] some basic marketing work. And in fact,
[8:56] if a team needs software, product,
[8:58] design, legal, and marketing, and it's a
[9:01] team of two,
[9:02] by definition, these two people have to
[9:04] have some skills in in all of these
[9:06] functional areas, and I find that smart
[9:09] AI native teams, they can use AI to help
[9:11] with some of these other functions can
[9:13] move really fast. Um not advising anyone
[9:16] to be a lawyer, but but frankly, I I I
[9:18] often have AI, you know, deal with legal
[9:21] stuff as a first draft and then take it
[9:23] to a real lawyer to sign off before I,
[9:25] right, before I uh launch something, but
[9:27] I find this AI native team moves really
[9:29] fast. Something I don't have time to
[9:30] talk about is how to structure multiple
[9:33] AI native teams to work together because
[9:35] again, not everything can be done by a
[9:36] 10-person team, but if you have a
[9:38] 100-person team of many AI native teams
[9:40] with limited communication and clear API
[9:42] boundaries, that also helps to scale
[9:44] beyond a single team.
[9:47] But if we come back to the work that
[9:48] needs to be done to create software,
[9:50] writing software code is just a small
[9:52] piece of it that's the third thing
[9:53] rapidly, but I just don't see the AI job
[9:56] apocalypse happening anytime soon. Um, I
[10:00] find that the business media often has
[10:03] to be more accurate than the popular
[10:05] press because the popular press can tell
[10:07] exciting stories, but the business media
[10:09] is paid to get it right, and I've been
[10:12] encouraged that over the last month or
[10:14] two a lot of the business media has been
[10:16] getting the story right that this AI job
[10:18] apocalypse now just missing Tesla
[10:20] vehicle's job apocalypse, job apocalypse
[10:23] being delayed, a Federal Reserve Bank
[10:25] small highlight, sorry if I can't read
[10:27] it, um, highlighted few CEOs need to
[10:29] reduce their workforce or study by the
[10:31] Federal Reserve Bank of Philadelphia.
[10:32] So, I'm actually um, and and to be
[10:35] clear, I know a lot of people are
[10:36] feeling job insecurity at all levels of
[10:39] insincerity. Um, I think we need to do
[10:41] something to address that, and I know
[10:43] many people have been laid off because
[10:45] of over hiring for the pandemic or
[10:47] hiring from zero interest rates period.
[10:50] So, I'm not saying the job situation is
[10:52] is perfect, but there's a lot of it
[10:54] that's not that pretty, but the job
[10:55] apocalypse is possible to talk in some
[10:57] circles. I just don't see it happening,
[10:59] um, which is why I'm eager to keep on
[11:01] investing in all of us becoming better
[11:03] at building these things.
[11:07] one of the hardest things to do,
[11:08] exciting most important hardest is as
[11:11] we're becoming better and better
[11:12] builders each of us, how to master these
[11:15] building blocks. I want to share with
[11:17] you a framework of parallel skill
[11:20] Here's what I mean.
[11:21] We talk a lot about how our coding
[11:23] agents are becoming more capable, and
[11:25] this includes agent skills like the
[11:28] Anthropic agent skills and so forth, but
[11:29] more generally our coding agents are
[11:31] just getting better and better.
[11:33] And then
[11:35] there's the education or training world
[11:36] I've been a part of for a long time that
[11:39] focuses on building human skills.
[11:41] But looking at the future, I think we
[11:43] increasingly need parallel skill
[11:45] development where as our coding agents
[11:48] become more capable,
[11:51] our people with people need the
[11:52] complimentary skills to help us to drive
[11:55] the coding agents in the appropriate way
[11:57] so that we can partner together to build
[11:59] new things.
[12:00] So, I want to briefly touch on two
[12:02] things in the rest of this presentation.
[12:03] One is Context Hub, which I talked about
[12:05] before, but I'll spend a couple of
[12:06] minutes on. And the second, which is the
[12:08] announcement I'll make toward the end,
[12:10] is Code Dream.
[12:12] So, um Context Hub. It turns out
[12:14] building blocks are proliferating so
[12:16] fast that most of our coding agents,
[12:18] which have a knowledge cutoff date,
[12:20] you're far in the distant past,
[12:22] sometimes a year old, sometimes a month
[12:23] old, will often hallucinate or use
[12:25] deprecated APIs or not know about the
[12:28] latest tools you want to use. So, it
[12:30] turns out even today, if you ask Auto
[12:32] Code um to call the OpenAI API, it will
[12:35] use the chat completions API, which is
[12:37] older and deprecated, and call older
[12:39] models because most of the training data
[12:41] on the internet uses this older API,
[12:44] even though the newer APIs have been out
[12:45] for a long time.
[12:48] Context Hub is a tool that some
[12:50] colleagues, uh Vivek Prasad, uh Sanyam
[12:52] Hota, and I built um in order to give
[12:55] your AI agent most up-to-date
[12:57] documentation. And it turns out that um
[13:01] if you run Context Hub
[13:03] with uh Auto Code, it will generate code
[13:06] with the newer responses API. Um maybe
[13:09] just to show you really briefly, I don't
[13:11] know, chop search OpenAI.
[13:15] Um so, this returns to this of packages.
[13:18] And then chop get
[13:20] this actually right OpenAI/chat.
[13:25] I did some more.
[13:26] And so, this will fetch the latest
[13:28] documentation on open AI that knows
[13:35] right knows about GPT 5.5 has the knows
[13:38] about the responses API and so on. And
[13:40] this is a tool that you are welcome to
[13:42] use of but it's actually you know built
[13:45] for your coding agent to use and so this
[13:49] um like all right a 600 line markdown
[13:51] file right kind of long for a human to
[13:53] read or you can you're welcome to read
[13:54] it to give you all the context it needs
[13:57] make these and other API calls
[13:58] correctly. So I pray many of you too
[14:00] right? I've had my coding agents
[14:02] hallucinate API calls
[14:04] definitely you know open AI Gemini calls
[14:07] make bad calls to various database
[14:09] services there's just so many tools our
[14:11] coding agents don't know about but
[14:13] feeding in this latest context I think
[14:14] can be very helpful.
[14:16] But beyond that I want to share with you
[14:19] a project I've been working on to help
[14:21] with human skill development. Um for a
[14:24] long time you know my team's been
[14:26] working on a variety of online courses
[14:28] and please keep on taking online courses
[14:30] I think it's an important part of how we
[14:32] can all stay up to date with the
[14:34] building blocks and other tools and
[14:36] we've been exploring one other
[14:38] alternative experience that um I'm
[14:41] announcing here for the first time today
[14:43] and that's the project we've been
[14:44] working on called Code Dream. Um
[14:48] the Wi-Fi here is not great so I'm going
[14:50] to see if the live demo works. It well
[14:53] may not. But let's see if this
[14:58] Welcome to Code Dream. This is not a
[15:00] course it's a conversation where I want
[15:02] to show you how to use a coding agent
[15:05] together with tool called context hub to
[15:07] write code using up-to-date API
[15:10] I say this is a conversation because I'd
[15:12] like you to imagine we're on a video
[15:13] conference call
[15:14] and you can interrupt me at any time
[15:17] using that little microphone button down
[15:19] The Code GG has created a voice agent
[15:21] that has information you need to try to
[15:23] answer your questions as I will.
[15:25] So, feel free to stop me if there's
[15:28] anything that you want to chat about. Or
[15:29] if you like, you can just lean back and
[15:31] watch the presentation.
[15:33] Here's the idea, all right.
[15:36] What are we going to learn about in this
[15:40] We're going to learn how to use Context
[15:42] Hub to keep coding agents up to date
[15:45] with the latest information. Then, we'll
[15:48] build a joke generator app together.
[15:51] So, this is not a slide, right? I just
[15:52] clicked into this and let's let's tell a
[15:55] dad joke about
[15:56] bad Wi-Fi.
[15:58] Why did the computer show later where
[16:00] was bad connection? Okay, not bad, could
[16:02] be worse.
[16:04] And the other thing about this being
[16:06] JavaScript is um you can also copy paste
[16:10] from these slides. So, for example, this
[16:12] is a slide with instructions on how to
[16:15] install Context Hub and how to prompt
[16:17] open code and so on. So, I should copy
[16:19] on hitting command C
[16:22] and then go into the Codoji build
[16:24] environment. And um this is a a terminal
[16:27] in my browser
[16:29] where I can
[16:31] you know, paste that command. I just
[16:33] copy pasted from my slide to run npm
[16:35] install chob. And then um I can do
[16:38] things like
[16:39] start up open code, which is open source
[16:42] version of a coding agent kind of like
[16:44] you know, alternatives to cloud code or
[16:45] I zero I open I codex. And then I don't
[16:48] know, write some
[16:50] Python uh
[16:54] Right. And so, this is a um learning
[16:56] practice environment that uh
[16:59] lets you practice using modern coding
[17:01] agents with tools like Context Hub.
[17:06] and so
[17:08] we have been working
[17:10] on this Codoji build environment for
[17:13] quite some time.
[17:14] And um I'm excited about exploring this
[17:17] concept where in s- in lieu of taking a
[17:21] course, you can come on to a video
[17:23] conversation and have a conversation
[17:25] with me or an AI version of me to try to
[17:29] gain new building blocks and code in
[17:31] this more modern AI coding way.
[17:34] And I am
[17:36] happy to announce that Code Realm is
[17:38] available as of today in preview.
[17:51] &gt;&gt; So, please check it out. Um, and the
[17:52] first experience will show you how to
[17:55] use Code Assist app and give us
[17:57] feedback. We're eager to keep on working
[17:59] to make this better.
[18:02] So, just to wrap up, um,
[18:06] coding agents are allowing us to
[18:08] assemble building blocks quickly to
[18:10] create software, and that acceleration
[18:13] is real. But, many of the downstream
[18:16] implications about whether new
[18:18] bottlenecks are are still being worked
[18:20] out, and I'm eager to help our entire
[18:22] community keep moving forward because
[18:24] the job openings are there. The job
[18:26] apocalypse is not being nearly as bad as
[18:28] people are hyping it up to be, and I
[18:30] think it's important that we keep on
[18:31] learning these building blocks and
[18:33] learning these skills.
[18:35] And for parallel skill development,
[18:37] coding agents are
[18:38] working well, but give them access to
[18:41] latest building blocks, given the right
[18:42] context, um, context help. will help.
[18:46] And for human skill development, I'm
[18:48] excited also to share with you the Code
[18:51] Realm conversations, and all of you in
[18:53] this room are the very first people in
[18:55] the world that I've shared this with uh
[18:57] outside outside our team. Um, and I hope
[18:59] you will check this out and that'll help
[19:01] you to master some new building blocks
[19:04] and master some new skills.
[19:06] So, with that, um,
[19:08] really excited to be here. Thank you for
[19:10] all coming, and thank you all very much.
