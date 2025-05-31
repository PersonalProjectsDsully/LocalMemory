---
type: youtube
title: System Design for Next-Gen Frontier Models — Dylan Patel, SemiAnalysis
author: AI Engineer
video_id: gFyBdBm0AGo
video_url: https://www.youtube.com/watch?v=gFyBdBm0AGo
thumbnail_url: https://img.youtube.com/vi/gFyBdBm0AGo/mqdefault.jpg
date_added: 2025-05-26
category: AI Infrastructure and Optimization
tags: ['AI infrastructure', 'large language models', 'cloud computing', 'GPU optimization', 'inference optimization', 'distributed systems', 'machine learning deployment', 'API scaling', 'AI hardware', 'model serving']
entities: ['llama CPP', 'Gole', 'Anthropic', 'Together', 'Fireworks', 'H100', 'A100', 'L40', 'disaggregated prefill', 'continuous batching']
concepts: ['compute intensive workloads', 'bandwidth intensive workloads', 'disaggregated prefill', 'continuous batching', 'noisy neighbors', 'model replication strategies', 'API inference optimization', 'cloud computing infrastructure']
content_structure: overview/explanation
difficulty_level: advanced
prerequisites: ['Understanding of AI/ML models', 'Familiarity with cloud computing', 'Basic knowledge of GPU architecture']
related_topics: ['AI model optimization', 'cloud computing infrastructure', 'GPU acceleration', 'API performance', 'distributed computing', 'machine learning deployment', 'AI inference systems', 'data center architecture']
authority_signals: ["'Gole Go's publicly said they're doing it'", "'you have a lot of noisy neighbors'"]
confidence_score: 0.8
---

# System Design for Next-Gen Frontier Models — Dylan Patel, SemiAnalysis

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=gFyBdBm0AGo)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: system-design, ai-models, inference, large-models, memory-bandwidth, compute-requirements, model-training  

## Summary

# Summary of "System Design for Next-Gen Frontier Models" by Dylan Patel

## Overview  
This video explores the challenges and system design considerations for running large language models (LLMs) at scale, focusing on inference workloads. Key themes include the computational and bandwidth demands of prefill and decode phases, the importance of efficient batching, and the shift toward disaggregated architectures to optimize cost and performance. The discussion also highlights the role of open-source tools and the need for infrastructure adaptations to support models like Llama 3 405b.

---

## Key Points  
- **Prefill vs. Decode Workloads**:  
  - **Prefill** (initial token generation) is **compute-intensive** and requires high-performance accelerators.  
  - **Decode** (generating subsequent tokens) is **bandwidth-intensive**, demanding efficient memory and communication.  
  - These are distinct workloads but are often treated as a single process in user-facing systems.  

- **Continuous Batching**:  
  - Running inference with **batch size one** (e.g., on personal devices) is inefficient for cloud-scale operations.  
  - **Continuous batching** enables handling multiple requests iteratively, reducing costs by up to 10x–100x compared to batch size one.  
  - Tools like **Llama CPP** lack support for this, necessitating custom solutions or open-source contributions.  

- **Disaggregated Prefill**:  
  - Companies like **Go**, **OpenAI**, **Anthropic**, **Together**, and **Fireworks** are adopting **disaggregated prefill**, separating compute-heavy prefill tasks from bandwidth-heavy decode tasks.  
  - This reduces "noisy neighbor" issues (resource contention in cloud environments) and optimizes accelerator utilization.  

- **Open-Source Tools**:  
  - **TensorRT-LLM** (Nvidia-specific) and **VM** (supporting AMD/Intel) are critical for optimizing inference.  
  - Llama 405b requires specialized tooling beyond basic frameworks like Llama CPP.  

- **Cost Implications**:  
  - High batch sizes and efficient infrastructure design are essential to mitigate the financial burden of large models.  
  - Disaggregation and continuous batching are key to achieving scalability and cost-effectiveness.  

---

## Quotes  
- *"You have a lot of noisy neighbors... it's very trivial to dramatically slow down most inference providers."*  
- *"Disaggregated prefill... once your inference volumes are high enough, you don't just replicate the model across chips."*  
- *"Continuous batching is one of the things you have to have support of... software today like Llama CPP doesn't have support for that."*  

--- 

This summary captures the core technical and operational challenges of scaling LLMs, emphasizing the need for tailored infrastructure and open-source innovation.

