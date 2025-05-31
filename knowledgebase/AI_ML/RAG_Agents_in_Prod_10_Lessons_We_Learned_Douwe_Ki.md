---
type: youtube
title: RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG
author: Channel Video
video_id: kPL-6-9MVyA
video_url: https://www.youtube.com/watch?v=kPL-6-9MVyA
thumbnail_url: https://img.youtube.com/vi/kPL-6-9MVyA/mqdefault.jpg
date_added: 2025-05-26
category: AI and Enterprise Solutions
tags: ['AI', 'enterprise', 'AGI', 'RAG', 'data management', 'machine learning', 'AI systems', 'model specialization', 'enterprise data', 'AI implementation']
entities: ['AGI', 'RAG pipeline', 'enterprise', 'data', 'AI', 'model', 'pipeline', 'McKinsey']
concepts: ['specialization over AGI', 'enterprise expertise', "data as the company's core", 'pilots vs. scaling', 'systems over models', 'noisy data handling', 'Retrieval-Augmented Generation (RAG)', 'Artificial General Intelligence (AGI)', 'enterprise data management', 'model specialization']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['basic understanding of AI models', 'familiarity with enterprise data systems', 'knowledge of AI pipelines']
related_topics: ['AI specialization', 'enterprise data management', 'RAG pipelines', 'AGI development', 'model systems', 'data cleaning', 'AI implementation challenges', 'enterprise AI strategies']
authority_signals: ["we've learned and I think that many of you might have learned already", 'the model is only a small part of the system and the system is the thing that solves the problem', "if you succeed in doing that that's how you get to differentiated value"]
confidence_score: 0.7
---

# RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=kPL-6-9MVyA)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: rag agents, enterprise ai, ai deployment, context paradox, machine learning, production challenges, ai research  

## Summary

```markdown
# Summary of "RAG Agents in Prod: 10 Lessons We Learned" by Douwe Kiela

## Overview
This video discusses key insights from deploying Retrieval-Augmented Generation (RAG) systems in enterprise settings. The speaker, Douwe Kiela (CEO of Contextual AI), emphasizes the importance of system design over model-centric approaches, the value of domain specialization, and the challenges of scaling AI solutions from pilots to real-world applications. He highlights the critical role of enterprise data and expertise in achieving differentiated value.

---

## Key Points
1. **Systems Over Models**:  
   - Language models are only 20% of the solution; the surrounding system (e.g., data pipelines, retrieval mechanisms) is critical.  
   - A "mediocre" model with a strong RAG pipeline outperforms a "great" model with a weak pipeline.

2. **Specialization Over AGI**:  
   - Enterprise expertise (institutional knowledge) is the fuel for AI.  
   - Specializing models for domain-specific tasks yields better results than relying on generalist AI (AGI) for niche problems.

3. **Data as the Core of the Enterprise**:  
   - Enterprise data, not people, defines the company long-term.  
   - Success depends on enabling AI to work with **noisy, unstructured data at scale**, not just clean data.

4. **The Context Paradox**:  
   - AI excels at "hard" tasks (e.g., code generation) but struggles with context-aware decisions (e.g., business expertise).  
   - Real-world value requires bridging this gap.

5. **Pilots vs. Scale**:  
   - Pilots are easy to build but often fail to scale.  
   - Enterprise solutions must address complexity, integration, and user adoption beyond initial prototypes.

6. **Unlocking Expertise**:  
   - Generalist assistants struggle to match human expertise.  
   - Specialized systems are necessary to capture and operationalize institutional knowledge.

---

## Notable Quotes
- *"The model is only a small part of the system and the system is the thing that solves the problem."*  
- *"Data is the company in the long term."*  
- *"Pilots are very easy... but scaling is incredibly difficult."*

---

## Actionable Takeaways
- **Prioritize system design** over model performance. Invest in robust RAG pipelines and data infrastructure.  
- **Specialize models** for domain-specific use cases to leverage enterprise expertise.  
- **Focus on noisy data** handling to unlock real-world value from existing enterprise data.  
- **Be cautious of pilot success**—scaling requires addressing complexity, integration, and user needs beyond initial proof-of-concept.  
```

## Full Transcript

