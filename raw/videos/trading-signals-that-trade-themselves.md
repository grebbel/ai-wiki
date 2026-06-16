---
title: Trading signals that trade themselves
video_id: EOg4gY0Yln0
url: https://www.youtube.com/watch?v=EOg4gY0Yln0
channel: Claude
channel_id: UCV03SRZXJEz-hchIAogeJOg
channel_url: https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg
publish_date: '2026-05-21T11:33:19-07:00'
upload_date: '2026-05-21T11:33:19-07:00'
category: Science & Technology
duration: '20:45'
length_seconds: 1245
view_count: 3323
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/EOg4gY0Yln0/maxresdefault.webp
keywords: []
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters: []
description: 'There are trading signals in production at Man Group right now — running real capital — that were researched, backtested, and proposed by AI. Tushara Fernando shares what made that possible inside a regulated investment firm: a governed skills framework and core data layer that taught Claude Code how Man Group''s quants have worked for decades, now scaled across ~750 developers and quants and 100+ skills. Walk away with the governance model that lets compliance say yes to AI on your most load-bearing workflows.'
notes: Transcript fetched via youtube-transcript-skill (Playwright path); manual English captions preferred where available.
---

## Transcript
[0:18] I'm Tashara Fernando. I'm head of data and AI at Mang Group.
[0:24] Mangroup are an alternative investment manager. We manage over $200 billion of assets.
[0:32] Our clients are pension funds, sovereign wealth funds, and large institutions.
[0:38] We manage real people's money, thousands of people's pensions and investment capital.
[0:45] So when we think about AI, the stakes are high for us. Our clients are real people from their teachers in Canada, their metal workers in Japan.
[0:57] So, we really need to get AI right. If we get this wrong, we could lose real money.
[1:04] 1 minute, 4 seconds One of the really large parts of our business is systematic trading. And that represents a huge opportunity to be aided by AI.
[1:13] 1 minute, 13 seconds By systematic trading, I mean algorithmic trading capabilities that look across thousands of securities
[1:21] 1 minute, 21 seconds and hundreds of markets to make investment decisions.
[1:29] 1 minute, 29 seconds So systematic trading is really about trading signals.
[1:34] 1 minute, 34 seconds And you can think of a signal like a fantasy football team. You can think that we want to pick the best players
[1:42] 1 minute, 42 seconds for our squad based on some intuitive strategy.
[1:46] 1 minute, 46 seconds So the green bars here would be a starting lineup. The red bars would be the reserve squad, the people that you
[1:54] 1 minute, 54 seconds don't want in the team. And the people in the middle, they might come in, you might kind of transfer them in, but they're they're not the star players at the moment. Maybe a subs bench.
[2:06] 2 minutes, 6 seconds So, a signal is really about thinking about a striker maybe hitting form, but
[2:13] 2 minutes, 13 seconds you need to transfer them in before the Friday deadline when the price might go up.
[2:19] 2 minutes, 19 seconds And then you have savvy managers who are really thinking about form fixtures and what might happen to get the most points in the season.
[2:29] 2 minutes, 29 seconds And they want to transfer the right players in at the right time and at the right cost. So this is quite similar to
[2:37] 2 minutes, 37 seconds systematic trading. A trading signal is really just this with stocks. So the bars here would represent company
[2:45] 2 minutes, 45 seconds stocks. We want to back the ones that would make money and we want to short the ones that won't.
[2:53] 2 minutes, 53 seconds So in this example, we've ranked the stocks by the past 3 month returns and we run that through history to see if it would have made money.
[3:04] 3 minutes, 4 seconds The interesting question is always what is that factor that you want to rank things by? What's the strategy to get the right stocks in your team? And does it work?
[3:17] 3 minutes, 17 seconds And how do you know whether it works or not? Well, the truth is you never really know. I'd love to be able to tell the
[3:25] 3 minutes, 25 seconds future, but I can't. So, the best thing that we can do is look at what happened
[3:32] 3 minutes, 32 seconds historically. We run that strategy, we codify it, and we run it against 15
[3:39] 3 minutes, 39 seconds years of history or even longer. And what that does is it runs that strategy through lots of macroeconomic environments, through lots of stresses.
[3:49] 3 minutes, 49 seconds And we can see how it performed.
[3:52] 3 minutes, 52 seconds And that back test produces lots of statistical factors. Some examples might be how much money did it make? So what's
[3:59] 3 minutes, 59 seconds the annualized return? When it lost money, and they always do at some point, how much did it lose? And we call that a
[4:07] 4 minutes, 7 seconds draw down. And we look at some even more complex statistical factors. One's called a sharp ratio which compares the
[4:15] 4 minutes, 15 seconds volatility of that strategy versus how much it returned.
[4:20] 4 minutes, 20 seconds And it's this process, this systematic trading workflow that we think that we can use AI to really enhance to come up
[4:29] 4 minutes, 29 seconds with those ideas to run the back tests and that has been our focus.
[4:38] 4 minutes, 38 seconds So there are trading signals running right now in production at Mang Group, a
[4:44] 4 minutes, 44 seconds regulated investment firm running real capital that were researched, back tested and proposed by AI.
[4:55] 4 minutes, 55 seconds By that I mean humans came up with the sorry AI came up with the idea. AI got
[5:02] 5 minutes, 2 seconds the data. AI ran the back test. AI then wrote up the strategy proposal and AI productionized the signal.
[5:13] 5 minutes, 13 seconds Humans of course reviewed all of the output to make sure that it was sensible. But a AI was at the center of that process.
[5:25] 5 minutes, 25 seconds And I'm sure you want to know what was that signal? What was that investment idea?
[5:31] 5 minutes, 31 seconds How much money did it make? How can I use it?
[5:37] 5 minutes, 37 seconds Sorry, I'm not going to tell you that today. That's our IP. What I'm here to tell you about today is our journey.
[5:43] 5 minutes, 43 seconds What was the foundation that allowed us to do that? And how can you apply those learnings in your company?
[5:52] 5 minutes, 52 seconds And it really starts with AI understanding our workflows. And to do that, we use skills.
[6:01] 6 minutes, 1 second Can I have a show of hands in the audience as to who's written a skill? Okay, that's great. Most of you.
[6:10] 6 minutes, 10 seconds So, coming up with the signal is the quick bit. The hard part is everything that you need, everything that's
[6:18] 6 minutes, 18 seconds underneath it, all of the workflows that make it happen, that allow you to act on it. Think of it like an iceberg. The
[6:27] 6 minutes, 27 seconds signal is the tip. Underneath it are all of the workflows that make it possible.
[6:33] 6 minutes, 33 seconds How do you clean the data? How do you stitch prices? How do you detect outliers?
[6:40] 6 minutes, 40 seconds How does it run? What's the infrastructure it runs on? How do you run those back tests?
[6:47] 6 minutes, 47 seconds And this is where it can quickly go wrong. If different teams are running different versions of those workflows, you get different answers.
[6:56] 6 minutes, 56 seconds One team's back test looks amazing. and other teams looks average. And because they're using different workflows, you
[7:04] 7 minutes, 4 seconds don't really know whether it was the idea that was better in one team than the other or whether they're just measuring things differently.
[7:14] 7 minutes, 14 seconds Shared workflows fix that. One common foundation means that effort isn't duplicated and you have consistency. The
[7:23] 7 minutes, 23 seconds outputs are comparable. And that's extremely important in systematic trading when we're comparing signals.
[7:35] 7 minutes, 35 seconds Out of the box, Claude is an amazing general purpose tool. It does a lot, but it doesn't know us. It doesn't know our
[7:44] 7 minutes, 44 seconds data. It doesn't know our systems. It doesn't know how we work. And it's the same for everybody in this room. So the
[7:53] 7 minutes, 53 seconds first thing that we had to do was teach it. Not by retraining it, not by doing
[8:01] 8 minutes, 1 second fine-tuning, but by giving it access to our data, our capabilities, and our workflows.
[8:10] 8 minutes, 10 seconds That's our superpower.
[8:12] 8 minutes, 12 seconds We have decades of institutional knowledge in systematic research and some of the best technical capabilities on the street.
[8:22] 8 minutes, 22 seconds And if we can connect that with AI, then AI can leverage that superpower.
[8:29] 8 minutes, 29 seconds Skills are the connective layer that allow AI to leverage that superpower. So getting them right is paramount and that was our focus.
[8:43] 8 minutes, 43 seconds But we got it wrong before we got it right. And I want to tell you about our story today.
[8:49] 8 minutes, 49 seconds We really focused on adoption. We went all in. We were doing skills workshops.
[8:55] 8 minutes, 55 seconds Anthropic helped us with that. We were doing hackathons. We wrote a blog. We were doing showand tell sessions.
[9:03] 9 minutes, 3 seconds Everybody was writing skills. The adoption was really out of this world.
[9:09] 9 minutes, 9 seconds But we started to see some cracks in our approach.
[9:12] 9 minutes, 12 seconds It was really the power users that were building the skills. It wasn't the process owners.
[9:20] 9 minutes, 20 seconds And what that meant is that all of the skills really represented a local optimization for one user. They weren't common organizational solves.
[9:32] 9 minutes, 32 seconds And nothing was really more symptomatic of this than when we ran one of the showand tell sessions one day and there
[9:41] 9 minutes, 41 seconds was a guy who used to travel a lot at Mang Group and he had loads of expenses to do and he spent loads of time doing this. So he wrote a skill for it. He
[9:49] 9 minutes, 49 seconds gave lots of pictures of receipts to Claude and it would do the expense report for him and he brought this to the show and tell session and he even
[9:58] 9 minutes, 58 seconds shared it with a few people in his team and it was working really well. And then a few days later, the expense approver came to us and was like, "Why is Claude
[10:07] 10 minutes, 7 seconds creating so many expense reports for my cost center? People from technology, people from the people team. Why do I have to approve all of them? I'm in
[10:15] 10 minutes, 15 seconds sales. I I don't want to approve everybody else's expense reports." And we dug into it and it was just because the the cost center code was hardcoded.
[10:23] 10 minutes, 23 seconds And it was really just that that was this um this local optimization.
[10:28] 10 minutes, 28 seconds Nobody had reviewed that skill. It worked for him. it worked for his team, so it was going to work for everybody. But that's not the case.
[10:35] 10 minutes, 35 seconds And he wasn't accountable for that. He kind of thought it was quite funny. And I mean, so did I, to be honest.
[10:42] 10 minutes, 42 seconds Um, but it was really symptomatic of a broader problem.
[10:46] 10 minutes, 46 seconds People were just codifying their ways of doing things. They weren't the organizational ways of doing things. And in many cases, they weren't actually the workflow owner.
[10:57] 10 minutes, 57 seconds And this is a huge problem when it comes to things like back testing and systematic trading.
[11:03] 11 minutes, 3 seconds It starts to become a blocker to scaling to enterprises.
[11:08] 11 minutes, 8 seconds Agents can't leverage those. There's no commonality. And we saw that something had to change.
[11:16] 11 minutes, 16 seconds Has anyone else faced this problem when they've been writing skills? That it was actually the process. It was the people who were the power users of a process
[11:23] 11 minutes, 23 seconds rather than the owners of it that were writing the skills. Can I have a show of hands for that? Good.
[11:32] 11 minutes, 32 seconds Yeah, we really saw that across the board.
[11:36] 11 minutes, 36 seconds But we saw that skills governance started to be the secret source that unlocked these enterprise use cases.
[11:44] 11 minutes, 44 seconds If you could connect your common workflows to AI, give it access to your data and
[11:52] 11 minutes, 52 seconds your capabilities, you could really allow agents to act on those skills.
[11:57] 11 minutes, 57 seconds And if you can do that, you can allow Claude code to do problems as complex as systematic trading.
[12:11] 12 minutes, 11 seconds So our solve for this was to have a common marketplace. Every skill was visible, tagged and tested with evals.
[12:20] 12 minutes, 20 seconds We wanted to ensure consistency. Imagine a library.
[12:27] 12 minutes, 27 seconds It captures decades of institutional knowledge.
[12:31] 12 minutes, 31 seconds There are sections for the finance department, the people department, the research department.
[12:39] 12 minutes, 39 seconds We care for every item. We care for every skill in those departments.
[12:45] 12 minutes, 45 seconds The skill is owned by the workflow owner. They're all tested. Usage is tracked. They're all reviewed. They have
[12:54] 12 minutes, 54 seconds a life cycle. And they're all visible to everybody to install.
[12:59] 12 minutes, 59 seconds It's really that care that makes this work. And it's the foundation that moves skills from individual productivity
[13:08] 13 minutes, 8 seconds solves to a foundation that can set you up for the agenda cage.
[13:14] 13 minutes, 14 seconds And it's through that that we were able to apply skills to systematic trading.
[13:20] 13 minutes, 20 seconds So now I will give you a bit of a flavor for what it's like to build a systematic signal. We've got a demo and a video on that.
[13:28] 13 minutes, 28 seconds This is my knowledge. It's where you'll find our collection of skills and manroup's context store. The skill suggestions are tailored to each
[13:37] 13 minutes, 37 seconds business unit. They have clear ownership and are organized into managed and community skills.
[13:43] 13 minutes, 43 seconds Skills and plugins can easily be installed in Claude. Plugins are useful groups of skills. For example, here we have a data plugin which gives us access to mangroups data sets.
[13:55] 13 minutes, 55 seconds We can also install skills individually.
[13:58] 13 minutes, 58 seconds For example, this is the data set skill which allows me to search man groups alternative data sets.
[14:06] 14 minutes, 6 seconds Now those foundational skills are installed, we can start to get a flavor of what it's like to build a systematic trading signal. We can use the
[14:13] 14 minutes, 13 seconds alternative data set skill to search for research such as credit card data.
[14:19] 14 minutes, 19 seconds We ask Claude what credit card data sets are available and it identifies a data set of US consumer transactions.
[14:28] 14 minutes, 28 seconds We can plot Amazon's monthly credit card spend against its stock price returns.
[14:39] 14 minutes, 39 seconds These are the results of the credit card data compared to the stock price for the same period.
[14:44] 14 minutes, 44 seconds The blue bars are credit card spend and the line is the stock price.
[14:49] 14 minutes, 49 seconds Interestingly, in the graph, you can see spikes for seasonal spend, such as Black Friday and Christmas.
[14:57] 14 minutes, 57 seconds Next, we run a back test to see if credit card spend is predictive of the stock price by comparing the peaks in credit card spending with the profits and losses of the stock.
[15:08] 15 minutes, 8 seconds In the results, the signal shows better performance than a buy and hold strategy. We can see that investing
[15:14] 15 minutes, 14 seconds $1,000 in 2021 using this signal would now be worth around $2,500.
[15:21] 15 minutes, 21 seconds This could be a fluke for Amazon. So, let's run it on a broader universe of retail companies. As there are multiple companies, we'll run it using our distributed compute infrastructure.
[15:32] 15 minutes, 32 seconds Each company is running an individual worker and then the findings are collected.
[15:39] 15 minutes, 39 seconds In this case study, we leveraged four skills to create a systematic trading signal. In reality, our signal research
[15:46] 15 minutes, 46 seconds is much more nuanced, accounting for things like seasonality, inflation, and broader sets of securities. We do this
[15:53] 15 minutes, 53 seconds with agents as well as humans exploring these ideas. The key takeaway is that the governance of these skills is key.
[16:01] 16 minutes, 1 second It ensures that everyone has access to the same data and everyone uses the same workflows.
[16:10] 16 minutes, 10 seconds Okay, so hopefully what you can see is that if you get that foundation right across the board, if you've got access
[16:18] 16 minutes, 18 seconds to all of the data, you can start to leverage more capabilities. Everything from scaling your compute to getting
[16:25] 16 minutes, 25 seconds alternative credit card data sets. And these are often owned by different teams. And it's really that that allows you to scale to the Agentic platform.
[16:36] 16 minutes, 36 seconds So what did we learn along the way?
[16:40] 16 minutes, 40 seconds These are the things that I would tell past me and that you can take away.
[16:47] 16 minutes, 47 seconds Firstly, focus on that organizational context. That is your IP. It's your moat. It's one of the few safe spaces
[16:56] 16 minutes, 56 seconds left in AI. The frontier labs are not going to solve context for you. It's not on the internet. They don't know your
[17:03] 17 minutes, 3 seconds workflows. And you already have that context.
[17:08] 17 minutes, 8 seconds You have decades of it. The work is on exposing it, not reinventing it.
[17:15] 17 minutes, 15 seconds And skills are how that those decades of institutional knowledge become leverage.
[17:21] 17 minutes, 21 seconds Treat those skills like production code because that's what they will become.
[17:27] 17 minutes, 27 seconds Plan your approach before you plan the roll out. Who's going to own the skill?
[17:33] 17 minutes, 33 seconds Who's going to review it? How does it get retired? How does it get tested?
[17:39] 17 minutes, 39 seconds Decide this be before shipping the first skill, not after the hundth like us.
[17:46] 17 minutes, 46 seconds Adoption is not a licensing problem.
[17:48] 17 minutes, 48 seconds It's a people problem. Once you've got that platform in place, you need to encourage people to engage with it.
[17:58] 17 minutes, 58 seconds We need to really think about how we capture that organizational context and rethink our workflows rather than just augmenting them.
[18:08] 18 minutes, 8 seconds And that's a training problem. It's an engagement problem. So you really need to outreach to people who are using this platform.
[18:20] 18 minutes, 20 seconds And it's through this it's through these ideas that we've been able to scale. man groups about 17 800 people 1,700 people
[18:29] 18 minutes, 29 seconds something like that and we now have 750 of them using claude code across developers quants the people team the
[18:38] 18 minutes, 38 seconds finance team everybody across all of the departments is using claude code we're seeing a lot of engagement because
[18:45] 18 minutes, 45 seconds they're able to use those capabilities in a simple way they don't need to know about everything they have this skills platform
[18:53] 18 minutes, 53 seconds that understands our workflows We now have over 100 governed skills and
[19:00] at least as many community skills that are looked after in a library and they're well governed. And what this has
[19:08] 19 minutes, 8 seconds done is it has allowed us to unlock the capability to use AI in systematic trading.
[19:21] 19 minutes, 21 seconds So skills governance really unlocks AI at that enterprise scale. The thing that I'm most proud of is that I feel that
[19:29] 19 minutes, 29 seconds we've got our eyes on the prize. We have a solid bedrock built on decades of institutional knowledge.
[19:38] 19 minutes, 38 seconds And in the not too distant future, I can see us having swarms of agents leveraging those skills to look for new investment opportunities.
[19:53] 19 minutes, 53 seconds So what's the takeaway for you?
[19:57] 19 minutes, 57 seconds Really think about how you're going to capture that context. Which department owns it?
[20:04] 20 minutes, 4 seconds What's the process for governing them?
[20:08] 20 minutes, 8 seconds Where will they live? How will you test them? How will you retire them?
[20:13] 20 minutes, 13 seconds connect a golden path from your AI platform to your capabilities and your context.
[20:21] 20 minutes, 21 seconds Once you have that basis of knowledge, if you care for it and AI can leverage it, that will really set you up for the agenda age.
[20:34] 20 minutes, 34 seconds Thank you very much everyone.
