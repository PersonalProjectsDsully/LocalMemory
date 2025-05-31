---
type: youtube
title: Trust, but Verify: Knowledge Agents for Finance Workflows - Mike Conover
author: Channel Video
video_id: MWTJIAwAAnk
video_url: https://www.youtube.com/watch?v=MWTJIAwAAnk
thumbnail_url: https://img.youtube.com/vi/MWTJIAwAAnk/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: []
entities: ['Brightcove', 'Adobe', 'DLP', 'SaaS', 'AI', 'machine learning', 'data science', 'natural language processing', 'predictive analytics', 'cloud computing']
concepts: ['AI agent development', 'data privacy', 'content delivery', 'enterprise software', 'cloud infrastructure', 'machine learning models', 'data science workflows', 'natural language processing techniques', 'predictive analytics applications', 'SaaS business model']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of AI and machine learning', 'familiarity with data science principles', 'knowledge of cloud computing concepts']
related_topics: ['AI ethics', 'data governance', 'enterprise AI solutions', 'cloud security', 'machine learning deployment', 'SaaS analytics', 'NLP applications', 'predictive modeling']
authority_signals: ["'the scaffolding that products put in place in order to orchestrate these workflows...'", "'the most interesting interactions I've had with language models are deep into a conversational tree...'"]
confidence_score: 0.8
---

# Trust, but Verify: Knowledge Agents for Finance Workflows - Mike Conover

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=MWTJIAwAAnk)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai, machine-learning, finance, knowledge-agents, data-processing, automation, financial-research  

## Summary

# Summary of "Trust, but Verify: Knowledge Agents for Finance Workflows"

## Overview  
Mike Conover, founder of Bright Way VI, discusses the challenges of managing vast amounts of data in finance workflows (e.g., due diligence, earnings reports, and contract analysis) and introduces the role of AI-driven knowledge agents. He draws parallels to the early days of spreadsheets, emphasizing how tools can transform labor-intensive tasks into efficient processes. The talk highlights technical hurdles like error accumulation in non-reasoning models, the need for human-like decision-making in agents, and the importance of product design to reduce user burden.

---

## Key Points  
1. **Challenges in Finance Workflows**  
   - Overwhelming data volumes in tasks like due diligence, earnings season, and vendor contract analysis.  
   - Manual processing is time-consuming and error-prone, with high human costs.  

2. **AI Agents as a Solution**  
   - Knowledge agents can automate tasks like analyzing SEC filings, earnings calls, and constructing knowledge graphs from past deals.  
   - Mimicking human decision-making by decomposing tasks (e.g., identifying public market comparables for cost analysis).  

3. **Technical Limitations**  
   - Non-reasoning models risk error accumulation and "off-the-rails" outputs.  
   - End-to-end reinforcement learning (RL) over tool use is critical but not yet fully solved.  

4. **Model Constraints and Regularization**  
   - Regularization parameters act as "safeguards" to limit model complexity and reduce degenerate outputs.  
   - Conversational trees and activations guide models toward solutions, akin to a human "chain of thought."  

5. **Product Design and User Experience**  
   - Users shouldn’t need 1,000+ hours of training to become prompting experts.  
   - Verticalized workflows and scaffolding (e.g., intent-driven interfaces) reduce user cognitive load.  

6. **The "Bitter Lesson"**  
   - More data, compute, and better models outperform expert systems or rule-based approaches.  

---

## Quotes & Insights  
- **"Trust, but verify"**: The title reflects the need for AI systems to be reliable yet require human oversight.  
- **"The human cost of manual data processing"**: Highlighting the inefficiency of current finance workflows.  
- **"Spreadsheets changed the role of accountants"**: A metaphor for how AI agents could redefine financial professionals' tasks.  
- **"The chain of thought is about nudging activations"**: Emphasizing the role of conversational interactions in guiding model behavior.  
- **"Verticalized product workflows are enduring"**: Suggesting that structured tools will remain critical for usability.  

---

## Actionable Items  
- **Invest in verticalized workflows**: Design products that encode intent and reduce user expertise requirements.  
- **Implement regularization**: Use constraints to prevent model instability and degenerate outputs.  
- **Prioritize end-to-end RL**: Focus on systems that integrate tool use with reasoning for complex tasks.  
- **Build scaffolding for orchestration**: Create interfaces that guide users without requiring deep prompting expertise.  
- **Decompose tasks humanely**: Mimic how humans approach problems (e.g., using comparables, knowledge graphs).  

--- 

