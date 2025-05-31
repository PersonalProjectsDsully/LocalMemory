---
type: youtube
title: Building LinkedIn's GenAI Platform — Xiaofeng Wang
author: AI Engineer
video_id: n9rjuBuShko
video_url: https://www.youtube.com/watch?v=n9rjuBuShko
thumbnail_url: https://img.youtube.com/vi/n9rjuBuShko/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['AI platform', 'machine learning', 'platform development', 'AI systems', 'orchestration', 'prompt engineering', 'memory management', 'responsible AI', 'AI governance', 'model optimization', 'SDK', 'AI infrastructure']
entities: ['LinkedIn JI ecosystem', 'open source models', 'fine-tune', 'responsible AI layers', 'AI platform or machine learning infrastructure team', 'onr model', 'hotel', 'SDK']
concepts: ['AI systems', 'platform development', 'orchestration', 'prompt engineering', 'skills invocation', 'memory management', 'operability', 'governance', 'best practices', 'AI model optimization']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Understanding of AI models and machine learning', 'Familiarity with software development practices', 'Basic knowledge of AI deployment pipelines']
related_topics: ['AI platform development', 'machine learning infrastructure', 'responsible AI', 'model optimization', 'AI governance', 'software architecture', 'AI model integration', 'devops for AI']
authority_signals: ['we feel like J is totally different new AI systems compared to the traditional AI systems', 'we can make sure our developers are building the applications efficiently but also responsibly', 'we started to invest on the operability']
confidence_score: 0.85
---

# Building LinkedIn's GenAI Platform — Xiaofeng Wang

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=n9rjuBuShko)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: generative ai, ai platform, gpt-4, python sdk, prompt engineering, machine learning, ai models  

## Summary

# Summary of "Building LinkedIn's GenAI Platform"  

## **Overview**  
Xiaofeng Wang discusses LinkedIn's journey in developing a unified Generative AI (GenAI) platform to streamline AI application development, address technical complexity, and enforce governance. The platform evolved iteratively, incorporating orchestration, prompt engineering, skills invocation, and memory management to support advanced AI systems like multi-agent frameworks and responsible AI practices.  

---

## **Key Points**  
- **Evolution of the Platform**:  
  - Started with early features like "collaborative articles" using GPT-4, then expanded to a second-gen co-pilot system.  
  - Built a four-layer architecture: **orchestration**, **prompt engineering tools**, **skills invocation**, and **memory management**.  
  - Introduced a multi-agent system for recruiters, enabling autonomous decision-making via API and LLM calls.  

- **Core Components**:  
  - **Orchestration**: Unified interface for complex AI ecosystems (e.g., model fine-tuning, responsible AI, ML infrastructure).  
  - **Prompt Engineering**: Tools to simplify integration with open-source or custom models.  
  - **Memory Systems**: Layers like working memory, long-term memory, and collective memories to enhance agent awareness.  
  - **Operability**: In-house solutions for tracking agent behavior, replaying interactions, and analytics for optimization.  

- **Why Build In-House?**  
  - Traditional AI systems separate model optimization and serving phases, but GenAI blurs this line.  
  - A centralized platform ensures governance, reduces infrastructure complexity, and enforces best practices.  

- **Sister Teams**:  
  - Collaboration with teams for model optimization, responsible AI policies, and ML infrastructure hosting.  

---

## **Important Insights**  
- **Centralized Platform Value**:  
  - Acts as a unified interface, allowing developers to switch models (e.g., open-source vs. custom) with minimal code changes.  
  - Enforces governance to ensure responsible AI development.  

- **Challenges Addressed**:  
  - Complexity of integrating multiple AI systems.  
  - Need for transparency and control over autonomous agent behavior.  

- **Key Takeaway**:  
  - Building a custom platform was critical for LinkedIn’s unique GenAI needs, as vendor products lacked flexibility and governance for their ecosystem.  

