---
type: youtube
title: Building Multi agent Systems with Finite State Machines
author: Channel Video
video_id: OD13PiXw60o
video_url: https://www.youtube.com/watch?v=OD13PiXw60o
thumbnail_url: https://img.youtube.com/vi/OD13PiXw60o/mqdefault.jpg
date_added: 2025-05-26
category: General
tags: ['tutorial', 'general']
entities: ['Building Multi agent Systems with Finite State Machines']
concepts: []
content_structure: tutorial
difficulty_level: intermediate
prerequisites: []
related_topics: []
authority_signals: []
confidence_score: 0.3
---

# Building Multi agent Systems with Finite State Machines

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=OD13PiXw60o)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: finite state machines, ai agents, state charts, multi agent systems, ai governance, actor model, system design  

## Summary

# Comprehensive Summary of "Building Multi-agent Systems with Finite State Machines"

## Overview  
This video explores how finite state machines (FSMs) provide a structured, reliable foundation for building autonomous AI agents and systems. Adam Charlson discusses their role in enhancing predictability, observability, and control, particularly in the context of 2025’s AI trends. He emphasizes combining FSMs with large language models (LLMs) and actor models to address the limitations of both, creating robust agentic systems.

---

## Key Points  
1. **FSMs as Building Blocks**:  
   - FSMs enforce predictable behaviors, traceability, and scalability, contrasting with LLMs’ unpredictability and opacity.  
   - Components: **states**, **transitions**, **actions**, and **guards**.  

2. **State Charts**:  
   - An extension of FSMs for handling complex, hierarchical state logic.  

3. **Actor Model Integration**:  
   - Actors enable autonomy and communication, while FSMs structure their behavior.  

4. **Advantages of FSMs**:  
   - Predictable, low-latency, and scalable.  
   - Mitigate LLM weaknesses (e.g., unreliability, lack of control).  

5. **Challenges**:  
   - **State explosion**, **concurrency management**, **versioning**, and **learning curve**.  
   - Unmodeled inputs are logged but not acted upon.  

6. **Agentic Systems Pattern**:  
   - Combines **LLMs** (dynamic intelligence) with **FSMs** (structured control).  
   - **Tool use**: LLMs interact with tools via prompts, not direct calls.  
   - **Human-in-the-loop**: FSMs enforce approval steps for safety.  
   - **Feedback mechanisms**: Improve relevance via retrieval-augmented generation.  

7. **Saga Patterns**:  
   - For managing distributed transactions and ensuring consistency.  

---

## Notable Quotes  
- *"The opportunity is that by combining LLMs and state machines together, we can build a system that leverages the strengths of one to mitigate the weaknesses of the other."*  
- *"FSMs are everything that LLMs are not: predictable, traceable, and recoverable."*  
- *"The learning curve [of FSMs] is a joy, but you may be feeling something else right now."*  

---

## Actionable Takeaways  
- **Adopt FSMs** for structured, predictable agent behavior.  
- **Combine FSMs with actors** to enable autonomy and communication.  
- **Integrate LLMs** for dynamic decision-making while using FSMs for control.  
- **Implement human-in-the-loop** steps via FSMs to manage tool use and approvals.  
- **Use state charts** for complex, hierarchical state logic.  
- **Address concurrency** with tools like Azure Service Bus or AWS SQS message groups.  

--- 

This summary highlights the strategic use of FSMs in modern AI systems, balancing flexibility with control.

## Full Transcript

