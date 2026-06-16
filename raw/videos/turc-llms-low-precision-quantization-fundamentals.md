---
title: How LLMs survive in low precision | Quantization Fundamentals
video_id: qoQJq5UwV1c
url: https://www.youtube.com/watch?v=qoQJq5UwV1c
channel: Julia Turc
channel_id: UCMUy_WsUIYbM_hKR9drb9dA
channel_url: https://www.youtube.com/channel/UCMUy_WsUIYbM_hKR9drb9dA
publish_date: '2025-05-17T06:01:34-07:00'
upload_date: '2025-05-17T06:01:34-07:00'
category: Science & Technology
duration: '20:34'
length_seconds: 1234
view_count: 54384
is_live: false
is_upcoming: false
is_private: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi/qoQJq5UwV1c/maxresdefault.jpg
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
available_countries:
- AD
- AE
- AF
- AG
- AI
- AL
- AM
- AO
- AQ
- AR
- AS
- AT
- AU
- AW
- AX
- AZ
- BA
- BB
- BD
- BE
- BF
- BG
- BH
- BI
- BJ
- BL
- BM
- BN
- BO
- BQ
- BR
- BS
- BT
- BV
- BW
- BY
- BZ
- CA
- CC
- CD
- CF
- CG
- CH
- CI
- CK
- CL
- CM
- CN
- CO
- CR
- CU
- CV
- CW
- CX
- CY
- CZ
- DE
- DJ
- DK
- DM
- DO
- DZ
- EC
- EE
- EG
- EH
- ER
- ES
- ET
- FI
- FJ
- FK
- FM
- FO
- FR
- GA
- GB
- GD
- GE
- GF
- GG
- GH
- GI
- GL
- GM
- GN
- GP
- GQ
- GR
- GS
- GT
- GU
- GW
- GY
- HK
- HM
- HN
- HR
- HT
- HU
- ID
- IE
- IL
- IM
- IN
- IO
- IQ
- IR
- IS
- IT
- JE
- JM
- JO
- JP
- KE
- KG
- KH
- KI
- KM
- KN
- KP
- KR
- KW
- KY
- KZ
- LA
- LB
- LC
- LI
- LK
- LR
- LS
- LT
- LU
- LV
- LY
- MA
- MC
- MD
- ME
- MF
- MG
- MH
- MK
- ML
- MM
- MN
- MO
- MP
- MQ
- MR
- MS
- MT
- MU
- MV
- MW
- MX
- MY
- MZ
- NA
- NC
- NE
- NF
- NG
- NI
- NL
- 'NO'
- NP
- NR
- NU
- NZ
- OM
- PA
- PE
- PF
- PG
- PH
- PK
- PL
- PM
- PN
- PR
- PS
- PT
- PW
- PY
- QA
- RE
- RO
- RS
- RU
- RW
- SA
- SB
- SC
- SD
- SE
- SG
- SH
- SI
- SJ
- SK
- SL
- SM
- SN
- SO
- SR
- SS
- ST
- SV
- SX
- SY
- SZ
- TC
- TD
- TF
- TG
- TH
- TJ
- TK
- TL
- TM
- TN
- TO
- TR
- TT
- TV
- TW
- TZ
- UA
- UG
- UM
- US
- UY
- UZ
- VA
- VC
- VE
- VG
- VI
- VN
- VU
- WF
- WS
- YE
- YT
- ZA
- ZM
- ZW
thumbnails:
- url: https://i.ytimg.com/vi/qoQJq5UwV1c/hqdefault.jpg?sqp=-oaymwEmCKgBEF5IWvKriqkDGQgBFQAAiEIYAdgBAeIBCggYEAIYBjgBQAE=&rs=AOn4CLBmI7bqhrJy-y4hFQVVyomIv8IBHg
  width: 168
  height: 94
- url: https://i.ytimg.com/vi/qoQJq5UwV1c/hqdefault.jpg?sqp=-oaymwEmCMQBEG5IWvKriqkDGQgBFQAAiEIYAdgBAeIBCggYEAIYBjgBQAE=&rs=AOn4CLD-j7TiZkwUiU6ZwG3g1MfeAg3zsw
  width: 196
  height: 110
- url: https://i.ytimg.com/vi/qoQJq5UwV1c/hqdefault.jpg?sqp=-oaymwEnCPYBEIoBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAudyJPvO8AM5SIhKPaZ1YAV8o0_g
  width: 246
  height: 138
- url: https://i.ytimg.com/vi/qoQJq5UwV1c/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD6sdtMY0LG3HvfJdvQD7LwI8zfAw
  width: 336
  height: 188
- url: https://i.ytimg.com/vi/qoQJq5UwV1c/maxresdefault.jpg
  width: 1920
  height: 1080
chapters:
- title: Intro
  start: 0:00
  start_ms: 0
- title: What
  start: 0:50
  start_ms: 0
- title: When
  start: '6:45'
  start_ms: 0
- title: How
  start: '9:21'
  start_ms: 0
- title: Fixed point arithmetic
  start: '14:40'
  start_ms: 0
- title: Matrix multiplications
  start: '18:00'
  start_ms: 0
- title: Outro
  start: '20:07'
  start_ms: 0
