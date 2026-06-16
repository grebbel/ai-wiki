---
title: Running an AI-native engineering org
video_id: igO8iyca2_g
url: https://www.youtube.com/watch?v=igO8iyca2_g
channel: Claude
channel_id: UCV03SRZXJEz-hchIAogeJOg
channel_url: https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg
publish_date: '2026-05-08T11:50:11-07:00'
upload_date: '2026-05-08T11:50:11-07:00'
category: Science & Technology
duration: '28:38'
length_seconds: 1718
view_count: 9626
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/igO8iyca2_g/maxresdefault.webp
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
thumbnails:
  - {url: 'https://i.ytimg.com/vi/igO8iyca2_g/hqdefault.jpg', width: 168, height: 94}
  - {url: 'https://i.ytimg.com/vi/igO8iyca2_g/hqdefault.jpg', width: 196, height: 110}
  - {url: 'https://i.ytimg.com/vi/igO8iyca2_g/hqdefault.jpg', width: 246, height: 138}
  - {url: 'https://i.ytimg.com/vi/igO8iyca2_g/hqdefault.jpg', width: 336, height: 188}
  - {url: 'https://i.ytimg.com/vi_webp/igO8iyca2_g/maxresdefault.webp', width: 1920, height: 1080}
description: |
  When agentic coding goes from individual tool to org-wide default, the tool isn't
  the hard part...your processes are. Fiona Fung, Director of Engineering for Claude
  Code, walks through what broke at Anthropic (review, ownership, hiring) and the
  norms we had to rewrite to keep shipping.
notes: |
  Cleaned from YouTube's auto-generated English captions. ASR-mistranscribed
  product/people names corrected (Cloud → Claude, co-work → Cowork, Fun → Fung,
  anthropic → Anthropic, etc.), most stutters trimmed, light punctuation added.
  Section headings inferred from topic shifts (the video itself has no YouTube
  chapters). Timestamps preserved.
---

## Intro

[0:00] *[music]*

[0:08] Hey folks, do y'all hear me? Okay, okay.

[0:12] I swear this is not a Claude Code thing, but do you mind if I take a photo? Because Boris and Jared had their session at two, and I really thought this was going to be empty. There was just no way people would still be coming in from that session. So — oh my gosh. *[applause]* Oh, thank you. I promise me and Boris don't just do selfies all the time. *[laughter]*

[0:34] Good afternoon and thanks for attending. My name is Fiona Fung and I lead Claude Code and Cowork engineering and product. So I work really closely with Boris and Cat. Before Anthropic I led and grew teams at Meta and Microsoft.

[0:52] For today's talk, this is the overall agenda — but the whole idea is: what are some of the lessons I've learned helping Claude Code and Cowork grow as we're building out the team? It's interesting — these are lessons I learned even thinking about my time at Meta or Microsoft, but at Anthropic too. It's funny: I did this slide deck maybe a month ago, and already I've had to change some of the content, because when I started this deck there were no routines, and even that way of working was different for me.

[1:25] I want to cover five themes that I've noticed. One: the bottlenecks have moved — they've shifted. When bottlenecks shift, what are some of the team norms we had to rewrite within the Claude Code team? I also want to share how we rolled them out, and what signals tell me, "yeah, we're trending in the right direction" — because it's always going to be important to keep checking, is this still serving us? Then I'll end with a few questions I still have for myself, and some suggestions you could take back to your teams to have conversations together.

## Section 1 — The shift: bottlenecks have moved

[2:11] First section: the bottlenecks have moved. I call it "the shift." You'll probably hear me repeat this subtitle a lot: **what served you prior may not serve you any longer**. Even thinking about my experience — Anthropic, Meta, Microsoft — the constant growth mindset is just a muscle that has served me really well. Especially right now, when the rate of change is just a little bit crazy, right? I remember the first time I started doing some vibe coding, last year, and it was still making bugs and I'm like, "ah, why are you using constants everywhere, that's not good engineering practice." Now it's just become so much more capable. That's the interesting shift I'm seeing — when the bottlenecks moved, how do you adapt everything else around the bottleneck?

[3:03] Maybe y'all are feeling this too: for years engineering bandwidth was the expensive thing. Coding throughput was really expensive. When you think about all the processes we have for shipping software, a lot of it was around — *(hi, welcome, there's a chair, take away those reserved tags, no one's sitting there. There's another one right here, sir, welcome.)* — all of that, even how we used to do planning… remember waterfall, then agile? Everything used to be that way because engineering bandwidth was really expensive.

