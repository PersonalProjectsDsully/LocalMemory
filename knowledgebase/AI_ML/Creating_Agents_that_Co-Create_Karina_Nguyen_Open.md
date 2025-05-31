---
type: youtube
title: Creating Agents that Co-Create — Karina Nguyen, OpenAI
author: AI Engineer
video_id: 1XvN5EBDnDw
video_url: https://www.youtube.com/watch?v=1XvN5EBDnDw
thumbnail_url: https://img.youtube.com/vi/1XvN5EBDnDw/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence Research
tags: ['AI', 'machine learning', 'reinforcement learning', 'Chain of Thought', 'human-AI collaboration', 'AI research', 'long context', 'tool use', 'complex reasoning', 'model training', 'interaction paradigms', 'AI development']
entities: ['OpenAI', 'GPT-4', 'Chain of Thought', 'reinforcement learning', 'human-AI collaboration', 'tools', 'long context', 'model training', 'interaction paradigms', 'complex reasoning']
concepts: ['reinforcement learning', 'Chain of Thought', 'interaction paradigms', 'complex reasoning', 'tool use', 'long context', 'human-AI collaboration', 'model training', 'problem-solving', 'AI research']
content_structure: discussion/opinion
difficulty_level: advanced
prerequisites: ['Understanding of AI models', 'Reinforcement learning fundamentals', 'Knowledge of Chain of Thought methodology']
related_topics: ['AI research', 'machine learning', 'natural language processing', 'human-computer interaction', 'AI ethics', 'tool integration', 'long-context modeling', 'AI collaboration']
authority_signals: ["One of the first projects that I've done at open a", 'we are only the beginning of it', 'the way we think about it is highly complex reason']
confidence_score: 0.8
---

# Creating Agents that Co-Create — Karina Nguyen, OpenAI

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=1XvN5EBDnDw)  
**Published**: 3 weeks ago  
**Category**: AI/ML  
**Tags**: ai-research, machine-learning, deep-learning, neural-networks, ai-agents, scaling-paradigms, pre-training  

## Summary

# Summary of "Scaling Paradigms and the Future of AI Agents"  

## **Overview**  
Karina Nguyen from OpenAI discusses two major AI research paradigms: **next token prediction** (pre-training) and **post-training** (e.g., RLHF, RLAF) for enhancing model capabilities. She highlights the evolution toward **complex reasoning** via Chain of Thought (CoT) and explores the future of AI agents as **co-innovators**, blending reasoning, tool use, and creativity through human-AI collaboration.  

---

## **Key Points**  
1. **Scaling Paradigms**  
   - **Next Token Prediction**: Models like GPT-4 learn by predicting the next token, acting as "world-building machines" through vast data.  
   - **Post-Training**: Techniques like RLHF (Reinforcement Learning from Human Feedback) and RLAF (Reinforcement Learning from AI Feedback) refine models for tasks like code completion, multi-line diffs, and problem-solving.  

2. **Chain of Thought (CoT)**  
   - A new paradigm where models simulate reasoning steps (e.g., solving medical problems) by scaling reinforcement learning.  
   - Challenges include ensuring **faithfulness** of CoT steps, detecting errors, and enabling self-correction.  

3. **Interaction Paradigms**  
   - Shifts from static responses to **streaming model thoughts** for real-time human collaboration.  
   - Design challenges include optimizing latency and communication efficiency.  

4. **Future of Agents**  
   - Moving beyond "collaborators" to **co-innovators** by integrating long-context reasoning, tool use (e.g., browsing, search), and creativity.  
   - Emphasizes **human-AI collaboration** as critical for enabling creativity.  

---

## **Key Quotes/Insights**  
- "The model is a world-building machine."  
- "Creative writing is hard to measure, but creativity requires human-AI collaboration."  
- "Chain of Thought is the future, but we’re only at the beginning of understanding its faithfulness."  
- "The next stage is agents that act as co-innovators, not just tools."  

---

