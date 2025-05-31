---
type: youtube
title: Lessons from the Trenches: Building LLM Evals That Work IRL: Aparna Dhinkaran
author: Channel Video
video_id: nbZzSC5A6hs
video_url: https://www.youtube.com/watch?v=nbZzSC5A6hs
thumbnail_url: https://img.youtube.com/vi/nbZzSC5A6hs/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: []
entities: ['Phoenix', 'product details function', 'product search function', 'promos function', 'discounts function', 'traces', 'application', 'function calls']
concepts: ['function call evaluation', 'trace analysis', 'application debugging', 'open-source tools', 'LLM application workflows', 'error detection', 'system tracing', 'parameter extraction']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Understanding of application tracing', 'Basic knowledge of function calls', 'Familiarity with debugging techniques']
related_topics: ['LLM application development', 'Function call optimization', 'System error analysis', 'Open-source tool evaluation', 'Application flow debugging', 'Trace visualization techniques', 'AI system monitoring', 'Parameter validation']
authority_signals: ['Phoenix is our open source Source product', 'you can go look at and see okay it says it got the function call wrong...']
confidence_score: 0.8
---

# Lessons from the Trenches: Building LLM Evals That Work IRL: Aparna Dhinkaran

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=nbZzSC5A6hs)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llm evaluations, ai evaluation, machine learning, model testing, ai metrics, real world, llm benchmarks  

## Summary

```markdown
# Summary of "Building LLM Evaluations That Work in the Real World" by Aparna Dhinkaran

## Overview
Aparna Dhinkaran from Arise discusses the practical challenges of implementing **LLM evaluations** in real-world applications. While many focus on theoretical metrics (e.g., MMLU), she emphasizes the importance of **task-based evaluations** that measure how well systems perform in complex, real scenarios. Using an e-commerce chat-to-purchase example, she highlights the critical role of **router evaluations** (ensuring correct function calls) and the need for tools like Phoenix for observability and debugging.

---

## Key Points
1. **Model vs. Task Evaluations**:
   - **Model evaluations** (e.g., MMLU) focus on benchmarking LLMs.
   - **Task evaluations** assess how well systems perform in real workflows (e.g., user intent classification, function call accuracy).

2. **Real-World Complexity**:
   - Applications like chat-to-purchase systems involve multiple layers (e.g., router, component-level evaluations).
   - A single error in the **router function call** (e.g., misclassifying user intent) can cascade, invalidating the entire execution branch.

3. **LLM as a Judge**:
   - LLMs can evaluate system outputs, but their judgments require **explanations** to identify root causes of failures.
   - Example: A user asking about "current promotions" might trigger a "product search" function instead of a dedicated "promos" function, leading to incorrect results.

4. **Tools for Observability**:
   - **Phoenix** (open-source tool) enables tracing application workflows, identifying where errors occur, and providing explanations for misclassifications.

---

## Key Quotes/Insights
- *"Evals are all you need" is a buzzphrase, but what does it mean in practice? It means evaluating at every layer of the system."*
- *"If the router gets the function call wrong, the entire execution branch is off. That’s why tracing and explanations matter."*
- *"Correct parameters matter more than the right function call. Even the best function fails without the right inputs."*

---

## Actionable Takeaways
1. **Prioritize Router Evaluations**: Ensure user intent is correctly mapped to the right function calls.
2. **Use Open-Source Tools**: Leverage tools like Phoenix for tracing and debugging workflows.
3. **Focus on Explanations**: When evaluations fail, get granular insights into where and why the system went wrong.
4. **Validate Parameters**: Double-check that function calls receive the correct parameters, even if the function itself is accurate.
5. **Monitor End-to-End Traces**: Track user queries through the entire application flow to identify bottlenecks.

---
```

## Full Transcript

