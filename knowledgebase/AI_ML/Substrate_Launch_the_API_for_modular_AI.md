---
type: youtube
title: Substrate Launch: the API for modular AI
author: AI Engineer
video_id: x8HbIJh2wpQ
video_url: https://www.youtube.com/watch?v=x8HbIJh2wpQ
thumbnail_url: https://img.youtube.com/vi/x8HbIJh2wpQ/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI API', 'modular systems', 'inference optimization', 'SDK development', 'AI architecture', 'computation graphs', 'machine learning tools', 'distributed AI', 'AI product development', 'model orchestration']
entities: ['Substrate', 'Channel Video', 'Subrate', 'JSON', 'SDK', 'inference engine', 'AI products', 'computation graph']
concepts: ['modular AI systems', 'computation graph abstraction', 'inference run optimization', 'latency reduction', 'system verifiability', 'AI product development', 'distributed compute coordination', 'multi-modal intelligence nodes']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with API development', 'Knowledge of inference runs in AI systems']
related_topics: ['AI system architecture', 'API design patterns', 'Machine learning optimization', 'Distributed computing frameworks', 'Modular software development', 'AI deployment strategies']
authority_signals: ["we've been working with private clients for about a year now", "I'm incredibly proud of the work we've done so far", "we've invested a lot into offering a best-in-class Json mode"]
confidence_score: 0.85
---

# Substrate Launch: the API for modular AI

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=x8HbIJh2wpQ)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai development, modular ai, api integration, machine learning, sdk tools  

## Summary

# Substrate Launch: The API for Modular AI Summary

## Overview  
The video introduces *Substrate*, a new API designed to streamline modular AI development by enabling efficient, flexible, and scalable systems of inference runs. The speaker highlights how modern AI products increasingly rely on combining multiple models and tasks, and Substrate aims to simplify this process through a unified framework that prioritizes speed, legibility, and extensibility.

---

## Key Points  
- **Modular vs. Monolithic AI**: Substrate emphasizes the superiority of modular systems over monolithic models, enabling easier debugging, verification, and scalability.  
- **Two Core Components**:  
  - A developer SDK for describing computation graphs across multiple AI nodes (e.g., text, image, code, JSON).  
  - An inference engine optimized for running these graphs efficiently.  
- **Performance Advantages**:  
  - Substrate reduces latency by transferring data between nodes in microseconds (10,000x faster than traditional API calls).  
  - Static and dynamic optimizations (batching, caching, concurrency) improve scalability.  
- **JSON Decoding Focus**: Substrate prioritizes reliability and speed in JSON-based workflows, a common pattern in multi-inference tasks.  
- **Use Cases**: Supports tasks from document summarization to end-to-end coding, with a focus on complex, structured AI workflows.  

---

## Important Quotes/Insights  
- *"Building with modular intelligence is always going to be more effective than building with a monolithic intelligence."*  
- *"The best products right now are all using systems of inference runs in a logical structure."*  
- *"Substrate is a new way to enable higher quality outcomes with AI, letting you work in a system that's more flexible, legible, and verifiable."*  

---

## Actionable Items  
- Visit the **Expo floor** to learn more and scan the QR code for credits.  
- Explore the **website** (substrate.run) for details.  
- Contact the team via **email** (rob@substrate.run) for inquiries.

## Full Transcript