## **Actionable Items**  
- Prioritize **post-training techniques** (RLHF, RLAF) to refine model capabilities.  
- Improve **Chain of Thought faithfulness** through better feedback mechanisms.  
- Develop **streaming interaction models** to reduce latency and enhance human-AI collaboration.  
- Focus on **human-AI creativity** by integrating tools, long-context reasoning, and iterative feedback.

## Full Transcript

[00:00] [Music]
[00:17] hey everyone my name is Karina and I'm
[00:20] an AI researcher at open AI before that
[00:24] I worked at antarik for about two years
[00:28] working on cloud so today I would love
[00:32] to chat more about what kind of scaling
[00:36] paradigms that has happened in the past
[00:39] two to four years in AI research and how
[00:41] those paradigms unlocked New Frontier
[00:44] product research I'm also going to share
[00:46] some of the vignettes from some of the
[00:49] lessons learned by developing claw and
[00:52] Chach PT products some design challenges
[00:56] and lessons um and how do I think about
[01:00] the future of Agents as they become from
[01:05] collaborators to co innovators um in the
[01:09] future I would also love to invite you
[01:12] to engage um in the conversation so I'd
[01:15] be more than happy to answer some of the
[01:17] questions at the
[01:19] end cool
[01:22] so not sure if probably the majority of
[01:25] you know this but I think there are two
[01:28] scaling paradigms that Hasen happened in
[01:30] AI research over the past few years the
[01:34] first Paradigm is the next token
[01:38] production and you might have heard this
[01:41] as called
[01:42] pre-training and what's really amazing
[01:46] about the next token prediction is that
[01:48] it's a World building machine the model
[01:51] learns to understand the World by
[01:53] predicting the next word and I think
[01:57] fundamentally if you think about it
[02:00] this is happening because certain
[02:02] sequence is caused by initial action and
[02:06] this is irreversible and so the model
[02:09] learns some of the physics of the world
[02:11] to understand and the token can be
[02:14] anything right the tokens that we pre-
[02:16] chained are strings words pixels it
[02:19] could be
[02:20] anything and so to predict what will
[02:24] happen next the model needs to
[02:27] understand how the world works and this
[02:29] is why
[02:30] raining worked and so you can imagine
[02:34] the next token prediction is the massive
[02:37] multitask
[02:39] learning and what's amazing about this
[02:42] is that during prating some tasks are
[02:45] really easy to learn such as translation
[02:48] right like the word boarding in French
[02:52] is the model also learns a lot about the
[02:56] world the capital of France is Paris and
[03:01] because some of the information is much
[03:03] more present on the internet and in some
[03:05] of the knowledge artifacts the model has
[03:08] much easier time to learn this but
[03:11] actually the reason why compute is so
[03:14] important and scaling Compu in the
[03:16] paining stage is so so important is
[03:19] because there is a new class there is a
[03:21] class of tasks that is really really
[03:24] hard to learn and for example the model
[03:27] learns a lot about the physics it learns
[03:30] so much about the problem solving
[03:32] generation and The Logical Expressions
[03:35] it learns some of the spal reasoning
[03:38] although it's not
[03:39] perfect um but we getting to the
[03:43] complexity of the tasks such as math
[03:46] when the model has to compute this
[03:49] number during the next token prediction
[03:52] is actually really high so that's why
[03:53] you need Chain of Thought or might spend
[03:57] more compute on the Chain of Thought
[04:00] to help the model to reason through more
[04:03] computational such tasks another class
[04:06] of tasks that I was thinking a lot about
[04:08] is creative writing it's actually really
[04:11] really hard and the reason why it's so
[04:13] hard for the model is because you know
[04:16] you can predict very nicely the style of
[04:19] the writing but a lot of the creative
[04:22] writing is actually World building and
[04:24] storytelling and the plot and it's much
[04:26] much easier for the model to make a
[04:28] mistake for the next token prediction in
[04:31] such a way where it will completely
[04:33] deteriorate the plot coherence which is
[04:35] really important for the stories and
[04:38] this is an open-ended like research
[04:40] problem um creative writing in itself
[04:44] and the reason why it's because it's
[04:46] really really hard to measure what is a
[04:48] good creative writing what is not a
[04:49] creative writing and obviously we would
[04:51] love for the models to invent new forms
[04:55] of writing and be extremely creative in
[04:59] their generation s but this is actually
[05:02] one of the hardest AI research problems
[05:05] today is um how do we make models to
[05:08] like write novels and have
[05:12] coherent stories over the long course of
[05:15] the period of
[05:17] time
[05:19] so I think the era of
[05:22] 2020 to 2021 that was an ER of scaling
[05:27] PR traing a lot both in at anic and at
[05:31] openi and actually the first at that
[05:34] time one of the first products was
[05:38] GitHub compilot and I thought it was
[05:40] completely interesting product the
[05:43] autocomplete because it's so imp paining
[05:46] the model has learned so much about the
[05:48] code and the next token prediction for
[05:51] The Code by the billions code tokens
[05:53] using from GitHub open source projects
[05:56] Etc and what has happened for the a
[05:59] complete tap to top in the cursor or
[06:02] gith Pilot is that the researchers
[06:06] constrained VI rhf reinforcement
[06:08] learning from Human feedback and
[06:10] reinforcement learning from AI feedback
[06:11] to make it extremely a little bit more
[06:13] useful to use and this is where the era
[06:16] of post training has gone off so in post
[06:23] training we teach the model how to
[06:24] complete function bodies understanding
[06:27] dog strings how to complete generating
[06:29] multi-line completions predicting the
[06:31] next diffs apply the next diffs and I
[06:35] think we are still in that era where
[06:37] there is so much more to be explored in
[06:39] the posttraining stage of rhf
[06:43] rlaf to push the capabilities and models
[06:47] to reason through complex code code
[06:51] basis the next Paradigm in AI
[06:54] research which has
[06:57] happened last year
[06:59] and and it was published by open a with
[07:01] a new model 01 is scaling reinforcement
[07:05] learning on Chain of Thought and this is
[07:08] why we call them it's highly complex
[07:12] reasoning and you can imagine you you
[07:15] spend a lot more test time
[07:17] comput on training in to scale
[07:21] reinforcement learning and the reason
[07:24] why it works is because the model learns
[07:27] how to think during the training and
[07:30] learn from the feedback by having really
[07:32] good signals in
[07:34] RL so on the left you can see the output
[07:38] of normal GPD 40 or
[07:41] gbd4 and on the right you can see the
[07:45] entire Chain of Thought that has been
[07:47] that the model has thought about to
[07:50] solve the complex problems and as we
[07:53] think about harder and harder tasks if
[07:55] you want the model to go from you know
[07:58] translation
[08:00] towards solving medical problems you
[08:02] actually need to spend you actually need
[08:04] the model to like spend a lot of time
[08:07] just thinking through the problem and
[08:11] completely creating more complex
[08:13] environments with tools and other other
[08:17] tools and more complex environments to
[08:19] think through and verify its outputs
[08:22] during the Chain of Thought So as you
[08:25] can see the chainnel thought itself is
[08:27] very interesting and the model is has
[08:31] certain words that it does um but um
[08:35] there's a lot of science to be done in
[08:37] terms of you know faithfulness in the
[08:40] Chain of Thought how do we measure the
[08:42] faithfulness what happens if the model
[08:46] goes into like wrong direction can it
[08:48] backtrack itself I think there was a lot
[08:51] of science around that and we are only
[08:52] the beginning of
[08:54] it one of the first projects that I've
[08:58] done at open a is actually how do
[09:02] we the interaction Paradigm is very
[09:05] different now so the interaction
[09:07] Paradigm is models thinks a lot to solve
[09:09] the problem if the problem is hard so
[09:12] but how do we create this interaction
[09:14] new interaction Paradigm with humans
[09:17] such that it will be much easier so that
[09:20] humans don't have to wait for 15 seconds
[09:24] or 30 minutes for a model to come back
[09:28] and one of the things that we did um as
[09:31] a simple approach is to have like a
[09:33] streaming models thoughts to a user and
[09:37] that way we had to communicate what
[09:40] exactly the summaries of the thoughts
[09:42] for the model and communicate very
[09:43] wisely to human but I think it's still
[09:46] one of the design challenges like as the
[09:47] model's capabilities and interraction
[09:49] paradigms change you have like new
[09:51] design challenges that you need to solve
[09:53] um for these types of
[09:57] models so and and I guess like this year
[10:01] open is the year of agents and the way
[10:03] we think about it is highly complex
[10:07] reason such as models trained on a and
[10:12] Chain of Thought using real world tools
[10:15] such as browsing search computer use uh
[10:20] over a long Horizon period of time over
[10:21] a long
[10:24] context but what's the next stage in my
[10:27] view the next stage stage level is co-
[10:31] innovators and the way I'm thinking
[10:33] about is it's agents that is built upon
[10:36] all the things that we've done with
[10:38] reasoning and Tool use and long context
[10:42] plus creativity and creativity is
[10:44] enabled only through human AI
[10:46] collaboration and I think this is where
[10:48] I'm really really excited about in the
[10:50] future is
[10:52] to create new affordances for humans to
[10:56] collaborate better with AI such that we
[10:59] both can co-create the future that we
[11:02] want and so those two scaling paradigms
[11:05] in AI research has unlocked us new kind
[11:08] of product research and you know you can
[11:12] imagine product research being oh we
[11:15] have API from the model and now we have
[11:18] to integrate in the products but it's
[11:20] actually what's happening on the ground
[11:22] is we have like a very now we have like
[11:24] a very nice rapid uation cycle of the
[11:27] product development and and the reason
[11:30] why is because we can use those highly
[11:33] reasoning models to distill back to
[11:38] smaller models or the models that we
[11:39] canate very very fast and we can use
[11:43] those highly complex reasoning models to
[11:46] synthetically generate new data such
[11:47] that we can create new post training new
[11:50] data sets new reinforcement learning
[11:53] environments so okay um so one of the
[11:57] things that we can do is is creating new
[12:00] completely new class of tasks and um you
[12:04] know if the task is um how do we create
[12:08] a multiplayer
[12:09] collaboration uh with a human nii you
[12:12] might want to simulate different users
[12:15] and how do you do that you might want to
[12:17] like synthetically generate data sets of
[12:21] different users conditioned on the
[12:22] different users and push chain on that
[12:26] so it actually highly depends on like
[12:28] what kind of product EXP experiences
[12:29] that you want to create and extrapolate
[12:33] that to a new class of tasks that you
[12:35] want to P the
[12:36] models um I think we are moving towards
[12:39] more complex reinforcement learning
[12:41] environments uh which means we can allow
[12:45] models to use search or browsing or much
[12:49] more collaborative tools like canvas
[12:52] during ourl such that they can learn how
[12:54] to be how to become better at
[12:57] collaborating um we can love things like
[13:00] in context learning I think models are
[13:03] extremely extremely good so you can
[13:04] essentially create something a new tool
[13:07] and then the model will learn just by
[13:09] few shot examples and this is extremely
[13:12] rapid uation cycle for any
[13:15] developer as I mentioned before
[13:17] synthetic data wide distillation is
[13:19] another thing I think we can also invent
[13:22] New Model Behavior and interactions to
[13:24] utilize user feedback so now we're going
[13:28] to go through for some of the Vettes
[13:30] that
[13:31] um that has happened um from Anar toi um
[13:37] I think the first concept that I've
[13:39] learned um is how do you bring
[13:41] unfamiliar capability into familiar from
[13:44] factor and the reason why 100K context
[13:47] uh was successful is because we found
[13:49] you know file uploads is extremely
[13:51] familiar from Factor everybody is
[13:54] working on documents but you can imagine
[13:57] we could have deployed 100 key content
[13:59] text via infinite chats such that it's
[14:01] like one huge long chat that you can
[14:04] interact with but I think finding the
[14:07] simplest form practice sometimes for
[14:08] unfamiliar capability uh is one of the
[14:11] design challenges uh in this new
[14:15] era the next project that I worked uh
[14:19] one the second project that I was I
[14:21] worked on at open is called Chach tasks
[14:24] um and actually I did not realize about
[14:26] this until it was shipped um you know
[14:30] reminders and tasks schedule tasks is
[14:34] actually it's very familiar thing that
[14:36] people do almost every day but what's
[14:39] amazing about this product is that you
[14:41] can scale this with new kind of
[14:44] capabilities and the models so CHP task
[14:47] is not just scheduled reminders and
[14:49] to-do lists it's actually you can create
[14:53] you can ask the model to continue the
[14:55] story every day for you H or you can ask
[14:58] the model model to
[15:00] search everything that you are
[15:02] interested in every day or every other
[15:04] every other day so in a way you can also
[15:08] like help yourself to like learn new
[15:10] language by having like extremely
[15:13] multimodal and interactive visualization
[15:15] that CH can create and so I I think this
[15:19] is concept of your product feature
[15:21] should enable modular compositions that
[15:24] will scale very nicely in the future as
[15:25] the models will develop much higher
[15:28] capability is um is one of the is is
[15:32] something that I've learned by doing
[15:33] chpt
[15:35] tasks um I think another design
[15:39] challenge that we have here is how do we
[15:42] Bridge together real-time interaction
[15:44] with models to a synchronous task
[15:47] completion and where we can ask the
[15:50] model to go off for like 10 hours to
[15:53] research or write code and then come
[15:55] back with the
[15:56] solution and the bottleneck here is
[16:00] trust and I believe
[16:02] that giving trust can be solved by
[16:05] giving humans new collaborative
[16:07] ordinances to verify edit model outputs
[16:11] and having them to give models realtime
[16:14] feedback so that the model can self
[16:17] improve and you know one of the first
[16:21] products uh from antar was actually CLA
[16:24] and slack and it was the first attempt
[16:26] to have a virtual teammate in your
[16:28] organization
[16:29] and it was an amazing concept because
[16:32] slack had all the affordances with tools
[16:34] and image uploads and multiplayer
[16:36] collaboration that you can
[16:38] create and there is something in there
[16:41] that is still I think there is still a
[16:44] lot of things that we can do here and
[16:46] take the lessons from clent slack to the
[16:49] next generational products um again the
[16:53] task was also like very much inspired by
[16:56] cloud and slack prototypes when Claud
[16:59] could just summarize channels slack
[17:02] channels across the organization every
[17:04] Friday and have a summaries for
[17:08] everybody my first project at open was
[17:12] canvas
[17:14] and I thought that human collabary
[17:17] affordances could scale and create new
[17:20] creative capabilities and what I really
[17:23] loved about the canvas and the way we
[17:25] operate in canvas as a team is that it
[17:29] was extremely flexible interface that we
[17:32] could come up with and here here are
[17:36] some like the vignettes that we had so
[17:38] the canvas itself can become like
[17:40] co-creator and co-editor and you can
[17:42] have like a very very fine grain editing
[17:45] uh interaction the model can also do
[17:47] search in order to generate the report
[17:50] and then you can also ask a question
[17:51] back hi verify this output and you can
[17:55] imagine this interface scales to
[17:57] multiplayer when other people can join
[17:59] your document or even multi-agents if I
[18:03] can create a model critic or an editor
[18:06] they can use you have like a multi-
[18:08] agentic and multiplay collaboration at
[18:10] the same time and so this is like a new
[18:12] design challenge that we need to
[18:13] navigate how do we do that I'm also
[18:16] excited for personalized tutors I think
[18:18] the models care are becoming extremely
[18:21] multimodal extremely flexible that you
[18:24] can learn new things in a new way the
[18:28] way you like like if I'm a visual
[18:29] learner and you are a more auditory
[18:32] learner the model can adapt to your
[18:35] personalization sorry um one thing that
[18:39] uh I did yesterday is that
[18:44] um I was on the plane and actually I
[18:47] used canvas to create me a game and so I
[18:50] really like this genor entertainment on
[18:52] the
[18:53] [Music]
[18:54] Fly anyone can create their own tools
[18:57] and VB apps now
[18:59] and I'm not sure what the future will
[19:01] look like but I think it will be
[19:03] extremely amazing if a non a person who
[19:08] never had to touch code ever before in
[19:10] their life for the first time can create
[19:12] the tool that they really wanted and
[19:14] deploy that um for themselves or to
[19:18] start a business from scratch and I
[19:21] think there's something around pair
[19:24] programming and code creators that we
[19:28] can
[19:29] use in order to create the future that
[19:31] we want and so canvas has also become
[19:34] mooo a PR programmer so the reason why
[19:36] canvas is so flexible is because it was
[19:39] ad it was trained both to become
[19:41] collaborative for writing and
[19:45] coding because it has tools such as
[19:49] search and can search for AP
[19:53] documentation it can become a data
[19:55] scientist too and especially if you
[19:58] upload the entire CSV docs um it can
[20:02] generate a real time um
[20:07] analysis and finally what I'm really
[20:09] really excited what everybody is excited
[20:10] in the ey is how do we
[20:12] actually help models to become better at
[20:17] research um and creating new
[20:21] knowledge and here you can see that the
[20:25] model that the model in the human can
[20:28] co-create document or co-create a new
[20:30] artifact that has never been happened
[20:34] before so here's a demo of the paper
[20:38] that I've co-published and then um I'm
[20:41] asking the model to kind of reproduce it
[20:44] and you can imagine this is like one of
[20:46] the maybe one of the most common tasks
[20:48] in research is to reproduce or you can
[20:51] imagine reproduce like open source
[20:53] GitHub repo and you you have like this
[20:57] very nice Interactive
[21:00] Paradigm where because the model can
[21:03] also leverage its own internal
[21:05] knowledge you and a you and a AI can
[21:10] work together to come up with new
[21:13] research hypotheses and verify certain
[21:16] like research um directions together and
[21:20] you can also handle delegate the tasks
[21:22] to an AI assistant to do
[21:26] that finally what are I'm really excited
[21:29] about the future is that there will be
[21:32] this layer of invisible software
[21:34] creation for all um and especially what
[21:38] I'm really excited is like from the
[21:40] mobile itself people can just create
[21:42] their own software
[21:44] tools I think the way you interact with
[21:48] AI fundamentally changes in a way that
[21:51] the way you access the internet will
[21:53] also change my prediction is that you
[21:56] will click less and less on the internet
[21:59] links and the way you will access the
[22:01] internet will be why models lens which
[22:03] will be much cleaner and in a much more
[22:06] personalized way and uh you can imagine
[22:09] have like very personalized multimodel
[22:10] outputs let's say if I say I want to
[22:13] learn more about the solar system
[22:14] instead of it giving me a text output it
[22:17] should give you a 3Gs interactive
[22:21] visualization of the solar system and
[22:24] you can have like highly richly
[22:26] interactive features to learn more and I
[22:30] think there is there'll be this like
[22:32] kind of cool future of like generator
[22:33] entertainment on the
[22:34] Fly for the people to learn and share
[22:38] new games with other
[22:40] people I think the way I'm thinking
[22:42] about it is the kind of interface to AI
[22:46] is is blank canvas that kind of self
[22:48] mores into your intent so for example
[22:52] you come to the work today and your
[22:55] intention is to just write code then the
[22:59] canvas becomes more of an IDE like a
[23:02] cursor or like a coding IDE although the
[23:05] future programming might change or if
[23:08] you're a writer and you decided to write
[23:11] a Noel together the model can start
[23:14] creating tools on the Fly for you such
[23:17] that it will be much easier for you to
[23:19] brainstorm or edit the writing or create
[23:23] character plots and
[23:24] visualize the structure of the plot
[23:27] itself and finally I think the
[23:31] co-innovation is actually going to
[23:33] happen with co-direction creative
[23:35] c-direction with the models itself and
[23:37] it's through
[23:39] collaboration with highly reasoning
[23:41] agenda systems uh that will be extremely
[23:45] capable of superum tasks to create new
[23:49] novels films games uh and essentially
[23:53] new science new knowledge
[23:56] creation cool um um thank you so much I
[24:00] think that's the end of my talk um
[24:08] [Music]
