---
type: youtube
title: AI Agents, Meet Test Driven Development
author: Channel Video
video_id: U3MVU6JpocU
video_url: https://www.youtube.com/watch?v=U3MVU6JpocU
thumbnail_url: https://img.youtube.com/vi/U3MVU6JpocU/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence Development
tags: ['Test-Driven Development', 'AI Product Development', 'Prompt Engineering', 'Model Agnosticism', 'AI System Evaluation', 'Continuous Monitoring', 'Domain Expertise Integration', 'AI Scalability', 'OCR Optimization', 'AI Experimentation Frameworks', 'Machine Learning Workflow', 'AI Trade-off Analysis']
entities: ['Anita', 'Vum', 'Gemini 2.0 Flash', 'React', 'Test-Driven Development', 'Chain of Thought', 'Prompt Engineering', 'AI Agents', 'OCR', 'Model Agnosticism']
concepts: ['Test-Driven Development for AI', 'AI Product Development', 'Prompting Techniques', 'Model Agnosticism', 'Trade-off Analysis in AI', 'Continuous Monitoring', 'Proof of Concept Experimentation', 'Domain Expert Involvement', 'AI System Evaluation', 'Scalability Testing']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with prompting techniques', 'Knowledge of test-driven development (TDD) principles', 'Experience with AI tooling (e.g., Gemini)']
related_topics: ['AI Model Optimization', 'Continuous Integration in AI', 'Prompt Engineering Best Practices', 'AI System Scalability', 'Machine Learning Operations (MLOps)', 'Domain-Specific AI Development', 'AI Ethics and Privacy', 'Agentic AI Workflows']
authority_signals: ["The best AI teams that I've seen follow this structured approach", "We've seen work really well lately", "Engineers shouldn't be the ones who are tweaking prompts"]
confidence_score: 0.85
---

# AI Agents, Meet Test Driven Development

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=U3MVU6JpocU)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: test-driven development, ai agents, machine learning, model deployment, software development, reinforcement learning, ai systems  

## Summary

# Comprehensive Summary of "AI Agents, Meet Test Driven Development"

## Overview  
Anita from Vum discusses how test-driven development (TDD) can enhance the reliability of AI systems, particularly in agentic workflows. She highlights the evolution of AI tools, the limitations of models, and the importance of structured approaches to build robust AI products. The video emphasizes balancing model capabilities with workflow design and continuous improvement.

---

## Key Points  
1. **Evolution of AI Tools**:  
   - Tools like Cursor AI demonstrate the growth of AI in productivity.  
   - Models face challenges like hallucinations, overfitting, and scalability.  

2. **New Training Methods**:  
   - Real reinforcement learning and techniques like Chain of Thought improve reasoning.  
   - Domain-specific models (e.g., Gemini 2.0 Flash for OCR) optimize performance.  

3. **Test-Driven Development (TDD) Stages**:  
   - **Experimentation**: Test prompting techniques (e.g., few-shot, Chain of Thought) and agentic workflows (e.g., REACT).  
   - **Evaluation**: Create datasets to balance quality, cost, latency, and privacy.  
   - **Scaling**: Prioritize trade-offs based on use cases (e.g., high quality vs. speed).  
   - **Continuous Improvement**: Monitor and refine workflows post-deployment.  

4. **Critical Practices**:  
   - Involve domain experts to avoid over-reliance on engineers for prompt tuning.  
   - Stay model-agnostic to leverage the best tools for specific tasks.  

---

## Important Quotes/Insights  
- *"The best AI teams follow a structured approach: experiment, evaluate, scale, and never stop improving."*  
- *"Success isn’t just about models—it’s about the surrounding workflow."*  
- *"No AI system gets quality, cost, latency, and privacy perfect; trade-offs are inevitable."*  
- *"The humanities last exam benchmark shows models still struggle with complex reasoning."*  

---

## Actionable Items  
1. **Experiment with techniques**:  
   - Test prompting methods (few-shot, Chain of Thought) and agentic workflows (REACT).  
   - Involve domain experts to validate use cases early.  

2. **Model Agnosticism**:  
   - Use multiple models (e.g., Gemini 2.0 Flash for OCR) to match task requirements.  

