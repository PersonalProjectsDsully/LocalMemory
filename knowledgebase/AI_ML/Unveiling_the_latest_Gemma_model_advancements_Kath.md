---
type: youtube
title: Unveiling the latest Gemma model advancements: Kathleen Kenealy
author: Channel Video
video_id: Xmkl27AM2VQ
video_url: https://www.youtube.com/watch?v=Xmkl27AM2VQ
thumbnail_url: https://img.youtube.com/vi/Xmkl27AM2VQ/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['Gemma models', 'AI development', 'machine learning', 'natural language processing', 'model architecture', 'open-source AI', 'multimodal systems', 'deep learning', 'large language models', 'code generation', 'inference optimization', 'parameter scaling']
entities: ['Kathleen', 'Gemma 2', 'Gemma 1.1', 'Recurrent Gemma', 'Sig lip Vision encoder', 'TensorFlow', 'Jack', 'Transformers', 'P Gemma', 'Gemma V2']
concepts: ['multimodality', 'instruction following', 'code generation', 'model architecture', 'inference efficiency', 'document understanding', 'parameter scaling', 'fine-tuning', 'context handling', 'open-source collaboration']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of machine learning models', 'Familiarity with deep learning frameworks (e.g., TensorFlow)', 'Knowledge of natural language processing concepts']
related_topics: ['AI model development', 'machine learning architecture', 'natural language processing', 'deep learning frameworks', 'model optimization techniques', 'open-source AI projects', 'multimodal systems', 'large language models']
authority_signals: ['we have been working very hard on these models since Gemma 1.0 launch date', 'we tried to do as much as we could to gather feedback from the community', "Gemma 2 isn't just powerful it's designed to easily integrate into the workflows"]
confidence_score: 0.85
---

# Unveiling the latest Gemma model advancements: Kathleen Kenealy

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=Xmkl27AM2VQ)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai research, machine learning, open source, deep learning, google deepmind, model advancements, neural networks  

## Summary

# Summary of "Unveiling the Latest Gemma Model Advancements" by Kathleen Kenealy

## Overview  
Kathleen Kenealy, a research engineer at Google DeepMind and technical lead of the Gemma team, highlights the open-source Gemma model family's mission to empower developers through advanced AI capabilities. The talk emphasizes Gemma's focus on safety, performance, and community-driven innovation, with recent updates including multimodal support, improved code generation, and larger parameter variants.

---

## Key Points  
- **Google's Open-Source AI Legacy**: Google has long prioritized open-source collaboration, with Gemma designed to accelerate community-driven AI development.  
- **Gemma's Core Features**:  
  - **Responsible Design**: Rigorous data curation ensures high-quality, safe training data.  
  - **Performance**: Gemma 2 outperforms models twice to three times its size, with enhanced instruction-following and chat capabilities.  
  - **Extensibility**: Compatible with frameworks like TensorFlow, JAX, and Transformers, enabling seamless integration into existing workflows.  
  - **Open Access**: Free availability of pre-trained and fine-tuned models for diverse use cases.  
- **Model Variants**:  
  - **Gemma 1.0**: Foundational LLMs.  
  - **Code Gemma**: Optimized for code generation and evaluation.  
  - **Recurrent Gemma**: A novel architecture for faster, efficient inference at long contexts.  
  - **P Gemma**: Multimodal model combining a vision encoder (Siglip) and text decoder for tasks like image captioning and object detection.  
  - **Gemma V2**: New 9B and 27B parameter versions with significant performance gains.  
- **Community-Driven Updates**: Feedback from the open-source community directly influenced improvements in Gemma 2, including better instruction-following and workflow compatibility.

---

## Key Quotes  
- *"We built Gemma to empower and accelerate the amazing work being done by the open-source community."*  
- *"We are manually inspecting data sets to ensure we’re training on the highest quality and safest data."*  
- *"Gemma 2 outperforms models that are two to three times larger than these base models."*  
- *"The open-source community is the most passionate developers there are."*

---

## Actionable Items  
1. **Explore New Variants**: Leverage P Gemma (multimodal) and Gemma V2 (9B/27B) for advanced tasks like image-text processing and high-performance applications.  
2. **Upgrade Workflows**: Developers using Gemma 1.0 can easily switch to Gemma 2 with minimal code changes for enhanced performance.  
3. **Engage with the Community**: Participate in feedback loops to shape future model improvements.  
4. **Utilize Framework Compatibility**: Take advantage of Gemma’s support for TensorFlow, JAX, Transformers, and other tools for seamless integration.

## Full Transcript

