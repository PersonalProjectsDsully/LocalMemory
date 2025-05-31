---
type: youtube
title: Optimizing LLMs in Insurance with DSPy: Jeronim Morina
author: Channel Video
video_id: IAdZxqjZ45U
video_url: https://www.youtube.com/watch?v=IAdZxqjZ45U
thumbnail_url: https://img.youtube.com/vi/IAdZxqjZ45U/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['AI', 'prompt engineering', 'system design', 'NLP', 'machine learning', 'tool evaluation', 'error handling', 'first principles', 'structured data', 'domain experts', 'model sensitivity', 'AI development']
entities: ['Jason Lou', 'Hil Hussein', 'secure GPT', 'Chain of Thought', 'zero shot learning', 'length chain guard rails', 'dpy instructor', 'MITM proxy', 'JSON', 'domain experts']
concepts: ['prompt engineering', 'first principles thinking', 'error handling', 'deterministic outputs', 'structured data', 'problem-solving', 'tool evaluation', 'system fragility', 'domain expertise', 'model sensitivity']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML models', 'Familiarity with prompt engineering', 'System design fundamentals']
related_topics: ['Natural Language Processing', 'AI ethics', 'Machine learning systems', 'Tool evaluation frameworks', 'Error handling in AI', 'Data structuring techniques', 'Domain-specific AI development', 'Model optimization strategies']
authority_signals: ['I highly recommend this amazing blog post from Hil Hussein', 'we came up with a dozen of examples immediately started prompting our internal secure GPT', 'the idea is just to use mitm proxy and to really inspect like what are all these tools used']
confidence_score: 0.8
---

# Optimizing LLMs in Insurance with DSPy: Jeronim Morina

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=IAdZxqjZ45U)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llms, dspy, insurance, ai-engineering, optimization, machine-learning, system-design  

## Summary

# Summary of "Optimizing LLMs in Insurance with DSPy: Jeronim Morina"

## Overview  
Jeronim Morina discusses strategies for optimizing large language models (LLMs) in the insurance sector, emphasizing the shift from manual prompt engineering to system-level design. The talk highlights challenges in deploying LLMs for real-world tasks, such as customer-facing chatbots, and introduces **DSPy** as a framework to improve structure, safety, and determinism in LLM outputs.

---

## Key Points  
1. **First Principles Thinking**  
   - Move beyond "black-box" tools by inspecting how prompts and templates are constructed.  
   - Avoid relying on tools without understanding their underlying mechanisms (e.g., using MITM proxy to analyze tool behavior).  

2. **Real-World Problem Solving**  
   - Focus on domain-specific challenges (e.g., simplifying complex insurance terms) rather than toy datasets.  
   - Collaborate with domain experts to craft clear examples and define problems precisely.  

3. **Structured Outputs**  
   - Use techniques like JSON formatting, Chain of Thought, and guardrails to ensure deterministic, safe, and structured LLM outputs.  
   - Highlight the limitations of traditional prompt engineering (e.g., sensitivity to minor changes).  

4. **DSPy as a Framework**  
   - Introduce **DSPy** (Dynamic Structured Prompting with Python) to optimize LLMs for arbitrary metrics, improve resilience, and reduce fragility in system design.  
   - Emphasize the need for transparency in tooling and avoiding "magic" solutions.  

5. **Insurance Use Case**  
   - Example: Building a chatbot to explain opaque insurance terms.  
   - Challenges included prompt sensitivity, over-complex error handling, and the need for production-ready solutions.  

6. **Collaborations and Tools**  
   - Mention partnerships with OP Ai and Mistal AI for secure, optimized LLM deployment.  
   - Recommend resources like Hil Hussein’s blog post *“Please Show Me the Prompt”* for tool transparency.  

---

## Key Insights  
- **AI engineers are “bad”** because they often prioritize quick fixes over deep problem-solving.  
- **Prompt engineering is “black magic”**—tools like DSPy and structured techniques are critical for reliability.  
- **Transparency and domain expertise** are essential for deploying LLMs in high-stakes environments like insurance.  

---

## Actionable Takeaways  
1. **Inspect tools** (e.g., MITM proxy) to understand their prompt templates and behavior.  
2. **Prioritize first principles** over off-the-shelf solutions.  
3. **Collaborate with domain experts** to define clear, real-world problems.  
4. **Adopt DSPy** for structured, deterministic, and optimized LLM workflows.  
5. **Avoid over-reliance on complex error handling**; focus on robust system design.  