[3:37] I'll take a little segue here. This is not the first time our industry has had to adapt. I'm going to put you all in a time machine — come back with me to the year 2000. That's when I started my career. I worked on Visual Studio, and we were shipping Visual Studio 2005. I kid you not, in those days we used to ship software on CD-ROMs. Before CD-ROMs it was floppy discs. I still remember VS 2005 — there were really hard deadlines. We had to hit them because we had to get the software to the manufacturing lab to print on the CDs to put in the boxes to ship in the stores. When we were able to distribute software online, that also changed how we ship software.

[4:17] So that's what I'm finding really interesting about this new shift: engineering bandwidth is no longer the expensive thing. On the Claude Code team, coding really isn't the slow part anymore. It's not just that it's not the slow part — the throughput has really increased. It's not only "yay, we're all getting to build more"; the *amount* we're generating has changed a lot.

[4:51] When your bottlenecks shift away from the act of typing — writing code, writing tests, refactoring used to be expensive. I remember all those conversations: "we have to schedule time to do refactoring." "Oh, but we have to do product work, and refactoring is expensive — when are you going to find time to do it?" All of that has shifted. That is no longer the bottleneck.

[5:17] When that happens, bottlenecks shift to other areas. For example: verification, review, cross-functional partners, security — because coding is no longer the bottleneck *and* we're doing so much more of it. These are the new bottlenecks we're seeing. So it's always us asking: is this code correct? Who reviews this code? That's probably one of the top questions I get from fellow eng leaders — "how are humans keeping up with how you're doing code reviews?" And how is it maintained, because now it's a lot easier for all of us to generate a lot of code — so the maintenance cost too.

[5:59] These are some of the processes I noticed quietly stop working. I love that phrase — "quietly stops working" — because we all put in processes hopefully for a reason, right? "Hey, there was a gap, we want to improve." But what I've found over the years is, **rarely do processes kill themselves.** We tend to just layer more and more on. I remember on one team we had so many SLAs — a P0 bug SLA, a high-pri SLA, a SEV review SLA. After a while I was like, "oh no, we need to stack-rank priorities so engineers know which SLA is even more important." Even at the time I thought, hey, we should defrag a little bit.

[6:45] These are the processes that might have served you. Again — what may have served you may not serve you any longer:

- **Planning norms** — we used to spend a lot more time pre-planning because coding time was expensive.
- **Code ownership** — there used to be a lot of questions of who wrote this code, who owns it. That's a little bit of an odd question now.
- **Code reviews** — we'll get into that.
- **Team makeup** — roles are blurring. Engineers now have AI to augment them, and my non-engineering partners are also all shipping code. What happens when roles start blurring and you don't have those silos anymore?
- **Knowledge sharing and onboarding** — another signal we're noticing at Claude Code that's changed for us.

## Section 2 — Norms we had to rewrite

[7:36] In the first section we talked about the shift. So within the Claude Code team, what are some of the norms we had to rewrite? I want to share those — hopefully some will resonate or be helpful.

The areas: **code review** (human judgment of who actually needs it), **onboarding**, **planning**, **hiring** (especially with roles blurring and team makeup changing), and **org shape** — that's one of my favorite spicy topics. I'll share that story with you. When I started proposing this at Anthropic, I love my recruiting partners — they're awesome — but one recruiting partner really did think I was crazy.

### Planning and technical debates

[8:25] How has planning changed? Also technical debates.

**Planning — we do a lot less of it.** And the timing — I call it JIT planning, almost like JIT compiling. When I first joined I was like, "don't we need a six-month roadmap?" We put some effort in, wrote it, it was pretty good for three months. Then I came back over the new year and so many things had already changed. So I realized — wow, a six-month roadmap just seems like a little bit too long. How do you do just the right amount in the right time? Because prototyping and code generation are not the bottleneck they used to be.

[9:05] **Technical debates — code wins.** When I first joined the Claude Code team, I wanted to do a refactoring — I wanted to learn the codebase. Boris and I had a healthy technical debate about which way to go, and I almost leaned into my old toolbox — almost tapped him on the shoulder, "let's go to that room, get a whiteboard." And I'm like, wait a minute — nowadays I can just generate all the different options we've been discussing. I generated three PRs. The cool part about that for the technical debate: I really cared not only about the implementation of the API, but about the impact to all the callers. Having Claude help me generate the three different versions let us debate not just implementation but impact to the colleagues. That's another really interesting pivotal change.

