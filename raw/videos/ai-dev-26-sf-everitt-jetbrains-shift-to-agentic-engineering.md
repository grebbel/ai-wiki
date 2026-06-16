---
title: 'AI Dev 26 x SF | Paul Everitt: The Shift to Agentic Engineering'
video_id: n366hY4JZ9U
url: https://www.youtube.com/watch?v=n366hY4JZ9U
channel: DeepLearningAI
channel_id: UCcIXc5mJsHVYTZR1maL5l9w
channel_url: https://www.youtube.com/channel/UCcIXc5mJsHVYTZR1maL5l9w
publish_date: '2026-05-22T08:29:32-07:00'
upload_date: '2026-05-22T08:29:32-07:00'
category: Education
duration: '28:17'
length_seconds: 1697
view_count: 543
is_live: false
thumbnail: https://i.ytimg.com/vi/n366hY4JZ9U/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgSig9MA8=&rs=AOn4CLAdlj-0bJAgz6p1SlzA1ountWxSaA
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "More code, fewer staff — the industry is on a bender. But what about quality? \nAt AI Dev 26 x San Francisco, Paul Everitt from JetBrains discussed the rise of agentic engineering and how old lessons can be adapted to build new professional practices."
notes: 'Auto-generated ASR cleaned: skill-fetched metadata via Playwright; transcript fetched separately via yt-dlp WebVTT fallback because the engagement panel timed out after 180s (recurring failure for ≥20-min talks per youtube-transcript-skill failure modes). VTT rolling-window dedup applied: second-line-of-each-cue content kept, inline <c>/<t> timing tags stripped, ~5-second buckets, HTML entities unescaped.'
---

## Transcript

[0:10] Today we are going to hear about uh the shift towards agentic engineering and increased code output. Uh welcome Paul.

[0:15] >> One minute into this conference,

[0:20] Jonathan said let's talk about the future of software

[0:25] engineering. Let's have a conversation. Let's figure

[0:30] it out. That's exactly what we're going to do in this talk on Agentic

[0:35] Engineering. Let's have some fun. I'm Paul from Jet Brains. I'm a

[0:40] developer advocate at Jet Brains. Best damn developer tools company on the

[0:45] planet. Three words I want you to know that make us really stand out. All three

[0:50] of these words are bleeping awesome.

[0:55] Privately held. We are currently on stage zero in our VC rounds. Never taken

[1:00] a dollar or a euro from anybody.

[1:05] Profitable. Yes, that exists. 25 years

[1:10] of making money the oldfashioned way from happy customers. Thank you. Let's

[1:15] hear for profitability.

[1:20] And then the one that I say because we're in a certain moment and when I say this everyone's eyes go,

[1:25] "Yeah, we're a European company."

[1:30] And these combined together. Yeah, exactly. The these combined together to

[1:35] make us just a really cool story to

[1:40] tell. 25 years of doing this code intelligence stuff and developer

[1:45] productivity, we've seen some transitions before. Speaking of transitions, I don't do the

[1:50] I love me slide, so instead I'll make fun of myself. This is me at the first

[1:55] Python meetup in 1994 before I got married and learned you can

[2:00] spend more than $5 on a haircut.

[2:05] Uh I'm a Python oldster, let's put it that way. When we were putting this all together, as Namita just said, it was

[2:10] kind of a cooperation with deep learning and we just had done this course on spec

[2:15] driven development and we wanted to kind of have a tie into it. What's the title

[2:20] going to be? What's the description going to be? Paul, what do you want? Well, this is what I wanted. We didn't

[2:25] get a chance to put those slides in the actual title, but I made the slides. So,

[2:30] I put these alternate titles here,

[2:35] which kind of gets into the theme of what I want us to talk about here today.

[2:40] Agentic engineering. There is something going on in our

[2:45] industry right now. Some problems. Let's talk about it. Let's talk about our

[2:50] discipline and then let's talk about a solution. Aentic engineering. Then what

[2:55] does this mean in practice? And then I want to finish with a CTA