3. **Data-Driven Evaluation**:  
   - Build test datasets to simulate production-scale challenges.  
   - Prioritize trade-offs (e.g., quality vs. cost, speed vs. privacy).  

4. **Continuous Monitoring**:  
   - Capture responses post-deployment to iteratively improve workflows.  

--- 

This summary captures the core strategies and insights from the video, emphasizing the importance of TDD in creating reliable, scalable AI systems.

## Full Transcript

[00:00] hi everybody my name is Anita and I'm
[00:02] currently leading gen growth and
[00:04] education here at vum and over the last
[00:06] few years we worked with hundreds of
[00:08] companies who have successfully deployed
[00:10] reliable AI Solutions in production from
[00:13] simple to more advanced agentic
[00:15] workflows one thing became very clear
[00:18] those companies who have adopted a test
[00:20] driven development approach were able to
[00:22] build reliable and stronger systems for
[00:25] production today I'm excited to share
[00:28] how you can apply that same approach to
[00:30] build your own effective agentic
[00:32] workflow that actually works but before
[00:35] we jump in let's take a step back and
[00:37] truly understand how we got here in the
[00:39] first place I'm so excited to get
[00:41] started let's do it so let's go back to
[00:44] 2023 everyone was building AI rappers
[00:47] and most people argued that there is no
[00:50] defensibility strategy around them and
[00:52] fast forward to today we have cursor AI
[00:55] which is the most popular and wildly
[00:57] used AI powered IDE that just hit 100
[01:01] million AR in just 12 months this is the
[01:05] fastest growing SAS in the history of
[01:07] SAS so why and how did this happen
[01:11] because models got better at coding sure
[01:14] because AI adoption skyrocketed that's
[01:17] absolutely correct because coding was an
[01:19] obvious first Target that was supposed
[01:21] to be disrupted by these AI models there
[01:24] is no doubt about that but more
[01:26] importantly we built new techniques and
[01:29] patterns on how how we can orchestrate
[01:31] these models to work better sync better
[01:33] with our data and then work effectively
[01:35] in production we rely on these
[01:38] techniques because there are clear
[01:39] limits to model performance
[01:41] hallucinations is still a thing
[01:43] overfitting is still a problem and
[01:45] developers needed more structured
[01:46] outputs and while model providers
[01:48] started to ship better tooling to Sol
[01:51] for all of this we didn't see another
[01:53] lip similar to the lip between GPD 3.5
[01:57] and gp4 these big jumps started to slow
[02:01] down and for years making models bigger
[02:04] and fitting them more data kept making
[02:06] them smarter but then we hit a wall no
[02:10] matter how much more data we added these
[02:12] improvements started to slow down and
[02:14] models started to reach their limits on
[02:17] existing test but is this true did we
[02:20] really hit that wall seems like there
[02:24] were some other avenues and new trining
[02:27] methods that we still haven't explored
[02:29] and so let's see what happened next so I
[02:32] don't really think that there is an
[02:33] issue here because since then and this
[02:35] happened in the last two to 3 months
[02:38] we've seen some new training methods
[02:39] that push the field forward for example
[02:42] we got the Deep seek R1 model which is
[02:45] the first model that was trained without
[02:47] using any labeled data we call this
[02:50] method real reinforcement learning and
[02:53] this means that this model was able to
[02:55] learn on its own reportedly this is what
[02:58] open used to train their reasoning
[03:01] models like 01 and 03 and all these
[03:03] reasoning models today they use Chain of
[03:06] Thought thinking at inference time or at
[03:09] response time to generate their answers
[03:12] in turn allowing these models to think
[03:15] before they give an answer to our
[03:17] questions it enables them to really
[03:20] solve more complex reasoning problems on
[03:23] top of this we're seeing all of these
[03:24] model providers to provide more
[03:27] capabilities to their models like use of
[03:30] tools more capabilities for research um
[03:33] near perfect OCR accuracy when it comes
[03:35] to the Gemini 2.0 Flash and really
[03:38] expand the field forward however
[03:41] traditional benchmarks are so saturated
[03:44] so people are starting to introduce new
[03:46] ones that will really capture the
[03:48] performance of these new reasoning
[03:50] models for example The Benchmark that
[03:52] you're currently seeing on the slide
[03:53] here the humanities last last exam it
[03:56] measures performance on truly difficult
[03:58] tasks so if you check the table on the
[04:01] slide you can clearly see that even the
[04:03] latest very smart models struggle with
[04:06] these challenges so yeah models are
[04:08] getting better the field is moving
[04:10] forward but for an AI product that
[04:13] actually works in production success
[04:15] isn't just about the models anymore it's
[04:17] about how you build around it and that's
[04:20] exactly what's been evolving in parallel
[04:23] to model training so we were learning
[04:25] how to prompt all of these models better
[04:27] and we developed more Advanced
[04:29] Techniques like Chain of Thought then we
[04:31] thought that we should be able to ground
[04:33] all of this models responses using our
[04:36] own data so rag became an important part
[04:39] of our workflows then we learned that
[04:42] for multi-threaded conversations memory
[04:45] is going to be the most important thing
[04:47] that we've had long context from the
[04:50] latest models enabled new use cases then
[04:52] we started to think about hierarchy of
[04:54] our responses so we started to
[04:56] experiment with graph rack and then just
[04:59] lately we're thinking about using all
[05:01] this reasoning models that in fact will
[05:03] take a lot more time to think in real
[05:06] time however it also develops new areas
[05:09] and use cases that we can develop and
[05:12] lately we're thinking about a gentic rag
[05:14] making our workflows even more powerful
[05:17] so that all this can work on its own and
[05:20] the field is still evolving but even
[05:22] using these techniques isn't enough you
[05:24] need to understand your problem deeply
[05:27] and take a test driven development
[05:29] approach to find the right mix of
[05:31] techniques models and logic that will
[05:34] actually work for your use case and this
[05:37] actually brings me to the main first
[05:40] topic of this presentation test driven
[05:43] development for building reliable AI
[05:46] products because the best AI teams that
[05:49] I've seen follow this structured
[05:52] approach they start to experiment then
[05:54] they evaluate it scale then finally when
[05:57] they deploy in production they never
[05:59] stop stop working on their workflow they
[06:01] capture all of those responses to then
[06:03] continuously monitor observe and improve
[06:06] their product for their customers let's
[06:09] look at what you can do at every stage
[06:12] of this process before you build
[06:14] anything production grade you need to
[06:16] experiment a lot you need to prove
[06:18] whether these AI models can actually
[06:20] solve for your use case so you should
[06:23] try different prompting techniques for
[06:24] example fuse shot or Chain of Thought
[06:27] some of these will work great for simple
[06:28] tasks and other will help with a bit
[06:31] more complex reasoning you should test
[06:33] various techniques prom chaining is
[06:35] usually very uh well received because
[06:38] it's going to work better if you split
[06:39] your instructions in multiple prompts or
[06:41] you can adopt a more agentic workflows
[06:44] like react that will have a stage to
[06:46] plan and then reason and refine before
[06:49] it actually gives you an answer what is
[06:51] really an important part in this stage
[06:53] is that you need to involve your domain
[06:55] experts um because Engineers shouldn't
[06:57] be the ones who are tweaking prompts uh
[07:00] and bringing all these experts will
[07:01] actually save a lot of your engineering
[07:03] time because once you do this phase
[07:06] right then you will actually have a
[07:08] proof that this works and that
[07:10] engineering time needs to be involved at
[07:13] this stage you should also stay model
[07:15] agnostic uh you should incorporate and
[07:17] has different models and especially when
[07:19] it comes to your use case you need to
[07:20] think about Which models can do the job
[07:23] better so in such case you can um maybe
[07:25] use some uh different uh models like
[07:28] Gemini 2.0 flash which is actually
[07:30] really well at OCR uh and something that
[07:33] we've seen work really well lately so
[07:35] let's say that at this stage you know
[07:37] that U these AI models can actually work
[07:40] you have a few examples that these
[07:41] models have like really good performance
[07:44] on but how can you test whether this
[07:46] will actually work in production when
[07:49] you will potentially have hundreds if
[07:51] not thousands or millions of requests
[07:53] per minute and so this is where
[07:55] Evolution comes in in this stage you
[07:57] actually create a data set of hundreds
[08:00] of examples that you're going to test
[08:01] your models and workflows against and so
[08:03] at this stage you need to uh try to
[08:06] balance quality and cost and latency and
[08:08] privacy and you're definitely going to
[08:10] make a lot of tradeoffs because no AI
[08:12] system is going to get all of this
[08:14] perfectly but for example if you need
[08:16] high quality maybe you can sacrifice
[08:19] speed if cost is critical you might need
[08:21] some lighter and cheaper model and this
[08:24] is the stage where where you need to
[08:25] Define your priorities because it's
[08:27] always better if you define your
[08:29] priorities earlier in the process you
[08:32] should use ground through data where
[08:34] possible if you want to evaluate all
[08:36] these workflows having your subject
[08:38] matter experts design these databases
[08:41] and test these models and workflows
[08:42] against is going to be very very useful
[08:46] synthetic benchmarks help however they
[08:48] will not really evaluate these models
[08:51] for your own use case so it's usually
[08:53] very very powerful if you can use your
[08:56] ground through data but don't worry even
[08:58] if you do not have ground through data
[09:00] you can use an llm to evaluate another
[09:04] model's response this is actually a very
[09:07] standard and reliable way when it comes
[09:10] to evaluating your
[09:11] models very importantly at this stage
[09:14] you should make sure that you're using a
[09:16] flexible testing framework no matter if
[09:19] you're building this in house or if
[09:21] you're using any external service your
[09:23] AI isn't static so your workflow should
[09:26] also be dynamic it should be able to
[09:28] capture all of this different
[09:30] non-deterministic responses you need to
[09:32] be able to Define custom metrics you
[09:34] need to be able to write those metcs
[09:37] metrics using python or typescript so
[09:40] you shouldn't be looking at a very
[09:42] strict framework customizability is a
[09:44] very big thing here and then finally you
[09:48] should run evaluations at every stage
[09:50] you should have guard rails that will
[09:52] check internal nodes and whether these
[09:54] models are actually producing responses
[09:56] at every step in your uh workflow
[09:59] actually producing responses that are
[10:01] correct at every step in your workflow
[10:03] and then you should also test while your
[10:05] prototyping but then you should also
[10:07] utilize this evaluation phase to come
[10:10] back once you have some real data but
[10:13] how are you going to get some real data
[10:15] so let's say that you evaluate your
[10:17] workflows extensively with your subject
[10:19] matter experts with your data that
[10:21] they've created and let's say that
[10:23] you're now satisfied with the product
[10:25] that you have so you're ready to deploy
[10:27] it in production so once that that
[10:29] happens what do you need to do is your
[10:32] job done here when it comes to AI
[10:35] development you need to monitor more
[10:37] things than deterministic outputs you
[10:39] need to log all llm calls you need to
[10:42] track all of those inputs and outputs
[10:44] and the latency because AI models they
[10:47] really they're really really
[10:49] unpredictable so you need to be able to
[10:51] debug issues and understand how your AI
[10:53] behaves at every step of the way and
[10:56] this is becoming extremely more
[10:58] important with a gentic workflows
[11:00] because gentic workflows are more
[11:02] complex workflows that can take
[11:04] different paths in your workflow and
[11:06] make decisions on their own you should
[11:09] also handle API reliability you need to
[11:12] maintain uh stability in your API calls
[11:14] you need to have retries you need to
[11:16] have fallback logic to prevent outages
[11:19] for example two months ago open AI had
[11:22] four hours of downtime so if you had a
[11:24] fallback logic in your productionize
[11:27] solution then your um AI will know to go
[11:31] back to another model and use another
[11:33] model instead you should definitely have
[11:35] Version Control and staging and you
[11:37] should always deploy in control
[11:39] environments before you roll out to The
[11:41] Wider uh public because with it when it
[11:44] comes to AI you need to be care careful
[11:47] that once you update a prompt you're not
[11:49] introducing a regression to another
[11:52] prompt or part of your workflow so you
[11:54] need to ensure that all these new
[11:56] updates they won't break whatever you
[11:58] have in production and the most
[12:00] important part here is that make sure to
[12:02] decouple your deployments from your
[12:05] scheduled app deployment schedule
[12:08] because the chances are that um you will
[12:11] need to update your AI features more
[12:14] frequently that you will need to update
[12:16] your app as a whole so make sure to do
[12:19] that and so let's say that now you have
[12:21] deployed you're starting to capture all
[12:24] of your responses from your users and
[12:26] create a feedback loop to identify edge
[12:29] cases that you capture in production to
[12:32] then continuously improve and make your
[12:35] workflow better you can capture all of
[12:38] these then run evaluations again and
[12:41] test whether um new prompts that you
[12:43] develop will solve for this new cases
[12:46] you should also think about building a
[12:47] caching layer because if your system is
[12:50] handling some repeat queries caching can
[12:52] drastically reduce costs and improve
[12:54] latency so for example instead of
[12:56] calling an expensive llm for the same
[12:59] request multiple times you can store and
[13:01] serve frequent responses instantly and
[13:03] this is something that is a standard
[13:05] these days when it comes to building
[13:07] with AI and finally let's say that your
[13:09] product has been running reliably in
[13:11] production for uh a longer period of
[13:14] time time that you feel comfortable to
[13:16] then go back to that data and use it to
[13:19] fine-tune a custom model that will um
[13:22] basically uh create better responses for
[13:24] your specific use case uh can reduce
[13:27] Reliance on API calls and in fact can
[13:29] work with lower costs and so this
[13:34] process is becoming even more important
[13:36] than ever when it comes with agentic
[13:39] workflows because these workflows are
[13:41] going to use a wide range of tools they
[13:43] will um call different apis they will
[13:48] have multi-agent structures that will
[13:51] execute a lot of things in parallel so
[13:53] when it comes to evaluation with a
[13:55] gentic workflows and with this test
[13:57] driven approach it's not just just about
[13:59] measuring performance at every step in
[14:01] your workflow because you also need to
[14:03] assess the behavior of these agents to
[14:06] so that you can make sure that they're
[14:08] making the right decisions and following
[14:10] the intended logic and this year more
[14:13] than ever everyone is talking about
[14:15] agentic workflows but what does that
[14:17] actually mean uh I would love to talk
[14:19] more about how you can build all this
[14:21] agentic workflows but I'm not here to
[14:24] give you the perfect definition of what
[14:26] an AI agent is and instead I'm going to
[14:29] try to Define different agentic
[14:30] behaviors and some different levels on
[14:33] how um they can be built so if you think
[14:36] about it every AI workflow has some
[14:40] level of ener gentic behavior in it it's
[14:43] just a question of how much control
[14:45] reasoning and autonomy it has so we've
[14:48] looked at the past the present and where
[14:50] we're headed and from that we put
[14:53] together this framework where we Define
[14:55] four or five different levels of gentic
[14:58] behav Behavior I'll go into more details
[15:01] on each level but keep in mind that this
[15:03] is not a final framework it's not set in
[15:06] stone as models evolve this can expand
[15:09] the things can blur and um a lot of
[15:11] things can shift but for now this will
[15:14] give us a way to define where we are
[15:16] today and what we expect to see next at
[15:19] this stage you have an llm call you
[15:21] retrieve some data from your vectory
[15:23] database and then you might have some
[15:25] inline evals and finally you're going to
[15:28] uh get some response from this workflow
[15:30] so you can notice that in this workflow
[15:32] there's no reasoning planning or
[15:33] decision making Beyond what's baked into
[15:36] the prompt and the Model Behavior so the
[15:38] model is doing all the reasoning here
[15:40] within the prompt itself and so there is
[15:43] no external agenda organizing uh the
[15:46] decisions or planning some actions
[15:48] however there is some reasoning and some
[15:49] agentic Behavior at the models level and
[15:52] so if we move from l0 to L1 we can see
[15:56] that in this stage our workplace can now
[15:59] use a lot of tools and so this EA System
[16:02] is no longer just calling apis it no now
[16:05] knows when to call them and when to make
[16:08] those actions and so this is where we
[16:10] start to see more gentic Behavior
[16:13] because the model can decide whether uh
[16:15] it will call a specific tool or whether
[16:18] it will call our Vector database to
[16:20] retrieve more data before it actually uh
[16:23] generates an output memory here starts
[16:25] to play a key role because we're going
[16:27] to have multi-threaded uh conver
[16:28] conversations and then uh all of this
[16:31] will potentially happen in parallel so
[16:33] we need to capture all context
[16:35] throughout the whole workflow evaluation
[16:37] is also needed at every state uh step of
[16:40] the way here because we need to ensure
[16:42] that this models are making the right
[16:44] decisions using the right tools and
[16:47] returning uh accurate responses but this
[16:50] workflows can be as simple as on the
[16:52] slide right here or even more
[16:54] complicated where you're going to have
[16:56] more different branching happen uh
[16:58] happens at every stage in this workflow
[17:00] where you can have 10 different tools
[17:02] and the agent needs to reason whether
[17:04] it's going to call the first five or the
[17:06] or the last two and so this is uh where
[17:09] again we see a lot more agentic Behavior
[17:12] but L2 is where we actually see that um
[17:15] these workflows now move from simple
[17:18] tool use which is not in many cases it's
[17:20] not a simple tool use like the previous
[17:23] workflows can be very complex but now we
[17:26] see some structured reasoning this work
[17:28] workflow will notice triggers it can
[17:31] plan actions and it can execute tasks in
[17:35] a structured sequence so this means that
[17:37] it can break down a task into multiple
[17:39] steps it can retrieve some information
[17:41] it can decide to call another tool it
[17:43] can evaluate its usefulness if it thinks
[17:45] that it needs to be refined at that
[17:47] stage and once it does this in a
[17:49] continuous loop it can generate the
[17:52] final output but um you can notice that
[17:55] atic behavior here starts to look more
[17:57] intentional because the system isn't
[17:59] just calling the tools that are listed
[18:02] uh for their use it's also actively
[18:05] deciding what needs to be done and
[18:07] spending more time to think what needs
[18:09] to be done instead of just deciding
[18:11] whether a tool should be called and so
[18:13] at this stage um one part is that the
[18:16] process is still finite so once this
[18:19] workflow completes the steps um as it
[18:22] plans to complete them it will terminate
[18:24] rather than it will run continuously but
[18:27] it's a Leap Forward
[18:29] um from just calling uh tools and so uh
[18:33] L3 however is where we see more autonomy
[18:36] where we see more uh decision making
[18:39] that are not um defined by us as the
[18:43] creators of this workload so the L for
[18:45] system can proactively take actions
[18:48] without waiting for direct input so
[18:50] instead of responding responding to a
[18:52] single request and then terminating this
[18:54] one will stay alive and will
[18:56] continuously monitor its environment and
[18:59] it will react as needed so for example
[19:02] um this means that it can uh look at
[19:04] your email slack Google drive or any
[19:06] other Tool uh external Services actually
[19:09] that you can give access to and it can
[19:11] plan its next moves whether it will
[19:13] execute actions in real time or asks uh
[19:16] the human for more input and so this is
[19:19] where uh our AI workflows become less of
[19:22] a tool and more of an independent system
[19:25] that we can use to truly make our work
[19:28] easier so for example this one can be
[19:30] like a marketer that will prepare this
[19:33] video or a presentation that you can
[19:34] just take and use whenever you want
[19:38] however the final stage is where we're
[19:39] going to have a fully creative workflow
[19:41] and so at L4 the AI moves between uh
[19:45] Beyond Automation and reasoning and it
[19:47] becomes an inventor so instead of just
[19:50] executing predefined tasks or just like
[19:53] reasoning within some bounds um it can
[19:56] create its own new workflows so it can
[19:58] create its own utilities whether it's
[20:00] agents prompts function calls tools that
[20:03] uh it needs to be designed uh it will
[20:06] Pro it will solve problems in novel way
[20:08] so well true L4 right now is definitely
[20:12] Out Of Reach because there's some
[20:14] constraints with models like overfitting
[20:16] because models they really love their
[20:18] training data and there is some issues
[20:20] with uh inductive bias where models will
[20:23] make assumptions again based on their
[20:25] training data this makes to be like a
[20:28] very hard task ask uh today but that's
[20:30] the goal AI that doesn't just follow
[20:32] instructions but will invent it will
[20:35] improve and it will solve problems in
[20:37] ways we didn't even think of before so I
[20:40] would say that L1 is where we're seeing
[20:42] a lot of production grade Solutions so
[20:44] at Bellum we've worked with companies
[20:46] like redin dra and headspace all of
[20:48] which have deployed production grade AI
[20:50] solutions that fall within the L1
[20:53] segment and again like just using tools
[20:56] it can be very simple or it can be very
[20:58] complex workflow uh the focus is though
[21:01] on orchestrations how do we turn our
[21:04] models to interact with our system
[21:07] better how do we make our models to work
[21:09] with our data better how do we make sure
[21:11] that whatever we retrieve from our
[21:13] Vector databases is the right and
[21:15] correct context for the uh question that
[21:18] the user is asking and so like we're
[21:21] experimented with different modalities
[21:22] and all of those techniques that we
[21:23] mentioned before and test driven
[21:25] development truly makes its case here
[21:28] because like you need to hack different
[21:30] tools and models and you need to be able
[21:32] to continuously improve on them to build
[21:34] not only a more efficient system But A
[21:36] system that will work continuously
[21:38] better and better um however L2 is where
[21:41] I think we're going to see most
[21:42] Innovation uh happen this year and this
[21:45] is where we're going to have a lot of AI
[21:47] agents that are being developed to plan
[21:49] and reason using models like 01 or O3 or
[21:53] deep sick uh we might see a bunch of
[21:56] different use cases we might see a lot
[21:58] of Innovations when it comes to the UI
[22:01] and the ux part of the system where we
[22:04] will definitely create some new
[22:05] experiments experiences for users and um
[22:09] essentially this will be uh a way for us
[22:12] to make true reasoners that will handle
[22:15] complex tasks so you're going to have
[22:17] bunch of these agents just working for
[22:19] you doing uh different things however L3
[22:22] and L4 they're still both limited by the
[22:25] models today as well as the surrounding
[22:27] logic however however that doesn't mean
[22:30] that uh there's a lot of innovation
[22:32] happening within those two as well so if
[22:34] you want to learn more about how to
[22:35] build your own uh AI agent I've included
[22:38] everything that I've shared in this
[22:39] presentation and more for example uh
[22:42] architectures that you can build what
[22:44] are the stages that you can test and
[22:46] similar things like that we also feature
[22:48] top researchers and professionals who
[22:50] have shared all of their learnings on
[22:52] how to build these for production so
[22:54] feel free to scan this QR code on the
[22:57] screen to download this resource so now
[23:00] I think it's time to get more practical
[23:02] I want to show you how I built my own
[23:04] SEO agent this specific agent automates
[23:07] my whole SEO process from keyword
[23:09] research to content analysis and finally
[23:12] for Content creation it decides whether
[23:14] to use tools and has an embedded
[23:16] evaluator that works on an Editor to
[23:18] tell the agent if it's doing a good job
[23:20] let's see a quick sketch of how this
[23:22] agent works so in a minute I'm going to
[23:25] show you a real demo on how this agent
[23:27] actually works however I wanted to give
[23:29] you a high level overview on what are
[23:31] the steps that this workflow will take
[23:34] and so when you look at the sketch on
[23:35] the screen right now you're going to
[23:37] notice that this workflow lies between
[23:39] L1 and L2 type of agentic workflow you
[23:43] have the SEO analyst and the researcher
[23:45] who will take a keyword and it will call
[23:47] Google search and it will analyze the
[23:50] top performing articles for that keyword
[23:52] one it will identify some of the good
[23:54] parts uh Within These articles that we
[23:57] also need to amplify in our own article
[24:00] but it will also Identify some missing
[24:02] segments or areas of improvement that we
[24:05] should definitely write about to make
[24:07] sure that our article is actually
[24:09] performing better than the ones that
[24:11] we're competing against and then after
[24:13] the research and planning is done the
[24:15] writer has everything it needs to start
[24:17] writing the first draft what then the
[24:19] first draft is passed to the editor
[24:21] which is an llm based judge that will
[24:24] evaluate whether the first draft is good
[24:26] enough based on predefined rules that
[24:29] we've set in its prompt then that
[24:31] feedback is passed back to the rouer and
[24:33] this will Loop uh continuously until
[24:37] some uh criteria is met uh within this
[24:40] Loop we also have a memory component
[24:42] that will capture all previous
[24:44] conversations between the writer and the
[24:46] editor and finally we're going to get a
[24:49] final article that's actually a very
[24:51] useful um piece of content that it's not
[24:54] a generated and not useful but truly
[24:57] using all of this context in a Smart Way
[25:00] enabling me to have a pretty impressive
[25:02] first draft to work with so now let's
[25:05] see the demo for the sake of time I'm
[25:07] going to start running this workflow as
[25:09] I explain what this agent does at every
[25:12] step in the workflow so we ran this
[25:14] workflow with the keyword Chain of
[25:16] Thought prompting and so the SEO analyst
[25:19] currently is taking that keyword is
[25:21] taking some other parameters like my
[25:22] writing style like the audience that
[25:24] we're trying to cater to and it analyzes
[25:27] the top articles that Google is ranking
[25:29] for that specific keywords it tries to
[25:31] identify some good components from those
[25:34] articles that we need to reinforce in
[25:36] our article but it also identifies some
[25:38] missing opportunities where the
[25:40] researcher is going to utilize those to
[25:43] then make another search and capture
[25:45] more data to make our article be better
[25:48] than the articles that we just analyzed
[25:50] so now that the SEO analyst uh is done
[25:53] with its job the researcher tries to
[25:56] capture more information about the
[25:58] things that um were previously
[26:00] identified as missing pieces to the
[26:02] puzzle and then the writer will take a
[26:05] lot of this information in its input and
[26:07] it will try to create a great first
[26:09] draft using that data as context so the
[26:13] content here that will be generated by
[26:15] the writer it's not going to be like a
[26:16] slop type of article it's not going to
[26:19] be something that it's really not useful
[26:21] it's going to actually use all the
[26:23] context that we're sending from
[26:25] different articles that we just analyzed
[26:27] you can also connect your rack here that
[26:29] it will look into your database of
[26:31] Articles and learnings and it can really
[26:33] create something that's extremely useful
[26:36] now the editor says okay this is a good
[26:38] enough article but here's some feedback
[26:40] and so it passes the feedback through
[26:42] the memory component here which is a
[26:44] chat history between these two and then
[26:46] um this node that uh basically
[26:48] structures that input for the sake of
[26:51] this demo the conditional here for the
[26:54] loop is that this Loop will break if the
[26:57] evaluator actually tells us that this is
[26:59] an excellent post which actually rarely
[27:01] happens so um we also said that if the
[27:05] loop runs for at least one time this
[27:08] Loop will break and so it already ran
[27:10] for one time we got still more feedback
[27:12] from the editor but in this case for
[27:14] this demo let's look at the output that
[27:17] we got so mastering Chain of Thought
[27:19] prompting in AI a comprehensive guide
[27:21] for developers I think it's pretty okay
[27:24] pretty nice I might change the title but
[27:26] I know that the components this article
[27:29] are the actual components that other
[27:31] articles are writing about and so uh
[27:34] this was great the latency was around
[27:36] 118 this usually takes around 300
[27:38] seconds to run when we have more
[27:40] evaluation Loops but it's pretty great
[27:42] it gives me some foundations on how I
[27:45] can continue to build on this content
[27:47] and it saves me a lot of my time so the
[27:49] product that I just used is called
[27:51] Bellum workflows and it was designed to
[27:53] bridge the gap between the product and
[27:54] Engineering teams so they can speed up
[27:56] AI development well still following this
[27:59] test driven approach that we talked so
[28:02] much about in this presentation however
[28:04] one thing became clear developers want
[28:07] more code developers want more control
[28:09] and flexibility and they want to own
[28:11] their definitions in their codebase so
[28:13] today I'm excited to introduce our
[28:14] workflow SDK it provides all the
[28:17] building blocks you need it's infinitely
[28:19] customizable and it has a
[28:21] self-documenting syntax where you can
[28:24] actually spot how this agent is working
[28:26] right in your code it's also also
[28:28] expressive enough so that you can
[28:30] understand what's happening at every
[28:31] stage in your code the best part is that
[28:34] the UI and the code stay in sync so
[28:36] whether you're defining debugging or
[28:38] improving your workflows everyone on
[28:40] your team can stay aligned I hope that
[28:43] you like it it's open source and free
[28:45] and you can check it out on GitHub feel
[28:47] free to run uh to scan this QR code uh
[28:50] to check out the repo and that's a wrap
[28:53] thank you so much for listening and I
[28:54] hope that today you learned something
[28:56] new if you want to talk more about AI I
[28:58] feel free to scan this QR code on the
[29:00] screen to connect on LinkedIn or if you
[29:02] have any questions feel free to um send
[29:05] me a text message on my email or on
[29:07] Twitter I'm GNA follow up for sure