[00:00] [Music]
[00:16] my name is D Kila I'm the CEO at
[00:18] contextual Ai and I'm here to talk to
[00:20] you about rag in production rag agents
[00:23] specifically um and I'll I'll share some
[00:26] of the lessons that I've learned so my
[00:27] background is in AI research uh but
[00:30] after that I became the CEO of a AI
[00:33] company focus on Enterprise so I thought
[00:36] I would share some of my learnings with
[00:38] you uh in the hope that that's
[00:40] useful so if you uh look at Enterprise
[00:44] AI uh if you work in this space you
[00:46] probably notice that there's a huge
[00:47] opportunity uh ahead of us right
[00:50] everybody wants to grab that opportunity
[00:52] there's there's these huge numbers
[00:54] flying around $4.4 trillion is is the
[00:57] estimated added value to the global
[00:59] economy according to to McKenzie so we
[01:01] have this giant opportunity but at the
[01:04] same time if you actually look at what's
[01:06] happening in Enterprises you see a lot
[01:08] of frustration it's probably even true
[01:10] for some of the people in the audience
[01:11] right here if you're a VP of AI then
[01:14] you're probably under some pressure
[01:15] right now it's like where's the ROI
[01:18] we're investing all this money in AI but
[01:20] where is it actually leading us to are
[01:23] we getting something out of this so uh
[01:26] Forbes has this interesting study where
[01:28] they showed that only one in four or
[01:30] businesses actually get value from AI so
[01:34] why is that happening right it feels a
[01:36] bit like a
[01:37] paradox uh so to to explain it we can
[01:40] look uh at a paradox that might be
[01:42] familiar to you it's it's something
[01:44] called morx Paradox it's from Robotics
[01:47] and in robotics they were very surprised
[01:49] when they found out that it's actually
[01:50] much easier to beat humans at chess than
[01:53] to have a robot that can vacuum clean
[01:55] your house or have a self-driving
[01:58] car um so the the the Paradox here is
[02:02] really that things that seem hard are
[02:04] actually much easier for computers than
[02:06] you would expect and things that seem
[02:08] easy actually turn out to be much harder
[02:11] right so there's something very similar
[02:13] happening right now in in Enterprise AI
[02:15] specifically and this is around context
[02:18] so on the one hand we have these amazing
[02:20] language models right you You' that's
[02:22] why we're all here basically because we
[02:23] see this revolution happening right in
[02:25] front of our eyes so language models can
[02:28] generate code much better than most
[02:30] humans they can solve mathematical
[02:32] problems much better than than most of
[02:34] us here can do uh and we're pretty smart
[02:37] um so it's really amazing what they can
[02:39] do but one of the things that they
[02:41] really still struggle with and that's
[02:42] one of the things that as humans we are
[02:45] very good at sort of without effort is
[02:48] putting things in the right context
[02:51] right so as humans we build on our
[02:53] expertise we build on our intuition that
[02:55] we've developed over the years
[02:57] especially if we're a specialist this is
[02:58] something that is very easy easy for us
[03:00] to do is to put something in the right
[03:02] context and um and in the right
[03:05] situation so that you can make sense of
[03:07] the information or the problem that
[03:08] you're
[03:10] solving so I would argue that this is
[03:13] really the key observation this this
[03:15] context Paradox um for unlocking Roi
[03:19] with AI and the reason for that is that
[03:21] where we are right now here is is in the
[03:23] bottom left right so we're we're mostly
[03:25] focused on convenience we have general
[03:27] purpose assistance they're very use
[03:30] mostly if you're lazy they help you sort
[03:32] of solve your problems faster but where
[03:34] you really want to get to is
[03:36] differentiated value if you're an
[03:38] Enterprise it's nice that you can make
[03:41] things more convenient you probably can
[03:43] make people more efficient and more
[03:44] productive that's great but where you
[03:46] want to get to is this business
[03:48] transformation ideal right that's what
[03:50] all the CEOs are probably telling you as
[03:52] a VP of AI like I want to change my
[03:54] entire business how am I going to do
[03:55] that so getting to that differentiated
[03:58] value that's where you want to get to
[04:00] but the problem is that the higher you
[04:02] go on that axis the further you go on
[04:04] the context axis so the the better you
[04:07] need to be at handling the context uh uh
[04:10] that exists within your
[04:13] Enterprise um so what should we do about
[04:16] that um so that observation is really
[04:18] why I started the company that I'm
[04:20] currently the the CEO of contextual AI
[04:23] um and we started this two years ago to
[04:26] try to help bridge this Gap um and we've
[04:28] learned some lessons along the way that
[04:30] I thought I would share with you uh in
[04:32] the hope that they're also useful for
[04:34] you so the first observation is really
[04:38] that language models are awesome but
[04:40] often they're only 20% of a much bigger
[04:43] system um so if you have an Enterprise
[04:46] AI deployment usually that means it's a
[04:48] rag system uh so I I think everybody
[04:52] here probably has heard of rag uh rag is
[04:54] something that I uh originally pioneered
[04:57] with my team at Facebook a research when
[04:59] I was there uh so rag is is really kind
[05:02] of the standard way that you get gen to
[05:04] work on your data so what happens very
[05:07] often these days is a new language model
[05:09] comes out everybody goes whoa new
[05:11] language model it's great everybody
[05:13] starts to think just about the language
[05:15] model but very few people actually think
[05:17] about the system around the language
[05:18] model and that system needs to solve the
[05:20] problem right so you can have a
[05:23] relatively mediocre language model but
[05:24] an amazing rag pipeline around it and
[05:27] that's going to be much better than an
[05:28] amazing language model with a terrible
[05:30] rag pipeline around it so the basic
[05:32] observation here or the lesson is that
[05:35] you should be thinking about systems not
[05:37] about models the model is only a small
[05:39] part of the system and the system is the
[05:41] thing that solves the
[05:42] problem the next observation is that if
[05:45] you're in an Enterprise expertise is
[05:47] really your fuel right so uh one of the
[05:50] the things that you want to be able to
[05:51] do as an Enterprise is unlock all of
[05:53] that expertise so you have all of this
[05:55] institutional knowledge in your company
[05:58] how do you get it out um so one way to
[06:01] try to do that is is using these
[06:03] generalist kind of general purpose
[06:05] assistant but it's very hard to get them
[06:07] to to uh to match the expertise of
[06:09] people in your company so ideally what
[06:11] you want to do is to specialize so that
[06:14] you can capture that expertise much
[06:16] better so uh at my company we call this
[06:19] specialization over AGI AGI is great
[06:21] there are lots of use cases for it if
[06:23] you really want to solve a very
[06:25] difficult problem that is very domain
[06:26] specific where you understand the use
[06:28] case you to specialize for it and you'll
[06:30] get much further so that's I guess uh
[06:33] pretty counterintuitive if you look at
[06:35] the sort of broader uh interest right
[06:38] most people are much more excited about
[06:39] AGI but solving real problems is much
[06:41] easier with
[06:44] specialization uh next lesson is uh at
[06:47] an Enterprise scale is your remote so if
[06:49] you think about what a company really is
[06:51] is a company maybe its people probably a
[06:54] little bit right but over time what the
[06:56] company really is or what makes a
[06:58] company a company is it's data because
[07:00] even people are transient right so the
[07:03] data that a company owns that is the
[07:05] company in the long term so now as an
[07:08] Enterprise you need to think how you can
[07:10] unlock all of that potential right and
[07:12] so U one of the the big issues that we
[07:15] see a lot is that enterprises think that
[07:18] uh you need to scrub the data and clean
[07:20] it and invest a lot of time in in uh
[07:22] making your data accessible with AI but
[07:25] what you really want to do is make sure
[07:26] that AI can work on your noisy data at
[07:29] scale and doing that is incredibly
[07:32] difficult but if you succeed in doing
[07:33] that that's how you get to
[07:35] differentiated value right that's how
[07:37] you get that mode because the data makes
[07:39] makes your company your company and so
[07:41] that data is really your
[07:44] mode uh one observation uh and this is
[07:47] really a hard truth that that we've
[07:49] learned and I think that many of you
[07:50] might have learned already or that
[07:52] you're about to find out uh if you're
[07:54] earlier in in your journey is that
[07:56] Pilots are very easy uh building a Mo
[08:00] not very difficult these days right if
[08:01] you want to build a rag system you take
[08:03] one of the Frameworks you put in some
[08:05] documents you have a working solution
[08:07] it's great you give it to your 10 users
[08:09] they all tell you it's fantastic and
[08:11] then you show it to the CEO and he says
[08:13] okay we're going to fire half the
[08:15] customer support team and we're going to
[08:16] replace them with AI and we're going to
[08:18] do that in three months and now you're
[08:20] on the hook for productionizing
[08:22] something that is actually much much
[08:23] harder right so getting this to work at
[08:26] tens of thousands or hundreds of
[08:28] thousands or millions of documents you
[08:31] can't do that with any existing tools uh
[08:33] that are out there on the open source
[08:34] market it's very very difficult to do
[08:36] that making the skill to thousands of
[08:38] users is very hard uh making it work for
[08:41] lots of different use cases if you're an
[08:42] Enterprise maybe you have 20,000
[08:44] different use cases that you want to
[08:46] cover so how do you scale if that's the
[08:48] problem that you're solving and then
[08:50] there's of course Enterprise
[08:51] requirements around security and and
[08:53] compliance so bridging that Gap is much
[08:55] harder than you think and and the the
[08:57] right way to deal with that is to really
[08:59] focus on production from day one so
[09:01] don't design for the pilot design for
[09:03] production uh and that can save you a
[09:05] lot of time and that brings me to the
[09:07] next observation is that speed is really
[09:10] much more important than Perfection what
[09:12] we see um in terms of production
[09:15] rollouts of uh rag agents it's all about
[09:19] speed um and and what that means is uh
[09:22] you need to give it to your users
[09:24] relatively early real users not not sort
[09:27] of uh testers who are are kind of
[09:29] friendly you want to give it to real
[09:31] users to get their feedback you want to
[09:34] do that early it doesn't have to be
[09:35] perfect it just needs to be barely
[09:37] functional and if you do that then you
[09:38] can Hill Climb to actually get to this
[09:40] level where it's good enough if you
[09:42] don't do that and you wait too long and
[09:44] then you try to design something that is
[09:46] perfect it's going to be very hard to to
[09:48] bridge that Gap from Pilot to production
[09:51] so iteration is really the key to a lot
[09:53] of uh successful uh production AI
[09:56] deployments in in Enterprises
[09:59] next observation is is related to this
[10:02] too which is that uh if you want your
[10:04] engineers to be fast and if you want to
[10:06] follow that that speed Maxim I just
[10:08] talked about then you don't want them
[10:10] work working on boring stuff uh sounds
[10:13] kind of obvious but it turns out that
[10:15] Engineers are working on a lot of very
[10:17] boring stuff um and so one of one of the
[10:20] the things that they have to worry about
[10:22] for example is what is the optimal
[10:23] chunking strategy for my rag system and
[10:25] it's different for every use case and
[10:27] it's different for every framework and
[10:29] then they have to think about what the
[10:30] right prompt is or really basic things
[10:32] that ideally they don't have to think
[10:34] about too much because you really want
[10:36] your engineers to think about how are am
[10:38] I going to deliver business value right
[10:41] how how do I make sure I have this
[10:42] differentiated value and that I'm
[10:44] actually better than my
[10:46] competitors um so make sure that your
[10:48] engineers spend time on the things that
[10:50] matter and not on the chunking strategy
[10:52] or or things that that can be abstracted
[10:55] away uh very well these days by by state
[10:57] ofth artk platforms for for drag
[11:00] agents next one is is about making AI
[11:04] easy to consume so what what I mean by
[11:07] that is we actually see uh this happen
[11:09] quite often where companies have Genai
[11:11] running in production and then the next
[11:14] question I often ask them is okay how
[11:15] many people are actually using it and
[11:18] and surprisingly often the answer is
[11:20] zero almost nobody's actually using it
[11:23] they did all this work but they had to
[11:25] make sure it came through uh sort of
[11:27] model risk and and uh teams like that so
[11:30] it was really like kneecapped almost and
[11:33] now it's barely useful uh so that's one
[11:35] scenario or or very often people just
[11:37] don't actually know how to use the
[11:39] technology so it it really is a journey
[11:42] that you are on uh and the easier you
[11:44] can make your solutions to consume the
[11:47] better it is and what that what that
[11:49] means for most Enterprises is not just
[11:51] thinking about your Enterprise data and
[11:53] how you make AI work on it but also how
[11:55] you integrate it into their workflows so
[11:58] the closer you can integrate ated into a
[11:59] workflow that already exists in your
[12:01] Enterprise the more successful you're
[12:03] going to be with real production
[12:06] usage uh next one is is related uh to
[12:11] the previous one as well uh where it's
[12:13] really about getting usage it's about
[12:15] sort of being sticky and and so this
[12:18] sounds maybe a little obvious but the
[12:21] the quicker you can wow users or get
[12:23] this sort of spark where they they
[12:25] suddenly get it like this for for me as
[12:27] a CEO of AI company that's really the
[12:29] special moment when people suddenly go
[12:31] like wow I didn't know that it could do
[12:33] this um so you can try to design your
[12:36] experiences for onboarding users around
[12:39] this observation too right so where
[12:41] where they get to the wow as quickly as
[12:43] possible so for us we had this really
[12:45] nice example with someone at Qualcomm so
[12:47] we're we're running in production
[12:49] globally with Qualcomm with thousands of
[12:51] customer engineers and one of them
[12:53] became so happy when they found this
[12:55] document it was 7 years old it was
[12:56] hidden away somewhere they didn't know
[12:58] it existed they had all these questions
[13:00] and they just never knew what the
[13:01] answers were and suddenly because they
[13:03] asked our system they got these answers
[13:05] and like their their world was never the
[13:08] same again after that um so these are
[13:11] the the small the small winds sort of uh
[13:13] that that really matter for for uh
[13:15] evangelizing uh production in
[13:19] AI uh so that brings me to the the
[13:22] penultimate learning which is that it's
[13:24] not even really about accuracy anymore
[13:26] so accuracy is almost table Stakes right
[13:29] uh so I I think as AI practitioners we
[13:31] probably know that getting 100% accuracy
[13:34] is very hard if not impossible getting
[13:36] 95% accuracy maybe you can get there or
[13:39] 90% but what Enterprises are are
[13:41] thinking about much more these days is
[13:43] what about the missing 5% or what about
[13:46] the missing 10% how do I deal with the
[13:48] things that might go wrong right um so
[13:51] there's a minimum requirement for
[13:52] accuracy but beyond that is really about
[13:54] inaccuracy and the way to deal with that
[13:56] is through observability so you want to
[13:58] be very care care f with how you
[13:59] evaluate these systems you want to be
[14:01] very careful with making sure you have
[14:03] proper audit Trails especially if you
[14:05] work in a regulated industry this is
[14:06] incredibly important right making sure
[14:08] that you have an audit Trill that says
[14:10] this is why I generated this answer it's
[14:12] because I found it here in this document
[14:15] basic things like that so attribution
[14:17] essentially in a rag system actually
[14:19] becomes very very important for dealing
[14:21] with the inaccuracies and similarly what
[14:23] you can do is you can check the claims
[14:25] that your system generates so do a lot
[14:27] of postprocessing to ensure that you
[14:29] have proper attributions uh that that
[14:31] you can really back up uh as
[14:38] evidence struggling with the clicker a
[14:40] bit so uh F final one uh that I want to
[14:44] end on and this sounds maybe a little
[14:45] bit cheesy but it it it really is is
[14:48] true is be ambitious we we actually see
[14:51] a lot of projects fail not because
[14:54] people are aiming too high but because
[14:55] people are aiming too low where where
[14:58] folks are going like I have gen running
[15:00] in production and then what does it do
[15:02] it answers basic questions about who
[15:03] your 401k provider is or how many days
[15:06] of vacation I get like that's not really
[15:09] where the ROI of AI is right so you want
[15:12] to aim for really ambitious things where
[15:14] if you solve them you actually have have
[15:16] Roi and you don't just have a gimmick
[15:18] that people don't really uh use anyway
[15:20] so try to be be ambitious because we
[15:23] really live in special times we have the
[15:25] the astronaut here on the slide um so so
[15:29] I I think it was a pretty special time
[15:31] to be alive during the the moon landing
[15:33] and when all of that happened right
[15:34] we're in a in a similar moment right now
[15:36] where AI is is really going to change
[15:38] everything is going to change our entire
[15:41] Society in the next couple of years um
[15:43] and so you have an opportunity being in
[15:45] the role that you're in to to Really uh
[15:48] uh affect that change in society
[15:50] yourself uh so so be ambitious when you
[15:53] do that uh and don't aim for the the
[15:55] loow hanging easy fruit uh aim for for
[15:58] the sky
[16:00] so uh that's really U what what my
[16:03] lessons were for you here uh this
[16:04] context Paradox is not going away um but
[16:08] by understanding these lessons that I I
[16:10] shared with you hopefully you can turn
[16:12] some of these challenges uh that we see
[16:14] everywhere in Enterprise AI into
[16:16] opportunities for yourself um so so it's
[16:19] really build better systems think about
[16:21] systems not models focus on your
[16:23] expertise and specialize for it don't
[16:25] settle for General Solutions specialize
[16:28] for for expertise that you have in your
[16:30] company and be ambitious and then you'll
[16:32] be very successful thank you
[16:35] [Applause]
[16:37] [Music]
