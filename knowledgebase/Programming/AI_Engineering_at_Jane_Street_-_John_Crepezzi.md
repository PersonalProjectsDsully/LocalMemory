---
type: youtube
title: AI Engineering at Jane Street - John Crepezzi
author: Channel Video
video_id: 0ML7ZLMdcl4
video_url: https://www.youtube.com/watch?v=0ML7ZLMdcl4
thumbnail_url: https://img.youtube.com/vi/0ML7ZLMdcl4/mqdefault.jpg
date_added: 2025-05-26
category: Machine Learning in Software Development
tags: ['machine learning', 'code generation', 'OCaml', 'code reviews', 'model training', 'software development', 'version control', 'data collection', 'AI in coding', 'diff generation']
entities: ['Iron', 'Features', 'OCaml', 'diffs', 'ML', 'mli', 'commits', 'pull requests', 'code review', 'training data']
concepts: ['generating diffs from prompts', 'model training', 'code reviews', 'data collection for training', 'programming languages', 'code changes', 'machine learning', 'software development practices']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['familiarity with code reviews', 'version control systems (e.g., Git)', 'programming languages (e.g., OCaml)', 'basic machine learning concepts']
related_topics: ['machine learning in software development', 'code generation', 'software development workflows', 'data annotation for AI', 'version control systems', 'AI-driven code analysis', 'programming language ecosystems']
authority_signals: ['we needed to First create a goal a thing that we wanted the model to be able to do', "it's not that easy in order to get good outcomes", 'we wanted to be able to generate diffs given a prompt']
confidence_score: 0.8
---

# AI Engineering at Jane Street - John Crepezzi

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=0ML7ZLMdcl4)  
**Published**: 1 month ago  
**Category**: Programming  
**Tags**: ocaml, ai-engineering, devtools, software-development, monorepo, emacs, ocaml-programming  

## Summary

# Summary of "AI Engineering at Jane Street - John Crepezzi"

## Overview  
John Crepezzi, part of Jane Street's AI Assistant team, discusses how the company leverages large language models (LLMs) to enhance developer workflows. Jane Street faces unique challenges due to its reliance on OCaml and internally developed tools, which limit the effectiveness of off-the-shelf LLM solutions. The team focuses on training custom models for specific tasks, such as generating code diffs, while addressing data collection and alignment challenges.

---

## Key Points  
1. **Custom Tools and OCaml Challenges**  
   - Jane Street uses OCaml, a niche language, and has developed proprietary systems (e.g., a code review tool called *Iron* and a build system).  
   - Off-the-shelf LLMs struggle with OCaml's syntax and internal workflows, requiring tailored solutions.  

2. **Training Custom LLMs**  
   - Initial naive approach (e.g., training on code alone) failed; models needed "training data shaped like the test data."  
   - Goal: Train models to generate code diffs (e.g., modifying multiple files) that apply cleanly and typecheck.  
   - Targeted task: Generate diffs of up to 100 lines, requiring structured data (context, prompt, diff).  

3. **Data Collection Strategies**  
   - **Features/PRs**: Used as training data but required splitting into smaller components due to their size and formatting.  
   - **Commits**: Smaller chunks than features, but still needed automation to extract meaningful examples.  
   - Emphasis on aligning training data with real-world user prompts (e.g., "fix that error" vs. formal descriptions).  

4. **Lessons Learned**  
   - LLMs require examples that mirror the exact input-output patterns they’ll encounter.  
   - Custom tools like *Iron* provide valuable data but need preprocessing to fit training needs.  
   - Collaboration between developers and ML teams is critical for aligning model capabilities with user workflows.  

---

## Notable Insights  
- *"The only thing moving faster than the progress of the models is our creativity around how to employ them."*  
- OCaml's use in systems like *Hack* (implemented in OCaml) highlights the challenge of training models for company-specific languages.  
- Generating diffs requires not just code understanding but also contextual awareness of user intent and system constraints.  