[3:00] with a little bit of a twist on it.

[3:05] So just to get us kind of started, get us warmed up. I want this to be not my

[3:10] talk, our talk. So let's do the raise your hand if raise your hand if

[3:15] in the last three months you've done anything that you would call coding.

[3:25] Good with an agent. Good. Did you like it?

[3:30] For the record, that's most of the

[3:35] hands. Did you ship any of that into production? Was it a bunch of Nex.js

[3:40] dashboards? Okay. A about twothirds of the hands. Do you think we're in a

[3:45] bubble? Raise your hand. Some of y'all are optimists.

[3:50] Do you think you know what this is all going to look like at the end of the

[3:55] year? Raise your hand if you think you

[4:00] know. Awesome. My whole talk depended on you not raising your hands. Zero hands went up.

[4:05] Nobody knows anything.

[4:10] I don't know anything. 101% of you are smarter than me. However, all of us seem

[4:15] to know everything at this moment right

[4:20] now. All of this out here, all these talks, all these great ideas. Go on

[4:25] archive and you'll see these papers. Every week there's like 10 revolutionary

[4:30] breakthroughs that are just sitting there. This is fine.

[4:35] Andrew in the leadup to the conference in his newsletter, The Batch, which you

[4:40] should subscribe to, talked about this. We're shaping the future in this

[4:45] conference, in this talk, because we're all gonna figure it out right here,

[4:50] right now, together. You should think of this as like riding into the future,

[4:55] kind of like the end of Thelma and

[5:00] Louise. All right, let's talk about the problem. I want to frame this on the way to getting to aentic engineering.

[5:05] We we've all seen these things. We have individual value that's happening, but

[5:10] we're not really getting organizational value yet from AI. Lots of things that

[5:15] I'm going to talk about in just a moment that this is part of it. We're getting

[5:20] some success, but it isn't durable to use the temporal word from yesterday.

[5:25] The most obvious one is productivity. In the middle of the year last year, there

[5:30] was this study that came out that really sent shock waves through the industry. Certainly 95%

[5:35] of companies got anything out of their

[5:40] investment. This is a name that I want you to remember. Duron Oamoglu,

[5:45] Nobel Prize winner. When you're putting slides together for a talk, citing a

[5:50] Nobel Prize winner is always a good strategy. 2024 economics and he talks

[5:55] about this productivity problem. Productivity is like five things in

[6:00] coding and in software engineering and

[6:05] coding is only one of those and you could speed that up completely and it would still only be partial. And you see

[6:10] this in the DX study. It ain't 10x, it's like 10%. And they had a follow-on study

[6:15] that talked about this a little bit more. Code was never the problem. Code

[6:20] was never the bottleneck. All the things

[6:25] that go with engineering and software engineering are more of it. Grady BCH has a wonderful interview, the

[6:30] third golden age of software engineering, where he talks about this.

[6:35] He's optimistic. He's realistic. He has some spicy hot takes. One of them is

[6:40] coding was never the whole thing for

[6:45] software engineering was so much more than that. Let's talk about quality. And this was

[6:50] uh reinforced in a uh talk yesterday

[6:55] about defects, phase defect rates. 50% bad number. I don't know if you feel

[7:00] that way. 50% feels kind of bad.

[7:05] Simon Willis has become the developer AI developer whisperer. Prolific guy from

[7:10] the Django co-founder of Django.

[7:15] He puts it pretty starkly from a quality perspective. He's worried about a

[7:20] challenger disaster. You take the human out of the loop. You let the agent shove

[7:25] stuff into production. Maybe it drops a bunch of tables. No, I'm sorry. That was this week. Maybe it does something

[7:30] really, really bad.

[7:35] Price is also an issue. Um, my guy Ed Zitron, I don't know if any of y'all

[7:40] follow Ed Zitron. Thank you.

[7:45] uh you should pay your money for these because these are these are fantastic

[7:50] newsletters. He's been banging this drum for a while. We can't keep subsidizing these tokens.

