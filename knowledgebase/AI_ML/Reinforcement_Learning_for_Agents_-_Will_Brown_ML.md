---
type: youtube
title: Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley
author: Channel Video
video_id: JIsgyk0Paic
video_url: https://www.youtube.com/watch?v=JIsgyk0Paic
thumbnail_url: https://img.youtube.com/vi/JIsgyk0Paic/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['reinforcement learning', 'AI model development', 'synthetic data', 'open source models', 'model scaling', 'agent systems', 'NLP techniques', 'test time scaling', 'distillation', 'RLHF', 'machine learning trends', 'AI research']
entities: ['DeepSeek', 'R1 model', '01 models', 'Reinforcement Learning from Human Feedback (RLHF)', 'synthetic data', 'open source models', 'distillation', 'test time scaling', 'Mistral', 'LLaMA']
concepts: ['reinforcement learning', 'pre-training', 'synthetic data', 'distillation', 'verification in the loop', 'rejection sampling', 'exploration and exploitation', 'problem-solving strategies', 'long chain of thought', 'model scaling']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['basic understanding of machine learning', 'familiarity with reinforcement learning', 'knowledge of NLP techniques']
related_topics: ['AI model development', 'reinforcement learning', 'synthetic data generation', 'model distillation', 'test time scaling', 'open-source AI models', 'agent systems', 'model training techniques']
authority_signals: []
confidence_score: 0.8
---

# Reinforcement Learning for Agents - Will Brown, ML Researcher at Morgan Stanley

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=JIsgyk0Paic)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: reinforcement-learning, machine-learning, ai-research, agents-systems, open-source, multi-agent, llm  

## Summary

# Video Summary: Reinforcement Learning for Autonomous Agents

## Overview  
Will Brown, a researcher from Morgan Stanley, discusses the role of **reinforcement learning (RL)** in advancing **autonomous agents** beyond current large language models (LLMs). The talk emphasizes the shift from chatbots and reasoners to systems that can **interact with environments, learn strategies, and improve over time**. Key themes include the limitations of current models, the potential of RL, and the resurgence of open-source efforts.

---

## Key Points  
- **Agents vs. Pipelines**:  
  - **Agents** are systems that interact with environments to achieve goals, learning strategies through trial and error.  
  - **Pipelines** are static workflows (e.g., prompt engineering) that lack adaptability.  
  - Current LLMs are often limited to "chatbot" or "reasoner" roles, not true agents.  

- **Model Limitations**:  
  - Pre-training shows diminishing returns, and synthetic data alone isn’t sufficient for breakthroughs.  
  - RL from Human Feedback (RLHF) improves chatbot friendliness but doesn’t push models toward higher intelligence.  

- **RL as a Solution**:  
  - RL focuses on **exploration and exploitation** (trying new strategies, refining based on feedback).  
  - DeepSeek’s R1 model demonstrated that **RL can unlock "test-time scaling"** (improving performance via iterative feedback), not just pre-training.  
  - Long chain-of-thought reasoning in models like 01/R1 emerges naturally from RL, not manual programming.  

- **Open-Source Revival**:  
  - Open-source models (e.g., replication of 01/R1) are gaining traction, enabling smaller, efficient models through distillation.  
  - Community efforts are accelerating innovation, reducing reliance on proprietary systems.  

- **Path Forward**:  
  - Current models struggle to reach 90% performance, even with prompt tuning.  
  - RL offers a framework to "turn the crank" of feedback, enabling continuous improvement without relying solely on better models.  

---

## Important Quotes  
- *"Reinforcement learning is about identifying good strategies for solving problems."*  
- *"The long chain of thought... emerges as a byproduct of RL, not manual programming."*  
- *"Open-source models are back in a big way... [they] enable replication and distillation of capabilities."*  

---

## Future Directions  
- **RL as a Core Tool**:  
  - RL will be critical for training agents to handle complex, dynamic environments.  
  - Integration of verification, rejection sampling, and synthetic data will enhance RL’s effectiveness.  

- **Agent-Centric Design**:  
  - Shift from static pipelines to systems that **learn and adapt**.  
  - Focus on strategies for exploration, feedback loops, and scalability.  

- **Collaborative Innovation**:  
  - Open-source communities will drive progress, democratizing access to cutting-edge RL techniques.  

--- 

This summary captures the essence of the talk, emphasizing RL’s transformative potential for building smarter, more autonomous systems.

## Full Transcript

