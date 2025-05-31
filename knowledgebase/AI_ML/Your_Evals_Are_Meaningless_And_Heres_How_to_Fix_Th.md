---
type: youtube
title: Your Evals Are Meaningless (And Here’s How to Fix Them)
author: AI Engineer
video_id: 3jwClx0Ft2E
video_url: https://www.youtube.com/watch?v=3jwClx0Ft2E
thumbnail_url: https://img.youtube.com/vi/3jwClx0Ft2E/mqdefault.jpg
date_added: 2025-05-26
category: AI Evaluation and Alignment
tags: ['AI evaluation', 'LM evaluators', 'human evaluation', 'model alignment', 'cost efficiency', 'scalability', 'dynamic systems', 'evaluation frameworks', 'machine learning', 'AI research']
entities: ['Anon', 'Mechanical Turk', 'LM evaluators', 'Hugging Face', 'Open AI', 'nlg eval', 'Spade', 'Anthropic']
concepts: ['LM evaluators', 'human evaluation', 'agent data set evaluators', 'alignment', 'scalability', 'cost reduction', 'consistency', 'dynamic system', 'evaluation methods', 'model providers']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of machine learning', 'familiarity with AI evaluation methods', 'knowledge of model training processes']
related_topics: ['AI evaluation', 'machine learning', 'model alignment', 'cost efficiency', 'scalability', 'human vs. automated evaluation', 'dynamic systems', 'evaluation frameworks']
authority_signals: ['research backing this is substantial there are papers like nlg eval and Spade that showed really strong correlations between human judgments and llm scores', "we've seen costs roughly in the $3 to 120 range depending on what model you choose"]
confidence_score: 0.85
---

# Your Evals Are Meaningless (And Here’s How to Fix Them)

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=3jwClx0Ft2E)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai evaluation, machine learning testing, model validation, ai engineering, evaluation frameworks, ml systems, ai testing  

## Summary

# Summary of "Your Evals Are Meaningless (And Here’s How to Fix Them)"

## Overview  
The video critiques the limitations of traditional AI evaluation methods and highlights the potential of Large Model (LM) evaluators to improve speed, cost, and scalability. The speaker, a co-founder of Honeyhive, emphasizes that evaluations must evolve dynamically with AI systems and stresses the importance of representative datasets and hybrid evaluation approaches.

---

## Key Points  
- **Three Core Components of Evaluations**:  
  1. **Agent**: The AI system being evaluated.  
  2. **Dataset**: Must be representative and evolve as the system improves.  
  3. **Evaluators**: Include human, LM (Large Model), and hybrid approaches.  

- **Shortcomings of Traditional Methods**:  
  - Human evaluators are slow (8–10 hours for 1,000 test cases) and expensive ($3–120 vs. $100+ for platforms like Mechanical Turk).  
  - Inconsistent human judgments (e.g., 80% consistency with LM evaluators, similar to human-to-human agreement).  

- **Rise of LM Evaluators**:  
  - **Benefits**: Faster (under 1 hour for 1,000 test cases), cheaper (10x cost reduction), and scalable.  
  - **Research Backing**: Papers like *NLG Eval* and *Spade* show strong correlations between LM scores and human judgments. Major providers (e.g., OpenAI, Anthropic) are adopting LM-based alignment.  

- **Dynamic Evaluation Needs**:  
  - Evaluations must adapt as the AI system improves, requiring updated datasets and evaluators.  

- **Uncomfortable Truths**:  
  - LM evaluators are not infallible; they require domain expertise for dataset design and may lack nuance in complex scenarios.  

---

## Important Quotes/Insights  
- *"Evaluations are not just about accuracy but about real-world performance."*  
- *"LM evaluators offer 80% consistency with human judgments, which is comparable to human-to-human agreement."*  
- *"The research backing LM evaluators is substantial, but they are not a silver bullet."*  

---