This summary captures the core themes, technical challenges, and practical recommendations from the talk, emphasizing the balance between AI capabilities and human-centric design in finance.

## Full Transcript

[00:00] [Music]
[00:16] I'm Mike con I am founder and CEO of
[00:19] bright wfe uh we build a research agent
[00:22] that digests very large corpuses of
[00:24] content in the financial domain so you
[00:27] can think of due diligence in a
[00:29] competitive of deal process you are
[00:31] pre-term sheet you step into a data room
[00:33] with thousands of pages of content uh
[00:35] you need to get to conviction quickly
[00:37] ahead of uh other teams you need to spot
[00:40] uh critical risk factors that would
[00:42] would diminish asset performance um it's
[00:45] a fairly non-trivial task um you think
[00:47] about mutual fund analysts its earning
[00:50] season you've got a universal coverage
[00:52] of 80 120 names there are calls
[00:55] transcripts filings it's um a fairly
[00:58] non-trivial problem to understand uh at
[01:01] a sector level but also at the
[01:02] individual uh ticker level what's what's
[01:05] happening in the market um or goodness
[01:08] you get into confirmatory diligence and
[01:10] you've got 8 80 800 vendor contracts and
[01:14] you need to spot uh early termination
[01:16] Clauses you need to understand
[01:17] thematically how is my entire portfolio
[01:20] uh negotiating their vendor contracts
[01:21] it's um frankly not a human level
[01:24] intelligence task and the reality as
[01:28] we've stepped into this space um is that
[01:32] these uh these professionals uh just get
[01:34] put in a meat grinder Junior analysts
[01:37] are um tasked to do The Impossible on
[01:40] extremely tight deadlines um I come from
[01:43] a a technical background um prior to
[01:45] Bright Way VI was a data bricks and
[01:47] create a language model called Dolly uh
[01:49] that was one of the earlier models to
[01:51] demonstrate the power of instruction
[01:53] tuning um for eliciting uh instruction
[01:56] following behavior from from open source
[01:58] Technologies and um
[02:01] as I have met with these professionals I
[02:03] have developed a deep sense of empathy
[02:04] for um the stakes and the human cost of
[02:09] doing this work uh
[02:11] manually when it comes to the role of
[02:14] the individual in uh finance workflows
[02:17] and financial research um we think of
[02:19] the parallels to early early
[02:22] spreadsheets you go to an accountant or
[02:25] Finance professional 1978 before the
[02:27] Advent of computational spreadsheets you
[02:29] say what's your job
[02:30] well I run the numbers it's cognitively
[02:32] demanding these people write this stuff
[02:34] out by hand on literally wide pieces of
[02:36] paper called spreadsheets it's
[02:37] cognitively demanding it's important to
[02:39] the business and it's time intensive it
[02:40] feels like real work and now nobody
[02:44] wants that job and it's not because
[02:47] there aren't Finance professionals it's
[02:48] not because nobody's doing analysis it's
[02:50] the sophistication of the thought that
[02:52] you can bring to bear on the problem has
[02:54] increased so substantially because there
[02:56] are tools that allow us to think more
[02:58] effectively more efficiently
[03:01] what we're seeing what we're hearing
[03:03] from our customers is that a system like
[03:05] brightweb that is able to D and not just
[03:08] bright wave these this class of
[03:10] knowledge agents is able to digest
[03:13] volumes of content and perform
[03:14] meaningful work that accelerates by
[03:16] orders of magnitude um the efficiency
[03:20] and also uh time to to value in these
[03:23] markets and so the purpose of this talk
[03:26] is to relate um sort of the intelligence
[03:31] that we've developed uh in in the course
[03:33] of building this High Fidelity research
[03:35] agent um and just things that we're
[03:36] seeing both technically but also in
[03:38] terms of product affordances I mean the
[03:40] the design problem that you have to
[03:42] solve is how do you reveal the thought
[03:44] process of something that's considered
[03:46] 10,000 pages of content to a human in a
[03:49] way that's useful and legible that is
[03:52] not a uiux problem it's not a product
[03:54] architecture problem that existed three
[03:57] years ago and the final form factor has
[04:01] not been determined chat everybody's
[04:02] very Target fixated on chat um that's
[04:05] probably not
[04:07] enough so the the first thing that I'll
[04:10] observe is that non- reasoning models
[04:12] are performing greedy local search so
[04:14] the the Bloomberg talk highlighted that
[04:16] sort of fidelity issue like a really
[04:17] concrete example you put a reuter's
[04:18] article in 40 and you ask it to extract
[04:21] all the organizations goodness if it's
[04:23] not going to give you products and if
[04:24] you have a 10 5% error rate and you
[04:27] chain calls like that you're going to
[04:29] introduce um sort of in an exponential
[04:32] way uh the likelihood of of error being
[04:34] in these models and so the the winning
[04:36] systems will perform end to end RL over
[04:39] tool use calls where the results of the
[04:42] API call are in fact part of the RL um
[04:46] sequence of decisions so that you can
[04:47] make locally suboptimal decisions in
[04:48] order to get globally optimal outputs um
[04:52] the reality is that that's still an open
[04:53] research problem you know how do I Avail
[04:55] myself of a knowledge graph
[04:58] or I did not do
[05:02] that
[05:04] um how do you Avail yourself of these
[05:06] tools in an intelligent way um so that
[05:08] you get globally optimal outputs it does
[05:10] seem like that that is not a solved
[05:11] question so the reality and I think it's
[05:14] like heartening to see um this is a
[05:16] theme and I think everybody in this room
[05:17] can be sort of comforted by this you got
[05:21] you got to build a product today and
[05:22] like you're you're there's going to be
[05:23] this talk of the bitter lesson that more
[05:24] data more compute better models dominate
[05:27] all other approaches like nobody wants
[05:29] an expert system nobody nobody wants to
[05:31] use spy to do named enery recognition um
[05:35] the sorry um I was not in the speaker
[05:38] notes uh it you can think of being more
[05:41] circumspect about what is the scope of
[05:43] behaviors that the system the agent is
[05:45] going to engage in sort of like a
[05:46] regularization parameter which
[05:48] constrains the complexity of the model
[05:50] and that limits the likelihood reduces
[05:52] the likelihood that it will go truly off
[05:54] the rails and begin to produce uh
[05:56] degenerate output you can think of it
[05:58] sort of like a
[06:01] like multi- the most interesting
[06:02] interactions I've had with language
[06:03] models are deep into a conversational
[06:05] tree where you can think of selecting at
[06:08] each branch each response there a set of
[06:11] uh reactions that I can have to the
[06:13] model output and I'm steering I'm
[06:15] choosing this is what knowing how to use
[06:17] language models it's it's a skill um and
[06:20] many people who have real full-time jobs
[06:22] may not invest in developing that skill
[06:25] this is not dissimilar to what these RL
[06:27] systems are doing and if you can think
[06:29] of a multi- turn conversation as not
[06:33] just establishing a a human orchestrated
[06:36] Chain of Thought but really that set of
[06:38] tokens defines the activations of the
[06:40] model and if you think of the
[06:42] activations of the model as defining a
[06:44] program what you are doing when you
[06:46] respond to the model and say no not
[06:47] quite like that more like this is if you
[06:50] think of the the activation weights the
[06:54] activations as a point in a vector space
[06:57] you are nudging the activations to a
[07:00] place where they can finally solve the
[07:01] problem at hand and I think that's what
[07:02] the chain of thought process or the sort
[07:04] of reasoning monologue is performing
[07:07] it's it's getting the activations to a
[07:09] position where it can actually solve the
[07:10] problem so it's actually not I don't
[07:12] it's cute that it you can interpret it
[07:14] but I would prefer if it just got to the
[07:16] right set of activations automatically
[07:19] um and so from a product affordance
[07:22] standpoint people are not going to want
[07:24] to really become prompting experts in a
[07:26] deep way and and frankly it takes you
[07:28] know easily a th000 hours s um and so
[07:31] the scaffolding that products put in
[07:34] place in order to orchestrate these
[07:36] workflows and and shape and the the the
[07:39] behavior of these systems um I think had
[07:41] you know these verticalized product
[07:43] workflows are probably going to be
[07:44] enduring because they specify intent
[07:47] they take that weight off the user um so
[07:50] some of the things that we see with
[07:53] respect to archetypal design patterns
[07:55] and this speak consider a basic
[07:57] autonomous agent you
[08:00] really want to mimic the human
[08:02] decision-making process and decompose
[08:05] what is it that a person would do well
[08:06] if I need to understand how this uh poly
[08:09] polypropylene resin uh manufacturer um
[08:12] is is managing costs I might look for
[08:14] public market comparables and that would
[08:15] that would you know maybe entail going
[08:17] to the SEC filings or earnings C
[08:18] transcripts and I would assess content
[08:20] potentially from a Knowledge Graph
[08:21] constructed from uh previous deals that
[08:25] that you know I as as a private Equity
[08:27] investor have done um news purposes
[08:30] assess which which document sets are
[08:32] relevant to me distill down from those
[08:34] documents findings that substantiate um
[08:37] premises or hypotheses that I might have
[08:40] about this question or this investment
[08:41] thesis um and then enrich and error
[08:45] correct those findings and so a couple
[08:46] points on this one is that um it is
[08:49] actually so I forget who it was but they
[08:51] were talking about it was the Deep
[08:52] research team talking about um on that
[08:55] next step what are my intermediary notes
[08:58] what is it that I believed on the basis
[09:00] of what I found that's actually an
[09:01] extremely useful think out loud about
[09:04] what do we believe given the facts as
[09:06] they uh have materialized on that first
[09:09] pass through the the the data set um
[09:12] enriching individual findings that are
[09:14] distilled down from documents is an
[09:16] extremely powerful um design pattern
[09:19] likewise um it's it's you can ask these
[09:22] models you know is this accurate for
[09:24] that reuter's example you can say uh is
[09:26] this factually entailed by this document
[09:28] or is this is actually an organization
[09:31] um and the model can frequently
[09:33] self-correct and what we've noticed is
[09:35] that it is you can do that in the Json
[09:37] um as sort of like a Chain of Thought
[09:39] Behavior but it's ALS it's actually more
[09:41] powerful to do it as a secondary call
[09:42] because the model is kind of primed to
[09:45] be credulous says well you know I told
[09:47] you it was and so yeah I'm probably
[09:49] right um so it's interesting how you can
[09:51] tease apart some of these steps into
[09:53] multiple different uh calls and then
[09:55] through this process of synthesis you're
[09:57] able to weave together fact patterns
[09:58] across many many many documents into a
[10:01] coherent narrative um and that control
[10:04] Loop we think that obviously human
[10:06] oversight is extremely important um the
[10:09] ability to nudge the model um with
[10:13] directives or or sort of selecting this
[10:15] is an interesting thread I want you to
[10:17] pull that is extremely important and
[10:18] that's because the human analyst always
[10:20] is going to have access to information
[10:21] that has not been digitized that's that
[10:23] conversation with management that's uh
[10:25] your portfolio manager thinks this class
[10:28] of Biotech is is just hairbrained um
[10:31] that taste making I think is going to be
[10:33] where you see um the most powerful uh
[10:36] products
[10:37] lean I firmly believe with respect to
[10:39] the nodes in that Knowledge Graph and we
[10:42] probably many people in this room
[10:43] probably reached this this conclusion as
[10:45] well you still see this oh we got a
[10:46] portfolio manager agent this is the fact
[10:48] Checker and that sort of it needless
[10:51] like anthropomorphizing of these systems
[10:54] um it constrains your flexibility if the
[10:57] design needs of your compute graph
[10:58] change and this is this 197 I think it
[11:01] was 1978 you know the Unix philosophy
[11:03] it's like you think about piping and
[11:05] teeing on The Bash command line or I
[11:08] guess I date myself I still use bash not
[11:09] Z Shale um just simple tools that do one
[11:13] thing and that work together well and
[11:15] tex is the universal interface um it's
[11:17] 40 years ago 50 years ago geez um so our
[11:21] friends at Laton space put together this
[11:23] plot with respect to the structure of
[11:25] these graphs obviously that Paro
[11:27] Frontier which is the sort of efficiency
[11:29] Frontier it's two bat in a thousand a
[11:32] day um the efficiency Frontier for
[11:35] compute and performance trade off or
[11:37] Price performance trade-off um that
[11:39] Frontier is going to continue to move
[11:40] out but there will I believe there will
[11:42] for at least an enduring time be a
[11:44] frontier and what's notable about that
[11:45] is that you have to select then which
[11:48] tool which system which model am I going
[11:50] to use for each node in the compute
[11:52] graph and the reason that this is
[11:54] important is
[11:59] what I call the latency trap if you
[12:01] think about the plot of timed to value
[12:03] and realized value for agentic systems
[12:05] and I think this is extremely important
[12:08] it's very easy to think oh man it's
[12:09] going to do all of these things it's
[12:11] going to you know I'm going to check it
[12:12] and air correct and then you know in 25
[12:15] minutes it's going to be Banger and I
[12:17] think even with high quality products
[12:19] like opening eyes deep research
[12:22] it's you're not always sure that what
[12:24] you're going to get out is high quality
[12:26] so there's there's kind of like a
[12:27] question of like which side of the
[12:28] diagonal it's probably not a straight
[12:29] line but is that product on but also
[12:31] from a reps standpoint the impulse
[12:34] response for the user how well how well
[12:37] refined is you can think of like my
[12:39] expectation for what the report is going
[12:40] to look like and what the report
[12:41] actually looks like is the loss and the
[12:43] user's mental model is developing a
[12:46] sense for how do how do my prompts
[12:48] elicit behaviors from these models if
[12:49] it's a 8 Minute feedback loop it's a
[12:51] 20-minute feedback loop goodness you're
[12:53] not going to do many of those in the
[12:54] course of a day and your faculty with
[12:56] the system and the product is going to
[12:57] be low
[13:00] so synthesis is is really where a lot of
[13:03] the magic happens in these systems and
[13:06] um a couple observations so notice that
[13:10] it I don't know has anybody in this room
[13:12] ever had a 50,000 token response from
[13:14] any
[13:16] model no they say that's you know o1 is
[13:20] 100,000 context output context length um
[13:23] I'm not so sure and it's because the
[13:25] instruction tuning demonstrations these
[13:27] human generos synthetic or human
[13:29] generated outputs that are used to
[13:31] postra the models have a characteristic
[13:33] output length it's hard to write 50,000
[13:36] coherent uh novel words and so the
[13:40] likelihood that the models are able to
[13:42] produce I mean even um A1 still is about
[13:45] 2,000 3,000 tokens it's better than 40
[13:48] and so what happens it's kind of like a
[13:50] comp there's a compression problem if I
[13:52] have a very very large context window
[13:53] for input I'm compressing that
[13:55] information into a set of tokens and so
[13:58] it's the like the difference between
[13:59] writing a book report and a synopsis of
[14:02] each chapter you can you can be more
[14:05] focused and um specific about what is it
[14:08] that I want those ,000 tokens to be
[14:10] focused on um here we have uh you know I
[14:13] said right right a an analysis of the
[14:16] global financial crisis goodness if I
[14:18] don't think the rise of the Shadow
[14:20] banking system warrants more than three
[14:22] sentences and so if you if you can be
[14:24] more granular and more specific um you
[14:27] can get higher quality higher Fidelity
[14:28] more information dense outputs out of
[14:30] these systems by decomposing your
[14:32] researched instructions into multiple
[14:34] sub themes um Additionally the last
[14:38] point I'll make on this problem is that
[14:40] of uh the the presence of Rec
[14:43] combinative reasoning demonstrations in
[14:45] the instruction tuning and posttraining
[14:46] corpuses is low so it is uh easy to say
[14:50] here you know given the text of The
[14:52] Great Gatsby this is the epilogue and
[14:55] write a new epilogue for The Great
[14:56] Gatsby because the cost of internalizing
[14:58] that Corpus is fixed effectively you
[15:01] read the book and then you write five
[15:03] epilogues and it's like goodness I got
[15:05] it synthesis really is about weaving
[15:07] together disparate fact patterns from
[15:09] multiple documents think about the
[15:10] applications to biomedical literature
[15:12] synthesis I need to read all of these
[15:15] papers and then have something useful to
[15:17] say that actually brings together the
[15:19] facts from these documents now there's
[15:21] like a a cute trick you could try which
[15:24] is to say given the bibliography of Any
[15:26] Given paper write the abstract as an in
[15:28] as as a posttraining exercise but it's
[15:31] just really hard to get highquality
[15:34] intelligent thoughtful analysis of many
[15:36] many many different documents and so
[15:39] there are limitations in practice for uh
[15:43] even state-of-the-art models in terms of
[15:44] how they are able to manage complex real
[15:47] world situ situations uh factors like
[15:50] temporality um the perplexity of a well
[15:54] so temporality is hard um and being able
[15:57] to understand you know something like a
[15:59] merger and an acquisition um you know
[16:01] this these proforma financial statements
[16:03] are different from those that came um
[16:05] before the event um if there are
[16:07] addendums to contracts it's important to
[16:09] propagate with um evidentiary um
[16:14] passages a metadata that contextualizes
[16:17] why do I care about this what do we
[16:19] think about this document um what how
[16:22] should I consider this in relation to
[16:24] the other de uh pieces of evidence in in
[16:26] the in the context window though
[16:29] um so I'll now shift a little bit with
[16:32] some some examples from from our the
[16:35] product that we've built which is um how
[16:38] do you reveal the thought process of
[16:40] something that's considered 10,000 pages
[16:41] of text and I think that it is more like
[16:45] a surface and one where you're able to
[16:49] um it's it's kind of like this like
[16:52] people you may know the Facebook and
[16:54] Linkedin recommendation algorithm for
[16:56] for um
[16:59] connections uh feels uncanny good in
[17:02] part not because I mean the algorithms
[17:04] are okay not great um have gotten a lot
[17:07] better over time but in your visual
[17:11] cortex there is a a bundle of nerves
[17:13] that are uh exclusively dedicated to
[17:16] face recognition and the ability to say
[17:18] in a in a you know 6x6 grid of faces
[17:21] goodness I know that person and so you
[17:23] attend to the things that matter even if
[17:26] it's actually a low Precision product
[17:28] experience and so so the ability to give
[17:30] the person um details on demand is
[17:33] extremely important um we'll see so here
[17:37] we have a brightwave report um we you
[17:40] know I think the ability to click on a
[17:42] citation and then get additional context
[17:44] about this not just what document is it
[17:46] from but how should I be thinking about
[17:47] this what was the model thinking in the
[17:49] course of this um as well as structured
[17:52] interactive outputs that give you the
[17:54] ability to pull the thread and say well
[17:56] tell me tell me more about that Rising
[17:57] capex spend in bright wve um you can
[18:00] highlight any passage of text so it's
[18:03] not just the citations but you can
[18:04] highlight any passage of text and say
[18:06] tell me more what are the implications
[18:08] of this I think open AI gestures towards
[18:10] this with respect to Canvas and the
[18:11] ability to increase the reading level of
[18:14] of a passage having a continuous surface
[18:17] that's not just these citations um but
[18:19] in fact any uh finding should be
[18:24] interrog
[18:25] um likewise you can think of actually
[18:29] pause it's not going to pause I'm going
[18:31] to go back and do this again
[18:36] um you can think of the set of things
[18:38] that the model has discovered it reads
[18:40] all of these documents it develops a
[18:42] view it weaves the facts together um as
[18:45] a as a high dimensional data structure
[18:47] and the report is one view on that data
[18:49] structure it's kind of a low low effort
[18:51] point of entry into the the space of
[18:54] ideas you want to be able to turn over
[18:56] that Cube and see especially and finance
[19:00] um the receipts what's the audit Trail
[19:02] for this system that's read all of these
[19:04] materials and so being able to in this
[19:06] example click into the documents is one
[19:07] level but having all of the findings
[19:09] laid out for you whether it's a
[19:11] fundraising timeline um ongoing
[19:13] litigation I'm able to if something
[19:16] catches my attention click on it this is
[19:18] where that that investor hello investor
[19:22] analyst taste comes into play I'm able
[19:24] to say tell me more about that it's like
[19:26] a magnifying glass for text something
[19:28] catches my eye this patent litigation
[19:30] goodness that seems important um you had
[19:33] a factory fire in Mexico that wiped out
[19:35] you know critical single Source supplier
[19:38] um what are you going to do about that
[19:39] that ability to drill in and get
[19:41] additional details on demand is
[19:42] extremely important in these systems and
[19:44] I think candidly um we we do not yet
[19:47] have the final version the final form
[19:49] factor of this class of products um but
[19:52] it it's an extremely interesting design
[19:54] problem and I will say uh we are we are
[19:57] hiring so these QR codes not only is it
[20:00] a great place to work we've got uh
[20:02] people from Goldman Sachs and UBS and
[20:04] meta and Instagram and anaplan and we
[20:06] just hired a senior staff software
[20:08] engineer from Brave um goodness we got a
[20:10] stack team we also have a $10,000
[20:12] referral bonus so I'm going to see a lot
[20:14] more phones come out
[20:16] now um $10,000 referral bonus for all of
[20:19] these roles primarily the product
[20:21] designer and the front end engineer
[20:22] we're hiring staff and Senior staff
[20:24] level professionals we we have a small
[20:26] team of extremely experienced indiv ual
[20:29] um and this is structured like the DARPA
[20:32] red balloon challenge if you're familiar
[20:34] um so if you refer the person that
[20:36] refers the person that we hire you get a
[20:38] th000 bucks and so on and so on and so
[20:40] on all along that exponentially
[20:42] exploding uh referral tree so we're
[20:44] bright wave we build knowledge agents
[20:46] for finance workflows I appreciate your
[20:48] time today
[20:51] [Music]