[00:04] hi I'm Adam charlson and in this video
[00:07] I'll walk you through how finite State
[00:10] machines provide a structured reliable
[00:12] foundation for building applications
[00:14] including AI agents as AI becomes more
[00:18] autonomous the challenge isn't just
[00:21] intelligence or model performance it's
[00:24] also how to build systems with
[00:26] predictability observability and control
[00:29] espe important qualities when
[00:32] orchestrating large language
[00:34] models so the year is 2025 and the top
[00:38] AI Trends as listed by Gartner and
[00:41] probably everyone else too is a gentic
[00:43] AI we're autonomous AI plans and acts to
[00:47] achieve all our hopes and dreams but the
[00:50] number two Trend called out by Gardner
[00:52] is just as if not more important and
[00:55] that is the development of AI governance
[00:58] platforms
[01:00] we humans need to find a way to manage
[01:02] the ethical legal and operational
[01:05] performance of agentic systems now State
[01:09] machines probably don't have much to
[01:11] offer to the ethical or perhaps legal
[01:14] challenges of AI governance but I
[01:17] believe they may have a foundational
[01:19] role to play in building platforms that
[01:22] effectively govern agent decision Mak
[01:24] and
[01:26] behavior so let's Dive Right In what is
[01:29] a finite State machine well it's a
[01:32] computational model of a system with
[01:34] States and transitions that are
[01:36] triggered by events the example shown
[01:39] here is for the game of rock paper
[01:41] scissors our game is defined by five key
[01:45] components the first are the state
[01:48] definitions this is a declarative uh set
[01:51] of system modes and
[01:54] configurations in our game it's the
[01:56] initial state of locking eyes the
[01:59] parallel states where players are
[02:01] selecting their throws all the way to
[02:03] the final State when the game is over
[02:06] there is transition Logic for how we
[02:08] move between these states when events
[02:10] occur like when we start the round uh
[02:14] but these can also be targetless
[02:16] transitions as is the case with rock
[02:18] paper and scissors on shoot we apply a
[02:22] guard which enforces valid transitions
[02:26] so on the case of shot we check if the
[02:28] throws match and if they do then we go
[02:31] back to select another throw otherwise
[02:33] we can continue on in the
[02:35] flow in each transition we can apply
[02:39] actions and effects side effects that
[02:41] are triggered by transitions like
[02:43] sending a message or updating context
[02:46] and context is store data that is used
[02:50] for transition logic and also uh final
[02:54] output now the lovely nerds out there
[02:57] are likely yelling at their screens at
[02:59] this point saying that's not a state
[03:01] machine it's a state chart you're right
[03:05] a state chart is an extension of the
[03:07] state machine that adds a richer
[03:10] vocabulary to the model including things
[03:13] like hierarchical and parallel states
[03:15] which I used in my game in this
[03:17] presentation however I may use these
[03:19] terms interchangeably it'll be
[03:23] okay a state chart models an
[03:26] applications Behavior but on its own it
[03:29] lacks a essential capabilities needed to
[03:31] build a whole application the actor
[03:34] model complements State charts by
[03:37] providing a framework for concurrent
[03:39] distributed and encapsulated execution
[03:43] that's right not an agent an
[03:45] actor so what is an actor uh an actor uh
[03:50] is an autonomous entity that interacts
[03:53] with other actors via message passing
[03:56] actors and software only have three
[03:58] capabilities they can send and receive
[04:01] messages they can update their internal
[04:03] State and they can create new actors and
[04:07] of course finite State machines can be
[04:09] used to define that actor's internal
[04:13] Behavior or
[04:14] logic so together State machines and
[04:17] actors create a scalable and
[04:19] maintainable application
[04:23] architecture a mentor of mine at Best
[04:25] Buy said that in more in his more than
[04:28] 40 years in it he's never met a finite
[04:32] State machine he did not like why would
[04:35] he today working as a senior principal
[04:37] security Architects say that and the
[04:39] answer is because of the significant
[04:42] advantages that state machines bring to
[04:45] the operator they are predictable
[04:47] they're traceable and auditable they're
[04:50] reliable and recoverable if you lose
[04:53] your current state you can actually
[04:55] recalculate it by playing your replaying
[04:58] your log of events
[05:00] if you only play back some of those
[05:02] events stopping at a certain point in
[05:04] time you can then create a new branch in
[05:07] history effectively traveling through
[05:10] time they're low latency they're
[05:13] declarative as we saw with the state
[05:15] chart itself they're easily tested you
[05:18] can do what's called modelbased testing
[05:20] where you can be programmatically
[05:22] certain that your tests are exercising
[05:24] every valid transition in your
[05:27] machine their modular and adaptable
[05:30] they're scalable and they allow you to
[05:33] handle the most complex error error
[05:35] scenarios even implementing what's
[05:37] called The Saga pattern for distributed
[05:40] transactions in the sagas pattern you
[05:42] have a transaction that takes place over
[05:45] multiple requests if a step in the
[05:47] process fails you can apply compensating
[05:50] transactions to undo the previous steps
[05:54] and get the customer back into a valid
[05:56] state of course they also come with
[05:59] challenges there's a limited uh
[06:02] flexibility to the system and if you're
[06:04] trying to model uh uh a system with
[06:08] thousands perhaps infinite number of
[06:10] states your state can really explode you
[06:13] have to model your transitions
[06:15] explicitly and you can sometimes have uh
[06:18] have an issue where an event lands on
[06:21] your machine that you haven't modeled
[06:23] yet and so thankfully your machine
[06:25] doesn't do anything in that case except
[06:27] for log it for remediation
[06:31] you do have to handle uh concurrency and
[06:35] parallelism because as I mentioned
[06:37] before the actor uh can only process one
[06:40] event at a time this is where something
[06:43] like Azure service bus sessions and AWS
[06:46] sqs 5o message groups would come into
[06:49] play versioning is a definite challenge
[06:52] as maybe you have a state in one version
[06:55] that goes away in the next now if you
[06:57] were to replay your log of events
[06:59] through your machine what state do you
[07:01] land in you have to take this into
[07:03] account and there's a learning curve
[07:05] associated with State machines I think
[07:08] that curve is a joy but you may be
[07:10] feeling something else right
[07:13] now what I want to draw your attention
[07:16] to is that these advantages brought by
[07:19] state machines are everything that llms
[07:23] are not llms are not predictable they're
[07:26] not traceable or auditable they're
[07:29] they're not reliable or recoverable
[07:31] they're not declarative or low latency
[07:34] Etc the opportunity is that by combining
[07:38] llms and state machines together we can
[07:41] build a system that leverages the
[07:43] strengths of one to mitigate the
[07:46] weaknesses of the
[07:49] other so we have our building blocks of
[07:52] agentic systems are actors enable
[07:55] autonomy and
[07:57] communication the state machine provides
[08:00] structure and enforces predictable
[08:02] behaviors and the llm enables Dynamic
[08:07] intelligence so let's put these building
[08:09] blocks into action in the agentic state
[08:11] machines pattern
[08:15] showcase our showcase begins as did the
[08:18] human race with tool use tool use is at
[08:21] the bottom of the autonomy chart because
[08:23] it really is foundational for the other
[08:25] patterns that follow that is it gives
[08:27] the llm the ability to act in tool use a
[08:32] description of available tools is passed
[08:34] to the llm including method names and
[08:37] and expected arguments and the llm
[08:39] returns a response describing to the
[08:41] caller how the tool should be called the
[08:44] llm doesn't call that method
[08:46] directly the llm then expects the next
[08:50] message uh in the flow to be the tool
[08:53] response this is motivated by especially
[08:56] needing to give additional capability
[08:58] and function ity to the llm allowing it
[09:01] to take action tools can also be used to
[09:05] improve response relevance via retrieval
[09:07] augmented generation in this example a
[09:10] model with a prompt to create a recipe
[09:13] is given a tool to fetch the inventory
[09:16] first so that the recipe returned uses
[09:18] only the ingredients that are actually
[09:22] available now right away we can talk
[09:24] about human in the loop human in the
[09:27] loop is something that state machines
[09:28] are natur natur Al very good at this
[09:30] doesn't have anything to do with agents
[09:32] but we all know that llms are famously
[09:35] unreliable so how do we put controls
[09:38] around its use of tools well we can
[09:41] simply add an intermediate intermediate
[09:44] approval step and wait for an
[09:46] authenticated and authorized message to
[09:49] direct what happens next in this example
[09:53] the admin first denies and then approves
[09:55] the request
[09:59] next
[10:00] feedback in feedback instead of having
[10:04] one agent we have two and agents just
[10:07] like humans improve over time with
[10:11] feedback we need to give llms time to
[10:14] think and iterating with feedback either
[10:17] from another agent another human or both
[10:20] can dramatically improve response
[10:22] quality in this example our recipe
[10:25] writer from before uh sends its output
[10:28] to the critic agent perhaps a specialist
[10:31] in nutrition the critic sends its
[10:34] feedback back like use less sugar and
[10:37] the recipe writer has the opportunity to
[10:40] improve its its
[10:42] response here we have two agents working
[10:46] directly together but what if we want a
[10:50] whole team of Agents well that is
[10:55] collaboration with collaboration
[10:57] multiple agents each specializing in
[11:00] their own small slice of a task work
[11:03] together to achieve a broader outcome
[11:06] this is motivated by the training
[11:08] limitations of llms and the scaling
[11:11] limitations of prompting them we can't
[11:14] achieve broad multifaceted goals with a
[11:17] single prompt to a model instead we
[11:20] create specialized units and compose
[11:23] them together into a broader workflow in
[11:27] this example of collaboration
[11:29] multiple agents work together to deliver
[11:32] a meal to a customer we have the recipe
[11:35] writer from before but also an agent
[11:37] specialized in procuring
[11:39] ingredients one that is responsible for
[11:42] preparing the meal getting feedback and
[11:45] finally publishing a
[11:47] report State machines don't need to have
[11:50] a final State and this example the
[11:53] report and any other context is used by
[11:56] the recipe writer as feedback for how it
[11:59] to continuously improve with State
[12:02] machines that flow is predictable and
[12:05] tightly
[12:06] governed but what if we want to change
[12:10] that what if we want to make the
[12:11] sequence of States itself determined by
[12:15] the llm and that is agentic
[12:19] orchestration with orchestration a
[12:21] centralized planning node can direct the
[12:24] next state this is helpful when
[12:27] reasoning around context is required to
[12:30] determine the next state for example by
[12:33] understanding if the goal has been
[12:35] achieved and whether it can exit the
[12:38] flow now the example that I'm showing
[12:40] here got a bit big so I apologize that
[12:43] it's hard to see but notice the bouncing
[12:46] back and forth between various States
[12:48] and the central planning
[12:50] agents the tool in this case that I gave
[12:53] to the planning agent was in fact a set
[12:56] of event
[12:57] emitters and then I implemented
[13:00] transition guards to enforce that these
[13:03] transitions are valid and direct to the
[13:05] appropriate
[13:07] state so we're definitely having fun now
[13:11] Beyond selecting the next state how can
[13:14] we take this even further well what if
[13:18] we gave the whole state chart over to
[13:20] the llm and asked it to generate
[13:23] it I call this agentic chartering I
[13:27] wasn't able to find much about this
[13:30] pattern online there may be a better
[13:33] name for it and if you know of one
[13:35] please let me know in the
[13:37] comments chartering is helpful when you
[13:40] want to separate your planning phase
[13:42] from your execution phase with
[13:44] chartering the agent has the capability
[13:47] of inventing a wholly new and novel
[13:50] process to achieve its goal with
[13:52] prompting and fine-tuning one can
[13:55] imagine llms being able to build these
[13:57] processes using off the-shelf patterns
[14:00] and tools like predetermined events
[14:03] known context available actors
[14:06] Etc so for example I hate postal junk
[14:10] mail when I get something sent to my
[14:13] house I do my best to get myself off
[14:16] whatever list they were using to send it
[14:19] to me wouldn't it be nice if I had a
[14:22] personal agent that could do this work
[14:24] for me to experiment with this I gave an
[14:27] article I found on privacy rights.org
[14:30] for how to remove myself from the White
[14:32] Pages data broker uh and I gave this
[14:36] process to 01 to build a new process uh
[14:39] and it did a remarkable good job
[14:41] especially considering this was done
[14:43] essentially zero shot with no examples
[14:47] uh
[14:49] given llms are also good at interpreting
[14:53] State charts visually just think we have
[14:56] 70 years of State charts s to train on
[15:00] we could add a visualization agent as
[15:03] feedback to the chartering agent to get
[15:06] uh on how to improve its plan that's the
[15:09] fun thing about agents whatever the
[15:12] problem is the solution is always to
[15:14] just add another
[15:17] agent so where is this graph
[15:22] leading I think the answer is towards
[15:26] emergence and now that's one pattern I
[15:28] haven't been able to express with a
[15:30] state chart yet but if we are going to
[15:35] achieve something that performs and
[15:37] feels like emergence I do not be I do
[15:40] not believe it will be because we've
[15:42] created a system model more closely to
[15:45] the human brain it'll be because we
[15:47] found a way to make Building agentic
[15:50] Systems feel like building with Legos
[15:54] all the best technology in my opinion
[15:57] has this quality in in common whether
[16:00] you're building an app with react native
[16:02] deploying it with GitHub actions or
[16:04] provisioning services on AWS with
[16:07] infrastructure as code each of these
[16:10] technologies have a model of composing
[16:12] specialized units together into a
[16:15] broader system that is greater than the
[16:17] sum of its
[16:18] parts so perhaps in achieving that the
[16:22] humble State machine may have a
[16:24] foundational role to play for the next
[16:27] 70 years as well
[16:30] a special thank you to xate the library
[16:33] I used for all the state charts and
[16:35] visualizations in this presentation if
[16:38] you haven't tried xstate already it's a
[16:40] really powerful tool for tackling system
[16:43] complexity and it's a joy to use
[16:45] especially with the changes they made in
[16:48] B5 if you want to see these patterns in
[16:51] action check out my demo red versus blue
[16:54] where I explore more about the
[16:57] operational side of State machines
[16:59] with a surprise emergence at the
[17:02] end please reach out to me on LinkedIn
[17:05] if you have any questions feedback or
[17:07] just want to connect thank you so much