--- 

## Resources  
- Blog post: *"Please Show Me the Prompt"* by Hil Hussein (for tool transparency).  
- DSPy framework: Dynamic Structured Prompting with Python.

## Full Transcript

[00:00] [Music]
[00:13] welcome to uh optimizing LMS with this
[00:16] pie Beyond manual tuning and um I hate
[00:20] to break it to you but we all bad AI
[00:25] Engineers yes you
[00:28] are so why why why is that um because we
[00:33] don't care enough about solving Rebo
[00:35] problems um it's that we all of keep
[00:37] tinkering around with tools and hotbot
[00:40] QA data sets but let bear with me
[00:43] there's a way out so let's start with
[00:46] first principles thinking again and
[00:48] reminding ourselves what we are we are
[00:51] Engineers you know we have to reconsider
[00:54] the thing we are doing these these days
[00:56] which is like prompt engineering and
[00:58] start programming is systems again I
[01:01] mean maybe you have seen this already
[01:03] like left we have this huge neuron
[01:05] Network model but usually neuron Network
[01:08] on themselves and being like language
[01:10] models or any other AI model are not
[01:12] useful on their own but are only useful
[01:15] if you considering them uh in an Huger
[01:18] system so the struggle is real when it
[01:21] comes to use cases in the LM space we
[01:24] all thrilled by the excitement around
[01:26] capabilities of ever new models but you
[01:29] have only idea of what we really want to
[01:32] achieve we throw a bunch of tools of
[01:34] them at the not well- defined problems
[01:35] we write some handwritten prompts use
[01:37] some prompt libraries and the hope that
[01:40] that will lead us to a magical solution
[01:41] of our problems I know myself how much I
[01:44] love to Tinker around with all these
[01:46] tools and see how they work but here I'm
[01:49] telling you to stop hoping that using
[01:51] API just works and solves all your
[01:54] problem so let's imagine you're an AI
[01:58] engineer and you your day by Brewing
[02:01] some specialty coffee sitting down
[02:02] delving into Focus mode and you fiddle
[02:05] around with a bunch of prompts and try
[02:07] the next tool to guide system output to
[02:10] for Jason so you evaluate the system
[02:12] with your most love metric the answers
[02:15] are all like looks good to me at 10 so I
[02:18] have just look at all of the outputs and
[02:20] they was like yeah that's fine enough I
[02:23] can I can do this but this is really the
[02:26] end and uh is it really that we've
[02:29] fiddle around with our prompts until
[02:31] they seem stable enough so the question
[02:33] is how do we become like great AI
[02:35] Engineers again I think we should stop
[02:38] start uh stop working on toy problems
[02:41] all these hotot QA data sets and
[02:43] everything and start working on real
[02:46] problems again so why am I telling you
[02:50] this so a company dude like me is going
[02:53] to explain you how to solve reward
[02:54] problems I mean yes uh we have to we
[02:58] have to solve reward problems s every
[03:00] day because we can and it's really about
[03:03] the data and helping our customers every
[03:05] day so we are data different company
[03:08] since like ever we don't have any assets
[03:10] I mean insurance is what they are they
[03:12] are selling you a good feeling you'll
[03:14] give us money and uh we give you money
[03:16] back in case something happens to you uh
[03:19] so there's no real asset but we always
[03:21] have been a data data focused um company
[03:25] and only providing non-touch assets so
[03:30] to to keep to keep with the Ia so one of
[03:34] the huge problems we're facing today is
[03:35] climate change and with that the ever
[03:38] increasing like incoming uh claims for
[03:42] example and more problems we are seeing
[03:44] with our customers so there's a huge
[03:46] rise of um of Labor we have to do and so
[03:52] that's a reason why AXA Germany started
[03:54] the data Innovation lab in 2017 and we
[03:57] are like a group of machine learning
[03:58] Engineers working with the data
[04:00] scientist of the business units and we
[04:03] are trying like to work cross
[04:05] collaboratively with the business units
[04:07] to to really make an impact on the
[04:10] customer service agents to help them
[04:12] make the customers happy every day so I
[04:15] know you think you you are like in a
[04:17] Silicon Valley and uh you're like these
[04:20] amazing speedboats you're like super
[04:22] fast you can change your ideas quickly
[04:24] every day and we like rather tankers and
[04:27] in a way you're right so we are these
[04:30] tankers but more like ice breakers often
[04:32] so it's like slowly but we are like
[04:35] making progress forward and um like
[04:38] pushing things forward and you can see
[04:40] this also in uh things that just made
[04:43] the announcement on Monday so in the
[04:45] Forefront already in 2023 in the
[04:47] beginning of the year we started
[04:48] collaborating with OP Ai and created
[04:50] this secure GPT geni platform internally
[04:54] uh which is hosted on Azure platform and
[04:57] even now we are now like announcing uh
[04:59] on day that we're working together with
[05:00] mistal AI so our internal gen platform
[05:04] gets like more usable every day and like
[05:07] especially not comprising our data
[05:10] security or anything our customers don't
[05:12] want to so that's super cool so that's
[05:16] the reason like the tanker uh has some
[05:19] impact and uh makes fun
[05:22] but what does it what does it take us to
[05:26] to get bad good Engineers so
[05:30] H how do we make this path um better so
[05:34] let's me let take me let me take you on
[05:36] a path on imaginary reward problem
[05:37] insurance so we're creating a customer
[05:40] facing chatbot to help them navigate our
[05:43] intr transparent terms and conditions so
[05:45] how would we tackle this I mean yeah we
[05:48] kind of have like everything but the
[05:51] main issue is like you really need to
[05:54] Define your problem really clearly so we
[05:58] went to The Domain experts and let us
[06:00] guide through the problem space
[06:01] especially crafting examples and this is
[06:03] especially true important for prompt
[06:05] engineering which are either super
[06:07] simple or like super hard to solve so we
[06:10] can understand the the domain space
[06:13] better and um that guided us to to learn
[06:17] a lot about what is expected in our
[06:20] production system the end so we came up
[06:22] with a dozen of examples immediately
[06:23] started prompting our internal secure
[06:25] GPT and um we we tried to up with some
[06:30] useful prompts but prompt engineering is
[06:33] like quite of black magic so who didn't
[06:35] use phrases like if you don't output
[06:37] Jason I'm going to quit or please please
[06:40] please output Jason and uh there are
[06:44] these prompts where you fiddle around
[06:46] you try to make your output better
[06:48] cleaner more structured and um one one
[06:53] way uh to do this is what Jason Lou
[06:56] already proposed last year um was to to
[06:59] high The Prompt and like say okay I'm an
[07:01] assistant here and we start the prompt
[07:05] by just giving in triple back ticks and
[07:07] Json and that then the model uh push
[07:11] forward into uh just creating Json but
[07:16] there are also other a dozen other of
[07:18] prompting techniques like Chain of
[07:19] Thought zero f shot learning uh tools
[07:22] like length chain guard rails dpy
[07:26] instructor and to help make use of these
[07:30] techniques um to make the output safer
[07:34] more deterministic more structured more
[07:37] resilient and optimized for maybe even
[07:40] arbitrary metrics and so we we filled
[07:43] around with all these tools and played
[07:45] around and to be honest that was a lot
[07:47] of work like finding a good prompt is
[07:49] hard and error prone as these prompt
[07:51] templates are often hardcoded and the
[07:54] usage is quite
[07:55] intransparent so please don't fall into
[07:59] the these tools will solve the problem
[08:01] for me trap so get your hands dirty
[08:03] inspect what these tools are really
[08:05] doing for you and I highly recommend um
[08:09] this amazing blog post from Hil Hussein
[08:13] so which is called uh please show me The
[08:17] Prompt it has another title but bear
[08:19] with me so um the idea is just to use
[08:24] mitm proxy and to really inspect like
[08:27] what are all these tools used I've been
[08:30] mentioning before what are they really
[08:32] sending so this is about first principes
[08:35] thinking I'm not advocating here to to
[08:37] use tools this and that and there and I
[08:40] will talk definitely about dspi
[08:43] but please do first principles thinking
[08:48] look at what these tools create what
[08:51] what kind of prompt templates they use
[08:53] what what they send to you LMS don't
[08:56] just believe that it will happen or it
[08:59] will do do something
[09:00] great so one issue we had been
[09:03] experiencing a lot was sensitivity to
[09:05] minor prompt changes so like very small
[09:08] prom changes led to very high problems
[09:11] in the end so what we what we had was
[09:14] what we tried to do was using chaining
[09:16] libraries to to fix these issues and
[09:19] throwing more and more error handling
[09:20] code at that so um we tried to make this
[09:25] a bit more achievable and but this lead
[09:30] led into the end to an overly complex
[09:32] and fragile system so we had the gut
[09:34] feeling that was by no means something
[09:36] we want to put in production but we
[09:39] could show that the task was at least
[09:41] achievable um or could serve as a
[09:44] baseline so before continuing further we
[09:46] knew we were missing some key pieces to
[09:48] fully understand what's happening and uh
[09:51] apart from inspecting our CS that was we
[09:54] were not logging any traces or something
[09:56] um for that we started using an open
[09:59] source Library called arise Phoenix and
[10:02] that definitely helped a lot um in
[10:05] understanding like which calls are Buel
[10:07] together which helped to see
[10:11] what what what is doing what is
[10:13] happening behind the
[10:16] curtains so and again here once again
[10:20] I'm advocating
[10:22] for first principle thinking you cannot
[10:26] improve anything which you don't measure
[10:28] and we we were still at that point in
[10:30] time we were still at the level looks
[10:32] good to me at 10 right which was our
[10:34] main driver so we need to definitely
[10:36] write some basic evaluations so
[10:39] preparing the data to match so if you
[10:43] want to evaluate something you need not
[10:44] only have your input data but also to
[10:46] have some labels and that was the hard
[10:48] part to be honest that took us some
[10:50] several months to really get scrape the
[10:52] production data we were already getting
[10:55] and uh looking at it and preparing it so
[10:57] we had like clean input output Pairs and
[11:00] one main thing is please don't stumble
[11:02] upon this data leakage is still a thing
[11:05] so it doesn't matter if you have like
[11:06] the coolest apis if you're using data
[11:10] which is has compromised data leakage in
[11:12] it and you already can deduce the output
[11:17] label from your input data that's really
[11:21] bad so if you creating your your
[11:25] evaluation data sets really really
[11:28] really pay attention to uh to not um to
[11:33] not
[11:35] uh destroy your evaluation
[11:40] so there's another blog post I would
[11:42] definitely recommend from Ham Hussein
[11:45] which is evals called evals is all you
[11:48] need or evals for your um for your uh
[11:52] llms please get into that that is
[11:55] amazing and will so much help you so
[11:58] feeling quite confident so this is the
[12:00] base setting and I encourage you please
[12:02] don't do anything with DSP or any other
[12:04] tools when you don't have like this base
[12:07] setting when you don't understand your
[12:09] data when you don't have enough examples
[12:11] because
[12:13] otherwise like what you you just saying
[12:15] prompt in DSP profit so what what's
[12:18] what's the case please please don't do
[12:20] this and to to be fair I I just went
[12:24] into DSP because I met Omar last year at
[12:27] scaleta Bay in uh in November and I was
[12:30] like okay cool so we are now giving this
[12:32] a chance
[12:34] but please bear with me this has a steep
[12:38] learning curve so I'm I love the idea of
[12:42] DSP I love how how it enabled us
[12:47] to now we have this overly complex
[12:49] system with this huge prompts and huge
[12:51] error handling code and everything and
[12:53] we all thought okay we're going to throw
[12:56] DSP it and it's going to be super easy
[12:58] but to be honest uh the the learning
[13:01] curve is quite Steep and it's maybe a
[13:03] bit too much overall so this is not a
[13:06] 100% recommendation go to dpy but uh
[13:10] please give it a try if you
[13:12] can okay
[13:14] so without dpy we had to break down our
[13:18] problems into step we have to prompt
[13:20] well like each step had to work well in
[13:22] isolation we had to tweak the steps to
[13:24] work together we had to generate
[13:27] examples to tunage step and to use these
[13:29] examples to maybe even fine-tune some
[13:32] smaller models and what we now could do
[13:36] with dpy was taking these base idea and
[13:38] you need to do that I encourage you
[13:42] please tow apart your problem into
[13:46] separate modules and we're talking about
[13:49] modules in a second um otherwise you
[13:52] won't be able to take advantage of DSP
[13:54] and also DSP is not going to take to be
[13:57] able to take advantage
[13:59] of your uh of your DSP program because
[14:03] it doesn't get any hints any any signal
[14:06] on how to improve uh the program you're
[14:09] providing it so don't come up with one
[14:12] huge uh react when we did this and is
[14:15] bad uh but rather split try to
[14:18] understand um how your flow of your
[14:21] program is like do you do you have a
[14:22] retriever step first U do you have uh do
[14:26] you want to have like multihop question
[14:29] answering do you want
[14:31] to bring together different pieces and
[14:34] answer them in one question at the end
[14:36] this this is really
[14:37] important
[14:39] so what do you do you have to separate
[14:42] your program into modules which are kind
[14:45] like the prompts and weights you have to
[14:47] add optimizers to tune your prompts and
[14:49] weights giving a metric and for us the
[14:52] metric was quite clear um for the
[14:54] chatbot we needed to find like the right
[14:57] answer and DSP compiles the same program
[15:01] them into different instructions fusure
[15:04] prompting and fine-tuning so instead of
[15:05] prompting one language model with a huge
[15:07] prompt as I told you uh please break it
[15:11] apart so there's this analogy to neuron
[15:14] networks for maybe for you to better
[15:16] understand how DSP Works um we have the
[15:19] separation into init and and forward
[15:21] step where you define in you init um how
[15:26] like in a in know this um
[15:30] how you find like a convolution or
[15:32] Dropout layers in pytorch you use then
[15:35] things like Chain of Thought or react
[15:37] and uh you describe in your forward path
[15:40] how you do the things you want to do
[15:43] like retrieving and other
[15:46] stuff okay so what were the key
[15:50] learnings um so if you want to do this
[15:54] for like German text answer exact match
[15:56] answer passage match only work for
[15:59] English text so metrics are really not
[16:01] working out of the box we have you have
[16:03] to come up with your own metrics you
[16:04] have to create your own metric um if you
[16:07] want to use um something like react so
[16:10] there's nothing like a typed react so we
[16:14] the Spy comes with these typed um typed
[16:18] things like type predictor um or type
[16:21] Chain of Thought but if you want to have
[16:23] something more specific for your case
[16:25] you need uh you need to come up with
[16:28] your own module and improve that and EV
[16:32] evaluation is also quite fixed on
[16:34] English language to be honest and in
[16:36] case you want to use D Pi for German
[16:38] optimization you need also to create
[16:40] like your own evaluators especially for
[16:42] the exact and passage
[16:45] match okay so we tried to come up with
[16:48] one big model and we found out like this
[16:51] is really not not
[16:55] working okay whoops sorry
[17:07] okay so what are your key takeaways uh
[17:08] you should definitely write prompts by
[17:10] hand and start with that otherwise uh
[17:13] you cannot say if your task is
[17:15] achievable at all uh you can't approve
[17:17] what you don't measure avoid metrics
[17:19] like looks good to me1 without any
[17:21] annotated data or clear goal metric
[17:24] there's no clear objective to validate
[17:25] if the results are getting even better
[17:28] you definitely should write basic
[17:30] evaluations start with some small
[17:32] evaluations like regx or string
[17:34] comparisons and then only then use
[17:36] techniques like LMS judge please don't
[17:39] over complicate things it's already
[17:42] super complicated and just make very
[17:47] very small
[17:49] adjustments so okay um what do you take
[17:54] home from this um so am I really
[17:57] thinking that you've learned learned how
[17:59] to use dpy like from a 20 minutes
[18:01] corporate T guide talk if yes cool
[18:04] you're amazing wow uh but to be honest
[18:08] um if you want to learn dsy go to all
[18:10] these learning resources from Conor
[18:12] shorton from the dsy website that itself
[18:16] um there are all these people like
[18:19] presenting it in a lot better fashion
[18:21] than I did but what what I wanted to do
[18:25] is like I wanted to spark some interest
[18:27] in you the same spark like I got when I
[18:30] when I saw this conference last year
[18:32] where I learned all the people uh where
[18:34] I learned all the guys who created these
[18:36] toolings
[18:38] and I want to spark that same curiosity
[18:41] in you and to see if you can get like a
[18:44] better AI Engineers by using not only
[18:48] the tools but also first principles
[18:50] thinking and I think we are meant to
[18:53] become like great AI Engineers so this
[18:55] conference is about you getting inspired
[18:57] get out and find like some good problems
[18:59] where you can try this out and which I
[19:02] would like wor solving with AI that
[19:03] wasn't possible before
[19:08] [Applause]
[19:13] [Music]