[10:02] When building is cheap, arguing is expensive. How does that shift your team norms? I do want to call out: this makes it even more important to set up team culture around alignment. For example, what totally won't fly — because code is so much faster to generate — is "the last person who checked in wins." "I'm going to stay up at 3am to submit this PR, set up a routine so I get the last word in." Definitely a no-no. That makes it even more important to make sure you have good team culture: open, honest technical debates, but also good team alignment.

### Design docs out, prototypes in — but verification way up

[10:41] I talked a lot about what we *reduce* in planning. On Claude Code we've definitely reduced the design-doc-before-every-code ritual. For certain teams and scenarios — especially async discussions — design docs are still really important. But on Claude Code, instead of a doc, most of our discussions are *a PR*. One of the words we have is, "hey, we have an idea — go prototype." We don't really do a lot of product reviews because the landscape is changing fast. So let's prototype, get a lot of internal Ants using it, ship it out to all of you, and hear all the excellent feedback. That's changed our planning ritual to be a lot less design docs and mostly discussions in PRs or prototypes.

[11:28] We reduced that. But what did we double down on? This is an area we actually need to do *more* and continue being better at: **verification**. The throughput is different, there are new ways to break — how do you scale out? I call it "shift left." In the old days you'd get code out, and I'd love to find bugs before any of you find them. What's better than me finding a bug is shift-left — more automation so we catch it earlier, closer to the source.

[12:04] The other thing that's interesting: because roles are blurring — for example, my designers — I'd love them to have more confidence that when they check in code, they don't break something. I remember I fixed a bug in resume or something, and the next day I was catching up on Boris's threads and saw someone tag him — "I'm noticing a bug." I had that sinking feeling. *Did I just cause a bug?* Because of the throughput, I really want to make sure everybody — regardless of role — has a lot higher confidence in the changes they're putting in.

### "Who made this change?" — double-click into the real question

[12:33] My advice here: because all our PRs are assisted by Claude, "who made this change?" is a little bit of an odd question. What's more helpful than that question is what I call **double-clicking into it.** In the old days, when you used to ask "who made this change?", what question are you really trying to answer? Are you looking for who caused this regression? Definitely don't want to blame, just want to know who last touched the code that might have caused the break. Or are you looking for an expert to answer a customer question? Or trying to gain context? Whatever the double-click question is, also think about whether you can automate it.

[13:15] It's funny — I mentioned I had to change a slide deck when I started this talk a month ago. Part of every morning was, I'd bring up my desktop Claude Code, go into the customer feedback channel, ask it to summarize. That was a morning ritual with my coffee. Now it's *routines* — I can set that up, and even better than what I was doing before, I just kick it off and with my morning cup of coffee I get a pretty good overview. So my point: code ownership is a little more fuzzy, but on the flip side, double-click to what question you're really trying to answer, and see how Claude can help with those.

### Code reviews — where to trust Claude, where to keep humans

[13:53] How do you keep up with code reviews? If y'all saw the keynote this morning, Cat talked about it — we definitely leverage Claude Code Review heavily. What's interesting is figuring out: where do you trust Claude (a lot), and where do you still want a human?

For sure — and as Cat showed you all — Claude does a great job babysitting PRs. We have Claude handle all the style and lint feedback, even maybe catching some bugs and fixing them before the full commit, and adding tests. That's what we've leaned heavily into Claude for.

[14:32] But where I still definitely want a human is expertise. **Trust but verify.** For example: legal review — I always want my legal partner. Risk tolerance — for trust boundaries and security-sensitive code, I still want to pull in the experts.

[14:49] The other area, which is kind of fun, is product sense and taste. One of the fun things I like to use Claude for: I like to decorate Claude for the holidays or seasons. Last holiday, I wanted to update Claude in the terminal to give it a holiday theme. I asked Claude Code, "can you turn Claude into a snowman?" Claude wasn't that good at ASCII art in those days. I asked my design partner, "hey, can you review this for me?" And she gave me such good feedback — she's like, "you turned Claude into the Mr. Peanut character." Because I was trying to make him a snowman. Okay — I'm going to do something more simple. So Claude was just ice-blue with a snowflake. Keep in mind that product sense.

### Team makeup — two profiles I index on

[15:40] Which leads to: what should my team makeup be? Because roles are blurring, Claude is augmenting. On Claude Code, two profiles for engineers I've heavily indexed on:

