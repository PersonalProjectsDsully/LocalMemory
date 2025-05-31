---
type: youtube
title: Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt
author: AI Engineer
video_id: zM9RYqCcioM
video_url: https://www.youtube.com/watch?v=zM9RYqCcioM
thumbnail_url: https://img.youtube.com/vi/zM9RYqCcioM/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['AI cost management', 'GPT-4', 'agentic workflows', 'NLP challenges', 'AI deployment', 'prompt engineering', 'machine learning scaling', 'AI error handling', 'cloud AI', 'financial data processing']
entities: ['GPT-4', 'OpenAI', 'agentic workflow', 'unstructured data', 'prompt engineering', 'cost optimization', 'AI error handling', 'natural language processing (NLP)', 'cloud computing', 'financial expertise']
concepts: ['agentic workflows', 'cost management in AI', 'prompt engineering challenges', 'scaling AI solutions', 'AI model limitations', 'data extraction techniques', 'machine learning deployment', 'error mitigation strategies', 'NLP applications', 'AI infrastructure optimization']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with NLP techniques', 'Knowledge of cloud computing platforms']
related_topics: ['AI cost optimization', 'NLP model fine-tuning', 'Machine learning deployment', 'AI ethics and bias', 'Cloud-based AI solutions', 'Prompt engineering best practices', 'Scalable AI architectures', 'AI error detection methods']
authority_signals: ['we put our heads down hack together this agentic workflow using GPD 4 and as expected you know it worked really well', 'the value that we were getting out of gp4 was so immense', "we couldn't really optimize for caching because of the variability and responses"]
confidence_score: 0.8
---

# Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=zM9RYqCcioM)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai agents, machine learning, production deployment, data aggregation, open source models, model training, scaling ai  

## Summary

```markdown
# Summary of "Finetuning: 500m AI Agents in Production with 2 Engineers"

## Overview
Method, a company focused on data aggregation, scaled to 500 million AI agents using minimal engineering resources. They transitioned from manual data extraction processes to leveraging GPT-4 for parsing unstructured data. However, they faced significant challenges with cost, scalability, and prompt engineering, leading to iterative refinements in their AI workflow.

---

## Key Points
- **Problem**: Manual data extraction was inefficient, error-prone, and unsustainable for large-scale operations.
- **AI Adoption**: GPT-4 was adopted to automate unstructured data parsing, initially showing strong results in controlled environments.
- **Cost Challenges**: High API costs ($70k/month) and lack of caching optimization made scaling difficult.
- **Prompt Engineering**: GPT-4 required detailed, scenario-specific prompts, leading to complex, hard-to-maintain workflows.
- **Scalability Issues**: Latency and variability in responses limited concurrent processing, similar to human error but in a different form (AI errors).
- **Iterative Solutions**: The team shifted from GPT-4 to a more optimized, agentic workflow, focusing on cost, caching, and prompt versioning.

---

## Quotes
- *"This is the perfect thing for us... it was a godsend."*
- *"The bill had to come do and it was a lot so $70,000 for our first month in production."*
- *"We couldn’t scale concurrently... similar to human errors but in a different nature."*

---

## Actionable Insights
1. **Leverage AI for Unstructured Data**: Use advanced LLMs like GPT-4 for tasks requiring summarization or classification of unstructured data.
2. **Optimize Costs**: Prioritize caching and batch processing to reduce API costs.
3. **Prompt Versioning**: Implement version control for prompts to manage complexity and ensure consistency across use cases.
4. **Focus on Scalability**: Design workflows to handle variability and latency, avoiding over-reliance on single API calls.
5. **Hybrid Approaches**: Combine AI with human oversight to mitigate errors and improve reliability.

---
```

## Full Transcript