---

## **Actionable Recommendations**  
1. **Build a Unified Platform**: Centralize AI components to simplify development and enforce governance.  
2. **Invest in Prompt Engineering**: Reduce infrastructure complexity through tools and abstraction.  
3. **Develop Memory Systems**: Create layered memory architectures to enhance agent awareness and decision-making.  
4. **Prioritize Operability**: Implement tracking and analytics for agent behavior to enable continuous optimization.  
5. **Balance Custom and Vendor Solutions**: Build in-house for unique needs, but leverage external tools where appropriate.

## Full Transcript

[00:00] [Music]
[00:17] uh it's my pleasure here to share our
[00:19] journey on building out linkedin's ji
[00:22] platform uh my name is sh ad manager of
[00:25] J
[00:28] Foundation uh and try it one more time
[00:31] cool uh in today's talk I'd like to
[00:35] First share our journey on building out
[00:37] this platform especially on why we're
[00:40] building it how we build it and what
[00:42] we're building it after that we will
[00:45] talk about uh some thought process on
[00:48] why this platform is critical for
[00:50] today's agent
[00:52] word um hopefully after that you agree
[00:54] with me this is critical component in
[00:56] your component uh uh in your company and
[00:59] you also want to build this team I want
[01:01] to share some tips on how to build such
[01:04] a team how to H for such a team towards
[01:06] the end we will share some K takeways
[01:08] and the Lessons
[01:10] Learned before we dive into this
[01:14] application uh platform journey I think
[01:17] it's important to first talk about the
[01:19] ji product experience because that's
[01:22] essentially what our platform is
[01:24] supporting for back in 2023 LinkedIn
[01:29] launched the four first the formal GI
[01:31] feature called collaborative articles
[01:34] this is a kind straightforward uh GI
[01:37] feature if we are thinking in this
[01:39] standard because it's a very simple
[01:42] prompt in string out type of
[01:45] application uh we leverage chat GPT uh I
[01:49] mean we leverage GPT 4 model uh to
[01:52] create the long content uh articles on
[01:54] the platform and they invite our members
[01:57] to comment on it at this stage our team
[02:00] helped to build some key component
[02:03] behind the scene including the gateway
[02:05] to centralize the access to the model uh
[02:08] some Pyon notebook for the prom
[02:10] engineering uh but at this time we
[02:13] actually have two different Tex Stacks
[02:16] uh to serve the uh experience in the
[02:19] online phase we use Java and in the back
[02:21] end we use Python uh we wouldn't call
[02:24] this as a platform at this
[02:27] time very soon we realize there are some
[02:30] limitation for this simple approach
[02:33] especially it lacks the capability to
[02:35] inject our reach data into the product
[02:39] experience then in the mid 2023 we
[02:42] started to develop the second generation
[02:45] of the ji product uh internally we
[02:48] called a co-pilot or coach here we're
[02:51] showing one popular such experience on
[02:53] LinkedIn right now uh basically it looks
[02:56] at uh your profile and the job
[02:59] description and then uh use uh some rag
[03:03] process to give you personalized uh
[03:06] recommendation on if you are good fit to
[03:08] the
[03:09] job at this time we started to build uh
[03:13] some platform capability uh specifically
[03:16] in the center of our platform we build
[03:19] the uh python SDK on top of the popular
[03:23] uh lunching framework to orchestrate
[03:26] ourm calls and it also provide the key
[03:29] value to integrate with our large scale
[03:31] infrastructure uh in this SDK so our
[03:35] developers can easily assemble
[03:38] application we started to unify the text
[03:40] stack at this stage because we realize
[03:43] it's really costly to transfer the
[03:45] python prompt into the Java world not to
[03:48] mention the arrow during this process we
[03:51] started to invest on the prompt
[03:53] management or promp source of Truth this
[03:56] is a subm module at this stage uh to
[03:59] help developers to version their prompt
[04:02] and to provide some structure around
[04:04] their meta
[04:06] prompt uh the most important piece I'd
[04:08] like to call out here is conversational
[04:11] memory uh this is uh infrastructure to
[04:14] help to keep track of the llm
[04:17] interactions and retrieval content and
[04:20] then inject those content into the final
[04:23] product it will help us to build this
[04:26] kind of conversational uh bot
[04:31] now uh zooming to this year uh actually
[04:33] in the last year uh we launched our
[04:35] first ever uh real multiagent system
[04:39] called uh LinkedIn H assistant uh this
[04:42] is uh multi-agent systems to help our
[04:45] recruiters to do their work uh
[04:48] efficiently especially it automate
[04:51] several teers task normally recuiter
[04:54] need to do manually like um post the job
[04:58] um and the valuate hundreds of
[05:01] candidates then reach out to
[05:05] them our platform also start to involve
[05:08] into the agent platform uh from the
[05:11] framework side we extend the support of
[05:15] the Python SDK into a more large skilled
[05:19] um distributed agent orchestration layer
[05:21] it will handle the distributed agent
[05:24] execution and also handled the more
[05:26] complicated scenarios like retry logic
[05:30] and the traffic shift uh for folks who
[05:33] build agent uh I think you probably know
[05:36] the skills or apis are one key aspect of
[05:39] the agent because we expect uh this
[05:42] agent to perform some action one
[05:45] investment we did at this uh time is
[05:48] around the skill registry basically we
[05:51] have a set of tools uh to help our
[05:54] developers to publish their API into
[05:56] this centralized skill registry this
[05:59] skill
[06:00] can handle the skill Discovery problem
[06:03] skill invocation problem so in your
[06:05] application it's actually very easy to
[06:07] call the API to perform some
[06:10] task another key component uh we invest
[06:14] at this stage is on the memory in
[06:16] addition to the conversational memory we
[06:18] extend uh it capability into the
[06:21] experential memory essentially it's a
[06:24] memory storage to uh extract and analyze
[06:28] and infer the tectural Knowledge from
[06:31] the interaction between the agent and
[06:32] our user we also organize this memory
[06:35] into different layers including the
[06:39] um working memory long-term memory
[06:42] Collective memories uh this can help our
[06:45] agent to be aware of the surrounding
[06:47] content uh lastly at this uh time we
[06:50] also realize the operability is super
[06:52] important because agent uh one key
[06:55] aspect to Define agent is autonomous
[06:58] right uh because agent can decide what
[07:01] API they can call what L LM they need to
[07:06] call so it's actually very hard to
[07:08] predict Its Behavior so we started to
[07:10] invest on the
[07:12] operability uh particularly we build our
[07:14] in-house Solution on top of the hotel to
[07:17] keep track very low level granularity of
[07:20] the uh telary data so we can use this
[07:24] data to replay the uh agent call and we
[07:27] also add a actual layer of the analytics
[07:30] on top of it so we can use that to guide
[07:32] the future optimization of our agent
[07:36] systems let's put together all the
[07:39] components we build for this platform uh
[07:42] we can classify them into four layers
[07:44] basically including the orchestration
[07:47] prom engineering tools and skills
[07:50] invocation content and the memory uh
[07:53] management uh of course that's not
[07:56] everything in the LinkedIn ji ecosystem
[07:59] uh in addition we have our sister teams
[08:02] to build out the modeling layer like
[08:04] fine tune the open source models
[08:06] responsible AI layers to make sure the
[08:09] agent is behave according to our policy
[08:12] and standard and also the uh AI platform
[08:16] or machine learning infrastructure team
[08:18] to host those
[08:20] models the key value preparation for
[08:23] this uh ji platform is actually to uh be
[08:27] the unified inter interace for this
[08:30] complex
[08:32] ecosystem so our developers don't need
[08:35] to necessarily understand all those
[08:37] individual box when they build uh their
[08:40] application instead they can leverage
[08:42] our platform to quickly access to this
[08:45] entire ecosystem uh for example uh in
[08:50] our SDK the developer can just switch
[08:53] one parameter in the one L of the code
[08:55] to switch from the open a model to our
[08:58] onr model model of course they still
[09:00] need to do the prompt engineering but
[09:02] that reduce a lot of the complexity on
[09:05] the infrastructure integration
[09:08] face uh last but the most importantly is
[09:12] because of this is centralized platform
[09:15] uh it provide a place to enforce the
[09:18] best practice and governance so we can
[09:20] make sure our developers are building
[09:22] the applications efficiently but also
[09:26] responsibly as you can see from our
[09:28] journey we actually start to build this
[09:31] uh platform piece by piece and then this
[09:33] platform start to emerge if we take one
[09:36] step back and think uh do we really need
[09:39] this platform at this time especially
[09:41] there are lots of uh uh uh vendor
[09:45] product on this space shall we buy it
[09:47] build it and why do we need to buy it or
[09:50] build it uh here are some
[09:52] thoughts um the short answer is yes the
[09:55] reason behind it is uh we feel like J is
[09:59] totally different new AI systems
[10:02] compared to the traditional AI systems
[10:04] so in the traditional AI systems there's
[10:06] a clear cut off between the uh AI model
[10:10] optimization phase and the model serving
[10:13] phase so AI engineers and product
[10:16] Engineers can operate in two different
[10:18] tax stack uh they usually don't uh need
[10:20] to uh work on the same code base but in
[10:24] the ji systems what we're seeing is this
[10:29] line between the optimization phase and
[10:31] the serving phase disappear basically
[10:34] everyone is a engineer who can optimize
[10:38] the overall system performance this
[10:41] actually created the new challenge of
[10:43] the tooling and the best practice in the
[10:46] company essentially we think this ji
[10:49] systems or agent systems is a compound
[10:53] AI system here we borrow the definition
[10:55] from Berkeley AI research lab a compound
[10:58] AI system can be defined as a system
[11:00] which tackles AI tasks using multiple
[11:03] interacting components including
[11:05] multiple cost to model retrievers or
[11:08] external tools as you can see this is
[11:10] actually skill across AI engineer and
[11:13] product engineer and I believe this uh J
[11:17] app platform is trying to bridge this
[11:22] Gap to summarize uh we believe this
[11:25] platform is critical for your success
[11:27] mainly because it can Bridge the skill
[11:30] gaps between those two group
[11:33] Engineers okay let's say if you want to
[11:36] build this uh platform in your company
[11:39] and how to hire it is a frequent
[11:42] question uh I heard um I basically look
[11:46] into uh my great engineering team and uh
[11:50] extract all the key qualifiers from
[11:52] those top engineers and uh I put all the
[11:55] qualifications here uh the ideal
[11:58] candidate in this team is a strong
[12:01] software engineer uh who can build
[12:05] infrastructure integration they have a
[12:07] good developer uh PM skills to design
[12:11] the interface uh ideally they have the
[12:14] AI and the data science background to
[12:17] understand the latest techniques they
[12:19] are the people who can learn from the
[12:21] latest techniques but at the same time
[12:23] they are hands
[12:25] on unfortunately it's really hard to
[12:28] guide those candidates if you get them
[12:30] uh it's probably worth more than
[12:32] unicorn realistically we are making
[12:35] multiple tradeoff in the Hing uh here
[12:38] are some principle uh we follow and it's
[12:41] actually working pretty well on to share
[12:44] here in terms of the core skills uh we
[12:47] usually prioritize the stronger software
[12:50] engineering skills over the AI expertise
[12:54] this might be controversial but uh uh uh
[12:57] we can discuss if you're
[12:59] interested second is instead of hiring
[13:03] for experience or degrees we hire for
[13:05] the potential because this field is
[13:08] involving so fast most of the experience
[13:11] might be
[13:13] outdated in case you won't be able to
[13:15] find a single engineer with all the
[13:17] qualifications we're showing here uh the
[13:21] way we are solving this problem is to
[13:24] hire a diversified team so so for
[13:27] example uh in our team we have some full
[13:31] stack software Engineers we have data
[13:34] scientist we have ai engineers and data
[13:37] Engineers we also have a fresh grads uh
[13:41] from the top research University and
[13:44] also uh some people from the startup
[13:48] background and then we put them together
[13:50] uh into the project what we've seen is
[13:53] based on those collaboration those
[13:56] strong Engineers start to pick up new
[13:57] skills in the project and very soon they
[14:00] started to grow into these ideal
[14:03] candidates uh lastly is uh want to
[14:06] emphasize is uh the critical thinking uh
[14:10] one constant topic uh in our team
[14:12] meeting is uh no matter what we're
[14:14] building right now it will be outdated
[14:16] within a year or even less than six
[14:19] month so we consistently evaluate the
[14:21] latest open source package talking with
[14:24] vendors and deprecate our solution more
[14:27] proactively
[14:30] cool let's talk about the say some uh K
[14:33] takeways uh especially on the tax stack
[14:37] choice if possible we strongly recommend
[14:40] python we started with Java and python
[14:43] uh there are some back and forth of the
[14:45] debate internally but finally we pick
[14:47] Python and I think that's a right choice
[14:50] especially most research and open source
[14:53] uh are in this space based on our
[14:56] experience it's also scalable
[14:59] in terms of the uh key components you
[15:01] want to build in this platform the first
[15:03] one is prompt source of Truth prompt in
[15:06] some way is like a traditional model
[15:09] parameters you want to have a really
[15:11] robust systems to Version Control your
[15:13] prompt this is really really critical
[15:16] for the operational stability you don't
[15:18] want accidentally addit your promp in
[15:20] production and uh see some really S
[15:24] effect second key component is on the
[15:26] memory I think in today's uh me Mee uh I
[15:30] mean today's talk someone already talked
[15:32] about it memory is a really key
[15:34] component to inject your Rich data into
[15:38] the agent experience lastly in the agent
[15:42] era uh one key new component we are
[15:46] building is on the uplifting our apis
[15:49] into skills which can be called from the
[15:53] agent easily so you can uh build some
[15:56] surrounding tooling and infrastructure
[15:58] to support this
[16:01] need all right let's talk about how to
[16:04] uh skill this solution and got get it
[16:07] adopted uh from our experience instead
[16:10] of trying to build this full-fledged the
[16:12] platform at the beginning try to solve
[16:15] immediate need for example we started
[16:18] with a simple python library to support
[16:21] orchestration then we started to grow
[16:23] into all the components we're seeing
[16:25] here second is uh focus on the
[16:29] infrastructure and the scalable solution
[16:31] and Linkedin we actually have a pretty
[16:33] good success story by leveraging our uh
[16:36] messaging infrastructure uh to be as a
[16:39] memory layer uh is both cost efficient
[16:42] and scalable last day is uh focus on the
[16:46] developer experience by the end of the
[16:49] day this platform is trying to help
[16:51] developer to be as productive as
[16:53] possible their adoption is a key for the
[16:56] success if you can design this platform
[16:59] please focus on uh how to align your
[17:02] technology with their existing uh
[17:05] workflow so it will ease adoption and uh
[17:08] be more
[17:10] successful uh we actually have lots of
[17:12] lowlevel details on the technical side
[17:15] uh if you are interested please check
[17:17] out our engineering blog post on
[17:19] LinkedIn by Cake s and
[17:23] myself uh with that uh thank you for
[17:26] your attention and uh if you are having
[17:28] more questions question happy to answer
[17:30] that after the talk thank you
[17:33] [Music]