1. **Creative builders with product sense** — the dreamers. Big sense of curiosity, passionate about "oh, here's a problem, maybe I could ship a product that solves it" — and then a lot of iteration to deliver a delightful experience.
2. **Deep systems expertise.** When I first joined the Claude Code team, we were pretty good with product generalists and creative folks, but missing folks with distributed-systems expertise. When you're building things like Claude Code remote — to ensure we can run Claude everywhere — you really still need that expertise.

[16:27] Whichever software engineering org you're part of or supporting, think about those hard parts you want to continue doubling down on. What I index *less* on is raw throughput, because thanks to the models we just have a lot more.

### Cross-functional gaps Claude can fill

[16:41] The cross-functional gaps is another interesting one. I wanted to do an update to how we do survey responses, but I didn't have a dedicated content designer to work with me. I'm an engineer — my writing skills are quite terrible. I struggle to write things short and succinct. I don't want to overload you all in the terminal — every line of space is really important. But that's where Claude — in the old days I'd be looking for a content designer to work with, give changes back and forth. Now Claude has really helped augment that role and was a really good content design partner to make sure the verbiage was good and succinct.

[17:26] On the flip side — say a PM — our PMs code a lot, which is really fun to see. With Claude, you have non-traditional coders now able to do more engineering, but you also have engineers who can lean into things that traditionally weren't on the technical side — content, design. Claude and AI have augmented roles all around.

### Org shape — flat, with managers starting as ICs

[17:55] This was a spicy one. When I first ran Claude Code, everyone was like, "okay, you're going to grow the team by some amount." I could tell recruiters were still using the typical 10-ICs-to-one-manager and asking how I'd start nesting. I really leaned into keeping it scrappy.

Let me step back. Whether it's at Anthropic or Meta or Microsoft, whether it was Visual Studio or Facebook Marketplace or AR/VR devices or Claude — what I've found really helps me ship product is heavy, heavy, heavy **dogfooding**, especially for leaders. Nowadays it's actually fun — I can still be in the code. For a while it wasn't. When you can't get your hands on the code, I always make sure I make maker-time so I'm using my product day in and day out.

[18:42] That's why I wanted every manager in Claude Code to start out as an IC first — also to earn some street cred with the team and learn how to be an effective engineer. I really structure the org to be as flat as possible because I want us to be super agile.

This was where my recruiters had concerns. They said, "you want to hire managers and they'll start as ICs first? No manager will be interested in that." I'm like — well, this is what dogfooding on the Claude Code team is about. This is what I expect, and if someone's not interested, it's better for us to do an earlier separation. Also, there's no way I'd be able to ramp or do code without Claude — there's just so much context-switching. So for the managers in the room, I encourage you to lean in.

[19:31] I'll be honest — for a long time at Meta, I'd still try every year to do one PR a year. But the workflows would always change — all the internal tools — by the time I learned one command it would have changed. Nowadays I don't even remember git commands; I just always ask Claude to help me out.

### Knowledge sharing — code as source of truth

[19:48] Knowledge sharing — what becomes your new source of truth? On our team on Claude Code, the **code is the source of truth.** When I'm answering customer requests, I just have my desktop Claude Code and all my local repositories, and I answer a lot of customer questions from there. Having the codebase be the source of truth prevents some of the lag you might have had before — keeping documentation correct alongside the code.

[20:18] But this is where you should do what makes sense for your team. If you have a lot of really good specs, check those into the repositories, and have Claude help: "hey, take a look at how my code execution still matches what I expect from the spec."

## Section 3 — How we roll it out

[20:40] How do we roll it out? These are the norms we changed. There's a blend of: what do we *mandate* as team norms — make sure you're gaining alignment with the team — and where do I *enable* each pod within Claude Code to do what makes sense for them?

In terms of forcing function: align with the team on the must-dos. These are a few of the core Claude Code team principles we live and breathe. And by the way — going back to that growth mindset — we keep these up to date. Every few months we ask, "is this still having the same effect, still serving the purpose we wanted?"

For example — and I should replace this slide — it's not "every engineer uses Claude Code." That's obvious. It's actually **every Claude Code team member, including cross-functional partners.** And we all use Cowork quite a bit too.

**Claudify everything you can.** What's better than one of us doing it? Having Claude. Always think about — is there some way to automate? Whether it's verification, more shift-left — always be thinking, what you're doing right now, is there some way Claude could actually help you do it?