## Full Transcript

[00:03] [Music]
[00:13] couple different things right like you
[00:14] know people have been talking about
[00:16] stagnation um and uh it's I I don't
[00:19] think anyone else anyone here sees that
[00:21] a lot of people have been talking about
[00:22] stagnation of models and a lot of a lot
[00:25] of that has to just do with the fact
[00:27] that we haven't seen a big capabilities
[00:29] leap uh the last bit uh but that that
[00:31] comes really from uh models that we're
[00:35] using today are largely the same as the
[00:37] models that were trained in 2022 right
[00:39] gp4 4 Turbo 40 those are just smaller
[00:42] models that are trained for longer so
[00:44] similar quality right um you know 3.5
[00:46] CET came out recently but again that's
[00:48] actually smaller than Opus but it's
[00:50] somehow better because they trained it
[00:52] for longer right but we haven't seen a
[00:54] extremely large Model come out yet and
[00:56] and but we will soon uh but one
[00:58] interesting thing right is gbd4 is like
[00:59] .8 trillion parameters it's crazy crazy
[01:02] expensive to run right uh 200 billion
[01:05] parameters uh each token requires you
[01:08] know almost 600 gig flops uh but that
[01:11] that that's almost going to be
[01:12] considered a last generation model right
[01:14] in in a year from now um so there's a
[01:16] couple things that I wanted to talk
[01:17] about regarding that right and and
[01:19] mostly on the inference side because I
[01:21] don't think you know anyone here is
[01:22] going to try and train that kind of Next
[01:24] Generation model but definitely we we
[01:26] need to be able to run it um and so you
[01:29] know a few things right so just just
[01:30] going to break down inference uh in
[01:33] detail right uh you know you know
[01:35] there's two parts of inference right
[01:36] there's pre-fill there's decode prefills
[01:38] The Prompt processing right and the
[01:40] interesting thing is if you have a 2K
[01:43] prompt 2K uh context length prompt right
[01:45] 2,000 tokens you input into GPT um
[01:48] that's that's a pedal flop itself right
[01:51] um and then you know if you have 32,000
[01:53] prompt that you enter it's 20 pedop
[01:54] flops actually so it's a an incredible
[01:56] amount of compute uh that's required to
[01:58] just process the prompt
[02:00] um and and you know while while prefill
[02:03] is is very compute intensive right it's
[02:06] actually the opposite of decode right
[02:08] decode is actually generating each token
[02:10] iteratively right so you you process the
[02:12] prompt and you generate a token you feed
[02:14] it back in and you keep going
[02:15] iteratively right um and decode is
[02:18] extremely memory bandwidth intensive
[02:20] right um You have to load the whole
[02:22] model from the weights the entire all
[02:25] the weights into the uh chip right or
[02:27] chips uh for decode um and the Big
[02:30] Challenge here is that you know hey if
[02:33] you have 1.8 trillion parameters if
[02:34] you're running out a reasonable batch
[02:36] size you're activating all the experts
[02:37] you need to load all 1.8 trillion
[02:40] parameters every single token generation
[02:43] right even if you're serving multiple
[02:45] users at once that means you're uh you
[02:47] need you know a 1.8 uh you need
[02:50] terabytes a second of memory bandwidth
[02:52] you want to do 30 tokens per second I
[02:54] think that's like a minimum bar for most
[02:55] people right uh a lot of people want
[02:57] hundreds of tokens per second but even
[02:59] if if you want 30 tokens per second per
[03:01] user 64 users you need 60 terab a second
[03:04] of memory bandwidth if even if you look
[03:06] at an h100 it has like three right so
[03:09] this is a extremely challenging systems
[03:11] problem um more you know decode while it
[03:14] is very bandwidth intensive it's
[03:16] actually quite cheap on the compute
[03:17] which is why uh if you look at like open
[03:19] AI pricing or Claud pricing you see a
[03:22] three or 4:1 ratio between prefill
[03:25] versus decode pricing right uh so the
[03:27] input tokens cost you know oneir that of
[03:30] the output tokens um or 1/4 that so so
[03:34] you know today the best models I think
[03:36] uh 40 and and 3.5 CET or uh I want to
[03:39] say it's $15 per million tokens and then
[03:42] it's $5 per million tokens for input uh
[03:44] 15 for output um so five for pre-fill 15
[03:48] for decode um and and soon we're going
[03:51] to have you know in the in the open
[03:52] source you know so what everyone here
[03:54] can touch is is llama 3 405b right and
[03:56] that's that's going to be a real
[03:58] capability sort of unlock
[04:00] um for the you know open source market
[04:03] as well as you know Builders here right
[04:05] and I think I think there's a couple
[04:07] things that uh people really need to be
[04:09] able to implement right like you can't
[04:10] just run llama CPP on llama 405b right
[04:14] like it's just not going to work um so
[04:15] there's a bunch of stuff that people
[04:17] have to work on um you know whether it's
[04:19] using you know Clos Source libraries
[04:21] like tensor rtlm uh that only work on
[04:23] Nvidia or like VM which is an open
[04:26] source library that works uh on AMD and
[04:29] inel and and soon other people's chips
[04:31] as well um you know there's there's a
[04:33] lot of stuff that people need to figure
[04:34] out one one of those is is continuous
[04:36] batching right uh because you're going
[04:38] to get you know running inference at
[04:40] batch size one is horrendously expensive
[04:42] um you know it's great to run if you're
[04:44] running it on your own personal devices
[04:46] but if you're running it in the cloud
[04:47] right you're renting gpus you're running
[04:49] batch size one you're you're going to
[04:51] cost yourself 10x more you know 10x is a
[04:54] low bar right it's actually could be 10x
[04:55] to 100x more than running at a high
[04:57] batch right so you have to figure out
[04:59] how to to run High batch sizes batch
[05:01] sizes how many concurrent users you're
[05:03] serving um and so one of those things
[05:06] that makes it difficult is that users
[05:08] requests come in at different times
[05:10] right uh one person might send a request
[05:11] now and then another person sends in a
[05:13] request 5 seconds later uh but the first
[05:15] person's request is not done so you need
[05:17] to be able to do continuous batching I.E
[05:19] sub uh be able to run through the model
[05:21] iteratively uh every time right um and
[05:24] and bring in new users so continuous
[05:26] batching is one of the things that you
[05:27] have to have to have support of and a
[05:29] lot of software today like llama CPP
[05:31] doesn't have support for that so either
[05:33] you need to build it yourself or um you
[05:36] know contribute to an open source
[05:37] project that that builds this um to to
[05:40] enable lowcost inference right for you
[05:43] know models like llama 405b right um
[05:46] another one of those is is uh
[05:49] disaggregated uh prefill or
[05:51] disaggregated batching right it depends
[05:53] on what you call it um but you know if
[05:55] you go back to earlier I was discussing
[05:58] uh prefill is very very compute
[06:00] intensive decode is very uh bandwidth
[06:02] intensive these are two different
[06:04] workloads but when you Ser when you're
[06:05] serving a user right whether it's uh you
[06:08] know in your own app or you're using an
[06:09] API what have you right like these users
[06:12] uh don't care that it's two different
[06:14] workloads right it's one workload to
[06:15] them uh I get tokens out right I submit
[06:17] something to you and I get tokens back
[06:19] uh but but for anyone running the infra
[06:21] themselves uh they need to they need to
[06:23] be keenly aware that these are two
[06:24] different workloads um so one thing that
[06:26] a lot of people have uh started to do um
[06:29] gole Go's publicly said they're doing it
[06:31] I believe opening ID and anthropic are
[06:32] also doing it um you know uh other firms
[06:36] like together and fireworks have hinted
[06:37] that they're doing this uh is is
[06:39] disaggregated pre-fill right so once
[06:42] your inference volumes are high enough
[06:43] you don't just run inference you know
[06:46] you don't just replicate the model
[06:47] across however many chips you have right
[06:49] uh say say it takes four mod four chips
[06:51] to serve llama 405b right in the future
[06:54] um you wouldn't just have you know if
[06:56] you have so many if you have enough
[06:57] users you don't just go for and then 8
[07:00] 16 whatever right you don't just
[07:01] replicate that across the world you
[07:03] actually do this thing called
[07:04] disaggregated prefill you have one set
[07:06] of accelerators do the pre-fill which is
[07:08] very compute intensive and then you hand
[07:10] it off to the other set of accelerators
[07:12] to do decode now today everyone just
[07:14] uses the same accelerator for that right
[07:16] h100 or a100 or you know maybe maybe l40
[07:19] or something but mostly h100
[07:22] uh but there's a there's a reason you do
[07:24] this right and and and that big reason
[07:26] is that you have a lot of noisy
[07:27] neighbors right um so if you've evered
[07:29] worked in like CPUs or on anything in
[07:31] cloud computing noisy neighbors are a
[07:33] huge huge issue um and actually like
[07:35] there's it's very trivial to
[07:37] dramatically slow down most inference
[07:39] providers Services uh if if you just uh
[07:42] send queries in a certain way like in a
[07:44] in a sort of malicious way um you can
[07:47] you can just slow down people's uh
[07:49] service right whether that's you know
[07:51] and and that'll that'll impact the users
[07:53] time to First token right um and I think
[07:55] that's a huge issue right if time to
[07:56] First token is too long people will just
[07:59] quit right using your service um if uh
[08:03] you know the tokens per second varies a
[08:05] lot right for a moment you're getting
[08:06] 100 tokens per second then it drops down
[08:08] to like 30 then it drops goes back up to
[08:10] 100 that's going to be really annoying
[08:12] to the user so so there's a lot of
[08:13] things around you know SLA and and
[08:16] reliability and all these things that
[08:18] you have to guarantee and so
[08:19] disaggregated prefill uh is is one of
[08:22] the techniques to do that right um and
[08:25] and so you don't want to have someone
[08:28] submit you know for example
[08:29] hey I have a database and I want to sub
[08:31] I want to run an llm query across every
[08:33] single Row in that database and I'm just
[08:35] going to submit it to you my service
[08:37] provider because you have this cool
[08:38] model or what have you that's fine tuned
[08:40] on some data set and what whatever it is
[08:42] right if I submit 10,000 rows to you at
[08:45] once that's going to kill everyone
[08:46] else's performance right so so this is
[08:48] one of the techniques that people have
[08:49] for uh making it so you know that that
[08:52] person who you definitely want to serve
[08:54] uh doesn't impact everyone else's usage
[08:57] uh because once you open up your service
[08:59] to the real world you're not going to be
[09:00] able to control who's submitting what
[09:02] and rate limits are the most annoying
[09:03] thing ever so that's not the correct way
[09:05] to go about it um another thing is
[09:08] context caching right so Google launched
[09:11] this recently uh they're the only one
[09:13] offering this today but I think this is
[09:14] a really big deal uh cuz when people
[09:17] talk about fine-tuning right of models
[09:18] that's great uh but in reality the best
[09:21] models are really expensive to fine tune
[09:23] or impossible to fine-tune right I can't
[09:26] go fine-tune 3.5 CET or fine tuning l
[09:29] 405b is going to take you know dozens
[09:31] and dozens of gpus right so so instead
[09:34] of that the the uh or you know in in
[09:36] close Source models generally so Google
[09:38] only does close Source models mostly for
[09:39] the big ones right so Gemini 1.5 Pro
[09:42] they offered this they brought this
[09:43] recently right which is context caching
[09:46] so instead of you know fine-tuning your
[09:48] model why not you know just fill out a
[09:50] context length of you know they they
[09:51] offer I think 2 million now today right
[09:53] 2 million context length um why not fill
[09:56] it out with your data there right um you
[09:58] know and and there's a couple you know
[10:01] advantages to that one is you can use
[10:03] the best models right in the case of
[10:04] fine-tune models you really are focused
[10:06] on like the Llama 7B or mix draw or
[10:09] llama uh you know 70b it's it's kind of
[10:12] much lower quality models than what's
[10:14] available in the close Source world uh
[10:16] so one of the things you can do is you
[10:18] can um Implement what Google has called
[10:20] context caching in the in the open
[10:22] source World we'll we'll have super long
[10:23] context models soon enough but uh
[10:26] economically right you know we talked
[10:27] about $15 token per per million tokens
[10:30] output um and 5 million per million
[10:33] tokens input if you were to have uh on
[10:35] on you know the best close Source models
[10:37] today if you were to submit a prompt of
[10:40] like you know a million tokens and and
[10:43] most most of the times you're looking at
[10:44] a document you get a query back right
[10:45] you your your output is very small
[10:47] almost all of the cost is just sending
[10:49] them that document right so that's
[10:51] that's going to really really hurt you
[10:52] so for people you know targeting maybe
[10:54] like a legal AI or like um you know some
[10:57] sort of other contract review AI a lot
[10:59] of these Enterprise use cases uh
[11:01] pre-fill is going to dominate your cost
[11:03] if you're using apis um and so Google
[11:06] has this context caching and and open
[11:08] source will have it so models you can
[11:09] run yourself and and others will deploy
[11:11] over time uh but basically you don't
[11:13] recompute the KV cache right the the
[11:17] context length every single time instead
[11:19] you cache it uh but the problem is to
[11:21] save save that takes in an incredible
[11:24] amount of memory um so you don't save it
[11:26] in the gpu's memory right you save it on
[11:28] the CP use memory or storage um and so
[11:32] uh VM uh which is an open source library
[11:35] for inference is contributing is
[11:37] building this currently so if you're
[11:39] interested in contributing to that uh
[11:41] check that out um or if you're
[11:43] interested in using it just start a
[11:44] project right um because you know while
[11:47] most of the models we have in the closed
[11:48] Source today are like only like 32 or 8K
[11:51] or 4K context length they're coming with
[11:53] longer um and being able to you know
[11:56] dramatically reduce your costs um by
[11:59] caching the context
[12:02] um is is very is gonna is going to
[12:04] dramatically reduce cost right um so now
[12:07] I'm just going to talk about like head
[12:08] in the cloud stuff instead of like real
[12:10] usable things which is um you know
[12:13] what's coming down the pipeline right
[12:14] which is you know gbd4 was like 20,000
[12:16] chips for 90 to 100 days um used you
[12:19] know 38 gwatt hours very very expensive
[12:21] cool um but you know what's what what
[12:24] are they building now right uh open AI
[12:26] xai um anthropic many others are
[12:29] building 100,000 chip clusters right and
[12:31] it would train gbd4 in 3 days right so
[12:33] it's kind of irrelevant um you know and
[12:36] and uh I'll skip over this part uh
[12:39] because it's not really uh too relevant
[12:41] um but you know what what what's a
[12:43] modern system capable of right like h100
[12:45] is is pretty uh pretty fast relative to
[12:48] a100 and and coming down the pipeline is
[12:50] these the new Nvidia chips but what
[12:52] what's com you know what's coming down
[12:54] with these 100,000 GPU clusters right um
[12:56] it's not going to be a 1.8 trillon
[12:57] parameter model it's actually going to
[12:58] be you know could be in the tens of
[13:00] trillions of parameters um you know the
[13:03] the training flops right I talked about
[13:04] gp4 is it's roughly 2 e25 flops right
[13:08] which is uh you know a number that's not
[13:11] really relevant or 2 e25 flop um but
[13:14] with 100,000 GPU cluster you can do 10
[13:16] e26 10 e27 flops uh and to run that
[13:19] model is going to require 200 gigabyt or
[13:21] terabytes of a second memory bandwidth
[13:23] right um but what what is that like what
[13:25] does that look like right so so this is
[13:27] a on the top right is an image
[13:30] of uh Microsoft's data centers in
[13:33] Arizona where they're making GPT 5 right
[13:36] um they have about 100,000 gpus here uh
[13:39] it's 150 megawatts right like the
[13:41] average home does not consume you know
[13:43] that's like that's like like tens of
[13:45] thousands if not hundreds of thousands
[13:46] of homes of power consumption right it's
[13:49] it's kind of insane um elon's talked
[13:51] about his next Generation cluster he's
[13:52] building 100,000 GPU cluster today uh
[13:55] but he's talked about his next
[13:56] Generation cluster is 300,000 gpus this
[13:58] kind kind of insane but the the power
[14:00] cost for that alone would be like $500
[14:03] million a year right so it's like you
[14:05] know people are people are kind of
[14:06] insane but it's pretty cool um but you
[14:10] know the the the interesting thing here
[14:12] is you know on training we we you know
[14:14] when when you when you try and train a
[14:16] model today people just talk about fully
[14:17] connected clusters uh every GPU is
[14:20] connected to every other GPU at some
[14:21] speed and you you know you have to do
[14:23] you know all your operations but that's
[14:25] not really possible when you go to these
[14:27] super large clusters right
[14:29] um so the 100,000 GPU clusters those are
[14:31] being built this year and then next year
[14:33] they're planning to build multiple
[14:34] 100,000 GPU clusters already you can see
[14:37] that it exists across multiple buildings
[14:39] right um and so there's a lot of
[14:42] complicated networking uh going on right
[14:45] to connect these data centers together
[14:48] um and and one other thing I that I
[14:50] think is just like kind of interesting
[14:51] to again head in the clouds just to
[14:52] think about is um when you connect these
[14:55] chips together there's a lot of Optics
[14:57] right uh you know you convert from
[14:59] electrical to Optical uh and then you
[15:01] know over fiber optics to connect
[15:02] between chips transceivers Etc right uh
[15:05] these are extremely unreliable right uh
[15:07] they tend to have a failure rate of
[15:09] around 5 years um and so what's
[15:12] interesting is if you're talking about a
[15:13] 100,000 GPU cluster um or if you're
[15:15] talking about a 500,000 GPU cluster
[15:18] you're going to have something fail like
[15:20] every 5 minutes right um which is insane
[15:23] right how do you even deal with
[15:25] something in your cluster failing every
[15:26] 5 minutes when you're training a model
[15:28] right right um so you know this is this
[15:31] is again more of like a hardware
[15:32] oriented thing but uh you know the the
[15:35] other thing that's interesting is like
[15:37] when you get chips they're not all the
[15:38] same speed you know h100 is not an h100
[15:41] um they're stragglers uh so if you get a
[15:44] large distribution of chips um what we
[15:46] call an industry is is called the
[15:47] Silicon Lottery um in that like you know
[15:51] you you can buy for example a a gaming
[15:54] GPU and and compare it to other people's
[15:56] gaming gpus on the forms and they're
[15:57] actually like percentages different
[15:59] in performance but when you do a massive
[16:01] training cluster um you end up with you
[16:04] know training is a synchronous workload
[16:06] right you know you you you update the
[16:09] weights you then you pass the gradients
[16:10] around right um and then you you know
[16:12] then you again run through a bunch of
[16:14] data uh update the weights or pass the
[16:16] gradients around update the weights
[16:18] right um so it's a synchronous workload
[16:20] so if one of them is 10% slower then
[16:22] everything is 10% slower and B dance had
[16:24] a cool paper where actually they saw a
[16:25] 25% decrease in speed just because one
[16:28] random GPU they got uh while it did
[16:31] technically work um in Nvidia and and
[16:33] and according to Nvidia it was fine it
[16:35] was like 25% slower than uh what they
[16:38] wanted right so they're you know this is
[16:40] like this is on like a 20,000 GPU
[16:42] cluster even right um so so it's uh it's
[16:45] it's quite interesting that you know
[16:48] that that's these are the problems
[16:49] people are running into at scale right
[16:51] so they pulled that GPU out um and then
[16:53] you you can sort of see their
[16:55] performance dramatically uplifted right
[16:57] um during during TR
[16:59] um and then again this is bite dance on
[17:01] a 20,000 GPU cluster so it's it's um
[17:05] it's it's a big big issue um and I think
[17:08] I think some of the other stuff in this
[17:09] presentation is not really relevant uh
[17:11] but I think I think what are these next
[17:14] Generation systems look like is a very
[17:17] um important question to ask yourself
[17:20] right um you know and what what do I
[17:22] what do I what do I do when I deal with
[17:24] that right like I think a lot of the
[17:26] scaffolding that people are building uh
[17:28] today for M are dealing with you know is
[17:31] is dealing with hallucinations and
[17:32] things like that and and the hope that
[17:34] everyone has or at least a lot of the
[17:36] AGI people have is that you know when I
[17:38] when I 100x the compute um you know when
[17:41] I build a cluster that takes $500
[17:42] million of electricity and I trade a
[17:44] model with it it's going to make
[17:45] something that uh uh you know yearly
[17:47] electricity cost and make a model with
[17:49] it and then the cluster itself cost over
[17:50] 10 billion by the way right uh it's it's
[17:52] going to get rid of a lot of this um the
[17:55] hallucinations it's going to let us do a
[17:57] lot of interesting things uh um yeah so
[18:00] so I think that's that's basically all
[18:02] for the talk I just wanted to you know
[18:03] uh mention you know sort of a reasonable
[18:06] thing which is how do you run llama 405b
[18:07] kind of some strategies that people need
[18:09] to implement that aren't necessarily
[18:11] implemented yet uh in the open source
[18:12] that are implemented at the labs um but
[18:15] then also like you know what are they
[18:16] doing right because they're not worried
[18:17] about you know llama 405b capable models
[18:22] [Music]