[00:00] [Music]
[00:13] my name is Kathleen canel I'm a research
[00:16] engineer at Google Deep Mind and as was
[00:19] just mentioned I'm the technical lead of
[00:21] the Gemma team before I get started I
[00:24] just wanted to say uh how awesome it is
[00:27] to get to be here with you all today
[00:30] when we were building Gemma our North
[00:33] Star the the thing we were most excited
[00:35] about was building something to empower
[00:38] and accelerate the amazing work being
[00:40] done by the open source community and
[00:44] since we launched our first models in
[00:46] February I have been absolutely Blown
[00:49] Away by the incredible projects and
[00:52] research and and innovations that have
[00:55] been already been built on top of Gemma
[00:58] um so I'm particularly excited to be
[01:00] here with so many developers today and
[01:04] especially delighted to unveil the
[01:06] latest advancements and additions to the
[01:09] Gemma model family so without further
[01:12] Ado we'll get
[01:14] started as many of you probably know
[01:17] Google has been a Pioneer in
[01:20] publications of AI and ml research for
[01:23] the past decade including publishing
[01:26] some of the key research that has
[01:28] sparked recent innov ations we've seen
[01:30] in AI research like the transformer
[01:34] senten piece Bert to name a few Google
[01:38] Deep Mind has really continued this
[01:40] tradition and is actively working to
[01:43] share our research for the world to
[01:46] validate and examine and build upon but
[01:49] Google's support of the open Community
[01:51] for AI and ml is not just limited to
[01:54] publishing research we've also been
[01:56] doing work to support ml across the
[01:59] entire technical stack for a long time
[02:02] from Hardware breakthroughs of tpus um
[02:05] which I imagine is especially relevant
[02:07] for this crowd in this track um all the
[02:10] way to an evolution in ml Frameworks
[02:13] from tensorflow to Jax through out all
[02:16] of this open development has been
[02:19] especially critical for Google our
[02:21] ability to collaborate with the open
[02:23] source Community has helped us all
[02:27] discover more innovate faster
[02:30] and really push the limits of what AI is
[02:33] capable of so this long history of
[02:36] support of the open source Community
[02:38] leads us to today and to Google's latest
[02:41] investment in open models Gemma Gemma is
[02:46] Google deep Minds family of open-source
[02:49] lightweight state-of-the-art models
[02:52] which we build from the same research
[02:54] and technology used to create the Gemini
[02:56] models I'm so sorry I think that's my
[02:59] phone off during this talk please feel
[03:02] free to rumage through that bag wow
[03:05] lesson learned that even the speaker
[03:07] needs to remember to silence her cell
[03:09] phone all right back to Gemma there are
[03:13] a couple of key advantages of the Gemma
[03:15] models that I want to highlight today
[03:18] the first is that Gemma models were
[03:20] built to be responsible from by Design I
[03:23] can tell you from personal experience
[03:26] that from day Zero of developing a Gemma
[03:29] model safety is a top priority that
[03:32] means we are manually inspecting data
[03:35] sets to make sure that we are not only
[03:37] training on the highest quality data but
[03:40] also the safest data we can this means
[03:43] that we are evaluating our models for
[03:45] safety starting with our earliest
[03:48] experimentation and ablations so that we
[03:50] are selecting training methodologies
[03:53] methodologies that we know will result
[03:55] in a safer model and at the end of our
[03:58] development our final model models are
[04:00] evaluated against the same rigorous
[04:03] state-of-the-art safety evaluations that
[04:05] we evaluate Gemini models against and we
[04:08] really do this to make sure that no
[04:12] matter where or how you deploy a Gemma
[04:14] model you can count on the fact that you
[04:17] will have a trustworthy and responsible
[04:19] AI application no matter how you've
[04:21] customized Gemma models you can trust
[04:24] that it will be a responsible
[04:26] model Gemma models also achieve un
[04:29] unparalleled breakthrough performance
[04:32] for models of their scale including
[04:35] outperforming significantly larger
[04:38] models but we'll get some more on that
[04:40] very
[04:42] shortly we also designed the Gemma
[04:44] models to be highly extensible so that
[04:47] you can use a demo model wherever and
[04:50] however you want this means they're
[04:52] optimized for tpus and gpus as well as
[04:55] for use on your local device they're
[04:57] supported across many Frameworks cancer
[04:59] flow Jack Caris pytorch olama
[05:03] Transformers you name it Gemma is
[05:05] probably there and finally the real
[05:08] power of the Gemma models comes from
[05:11] their Open Access and open
[05:13] license that period that's what's
[05:16] powerful about Gemma we put
[05:18] state-of-the-art technology into your
[05:21] hands so you can decide what the next
[05:23] wave of innovation looks
[05:25] like when we decided to launch the Gemma
[05:28] models we wanted to make sure that we
[05:30] could meet developers exactly where they
[05:32] are which is why gemo models are
[05:35] available anywhere and everywhere you
[05:38] can find an open model I will not list
[05:41] all of the Frameworks on this slide but
[05:43] this is only a fraction of the places
[05:45] where you can find Gemma models today
[05:48] this means you can use Gemma how you
[05:50] need it when you need it with the tools
[05:53] that you prefer for
[05:56] development since our initial launch
[05:58] back in February we've added a couple of
[06:01] different variants to the Gemma model
[06:02] family we of course have our initial
[06:05] models Gemma 1.0 which are our
[06:07] foundational llms we also released
[06:11] shortly after that code Gemma which are
[06:13] the Gemma 1.0 models fine tuned for
[06:16] improved performance on code generation
[06:18] and code
[06:19] evaluation and one variant that I am
[06:22] particularly excited about is recurrent
[06:24] Gemma which is a novel architecture a
[06:27] state space model that's designed for
[06:30] faster and more efficient inference
[06:32] especially at long
[06:34] contexts we've also updated all of these
[06:38] models since their initial release we
[06:40] now have Gemma 1.1 which is better at
[06:43] instruction following and chat we've
[06:45] updated code Gemma to have even more
[06:47] improved code performance and we now
[06:50] have recurrent Gemma not not only the
[06:52] original 2B size but also at a 9 billion
[06:55] parameter
[06:57] size so there's a lot going on in the
[07:01] Gemma model family and I'm especially
[07:03] excited to tell you about our two most
[07:06] recent
[07:07] launches um the first one is actually
[07:10] our most highly requested feature since
[07:13] day Zero of launch and that was
[07:18] multimodality so we launched P Gemma P
[07:22] Gemma oh thank you I appreciate
[07:25] it this is why I love the open source
[07:28] Community truly the most passionate
[07:30] developers that there are P Gemma is a
[07:33] combination of the Sig lip Vision
[07:35] encoder combined with the Gemma 1.0 text
[07:39] decoder this combination allows us to do
[07:42] a variety of image text sort of tasks
[07:46] and capabilities including question
[07:48] answering image and video captioning
[07:51] object detection and object
[07:54] segmentation the model comes in a couple
[07:56] of different variants it's currently
[07:58] only available at the two V size but we
[08:00] have pre-trained weights that are
[08:02] available that can be fine-tuned for
[08:04] specific tasks we have a couple of
[08:06] different fine-tuned variants as well
[08:08] that are already targeted towards things
[08:10] like object detection and object
[08:12] segmentation and we also have transfer
[08:15] checkpoints that are models that are
[08:17] specialized to Target a couple of
[08:19] academic
[08:22] benchmarks up until this morning that
[08:25] was our latest release but I'm very
[08:28] excited to be here today with you guys
[08:31] because it is Gemma V2 launch day
[08:36] woohoo wow
[08:38] thanks we have been working very hard on
[08:42] these models since Gemma 1.0 launch date
[08:46] we tried to do as much as we could to
[08:48] gather feedback from the community to
[08:50] learn where the 1.0 and 1.1 models fell
[08:54] short and what we could do to make them
[08:56] better and so we created Gemma 2 Gemma 2
[09:00] comes in both a 9 billion parameter size
[09:03] and a 27 billion parameter size both
[09:06] models are without a doubt the most
[09:10] performant of their size and both models
[09:13] also
[09:14] outperform models that are even two to
[09:17] three times larger than these base
[09:20] models but Gemma 2 isn't just powerful
[09:23] it's designed to easily integrate into
[09:25] the workflows that you already have
[09:27] existing so Gemma 2 uses all of the same
[09:31] tools all of the same Frameworks as
[09:33] Gemma 1 which means if you've already
[09:35] started developing with Gemma one you
[09:38] can with only a couple of lines of code
[09:41] automatically switch to using the Gemma
[09:43] 2 models and have increased performance
[09:46] and um more power behind your
[09:49] applications we also have the same broad
[09:52] framework compatibility again tensorflow
[09:55] Jacks Transformers AMA all of the ones I
[09:58] previously named we have them for Gemma
[10:00] 2 as well we also have significantly
[10:04] improved documentation we have more
[10:06] guides more tutorials so that we can
[10:09] coach you through how to get started not
[10:10] only with inference but with Advanced
[10:13] and efficient fine-tuning from day Zero
[10:17] and finally we really wanted to Target
[10:19] fine-tuning as one of the key
[10:21] capabilities of these models we did
[10:24] extensive research into how our core
[10:28] modeling decision
[10:30] impact users ability to do Downstream
[10:32] fine-tuning so we believe these models
[10:34] are going to be incredibly easy to find
[10:37] tune so you can customize them to
[10:39] whatever your use case may
[10:42] be in addition to make it especially
[10:44] easy to get started using Gemma 2 models
[10:48] we have made the 27b model available in
[10:51] Google AI Studios this means you can go
[10:53] to the AI Studio homepage and select
[10:56] Gemma 2 now if you wanted to and start
[11:00] playing around with prompts right away
[11:02] you shouldn't have to do anything except
[11:05] come up with an idea for how you want to
[11:06] push the limits of our model I am I am
[11:10] especially excited to see what you all
[11:12] end up doing with AI Studios and Gemma
[11:16] um and we have a couple of different
[11:18] ways for you to let us know what you're
[11:19] building which I'll get to down the road
[11:22] um but if you have ideas I'll be here
[11:24] all day and want to hear what you're
[11:26] doing with the Gemma
[11:28] models but let's dive a little bit more
[11:30] into performance we are incredibly proud
[11:35] of the models that we've made as I
[11:37] mentioned they are without a doubt the
[11:39] best most performant models of their
[11:41] size and are also competitive with
[11:44] models two to three times larger so our
[11:47] 27b model is has performance in the same
[11:51] ballpark as llama
[11:53] 370b and outperforms grock models on
[11:57] many benchmarks by a fairly sign
[11:59] significant margin in some cases um but
[12:03] I think academic benchmarks are only
[12:06] part of the way that we evaluate Gemma
[12:08] models sometimes these benchmarks are
[12:10] not always indicative of how a model
[12:13] will perform once it's in your hands so
[12:15] we've done extensive human evaluations
[12:18] as well where we find that the Gemma
[12:20] models are consistently heavily
[12:24] preferred to other open models including
[12:27] larger open models um and I'm also proud
[12:30] to say that the Gemma 27b model is
[12:34] currently the number one open model of
[12:36] its size and it currently outranks llama
[12:40] 370b neotron 340b Gro claw three many
[12:46] many other models as well um thank you
[12:52] wow you guys are very supportive I
[12:54] appreciate
[12:55] it um the only other open model of any e
[12:59] size that outperforms the Gemma 27b
[13:02] model is the E large model on on LMS um
[13:07] so we expect that you should have some
[13:09] fun playing around with it especially
[13:11] for chat applications we found in our
[13:13] evaluations that the Gemma 2 models are
[13:16] even better at instruction following
[13:18] they're even more creative they're
[13:20] better at factuality better all around
[13:23] than the geml 1.0 and 1.1
[13:26] models the other important thing that I
[13:29] want to make sure to highlight from our
[13:32] most recent launch is the Gemma cookbook
[13:35] current the Gemma cookbook is available
[13:36] on GitHub now and contains 20 different
[13:39] recipes of ranging from easy to very
[13:42] Advanced applications of how to use the
[13:44] Gemma models and the thing that I am
[13:47] most excited about is the Gemma cookbook
[13:49] is currently accepting poll requests so
[13:52] this is a great opportunity to share
[13:55] with us what you're building with the
[13:57] Gemma models and so we can help share it
[14:00] with the rest of the
[14:01] world and of course I have to say we
[14:05] also wouldn't mind if you start the
[14:06] repository come go take a look and tell
[14:08] us what you're building with
[14:10] Gemma so there are a couple of different
[14:13] ways you can get started with the Gemma
[14:15] to models of course I just mentioned the
[14:17] cookbook you can also apply to get uh
[14:20] gcp credits to accelerate your research
[14:24] using Gemma 2 we have a lot of funding
[14:27] available to support research I would
[14:30] really encourage you to fill out an
[14:32] application regardless of how small or
[14:35] big your project is we also as I
[14:38] mentioned have significantly improved
[14:40] documentation we have many guides
[14:43] tutorials collabs across every framework
[14:46] so you can get started doing inference
[14:47] fine-tuning and evaluation with Gemma 2
[14:50] models you can download them anywhere
[14:52] open models are available and please
[14:55] chat with us on Discord or other social
[14:58] media channels so we can learn more
[15:00] about what you're
[15:02] building and that's about all from me
[15:05] today I am so excited to see what you
[15:09] all build with Gemma I have been working
[15:12] on this project for almost two years now
[15:17] and started working on this project
[15:19] because I as a researcher in Academia
[15:22] was disappointed to see how far behind
[15:26] open foundational llms were compared to
[15:29] the rapid improvements we were seeing in
[15:31] proprietary models so this is something
[15:34] that's very near and dear to my heart
[15:36] and that I wish I had had when I was
[15:40] actively part of the open source
[15:41] community so I'm very excited to see the
[15:44] projects and the research that you all
[15:46] do with these models please engage with
[15:48] us on social media on GitHub on hugging
[15:51] face here at the event and let us know
[15:55] what you think of the models let us know
[15:57] what you think we can do better for next
[15:59] time and thank you all very much really
[16:03] appreciate your time
[16:07] [Applause]
[16:09] [Music]