The last one is my favorite: **explicit permission to kill those processes.** Processes will not kill themselves. As you're supporting teams, it's really important to get fast feedback: what are the things we're spending a lot of time on?

[22:08] I remember when I first joined, we used to do standups. The team got a little bigger so we had a spreadsheet — we'd all put up our weekly progress. All of a sudden we were like, "oh wait, we should just do a script — a standup script — so we can run Claude and all of us are much more aware of what everybody else is doing." That's an example: one day I was looking at the spreadsheet going, wait, this doesn't make sense anymore. Always question, always look to defrag and kill old processes.

[22:44] I want to leave a lot of room for pods to adapt. Each team has a lot of high agency for how they do triage or leverage Claude to do triage, planning rituals, standups, on-calls, and which workflows to Claudify first. We don't usually mandate "thou shalt automate this." We have suggestions and learnings, but always give room to your team — they may be touching on different problem areas.

[23:13] If I zoom out, the three things I prioritized that made the biggest difference:

1. **Keeping the team as flat as possible** — pods of work, but really keep it agile. On Claude Code and Cowork we have one overall team mission. Sometimes when you start creating pods, each pod sets up its own mission, and any time you have to shift it takes a lot of time to walk people through. As flat as you can — that served us really well.
2. **Claudify everything** — better than you doing it. See how Claude can help. It frees us up to do the harder work.
3. **Processes pile on.** Work with your team to see what processes you should let go.

## Section 4 — Does it actually work? Signals to watch

[24:05] Does it actually work? I can't go into the explicit numbers, but three general metrics you can look at as you roll out changes that might tell you, "yeah, this seems like it's starting to be successful":

- **Onboarding ramp-up time has dramatically reduced.** How soon an engineer or designer or PM can start being effective on your team.
- **PR cycle time shortening.** This one is interesting to double-click into, because it might actually help you identify a gap that's not just about lack of AI adoption — it's where the rest of the pipeline might be struggling to scale. As we put through so much more code, sometimes product infrastructure or CI can't keep up with the amount engineers are checking in.
- **Claude-assisted commits going up.** For us, by default every commit is Claude-assisted. I don't think I've seen a non-Claude-assisted commit probably in the last four months.

[25:12] Hopefully these three resonate as metrics you could look at on your own team.

[25:19] I'd also say — outside of just number of commits, also think about the end goal. Zoom out: what is the product you're trying to make more delightful for users, or what is the problem you're trying to solve? Sometimes you see headlines: "this company said X% of code is now generated by AI." Throughput is great, but really think about how you measure what you're actually trying to solve. For example, we really want to keep an eye on quality and reliability. So those are some of the things we're paying more attention to as well.

## Section 5 — Audit your own efforts (questions I'm still asking)

[25:51] My last section — audit your own efforts. I'll share transparently: I still have a couple of questions I'm asking myself.

- **iOS and Android orgs.** When engineers can now more efficiently flex across mobile platforms, does the more traditional way of having an iOS team and an Android team still make sense? I'm still thinking that through.
- **How much do you push fully automated review?** When do you strike that balance between fast enough, and we lost something important? It goes back to trust but verify.
- And what's interesting — you might have heard in Daren Lannon's earlier talk — the model capabilities keep improving. So even if you might need to do more verify than trust for a certain section of work, that might also change with the next model. That's why it's always important to re-evaluate.
- **Roles are blurring** — how do you make sure everybody feels equally productive?

[26:52] If I were to leave you with one thing to take back: pick your noisiest workflow. By "noisiest" I mean most expensive — something you yourself might be dreading, or your team might not look forward to — and ask, **is it still really serving its purpose?**

[27:09] I'll share another funny story. There was a team I was on where we used to have this weekly review. Very expensive — like 50 people in this large room. I noticed everybody was on their laptops, except for when it was their turn to give their status report, and then they'd pop their head up, say the status, and go back down. I'm like, this is a very expensive meeting. I just asked the simple question: why are we having it? And just that one question — everybody's like, "yeah, it's true." So we canceled it.

[27:34] That's why it's always important to think. I figured this might be something fun for you to take back — look and see what's one piece of workflow you might consider. Can you either automate it, or even — is it still serving its intended purpose?

[27:50] So with that, that's the end of our talk. *[applause]* Thank you.

[28:03] Thanks a lot for attending. I really thought this room was going to be empty, so thanks for not having me sit by myself. I'm around here today and tomorrow — if you have any questions or want to chat more, feel free to introduce yourself, happy to chat. Thank you.