[7:55] Guess what? It started to happen. If you want to have a provocative presentation,

[8:00] put in a slide from the register. Always a source of a good hot take. It already

[8:05] started happening this month. Pricing is going to change. Trust is another issue.

[8:10] This was another big one from last year. Developers are like, "Eh,

[8:15] not so sure how I feel about this." Only

[8:20] 3% last year had a lot of confidence in

[8:25] the accuracy of the generated results. I didn't know that my vocabulary needed

[8:30] a new word, but here we are. Token

[8:35] maxing employees and part of organizational trust and organizational value.

[8:40] You give them a system, they will give you a game, a way to game the system.

[8:45] And on that, you see what has been mentioned in several talks

[8:50] in the last couple of days. Uber is like, oops, annual gone in three months.

[8:55] And when you start seeing Fortune

[9:00] magazine talking about workers and engineers are outright rebelling, you've

[9:05] got a problem on your hands. This was a little bit farther into the article. a 67 point gap between how management

[9:10] feels and how engineers feel about this

[9:15] mental health. I come from the open source community. I don't know if any of

[9:20] you are in open source, but if you are, big heart for me. We've been talking

[9:25] about this a lot, PR swap, but that's the same internally.

[9:30] You have this issue with maintainers being shoved all of this stuff and it's

[9:35] a tragedy to the commons. That is

[9:40] definitely true. Uh you need open source. Please keep that in your brain.

[9:45] Uh I believe that Paige stole this from

[9:50] me on the first day. So I already know the answer to this and then Marina in her panel discussion talked about it a

[9:55] little bit. But just to be clear, the rest of the world might not be like

[10:00] us. In Europe, they might be a little bit different. In regulated industries

[10:05] like banks, I was talking with Oh,

[10:10] Michael, just in a previous uh talk, he's in the insurance business. I said,

[10:15] "Michael, how does insurance business feel about move fast and break things?"

[10:20] And he just laughed. And from a governance perspective, you're starting to hear talks about

[10:25] sovereignity. 84% of Europeans are like,

[10:30] "Eh." But the sad part of this is these are all the problems and as Daron Asamoglu says, it's a missed opportunity. You've

[10:35] been given the god box.

[10:40] What are you doing with the god box? Are you creating magnificent new solutions

[10:45] for your customers or are you just squeezing the profit margin?

[10:50] This showed up with Anthropic. 27% of the work went to things that couldn't

[10:55] have been possible without the god box. Grady talked about this in this podcast.

[11:00] Uh Grady Buch is the uh creator of UML,

[11:05] which is a pictorial representation of code. Sounds kind of like the moment

[11:10] we're in. And he really said this that I'm able to

[11:15] build things I never would have been a able to build before. I can use my imagination. So, the industry looks at

[11:20] all this and says, "What do we do about

[11:25] these problems?" I've got a great idea. Let's have layoffs.

[11:30] That'll solve everything. Let's make wild claims about the

[11:35] elimination of entire industries. And then another word enters my

[11:40] vocabulary that I didn't ask for. mega layoff at lasten and uh Block and Stripe

[11:45] and Amazon all this month. Why do they

[11:50] do it? See if you can answer my question before me. Why do they do it? Their stock price

[11:55] goes up. Did any of you get it right?

[12:00] Yeah. All right, cynic. But then you see the counter counter

[12:05] example. Sam Alman brings up another

[12:10] word into my vocabulary. AI AI washing and so now I'm a cheerleader for Sam

[12:15] Alman. Uh then you have the counter counter example. Maybe jobs aren't being

[12:20] eliminated. Maybe they're being created. Maybe it's not just hiring is up for

[12:25] junior developers. Hiring is up for hiring people for HR managers. Crazy

[12:30] world we live in. And the response to this from leadership

[12:35] has been more code fewer people. And we

[12:40] need to give an answer to this. We

[12:45] need as engineering we need to give them a new frame. That new frame is

[12:50] engineering. But a new engineering poured into old

