---
title: Rethinking Agents - Harness is All you Need
video_id: A0xu44a1BHE
url: https://youtu.be/A0xu44a1BHE?si=4Zm9U1tpM5xQk4-B
channel: Prompt Engineering
channel_id: UCDq7SjbgRKty5TgGafW8Clg
channel_url: https://www.youtube.com/channel/UCDq7SjbgRKty5TgGafW8Clg
publish_date: '2026-05-04T06:45:03-07:00'
upload_date: '2026-05-04T06:45:03-07:00'
category: Science & Technology
duration: '14:13'
length_seconds: 853
view_count: 11686
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/A0xu44a1BHE/maxresdefault.webp
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: Harness Beats Model
  start: 0:00
  start_ms: 0
- title: What Is a Harness
  start: '1:12'
  start_ms: 0
- title: What's wrong with Harness Today
  start: '2:44'
  start_ms: 0
- title: Ablations and Compute Costs
  start: '4:02'
  start_ms: 0
- title: Natural Language Migration Win
  start: '5:25'
  start_ms: 0
- title: Sponsor Data Impulse
  start: '6:29'
  start_ms: 0
- title: Meta Harness Auto Optimization
  start: '8:02'
  start_ms: 0
- title: Transferable Harness Insight
  start: '10:00'
  start_ms: 0
- title: Subtraction Principle
  start: '11:31'
  start_ms: 0
- title: Audit Checklist for Builders
  start: '13:12'
  start_ms: 0
description: "Thanks to DataImpluse for sponsoring this video: https://dataimpulse.com/?utm_source=youtube&utm_medium=video&utm_campaign=engineerprompt\n\
  \nTwo new papers from Stanford and Tsinghua just put hard numbers on something most agent builders have\
  \ been feeling — the orchestration code wrapping your LLM now drives more performance variation than\
  \ the model itself. Same model, six-times the gap, depending entirely on what researchers are calling\
  \ the harness. If you build agents, the lever you should be pulling is almost never the one you've been\
  \ reaching for.\n\nLINKS:\nTsinghua University:  https://arxiv.org/abs/2603.25723\nStanford University:\
  \ https://arxiv.org/abs/2603.28052v1\n\nMy voice to text App: whryte.com\nWebsite: https://engineerprompt.ai/\n\
  RAG Beyond Basics Course:\nhttps://prompt-s-site.thinkific.com/courses/rag\nSignup for Newsletter, localgpt:\n\
  https://tally.so/r/3y9bb0\n\nLet's Connect: \n\U0001F9BE Discord: https://discord.com/invite/t4eYQRUcXB\n\
  ☕ Buy me a Coffee: https://ko-fi.com/promptengineering\n|\U0001F534 Patreon: https://www.patreon.com/PromptEngineering\n\
  \U0001F4BCConsulting: https://calendly.com/engineerprompt/consulting-call\n\U0001F4E7 Business Contact:\
  \ engineerprompt@gmail.com\nBecome Member: http://tinyurl.com/y5h28s6h\n\n\U0001F4BB Pre-configured\
  \ localGPT VM: https://bit.ly/localGPT (use Code: PromptEngineering for 50% off).  \n\nSignup for Newsletter,\
  \ localgpt:\nhttps://tally.so/r/3y9bb0\n\n\n00:00 Harness Beats Model\n01:12 What Is a Harness\n02:44\
  \ What's wrong with Harness Today\n04:02 Ablations and Compute Costs\n05:25 Natural Language Migration\
  \ Win\n06:29 Sponsor Data Impulse\n08:02 Meta Harness Auto Optimization\n10:00 Transferable Harness\
  \ Insight\n11:31 Subtraction Principle\n13:12 Audit Checklist for Builders"
