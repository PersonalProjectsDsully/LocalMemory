---
type: youtube
title: Customized, production ready inference with open source models: Dmytro (Dima) Dzhulgakov
author: AI Engineer
video_id: ePMvfa8vgL8
video_url: https://www.youtube.com/watch?v=ePMvfa8vgL8
thumbnail_url: https://img.youtube.com/vi/ePMvfa8vgL8/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning Infrastructure
tags: ['LLM deployment', 'AI optimization', 'GPU efficiency', 'multi-modal models', 'cloud AI infrastructure', 'model serving', 'AI scalability', 'latency optimization', 'enterprise AI', 'machine learning operations']
entities: ['Denny', 'Fireworks AI', 'CUDA kernels', 'SDXL', 'SD3', 'Stability', 'RAG', 'LLMs', 'GPU', 'Cloud Computing']
concepts: ['LLM deployment challenges', 'Custom serving stack optimization', 'Latency-throughput trade-offs', 'Multi-modal model support', 'Cost optimization under constraints', 'Production readiness for AI', 'Runtime configuration tuning', 'AI infrastructure scalability']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with LLMs and their deployment challenges', 'Knowledge of cloud computing infrastructure']
related_topics: ['AI model optimization', 'Cloud infrastructure for AI', 'Multi-modal machine learning', 'Latency-critical systems', 'AI deployment pipelines', 'GPU-accelerated computing', 'Enterprise AI scalability']
authority_signals: ['We built our own custom serving stack from the ground up', 'We believe is one of the fastest if not the fastest', 'Our solutions address the complexities of model deployment']
confidence_score: 0.85
---

# Customized, production ready inference with open source models: Dmytro (Dima) Dzhulgakov

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=ePMvfa8vgL8)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: open-source-models, ai-deployment, model-optimization, machine-learning, latency-reduction, custom-ai, deep-learning  

## Summary

# Summary of "Customized, Production-Ready Inference with Open-Source Models"  

## Overview  
Dmytro (Dima) Dzhulgakov of Fireworks discusses the challenges and opportunities of using open-source models for production-grade inference. He highlights the limitations of proprietary models (e.g., cost, latency, lack of customization) and emphasizes the advantages of open-source models in domain adaptability, cost efficiency, and flexibility. Fireworks addresses the complexities of deploying open-source models through optimized serving stacks and multi-modal support.  

---

## Key Points  
- **Background**: Fireworks focuses on making open-source models (e.g., LLMs, image generators) production-ready with efficiency, scalability, and customization.  
- **Challenges with Proprietary Models**:  
  - High costs for large-scale inference.  
  - Limited customization for specific use cases.  
  - Inflexible latency/cost trade-offs.  
- **Advantages of Open-Source Models**:  
  - **Domain Adaptability**: Open weights allow fine-tuning for niche applications (e.g., 10,000+ model variants).  
  - **Cost Efficiency**: Smaller models reduce inference costs (e.g., 10x savings vs. proprietary alternatives).  
  - **Flexibility**: Customizable settings for latency, throughput, and prompt length.  
- **Challenges in Deployment**:  
  - Complex setup/maintenance (GPU selection, frameworks, optimization).  
  - Difficulties in scaling to enterprise-level reliability, telemetry, and observability.  
- **Fireworks’ Solutions**:  
  - **Custom Serving Stack**: Optimized from CUDA kernels to deployment orchestration for speed and customization.  
  - **Multi-Modal Support**: Fastest provider for SDXL and SD3 image generation models.  
  - **Performance Tuning**: Tailored settings for latency, cost, and use-case requirements (e.g., long prompts, interactive applications).  

---

## Important Quotes/Insights  
- *"Open-source models are great for customization... because the weights are open, you can always tailor them to your use case."*  
- *"We don’t only focus on LMs; we handle many modalities, like image generation."*  
- *"Optimizing settings across the stack can yield multiple X improvements in performance."*  

---