[12:55] wine poured into a new bottle. Agentic engineering. Let's bring back for reals

[13:00] engineering. Vibe coding created around 14 15 minutes

[13:05] uh minutes ago months ago uh by Carpati and then he's

[13:10] like okay clean up. What I meant was agentic engineering. So he coined the

[13:15] phrase a few months ago and it seems to have caught on a little bit. My guy

[13:20] Simon Wilson had been talking about it. He started adopting that phrase and

[13:25] Simon's actually writing a book on this where he's doing kind of a taxonomy of these things. Addi Osmani wrote a blog

[13:30] post about uh Gentic Engineering. And as

[13:35] I tell you these blah blah wrote a blah blah in your mind you should be thinking

[13:40] it's entering the hype cycle. I should put this on my LinkedIn as a global

[13:45] recognized expert and this thing that existed for two months. And then Addie

[13:50] has this wonderful line about vibe coding. Vive coding is an engineer. It's just hoping

[13:55] the one that influenced me the most. I wonder if any of you saw this one from

[14:00] the open AI team. Harness engineering has so many like really piercing

[14:05] thoughts about the jump from software engineering up to uh agentic engineering

[14:10] and redefining the role to be about

[14:15] systems and scaffolding and getting more leverage from the humans from the

[14:20] humans. There will be humans. Good news. And in the old mode, engineers built the

[14:25] thing. And in this harness engineering, open AI, we build the thing that builds

[14:30] the thing. That will be our value ad. If

[14:35] you hit a problem like they had AI slop Friday where they would fix all the

[14:40] stuff. Don't do that. Go fix the thing that caused the problem. Always be

[14:45] making the system better. And the human will always be the bottleneck. But don't

[14:50] eliminate the human, augment the human.

[14:55] Simon talks about the dark factory pattern. You can turn the lights off in the factory because there ain't no

[15:00] humans in the factory. The humans are on the outside building the stuff in the

[15:05] factory to run the factory. Grady rightly pushed back, isn't this

[15:10] just software engineering? And if you go look at the classic

[15:15] definitions like Dave Farley from modern software engineering, coding is just

[15:20] again it's just one of the parts of engineering and Grady kind of leans into

[15:25] this in this interview really talks about uh coding was never really the big

[15:30] thing. I really encourage you this really put joy in my heart listening to

[15:35] this and he went past we went backwards past Archimedes. IBM wrote about this

[15:40] very topic and reinforced something Grady really talked about in the

[15:45] classics from the first agent gold or first golden age. Go back to first

[15:50] principles. You want to be valuable? Go back to first principles and master

[15:55] systems design. So just to recap when we

[16:00] say aentic engineering what do we mean? You build the thing that builds the

[16:05] thing. You're always trying to not make the human the bottleneck. You're trying

[16:10] to think of things like the dark track, but most of all just blah blah blah blah engineering. Let's bring back the

[16:15] discipline of engineering in your organization or even better systems

[16:20] design. So, what does agentic engineering mean in practice?

[16:30] It's just a big bag of words. Kai has the funniest videos. And just before this, he was playing the role of the CEO

[16:35] saying blah blah blah blah authentic engineering blah blah blah blah. And

[16:40] this is the engineers like it's just they're making this up. As I mentioned,

[16:45] Simon is doing he's writing a book in front of you. Highly encourage you to follow Simon. He's a hardcore developer

[16:50] and so he's one of us.

[16:55] Meta video from a meta staff engineer did a little bit of a taxonomy. All five

[17:00] of these points are fantastic. What I what you'll see in the next couple of slides there are whole disciplines there

[17:05] have been talks on whole disciplines context engineering from unboxed that

[17:10] can be part of this broader thing which

[17:15] is software engineering in the world of agents the new stack had a a good

[17:20] article with a taxonomy on it and this is kind of for me the transition we want

[17:25] engineering we want software engineering for agents it's a new thing

[17:30] in practice. I'm going to cover a a