[00:00] [Music]
[00:13] yeah it's really good to be here um this
[00:15] is a particularly exciting talk for us
[00:17] because we've been working with private
[00:20] clients for about a year now but this is
[00:21] the first time we've really talked about
[00:23] it in public um since our launch last
[00:26] week um I'm incredibly proud of the work
[00:30] we've done so far and um excited to take
[00:33] a few minutes to tell you about it um so
[00:36] if you look at the products out there
[00:38] that have really successfully leveraged
[00:40] this generation of AI I think one thing
[00:42] is true about nearly all of them is that
[00:46] they're using more than one inference
[00:48] runs often many different types of
[00:50] models in tandem to accomplish a
[00:52] specific kind of task really well
[00:55] and I think people really quickly
[00:57] realize that the foundation model is not
[01:00] enough and even very simple tasks like
[01:04] summarizing a document to much much more
[01:07] complex task like solving coding
[01:09] problems end to end I think the best
[01:11] products right now are all using systems
[01:14] of inference runs in a logical structure
[01:18] so I think at subrate we believe that
[01:21] building with modular intelligence is
[01:24] always going to be more effective than
[01:26] building with a monolithic intelligence
[01:29] um these systems are inherently more
[01:32] legible which means you can understand
[01:34] them structurally which means that
[01:35] they're debuggable and they're
[01:37] extensible and evals become a lot easier
[01:41] because the decision trees are explicit
[01:43] and you can sort of verify at every step
[01:46] what's going on and what's going wrong
[01:49] um
[01:50] so substrate I think is a is sort of New
[01:54] Way new approach to this um I think our
[01:57] model is sort of fast in ways that other
[01:59] paradigms can't be it's sort of flexible
[02:02] enough to build any AI product out there
[02:05] and it works a scale by default so what
[02:08] is it um I think at its core substrate
[02:11] is a coupling of two things first I
[02:15] think it's a really elegant developer
[02:17] SDK that lets you describe a computation
[02:21] graph over any number of nodes um and
[02:25] the abstractions here are are really
[02:27] General and so we have we have a bunch
[02:29] of intelligence nodes across all the
[02:32] modalities that you might care about
[02:34] which is like generating images
[02:35] transcribing speech generating text Json
[02:38] embeddings executing code um but second
[02:43] substrate is also an inference engine
[02:46] specifically built to run these
[02:48] computation graphs as efficiently as
[02:50] possible um so these graph
[02:52] representations here um are it's a
[02:57] representation of many tasks and their
[02:58] relationships and since we run a very
[03:01] coordinated compute cluster um we can
[03:04] statically and dynamically optimize
[03:06] things like batching caching sort of
[03:10] networking concurrency physical
[03:12] placement um which really makes a big
[03:14] difference uh and if you look at most
[03:16] Frameworks out there um they're
[03:18] typically involving dispatching a bunch
[03:20] of API calls separately and if you look
[03:23] at what happens mechanically when you do
[03:25] that it's every step means you've got to
[03:28] resolve DNS you've got to go through
[03:29] through proxies you've got it through
[03:31] authentication like balance checks um
[03:36] and all of that sort of adds hundreds of
[03:39] milliseconds of latency on every single
[03:41] step and if you contrast that with
[03:43] substrate we we transfer data from node
[03:46] to node process to process on the order
[03:48] of microseconds which is some 10,000
[03:50] times faster meaning that it's actually
[03:52] feasible now to run online applications
[03:55] that involve dozens of nodes um we've
[03:59] also notice that Json decoding is is one
[04:02] of the most useful patterns for multi-
[04:04] inference runs and I think we've
[04:06] invested a lot
[04:08] into offering a a best-in-class um Json
[04:11] mode both in terms of reliability and
[04:14] speed and if you look at all of this
[04:17] together I think what it means is that
[04:19] substrate is is is really a way that way
[04:22] to enable higher quality outcomes with
[04:25] AI letting you work in a system that's
[04:29] more flexible it's more legible it's
[04:31] more verifiable than any of the current
[04:33] paradigms that sort of exist now um I
[04:37] think there's a lot more to say there
[04:39] all the time I really have today it's
[04:41] only 5 minutes um but if you're curious
[04:45] um please come out and say hi on the
[04:47] Expo floor um you can scan this QR code
[04:51] we and get some credits um and go to the
[04:55] website se. run um or give me an email
[04:58] at uh Rob at St straight down run
[05:04] [Music]