description: |-
  In this video, we discuss the fundamentals of model quantization, the technique that allows us to run inference on massive LLMs like DeepSeek-R1 or Qwen.

  Among others, we'll discuss:
  ⚆ What quantization really means (hint: it’s more than just rounding)
  ⚆ Why integers are faster than floats (with a deep dive into their internal structure)
  ⚆ How quantization preserves model accuracy
  ⚆ When to quantize: during training vs after training (PTQ vs QAT)
  ⚆ A hands-on explanation of scale, zero point, clipping ranges, and fixed-point math

  If you enjoyed this, consider subscribing for upcoming videos on:
  ⚆ Post-training quantization (PTQ)
  ⚆ Quantization-aware training (QAT)
  ⚆ Training in low precision (e.g., FP4)
  ⚆ 1-bit LLMs

  #Quantization #MachineLearning #AIOptimization #LLM #NeuralNetworks #QAT #PTQ #DeepLearning #EdgeAI #FixedPoint #BFloat16 #TensorRT #ONNX #AIAccelerators

  00:00 Intro
  00:50 What
  02:10: Why
  03:50: Integer vs floating point formats
  06:45 When
  09:21 How
  14:40 Fixed point arithmetic
  18:00 Matrix multiplications
  20:07 Outro
playability:
  status: OK
  reason: null
---

## [0:00] Intro


## [0:50] What


## [6:45] When


## [9:21] How


## [14:40] Fixed point arithmetic


## [18:00] Matrix multiplications


## [20:07] Outro