[17:35] number of these things. Some of them might be really interesting to you. I hope this one's interesting to you. We

[17:40] just did a course with deep learning, my colleagues Zena and Costia,

[17:45] uh, and with Isabelle, and we had such a fun time, put a lot of work into it.

[17:50] Spec is the way for the human to steer the work and to get all of the

[17:55] stakeholders aligned. I would love to hear your feedback on

[18:00] this course. Then what is good?

[18:05] Is your agent good? Is your code good?

[18:10] If the answer is button go clicky, it

[18:15] ain't engineering. So the very first thing we got to get good at is evals.

[18:20] Did it generate good code in the right budget with the number of turns blah

[18:25] blah blah. In the talk just before from Sonar, Tom showed how all these models

[18:30] are different and they have different characteristics that change over time.

[18:35] That's going to be your job when a new model comes out. How does it perform?

[18:40] And so we're actually going to need data scientists doing actual work again because you don't want the LLM to be the

[18:45] judge all the time. Harness engineering is a fascinating one to me. a couple of

[18:50] talks here about this and this is from lang chain a good Python company and the

[18:55] thing can you read it is that contrast

[19:05] if you don't own your harness you don't own your memory bold provocative

[19:10] statement tooling this is another fascinating topic that I hope but I predict in the

[19:15] next six months will get on your radar and claude are talking about code mode

[19:20] uh and Cloudflare and others, the agent

[19:25] needs to run a tool. And so at that moment, it generates some code and runs

[19:30] it in a secure sandbox, exactly the code

[19:35] that it needs, not said and Grep and walking around until it figures out the

[19:40] problem. And my friends at paidandic have a rustbased subset of Python called

[19:45] Monty of course for running tool code in

[19:50] uh sandboxes at very high latency or low

[19:55] latency high lating

[20:00] in several of the uh podcasts like Lenny's podcast that Simon was on. Red

[20:05] green testing is one of those things we as engineers know about. Red green

[20:10] testing, we just don't do it because we

[20:15] can get the button to go clicky without writing a test.

[20:20] If you will write a broken test as the first step in your agent's work, the as

[20:25] he said, the agent will start to learn the way you like to write tests and will

[20:30] mimic your testing style, which is super

[20:35] cool. And then you've kind of defined success. What is green? And it instead of

[20:40] wandering around trying to figure out how to please you, it knows exactly how

[20:45] to please you. As he says, a fantastic fit for coding agents.

[20:50] This one is fascinating for me. Uh I'm going to ask this in a vague way to get

[20:55] a lot of hands to raise. Raise your hand if you work on a big old codebase.

[21:05] I'll go with 20%. We're jet brains. We're Intelligj. We've

[21:10] been 25 years of this stuff. We got a big old code base. And as we're

[21:15] learning, modularity looks a little bit different when you

[21:20] want to have parallel sub aents and highly specialized sub aents and really

[21:25] good context engineering. You might reorganize your code around some

[21:30] different principles. Principles called Ojic engineering

[21:35] QA agents. This is from the um the harness engineering and this one really

[21:40] popped for me that as humans kind of

[21:45] become the bottleneck. We we want to speed them up a little bit. So we're going to make QA agents.

[21:50] Maybe they don't do all the work, they just kind of prep the work or something like that. But the secret is

[21:55] to move more capabilities into the

[22:00] agent. try and scan the last paragraph real quick. Get a browser or the

[22:05] DevTools protocol into the agent so it

[22:10] can collect the instrumentation itself as it deems fit.

[22:15] And that kind of integration with the outside world can only come from you. I

[22:20] predict you're going to be writing some code as your organizations need to glue

[22:25] all these things together. You're building the thing that builds the

[22:30] thing. And I think that stuff is really

[22:35] interesting. Observability. Another topic that we hear a lot about here. Uh Pyantic says,

[22:40] you know, you got general system observability. We all know about that. We got AI observability. We're all

[22:45] learning about that. You probably need something that can do both.

[22:50] Orchestration is one that gets talked about. There are probably 500 Silicon