notes: 'Re-fetched 2026-05-09 after skill fix landed (GH #2); rich metadata now populated. Body is the
  manually-cleaned transcript carried over verbatim from the original legacy file (the skill couldn''t
  extract the transcript itself on this video due to a separate engagement-panel-render bug noted in GH
  #2 follow-up; the transcript was manually copied from YouTube''s transcript panel by the user).'
---

0:00
Okay, so the orchestration code wrapping
0:02
your LLM now drives more performance
0:05
variation than the model itself. Same
0:08
model six times the performance gap
0:10
depending entirely on the wrapper or
0:12
harness around it. That's the headline
0:16
finding from two papers from Stanford
0:19
and Chinha University and it means that
0:22
the entire which model is the best
0:25
debate has been wrong question for a
0:27
while now. Now in this video I'm going
0:29
to walk you through three things. First
0:32
exactly what a harness is and why it
0:36
matters more than the model itself. Now
0:39
second the two papers from the Chinua
0:42
and Stanford that formalize this as a
0:46
discipline that is known as harness
0:48
engineering. And third, the practical
0:50
takeaways
0:52
uh what specifically you should change
0:55
about how you build agents starting
0:57
today. By the end of this video, you
1:00
will know exactly which levers to pull
1:03
when your agent is underperforming. And
1:06
I think you will find it's almost never
1:10
the lever you are reaching out for.
What Is a Harness
1:13
Okay, so let me break it down for you.
1:16
In simple terms, a harness is a
1:18
architecture that turns a model into an
1:21
agent. The agent itself is just a
1:24
oneshot text generator. You ask, it
1:27
answers, and then it stops. The harness
1:30
is what gives it the ability to take
1:32
actions, see the consequences, and keep
1:35
going until the problem is actually
1:37
solved. Now there is a really clean way
1:40
to think about this and it's an
1:43
operating system analogy. The raw LLM is
1:48
the CPU which is powerful but inert. No
1:51
memory, no storage, no IIO. Your context
1:55
window acts as RAM which is fast but
1:59
limited. External databases serve as
2:04
disk. Tool integrations are device
2:06
drivers and the harness is the operating
2:10
system deciding what the CPU sees and
2:14
when. And I think this analogy actually
2:16
maps really really cleanly onto the nine
2:19
harness components I covered in my
2:21
previous video. Now here is why this
2:25
matters for today's video. My previous
2:27
video answered what a harness is. What
2:31
this video is about is something
2:33
different. Why is the same harness
2:36
producing six times performance
2:38
differences depending on exactly how
2:41
those components are structured? Okay,
What's wrong with Harness Today
2:44
so let's look at the first paper and
2:47
this is where it gets really
2:49
interesting. The first paper is from Pan
2:52
and team and Shinua University which was
2:55
published in March 2026. They asked a
2:57
simple question. What if you could write
2:59
an agent's entire or control logic not
3:02
in Python not in YAML but in structured
3:07
natural language? The structure has
3:10
three layers at the bottom back end the
3:13
actual infrastructure and tools. in the
3:17
middle what they call the runtime
3:21
charter which is a universal physics
3:24
basically how contracts bind how state
3:27
persists how sub agents or child agents
3:31
are managed and on the top the natural
3:35
language agent harness itself which
3:37
holds the state specific logic these
3:40
include contracts roles state structure
3:43
and failure modes now why does this
3:46
separation ation matter. It [snorts]
3:48
gives harness engineering controlled
3:50
experimentation.
3:51
So you can swap the harness while fixing
3:54
the runtime and you are testing harness
3:57
design in isolation
3:59
which gives you clean ablation. Now
Ablations and Compute Costs
4:03
here's um where the results get
4:04
interesting. on SUB bench verified with
4:07
GPD54 at maximum reasoning. Uh the
4:11
result rate clustered around 74 and 76
4:15
persons regardless of the configuration
4:18
but the full harness burned 16.3 million
4:22
prompt tokens per sample. You're talking
4:25
about more than 600 tool calls with more
4:29
than 32 minutes runtime. But then they
4:32
stripped down a version of this which
4:36
used 1.2 million tokens, 51 calls under
4:39
7 minutes, same destination, 14 times
4:43
the compute for the same result. Uh they
4:47
did a module by module ablation which
4:50
means that they started removing or
4:53
subtracting parts of the system.
4:55
Self-evolution was the only consistently
4:58
helpful module. verifiers actually start
5:02
hurting. They saw minus.8 on Sweetbench,
5:06
minus 8.4 on OS World. So multicandidate
5:10
search hurt by 5.6. More structure is
5:14
not always better, which is kind of a
5:16
surprising result, but if you think
5:19
about it, it kind of makes sense. I'm
5:22
going to come back to this in the
5:23
practical takeaways. But the headline
Natural Language Migration Win
5:26
results from this paper came from a
5:28
different experiment. They took OS
5:31
symfony uh native code harness for
5:34
desktop automation and migrated its
5:37
logic into natural language
5:39
representation. Again they use the same
5:41
strategy uh but just rewritten in
5:45
natural language. And in this case
5:48
performance jumped from 30.4%
5:51
to 47.2%.
5:53
Run time dropped from 361 minutes to
5:58
41 minutes. LLM calls collapsed from
6:03
1200 to 34. The representation itself
6:07
drew the gain. That's a really really
6:09
significant finding. Now keep this in
6:12
mind. But let's look at this other paper
6:14
which was released by Omar Katab who
6:17
built DSP and they took it one step
6:21
further. If representation matters this
6:24
much, can we find the right harness
6:28
automatically?
Sponsor Data Impulse
6:29
A quick word from today's sponsor. If
6:32
you're building production systems that
6:34
need to access data available on the
6:36
web, whether it's a rack system or an
6:38
agentic system, you probably have
6:40
noticed that as you scale up, some of
6:43
the requests are going to be blocked. It
6:46
doesn't matter how good your logic is.
6:48
If the IP gets flagged, the data stops
6:52
moving. The fix is to have good proxies.
6:55
This is where today's sponsor, Data
6:56
Impulse, comes into play. The
6:58
residential pool is honestly hard to
7:01
beat on value. Pricing starts at a
7:05
dollar a gigabyte, and what you buy does
7:09
not expire. On top of that, over 90
7:12
million ethically sourced IPs across 195
7:16
different countries. If you're already
7:19
running Scrapey, Playright or Puppeteer,
7:22
they have got full integration guides on
7:24
each one right in their docs. So you can
7:27
wire their proxies straight into the
7:29
applications that you are already
7:30
building. And if your app needs mobile
7:33
traffic, you can swipe right over that.
7:36
There is a dedicated mobile pool and
7:38
your script barely changes. You're using
7:41
the same o same call a different
7:44
endpoint and you're routing through a
7:47
phone class IP. Link is going to be in
7:50
the description. If you're shipping a
7:52
data pipeline needs IPs in specific city
7:55
or you just want scrapping to stop being
7:58
a daily fight. Take a look. Now back to
8:01
the video again. It's structured
Meta Harness Auto Optimization
8:04
retrieval memory orchestration topology.
8:08
It controls everything. Now, here's how
8:11
the loop works. The agentic proposal uh
8:15
in this case they used cloud opus 46
8:19
reads failed execution traces, diagnoses
8:22
what broke and rewrites the complete new
8:25
harness. The final scores and rot traces
8:29
accumulate in a growing file system and
8:32
the loop repeats.
8:34
The scale here is what makes this work.
8:36
Uh we're looking at 10 million tokens
8:38
per iteration, 400 times more feedback
8:42
than any prior method. It's reading
8:44
about 82 files per round. And those raw
8:48
traces are irreplaceable.
8:51
When they removed them, accuracy dropped
8:55
from 50% to 34%. When they replaced
9:00
traces with summaries, 34.9%.
9:04
This signal lives in the raw details. If
9:08
you summarize prior failures and just
9:10
feed those into the model, it could hurt
9:15
the performance of your agent. Now the
9:18
results rank two with Opus rank with one
9:21
with Haik coup. So in this case a
9:23
smaller model outranking larger ones
9:26
through harness optimization alone. The
9:29
numbers are 76.4% on terminal bench 2.
9:33
The only autooptimized system in a field
9:37
of hand engineer entries on a 215 text
9:41
classification. It was scoring 7.7
9:45
points above state-of-the-art using four
9:48
times fewer tokens. But here's the
9:51
finding that I think is going to be
9:52
significant. A harness optimized on one
9:55
model transferred to five other models
9:59
and improving them all. So think about
Transferable Harness Insight
10:02
this and what exactly does this mean?
10:05
The reusable asset is not the model,
10:08
it's the harness. You can build it once.
10:11
It works across the model landscape.
10:14
Now, I don't want to generalize it too
10:16
much. Now, this all might sound academic
10:18
until you map it onto something you have
10:22
probably already noticed yourself. Take
10:25
any Frontier model, say Claude Opus 46
10:30
or 47, GBD54 or even Gemini, doesn't
10:34
matter which. run the exact same prompt
10:39
through it inside cloud code, then
10:41
cursor, then anti-gravity. And the idea
10:44
is that you keep the model exactly the
10:46
same. You just change the harness. Now,
10:48
the prompt needs to be relatively
10:50
complex, but you're going to see
10:52
noticeably different results. You're
10:55
going to see different reasoning paths
10:58
with different token spends and
11:00
potentially different success rates. And
11:03
all of this is driven by not the model
11:05
but the harness that you are using with
11:08
the agent. Opus 47
11:12
behaves very differently in cloud code
11:16
than inside cursor or other third party
11:20
harnesses like open code. Okay. So the
11:23
most important uh practical takeaway
11:24
from all this and the one I think most
11:27
builders are getting wrong is what
11:30
enthropic calls the subtraction
Subtraction Principle
11:32
principle. So every harness components
11:35
and remember in my last video we walked
11:38
through nine of them encodes an
11:40
assumption about what the model cannot
11:43
do alone and those assumption expires
11:46
when the models improve. When Opus 46
11:50
stopped needing context resets,
11:53
Anthropic just dropped them entirely.
11:56
Manis, the agent platform, rewrote their
12:00
harness five times in 6 months. Warel
12:04
removed 80% of the agents tool and got
12:06
better results. That is pretty
12:09
significant.
12:11
Now, here's what it means. Mature
12:13
harness work looks less like building
12:17
structure up and more like pruning it
12:19
down. In the last year, the idea was to
12:23
provide agents more and more tools, but
12:26
that is going away. Simpler is much
12:30
better. A craft of subtraction as much
12:34
as addition. Shinua ablation we just
12:37
looked at really proves this. Sometimes
12:40
the verifier can actually hurt your
12:44
agent a lot more than it can help. The
12:46
way you want to think about it is that
12:49
if the model is able to do
12:52
uh an aspect that was handcrafted in the
12:56
harness before, you want to simplify
12:58
your harness and drop that specific
13:02
tool. Now um if you are building an
13:04
agent, you are a harness engineer
13:07
whether you call yourself or not. So
13:09
when you run into something that is not
Audit Checklist for Builders
13:12
working, here is the order of operations
13:14
I would suggest. Don't switch the model
13:17
first. Audit the harness. And here are
13:22
four questions that you can ask
13:23
yourself. One, what's in your context
13:27
window that does not need to be there?
13:30
Two, which tool do you have that the
13:33
agent rarely uses? as well. Three, are
13:37
you adding verification or search loops
13:39
that might be hurting performance like
13:42
the Shenha University found? And four,
13:46
is your control logic written in code or
13:48
in language? Because the migration
13:51
experiment we looked at before showed
13:54
almost 17 point points gain just from
13:57
rewriting the same logic. And it's no
14:01
longer a question of which model to
14:02
pick, it's a question of which structure
14:05
to remove. Anyways, I hope you found
14:08
this video useful. Thanks for watching
14:10
and I'll see you in the next one.