--- 

This summary captures the technical depth of Jane Street's approach to integrating LLMs while addressing the unique hurdles of their tooling and language ecosystem.

## Full Transcript

[00:00] [Music]
[00:17] my name is John kzi and I work on a team
[00:19] at Jane Street called AI assistant our
[00:22] group roughly uh is there at Jan Street
[00:24] to try to maximize the value that Jan
[00:26] Street can get from large language
[00:28] models and I've spent my entire career
[00:31] uh in Dev tools before I worked at Jan
[00:33] street I was a GitHub for a long time
[00:35] and then before that I worked at a
[00:36] variety of other Dev tools companies and
[00:38] llms kind of present this really amazing
[00:40] opportunity in that they're so
[00:42] open-ended that we can build kind of
[00:43] anything that we can imagine and it
[00:45] seems like right now the only thing
[00:47] moving faster than the progress of the
[00:48] models is kind of our creativity around
[00:50] how to employ them uh at Jan street
[00:53] though we've made some choices that make
[00:55] adoption of off-the-shelf tooling a
[00:57] little bit more difficult than it is for
[00:59] other companies
[01:01] and kind of the biggest reason that we
[01:02] have this problem is that we use o camel
[01:05] as a development platform for those not
[01:08] familiar with oaml it is a a functional
[01:11] very powerful language but it's also
[01:13] incredibly obscure language uh it was
[01:15] built in France and its most common
[01:17] applications are in things like theorem
[01:20] proving or formal verification it's also
[01:22] used to write programming
[01:24] languages um we use oaml kind of for
[01:28] everything at change
[01:31] so just a couple quick examples when we
[01:32] write web applications of course web
[01:34] applications have to be written in
[01:36] JavaScript but instead we write oaml and
[01:38] we use a library called JS of oaml that
[01:41] is essentially a oaml bik code to
[01:44] JavaScript
[01:45] transpiler when we write plugins for Vim
[01:48] those have to be written in Vim script
[01:50] uh but we actually use a library called
[01:51] vaml which again is oaml to vimscript
[01:55] transpiler and uh even people at the
[01:58] company that are working on fpga code
[02:00] they're not writing verog they're
[02:02] writing in an O camel Library called
[02:04] hard
[02:05] camel uh so why are the tools on the
[02:08] market available not good for working
[02:10] with oaml I think it kind of comes down
[02:12] to a few primary reasons the first and
[02:14] the most important is that models
[02:16] themselves are just not very good at
[02:18] oaml and this isn't the fault of the AI
[02:20] labs this is just kind of a byproduct of
[02:22] the amount of data that exists for
[02:24] training so it's there's a really good
[02:26] chance that the amount of okl code that
[02:28] we have inside of J street it's just
[02:30] more than like the total combined amount
[02:32] of oam code that there exists in the
[02:34] world uh outside of our
[02:36] walls the second is that we've made
[02:38] things really hard on ourselves
[02:40] partially as a byproduct of working in O
[02:42] camel we've had to build our own build
[02:44] systems we built our own distributed
[02:46] build environment we even built our own
[02:47] code review system which is called
[02:50] iron we develop all of our software on a
[02:53] giant monor repo application and just
[02:55] for fun instead of storing that monor
[02:57] repo in git we store it in mercurial
[03:02] and uh at last count 67% of the firm
[03:06] uses emac instead of normal editors
[03:08] maybe like vs code uh we do have people
[03:11] using vs code but emac is the most
[03:13] popular and the last thing is we're
[03:15] dreamers I mean kind of everyone in this
[03:16] room hopefully is is a dreamer in a way
[03:19] uh and what I mean by this is we want
[03:20] the ability to kind of take llms and
[03:22] apply them to different parts of our
[03:24] development flow and light up different
[03:25] parts so maybe we want to use large
[03:27] language models to resolve merge
[03:29] conflict or build better feature
[03:31] descriptions or figure out who reviewers
[03:33] for features be and we don't want to be
[03:34] hampered by the boundaries between
[03:37] different systems when we do
[03:40] that over the next 15 minutes I'm going
[03:42] to cover our approach to large language
[03:44] models at CH Street uh particularly when
[03:46] it comes to developer tools um I'm going
[03:49] to talk about custom models that we're
[03:51] building and how we build them I'm going
[03:52] to talk about editor Integrations so
[03:54] these are the Integrations into uh to vs
[03:57] code emac and neovim
[04:00] and I will talk about uh the ability
[04:02] that we've built over time to evaluate
[04:03] models and figure out how to make them
[04:05] perform
[04:06] best and I guess at first glance it's
[04:08] not really obvious that training models
[04:10] at all is a good idea I mean it's very
[04:12] expensive proposition it takes a lot of
[04:14] time and it can go wrong in a ton of
[04:15] different ways who here has trained a
[04:16] model before or tried to train something
[04:18] like a model maybe took a foundation
[04:20] model and trained on top of
[04:22] it
[04:24] cool we were more convinced after we
[04:26] read this paper this is a paper from
[04:28] meta about a project called code compose
[04:31] and in this paper they detail their
[04:32] results fine tuning a model specifically
[04:34] for use with hack uh hack is actually
[04:37] pretty similar to O camel uh not in its
[04:39] like syntax or function but really just
[04:42] in the fact that it's used primarily at
[04:43] one company and not really used much
[04:45] outside of that company even though it's
[04:47] open source so oh actually a fun fact
[04:50] hack is implemented in no camel I think
[04:53] that's just like a total coincidence
[04:55] but uh we were pretty naive early on we
[04:58] read this paper and we decided that it
[05:00] would be really cool if we could
[05:01] replicate the results we thought we
[05:03] would just take a model off the shelf we
[05:05] would show it a bunch of our code and
[05:06] then we would get back a model that uh
[05:08] worked like the original model but knew
[05:10] about our libraries and
[05:12] idioms it turns out that's just not how
[05:14] it works uh it's not that easy in order
[05:16] to get good outcomes you have to have
[05:19] the model see a bunch of examples that
[05:20] are in the shape of the type of question
[05:22] that you want to ask the model so we
[05:24] needed to First create a goal a thing
[05:26] that we wanted the model to be able to
[05:27] do and in our in our world the goal that
[05:30] we came up with was this we wanted to be
[05:32] able to generate diffs given a prompt so
[05:35] what that means is we wanted a user
[05:37] inside of an Editor to be able to write
[05:39] a description of what they wanted to
[05:40] happen and then have the model suggest a
[05:43] potentially multifile diff so maybe you
[05:45] want to modify the test file an ml file
[05:48] and an mli which is kind of like a
[05:49] header
[05:50] file we wanted the diffs to apply
[05:52] cleanly and we wanted them to have a
[05:54] good likelihood of typechecking after
[05:56] they had been applied and we were kind
[05:59] of targeting this range of up to 100
[06:01] lines as an ideal zone of what we
[06:04] thought llms would actually be capable
[06:07] of and in order for that to work we
[06:09] needed to collect data like I was
[06:11] talking about before we needed data of
[06:12] the training shape that looked just like
[06:13] the test shape and this is what that
[06:16] shape looks like for this task you need
[06:17] to be able to collect a bunch of
[06:19] examples of what context the model would
[06:21] have had beforehand and then some prompt
[06:23] of what you want the model to do written
[06:25] hopefully in the same way that a human
[06:26] would write it and then some diff that
[06:28] would accomplish that goal so context
[06:30] prompt diff and we need a bunch of these
[06:32] examples so how do we get these how do
[06:34] we get these training
[06:36] examples kind of the first place to look
[06:38] is features features is I mentioned a
[06:41] code review system that we built
[06:42] internally this is what it looks like
[06:43] it's called iron uh features are very
[06:46] similar to poll requests I think you can
[06:48] just you know swap that term in your
[06:50] head and features at first glance have
[06:52] exactly the data they want on the
[06:54] description tab they have a human
[06:55] written description of a change and on
[06:57] the diff tab they have the code that
[06:59] accom is the goal of the
[07:01] developer but on closer look they're not
[07:03] exactly what you want right the way that
[07:05] you write a feature description or a p
[07:07] request description is really very
[07:08] different from what you might want to
[07:10] say inside of an editor so you're not
[07:11] writing multiple paragraphs in the
[07:13] editor you're just saying something like
[07:15] fix that error that's happening right
[07:16] now and that's just not how we write
[07:17] feature descriptions another problem
[07:20] with these features or P requests is
[07:22] that they're really large right often
[07:24] it's a feature is 500 lines or a
[07:26] thousand lines so in order to use it as
[07:28] training data we would need to have an
[07:29] automated way to pull features apart
[07:32] into individual smaller components that
[07:34] we could train
[07:35] on so we need smaller things than
[07:37] features what are those well maybe
[07:39] commits commits are smaller chunks than
[07:41] features uh this is what a typical
[07:43] commit log looks like at Jan street so
[07:46] this is not like a git short log this is
[07:47] literally just like an actual I want you
[07:49] to look at this as an actual git log and
[07:52] where it says summary Z that's my commit
[07:56] message we don't really use commits the
[07:59] same way the rest of the world use
[08:00] system so we use commits mostly As
[08:02] checkpoints between different parts
[08:03] parts of a development cycle that you
[08:05] might want to revert back to commits
[08:08] don't have a description and they also
[08:09] have the same problem in that they're
[08:11] not isolated changes they're they're a
[08:13] collection of changes what we actually
[08:15] ended up with was a approach called
[08:17] workspace snapshotting and the way that
[08:19] that works is we take snapshots of
[08:21] developer workstations throughout the
[08:23] workday so you can think like every 20
[08:25] seconds we just take a snapshot of what
[08:26] the developer doing and as we take the
[08:28] snapshots we also take snapshots of the
[08:30] build status so the build that's running
[08:32] on the box we can see what the error is
[08:34] or whether the build is green and we can
[08:36] kind of notice these little patterns if
[08:38] you have a green to Red to Green that
[08:40] often corresponds to a place where a
[08:42] developer has made an isolated change
[08:44] right you start writing some code you
[08:46] break the build and then you get it back
[08:47] to green and that's how you make a
[08:49] change maybe this one the red to Green
[08:51] this is the place where the developer
[08:53] encountered an error whether that's a
[08:54] type error or a compilation error and
[08:57] then they fixed it so if we capture the
[08:58] build error at the Red State and then
[09:00] the diff from red to Green we can use
[09:02] that as training data to help the model
[09:04] be able to recover from
[09:06] mistakes the next thing we need is a
[09:08] description and the way that we did that
[09:10] we just used the large language model so
[09:11] we had a large language model write a
[09:13] really detailed description of a change
[09:15] in in as much words as it possibly could
[09:17] and then we just kept filtering it down
[09:19] until it was something that was around
[09:20] the right level of what a human would
[09:23] write so now we have this training data
[09:26] and training data is kind of only half
[09:27] the picture of training a model so you
[09:29] you have the the supervised training
[09:31] data and then you need to do the second
[09:32] part which is the reinforcement learning
[09:34] this is really where models get a lot of
[09:36] their power right we we align the
[09:38] model's ability to what humans think is
[09:41] actually good code so what is good code
[09:45] I guess on the surface good code is I
[09:47] mean it's it's code it has the parse is
[09:49] code meaning if a piece of code doesn't
[09:52] go through the O camel parser and come
[09:53] out with a green status that is that is
[09:55] not good code I would say by most
[09:57] definitions
[09:59] uh good code in oaml because it's
[10:01] statically typed is code that type
[10:03] checks so we want to have good code be
[10:05] code that when it is applied on top of a
[10:08] base revision can go through the type
[10:10] Checker and the type Checker agrees that
[10:11] the code is
[10:13] valid and of course the the gold
[10:15] standard is that good code is code that
[10:16] compiles and passes tests so ideally in
[10:20] during the reinforcement learning phase
[10:21] of a model you could give the model a
[10:23] bunch of tasks that are like verifiable
[10:26] we have the model performs some some
[10:28] edit and then we check whether or not it
[10:30] actually passes the test when applied to
[10:32] the
[10:33] code so we did that uh we've done this
[10:36] as part of our our training cycle and we
[10:38] built this thing that is called uh CES
[10:41] it's the code evaluation service you can
[10:43] think of it kind of like a build service
[10:45] except with a slight modification to
[10:47] make it much faster and that's that
[10:50] first we pre-warm a build it sits at a a
[10:52] revision and is green and then we have
[10:55] these workers that all day just take
[10:57] diffs from the model they apply them and
[10:59] then we determine whether the build
[11:00] status turns red or green and then we
[11:02] report that error or or success back up
[11:05] to the build function and through
[11:07] continued use of this service over the
[11:09] course of like months we're able to
[11:10] better align the model to write code
[11:13] that actually does compile and past
[11:17] tests it turns out this exact same setup
[11:20] is the one that you would want for
[11:22] evaluation so if you just hold out some
[11:24] of the RL data you can also use it to
[11:26] evaluate model's ability to write code
[11:28] kind of looks like this you give the
[11:29] model a problem you let it write some
[11:31] code and then you evaluate whether or
[11:33] not the code that it writes actually
[11:37] works and training is hard and it can
[11:39] have kind of uh catastrophic but
[11:42] hilarious results so at one point we
[11:45] were training a code review model and
[11:47] this is a totally separate model but the
[11:49] idea was we want to be able to give some
[11:50] code to this model and have it do a
[11:52] first passive code review just like a
[11:53] human would do to try to save some of
[11:55] the toil of of code review we train this
[11:58] model we put a bunch of dat dat into it
[11:59] we worked on it for months we're real
[12:01] excited and we put our first code in for
[12:03] uh for code review through the automated
[12:05] agent it spun for a bit and it came back
[12:08] with something along the lines of um
[12:10] I'll do it
[12:12] tomorrow and like of course it did that
[12:15] because it's trained on a bunch of human
[12:16] examples and humans write things like
[12:18] I'll do things or I'll do this tomorrow
[12:21] uh so it's it's you know not very
[12:22] surprising so having evaluations that
[12:24] are meaningful is kind of a Cornerstone
[12:26] of making sure that models don't go off
[12:28] the rails like this and you don't waste
[12:29] a bunch of your time and
[12:31] money in the end though the real test of
[12:33] models is whether or not they work for
[12:35] humans so I'm going to talk a little bit
[12:37] about the editor Integrations that we've
[12:39] built to expose these models to
[12:40] developers at Jan
[12:42] Street kind of when we were starting
[12:44] building these Integrations we had three
[12:45] ideas in mind the first idea was wow we
[12:48] support three editors we have neovim vs
[12:51] code and emac and we really don't want
[12:52] to write the same thing three times so
[12:55] ideally we don't want to write all the
[12:56] same context building strategies and all
[12:58] of the same prompting strategies we want
[13:00] to just write at once the second is that
[13:02] we wanted to maintain flexibility so we
[13:04] had a model that we were using at the
[13:06] time uh that was not a fine tuned model
[13:08] we were pretty convinced that a fine
[13:09] tuned model was in our future we wanted
[13:11] the ability to do things like swap the
[13:13] model or swap the prompting strategy out
[13:15] and lastly we wanted to be able to
[13:17] collect metrics so in a developer uh in
[13:20] their in their editor developers care
[13:23] about latency and they care about
[13:24] whether or not the diffs actually apply
[13:26] so we wanted to get kind of on the
[13:27] ground real experience of whether or not
[13:28] the diffs really were meaningful for
[13:32] people this is the simplified version of
[13:34] the architecture that we settled on for
[13:36] this service the AI development
[13:38] environment essentially you have llms on
[13:41] one side and then Aid handles all of the
[13:44] uh ability to construct prompts and to
[13:46] construct context and to see the build
[13:48] status and then we are able to just
[13:49] write these really thin layers on top of
[13:51] Aid uh for each of the individual
[13:53] editors and what's really neat about
[13:55] this is that Aid sits as a sidecar
[13:57] application on the Developers machine
[14:00] which means that we when we want to make
[14:01] changes to Aid we don't have to make
[14:03] changes to the individual editors and
[14:05] hope that people restart their editors
[14:07] we can just restart the Aid Service on
[14:08] all of the boxes so we restart Aid and
[14:11] then everyone gets the most recent
[14:15] copy uh this is an example of Aid
[14:17] working inside of vs code so this is the
[14:19] sidebar in vs code very similar to
[14:21] something like co-pilot except this
[14:23] thing allows you to uh ask for it and
[14:25] get back multifile diffs uh and you can
[14:28] see it kind of looks like what you'd
[14:29] expect in VSS code it's it's you know a
[14:31] visual interface that lays things out
[14:33] really
[14:34] nicely this is what we built in emac
[14:36] though so in emac developers are used to
[14:39] working in text buffers they move around
[14:41] files they want to be able to copy
[14:42] things the normal way that they copy
[14:44] things so we actually built the eight
[14:46] experience in emac into a markdown
[14:47] buffer so users can move around inside
[14:50] this markdown buffer they can ask
[14:51] questions and then there are key binds
[14:53] that essentially append extra content to
[14:54] the bottom of the markdown
[14:58] buffer AIDS architecture lets us plug
[15:00] various pieces in and out like I
[15:02] mentioned uh so we can swap in new
[15:05] models we can uh make changes to the
[15:07] context building we can add support for
[15:09] new editors which I think probably
[15:11] sounds far-fetched but this is something
[15:12] we're actually just doing right
[15:14] now uh and we can even add domain
[15:16] specific tools so different areas of the
[15:19] company can supply tools that are
[15:20] available inside of the editors and they
[15:23] kind of end up in all the editors
[15:24] without having to write individual
[15:26] Integrations eight also allows us to AB
[15:29] test different approaches so we can do
[15:30] something like send 50% of the company
[15:32] to one model and 50% to another and then
[15:34] determine which one gets the higher
[15:36] acceptance rate a is kind of a an
[15:39] investment that pays off over time every
[15:41] time something changes in large language
[15:43] models we're able to change it in one
[15:45] place Downstream of the editors and then
[15:47] have it available
[15:50] everywhere and things change like really
[15:53] often and we need to be ready uh when
[15:55] things change what I what I've had time
[15:57] to show you today is only a small
[15:59] portion of what my team is doing we've
[16:01] got a lot of other things going on so
[16:03] we're finding new ways to apply rag
[16:05] inside of the editors we're applying
[16:07] similar approaches to what you've seen
[16:08] here to large scale uh multi-agent
[16:11] workflows we are working with reasoning
[16:14] models more and more but the approach is
[16:16] the same through all of these we keep
[16:18] things pluggable we lay a strong
[16:20] Foundation to build on top of and we
[16:22] build the ways for the rest of the
[16:24] company to add to our experience by
[16:26] adding more domain specific tooling on
[16:28] top of it
[16:30] uh if you think what I've said is
[16:31] interesting and you want to talk more
[16:32] about this I would love to hear from you
[16:34] you can just find me outside and thank
[16:36] you for your time
[16:38] [Music]
[16:38] [Applause]
[16:43] [Music]
