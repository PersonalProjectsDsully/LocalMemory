---
type: youtube
title: Agentic Workflows on Vertex AI: Rukma Sen
author: AI Engineer
video_id: n0qemluQDtQ
video_url: https://www.youtube.com/watch?v=n0qemluQDtQ
thumbnail_url: https://img.youtube.com/vi/n0qemluQDtQ/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: []
entities: ['Google Cloud Booth', 'Spider-Man', 'Calculator', 'Large Language Models', 'AI Agent', 'Tools', 'Orchestration', 'Deterministic Agents', 'Generative Agents', 'Hybrid Agents']
concepts: ['AI Agent', 'Orchestration', 'Tools', 'Deterministic Agents', 'Generative Agents', 'Hybrid Agents', 'Goal-Oriented Systems', 'Interaction with Environment', 'Memory and State', 'Action Inclusion']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI concepts', 'Familiarity with machine learning', 'Knowledge of APIs or tools']
related_topics: ['AI Agents', 'Machine Learning', 'Natural Language Processing', 'System Design', 'Automation', 'Software Architecture', 'AI Ethics', 'Tool Integration']
authority_signals: ['I would be happy to discuss this with you', "This is the model that's responsible for reasoning", "I'm actually really curious about this but this talk is not actually going to focus on..."]
confidence_score: 0.8
---

# Agentic Workflows on Vertex AI: Rukma Sen

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=n0qemluQDtQ)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: vertex ai, agentic workflows, ai agents, generative ai, machine learning, ethical ai, ai interaction  

## Summary

# Summary of Rukma Sen's Talk on Agentic Workflows in AI

## Overview
Rukma Sen from Google Cloud discusses the role of AI agents in bridging large language models (LLMs) and end-users, emphasizing their potential to autonomously achieve goals through interaction with environments. The talk highlights ethical design, key components (models, tools, orchestration), and the importance of balancing innovation with safety, privacy, and responsibility.

---

## Key Points
- **AI Agents as the Interface**:  
  - Agents act as the bridge between users and AI systems, enabling autonomous task execution through reasoning, action, and memory management.  
  - They differ from traditional AI systems by combining *reasoning* (model), *action* (tools), and *coordination* (orchestration).  

- **Core Components of AI Agents**:  
  1. **Model**: The "brain" responsible for reasoning, planning, and decision-making.  
  2. **Tools**: The "hands" that enable interaction (e.g., APIs, data fetching, payment processing).  
  3. **Orchestration**: The "nervous system" managing memory, state, and goal tracking.  

- **Types of Agents**:  
  - **Deterministic Agents**: Follow fixed rules (e.g., calculators).  
  - **Generative Agents**: Use LLMs for dynamic, context-aware decisions.  
  - **Hybrid Agents**: Combine deterministic and generative approaches.  

- **Ethical and Safety Considerations**:  
  - Emphasizes the "Spider-Man principle" (power and responsibility) to ensure agents are transparent, safe, and aligned with user values.  
  - Highlights risks of uncontrolled autonomy and the need for rigorous testing.  

- **Evolution of Human-AI Interaction**:  
  - Shifts from static machine interfaces to dynamic, AI-driven systems that adapt to user needs.  

---

## Important Quotes/Insights
- *"An AI agent is a system designed to achieve specific goals by interacting with its environment."*  
- *"Tools are the hands of the agent; orchestration is the nervous system."*  
- *"The real question is not just what agents can do, but what they should do."*  
- *"A calculator is a deterministic agent—2+2 will always be 4, unless we're in a mirror dimension."*  

---

## Actionable Takeaways
1. **Prioritize Ethical Design**: Embed safety, transparency, and accountability into agent development.  
2. **Leverage Orchestration**: Use memory and state management to enhance autonomy and task continuity.  
3. **Balance Agent Types**: Choose deterministic, generative, or hybrid models based on use cases.  
4. **Engage with the Community**: Explore deeper discussions on agent ontologies at the Google Cloud Booth.  

--- 

This summary captures the essence of Rukma Sen's talk, focusing on the transformative potential of AI agents while underscoring the critical need for responsible innovation.

## Full Transcript