[00:00] [Music]
[00:14] all right hey everyone my name is aparta
[00:15] one of the founders of arise uh we do
[00:18] llm evals and observability um I wanted
[00:22] to do a session going really deep on
[00:23] this stuff because you guys all hear LM
[00:26] as a judge and you're probably like yeah
[00:28] yeah yeah but how does actually work in
[00:30] the real world well we work with some of
[00:32] the top companies in the space um who
[00:35] are all deploying llm applications and
[00:39] we've seen a lot go well and not go well
[00:41] in the real world and so even though
[00:44] you've probably seen this tweet from
[00:45] Greg a bunch evals are all you need
[00:48] you're probably like what does that
[00:49] actually mean when you're putting it in
[00:51] the real world and I'm going to
[00:53] demystify a little bit of that and talk
[00:55] about some real examples today so first
[00:57] off there's a distinction between types
[00:59] of EV valves that we should we should
[01:02] just clarify first is there's model EV
[01:04] vales if you're on hugging face you're
[01:06] looking at the open llm leaderboard and
[01:08] you're like okay llama 3B whatever 7B is
[01:12] better than this because of some MML U
[01:14] metric well they're actually stacking
[01:16] and ranking different models against
[01:18] each other and these are really helpful
[01:20] um when you see things like the needle
[01:22] and the hay stack test um to understand
[01:24] which model to actually use but for most
[01:27] of you in the room who are probably
[01:28] building the applic
[01:30] you probably care more about task EV
[01:32] vals and what I mean by that is is the
[01:34] llm application actually working and how
[01:37] do you define evals that actually help
[01:40] you figure that out so let's talk about
[01:42] how task evals work in the real world
[01:45] this is probably review to most of you
[01:47] most of the industry is converging
[01:49] around a couple different options LM as
[01:50] a judge user feedback heuristic based
[01:53] approaches just as a overview for folks
[01:56] who don't know what llm as a judge is
[01:58] it's basically when you're using AI to
[02:00] evaluate AI I take inputs from I take
[02:03] the output of my response I might take
[02:05] the context that it was given pass it
[02:07] into an eval prompt template and then I
[02:10] can actually have llm as a judge come
[02:12] back with an evaluation of how it works
[02:15] let's talk about how this works in a
[02:16] simple application so this is a really
[02:18] common one we're seeing in the ecosystem
[02:21] uh it's a chat to purchase type of
[02:22] application eCommerce applications use
[02:25] this a lot so the way it begins is the
[02:29] customer ask ask some kind of question
[02:31] hey blah blah blah I'm looking for a new
[02:33] Kindle and there's first this component
[02:36] call it like a router that actually is
[02:39] deciding what the customer intent is a
[02:41] lot of folks actually use function
[02:42] calling for this and so there's a
[02:44] function call that happens it determines
[02:47] what the path to send a user down is and
[02:50] then there's the actual workflow
[02:52] execution branch of what to happen this
[02:54] is a really really simple one in the
[02:57] real world the applications get a lot
[02:59] lot more complex there a real I see
[03:03] probably a couple of these you know
[03:04] every week we basically the user intent
[03:08] gets decided by an llm call and then it
[03:11] has to get the user intent correct this
[03:14] is what they all care about because
[03:15] otherwise it sends users down the wrong
[03:17] path it can send it down if user asking
[03:19] you a question about hey recommend me
[03:22] some product to go buy but then it sends
[03:24] me down something related to customer
[03:25] support well the issue actually you want
[03:28] to catch is did it get the function call
[03:31] of determining that user intent
[03:33] correctly and so when you look at an
[03:35] application like this where there's a
[03:37] router and routers are you know probably
[03:39] the most common agentic type of
[03:40] workflows we're actually seeing in
[03:42] production today there's a router call
[03:45] then there's llm calls then there's
[03:47] application calls and then there's maybe
[03:49] even calls to traditional ml models
[03:52] doing in the middle of where you're
[03:54] actually calling out to search how many
[03:55] you guys have an application that looks
[03:57] like this or have seen you know have
[03:59] built bu one internally okay awesome
[04:01] awesome awesome this is this is kind of
[04:05] where we're seeing a lot of um we're
[04:09] seeing a lot of applications being built
[04:11] it's not just a simple API call and and
[04:14] here's a response it's actually built on
[04:17] top of levels and so as your
[04:19] applications get more complex your evals
[04:22] are going to get more
[04:23] complex and there's levels to this is is
[04:27] kind of the theme you'll hear today if
[04:29] you're evaluating something like this
[04:31] you want evals at different levels of
[04:33] your application there's an eval most
[04:36] importantly at the router level to help
[04:38] you figure out what's the path that it
[04:41] should go down did it go down the right
[04:44] execution branch and then within each
[04:46] execution Branch there's often component
[04:49] level evals that are being
[04:52] done I'm going to actually give you guys
[04:54] a demo so we can show your real
[04:56] application and we can show you where
[04:57] something goes wrong but just to set
[04:59] some context you will actually dive
[05:01] really deep today into this router eval
[05:04] in applications um the key thing I think
[05:08] to take away is you'll see questions
[05:10] like this from the demo we're going to
[05:12] give but users ask you know questions in
[05:15] the applications and typically you want
[05:17] to figure out well did it go down the
[05:19] right function call so in this case did
[05:21] it go down something like the user asked
[05:23] about details of a product did it go
[05:25] down the product details function call
[05:28] and then there's another kind of
[05:29] implicit one that's often done which is
[05:32] did we extract the right parameters for
[05:34] the function call and do we give it the
[05:36] right parameters because if you don't
[05:38] give it the right parameters then it
[05:40] doesn't matter if you pick the right
[05:41] function call it's still not going to
[05:42] get it right so these are kind of the
[05:45] two ones I'm going to actually walk
[05:46] through and show you guys um what it
[05:49] looks like um let me make it big screen
[05:54] give me one second okay uh I'm going to
[05:57] actually show you guys Phoenix today
[05:58] Phoenix is our open source Source
[05:59] product you guys are welcome to try it
[06:02] out and download it uh this is actually
[06:04] Phoenix live for my application that I
[06:06] was talking about and right now what
[06:09] you're actually looking at is a trace of
[06:12] the application very simplified trace of
[06:14] the application um this is what a user
[06:17] asked me could you tell me if there is
[06:21] any current promotions for Samsung
[06:24] whatever phone and then this is actually
[06:27] the output that was responded from the
[06:30] application within this um and you can
[06:33] go and you can look through kind of all
[06:34] the different applications here all the
[06:37] different kind of questions that users
[06:38] are asking and you can actually see what
[06:42] what kind of questions that users are
[06:43] asking here each one of these you'll
[06:45] actually see a full stack Trace what's
[06:47] most important here and you kind of see
[06:49] the one I clicked on is one where it
[06:50] actually says it got the function call
[06:52] wrong so I'm going to actually go dive
[06:55] into that one and we can go look at it
[06:58] you can go look at and see okay it says
[06:59] it got the function call wrong it says
[07:01] the user is actually asking about
[07:04] current promotions for this phone the
[07:07] generated function call is for a product
[07:09] search which may not specifically
[07:11] address promotions a more appropriate
[07:13] function call might be the one that
[07:15] directly queries promotions or discounts
[07:18] we actually do have within the
[07:21] application uh a function called that's
[07:23] available for promos and discounts um
[07:27] might be easier to see that one in the
[07:28] slides but it didn't actually call that
[07:30] one it actually called the one that's
[07:32] specifically about product search
[07:34] instead and so it called the wrong
[07:37] function call and this is actually one
[07:39] where the rest of the entire execution
[07:41] branch is going to be off because it got
[07:43] the first call
[07:45] wrong this is why it's really important
[07:48] to if I had to zoom back out to just
[07:50] what do you care about in an application
[07:52] like this you care about first your
[07:54] traces because you want to see what the
[07:56] heck's happening where is it going down
[07:58] the flow you care about evals you care
[08:01] about evals knowing well something like
[08:04] where did it get in the application it
[08:07] wrong and then you also care about we'll
[08:09] go into this explanations of the
[08:11] evaluation so that when it gets it wrong
[08:14] you get a view of actually where did it
[08:16] go wrong what to go fix and what should
[08:19] I actually go do to iterate and improve
[08:20] the
[08:21] application um traces you want to
[08:24] evaluate it and then you want to use it
[08:26] to actually iterate on your application
[08:28] that's kind of the loop that people do
[08:30] as they're building these I can take
[08:32] this example I can go add it to my data
[08:34] set for example um and then I can say
[08:37] all right every single time I get
[08:39] something wrong like this I'm going to
[08:41] go build up my data set and then use
[08:42] these to now eventually run experiments
[08:46] and run experiments where I can track
[08:48] and improve and this is one where I
[08:50] modified The Prompt and I can run these
[08:52] experiments and then continuously
[08:54] iterate to make sure maybe the function
[08:56] description wasn't right maybe the call
[08:58] from the llm wasn't wasn't right and so
[09:01] there's all sorts of things you can
[09:02] actually do to improve but it really
[09:04] helps when you have evals at different
[09:07] levels of the application to be able
[09:11] to loading evals at different levels of
[09:14] the application so that you know where
[09:16] to go focus and where to actually go
[09:18] improve um so with that I'm going to
[09:21] actually jump into just some of the best
[09:23] practices we've seen from the ground um
[09:26] so you saw an example of basically a
[09:28] router-based application and function
[09:30] calling evals there's different types of
[09:31] levels that we see to to Applications uh
[09:35] how many of you guys have a chat bot
[09:36] with multiple back and forths sessions
[09:39] basically in there well typically you
[09:42] want evals at different levels of that
[09:44] at a session level often at a trace
[09:46] level often at a span level so getting
[09:50] this stuff to actually work in the real
[09:52] world isn't just single eval and we're
[09:55] good it's it's often single eval help me
[09:59] understand understand an explanation let
[10:00] me drill down to where exactly what
[10:02] component and so these these levels
[10:04] really help you do that and what we see
[10:07] folks do is they actually start to do
[10:09] this in iterative phases they first
[10:11] start off benchmarking The evals when
[10:13] they're
[10:14] building um and then as they're actually
[10:17] building the application and they're
[10:19] building each of the different
[10:20] components they're developing those eval
[10:23] templates iteratively along the
[10:25] application and then as they move into
[10:27] production they can actually go monitor
[10:28] it run it and you know run it as jobs
[10:30] but you're doing this as an iterative
[10:33] process as you're as you're kind of
[10:35] building um if there's one thing you
[10:37] take away from my talk today I hope it's
[10:38] actually this
[10:39] slide um evals with explanations are by
[10:43] far what we see
[10:46] real you know real people deploying
[10:48] applications finding the most useful in
[10:51] production a single incorrect not
[10:54] incorrect is just really hard to know
[10:56] what to go fix but when you have
[10:57] something like an explanation like we
[10:59] were looking at it makes it easier for
[11:01] teams to go okay here's what I go fix
[11:03] here's what I go dig into um and so run
[11:07] your evals with explanations um if you
[11:11] can there's different types of ways you
[11:13] can generate these evals actually
[11:15] there's if any of you guys are familiar
[11:16] with like you know in ml there's like
[11:18] regression type of models classification
[11:20] types of models Etc well there's
[11:22] different types of evals too there's
[11:24] numeric score outputs there's
[11:26] categorical outputs multi outputs multi
[11:29] class um can I actually maybe this is a
[11:32] fun question how many of you guys use
[11:34] numerical outputs as your as your L
[11:37] evals okay okay few Brave folks how many
[11:41] you guys use categorical
[11:43] evals okay both okay nice um I'm going
[11:48] to actually share we did a ton of
[11:50] research around this and we've been
[11:51] sharing about this but if you are using
[11:55] numerical outputs today highly recommend
[11:58] you actually don't only rely on them um
[12:01] here's a little research we shared and
[12:03] I'll I'll share some results of this but
[12:06] uh numeric scores just for people who
[12:09] you know need a refresher on it is um
[12:12] you basically have the output of your
[12:14] llm as a judge be a single number and
[12:17] this is a simple example I have a
[12:19] document one where we've corrup
[12:21] corrupted the document with a lot of
[12:23] spelling errors and one where we've
[12:24] corrupted the document with very little
[12:26] spelling errors so one of them the
[12:27] corruption is like 80% the other one's
[12:29] Corruptions like 11% and we asked the
[12:32] Elum as a judge hey can you evaluate and
[12:35] tell us how bad of the spelling errors
[12:37] are actually in this document for both
[12:39] of them it actually gave an eval score
[12:42] of 10 on it and we actually noticed this
[12:45] was really consistent
[12:47] across all the foundational models I
[12:49] think mistol actually did pretty good
[12:52] compared to some of the rest but uh
[12:55] across all the foundational models it
[12:57] was actually pretty binary in how it did
[13:01] the scores it was either a zero or it
[13:03] was it was either a one or it was a 10
[13:06] but it was never like this linear range
[13:09] of scores that you'd want it to expect
[13:11] so as you increase the density of
[13:13] corruption you actually get an increase
[13:15] in the number of scores it was pretty
[13:17] binary which kind of just indicated that
[13:18] if you're using numeric scores it might
[13:21] not be the right way to evaluate because
[13:24] you're not going to catch the
[13:26] granularity you know an 80% doesn't
[13:28] actually mean anything it's not going to
[13:30] really mean anything different than a
[13:32] 10% evaluation um so just a little best
[13:36] practices from the ground that we've
[13:37] been seeing as we've been running evals
[13:39] with with
[13:40] customers um in the last like four
[13:43] minutes here I'll share a couple more
[13:45] this is slightly more model evals
[13:47] related research uh for folks to kind of
[13:50] see the latest on on that front um for
[13:54] folks who have been following the needle
[13:56] and a haast stack test this was a really
[13:58] popular one on tring on Twitter um
[14:02] recently needle and the hyack test was
[14:04] basically we put a needle in a Hast
[14:06] stack we hid a fact in some context
[14:10] window um and the context window size
[14:14] can
[14:15] change but the key thing we were also
[14:18] trying to figure out is Does placement
[14:20] in the context window matter so this is
[14:22] an example where the fact was placed
[14:25] within the first 5% of the context
[14:27] window this is an example where the
[14:29] context was placed kind of lower down in
[14:32] the context window 90% And the reason to
[14:34] do this type of research is well if
[14:36] you're using rag which I'm sure many of
[14:38] you guys in this room are well does it
[14:40] matter if what you put in the context
[14:43] window that's the most important part is
[14:45] actually lower in the document does that
[14:47] actually impact the final output of the
[14:49] llm that's given and turns out it
[14:51] actually does so we did a lot of
[14:53] pressure testing against a number of
[14:55] foundational models um we do have the
[14:58] latest uh from the Opus model I just
[15:01] don't have it in this deck right now but
[15:03] this is actually results from anthropic
[15:04] Cloud 2.1 versus
[15:07] gp4 um the sorry it's hard to read but
[15:11] the x axis on the bottom is basically
[15:14] the context window size and then the Y
[15:17] AIS is basically the depth in the
[15:19] document and I mean gb4 was for sure
[15:23] better um in in being able to retrieve
[15:26] the fact but we consistently noticed
[15:29] actually that if you put the fact
[15:31] especially as you increased the context
[15:33] window if you put the fact earlier in
[15:36] the context window it actually had a
[15:38] really hard time almost remembering or
[15:41] retrieving to pull that document and so
[15:45] it we repeatedly as we ran this saw this
[15:48] kind of you know Red's where it gets it
[15:50] wrong Green's where it gets it right but
[15:52] it consistently has this like red block
[15:54] earlier in the context window so um for
[15:57] folks who are actually using rag
[15:59] depending on how much information you're
[16:01] putting in the document it's important
[16:03] to just balance where you place it in
[16:06] the document as well um uh another
[16:09] couple research results we um also
[16:12] tested not just retrieval but also
[16:14] retrieval with
[16:16] generation what do I mean by Generation
[16:19] Well after you did the retrieval you can
[16:21] do things like generation on it's kind
[16:23] of like the G and rag uh you actually
[16:26] generate a response after that so some
[16:29] of the common types of generations were
[16:31] things like um from this financial
[16:34] document round the numbers or map the
[16:36] dates or concatenate the string so these
[16:38] are all common types of generation tasks
[16:42] and um again we stack ranked two
[16:45] different models against each other this
[16:47] one's actually super interesting because
[16:50] gbd4 which you know at that point state
[16:53] of the art uh did worse than anthropic
[16:56] 2.1 almost four times was worse
[16:59] and we were really confused at why uh it
[17:05] was really great at retrieval but it
[17:06] wasn't great at generation and we kept
[17:09] going back and trying to understand like
[17:11] why this is over so many results and um
[17:14] talk to the team and basically we
[17:17] modified something in the prompt that
[17:21] made it so much better we asked it to
[17:24] please explain yourself and then answer
[17:26] the question if any of you guys have
[17:27] noticed but anthropic
[17:29] models are slightly worder and actually
[17:32] in this scenario it was more of a
[17:34] feature versus a bug because it was
[17:37] wordier it kept kind of asking itself to
[17:40] it like thought through the process and
[17:43] it thought through the process and then
[17:45] answered the question correctly and did
[17:47] the generation at the end as opposed to
[17:49] gp4 but when we asked gp4 to actually
[17:52] explain itself and then answer the
[17:54] question I was able to get a pretty
[17:56] remarkable jump in performance on
[17:59] generation so
[18:01] um uh hopefully this was helpful to give
[18:04] you guys a view of just like different
[18:05] type of task and model evals if you want
[18:08] to hear more about this um we're
[18:09] actually hosting uh an event rise
[18:12] observe on July 11th this is uh my code
[18:14] for a free ticket if any of you guys
[18:16] want to go there's all sorts of
[18:18] researchers from open ey anthropic
[18:20] mistol who are all coming to share model
[18:23] evals as well as Builders who are
[18:25] sharing their own task evals so um check
[18:28] it out thanks everyone
[18:33] [Music]
[18:42] [Music]