[22:55] Valley startups in series X of their funding. And Grady asked me to put in a

[23:00] line on orchestration

[23:05] about remember your architecture gluing this big big system together. Have some

[23:10] system design principles in it

[23:15] and context engineering. This is from my friends at um uh in Python. But for a

[23:20] better point on this, go see Unbox that uh Brandon gave one of the best

[23:25] presentations that I saw in the last couple of days. Some really great

[23:30] thinking out there from them and from other people. This is going to be such a fascinating field.

[23:35] And then finally, leadership and culture. I know this is kind of an unusual one from an engineering

[23:40] perspective, but some of you are engineering leads, team leads, some of

[23:45] you are CTOs. I sat at dinner last night with Raphael. Fantastic conversation. Got to hear

[23:50] firsthand about culture on all of this.

[23:55] You're going to have to manage up to your stakeholders, but really you're

[24:00] going to have to manage down. Fobbo, fear of being obsolete. Another thing

[24:05] that entered my vocabulary this month. Your folks are worried.

[24:10] That was a dramatic effect. Your folks are worried. You're a leader. You have

[24:15] to get them going in the right direction, but you have to be honest and

[24:20] authentic. I said CTA with a little bit of a twist.

[24:25] It's actually call to arms, not call to action. I want us in this room in the

[24:30] Q&A afterwards to take ownership of

[24:35] something. Again, leadership thinks this is about

[24:40] profit margin margining the old things,

[24:45] whereas we need to get them shifted to something else. That something else

[24:50] is a little bit on us. We are the ones

[24:55] they listen to. Most of you have

[25:00] probably seen this pattern over and over. They're good at what they do, but they know they can't do your job, and so

[25:05] they listen to you. Let's get them a better frame. Let's get them back to

[25:10] engineering. And so the message needs to be something that transmits well that we

[25:15] agree and talk about instead of vibe coding. we should be doing agentic

[25:20] engineering and then they will start to see it mentioning everywhere and then

[25:25] they'll start to believe and we'll get them off of automating the current and

[25:30] replacing the current workforce and over to innovation augmenting the humans

[25:35] getting great bold new things done

[25:40] and from the impractice on this get back to a discipline engineering is an actual

[25:45] discipline if you watch Grady's talk you'll see that it goes back past

[25:50] Archimedes. There are rules. It's a science. It's a practice. You can learn

[25:55] it and master it. And again, engineering

[26:00] builds the thing that builds the thing. Your stakeholders will understand that.

[26:05] Grady asked me to give a call to action to you. So Grady's cohort did unified

[26:10] modeling language did design patterns

[26:15] kind of built the field of modern software engineering.

[26:20] He knows there is a next thing called

[26:25] agentic patterns and he wants one of you in the audience

[26:30] to be the one that gets the ball rolling and helps us all figure out this

[26:35] discipline of agentic design patterns, agentic engineering

[26:40] and the folks at deep learning have been so wonderful at this conference. the

[26:45] folks at deep learn like being the host

[26:50] for two days like Mima has been all the helpers and in fact I should have done

[26:55] that at the start please they're super smart but they're also wonderful people

[27:00] a round of applause for deep learning

[27:10] maybe deep learning is the home where we all come together and create this new discipline called agentic engineering

[27:15] two best words in any presentation.

[27:20] This is from the last two slides of Grady's uh history of software

[27:25] engineering talk. You write code, you are engineers, but that code actually

[27:30] tells a story and you're the storytellers. And we are in a moment.

[27:35] We're in a weird moment. We're in a moment that needs some storytelling,

[27:40] some message, and some messengers. And that's you.

[27:45] And this best part, Simon did a sign off of a podcast. He was asked, "What's left

[27:50] for the humans?" So much stuff. He said it in such a wonderful, hopeful,

[27:55] actionable way. I'll close with the same

[28:00] two words I always sign I always sign off with. Find the joy in all that you

[28:05] do. Find the purpose in all that you do. Thank you for spending time with me.