[0:00] Quantization is what allows us to run
[0:02] massive models like Deepseek R1 on just
[0:06] two GPUs and deploy AI models on edge
[0:09] devices that don't even support
[0:11] floatingoint
[0:12] operations. If you watch the Severance
[0:15] TV show, quantization is a little bit
[0:17] like working for the MDR department. We
[0:20] take real values, we put them into
[0:23] buckets, and never really understand
[0:25] what they
[0:26] mean. Because quantization is a big
[0:29] topic, I'm splitting it into multiple
[0:31] parts. This video covers the basics.
[0:34] Why, when, and how. In future videos,
[0:38] we'll dive deeper into topics like one
[0:41] bit LLM, quantization aware training,
[0:44] post-raining quantization, and so on.
[0:47] But for now, let's start with the
[0:49] basics. Quantization is the process of
[0:52] mapping a continuous space to a discrete
[0:55] one. Consider all the real values
[0:58] between 0 and 1. To quantize this
[1:00] interval, we can split it into 10
[1:03] equally sized buckets. For instance, all
[1:06] the real values between 04 and.5 fall
[1:09] into bucket number four. Quantization
[1:12] was first used in signal processing,
[1:15] turning real world waveforms like sound
[1:18] into digital data. So given a physical
[1:21] soundwave with varying amplitude over
[1:24] time, we normally use a microphone to
[1:27] sample the amplitude at regular
[1:30] intervals. Sampling is already a form of
[1:32] quantization. We can't measure the
[1:35] signal at every infinite decimal moment.
[1:38] So it takes snapshots instead. A second
[1:40] form of quantization is rounding the
[1:43] amplitude to the closest value that can
[1:45] be represented in a computer system.
[1:48] In machine learning, quantization
[1:50] converts the model weights and sometimes
[1:53] activations from real values to
[1:56] integers. Here, my original model
[1:58] parameters are values between minus1 and
[2:01] 1. But in my quantized model, values
[2:04] range from minus 128 to +
[2:08] 127. This might sound very strange at
[2:11] first. Why would we want to work with
[2:13] integers? And how do we preserve the
[2:15] integrity of the model output in this
[2:17] integer space? Well, by the end of the
[2:20] video, you'll have an answer to both of
[2:21] these questions. So, let's start with
[2:24] the why. Obviously, modern LLMs are
[2:28] massive. Deepseek R1, the largest open
[2:31] weights model today, has a total of
[2:35] 671 billion parameters. In its original
[2:38] floatingpoint precision, that's about
[2:41] 720 GB. Granted, it uses a mixture of
[2:45] experts architecture, so only a subset
[2:47] of its parameters are active at once,
[2:50] but we often still need to load the
[2:52] entire model in memory for inference.
[2:55] Quantization can shrink that footprint
[2:57] by over 80% down to 131 GB, which is
[3:02] small enough to fit across two Nvidia
[3:04] H100 GPUs. So long story short,
[3:08] quantization is a method for model
[3:10] compression and faster inference. But it
[3:13] doesn't just apply to large language
[3:15] models deployed on powerful
[3:17] accelerators. At the other end of the
[3:19] spectrum, it enables machine learning on
[3:22] edge devices. Consider, for instance,
[3:25] Google's Coral Edge TPU, a processor
[3:28] found in IoT devices like sensors or
[3:31] smart cameras. It was optimized for low
[3:34] power consumption and doesn't even
[3:36] support floatingoint operations at all.
[3:40] So the only way to locally deploy your
[3:43] porch pirate detection model would be to
[3:45] quantize it into 8 bits integers. So why
[3:49] are integers so special? Why can we get
[3:52] away with fewer bits and fewer
[3:55] kilowatts? Well, their efficiency stems
[3:57] from their very straightforward
[3:59] representation.
[4:01] An unsigned integer simply stores a
[4:04] number in base 2. Signed integers are
[4:07] just as efficient with no additional
[4:09] overhead other than using a bit to store
[4:12] the sign. This is due to a format
[4:15] everyone embraced back in the 1960s
[4:18] called TW's complement. If you're
[4:21] interested, you can find more details on
[4:23] Wikipedia. The simple representation
[4:26] leads to efficient operations. For
[4:28] instance, adding two integers is a
[4:30] trivial bitwise exor operation with
[4:33] carryover. On modern CPUs, this
[4:36] instruction typically completes in a
[4:38] single clock
[4:39] cycle. Floating numbers, on the other
[4:42] hand, are more complex. They store a
[4:45] sign, an exponent, and the significant,
[4:48] also called mantisa. These components
[4:51] come together in a formula that somewhat
[4:53] resembles the scientific notation but
[4:56] with some extra quirks like this one
[4:59] which makes up for something called a
[5:01] hidden bit or this bias which ends up
[5:05] giving us an extra bit of precision. You
[5:08] don't need to worry about these details.
[5:10] Just take a moment to appreciate the
[5:12] complexity of this
[5:13] representation. Also, not everyone
[5:16] agrees how to divide the bits across
[5:18] these components.
[5:20] There are multiple recognized standards,
[5:22] each making a different tradeoff. What
[5:25] you see here is the ILE E standard, the
[5:28] most common general purpose format. But
[5:30] you might also have heard of Bflat 16.
[5:33] This was introduced by Google Brain,
[5:35] hence the B specifically for machine
[5:38] learning. It allocates more bits to the
[5:40] exponent, which increases something
[5:42] called the dynamic range or the ability
[5:46] to represent numbers at different orders
[5:48] of magnitude. This turns out to be
[5:50] important for training models where we
[5:52] want the ability to represent very low
[5:54] numbers in the vicinity of zero.
[5:57] Needless to say, floatingoint operations
[5:59] are more involved than integer
[6:02] operations. Adding two floats requires a
[6:04] bunch of steps. Aligning the exponents,
[6:07] add the significance, normalize the
[6:09] results, and so on. On modern CPUs, this
[6:13] instruction can take three or even four
[6:15] clock cycles.
[6:18] So quantization enables us to store the
[6:21] model weights and activations into a
[6:23] more efficient format. This leads to
[6:26] smaller models, less memory usage, and
[6:29] faster inference. But of course, there's
[6:32] no free lunch. So it comes at the cost
[6:34] of precision. We know we can throw away
[6:37] some precision because models come with
[6:39] built-in redundancy, but it's always a
[6:42] tricky balance to strike. Now let's talk
[6:45] about the when. When exactly in the
[6:47] lifetime of a model does quantization
[6:50] happen. Obviously, the two big
[6:53] milestones are training and deployment
[6:55] or inference. During training, there's
[6:58] no way to avoid real values. Calculating
[7:01] the gradients and model updates require
[7:04] fine grain precision. Historically,
[7:07] models were trained in full precision or
[7:09] floating point 32. Throughout the years,
[7:12] we've been striving to make do with less
[7:15] precision so that we can speed up the
[7:17] training process. Today, we mostly train
[7:20] in half precision or floatingoint 16
[7:22] enabled by Google's Bloat 16 format.
[7:25] Recent LLMs like Deepsee R1 and Llama 4
[7:28] managed to train in floating point 8.
[7:30] Though the mechanics are not well
[7:32] understood publicly, there's a natural
[7:35] end to this trend and it's unlikely that
[7:37] gradient descend will allow us to go
[7:38] much lower. Inference on the other hand
[7:41] which only consists of a forward pass is
[7:44] more resilient to the loss in precision.
[7:46] People have successfully run inference
[7:48] in integer precision as low as 8, four
[7:51] or even one bit. So a natural point to
[7:55] insert quantization is right after model
[7:58] training and before deployment. This
[8:00] choice is known as postraining
[8:03] quantization or PTQ. This is the case
[8:06] for most open weights LLM today. Some
[8:09] providers like Meta and DeepSeek publish
[8:12] their models only in their original
[8:14] floatingpoint format. Then open source
[8:17] communities and infrastructure companies
[8:19] like Unsloth pick them up and quantize
[8:22] them. But other providers like Quen do
[8:25] publish quantized versions of their
[8:27] models. You'll recognize them by
[8:29] suffixes like GGUF, GBTQ, or AWQ. I'll
[8:33] go into more detail in a future video
[8:35] specifically dedicated to post-training
[8:39] quantization. Sometimes we build models
[8:41] with the foresight that they will
[8:43] eventually be quantized. In this case,
[8:46] we can tweak the training process so
[8:48] that when quantization time does come
[8:51] right before deployment, the model is
[8:53] more resilient to the loss in precision.
[8:56] This is known as quantizationaware
[8:58] training or QAT for short. Extreme
[9:02] quantization down to four bits or lower
[9:05] is very likely to require this in order
[9:07] to avoid significant degradation in
[9:10] model
[9:10] performance. This is how the famous one
[9:13] bit LLMs are trained. It's a really
[9:15] interesting research topic. Stay tuned
[9:17] for a separate video on
[9:19] it. Now let's talk about the how. How do
[9:23] we turn floats into integers, float
[9:25] operations into integer operations? And
[9:29] how do we preserve the integrity of the
[9:30] model in integer
[9:32] space? The exact formula that converts a
[9:35] float into an integer is called the
[9:37] quantization scheme or quantization
[9:41] paradigm. Let's take a concrete example
[9:43] where we quantize a float 16 number into
[9:46] an int4. The standard signed integer
[9:49] representation that we already discussed
[9:51] 2's complement encodes an asymmetric
[9:54] interval for int 4. That's -8 to 7.
[9:58] Quadization frameworks often disregard
[10:00] the extra negative bucket to get a
[10:03] symmetric range. Of course, float 16 can
[10:06] represent a wide range of numbers, but
[10:08] the values in a neural network are
[10:10] typically in a narrow range between some
[10:12] values alpha and beta. This is called
[10:15] the clipping range. The process of
[10:17] determining alpha and beta by finding
[10:19] the minimum and maximum values flowing
[10:22] through the network is called
[10:23] calibration. Calibration is easy for
[10:26] parameters but non-trivial for
[10:29] activations. For the latter, we need to
[10:31] run inference on a calibration data set
[10:33] which depending on the size of the model
[10:35] and your hardware can take a few minutes
[10:37] to a few hours. For symmetric clipping
[10:40] ranges like minus1 to 1, the process is
[10:43] called symmetric quantization. This is
[10:46] the most straightforward case. So
[10:48] defining a quantization scheme means
[10:51] figuring out what bucket each real value
[10:53] falls into. We'll first compute the
[10:56] relative scale s of the two ranges as
[10:59] the ratio between their lengths. Now
[11:01] given a value r say 42, quantization
[11:05] means dividing r by the scale s and
[11:08] rounding to the closest integer which is
[11:11] three in this case. Sometimes the
[11:13] clipping range can be asymmetric. This
[11:16] can be caused by operations like relu
[11:18] which have strictly positive outputs and
[11:21] therefore skew the overall distribution
[11:23] of the model
[11:25] activations. Let's figure out how the
[11:27] mapping changes in this case. Trivially
[11:30] alpha should go into the leftmost bucket
[11:32] and beta into the rightmost. Then
[11:34] naturally zero will fall 1/3 of the way
[11:37] in between them. Its host bucket in this
[11:40] case minus2 is known as the zero point
[11:43] and is denoted by z. It acts as an
[11:46] offset for our previous mapping. So just
[11:49] as before, we'll compute the scale and
[11:52] our value r now maps to bucket number
[11:55] two. But this time we'll shift left by
[11:58] two positions as indicated by the zero
[12:01] point. So the final quantized value of
[12:04] 42 is now zero. We'll denote it by Q.
[12:09] Now let's formalize this. Here's a
[12:11] closed form expression for the zero
[12:13] point. The easiest way to see it is to
[12:16] think of s as this length and minus
[12:19] alpha as this length in terms of how
[12:22] much real space they cover. Their ratio
[12:26] tells us how many s hops from the left
[12:29] are needed to reach the zero bucket.
[12:32] That's 1 2 3 4 5. And then we'll add Q
[12:38] min which is minus 7 to finally get
[12:41] minus2.
[12:43] Now we can get an expression for the
[12:45] quantization process which reflects how
[12:48] we turned 42 into zero. And finally we
[12:52] can also define the reverse process of
[12:54] mapping Q back into a real value. This
[12:57] is called
[12:58] dequantization. Of course we can only
[13:00] recover an approximation of the original
[13:03] value R in this case4 because we cannot
[13:07] undo the entire damage of the rounding
[13:09] operation.
[13:12] So now we have a quantization scheme
[13:14] that maps real values to integers. But
[13:17] quantizing the model weights is only
[13:19] part of the story. Running inference
[13:22] means executing operations which also
[13:24] need to be translated from real to
[13:27] integer space. Let's start with
[13:29] something basic. Multiplying two scalers
[13:32] R1 and R2 into a product R3. So what
[13:36] does this look like in integer space? We
[13:39] start by quantizing the operants R1 into
[13:43] Q1 and R2 into Q2. Now what function f
[13:48] should we apply to recover the product
[13:50] but in integer space? Ideally
[13:53] quantization followed by dequantization
[13:56] is almost a noop. We want the
[13:59] dequantized values to preserve the
[14:01] original
[14:02] relationship. With this property in
[14:05] mind, let's work out what f is. We can
[14:08] apply the dq1 formula to each value and
[14:11] then rearrange to solve for q3. This
[14:15] expression is our function f. Now by
[14:19] construction, z is an integer. So adding
[14:22] or subtracting it is trivial. However,
[14:25] remember that the scale is a real value.
[14:28] So how can we implement this
[14:30] multiplication in a way that doesn't
[14:32] defeat the whole purpose of
[14:33] quantization? Because multiplying by a
[14:36] floatingoint number is what we're trying
[14:38] to escape in the first place. The trick
[14:41] is called fixed point arithmetic, a way
[14:44] to represent fractions using only
[14:47] integers. For example, to represent a
[14:50] value like
[14:52] $12.34, we could instead store it as
[14:56] $1,234 and keep track of the scale. That
[15:00] means to recover the original value,
[15:03] we'd have to divide by 100. So fixed
[15:07] point means the decimal point doesn't
[15:09] float. We fixed it two positions from
[15:12] the right. In practice, we don't use
[15:14] base 10 for the scale. We use powers of
[15:17] two instead. So if we have an unsigned
[15:20] integer with four bits, then the
[15:23] smallest step size we can represent is 2
[15:25] to the^ minus4.
[15:27] So the stored value is our dollar amount
[15:30] multiplied by the inverse of the scale
[15:32] and rounded to the nearest integer.
[15:35] That's 197 in this case. Just to
[15:38] establish some notation for an actual
[15:41] value v, I'll use vend for its stored
[15:44] value in fixed
[15:46] point. So how can we leverage fixed
[15:49] point arithmetic to multiply an integer
[15:51] x by a real value s and get an integer y
[15:56] in return?
[15:57] Your first instinct might be just store
[16:00] s as a fixed point number and perform
[16:02] the multiplication with fixed point
[16:05] arithmetic. But that's not quite right.
[16:08] If it were this easy, we wouldn't bother
[16:10] with quantization and just use fixed
[16:13] point instead of floating point from the
[16:15] get- go. The main problem is there's too
[16:18] much loss in precision. If s is a
[16:21] relatively small value like
[16:23] 0.003, it ends up rounded to zero. So
[16:26] the final product y would also be
[16:29] zero. Instead we express s as the
[16:33] product between a negative power of two
[16:36] and some other real value as zero.
[16:40] Intuitively what we're doing here is
[16:43] absorbing a lot of the precision into
[16:46] this negative power of two so that the
[16:49] leftover s0 is by choice higher than.5.
[16:56] If we store s0 as a fixed point number,
[16:59] we're not so concerned by the loss in
[17:01] precision anymore because we know it's a
[17:03] fairly large number. We chose it to be
[17:06] this way. So multiplying x * s
[17:10] translates to a integer multiplication
[17:14] followed by some bit
[17:16] shifts. Also as an optimization we can
[17:20] premputee the decomposition of s only
[17:23] once before deploying the
[17:25] model. So now that we know how to handle
[17:28] this multiplication by s in integer
[17:30] space, we have a full recipe for
[17:33] quantized multiplication of two scalers.
[17:35] But as you probably know, scalar
[17:37] multiplication is not the building block
[17:39] of deep learning. Matrix multiplication
[17:42] is. In the matrix world, the exact same
[17:46] principles apply, except that
[17:48] quantization and dequantization are
[17:51] applied to each value in the matrix. To
[17:54] work out what matrix multiply looks like
[17:56] in integer space, we'll use its
[17:58] definition to generalize the expression
[18:01] we deduced for the scalar case. And we
[18:04] end up with a very similar formula with
[18:06] this extra sum over all the entries in a
[18:09] row. In matrix multiplication,
[18:12] efficiency gains become much clearer.
[18:15] Under the hood, it requires m * n * p
[18:19] multiplications where mn and p are the
[18:22] dimensions of the matrices. In a modern
[18:24] LLM like llama 4, where we find matrices
[18:27] of size 4,000x 4,000, that's 10 billion
[18:31] operations that we implemented more
[18:34] effectively. And here is another subtle
[18:36] optimization. The scale S only needs to
[18:39] be applied once per output row as
[18:41] opposed to every entry and that's only a
[18:43] few thousand times for a matrix. So when
[18:46] the hardware allows it, certain
[18:48] quantization implementations actually
[18:51] perform the scale multiplication in
[18:53] floating point. On modern GPUs like
[18:56] Nvidia, float and int multiplications
[18:59] can be similarly fast. And in those
[19:01] cases, the real bottleneck isn't really
[19:04] compute, it's memory bandwidth. And the
[19:07] real gain from quantization is the
[19:09] reduced bit
[19:11] width. So far we made the assumption
[19:13] that we work with a single pair of
[19:16] quantization constants S and Z across
[19:19] the entire network. But in practice it's
[19:22] common to have multiple sets of
[19:24] constants. The granularity can vary. It
[19:27] can be per layer, per matrix, or even
[19:30] per matrix row. And this granularity
[19:33] applies both to weights and
[19:36] activations. Hopefully this gave you a
[19:38] solid understanding of how quantization
[19:40] arithmetic translates between real
[19:42] valued and integer space. In practice,
[19:46] you probably won't have to implement
[19:47] these low-level tricks yourself. Most ML
[19:50] frameworks like PyTorch and TensorFlow
[19:53] offer built-in support for quantization.
[19:55] And for deployment inference engines
[19:58] like the Onyx runtime or Nvidia Tensor
[20:01] RT apply even more aggressive hardware
[20:04] specific optimizations under the hood.
[20:07] Hopefully this video gave you a solid
[20:09] intuition on how quantization works. If
[20:12] that's the case, consider sharing or
[20:14] commenting because it really helps me
[20:16] keep these videos hype free and
[20:18] clickbait free without getting buried by
[20:20] the YouTube algorithm. As usual, my
[20:23] slide deck and my reading list are
[20:25] available on Patreon. Stay tuned for
[20:28] more in-depth quantization videos as
[20:30] part of this minieries. Thanks for
[20:32] watching.
[0:00] Quantization is what allows us to run
[0:02] massive models like Deepseek R1 on just
[0:06] two GPUs and deploy AI models on edge
[0:09] devices that don't even support
[0:11] floatingoint
[0:12] operations. If you watch the Severance
[0:15] TV show, quantization is a little bit
[0:17] like working for the MDR department. We
[0:20] take real values, we put them into
[0:23] buckets, and never really understand
[0:25] what they
[0:26] mean. Because quantization is a big
[0:29] topic, I'm splitting it into multiple
[0:31] parts. This video covers the basics.
[0:34] Why, when, and how. In future videos,
[0:38] we'll dive deeper into topics like one
[0:41] bit LLM, quantization aware training,
[0:44] post-raining quantization, and so on.
[0:47] But for now, let's start with the
[0:49] basics. Quantization is the process of
[0:52] mapping a continuous space to a discrete
[0:55] one. Consider all the real values
[0:58] between 0 and 1. To quantize this
[1:00] interval, we can split it into 10
[1:03] equally sized buckets. For instance, all
[1:06] the real values between 04 and.5 fall
[1:09] into bucket number four. Quantization
[1:12] was first used in signal processing,
[1:15] turning real world waveforms like sound
[1:18] into digital data. So given a physical
[1:21] soundwave with varying amplitude over
[1:24] time, we normally use a microphone to
[1:27] sample the amplitude at regular
[1:30] intervals. Sampling is already a form of
[1:32] quantization. We can't measure the
[1:35] signal at every infinite decimal moment.
[1:38] So it takes snapshots instead. A second
[1:40] form of quantization is rounding the
[1:43] amplitude to the closest value that can
[1:45] be represented in a computer system.
[1:48] In machine learning, quantization
[1:50] converts the model weights and sometimes
[1:53] activations from real values to
[1:56] integers. Here, my original model
[1:58] parameters are values between minus1 and
[2:01] 1. But in my quantized model, values
[2:04] range from minus 128 to +
[2:08] 127. This might sound very strange at
[2:11] first. Why would we want to work with
[2:13] integers? And how do we preserve the
[2:15] integrity of the model output in this
[2:17] integer space? Well, by the end of the
[2:20] video, you'll have an answer to both of
[2:21] these questions. So, let's start with
[2:24] the why. Obviously, modern LLMs are
[2:28] massive. Deepseek R1, the largest open
[2:31] weights model today, has a total of
[2:35] 671 billion parameters. In its original
[2:38] floatingpoint precision, that's about
[2:41] 720 GB. Granted, it uses a mixture of
[2:45] experts architecture, so only a subset
[2:47] of its parameters are active at once,
[2:50] but we often still need to load the
[2:52] entire model in memory for inference.
[2:55] Quantization can shrink that footprint
[2:57] by over 80% down to 131 GB, which is
[3:02] small enough to fit across two Nvidia
[3:04] H100 GPUs. So long story short,
[3:08] quantization is a method for model
[3:10] compression and faster inference. But it
[3:13] doesn't just apply to large language
[3:15] models deployed on powerful
[3:17] accelerators. At the other end of the
[3:19] spectrum, it enables machine learning on
[3:22] edge devices. Consider, for instance,
[3:25] Google's Coral Edge TPU, a processor
[3:28] found in IoT devices like sensors or
[3:31] smart cameras. It was optimized for low
[3:34] power consumption and doesn't even
[3:36] support floatingoint operations at all.
[3:40] So the only way to locally deploy your
[3:43] porch pirate detection model would be to
[3:45] quantize it into 8 bits integers. So why
[3:49] are integers so special? Why can we get
[3:52] away with fewer bits and fewer
[3:55] kilowatts? Well, their efficiency stems
[3:57] from their very straightforward
[3:59] representation.
[4:01] An unsigned integer simply stores a
[4:04] number in base 2. Signed integers are
[4:07] just as efficient with no additional
[4:09] overhead other than using a bit to store
[4:12] the sign. This is due to a format
[4:15] everyone embraced back in the 1960s
[4:18] called TW's complement. If you're
[4:21] interested, you can find more details on
[4:23] Wikipedia. The simple representation
[4:26] leads to efficient operations. For
[4:28] instance, adding two integers is a
[4:30] trivial bitwise exor operation with
[4:33] carryover. On modern CPUs, this
[4:36] instruction typically completes in a
[4:38] single clock
[4:39] cycle. Floating numbers, on the other
[4:42] hand, are more complex. They store a
[4:45] sign, an exponent, and the significant,
[4:48] also called mantisa. These components
[4:51] come together in a formula that somewhat
[4:53] resembles the scientific notation but
[4:56] with some extra quirks like this one
[4:59] which makes up for something called a
[5:01] hidden bit or this bias which ends up
[5:05] giving us an extra bit of precision. You
[5:08] don't need to worry about these details.
[5:10] Just take a moment to appreciate the
[5:12] complexity of this
[5:13] representation. Also, not everyone
[5:16] agrees how to divide the bits across
[5:18] these components.
[5:20] There are multiple recognized standards,
[5:22] each making a different tradeoff. What
[5:25] you see here is the ILE E standard, the
[5:28] most common general purpose format. But
[5:30] you might also have heard of Bflat 16.
[5:33] This was introduced by Google Brain,
[5:35] hence the B specifically for machine
[5:38] learning. It allocates more bits to the
[5:40] exponent, which increases something
[5:42] called the dynamic range or the ability
[5:46] to represent numbers at different orders
[5:48] of magnitude. This turns out to be
[5:50] important for training models where we
[5:52] want the ability to represent very low
[5:54] numbers in the vicinity of zero.
[5:57] Needless to say, floatingoint operations
[5:59] are more involved than integer
[6:02] operations. Adding two floats requires a
[6:04] bunch of steps. Aligning the exponents,
[6:07] add the significance, normalize the
[6:09] results, and so on. On modern CPUs, this
[6:13] instruction can take three or even four
[6:15] clock cycles.
[6:18] So quantization enables us to store the
[6:21] model weights and activations into a
[6:23] more efficient format. This leads to
[6:26] smaller models, less memory usage, and
[6:29] faster inference. But of course, there's
[6:32] no free lunch. So it comes at the cost
[6:34] of precision. We know we can throw away
[6:37] some precision because models come with
[6:39] built-in redundancy, but it's always a
[6:42] tricky balance to strike. Now let's talk
[6:45] about the when. When exactly in the
[6:47] lifetime of a model does quantization
[6:50] happen. Obviously, the two big
[6:53] milestones are training and deployment
[6:55] or inference. During training, there's
[6:58] no way to avoid real values. Calculating
[7:01] the gradients and model updates require
[7:04] fine grain precision. Historically,
[7:07] models were trained in full precision or
[7:09] floating point 32. Throughout the years,
[7:12] we've been striving to make do with less
[7:15] precision so that we can speed up the
[7:17] training process. Today, we mostly train
[7:20] in half precision or floatingoint 16
[7:22] enabled by Google's Bloat 16 format.
[7:25] Recent LLMs like Deepsee R1 and Llama 4
[7:28] managed to train in floating point 8.
[7:30] Though the mechanics are not well
[7:32] understood publicly, there's a natural
[7:35] end to this trend and it's unlikely that
[7:37] gradient descend will allow us to go
[7:38] much lower. Inference on the other hand
[7:41] which only consists of a forward pass is
[7:44] more resilient to the loss in precision.
[7:46] People have successfully run inference
[7:48] in integer precision as low as 8, four
[7:51] or even one bit. So a natural point to
[7:55] insert quantization is right after model
[7:58] training and before deployment. This
[8:00] choice is known as postraining
[8:03] quantization or PTQ. This is the case
[8:06] for most open weights LLM today. Some
[8:09] providers like Meta and DeepSeek publish
[8:12] their models only in their original
[8:14] floatingpoint format. Then open source
[8:17] communities and infrastructure companies
[8:19] like Unsloth pick them up and quantize
[8:22] them. But other providers like Quen do
[8:25] publish quantized versions of their
[8:27] models. You'll recognize them by
[8:29] suffixes like GGUF, GBTQ, or AWQ. I'll
[8:33] go into more detail in a future video
[8:35] specifically dedicated to post-training
[8:39] quantization. Sometimes we build models
[8:41] with the foresight that they will
[8:43] eventually be quantized. In this case,
[8:46] we can tweak the training process so
[8:48] that when quantization time does come
[8:51] right before deployment, the model is
[8:53] more resilient to the loss in precision.
[8:56] This is known as quantizationaware
[8:58] training or QAT for short. Extreme
[9:02] quantization down to four bits or lower
[9:05] is very likely to require this in order
[9:07] to avoid significant degradation in
[9:10] model
[9:10] performance. This is how the famous one
[9:13] bit LLMs are trained. It's a really
[9:15] interesting research topic. Stay tuned
[9:17] for a separate video on
[9:19] it. Now let's talk about the how. How do
[9:23] we turn floats into integers, float
[9:25] operations into integer operations? And
[9:29] how do we preserve the integrity of the
[9:30] model in integer
[9:32] space? The exact formula that converts a
[9:35] float into an integer is called the
[9:37] quantization scheme or quantization
[9:41] paradigm. Let's take a concrete example
[9:43] where we quantize a float 16 number into
[9:46] an int4. The standard signed integer
[9:49] representation that we already discussed
[9:51] 2's complement encodes an asymmetric
[9:54] interval for int 4. That's -8 to 7.
[9:58] Quadization frameworks often disregard
[10:00] the extra negative bucket to get a
[10:03] symmetric range. Of course, float 16 can
[10:06] represent a wide range of numbers, but
[10:08] the values in a neural network are
[10:10] typically in a narrow range between some
[10:12] values alpha and beta. This is called
[10:15] the clipping range. The process of
[10:17] determining alpha and beta by finding
[10:19] the minimum and maximum values flowing
[10:22] through the network is called
[10:23] calibration. Calibration is easy for
[10:26] parameters but non-trivial for
[10:29] activations. For the latter, we need to
[10:31] run inference on a calibration data set
[10:33] which depending on the size of the model
[10:35] and your hardware can take a few minutes
[10:37] to a few hours. For symmetric clipping
[10:40] ranges like minus1 to 1, the process is
[10:43] called symmetric quantization. This is
[10:46] the most straightforward case. So
[10:48] defining a quantization scheme means
[10:51] figuring out what bucket each real value
[10:53] falls into. We'll first compute the
[10:56] relative scale s of the two ranges as
[10:59] the ratio between their lengths. Now
[11:01] given a value r say 42, quantization
[11:05] means dividing r by the scale s and
[11:08] rounding to the closest integer which is
[11:11] three in this case. Sometimes the
[11:13] clipping range can be asymmetric. This
[11:16] can be caused by operations like relu
[11:18] which have strictly positive outputs and
[11:21] therefore skew the overall distribution
[11:23] of the model
[11:25] activations. Let's figure out how the
[11:27] mapping changes in this case. Trivially
[11:30] alpha should go into the leftmost bucket
[11:32] and beta into the rightmost. Then
[11:34] naturally zero will fall 1/3 of the way
[11:37] in between them. Its host bucket in this
[11:40] case minus2 is known as the zero point
[11:43] and is denoted by z. It acts as an
[11:46] offset for our previous mapping. So just
[11:49] as before, we'll compute the scale and
[11:52] our value r now maps to bucket number
[11:55] two. But this time we'll shift left by
[11:58] two positions as indicated by the zero
[12:01] point. So the final quantized value of
[12:04] 42 is now zero. We'll denote it by Q.
[12:09] Now let's formalize this. Here's a
[12:11] closed form expression for the zero
[12:13] point. The easiest way to see it is to
[12:16] think of s as this length and minus
[12:19] alpha as this length in terms of how
[12:22] much real space they cover. Their ratio
[12:26] tells us how many s hops from the left
[12:29] are needed to reach the zero bucket.
[12:32] That's 1 2 3 4 5. And then we'll add Q
[12:38] min which is minus 7 to finally get
[12:41] minus2.
[12:43] Now we can get an expression for the
[12:45] quantization process which reflects how
[12:48] we turned 42 into zero. And finally we
[12:52] can also define the reverse process of
[12:54] mapping Q back into a real value. This
[12:57] is called
[12:58] dequantization. Of course we can only
[13:00] recover an approximation of the original
[13:03] value R in this case4 because we cannot
[13:07] undo the entire damage of the rounding
[13:09] operation.
[13:12] So now we have a quantization scheme
[13:14] that maps real values to integers. But
[13:17] quantizing the model weights is only
[13:19] part of the story. Running inference
[13:22] means executing operations which also
[13:24] need to be translated from real to
[13:27] integer space. Let's start with
[13:29] something basic. Multiplying two scalers
[13:32] R1 and R2 into a product R3. So what
[13:36] does this look like in integer space? We
[13:39] start by quantizing the operants R1 into
[13:43] Q1 and R2 into Q2. Now what function f
[13:48] should we apply to recover the product
[13:50] but in integer space? Ideally
[13:53] quantization followed by dequantization
[13:56] is almost a noop. We want the
[13:59] dequantized values to preserve the
[14:01] original
[14:02] relationship. With this property in
[14:05] mind, let's work out what f is. We can
[14:08] apply the dq1 formula to each value and
[14:11] then rearrange to solve for q3. This
[14:15] expression is our function f. Now by
[14:19] construction, z is an integer. So adding
[14:22] or subtracting it is trivial. However,
[14:25] remember that the scale is a real value.
[14:28] So how can we implement this
[14:30] multiplication in a way that doesn't
[14:32] defeat the whole purpose of
[14:33] quantization? Because multiplying by a
[14:36] floatingoint number is what we're trying
[14:38] to escape in the first place. The trick
[14:41] is called fixed point arithmetic, a way
[14:44] to represent fractions using only
[14:47] integers. For example, to represent a
[14:50] value like
[14:52] $12.34, we could instead store it as
[14:56] $1,234 and keep track of the scale. That
[15:00] means to recover the original value,
[15:03] we'd have to divide by 100. So fixed
[15:07] point means the decimal point doesn't
[15:09] float. We fixed it two positions from
[15:12] the right. In practice, we don't use
[15:14] base 10 for the scale. We use powers of
[15:17] two instead. So if we have an unsigned
[15:20] integer with four bits, then the
[15:23] smallest step size we can represent is 2
[15:25] to the^ minus4.
[15:27] So the stored value is our dollar amount
[15:30] multiplied by the inverse of the scale
[15:32] and rounded to the nearest integer.
[15:35] That's 197 in this case. Just to
[15:38] establish some notation for an actual
[15:41] value v, I'll use vend for its stored
[15:44] value in fixed
[15:46] point. So how can we leverage fixed
[15:49] point arithmetic to multiply an integer
[15:51] x by a real value s and get an integer y
[15:56] in return?
[15:57] Your first instinct might be just store
[16:00] s as a fixed point number and perform
[16:02] the multiplication with fixed point
[16:05] arithmetic. But that's not quite right.
[16:08] If it were this easy, we wouldn't bother
[16:10] with quantization and just use fixed
[16:13] point instead of floating point from the
[16:15] get- go. The main problem is there's too
[16:18] much loss in precision. If s is a
[16:21] relatively small value like
[16:23] 0.003, it ends up rounded to zero. So
[16:26] the final product y would also be
[16:29] zero. Instead we express s as the
[16:33] product between a negative power of two
[16:36] and some other real value as zero.
[16:40] Intuitively what we're doing here is
[16:43] absorbing a lot of the precision into
[16:46] this negative power of two so that the
[16:49] leftover s0 is by choice higher than.5.
[16:56] If we store s0 as a fixed point number,
[16:59] we're not so concerned by the loss in
[17:01] precision anymore because we know it's a
[17:03] fairly large number. We chose it to be
[17:06] this way. So multiplying x * s
[17:10] translates to a integer multiplication
[17:14] followed by some bit
[17:16] shifts. Also as an optimization we can
[17:20] premputee the decomposition of s only
[17:23] once before deploying the
[17:25] model. So now that we know how to handle
[17:28] this multiplication by s in integer
[17:30] space, we have a full recipe for
[17:33] quantized multiplication of two scalers.
[17:35] But as you probably know, scalar
[17:37] multiplication is not the building block
[17:39] of deep learning. Matrix multiplication
[17:42] is. In the matrix world, the exact same
[17:46] principles apply, except that
[17:48] quantization and dequantization are
[17:51] applied to each value in the matrix. To
[17:54] work out what matrix multiply looks like
[17:56] in integer space, we'll use its
[17:58] definition to generalize the expression
[18:01] we deduced for the scalar case. And we
[18:04] end up with a very similar formula with
[18:06] this extra sum over all the entries in a
[18:09] row. In matrix multiplication,
[18:12] efficiency gains become much clearer.
[18:15] Under the hood, it requires m * n * p
[18:19] multiplications where mn and p are the
[18:22] dimensions of the matrices. In a modern
[18:24] LLM like llama 4, where we find matrices
[18:27] of size 4,000x 4,000, that's 10 billion
[18:31] operations that we implemented more
[18:34] effectively. And here is another subtle
[18:36] optimization. The scale S only needs to
[18:39] be applied once per output row as
[18:41] opposed to every entry and that's only a
[18:43] few thousand times for a matrix. So when
[18:46] the hardware allows it, certain
[18:48] quantization implementations actually
[18:51] perform the scale multiplication in
[18:53] floating point. On modern GPUs like
[18:56] Nvidia, float and int multiplications
[18:59] can be similarly fast. And in those
[19:01] cases, the real bottleneck isn't really
[19:04] compute, it's memory bandwidth. And the
[19:07] real gain from quantization is the
[19:09] reduced bit
[19:11] width. So far we made the assumption
[19:13] that we work with a single pair of
[19:16] quantization constants S and Z across
[19:19] the entire network. But in practice it's
[19:22] common to have multiple sets of
[19:24] constants. The granularity can vary. It
[19:27] can be per layer, per matrix, or even
[19:30] per matrix row. And this granularity
[19:33] applies both to weights and
[19:36] activations. Hopefully this gave you a
[19:38] solid understanding of how quantization
[19:40] arithmetic translates between real
[19:42] valued and integer space. In practice,
[19:46] you probably won't have to implement
[19:47] these low-level tricks yourself. Most ML
[19:50] frameworks like PyTorch and TensorFlow
[19:53] offer built-in support for quantization.
[19:55] And for deployment inference engines
[19:58] like the Onyx runtime or Nvidia Tensor
[20:01] RT apply even more aggressive hardware
[20:04] specific optimizations under the hood.
[20:07] Hopefully this video gave you a solid
[20:09] intuition on how quantization works. If
[20:12] that's the case, consider sharing or
[20:14] commenting because it really helps me
[20:16] keep these videos hype free and
[20:18] clickbait free without getting buried by
[20:20] the YouTube algorithm. As usual, my
[20:23] slide deck and my reading list are
[20:25] available on Patreon. Stay tuned for
[20:28] more in-depth quantization videos as
[20:30] part of this minieries. Thanks for
[20:32] watching.