## Actionable Recommendations  
1. **Build Representative Datasets**: Involve domain experts to ensure test sets reflect real-world scenarios.  
2. **Leverage LM Evaluators Strategically**: Use them for speed and cost but validate results with human oversight.  
3. **Adapt Dynamically**: Continuously update datasets and evaluators as AI systems evolve.  
4. **Hybrid Approaches**: Combine human and LM evaluators to balance nuance and scalability.  

--- 

This summary highlights the need for robust, adaptive evaluation frameworks to ensure AI systems perform effectively in real-world contexts.

## Full Transcript

[00:03] hey everyone really excited to present
[00:05] today at the AI engineering
[00:07] Summit uh before we dive into the topic
[00:10] of LM evaluations let me set the stage
[00:13] for what we're going to be covering uh
[00:15] why your evals might be meaningless and
[00:17] more importantly how can we fix them now
[00:21] some of you might be thinking my EVS are
[00:24] fine we've got a robust testing
[00:26] framework and you know what I have the
[00:29] exact same thoughts when I was building
[00:31] the ml systems platform at templified
[00:33] but after working with hundreds of teams
[00:36] I've seen patterns emerge that
[00:38] completely change how I think about
[00:40] evaluation so let me tell you why this
[00:43] matters though first of all a bit about
[00:46] me and why I'm obsessing over this
[00:48] problem I co-founded honeyhive in late
[00:51] 2022 to build evaluation tooling for AI
[00:55] Engineers before that I was leading the
[00:57] data and ml platform team at temp of
[01:00] a series D Enterprise
[01:02] startup but then something really
[01:04] interesting happened at honeyhive we
[01:08] started working with teams across the
[01:10] entire spectrum of AI we talking
[01:12] hundreds of teams from two person
[01:14] startups to Fortune one 100
[01:16] Enterprises and the use cases they
[01:19] really span from everything you can
[01:20] imagine multi-agent systems text to
[01:23] sequel rack so on and so
[01:26] forth and across all these different
[01:29] teams we we kept seeing the same
[01:31] problems with evaluation coming up again
[01:33] and again problems that standard testing
[01:36] Frameworks just weren't equipped to
[01:38] handle today I'm going to show what
[01:40] we've learned we'll look at traditional
[01:43] evaluation approaches why exactly they
[01:45] fall short and more importantly what can
[01:47] you do about it right because here's the
[01:50] thing like getting your evaluation right
[01:52] isn't just about catching bugs measuring
[01:54] accuracy Etc I think it's really just
[01:57] about building AI systems that actually
[01:59] deliver our in the real world and
[02:01] they're not just fancy
[02:03] demos so let's start with the
[02:06] fundamentals right what exactly is an
[02:09] evaluation the fundamental State back to
[02:11] unit integration testing in traditional
[02:14] software just like you wouldn't want to
[02:17] push changes to production without any
[02:19] tests in traditional software you
[02:21] wouldn't want to push changes to your AI
[02:22] application without any EV abouts and
[02:25] what's really funny is like when I talk
[02:28] to teams and ask them about their
[02:29] evaluation strategy I often get
[02:32] responses like oh yeah we test things
[02:35] before production or we have some
[02:36] automated test setup but when we dig
[02:39] deeper there's really a lot of
[02:42] uncertainty about what makes a good
[02:44] evaluation framework so let's just break
[02:46] it this down piece by piece right to
[02:49] test quality before production we need
[02:52] three key components first we need an
[02:55] agent here this is basically whatever
[02:59] you are evaluating it could be an end to
[03:01] an agent it could be a small function
[03:03] within an agent it could be just your
[03:05] retrieval pipeline so on and so forth
[03:08] now an agent itself could be many things
[03:10] it could be customer service chatot
[03:12] you've built maybe it's a Q&A agent that
[03:14] is passing through legal contracts and
[03:16] so on and so forth each of these has its
[03:19] own unique requirements challenges and
[03:22] such like for instance if you're
[03:24] building a document Q&A system it needs
[03:27] to not just be accurate but it also
[03:29] needs to be compliant with regulations
[03:32] let's say if it's Financial Q&A you want
[03:34] to be able to explain its reasoning it
[03:36] needs to have some level of nuance
[03:38] around financial accounting standards
[03:40] and so on so forth your evaluation needs
[03:43] to account for all these different
[03:45] aspects second component in this sort of
[03:48] piece of evals is a data set and it's
[03:51] the most important in my opinion really
[03:53] this is what you're evaluating against
[03:56] this is where I see a lot of teams
[03:57] stumble they'll show me a couple of test
[03:59] cases maybe they built spy queries all
[04:02] handwritten by their developers and they
[04:04] say oh well yeah this covers all our use
[04:07] cases right but does it really I don't
[04:10] think so your data set really needs to
[04:12] include both your inputs the kinds of
[04:15] queries and requests your system will
[04:16] actually receive in production and the
[04:19] ideal outputs what good responses your
[04:22] ideal responses should look like and
[04:24] these need to cover not just the happy
[04:26] path but also the tricky edge cases
[04:29] where things might actually go wrong and
[04:32] these are the sort of examples that
[04:34] really need to be written by domain
[04:35] experts people who understand the
[04:38] necessary business context to be able to
[04:40] judge quality and really just Define
[04:43] what should be the requirements for this
[04:45] agent what exactly is the contract that
[04:46] we building here third this is really
[04:50] crucial right we need
[04:52] evaluators this is essentially how
[04:55] exactly are you measuring quality now
[04:57] traditionally this meant you evaluators
[05:00] You' have subject matter experts
[05:02] reviewing outputs scoring them providing
[05:05] feedback this kind of works but it's
[05:07] very slow and expensive then you have
[05:09] go-based evaluators great for subjective
[05:12] things like response time latency could
[05:14] even be metrics like roach L which don't
[05:17] really work but that's a whole another
[05:19] story and a talking in of itself and now
[05:21] we have LM evaluators which promise to
[05:24] combine The Best of Both Worlds right
[05:26] you have Nuance reasoning with uh that
[05:29] can really understand humans and the
[05:31] human nuance and context Behind these
[05:34] applications with the speed and
[05:35] scalability of automated systems so when
[05:38] you sort of break it down into three
[05:40] components really it's agent data set
[05:42] evaluators you can start asking the
[05:44] right questions what aspects of your
[05:47] system does really matter how
[05:49] representative is your test set are your
[05:52] evaluation methods really measuring what
[05:55] you think they're measuring right and
[05:57] here's the thing these components are on
[06:00] static in nature they need to evolve
[06:02] over time as your agent improves your
[06:04] data set might need to include more
[06:06] challenges Cas challenging cases as your
[06:08] evaluation criteria becomes more
[06:10] sophisticated you might need different
[06:12] kinds of evaluators it's a very dynamic
[06:16] system now let's talk a little bit about
[06:19] why LM evaluators have become so popular
[06:22] and I really mean popular right I'm
[06:24] seeing teams who are switching their
[06:26] entire evaluation stack to rely upon LM
[06:29] as a
[06:31] judge the main promise here is really
[06:34] compelling they're cheaper faster and
[06:36] more scalable than human evaluation but
[06:39] why does this actually matter and what
[06:41] does this mean in practice first off
[06:43] it's speed we seeing evaluations that
[06:46] used to take roughly about 8 to 10 hours
[06:48] with human evaluators they can now be
[06:50] completed in under an hour so imagine
[06:54] thousand test cases that you're
[06:55] processing with human evals like
[06:58] something like Mechanical Turk it might
[07:00] take roughly about a full day of work so
[07:02] you're talking about eight hours right
[07:04] with something like an LM evaluator it
[07:07] could be about 50 to 60 Minutes assuming
[07:09] you're executing these eval sequentially
[07:11] and not paralyzing them that's just an
[07:14] incremental Improvement right it's it's
[07:16] a huge Improvement cost is another
[07:19] Factor now just to thr some real numbers
[07:21] here uh a traditional human eval through
[07:24] Mechanical Turk you're looking at
[07:26] several hundred for about thousand
[07:28] ratings LM evaluators we've seen costs
[07:31] roughly in the $3 to120 range depending
[07:34] on what model you choose now that's a
[07:36] 10x reduction in cost huge Roi and
[07:40] here's where things get really
[07:41] interesting it's the consistency we are
[07:45] seeing over 80% consistency with human
[07:47] judgments and I know some of you are
[07:49] thinking okay it's only 80% but here's
[07:52] the thing right when we measure
[07:55] agreement between different human
[07:57] evaluators we often see Sim response
[08:00] rates and similar levels of consistency
[08:03] humans don't necessarily agree with each
[08:04] other 100% of the time either and we see
[08:07] that with LM as a judge as well the
[08:09] research backing this is substantial
[08:12] there are papers like nlg eval and Spade
[08:14] that showed really strong correlations
[08:16] between human judgments and llm scores
[08:20] and major model providers like open AI
[08:22] anthropic are increasingly pursuing this
[08:25] direction for alignment as well now all
[08:29] of this sounds amazing right it's almost
[08:31] too good to be true hold that thought
[08:33] for a sec because this this is where
[08:35] things really get very
[08:37] interesting I think the most
[08:40] uncomfortable truth that we need to face
[08:42] is that Elm evaluators have two very
[08:46] major problems right I think the first
[08:49] one is what I consider criteria drift
[08:51] it's a very sneaky one if you're using a
[08:54] popular framewor like let's say fragas
[08:56] prom Fu Lang chain you're like ly
[08:59] relying on their built-in evaluation
[09:01] criteria and it seems pretty reasonable
[09:03] right these tools are very established
[09:06] they have hundreds of thousands about
[09:08] millions of downloads but here's the
[09:10] thing their evaluation criteria is
[09:13] designed for
[09:14] generalizability it doesn't necessarily
[09:16] measure what's important to your unique
[09:18] use case so here's a very real world
[09:21] example that that I have personally face
[09:24] working with a customer we started with
[09:26] a working with a company uh an AI
[09:29] startup building an LM based
[09:31] recommendation system for e-commerce
[09:33] websites their evaluat was checking
[09:36] things like all the standard boxes
[09:38] context relevance on the retrieval side
[09:40] uh on relevance on the generation side
[09:43] of things and things really look great
[09:46] in testing right but when they push this
[09:48] to production that's where things
[09:50] started breaking there were a lot of
[09:52] user
[09:53] complaints the evaluator just completely
[09:56] missed the users's requirements for
[09:58] relevance they evaluator index too hard
[10:00] on keyword relevance without really
[10:03] thinking about the larger context of
[10:05] what the product description means how
[10:07] is it relevant to the user query so on
[10:10] so forth and as a result The evals
[10:12] couldn't really catch any real relevance
[10:15] issues right and I've also seen uh the
[10:19] grading of uh the these evaluators where
[10:22] it might work fine on just a single test
[10:25] case then it stops grading the user
[10:27] query on the same test case
[10:30] uh consistently because you know they
[10:32] were using maybe an llm that the
[10:35] underlying model just changed they
[10:37] weren't using a stable version of open
[10:38] AI so this is what we consider criteria
[10:41] drift essentially when your evaluator's
[10:44] notion of what is good no longer aligns
[10:47] with the user's notion of good sh
[10:50] Shanker and team at Berkeley they
[10:52] published this paper called eval genen
[10:54] which really explosed this concept in
[10:56] depth they found that evaluation
[10:58] criteria basically needs to evolve over
[11:00] time and the main challenge is how you
[11:03] balance true positives with false
[11:05] positives and basically maximize your F1
[11:08] score when you're measuring alignment
[11:10] against human
[11:11] judgments so this is a huge problem but
[11:14] there's another one
[11:16] here this is the what I like to call
[11:19] data set drift this is essentially your
[11:21] data sets basically lack test coverage
[11:23] right so picture this you spent weeks
[11:27] creating the perfect test cases clear
[11:29] queres obvious right answers and wrong
[11:32] answers your test Suite is golden right
[11:36] and then you launch in beta and then
[11:38] real world users start using your system
[11:41] and then suddenly they type way context
[11:43] dependent messy inputs and your
[11:46] beautiful test cases that you spent so
[11:48] hard writing they just don't hold up
[11:50] they don't represent reality anymore
[11:53] this is a usage pattern that we see
[11:55] everywhere users are constantly asking
[11:57] about topics way broader than you
[11:59] natural test cases users sometimes ask
[12:02] data that requires you to use real world
[12:04] user queries like let's say Ser API
[12:07] results sometimes user ask and combine
[12:10] multiple questions in ways you didn't
[12:12] really anticipate so this is what really
[12:15] makes you know data sets particularly
[12:18] dangerous uh your metrics might still
[12:20] look good your evaluator is happily
[12:22] scoring on these test cases uh it's like
[12:26] practicing for a marathon right and
[12:28] you're sort of running on the treadmill
[12:31] you might think you're getting really
[12:32] good at it but that's where another the
[12:34] race happens you're ultimately not
[12:36] accounting for things like incline
[12:38] surface traction and whatnot like your
[12:40] test cases no longer just represent what
[12:42] the reality actually looks like and so
[12:46] how do we go about this right uh how do
[12:49] we fix these problems and how do we
[12:50] actually make ebots work for
[12:53] ourselves the very simple Insight that
[12:56] changed everything for us is this
[12:59] evaluators and data sets they need to be
[13:01] iteratively aligned pretty much like how
[13:04] you align your actual llm
[13:06] application so here's a three-step
[13:08] approach that I found that I really want
[13:10] to break down and this has worked for a
[13:12] lot of our customers and folks like
[13:14] hamis and online have also written
[13:16] extensively about this but really first
[13:19] off you need to align your evaluators
[13:22] with dom main experts this is crucial
[13:25] have your experts regularly grade
[13:27] outputs not just one steering setup but
[13:30] continuously have them critique the
[13:32] evaluator results itself what is it
[13:35] missing what is it
[13:36] overemphasizing use the critiques of
[13:38] feot examples in your evaluator prompt
[13:40] and further ground your evaluator with a
[13:42] real world notion of what's good what's
[13:44] bad right there's a lot of massaging and
[13:47] iteration that just needs to be done on
[13:49] the evaluator prompt itself so don't
[13:51] just go ahead and rely on a templated
[13:53] library of metrics but look at the
[13:55] underlying prompt actually iterate upon
[13:57] it see if you agree with the outputs
[14:00] yourself and keep that process going
[14:03] until there's some level of agreement
[14:05] that feels
[14:06] satisfactory second really keep your
[14:09] data sets aligned with you real world
[14:11] user queries right it all starts by
[14:13] logging really your test Bank it needs
[14:16] to be living breathing thing right when
[14:19] you see underperforming queries in prod
[14:22] automatically flow them back into test
[14:23] Suite you can do this manually or you
[14:25] can set up automations using the various
[14:27] llm obstacles that are out there third
[14:31] this is where most teams really drop the
[14:33] ball measure and track alignment over
[14:35] time use conrete metrics like F1 score
[14:39] for binary judgments or correlation
[14:41] coefficients for liard scales track how
[14:44] well your evaluator matches human
[14:47] judgment with every iteration this will
[14:50] really inform you whether your evaluator
[14:51] is truly improving over time or are you
[14:53] regressing over time so on so forth and
[14:56] it's a lot of work it sounds like a lot
[14:58] of work
[14:59] here's the thing right it's far less
[15:01] work than dealing with the consequences
[15:03] of a meaningless eal that doesn't really
[15:05] tell you anything and doesn't measure
[15:07] anything
[15:09] meaningful in practice the most
[15:11] important step I personally found is to
[15:14] actually customize the LM evaluator
[15:16] prompt I think a lot of teams today are
[15:18] relying on these templated metrics that
[15:20] are rather meaningless you want to
[15:22] carefully T your evaluation criteria add
[15:25] few shot examples of critiques provided
[15:27] by domain experts
[15:29] pay attention to whether you're actually
[15:31] using binary skilles or lard skills for
[15:33] Ratings highly recommend binary by the
[15:35] way and make sure you're measuring
[15:38] something which is actually meaningful
[15:40] instead of just relying on out of the
[15:41] box metrics that you know don't really
[15:44] measure what's important to your use
[15:46] case your application your business
[15:50] context next you want to involve domain
[15:53] experts as early as possible and get
[15:56] them to evaluate the evaluator doing
[15:59] this in spreadsheets is a really good
[16:00] start you can start with even like 20
[16:02] examples and it will give you a good
[16:03] sense of whether evaluated judgments are
[16:05] actually in line with your demain
[16:07] experts or not this will also help
[16:09] inform what changes you should make next
[16:11] as you're improving your evaluator
[16:14] prompt putting this all together in
[16:17] practice really I'd recommend to start
[16:19] with logging like as hamis and really
[16:22] likes to say just read your logs right
[16:26] every time your system underperforms in
[16:28] production that's an opportunity to
[16:30] improve your test Bank these are real
[16:32] world failures that are just golden
[16:35] because these are the exact kinds of
[16:37] problems that your application needs to
[16:38] be improving upon they show exactly
[16:41] where your evaluation system is falling
[16:43] short and you should continuously add
[16:45] these test cases to your test bank and
[16:47] add the ground TR data sets as well uh
[16:50] ground TR labels so you can continuously
[16:52] improve your test Bank over time next
[16:55] iteration your LM evaluator promts they
[16:58] they aren't sacred texts right they need
[17:01] to evolve over time test new versions
[17:04] against your expanding test Bank make
[17:06] them more specific to your use case
[17:08] invest in an eval console sort of tool
[17:10] build this internally if you have to
[17:12] just to allow domain experts themselves
[17:14] to iterate on the evaluator prompt and
[17:16] get a sense of whether they agree with
[17:19] the evaluator critiques and judgments or
[17:21] not finally
[17:23] measurement you can't really improve
[17:26] what you don't measure so tracking your
[17:28] alignments go over time is extremely
[17:30] important we recommend setting up a
[17:32] simple dashboard to to track your
[17:34] alignment score it could be F1 if you
[17:36] using simple binary judgments it could
[17:39] be correlation metrics if you're using
[17:41] lyer scales really this will just allow
[17:44] you to track in a more systematic manner
[17:47] as you're improving your evaluator
[17:49] template whether it's improving over
[17:50] time or not very similar to how you
[17:52] might be testing your own original
[17:54] prompt for your LM application as well
[17:57] right and remember remember the goal
[18:00] here isn't perfection it's continuous
[18:02] Improvement and here's what I want you
[18:04] to take away from this talk ultimately
[18:07] your LM evals are really only as good as
[18:10] the alignment with real world usage so
[18:13] please don't fall into the Trap of
[18:14] static evaluation don't treat tests like
[18:17] static tests in traditional software
[18:20] llms don't work that way don't just set
[18:22] it and forget it right build these
[18:24] iterative feedback loops into your
[18:26] development process the payoff is huge
[18:28] especially when you're trying to improve
[18:29] your eval over
[18:31] time yep that's it thank you for all
[18:34] your time feel free to connect with me
[18:36] on LinkedIn if you want to discuss this
[18:38] more in depth and if you're looking for
[18:40] tools to implement this workflow inside
[18:42] your team uh check out our platform
[18:44] honeyhive at honeyhive doai thank you