[00:00] [Music]
[00:17] hey everybody uh yep I'm Kyle Corbett
[00:19] from open pipe and I'm here with Mustafa
[00:20] Ali from method we're going to be
[00:22] talking about how method has scaled in
[00:25] production to over 500 million agents uh
[00:28] and basically all the the tricks they
[00:29] use to make that actually work so a
[00:31] little bit about method is that we
[00:33] essentially collect and centralize
[00:35] liability data from across hundreds of
[00:37] different data sources this includes
[00:39] tapping into the credit bureaus uh
[00:41] connecting with the card networks like
[00:42] visa and MasterCard um and just direct
[00:44] connections with the financial
[00:45] institutions and various other third
[00:47] party sources and you know we uh sort of
[00:50] aggregate and enhance this data and
[00:52] serve it to our customers who are
[00:54] typically other fintechs Banks or
[00:56] lenders and they use this enhanced data
[00:58] to um anything really to do with debt
[01:01] management so refinancing loan
[01:03] consolidation liability payments or just
[01:05] Personal Finance Management
[01:08] um yeah and at open pipe what we do is
[01:11] we help you build uh train and deploy
[01:14] open source models um for actual usage
[01:17] we also let you use in production your
[01:19] signals you get from users from the
[01:21] environment to improve your model
[01:23] continuously over time and that's some
[01:24] of the things we'll be talking about uh
[01:26] what we did with method nice
[01:31] so one of the early challenges that we
[01:33] faced at method while coming up with
[01:35] this you know aggregation pipeline uh
[01:37] was that some of our customers basically
[01:39] came to us and said you know it's really
[01:41] nice that you can give us the balance
[01:42] and payment information on a specific
[01:44] liability for their end consumers but
[01:46] you know what would be really nice is if
[01:48] you could also give us some of these
[01:50] liability specific data points like the
[01:52] payoff amount on an auto loan or the
[01:54] escrow balance for a mortgage and you
[01:57] know we said okay let's do some research
[01:59] so we go back to to some of our data
[02:00] partners and basically ask them you know
[02:02] is there anything you know we can plug
[02:04] into to get these kinds of data points
[02:05] and what we found was there's really no
[02:07] Central API that we could get access to
[02:10] that would allow us to get some of these
[02:12] data points and of course ideally we
[02:14] would want to work with uh directly with
[02:15] the banks but you know having already
[02:17] worked with banks before and just from
[02:19] initial conversations we realized that
[02:21] it would easily take up to at least a
[02:22] couple of years before getting anything
[02:24] solid done and you know we we're an
[02:26] early stage company so we want to build
[02:27] for the customer fast um and so that's
[02:29] really what we're trying to come up with
[02:31] a solution that we can just you know uh
[02:33] push into production
[02:36] tomorrow and so just to get better
[02:38] understanding of how some of these
[02:40] companies are operating today uh the
[02:42] services that they're providing today
[02:43] how are they doing that in the first
[02:44] place right like they must be getting
[02:45] that data somehow so we go back to some
[02:48] of these customers and basically ask
[02:49] them you know how are you guys operating
[02:51] and what they tell us is is kind of
[02:53] interesting so a lot of these companies
[02:55] they basically hire offshore teams of
[02:57] contractors and you know they uh these
[03:00] teams are basically responsible for
[03:02] calling these Banks um on behalf of the
[03:05] company and the end consumer they
[03:06] authenticate with the banks gather the
[03:08] necessary information somebody has to
[03:10] proof check it it gets sent back um and
[03:12] then it gets integrated into the
[03:14] financial platforms um and it get surfac
[03:16] to the user is used for underwriting
[03:18] stuff like that and so that's the status
[03:21] quo that we're dealing with here and
[03:23] when you think about it that's a very
[03:24] inefficient manual process right it's
[03:27] it's when you try to think about scaling
[03:29] it does doesn't really scale it's a very
[03:31] um it has a lot of problems you know
[03:33] it's expensive because one person can
[03:35] only do one thing at a time right so if
[03:37] you want to scale uh you basically have
[03:39] to hire more people and for the same
[03:41] reason because it's so synchronous it's
[03:43] also really slow um and the main I guess
[03:46] the the biggest problem with that is
[03:48] also that it's there's a lot of human
[03:49] error involved and um you you need to
[03:51] hire a team to fact check it uh to proof
[03:54] check it and um it's the the the the
[03:58] worst thing that you can end up with is
[03:59] to surface basically inaccurate
[04:01] financial
[04:02] information and so conceptually though
[04:04] if you think about it it's kind of like
[04:05] an API right you have the request
[04:07] component you have the authentication
[04:09] component you have the response
[04:10] validation all that stuff uh so
[04:13] essentially when you drill this problem
[04:15] down into the core problem that's really
[04:17] just trying to make sense of um
[04:19] unstructured data right so if only there
[04:21] was this magic tool or software that we
[04:24] could use that was really good at
[04:26] parsing unstructured
[04:28] data and and you know lucky for us
[04:31] around the time that we were trying to
[04:32] solve this problem open aai announced
[04:35] gbd4 and you know as people like to call
[04:37] it there was this Cambrian explosion of
[04:39] AI or llm enabled applications all
[04:42] around us and the results were just
[04:44] mind-blowing um and we thought to
[04:46] ourselves you know this this this is the
[04:48] perfect thing for us this is like a
[04:49] godsend uh so we tried to like you know
[04:51] we tried to see if there's anything
[04:53] there that we could use and if there's
[04:54] one thing that we all know in this room
[04:56] is that advanced llms especially post
[04:58] gbd4 are really good with um with
[05:02] parsing unstructured data so tasks like
[05:04] summarization or classification they're
[05:07] really good with that kind of thing so
[05:08] we want to test that theory out and see
[05:10] what that can get
[05:13] us and so we put our heads down hack
[05:16] together this agentic workflow using GPD
[05:18] 4 and as expected you know it worked
[05:21] really well so we tried to like expand
[05:23] some of our use cases because you know
[05:25] the API costs are high so we wanted to
[05:27] get as much as we could from a single
[05:29] API call and you know it turned out to
[05:31] be really good at that so we tried to
[05:33] obviously this was in a very controlled
[05:35] manner um but this was in production and
[05:38] so we were testing out uh different uh
[05:40] extractions basically and um you know
[05:43] everything was going really good uh but
[05:45] as soon as we started to increase a
[05:47] little bit of uh traffic uh what we
[05:50] found was you know the bill had to come
[05:53] do and um it was a lot so $70,000 for
[05:57] our first month in production with gbd4
[06:00] and you know this was this made
[06:01] leadership really unhappy and you know
[06:03] but um but it was something it was
[06:05] something they were they were fine with
[06:07] because the value that we were getting
[06:08] out of gp4 was so immense um and so we
[06:11] actually kept this thing in production
[06:13] for at least a couple more months as we
[06:15] tried to work around this kind of cost
[06:17] problem and you know cost wasn't the
[06:20] only thing that we were concerned with
[06:21] um as we started to scale some of these
[06:23] use cases we quickly ran into a wall
[06:25] with prompt engineering it only takes
[06:27] you so far um one thing we realized that
[06:29] even though gbd is really smart it's not
[06:31] a financial expert so you had to give it
[06:34] really detailed instructions and
[06:35] examples uh to really make it work with
[06:38] all kinds of use cases that we were
[06:39] trying to Target um so it's hard to
[06:41] generalize those kinds of prompts they
[06:42] become really long convoluted it's
[06:44] always a cat and mouse Chase with you
[06:46] fix it for a certain scenario and it
[06:48] breaks for another one you fix it for
[06:49] that one it breaks for the previous one
[06:51] and so you're all this going back and
[06:52] forth we didn't have any prompt
[06:53] versioning so we had to figure out a
[06:55] better way to make this work for all of
[06:57] our use cases
[07:02] and so the tldr here is that you know we
[07:05] we didn't want to adopt that initial
[07:06] solution that I just talked about
[07:07] earlier in the slides because of its
[07:09] scaling challenges and just because it
[07:11] was so inefficient but we kind of ran
[07:13] into the same scaling challenges with
[07:15] GPT where it was expensive because we
[07:18] couldn't really optimize for caching
[07:20] because of the variability and responses
[07:22] and the prompt tweaks we were making all
[07:24] the time and the Baseline latency that
[07:26] we were finding was actually really slow
[07:28] so we couldn't you know it was overall
[07:29] we couldn't scale concurrently and
[07:32] similar to human errors that were kind
[07:34] of uh in a different nature we had AI
[07:36] errors which were just hallucinations
[07:38] that were hard to catch um and we just
[07:41] couldn't scale with this kind of system
[07:43] but we still kept it in production
[07:44] because for a specific use cases was
[07:46] actually really really
[07:48] good and so now the problem shifted from
[07:51] solving that core problem of trying to
[07:53] make sense of unstructured data that was
[07:55] solved with GPT now the problem shifted
[07:57] to how do we scale this system how do we
[07:59] build
[07:59] a robust uh you know agentic workflow
[08:02] that can handle this kind of volume
[08:04] reliably and so some of the ballpark
[08:07] figures that we came up with you know is
[08:09] that we we're going to be at least
[08:10] making 16 million requests per day uh
[08:12] we're going to have at least 100K
[08:14] concurrent load and you know we need
[08:16] minimal latency to um handle this kind
[08:19] of real-time agentic workflow so sub 200
[08:21] milliseconds and you know so the natural
[08:23] next step for us was like we thought to
[08:25] ourselves do we buy more gpus do we host
[08:27] our own model like what do we do at this
[08:29] point
[08:30] um so that at that point open pipe comes
[08:33] in yeah so about a year ago we started
[08:35] working with method on solving these
[08:37] issues that Mustafa just listed and we
[08:40] actually found that the those three
[08:42] issues he listed right which are quality
[08:44] cost um and latency are very common um
[08:47] these are things that you know across
[08:48] almost everyone we work with uh at least
[08:50] some subset of those are really top of
[08:52] mind um and so with uh method
[08:56] specifically we were working on okay how
[08:57] do we how do we solve those problems in
[08:59] a way that that makes this uh you know a
[09:01] viable business for you so uh the first
[09:04] thing we did was start measuring error
[09:05] rates um you know like like he mentioned
[09:08] uh even AI models are not perfect uh
[09:10] these are all probabilistic systems
[09:12] getting to a 0% error rate was not
[09:14] really feasible but we were able to see
[09:17] different models had different uh had
[09:18] different performance characteristics
[09:20] there so on Modern models on the task
[09:22] they're doing these are the rates we're
[09:24] seeing on gbd4 um we're at about an 11%
[09:26] error rate uh and with 03 mini it's much
[09:28] better it's a 4% error rate um the way
[09:32] you measure that is going to be specific
[09:33] to your business and that that's
[09:34] actually true to some extent for all
[09:36] three of these things we'll talk about
[09:38] uh in the case of method this is
[09:39] actually relatively easy to measure
[09:41] luckily because they have this agentic
[09:42] workflow but like ultimately what the
[09:44] agent is trying to do is is fill out um
[09:46] you know extract all this information he
[09:48] was talking about Bank balances things
[09:49] like that and so you can you can have a
[09:51] human go through the flow and figure out
[09:53] what the real number should be and then
[09:54] you can compare an agentic systems final
[09:57] outputs to that and see if it was
[09:58] successful or not
[09:59] um which which made this part relatively
[10:01] easy to calculate uh so these are kind
[10:03] of the error rates we're getting um on
[10:05] the latency point of view uh we see that
[10:08] gp40 is around a second uh to respond uh
[10:12] and then o03 mini takes about 5 seconds
[10:14] for their specific task again this is
[10:15] somewhat task dependent uh depending on
[10:17] how much you know for example O3 has to
[10:19] think as you're measuring this you also
[10:21] want to make sure that you're using real
[10:22] production conditions that you're
[10:23] actually doing um you know like a real
[10:25] diversity of tasks uh that that match
[10:27] what you're actually doing and at a
[10:28] reasonable and currency level that
[10:30] matches your production um and we also
[10:32] measured the cost um so again cost uh
[10:35] this is something that is going to
[10:36] obviously be specific and how much it
[10:38] matters is also very specific to your
[10:39] use case as well um interestingly 03
[10:42] mini even though it has a much lower per
[10:44] token cost than GPD 40 if you just look
[10:46] at like the pricing page on the API for
[10:49] their specific use case uh we found it
[10:50] was a little bit more expensive because
[10:52] it has it generates many more reasoning
[10:54] tokens so it has much longer outputs um
[10:56] again though this is somewhat Tas
[10:58] dependent so I just recommend
[11:00] um actually just just as an aside I
[11:02] would recommend once you get to the
[11:04] point that you're trying to optimize
[11:05] that you have sort of that initial proof
[11:06] of concept with with some model
[11:08] something that works I think it's really
[11:10] worthwhile to it can be as simple as
[11:12] like literally just writing like you
[11:13] know three different Python scripts that
[11:15] like are able to categorize each of
[11:16] these for a different model um and then
[11:18] as new models come out you'll be able to
[11:19] quickly tell how they're doing um okay
[11:23] once you've done or in this case once
[11:25] we've done this this sort of um
[11:27] benchmarking of where the models are
[11:29] next question is all right what is where
[11:31] do we need these models to be where do
[11:32] we need to get to um and so again this
[11:35] is very task dependent uh in the case of
[11:37] method uh they do have special like they
[11:40] have um extra checks that happen after
[11:42] this where they look and see okay are
[11:44] the numbers that came out plausible do
[11:45] they match you know the types of things
[11:46] we're seeing before all the all these
[11:47] different kinds of checks they're doing
[11:48] and so they didn't need to get all the
[11:50] way down to a 0% error rate but of
[11:52] course those checks are still followable
[11:53] and so um if it's over a certain point
[11:55] then then some fraction of those errors
[11:57] are going to get through and that's
[11:58] going to be bad so we found around a 9%
[12:00] error rate was was able to get them what
[12:01] they needed um from a latency point of
[12:04] view so the way their agent works is a
[12:06] realtime system uh it it needs to be
[12:09] able to respond quickly to to move uh
[12:11] through the the basically like through
[12:14] the whole flow to get the information it
[12:15] needs and so they did have a hard
[12:17] latency cut off um we see a wide variety
[12:19] in this for what it's worth we have some
[12:21] customers that I talked to who it's like
[12:22] hey if I get a result back at some point
[12:24] in the next few days like that's totally
[12:25] fine this is a background bash process
[12:27] um we have other customers who are doing
[12:28] real-time voice with the human on the
[12:30] other end of the line and it's like hey
[12:31] you know if I'm over 500 milliseconds
[12:33] that's not going to work for me and so
[12:35] again you just have to know for your
[12:36] specific case how much this matters same
[12:38] with cost um in their case because of
[12:40] that very high volume as mustaf was
[12:42] mentioning cost is pretty important to
[12:44] them um again depending on your use case
[12:46] usually mostly dependent on how high
[12:48] volume it is um will determine how much
[12:51] cost matters to you but but it's
[12:52] something you you you should know these
[12:53] numbers for your specific task as you're
[12:55] comparing different models okay so um
[12:59] we're looking here at this uh of course
[13:02] as you're looking at this this slide you
[13:03] can you may see there's a problem here
[13:05] which is um of the two models we're
[13:07] comparing at least none of them actually
[13:09] meet all three of the requirements we
[13:11] need to be able to deploy this in
[13:12] production and uh you know gbd4 on both
[13:16] the error rate as well as the cost we're
[13:18] not quite there um and then 03 mini uh
[13:21] on the cost but especially on the
[13:22] latency it's just not going to work for
[13:23] what we need so this is the point at
[13:26] which uh method came and they talked to
[13:28] us we're like hey we're not able to hit
[13:29] what we need here um because again we're
[13:33] not uh yeah we're these these models
[13:35] aren't getting us where we need to be so
[13:37] what we work on in open pipe is fine
[13:39] tuning we work on building custom models
[13:41] for your specific use case and so I'm
[13:43] going to talk about why you would want
[13:44] to do that and how that helps in this
[13:46] case um first I would say fine-tuning is
[13:48] a power tool uh it does take more time
[13:51] it takes more um engineering investment
[13:54] than just prompting a model uh so you
[13:56] don't really want to do that until you
[13:59] have actually benchmarked the production
[14:01] models just prompting them and seen
[14:03] whether they work or not um so in this
[14:04] case in meth's case and and in all of
[14:06] our customers cases uh they found that
[14:07] they were not able to hit the numbers
[14:09] they needed um and so that's the time
[14:10] you want to bring in fine
[14:12] tuning um so let's look at we were able
[14:15] to find tuna model and see uh how that
[14:17] was able to help uh because it can
[14:18] actually really bend that price
[14:20] performance curve a lot um so on the the
[14:24] error rate uh which is basically just
[14:25] the inverse of of accuracy if you want
[14:26] to measure it that way um we were able
[14:28] to get to a place where we were doing
[14:30] significantly better than GPD 4 and
[14:31] importantly better than that threshold
[14:33] they needed uh this used to actually be
[14:35] much harder to achieve it required a lot
[14:37] of manual uh labeling of data and things
[14:39] like that it's actually become much
[14:40] easier over time because of the
[14:42] existence of models like now o03 mini um
[14:45] which allows you to just use your
[14:47] production data you can you can use your
[14:50] uh basically the inputs you're using
[14:51] production you can uh generate outputs
[14:54] for them using a model like O3 mini and
[14:56] train on them we find like in this case
[14:58] that often you're not able to quite get
[15:00] uh to the the performance of the the
[15:02] teacher model the model o03 mini in this
[15:04] case that you're using but you can get
[15:06] quite close to it and usually do much
[15:07] better than you know uh a slightly less
[15:10] good but much much larger model um you
[15:12] know in this case uh the model we ended
[15:14] up deploying with them is just an 8
[15:15] billion parameter LL 3.1 model and and
[15:18] we find that actually for the majority
[15:19] of our customers a model that large or
[15:20] smaller is is good enough and is able to
[15:23] hit the numbers you need from quality um
[15:25] but uh yeah the important thing is to be
[15:27] able to Benchmark that and to answer
[15:28] that question for yourself
[15:30] um on the latency point of view because
[15:34] actually this this is sort of the magic
[15:35] of being able to move to that much
[15:36] smaller model because we've got this AP
[15:37] billion parameter model it is way easier
[15:40] to deploy in a low latency way um
[15:43] there's just many few fewer calculations
[15:45] for your sequential calculations with
[15:46] the number of layers and so you can get
[15:47] just a much lower latency you can even
[15:49] and we we didn't actually have to do
[15:50] this in method's case but something you
[15:51] can do is you can train this model you
[15:53] can deploy it within your own
[15:54] infrastructure collocate it with the
[15:55] application code that's using it um and
[15:58] even completely eliminate the the
[15:59] network
[16:00] latency uh and then finally uh on the
[16:02] cost front again just because this is
[16:04] such a smaller model um you end up with
[16:06] a much much lower cost uh and so that
[16:09] for many of our customers is a big is
[16:12] incredibly important is to be able to
[16:13] get that performance number you need um
[16:15] while still maintaining a relatively low
[16:17] cost um in in method's case we were
[16:20] actually able to far exceed the sort of
[16:21] cost thresholds that they were looking
[16:23] for to make this viable um which means
[16:25] that they don't have to worry about this
[16:26] from sort of a unit economics point of
[16:28] view uh in in in the way that they did
[16:30] when they were using the larger
[16:32] models um so just um to sort of
[16:36] reiterate what I started with before um
[16:39] this is a power tool uh the fine tuning
[16:41] uh is it does take a fair amount of work
[16:44] um not an extreme amount of work but
[16:45] significantly more work than you do for
[16:47] prompt
[16:48] engineering however if you're not able
[16:50] to get to the reliability numbers you
[16:52] need uh through just prompt engineering
[16:54] with the models that exist out there
[16:55] without tuning it is a viable way to
[16:58] very strong bend that price performance
[17:00] curve and get to a much better place uh
[17:03] which uh which which can help you get to
[17:04] a very large scale in production just
[17:06] like method
[17:09] did nice um so yeah just to wrap up here
[17:13] uh one thing that or at least a couple
[17:15] couple points that we want to highlight
[17:17] is that you know the reason we put two
[17:19] engineers in the title is also because
[17:21] it's not that it's not that complicated
[17:23] right you can get away with using we
[17:25] identified a specific use case and we
[17:28] got away with just using the cheapest
[17:29] model that was out there uh we
[17:30] fine-tuned it we already had the data
[17:32] from GPT in production so we already had
[17:34] the data we didn't have to go digging
[17:35] around for the data in the first place
[17:37] uh so we already used that and we used
[17:39] the cheapest model that gave us the
[17:40] fastest performance and you know you
[17:42] don't need to buy your own gpus um and
[17:46] the the other thing that we realize is
[17:47] that productionizing AI agents actually
[17:49] requires a little bit of uh some level
[17:51] of openness uh and patience from the
[17:53] engineering team from the leadership
[17:55] team is because when you write code
[17:57] we're all used to writing code that just
[17:58] work works you push out a feature and
[17:59] never breaks because you're not changing
[18:01] anything but with AI agents you it takes
[18:03] some time to get to a point where it's
[18:05] like production ready and actually gives
[18:07] you the responses that you're looking
[18:09] for um and you know I I feel compelled
[18:12] to say something about as to Mark the
[18:14] top of the traditional software
[18:15] engineering job so I'll leave you with
[18:16] these last few words if you're Inu pivot
[18:19] to
[18:21] AE thank you thanks everyone
[18:25] [Music]