[00:03] [Music]
[00:13] I'm rukma I work at Google Cloud on our
[00:16] vertex AI product um and at towards the
[00:19] end of the talk for those of you who
[00:21] don't know what that is I will discuss
[00:23] it a just a little bit more but where I
[00:27] want to start today is with agents so
[00:31] this slide you're like understatement
[00:33] much right you're like yeah you're right
[00:36] that's why we're here at this conference
[00:38] because generative AI is transforming
[00:40] how we interact with technology and if
[00:43] any of you are wondering hey is this is
[00:45] the rest of this person's talk filled
[00:46] with such groundbreaking insights maybe
[00:49] maybe not stick around and find out i k
[00:52] i kid um the interesting thing about
[00:56] this statement that I want to think
[00:57] about is what is the interface of that
[01:01] interaction where do all of these all of
[01:04] us whether we're de developers employees
[01:08] parents students interface with AI um I
[01:12] would posit that for the vast majority
[01:15] of many of our use cases that we
[01:18] actually want to accomplish that
[01:19] interface of interaction with generative
[01:22] AI is going to be an agent of some kind
[01:25] so the power of generative AI as I'm
[01:27] sure I don't need to belor this point to
[01:30] you guys is immense but it can be kind
[01:33] of intimidating and is inaccessible to
[01:36] many people perhaps many people who are
[01:39] not in the room right now with us but we
[01:42] can think about these personas people we
[01:44] want to help people we want to build for
[01:46] right um and that's kind of where I
[01:49] think Agents come in and where they're
[01:51] really powerful they're the bridge
[01:53] between the models and everyday users so
[01:57] they help you go from speaking model
[01:59] Lang language to speaking natural
[02:01] language funny joke no no no I'm very
[02:07] sad you guys give me a
[02:10] laugh no all right all right all right
[02:13] all right I'll try I'll try I'll
[02:16] try we'll we'll we'll make it there
[02:19] we'll make it there um what I think is
[02:22] actually really cool though is that for
[02:25] actually all of us in this room we speak
[02:28] both languages so we're going to be the
[02:30] ones developing these agents right so
[02:33] we're going to be designing how they
[02:35] interact with people what kinds of
[02:37] limits and Frameworks we're putting
[02:39] around them to make sure that you know
[02:41] we're being ethical we're being helpful
[02:43] we're being Humane we're being safe and
[02:46] that I think is kind of magical think
[02:49] back to the days before the internet
[02:52] existed right what was the human
[02:54] interaction interface with technology it
[02:57] was machines it was things like
[03:00] appliances in the home and then the
[03:02] internet came about and the whole way
[03:05] human beings and Technology interact
[03:07] completely changed we're all looking at
[03:10] our screens we use gestures like swiping
[03:13] and zooming and
[03:15] scrolling think about how cool it could
[03:18] be if you were the one building the next
[03:21] interface the next kind of boundary of
[03:23] interaction between human beings and
[03:26] Technology um I'm wearing a little NE
[03:30] that says wizard in training because I
[03:32] think this is actually kind of magical
[03:34] that one got a better reaction okay we
[03:37] like Wizards in this
[03:41] room given that though to quote my
[03:44] favorite spider person with great power
[03:47] comes great responsibility we all know
[03:49] who to attribute this to Uncle Ben in
[03:52] every version of every Spiderman ever I
[03:55] promised Spider-Man to someone in this
[03:57] room I did say there was Spider-Man
[03:58] coming up in my to and I'm hoping I
[04:00] delivered on that promise he's here he's
[04:02] here um but the point Spider-Man is
[04:05] making I think is actually serious and
[04:08] something we should we should be
[04:09] thinking about so with the power to
[04:12] really shape how people are interacting
[04:14] with AI does come responsibility we must
[04:18] ensure that these interactions are like
[04:20] I said safe Humane and helpful when you
[04:24] think about like what is this
[04:25] responsibility I would say there are
[04:28] several kind of sources but some I would
[04:31] just highlight for everybody to think
[04:32] about are first ethical considerations
[04:35] what are our moral obligations to
[04:37] protect users who are using these
[04:38] technologies that have really great
[04:41] unlimited powers in some ways how can we
[04:44] build guard rails that protects people
[04:46] that keeps them safe um prevents kind of
[04:49] the spread of
[04:50] misinformation um and make it really
[04:52] clear when let's say an agent is
[04:55] producing something that's generated
[04:57] versus when it's producing something
[04:59] that
[05:00] is should be taken as a true fact we
[05:03] should also think a good bit I think
[05:05] about safety cyber security data privacy
[05:09] where are we storing the data that we
[05:12] reason over with these models how are we
[05:15] thinking about making sure that we're
[05:17] safeguarding people's privacy um with
[05:20] the rise of a lot of things like
[05:22] wearables um and kind of just a lot of
[05:25] what I like to think about as like
[05:27] unobtrusive compute where it's just out
[05:30] there in the world these become I think
[05:32] even more important um you know things
[05:35] to think about
[05:37] so great I talked a lot about agents and
[05:41] how we should think about making them
[05:43] but let's talk really quickly about what
[05:47] an agent is now real talk the reason
[05:50] this talk was supposed to be open models
[05:53] is because we did have a last minute
[05:54] schedule shift and fully true story
[05:58] before I knew I was going to deliver
[05:59] deliver this talk and I was you know one
[06:01] week ago registering for this and they
[06:03] asked hey what is it you really want to
[06:06] learn I said what's an agent
[06:09] really so so I'm actually really curious
[06:12] about this but this talk is not actually
[06:14] going to focus on kind of the
[06:15] philosophies and ontologies of Agents if
[06:18] you want to chat with me about it please
[06:19] drop by the Google Cloud Booth I would
[06:21] be happy to discuss this with you can we
[06:24] appreciate that I got a Spider-Man
[06:25] reference and ontology in the same talk
[06:28] I'm very proud of myself
[06:32] okay so given that we're just going to
[06:34] move forward with a working definition
[06:37] and what is a working definition this
[06:39] this is probably the kind of broadest
[06:41] most overarching definition you can
[06:43] think about um for our purposes and AI
[06:45] agent simply is a system that's designed
[06:48] to achieve specific goals by interacting
[06:51] with its environment so let's break that
[06:54] kind of down into what its key
[06:55] components are so at the heart of every
[06:58] AI agent is a powerful model often this
[07:01] is based on large language models right
[07:03] this is the model that's responsible for
[07:05] reasoning over what are the goals of
[07:07] this agent kind of determining what the
[07:10] next best plan of action is and then
[07:12] guiding Its Behavior think about it as
[07:15] your agent's brain or Executive Center
[07:17] if you will then let's think tools so an
[07:21] AI agent doesn't just think it also acts
[07:24] and I think this is actually a key piece
[07:26] of the definition where you can separate
[07:28] it from something where um the primary
[07:31] function is just thinking or reasoning
[07:34] or generating with an AI agent you do
[07:37] want to have an action included so this
[07:39] is where tools come in tools are if that
[07:42] if the model was the brain tools are
[07:44] your AI agent's hands this is where you
[07:47] get to interact you can do things like
[07:49] fetch data from the internet more
[07:52] complex action calling external apis to
[07:54] do things like say book flights process
[07:56] payments Etc and then orchestration is
[07:59] the glue that kind of holds everything
[08:02] together it maintains memory and state
[08:04] which is really important it keep sort
[08:06] of track of the goals and if in this
[08:09] analogy of brain and hands orchestration
[08:11] is really the nervous system tying it
[08:13] all kind of together so these three
[08:16] components work together kind of
[08:18] allowing the AI agent to function
[08:20] autonomously and accomplish tasks that
[08:23] being said I really quickly want to say
[08:25] that there are different types of AI
[08:27] agents and some of these you could say
[08:29] have existed for a very long time way
[08:32] before generative AI really you know
[08:34] boomed in the marketplace so there are
[08:37] deterministic agents generative agents
[08:40] and obviously kind of hybrid agents
[08:42] deterministic agents are basically
[08:45] following a fixed set of rules or
[08:47] algorithms to make decisions so given a
[08:50] specific input that type of agent is
[08:53] always consistently going to return the
[08:55] same output as I'm sure you can tell
[08:58] this is quite different different from
[09:00] when you're say prompting with a
[09:02] generative
[09:03] agent an example a very simple example
[09:06] of this could be a calculator when you
[09:08] give it the input of 2 plus 2 it will
[09:11] always return four unless something's
[09:13] deeply wrong and you're in a mirror
[09:15] Dimension let's hope not generative
[09:18] agents on the other hand are more
[09:21] creative they kind of will work best in
[09:26] use cases where you want to be cre
[09:29] creative you want to combine rules in
[09:31] ways that they haven't been combined
[09:33] together before and they are capable of
[09:36] a much wider range of diverse outputs
[09:39] kind of based on the input they receive
[09:41] so an examp a simple example of a
[09:43] generative agent is a chatbot designed
[09:45] to answer kind of customer questions a
[09:47] customer service chat bot when asked
[09:49] about kind of a product it will generate
[09:52] generate an hopefully helpful and
[09:54] informative answers based on whatever
[09:57] data source it has about your company's
[09:59] product Etc and hybrid agents combine
[10:01] sort of the strengths of the two an
[10:03] example of this could be like a
[10:04] financial advisor that uses
[10:07] deterministic agents to analyze the
[10:09] market and predict the right places to
[10:11] invest but then use as a generative
[10:13] agent to actually uh communicate this or
[10:16] go out and talk about this strategy to
[10:19] customers okay so this is I think where
[10:23] things get really interesting so given
[10:26] the different types of Agents you can
[10:28] actually architect them quite
[10:31] differently across the Spectrum so from
[10:34] single agent to multi-agent architecture
[10:37] I think increases the kind of
[10:38] sophistication and complexity that your
[10:41] agent is capable of very very quickly so
[10:45] just to like kind of very quickly go
[10:47] over the single agent one this is not I
[10:50] think hopefully new to most people this
[10:52] is where a single model is just
[10:54] responsible for everything reasoning
[10:56] planning acting super straightforward
[10:58] architecture to implement you just
[11:00] provide it with instructions and a set
[11:01] of tools to kind of achieve a goal
[11:04] right so what is the problem here great
[11:08] like you know
[11:09] great tell her what to do it's going to
[11:11] do it it's going to return the output
[11:13] well have you ever tried a prompt like
[11:16] count how many instances of the letter A
[11:18] are in the word banana and the model
[11:20] will say four and then you say hey can
[11:23] you check that and then it will say two
[11:26] and then you say hey can you check that
[11:27] and then it'll say one
[11:29] so in cases where you're trying to
[11:32] deploy a production ready app something
[11:34] like this can you know really be a
[11:37] problem so now we get to a much more
[11:41] powerful way to design agents which is
[11:43] multi-agent architecture so just like
[11:46] complex human systems like let's say a
[11:48] company you work at have people
[11:50] specialized in different roles working
[11:52] together to achieve a common goal that's
[11:54] what multi-agent architecture does as an
[11:57] example of this is a customer service
[11:58] system
[12:00] so let's say there's three levels of
[12:01] agent level one you have a dispatcher
[12:04] agent the job of this agent is simply to
[12:06] triage everything that comes in assess
[12:09] the customer's issue and determine where
[12:11] toout it so it triages second level
[12:14] agent subject matter experts these
[12:16] agents are trained in specific subject
[12:19] matter maybe specific product lines or
[12:21] specific regions if that's how your
[12:23] company functions um and when they are
[12:25] assigned a case by that first agent they
[12:28] have the expertise to respond and then
[12:31] finally as a level three check you also
[12:32] have a supervisor agent that quality
[12:34] checks the work against a predefined
[12:37] data set it that agent has the ability
[12:40] to go in and solve some issues for
[12:42] example um fun story I created a
[12:46] multi-agent kind of architecture once
[12:48] and the supervisor agent was supposed to
[12:51] return the the sentence this is not good
[12:54] enough please try again if it wasn't
[12:56] happy with the output and it just kept
[12:58] doing
[12:59] and it did not like anything my first
[13:01] agent did until I went back and like
[13:03] recreated the whole whole thing okay
[13:07] so as agents are becoming more and more
[13:10] common across Industries we're largely
[13:12] kind of seeing development in four types
[13:14] and I just wanted to give like show you
[13:16] really quickly like what a set of use
[13:19] cases for agents could look like so with
[13:22] customer I already talked for example
[13:24] through what it would look like for a
[13:26] customer support agent um but also
[13:28] things like like Ecommerce being able to
[13:31] support B2B supporting travel if you are
[13:34] a travel vendor for example there's also
[13:37] internal facing employee agents HR
[13:40] things like enrollment benefits
[13:41] questions those things sales of course
[13:45] as I'm sure you can see would be a great
[13:47] opportunity payable supply chain so
[13:50] those are kind of thinking about who the
[13:52] agent is targeted to and then knowledge
[13:54] agents um are specialized agents in
[13:57] terms of what exactly
[13:59] is their subject matter of expertise so
[14:02] you could have an agent that's
[14:03] specifically very good at answering
[14:05] legal questions for
[14:07] example um and then finally we are also
[14:10] seeing um through the use of multimodal
[14:12] use cases a huge uptick in voice agents
[14:16] especially in scenarios like say a fast
[14:19] food drive-thru so I'm sure you can
[14:22] imagine what like where a voice agent
[14:24] would come in here you go in you make
[14:26] that order using your voice and the
[14:29] agent basically transcribes that and
[14:31] sends it through to the ordering system
[14:33] so that the person at the delivery
[14:34] window can go ahead and serve
[14:37] you okay so we're more than halfway
[14:40] through this talk so quick moment so we
[14:43] looked at why we should care about agent
[14:44] design then we kind of peaked under the
[14:46] hood really quickly to talk about what
[14:49] what the kind of components of agents
[14:51] are then we thought through a
[14:53] architecture a little bit and kind of
[14:54] looked at what the top use cases are so
[14:58] just before before wrapping up the last
[15:00] thing I'm going to do so you can see my
[15:01] shirt I'm going to talk about tooling
[15:05] and specifically Google Cloud's
[15:07] developer platform vertex AI so Google
[15:10] Cloud's developer platform vertex AI
[15:13] offers essentially a full life cycle AI
[15:17] development platform so whatever it is
[15:19] you want to do whether it's things I
[15:21] didn't talk about today like uh calling
[15:23] models and fine-tuning them or it is
[15:25] stuff like I talked about today such as
[15:27] building agents we offer you a spectrum
[15:30] of ways to enable that whether that's
[15:32] super low code even no code in some
[15:35] cases all the way up to very high
[15:37] customization High code methods to do it
[15:40] vertex offers you access to 150 plus
[15:43] models obviously all of our first-party
[15:44] Google Cloud models but we also have um
[15:47] all of anthropics models on there llama
[15:49] 2 and llama 3 as well as a whole bunch
[15:51] of Open Source models um we try to make
[15:54] it easy to prototype so you can get apis
[15:57] for all of this and Start experiment
[15:58] expending start building um without
[16:01] having to you know go through a whole
[16:02] bunch of setup we also want to make it
[16:05] very simple to kind of be able to deploy
[16:08] and have peace of mind that your
[16:10] security and all those Enterprise
[16:12] concerns I was talking about earlier
[16:13] when it comes to things like data
[16:15] privacy Etc are taken care of so we back
[16:18] all of this with Google Cloud level
[16:20] Enterprise Readiness security uh you
[16:24] know things like compute orchestration
[16:26] so you're not ending up paying too much
[16:28] for something if you don't have to and
[16:30] all of
[16:31] that um I wanted to quickly flash model
[16:34] Garden for you since this is the piece
[16:36] of vertex a I did not cover in today's
[16:38] talk but model Garden is where you can
[16:40] go in pick your model get you know fine
[16:44] tune it we have a couple of model eval
[16:46] workflows that you can run to try to
[16:48] match the model to your specific use
[16:51] case as well and then finally agent
[16:53] Builder as I said all the way from no
[16:56] code to kind of full code ways to to
[16:59] build those cool exciting agents that I
[17:01] was just telling you about um the last
[17:05] thought I want to leave you with is this
[17:08] we're building for Builders vertex AI is
[17:11] designed with developers first in mind
[17:13] and all the choices we make as we build
[17:15] this from training and quick start
[17:18] resources all the way through to
[17:20] deployment is for you so we love
[17:23] feedback please stop by our booth tell
[17:26] us if you've used the product what you
[17:28] love what you hate we would love to
[17:30] learn from all of you with that I will
[17:34] ask you to please do me a giant favor
[17:38] and take a quick survey to tell us how
[17:40] we did and mayv my colleague in the
[17:44] green skirt there will give you a cute
[17:46] vertex AI branded water bottle if you
[17:48] show her you completed the survey that's
[17:51] it thank you guys
[17:56] [Music]