## Actionable Takeaways  
1. **Leverage Open-Source Models**: Prioritize open-source models for cost efficiency and domain-specific customization.  
2. **Optimize Deployment Settings**: Tailor inference parameters (latency, throughput, prompt length) to align with use-case requirements.  
3. **Use Fireworks’ Tools**: Utilize their custom serving stack for production-grade reliability, multi-modal support, and performance tuning.  
4. **Focus on Efficiency**: Invest in optimization techniques (e.g., runtime-level adjustments) to maximize cost and latency trade-offs.  

--- 

## Final Note  
Fireworks aims to bridge the gap between open-source model experimentation and enterprise deployment, emphasizing speed, flexibility, and scalability for diverse applications.

## Full Transcript

[00:00] [Music]
[00:14] hello everyone so my name is Dima um as
[00:17] mentioned uh unfortunately my co-founder
[00:20] Lino was on the schedule couldn't make
[00:21] it today because of some personal
[00:23] emergency so you got me and as you saw
[00:26] we don't have yet AI to figure out video
[00:29] projection but we have a for a lot of
[00:31] other things uh so today I'm going to
[00:33] talk about fireworks Ai and generally
[00:35] I'm going to continue this te which kin
[00:37] started about open models uh and how we
[00:41] uh basically focus on
[00:47] productionize but first uh as an
[00:49] introduction uh what's our background uh
[00:52] so the founding team of fireworks comes
[00:55] from PCH leads at meta and some veterans
[00:58] from Google AI so we combined have like
[01:01] probably decade of experience in
[01:02] productionizing Ai and some of the
[01:03] biggest companies in the world and I
[01:06] myself personally has been core
[01:08] maintainer of PCH uh for the past 5
[01:10] years so topic of Open Source is really
[01:13] close to my heart and since we kind of
[01:16] LED this revolution of Open Source tool
[01:19] chain for deep learning through our work
[01:21] on P and some of the Google Technologies
[01:23] we really believe that open source uh
[01:26] models are the future also for like for
[01:30] for Gen application and our focus at
[01:32] fireworks is precisely on
[01:34] that um
[01:37] so I mean uh how many people in the
[01:40] audience actually like use GPT and
[01:42] deploy it in for
[01:44] production and how many people how many
[01:46] folks use open models um AO prodction oh
[01:51] okay so I was about to convince you that
[01:53] share of Open Source models is going to
[01:55] grow over time but it looks like in this
[01:57] audience it's already already sizable
[01:59] but
[02:00] nevertheless um so why why basically
[02:03] this tradeoff why go big or why go small
[02:07] uh currently still like bulk of
[02:08] production inference is still based on
[02:10] proprietary models and uh the catch with
[02:13] that those are really good models and
[02:15] often froner in in many domains uh
[02:18] however the catch is that it's one model
[02:20] which is good in many many things and
[02:22] it's often served uh in the same way uh
[02:24] regardless of the use case which means
[02:26] that maybe if you have bch inference uh
[02:29] on some nrow domain or you have some
[02:31] super realtime use case uh where you
[02:33] need to you need to do like voice
[02:36] assistant or something uh those often
[02:38] serve from the same infrastructure
[02:39] without customization in terms of model
[02:41] capabilities it also means yeah like GPT
[02:43] 4 is great or CLA is great and can
[02:46] handle a lot of sense but you are often
[02:48] paying a lot for additional capabilities
[02:51] which are not needed in particular this
[02:52] case you don't really need customer
[02:54] support chatbot to know about 150
[02:57] Pokémons or be able to write write your
[02:59] poetry uh but you really want it to be
[03:02] really good in the particular uh narrow
[03:05] domain so this uh kind uh this kind of
[03:08] discrepancy for large models leads to
[03:09] several issues one as I mention is high
[03:11] latency because using a big model means
[03:14] uh longer response times uh which is
[03:18] particularly important for Real Time use
[03:19] cases like voice assistance it gets more
[03:22] and more important with tic stuff
[03:24] because for stuff like um for example
[03:28] next talk is going to be de right like
[03:29] you you need to do a lot of steps for
[03:31] like something like agent like
[03:33] application to do reasoning and call the
[03:35] model many times so latency is really
[03:37] important and often you see that you can
[03:39] pick smaller models like lar or Gemma
[03:43] which you just talk about and achieve
[03:45] the for an nrow domain uh same of better
[03:48] quality while being you know up to 10
[03:50] times faster uh for example for some of
[03:53] the function calling use cases like
[03:54] externally Benchmark from uh from
[03:57] Berkeley yeah like the you get similar
[03:59] performance from F tune Lama 3 at 10x
[04:02] speed cost is also uh is also an issue
[04:06] if you're running a big model for uh on
[04:08] a lot of traffic you know even if you
[04:10] have perhaps I know 5K tokens prompt and
[04:13] 10,000 users and each of them call sell
[04:16] them 20 times per day you know on GPT 4
[04:18] even on GPT 40 it probably adds up to
[04:20] like 10K per day or something like
[04:22] several million per month Al 7 million
[04:25] per year which is a sizable cost of a
[04:27] startup you can easily cut that with
[04:29] much smaller model models and that often
[04:30] we see as a uh as a kind of motivation
[04:34] for reaching out for smaller and more
[04:36] customizable models uh but really the uh
[04:40] like where open models shine is domain
[04:42] adaptability and that comes uh in two
[04:45] aspects first um there is so many
[04:48] different F tunes and customizations uh
[04:50] I think Kaitlyn was mentioning about you
[04:51] know Gemma built Indian languages
[04:54] adaptation like there are model
[04:55] specialized for coder for medicine if
[04:57] you had to hug and face there are like
[04:59] 10 of thousands of different model
[05:01] variants and because the weights are
[05:02] open you can always customize to your
[05:04] particular use case and tune and uh tune
[05:08] quality specifically for for what you
[05:10] need so open source models are great so
[05:13] what are the challenges uh the
[05:14] challenges really come from three areas
[05:16] uh first like what we usually see when
[05:19] people try to use you know open model
[05:20] something like gem or whatever uh or or
[05:24] lb uh you run into complicated setup and
[05:27] maintenance right you need to go and
[05:28] find gpus somewhere you need to figure
[05:30] out which Frameworks to run on those you
[05:33] need to like download the models maybe
[05:35] do some performance optimization tun in
[05:37] and you kind of have to repeat this
[05:38] process end to end every time the model
[05:40] gets updated or new version is released
[05:43] Etc uh on optimization itself uh there
[05:46] is especially for llms but generally for
[05:48] Gen models there are many attributes uh
[05:52] and settings which are really really
[05:54] dependent on your use casing
[05:56] requirements somebody needs low latency
[05:57] somebody needs High throughput proms can
[06:00] be short proms can be long Etc and
[06:02] choosing the optimal settings across the
[06:03] stack is actually not trival and as I
[06:06] show later in many cases you can get
[06:08] multiple X improvements from doing from
[06:10] doing this efficiently and finally like
[06:13] just getting it production ready is
[06:15] actually hard uh if as you kind of go
[06:18] from experimentation to production even
[06:20] just BB sitting gpus on public clouds is
[06:23] not not as easy because gpus Ain not
[06:25] always reliable uh but getting to
[06:27] Enterprise scale requires you know SC
[06:29] scalability technology Telemetry
[06:31] observability Etc so those are uh things
[06:34] which we focus on uh solving at
[06:36] fireworks so starting with efficiency we
[06:39] built uh our own custom serving stack
[06:42] which we believe is one of the fastest
[06:44] if not the fastest uh we did it did it
[06:47] from the ground up meaning from writing
[06:49] our own you know Cuda kernels all the
[06:51] way to customizing how the stuff gets
[06:54] deployed and orchestrated on the service
[06:56] level and that brings multiple
[06:58] optimizations but most importantly we
[07:00] really focus on customizing this service
[07:02] tech to your needs uh which basically
[07:04] means for your custom work cloud and for
[07:06] your custom cost and latency latency
[07:09] requirements we can we can tune it for
[07:12] uh for those settings what does it mean
[07:14] in practice what do customization means
[07:16] in practice uh for example many use
[07:18] cases use Rag and use very long prompts
[07:21] uh so there are many settings you can
[07:23] tune actually on the runtime level at
[07:25] the deployment level to optimize for
[07:27] loan prompts which often can be rep
[07:29] fitable so cing is useful or just tun in
[07:32] settings so the stut is higher while
[07:34] maintaining latency so this is
[07:36] independently Benchmark if you go to uh
[07:39] you know artificial analysis and select
[07:40] La prompt where Firebox actually is the
[07:42] fastest even faster than some of the
[07:44] other providers which are over there at
[07:46] expoo uh and uh we don't only focus we
[07:50] don't only focus on LM and Friends uh we
[07:52] focus on many modalities uh as an
[07:54] example for image generation we are the
[07:56] fastest provider serving sdxl we also
[07:59] the only providers Ser in sd3 uh
[08:02] stabilities new model because their API
[08:04] actually routes to our servers um and
[08:08] finally as I mentioned for like LMS like
[08:10] customiz especially for LMS
[08:12] customization matters a lot uh One
[08:14] require like one paradig we how to think
[08:16] about performance of LMS often it's
[08:18] useful for use cases is to think about
[08:20] Max like minimizing cost under a
[08:22] particular latency constraint we often
[08:23] have customers coming and say like hey I
[08:25] need to like have this my interactive
[08:27] application I need to generate that many
[08:29] tokens under two seconds and that's
[08:32] where that's really where like cross
[08:33] stack optimizations shine uh whereby uh
[08:37] T into particular like latency cut off
[08:39] and change in many settings you can
[08:41] deliver much higher throughput multiple
[08:43] times higher throughput uh which B
[08:45] higher throughput basically means fewer
[08:46] gpus and lower
[08:49] cost uh in terms in terms of model
[08:52] support we support support best quality
[08:55] open source models uh we heard about
[08:57] Gemma now obviously llamas uh some of
[09:00] the ASR inext to speech models pretty
[09:03] much from from many providers we also
[09:05] work with model Developers for examp for
[09:07] example e large uh in US is also served
[09:10] on uh on fireworks launched launch last
[09:14] week and uh as a kind of platform
[09:18] capabilities as I mentioned we have a
[09:20] lot of Open Source models to uh to get
[09:22] you started or customized ones we do
[09:24] some of the fine tuning of those models
[09:26] uh in house so I'm going to talk a
[09:28] little bit about function specialized
[09:30] models uh later on or we do some of the
[09:34] vision language model Fusion ourselves
[09:36] which we release as well and of course
[09:38] the key for open source um open model
[09:42] development is it can tuned for
[09:43] particular use case so we do provide a
[09:45] platform for fine tuning uh whether
[09:47] you're bringing your data set collected
[09:50] elsewhere or collecting it life uh with
[09:52] a feedback when serves on our
[09:55] platform uh specifically on
[09:57] customization it's like one uh interest
[09:58] one inter in feature which a lot of
[10:00] people starting to experiment with
[10:02] models uh find interesting is if you try
[10:05] to find fine tune and deploy the
[10:06] resulting model how uh how to serve it
[10:09] efficiently uh turns out if you do lying
[10:11] tun which a lot of folks do uh you can
[10:13] do uh smart tricks and deploy multiple
[10:16] plur models on the same GPU uh actually
[10:19] thousands of them which means that we
[10:20] can give you still serverless inference
[10:22] with pain per token even if you have
[10:24] like thousands of model variants uh
[10:27] sitting and deployed there without
[10:28] having to pay any fixed
[10:32] cost of course single model is all great
[10:35] uh but what we see increasingly more and
[10:37] more in applications is model is not the
[10:40] product right uh uh by itself you need a
[10:43] kind of bigger system uh in order to
[10:45] solve Target application and the reason
[10:47] for that is because uh models by
[10:49] themselves tend to hallucinate so you
[10:51] need some ground in and that's where
[10:53] like rag or access to external knowledge
[10:56] bases comes in uh also we don't have you
[10:58] no yet in Industry magical multimodel uh
[11:02] AI across all the modalities so often
[11:04] you have to kind of chain multiple types
[11:06] of models and of course you have all
[11:07] this like external tools and external
[11:09] actions which uh kind of end to end
[11:12] applications might want to do in tic
[11:15] form uh so I think the term which I
[11:17] really like which is like popularized by
[11:19] data Brak is like compound AI system but
[11:22] basically increasingly seen like
[11:24] transition from just the model being the
[11:26] product to kind of this combination of
[11:28] maybe like Rag and function call and
[11:29] external tools Etc built together as the
[11:32] product and that's pretty much Direction
[11:34] which we kind of see uh this field
[11:37] moving along uh over time so what does
[11:40] it mean from uh from kind of our
[11:42] perspective what we what we do in this
[11:43] case uh so we see kind of as a function
[11:47] calling like agent as a at the core of
[11:49] this uh emerging architecture which
[11:52] might be connected to either domain
[11:53] specialized models uh served on our
[11:57] platform directly or maybe tuned for for
[11:59] part different needs and connected to
[12:01] external tools uh maybe it's a cond
[12:02] interpreter or maybe it's like external
[12:04] apis somewhere uh with really like this
[12:07] kind of central agentic uh view uh kind
[12:10] Central Central model kind of
[12:12] coordinating and trying to trash the uh
[12:15] user user requirements if it's for
[12:17] example a chatbot or something uh you
[12:19] probably all uh heard about like
[12:21] function calling you know popularized by
[12:22] open air initially that's that's
[12:24] basically the same idea uh so yeah the
[12:27] function qu is really like a how to how
[12:30] to connect llm to external tools and
[12:33] exter and external elements what does it
[12:36] mean in practice so we actually uh focus
[12:40] on F models specifically for function
[12:41] calling so we release a series of models
[12:44] like that like the latest one fire
[12:45] function V was released two uh two weeks
[12:47] ago and uh what you can do with that is
[12:52] uh okay if I manage to
[12:55] click if I manage to click on this
[12:58] button
[13:00] uh what it means is that you can build
[13:02] uh applications which kind of combine
[13:04] free form General chat uh capabilities
[13:07] with function Co so in this case the
[13:09] this is you know this fire function has
[13:11] some chat capabilities so you could see
[13:14] you can like ask it what what you can
[13:15] you do and it has like some
[13:16] self-reflection to tell you what it can
[13:18] do it's also connected in this demo app
[13:20] to a bunch of uh external tools so it
[13:22] can uh query uh like stock quotes it can
[13:26] plot some charts all those like external
[13:28] apis
[13:29] uh it can U also gener generate images
[13:33] but what it really needs to figure out
[13:35] is how to translate user query into do
[13:38] complex reasoning translate it into
[13:39] function calls so for example if we ask
[13:41] it to generate a bar chart with top
[13:44] three uh like this stocks of top Cloud
[13:47] providers like the big three it actually
[13:49] needs to do several steps right it needs
[13:51] to understand that like top three Cloud
[13:53] providers means you knows gcp and uh an
[13:57] Azure right aure is on by Microsoft it
[14:00] needs to uh then go do function calls
[14:03] querying their stock prices and finally
[14:05] it needs to combine those information
[14:06] and send it to chat plotting API which
[14:09] is what just happened uh in the in the
[14:11] background uh another important aspect
[14:14] which you have to do for like efficient
[14:16] uh kind of function calling chat
[14:18] capabilities you need to have contextual
[14:20] awareness so if I ask it to add
[14:22] particular uh if I ask to add Oracle to
[14:24] this graph it needs to understand what
[14:25] I'm referring to and like still keep the
[14:27] previous context and regenerate the
[14:29] image and finally you know if I switch
[14:31] to a part to a different topic it kind
[14:33] of needs to drop the previous context
[14:35] and understand that like hey this is
[14:37] less uh this historical context is less
[14:39] important I'm going to start from
[14:40] scratch so there is no like Oracle in
[14:42] that cat photo or whatever uh so you
[14:45] know this particular demo is uh is
[14:47] actually open source you can like go to
[14:49] our GitHub and try it out it's built
[14:51] with fire function and it's built with
[14:52] like a few other a few other models
[14:54] including like sdxl which are run on our
[14:57] platform uh the model s for function
[14:59] Callin is actually open source uh it's
[15:02] on higen phas I mean you can of course
[15:04] call it on uh at fireworks with for
[15:06] optimal speeds but you can also uh run
[15:08] it locally if you want it uses a bunch
[15:10] of uh you know functionality on our
[15:12] platform uh for example like structure
[15:14] generation uh with like with Json model
[15:17] grammar mode which I think was similar
[15:19] to some of the previous talks from like
[15:21] outline guys which we were talking here
[15:24] yesterday uh yeah so finally try try it
[15:26] out and generally like how to get
[15:29] started in fireworks so if you had head
[15:31] out of fireworks a such models you'll
[15:33] you'll find a lot of uh open open source
[15:36] open wte models which I mentioned about
[15:38] they're available in the playground in
[15:40] terms of product offering uh we have
[15:42] this kind of range which can take you
[15:44] from early prototyping all the way to
[15:46] Enterprise scale so you can start with
[15:48] serverless inference which is you know
[15:49] not different from uh getting to open
[15:52] API open air playground or something
[15:54] where you pay per token uh it's a Conant
[15:57] price you don't need to worry about like
[15:59] Hardware settings or anything as I
[16:00] mentioned you can still do fine tune in
[16:02] so you can you can do host at fine tun
[16:04] our platform you can bring your own lur
[16:06] adapter and still serve with several L
[16:08] as you kind of graduate like maybe like
[16:09] a startup and you graduate to uh more
[16:12] production scale uh you might want to go
[16:14] to on demand where where it's more like
[16:16] dedicated Hardware with more settings
[16:18] and modifications uh for your use case
[16:20] uh you can Brint your own custom model f
[16:22] tune from scratch or do it on our
[16:24] platform and finally you kind of if you
[16:26] scale up uh to bigger volume and want to
[16:29] go to enter enter Enterprise level where
[16:32] it's kind discounted longterm longterm
[16:34] contracts and we also will help you to
[16:36] kind of personalize Hardware set up and
[16:38] do some of those tune in for performance
[16:40] which I which I talked about earlier and
[16:43] in terms of these cases I mean we're
[16:45] running production for uh for many many
[16:48] companies ranging from small startups to
[16:49] Big Enterprises we're serving like last
[16:52] time I checked like more than 150
[16:53] billion tokens per day so you know
[16:55] companies like quora built chat Bots
[16:58] like Po
[16:59] uh sour draft and cursor which I think I
[17:01] think cursor had a talk here yesterday
[17:03] they use us for like some of the code
[17:05] assistant functionality and their like
[17:06] latency is really important uh as you
[17:08] can imagine you know Fox like upstage
[17:11] liner building like different assistants
[17:13] and agents uh on top of that so uh we're
[17:17] definitely production ready go try try
[17:19] it out uh finally we care a lot about
[17:21] developers you uh you guys um so
[17:24] actually this is external numbers from
[17:27] uh like last year BL chain state of
[17:29] stuff where turns out we are one of the
[17:31] like after Hing pH the most popular
[17:34] platform for where people pull models
[17:35] which is great is was very nice to uh
[17:37] nice to hear and again for like for
[17:39] getting started just uh you know head
[17:42] out to head out to our website you can
[17:45] go in the go play in the playground uh
[17:47] right away so for example you can run
[17:49] you know Llama Or GMA or whatever at the
[17:51] at the top speeds um and kind of go
[17:54] start building from there I'm really
[17:56] excited to see what you can build with
[17:57] open models of Fire function or some
[18:00] stuff which you can uh which you can
[18:02] fune on on your own and yeah last point
[18:05] we're as I mentioned open a API
[18:07] compatible so you can still use you know
[18:09] your your favorite tools uh the same
[18:11] clients or you can use Frameworks like
[18:14] Len chain or Lama index or Etc so yeah
[18:17] really excited uh uh to kind of to be
[18:21] here and talk tell a little bit about
[18:23] open source uh open source models and
[18:25] how we had fireworks uh focusing on
[18:27] productionizing that and scaling it up
[18:30] uh go try it out and you can also find
[18:32] us at the Boost uh at the Expo thank you
[18:39] [Music]