[00:00] [Music]
[00:16] Hello everyone. Uh, thanks Rick and the
[00:18] whole AI engineer conference team for
[00:20] putting this together and having me. I
[00:22] am Will Brown. I am a machine learning
[00:24] researcher at Morgan Stanley. And today
[00:26] I want to talk to you all a bit about
[00:27] what I think reinforcement learning or
[00:30] RL means for agents. So I was in grad
[00:33] school at Columbia for a while and I
[00:35] mostly worked on theory for multi-agent
[00:37] reinforcement learning and over the past
[00:38] couple years I have been working at
[00:40] Morgan Stanley on a wide range of LM
[00:43] related projects some of which look kind
[00:45] of like agents but I will not really be
[00:46] talking too much about that today. Uh
[00:48] I'm also relatively active on X the
[00:51] everything app and that will become
[00:52] relevant later in the talk. This talk I
[00:55] think will be probably a little
[00:56] different from most of the talks at the
[00:57] conference. Um it's not about things we
[00:59] ship to prod. It's not about things that
[01:02] definitely work and you should go do
[01:04] tomorrow that are like proven science or
[01:06] best practices. It's about where we
[01:08] might be headed. And I want to really
[01:10] just tell a story that will synthesize
[01:12] some things that have been happening in
[01:14] the broader research community um and uh
[01:16] where these trends might be pointing, do
[01:19] some speculation, and also talk about
[01:20] some uh recent open source work of my
[01:22] own. Um, and the goal of this is to help
[01:25] you plan and understand what
[01:28] reinforcement learning means, what it
[01:29] means for agents, and how to best be
[01:32] ready for a potential future, which may
[01:35] involve reinforcement learning as part
[01:37] of the agent engineering
[01:39] loop. So, um, where are we today? Most
[01:42] LLMs that we work with are essentially
[01:44] chatbots. I think it's helpful to think
[01:45] about OpenAI's, uh, five levels
[01:48] framework here. So, we did pretty well
[01:50] with chatbots. Seems like we're doing
[01:51] pretty well with reasoners. Um, these
[01:53] are great models for question answer.
[01:55] They're very helpful for interactive
[01:56] problem solving. We have the 01, 03, R1,
[02:00] Gro 3, Gemini, etc. models that are
[02:02] really good at kind of thinking longer.
[02:04] Um, and we're trying to figure out how
[02:06] we take all of this and make agents
[02:08] level three. Um, and these are systems
[02:10] that are taking actions. These are
[02:12] systems that are doing things that are
[02:13] longer and harder and more complex. And
[02:15] currently the way we tend to do this is
[02:17] chaining together multiple calls to
[02:19] these underlying chatbot or reasoner
[02:21] LLM. And we do lots of things like
[02:24] prompt engineering, tool calling, eval
[02:27] giving the models tools of their own to
[02:29] use, having humans in the loop. And the
[02:31] results are like pretty good. Um,
[02:32] there's a lot of things that we can do
[02:34] and then there's a lot of stuff that it
[02:35] feels like is around the corner that
[02:37] we're all imagining about AGI, but we're
[02:40] not really to the point yet where these
[02:42] things are going off and doing the
[02:45] things that we would imagine an AGI is
[02:47] really doing to the degree of autonomy
[02:49] that that would, I presume, entail. So,
[02:53] I think it's useful a bit to distinguish
[02:55] between agents and pipelines. I think
[02:57] Barry's talk earlier was a good way to
[02:58] kind of frame this. I'm going to use
[02:59] pipelines to encapsulate what Barry
[03:01] called workflows. Um, and I think these
[03:04] are really systems with fairly low
[03:06] degrees of autonomy. And there's a very
[03:08] non-trivial non-trivial amount of
[03:10] engineering required to determine these
[03:11] decision trees to say how does one
[03:13] action or call flow into another? How uh
[03:16] to another? How do we refine the
[03:17] prompts? Um, and it seems like a lot of
[03:20] the winning apps in the agent space have
[03:22] very tight feedback loops. And so
[03:24] whether or not you want to call these
[03:25] agents or pipelines, these are things
[03:27] where a user is interacting with some
[03:29] sort of interface. They're telling it
[03:30] what to do. The thing will do some stuff
[03:32] and come back relatively quickly. Things
[03:34] like the idees like cursor, wind, surf,
[03:36] and replet um and search tools that are
[03:38] really good at harder question answer
[03:39] maybe with some web search or research
[03:41] integrated. But there's not that many
[03:42] agents nowadays that will go off and
[03:44] like do stuff for more than 10 minutes
[03:46] at a time. I think Devon, Operator, and
[03:48] OpenAI's deep research are the three
[03:50] that really come to mind as like feeling
[03:52] a little more in the like autonomous
[03:55] agent direction. And I think a lot of us
[03:57] might be wondering how do we make more
[03:58] of these? And the kind of traditional
[04:02] wisdom is like okay, we'll just wait for
[04:03] better models. Once better models are
[04:04] around, we can just like use those,
[04:07] we'll be good. But I think it's also to
[04:09] kind of take note of like the
[04:11] traditional definition of reinforcement
[04:12] learning and what an agent means there,
[04:14] which is this idea of a thing that is
[04:16] interacting with an environment with a
[04:17] goal. And the goal of that and the
[04:19] system is designed to learn how to get
[04:22] better at that goal over time via
[04:24] repeated interaction uh with the system.
[04:26] And I think this is something that a lot
[04:27] of us are either doing manually or don't
[04:30] really have the tools to do, which is
[04:31] once we have our thing that it's set up
[04:34] to make the calls we want and the
[04:36] performance is like 70%. And we've done
[04:38] a lot of prompt tuning and we want to
[04:39] get it up to 90% but we just like don't
[04:41] have the models to do it or the models
[04:43] struggle to get the success. What's our
[04:45] path forward? Um, and so in terms of
[04:47] model trends, I think I won't spend too
[04:49] much time talking about this, but uh
[04:51] pre-training seems to be having
[04:53] diminishing returns to capital at least.
[04:54] We're still seeing kind of like loss go
[04:56] down, but uh it does kind of feel like
[04:59] we need new tricks. Um reinforcement
[05:01] learning from human feedback is great
[05:02] for making kind of friendly chat bots.
[05:04] Um but it doesn't really seem to uh be
[05:07] continually pushing us at the frontier
[05:09] of smarter and smarter and smarter
[05:11] models. uh we talk a lot about synthetic
[05:13] data and I think synthetic data is great
[05:14] for distilling uh larger models down
[05:17] into smaller models to have kind of
[05:18] really tiny models that are really
[05:19] performant but on its own it doesn't
[05:22] seem to be an unlock for like massive
[05:24] capabilities uh getting better and
[05:26] better unless we throw in verification
[05:29] in the loop or rejection sampling or any
[05:31] of these things and that really takes us
[05:33] to the world of reinforcement learning
[05:34] where this seems to be the trick that
[05:36] unlocked test time scaling for 01 models
[05:38] in R1 um it's not bottlenecked by
[05:40] needing manually curated human data and
[05:42] it does seem to actually work. Um, I
[05:45] think we all kind of took note about a
[05:47] month ago when DeepSeek released the R1
[05:51] model and paper to the world and I think
[05:53] this was really exciting because it was
[05:54] the first paper that really explained
[05:56] how you build a thing like 01. We'd had
[05:59] kind of speculation and some rumors, but
[06:01] they really laid out the algorithm and
[06:03] the mechanisms for what it takes to get
[06:06] a model to learn to do this kind of
[06:08] reasoning. And it turns out it was
[06:10] essentially just reinforcement learning
[06:12] where you give the model some questions,
[06:14] you measure if it's getting the answer
[06:15] right, and you just kind of turn this
[06:17] crank of giving it feedback to do more
[06:19] like the things that worked well and
[06:21] less like the things that didn't work.
[06:22] Um, and what you end up seeing is that
[06:24] the the long chain of thought from
[06:26] models like 01 and R1 actually emerges
[06:28] as a byproduct of this. It wasn't kind
[06:30] of manually programmed in where the
[06:32] models were like given data of like
[06:34] 10,000 token reasoning steps. this was a
[06:36] thing the model learned to do because it
[06:38] was a good strategy and reinforcement
[06:40] learning at the core is really about
[06:41] identifying good strategies for solving
[06:43] problems. Um it also seems like open
[06:45] source models are are back in a big way.
[06:47] There's a lot of excitement around the
[06:48] open source community. Um people have
[06:50] been working on replication efforts for
[06:52] the 01 project um and have also been
[06:54] trying to distill data from 01 down into
[06:56] smaller models. And so what next? How
[06:58] does this relate to agents? Um I think
[07:00] it'll be helpful to know a little bit
[07:02] about how reinforcement learning works.
[07:03] The key idea is to explore and exploit.
[07:05] So you want to try stuff, see what
[07:07] works, do more of the things that
[07:08] worked, less of the things that didn't.
[07:10] And so in this feedback loop um
[07:12] demonstrated here in the image, we can
[07:13] see a ch a challenge where a model is uh
[07:16] supposed to be writing code to pass test
[07:17] cases and we give it rewards that
[07:19] correspond to things like formatting
[07:21] using the right language and then
[07:22] ultimately whether or not the test cases
[07:24] are passing. And so this is kind of a
[07:25] numerical signal that rather than like
[07:27] training on data uh where we are kind of
[07:30] curating this in advance, we are letting
[07:32] the model do synthetic data rollouts and
[07:34] seeing scores from these rollouts which
[07:36] then are fed back into the model. And so
[07:38] the GRPO algorithm which maybe some of
[07:40] you have heard about is the algorithm
[07:41] DeepC used. I think it's less of like a
[07:43] technical breakthrough in terms of it
[07:45] being a really important new algorithm
[07:46] to study, but I think it's very
[07:48] conceptually simple and I think it's a
[07:49] nice way to think about what
[07:50] reinforcement learning means. And the
[07:52] idea really is just that you for a given
[07:53] prompt sample n completions. You score
[07:56] them all and you tell the model be more
[07:58] like the ones with higher scores. Um
[08:01] this is still in kind of the single turn
[08:03] reasoner model non-aggentic world. Uh
[08:06] and so the challenges that lie ahead um
[08:08] are going to be about how do we take
[08:10] these ideas uh and extend them into uh
[08:13] more powerful, more agent, more
[08:14] autonomous systems. But we do know that
[08:17] it can be done. So, OpenAI's deep
[08:19] research still has a lot of questions
[08:20] that we do not know the answers to about
[08:22] how it works, but they have told us that
[08:24] it was endto-end reinforcement learning.
[08:25] And so, this is a case where the model
[08:27] is taking up to potentially a hundred
[08:28] different tool calls of browsing or
[08:31] querying different parts of the internet
[08:32] to synthesize a large angler. And it
[08:34] does seem, I think, to many people's
[08:36] vibe check opinions very impressive. Um,
[08:39] but it also is like not AGI in the sense
[08:41] of you can't get it to go like uh work
[08:44] in a repo or like solve hard software
[08:46] engineering tasks. And people have kind
[08:47] of anecdotally found that it does
[08:49] struggle a bit for like out of
[08:50] distribution tasks or like if you wanted
[08:52] to fill out a table with like a 100 very
[08:54] manual calculations, it can struggle
[08:56] there. And so it seems like
[08:58] reinforcement learning on one hand is a
[09:00] big unlock for new skills and more
[09:02] autonomy, but it's not a thing that so
[09:05] far has granted us agents that can just
[09:08] do everything and know how to solve all
[09:10] kinds of problems. But it is a path
[09:12] forward for teaching a model skills and
[09:14] having the model learn how to get better
[09:16] at certain skills, particularly in
[09:18] conjunction with environments and tools
[09:21] and verification.
[09:23] Um, and so there is infrastructure out
[09:25] there for doing this on our own kind of.
[09:28] Um, a lot of it is still RLHF style by
[09:31] which I mean it's about kind of single
[09:33] turn interactions where the goal is we
[09:35] have reward signals that come from kind
[09:37] of human data that has been combined
[09:39] into a reward model. Um, and if we want
[09:42] to have RL agents becoming part of our
[09:44] systems, maybe we will get really good
[09:46] API services from the large labs that
[09:48] let us build these things and hook into
[09:50] GPT whatever um or cloud whatever and
[09:53] train these sorts of models on our own
[09:55] with fine-tuning, but we also don't
[09:56] really have these options yet. Um,
[09:58] OpenAI has kind of teased their
[09:59] reinforcement fine-tuning feedback, but
[10:01] it's not uh multi-step tool tool calling
[10:03] yet. And so I think if we want to plan
[10:05] ahead, it's worth kind of noting and
[10:07] asking what would this ecosystem look
[10:10] like? And there's a lot of unknown
[10:12] questions like how much this will cost,
[10:13] how small can the models be, will it
[10:15] generalize across tasks, uh and how do
[10:17] we design good rewards and good
[10:19] environments? And there's a lot of
[10:20] opportunity here. Um open source uh
[10:23] infrastructure, there's a lot of room to
[10:25] build and grow and determine what the
[10:26] best practices are going to be, what the
[10:27] right tools will be, as well as
[10:29] companies that can build tools for to
[10:31] support this ecosystem. uh whether or
[10:33] not they're already in the fine-tuning
[10:34] world or not. Um and services for
[10:37] supporting this kind of agentic RL and I
[10:39] think also it is worth thinking about
[10:41] things that are like not literal RL in
[10:42] the sense of training the model but at
[10:44] the prompt level there's all sorts of
[10:45] automation we can do. So if you've used
[10:47] DSPI I think that is kind of adjacent to
[10:49] RL in the flavor of having a signal that
[10:52] we can then uh bootstrap from to improve
[10:55] our uh underlying system based on
[10:58] improving some downstream scores. Um,
[11:01] now I want to share a story with you
[11:02] about a single Python file I wrote a
[11:04] couple weeks ago. Um, so this was the
[11:06] weekend after R1 came out and I'd been
[11:09] reading the paper and thought it was
[11:10] really cool. We had not had the Nvidia
[11:12] stock crash quite yet. Um, and uh, I was
[11:16] just playing around with some
[11:16] experiments. I was taking the a hug a
[11:18] trainer from HuggingFace that had the
[11:20] GRPO algorithm and I was getting a
[11:23] really small language model llama 1B to
[11:26] do some reasoning and then give an
[11:28] answer for math questions. And I started
[11:29] with like a pretty simple system prompt
[11:32] and I was just training the model to let
[11:34] it see what it did. And I had kind of
[11:35] manually cured some rewards in terms of
[11:38] what the scoring function should look
[11:39] like. And I just kind of like tweeted it
[11:41] out um where I had an example of the
[11:43] model kind of looking like it's doing
[11:45] some selfcorrection and so showing that
[11:48] the accuracy gets better as well as the
[11:51] uh length of response will initially
[11:52] drop once it learns to kind of follow
[11:54] the format. Then it goes back up as it
[11:57] learns to kind of take advantage of
[11:58] longer chains of thought to do its
[12:00] reasoning. And this was not the first
[12:02] thing to replicate in any sense. I
[12:04] wouldn't really call it a true
[12:05] replication. Um it was far from the most
[12:07] complicated and I think that actually
[12:10] caught a lot of people's imaginations
[12:12] and it became kind of a thing. Um, so
[12:15] over the next two weeks after that, it
[12:18] just took on a life of its own where a
[12:20] lot of people were kind of tweeting
[12:21] about it and forking it and making
[12:23] modifications to it and making it
[12:25] something you could run in a Jupyter
[12:26] notebook, making it more accessible,
[12:28] writing blog posts about it. And it was
[12:31] interesting um because it to me didn't
[12:34] feel like a thing that kind of merited
[12:37] this level of excitement. But what I
[12:40] think was catching people's imagination
[12:42] was that it was one file of code. It was
[12:44] really simple and it invited uh
[12:47] modification in a very userfriendly
[12:49] engaging way which I like to call rubric
[12:52] engineering. And so the idea of rubric
[12:54] engineering here is that similar to
[12:57] prompt engineering um to have a model do
[13:01] reinforcement learning it's going to get
[13:02] some reward but what should this reward
[13:04] be? In the most simple version it's just
[13:05] like did it get the question right or
[13:06] wrong like does a equal b. But there's a
[13:09] lot more you can do beyond this. And so
[13:10] I think the the single file of code
[13:12] exposed uh examples of this where you
[13:15] can give the model points for things
[13:16] like following this XML structure. Like
[13:19] if it gets a certain tag right you give
[13:20] it plus one point. Um, if it has an
[13:23] integer answer that's still the wrong
[13:24] answer, but it's learned that the format
[13:25] should be an integer answer. Get some
[13:27] points for that. Um, and there's a lot
[13:30] of room here for getting creative and
[13:32] for designing rules that are not just
[13:34] downstream eval to for our own sake know
[13:37] whether a thing is working, but to allow
[13:38] the model itself to know whether it's
[13:40] working and use that as feedback for
[13:43] going further and training more. Um, and
[13:45] this is very early stages. There's a lot
[13:47] of things we don't know and I think
[13:48] there's a lot of opportunity to get
[13:50] creative and explore and try things out
[13:52] such as using LMS to design these
[13:53] rubrics. Uh autotuning these rubrics or
[13:56] autotuning your prompts with frameworks
[13:57] like DSPI. Um incorporating LM judges as
[14:01] part of the scoring system. And then
[14:02] also I think reward hacking is an issue
[14:04] to be very cautious of where the idea is
[14:07] you want to ensure that the the reward
[14:09] model you're using is actually capturing
[14:11] the goal and it doesn't have kind of
[14:12] these back doors where a model can kind
[14:14] of cheat and do something else that
[14:17] ultimately results in it kind of getting
[14:19] a super high reward without learning to
[14:22] do the actual task. Um, and following
[14:25] this, I have been trying to learn from
[14:27] those lessons of what I saw people using
[14:29] out in the wild and make something that
[14:31] is a little more uh robust and uh usable
[14:34] for actual projects beyond just one file
[14:36] of code. Um, and this has been a kind of
[14:38] very recent effort. It's not a thing
[14:39] that I'm telling you to go use for all
[14:41] your problems tomorrow, but I think it's
[14:43] my attempt doing some open- source uh
[14:46] research code um that will help people
[14:48] potentially try these things out easier
[14:50] and answer some questions uh about this.
[14:52] And so what this really is, it's a a
[14:55] framework for doing RL inside of
[14:57] multi-step environments. So the idea
[14:59] here is that lots of us have built these
[15:01] great agent frameworks for using API
[15:03] models. And the hope would be that we
[15:06] can leverage those existing environments
[15:08] and uh frameworks to uh h actually do
[15:11] RL. So here the idea is you can just
[15:13] create this environment thing that the
[15:14] model plugs into and you don't have to
[15:16] worry about the weights or the tokens.
[15:18] you can just write an interaction
[15:20] protocol and then this gets fed into a
[15:22] trainer and so once you build this
[15:23] environment you can just kind of let it
[15:24] run and uh have a model that once you
[15:28] give it some rewards learns to get
[15:29] better and better over time. Um and to
[15:32] conclude I want to talk about what I
[15:34] think AI engineering might look like in
[15:36] the RL era. So this is all still
[15:40] something that is very new. Uh, we don't
[15:42] know whether the off-the-shelf API
[15:45] models are going to just work for the
[15:46] tasks we throw at them. It might be the
[15:48] case that they do. It might be the case
[15:50] that they don't. Um, one reason I think
[15:53] that they might not be the entire
[15:55] solution is that it is really hard to
[15:58] include a skill in a prompt. You can
[16:00] include knowledge in a prompt. Um, but a
[16:03] lot of us when we try something, we
[16:05] don't nail it the first time and it
[16:06] takes a little bit of trial and error.
[16:08] Um, and it seems to be the case that
[16:12] models are like this as well, where a
[16:14] model does get better at a thing and
[16:15] really gets a skill nailed down by trial
[16:19] and error. And this has been the most
[16:21] promising unlock we've seen so far for
[16:24] these higher autonomy agents like deep
[16:26] research. Um, fine-tuning might still be
[16:29] important. And I think a lot of people
[16:30] wrote off fine-tuning for a while
[16:32] because open models were far enough
[16:34] behind the frontier that like a prompted
[16:36] o uh frontier model API was just going
[16:38] to beat a smaller fine-tuned model. I
[16:40] think one we're now seeing the open and
[16:42] closed source gap be close enough that
[16:44] this is less of a concern. A lot of
[16:46] people are using open source hosted
[16:48] models in their platforms. Um, and also,
[16:51] uh, RL, the most kind of true version of
[16:55] RL that DeepS did for their R1 model
[16:57] that OpenAI has talked about doing for,
[16:59] uh, deep research requires doing some
[17:01] reinforcement learning. Um, there's a
[17:03] lot of challenges here. There's a lot of
[17:05] research questions we don't know the
[17:06] answers to. Um, but there's a lot of
[17:08] things that I think these skills we've
[17:09] learned from doing AI engineering over
[17:11] the past couple years translate very
[17:13] directly to, which is that the challenge
[17:15] of building environments and rubrics is
[17:17] not that different from the challenge of
[17:18] building evals and prompts. We still
[17:21] need good monitoring tools. We still
[17:22] need a large ecosystem of companies and
[17:24] platforms and products that support the
[17:26] kinds of agents we want to build. Um, so
[17:30] I think all the stuff we've been doing
[17:32] is going to be essential and it's worth
[17:35] looking ahead a little bit to see if we
[17:37] end up in a world where we have to do a
[17:39] little bit more reinforcement learning
[17:40] to unlock things like true autonomous
[17:43] agents or innovators or organizations
[17:46] that are powered by language models. Um,
[17:48] what does that look like? Uh, we will
[17:51] find out.
[17:53] [Music]
[17:55] [Applause]
[17:58] [Music]
