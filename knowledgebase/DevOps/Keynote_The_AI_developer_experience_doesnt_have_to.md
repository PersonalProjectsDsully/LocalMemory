---
type: youtube
title: Keynote: The AI developer experience doesn't have to suck – why and how we built Modal
author: AI Engineer
video_id: qeDPKbWjsuk
video_url: https://www.youtube.com/watch?v=qeDPKbWjsuk
thumbnail_url: https://img.youtube.com/vi/qeDPKbWjsuk/mqdefault.jpg
date_added: 2025-05-26
category: Cloud Computing & DevOps
tags: ['modal', 'serverless', 'cloud computing', 'containerization', 'GPU acceleration', 'Python', 'machine learning', 'cloud deployment', 'devops', 'distributed systems', 'cloud infrastructure', 'iterative development']
entities: ['Modal', 'NVIDIA H100', 'A100', 'T4', 'PyTorch', 'Docker', 'Python', 'serverless functions', 'cloud computing', 'containerization']
concepts: ['serverless computing', 'containerization', 'GPU acceleration', 'iterative development', 'cloud deployment', 'Python function orchestration', 'distributed computing', 'machine learning infrastructure']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic Python programming skills', 'Familiarity with cloud computing concepts', 'Understanding of containerization (Docker)']
related_topics: ['Cloud architecture design', 'Serverless application development', 'GPU optimization for ML', 'Container orchestration', 'Python-based cloud tools', 'Machine learning deployment pipelines', 'DevOps automation']
authority_signals: ["I've been working on Modal for a while", 'this is how we designed it', "we want to make it fast and feel like we're almost developing things locally"]
confidence_score: 0.85
---

# Keynote: The AI developer experience doesn't have to suck – why and how we built Modal

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=qeDPKbWjsuk)  
**Published**: 3 months ago  
**Category**: DevOps  
**Tags**: ai-development, devops, cloud-computing, containerization, python, machine-learning, infrastructure  

## Summary

# Summary of Modal's Developer Experience Focus

## Overview
Eric Bernhardson, CEO of Modal, discusses the company's mission to build an infrastructure platform for AI/ML that prioritizes a seamless developer experience. Modal aims to address the challenges of slow feedback loops and complex deployment processes by enabling developers to run Python functions in the cloud with minimal friction, similar to local development.

---

## Key Points

### 1. **Problem with Current Developer Experiences**
- **Slow Feedback Loops**: Traditional cloud workflows involve lengthy cycles of building, pushing, and deploying containers, which hinders rapid iteration.
- **Complexity**: Managing infrastructure, hardware, and environments often diverts focus from core development tasks.

### 2. **Modal's Solution**
- **Serverless Functions**: Converts Python functions into cloud-executable tasks, abstracting infrastructure complexity.
- **Fast Iteration**: Supports real-time code updates without rebuilding or redeploying containers.
- **Hardware Flexibility**: Developers can specify hardware (e.g., GPU types like H100) directly in code.

### 3. **Technical Approach**
- **Containerization**: Uses Docker images defined in code (via Modal's SDK) to manage environments (e.g., installing PyTorch).
- **Custom Scheduling**: Built-in infrastructure for container orchestration, GPU allocation, and resource management.
- **CLI Integration**: Command-line tools enable interactive cloud execution, streaming logs in real time.

### 4. **Use Cases**
- **Generative AI**: Supports inference, batch embeddings, and fine-tuning (e.g., AI-generated music via "isso").
- **Scalability**: Handles large-scale applications across diverse hardware (e.g., A100, T4, H100 GPUs).

### 5. **Developer-Centric Design**
- **Local-Like Experience**: Emulates local development speed and simplicity for cloud tasks.
- **Code-Defined Environments**: Eliminates manual Dockerfile management by embedding environment setup in code.

---

## Key Quotes
- *"The whole point is to make it fast and feel like we're almost developing things locally."*
- *"We want to make it fast and feel like we're almost developing things locally."*
- *"Modal is not an AI API—it's about running any code in the cloud with full control."*

---

## Actionable Insights
1. **Prioritize Fast Container Start Times**: Reduce friction in development cycles by optimizing containerization workflows.
2. **Leverage Python for AI/ML**: Use Python's simplicity and ecosystem for building scalable, hardware-agnostic applications.
3. **Adopt Serverless Abstractions**: Shift from infrastructure management to code-centric workflows for faster iteration.
4. **Define Environments in Code**: Embed dependency management (e.g., PyTorch) directly in code to avoid manual Dockerfile maintenance.

--- 

This summary captures Modal's focus on redefining the AI/ML developer experience through speed, simplicity, and flexibility.

## Full Transcript

[00:00] hi my name is Eric bernhardson it's
[00:02] great to be here
[00:04] virtually uh who am I I am the CEO of a
[00:07] company called modal we are based here
[00:08] in New York most of my background is in
[00:11] data AI machine learning and in
[00:13] particular I was at Spotify for many
[00:15] years and built a music recommendation
[00:17] system there I did leave about 10 years
[00:19] ago and did all kinds of other stuff in
[00:20] between but started modol about 4 or
[00:24] five years ago during the pandemic and
[00:26] the mission I had at that point was to
[00:29] build
[00:30] an infrastructure platform for data AI
[00:34] machine learning in a way that takes all
[00:35] the that that makes it fun again to
[00:38] write these applications to to basically
[00:41] to to deploy models scale them out run
[00:43] large scale back jobs making it possible
[00:46] to focus on writing code and not have to
[00:48] deal with infrastructure as it turned
[00:50] out gen was a perfect use case for this
[00:52] we just didn't know it at that time uh
[00:54] modal is very much focused on high code
[00:56] use cases what that means is we focus on
[00:58] people want to write their own code in
[01:00] particular writing their own models but
[01:02] also in many cases using existing models
[01:04] in a way where you have want have
[01:05] control or the workflow or or other
[01:07] thing and so you can think of us more as
[01:09] like kubernetes or AWS Lambda in the
[01:12] sense that we can run arbitrary
[01:13] containers or arbitrary code we do focus
[01:15] on python right now might add other
[01:17] languages in the future unlike system
[01:20] like kubernetes we're fully managed so
[01:23] we we run all the infrastructure we have
[01:24] a big pool of thousands of gpus and CPUs
[01:28] uh but we let you run all kinds of of
[01:30] applications in our cloud and uh this
[01:34] could really be anything in that sense
[01:36] we're not an AI API we don't have one
[01:38] model or 10 models that we put behind an
[01:41] API doing next token prediction you can
[01:43] really it run anything which puts a
[01:44] little bit more owners on the developer
[01:46] to to build this thing but it also makes
[01:48] this a lot more
[01:49] powerful in particular when I think
[01:51] about platforms and how they make you
[01:54] productive and makes it fun to write
[01:56] code a lot of my experience is that it
[01:59] comes down to fast feedback loops so in
[02:02] order to make Engineers fast and make
[02:04] them more productive you want to have
[02:05] this like super fast feedback loop that
[02:07] let you iterate on code very quickly I
[02:09] think cloud has been a phenomenal
[02:11] invention and lets us build things with
[02:13] you know far more powerful things but
[02:15] it's arguably a step backwards in terms
[02:17] of developer experience and and thinking
[02:19] a lot about this problem what what I
[02:21] realized was in order to solve this we
[02:23] had to build our own system to start
[02:26] containers in the cloud very fast
[02:28] because if you can start containers in
[02:29] the cloud very fast you can take code
[02:31] that that the user is building locally
[02:33] and execute in the cloud maybe inside a
[02:35] custom image running on a GPU whatever
[02:38] uh and and have that sort of fast
[02:39] feedback loop that you like when you run
[02:41] things
[02:42] locally uh as it turns out solving
[02:45] container C start in a distributed
[02:47] system is a very very deep rabbit hole
[02:49] we have to build our own scheduler we
[02:51] have to build all build our own file
[02:53] system and and many other things we we
[02:55] we sit out on a multi-year journey that
[02:57] we still haven't completed building a
[02:58] lot of this very very core very
[02:59] foundational
[03:01] infrastructure model today you can think
[03:03] of it as two facets one is a big
[03:05] resource
[03:06] pool we on thousands of gpus different
[03:09] types h100s A1 100s l4s t4s you name it
[03:13] and the only way to access those is
[03:14] through python esk we might add other
[03:17] languages in the future like I mentioned
[03:18] but right now it's Python and and the
[03:19] reason we started with python is
[03:21] obviously that python is such a dominant
[03:23] language in AI machine learning and and
[03:26] data applications one way to think about
[03:28] model is that it's it's a serverless
[03:30] framework that basically lets you take
[03:32] any python function and turn that into
[03:34] serverless function and so you do that
[03:37] by applying this decator as you can see
[03:38] in this code sample I'll show you a
[03:40] little bit more examples in a second uh
[03:43] people use model for very large scale
[03:45] applications but also small scale
[03:46] applications the the biggest use case is
[03:49] most likely gen
[03:51] inference uh we in particularly have
[03:54] seen a lot of traction within diffusion
[03:56] models so for instance AI generated
[03:59] music video images but also a lot of
[04:03] bass jobs a lot of for instance
[04:04] processing very large scale medical
[04:07] images or doing computer vision on on
[04:11] frames of videos um seeing a lot of
[04:13] traction in computational BIO things
[04:15] like protein folding both things running
[04:17] on gpus or or but also CPUs of course
[04:20] LMS you can't talk about geni without
[04:22] mentioning LMS we have a lot of
[04:24] fine-tuning applications batch
[04:26] embeddings uh of course inference as
[04:28] well uh some of our customers one
[04:31] customer I always think is incredibly
[04:33] cool is isso they uh do AI generated
[04:38] music and and run a lot of their
[04:40] inference on model but we have many
[04:42] other use cases for for modal some
[04:44] running a very large scale uh doing all
[04:47] kinds of different different
[04:48] applications model it's a little bit
[04:50] abstract to talk about model without
[04:52] going into code so I'm going to do some
[04:54] live coding uh so let's jump into the
[04:57] terminal and I'll show you exactly try
[04:59] to give you an idea of like what it
[05:01] looks like in code so let's look at a
[05:04] very very basic modal
[05:06] application uh model basically one way
[05:09] to think about it is we take python
[05:11] functions and turn them into things that
[05:12] run in the cloud uh there's a very
[05:14] simple function in a called Square which
[05:17] returns a square of a number and also
[05:19] prints on stuff the standard error and
[05:21] this decorator that we apply apop
[05:24] function takes that and turns that into
[05:26] a serverless function running in the
[05:28] cloud and there's a few different ways
[05:30] to invoke this thing but we have a
[05:32] little thing here that basically make
[05:33] sure to trigger it from our laptop when
[05:35] we run it from the command line so we're
[05:37] going to do that so mod has a little
[05:38] command line interface where basically
[05:41] it lets you run things
[05:42] interactively and what happens when we
[05:44] run this thing is we take the code we
[05:46] stick it in a container we execute it in
[05:48] the cloud as it's executing it streams
[05:50] the output back and the whole point of
[05:52] this is like we want to make it fast and
[05:54] feel like we're almost developing things
[05:55] locally it's almost as fast as running
[05:57] things locally and this extends to
[05:58] things like let's say want to edit this
[06:00] thing uh and just you know print
[06:03] something
[06:04] else and in instead of having to rebuild
[06:08] a container push that the container to
[06:10] the cloud download logs Etc with a slow
[06:12] feedback Lo we just it just picks up the
[06:14] latest code rather and rebuilds the
[06:15] container automatically and all these
[06:16] things right and so while you're like
[06:19] building applications and rewriting code
[06:21] you can always just run things in the
[06:23] cloud very very fast so far this is just
[06:26] showcases like the sort of iteration
[06:28] speed but also let's let's look at the
[06:29] power of model like what can you do with
[06:31] model like what kinds of stuff can you
[06:32] can we get to scale can we run things on
[06:34] on on other types of Hardware so let's
[06:37] let's actually run this on an h100 and
[06:40] and the way in model you do that is by
[06:41] saying just on the function decorator
[06:43] you say GPU equals one h100 uh we have a
[06:47] bunch of other types as I mentioned we
[06:49] have A1 100s and t4s and all kinds of
[06:51] other ones but let's run this on an h100
[06:53] which is nvidia's
[06:55] Flagship um and we can get access to an
[06:59] h100 in a couple of seconds this is
[07:01] obviously not using the h100 uh but
[07:03] we're running it in a container that has
[07:05] access to an h100 so let's say we want
[07:08] to actually access it now we need to
[07:09] probably install some software right so
[07:12] we might want to install torch in this
[07:13] case uh there's a few different ways you
[07:15] can do that in model you can give us a
[07:17] Docker file you can also point the
[07:18] docker image but the easiest thing to do
[07:21] that is to basically Define the entire
[07:24] compute environment in code so we're
[07:26] going to define the the container image
[07:28] using modal mod python SDK so we're
[07:31] going to say image equals model. image.
[07:34] Debian slim as a base image and we're
[07:36] going to pip install torch and then
[07:39] we're going to use this image on this
[07:41] function and we're going to import torch
[07:44] and just to show that it works we're
[07:45] going to
[07:46] print torch. Cuda doget device
[07:51] name hopefully this works when I run
[07:53] this we'll delete this line and when I
[07:55] run this thing hopefully it will print
[07:57] something like we're running on h100
[08:01] and um as you can see it's still very
[08:04] fast but slightly slower this time uh
[08:07] because loading torch takes a little bit
[08:09] of extra overhead and we'll talk about
[08:11] it in a second what we've done to to
[08:12] reduce that overhead but but it takes
[08:14] maybe about a second to initialize torch
[08:17] uh okay cool so now we can run stuff on
[08:21] h100s let's try to run things on a lot
[08:23] of h100s uh and so let's try to scale
[08:25] things out a little bit uh in modal any
[08:28] function can you can map over any
[08:30] function in model just in code so
[08:32] instead of calling just a single
[08:35] function invocation we're going to Fan
[08:37] out and do a TH or maybe let's do 10,000
[08:39] function invocation and you can do this
[08:41] in Code by just saying we're going to
[08:43] map over 5,000 I said 10,000 actually so
[08:47] let's do that and we're going to unpack
[08:49] the the iterator and let's um print X
[08:55] just to show some progress and what
[08:57] model does when you fan out is that it's
[09:00] going to spin up as many containers as
[09:02] possible and so you can see we're
[09:04] already running five containers six
[09:06] containers eight containers uh it makes
[09:08] it very easy to to Fan out and start you
[09:11] know even hundreds of containers or even
[09:13] thousands of containers running on gpus
[09:15] if we keep this running for several
[09:16] minutes we can easily scale up to very
[09:19] large um number um so this gives you
[09:23] basically the ability to take something
[09:25] like you know that needs a lot of
[09:26] compute and you know something like a
[09:29] that's job and fan out spin up thousands
[09:31] of containers paralyze over it and and
[09:34] get results much faster uh we're going
[09:37] to take a look at
[09:39] the UI for a second uh model also has a
[09:43] UI uh that you can access if you go to
[09:46] the uh website uh the URL is printed in
[09:50] the console so let's take a look at
[09:53] that uh so we can see the app details in
[09:57] our UI there's all kinds of of
[09:59] interesting things here modal has a
[10:01] pretty rich UI that lets you see
[10:03] container metrics logs uh lets you set
[10:06] up users and many other things so if you
[10:08] zoom in for instance on the number of
[10:10] containers we can see here we spawn up
[10:12] 18 containers at Peak as I mentioned if
[10:14] we had kept going we would reach a much
[10:16] larger number uh we got at 18 containers
[10:19] at this point can look at CPU
[10:21] utilization GPU Etc um could look at GPU
[10:24] temperature 33 cels uh even the the watt
[10:29] could consumption so there a a lot of
[10:31] other things here we can look at app
[10:32] logs and many other
[10:34] things
[10:35] um okay let's switch back to the
[10:40] terminal for a second and see some other
[10:42] stuff there's a lot of stuff so I'm not
[10:43] going to go into every single
[10:46] possibility of how to use model but one
[10:48] thing I didn't show that I think is
[10:50] interesting and very valuable is you can
[10:52] also deploy these things so so far we
[10:55] only showed how to run things
[10:56] interactively which means we have sort
[10:58] of you know we run things from our
[10:59] laptop but if I take this code and
[11:02] deploy this using model
[11:05] deploy uh we get this persistent
[11:08] endpoint and what's nice about that is
[11:10] now we have this thing we can call from
[11:12] any other context in Python and I'm just
[11:14] going to show this using my rapple if we
[11:16] import model and if we do look up like
[11:21] this uh we get this handle to this
[11:23] remote function so let's call This And
[11:26] the first time we're going to call it
[11:27] we're going to have inquir a call start
[11:29] so it's going to take a couple seconds
[11:31] because the container has to start up
[11:32] and remember we're we're importing torch
[11:34] and we're running this on an h100 so it
[11:35] takes a little bit of extra time the
[11:37] container keeps running for a few for
[11:39] for for 60 seconds by default and then
[11:40] shuts down so now it's actually idle so
[11:42] if we call this again typically it' be a
[11:44] little bit faster and uh we're obviously
[11:47] you know wasting an enormous amount of
[11:49] flops using a GPU to calculate the
[11:51] square of a number uh but but this
[11:54] showcases you know how you can easily
[11:55] take things and deploy it uh even on
[11:58] very powerful hardware and and building
[12:01] serverless endpoints for instance doing
[12:02] inference and and you know and modal
[12:04] handles all the scaling so when you
[12:06] invoke this function multiple times will
[12:08] just scale up using more and more
[12:09] containers and shut down um many other
[12:12] things you can do with model you can set
[12:14] up distribute file systems that you can
[12:17] mount to each container so you can like
[12:18] exchange information using the file
[12:20] system you can set up web end points you
[12:23] can set up cron jobs and many other
[12:26] things uh so this hopefully gives you a
[12:28] little bit more of an idea of like what
[12:29] modal looks like from an engineering
[12:31] perspective like what does it look like
[12:32] when you're interacting through code
[12:34] with
[12:35] modal let's talk a bit about how modal
[12:37] Works under the hood and as I mentioned
[12:40] modal in order to deliver on this
[12:43] developer experience that I always
[12:44] wanted to have we had to go down this
[12:46] very deep rabbit hole and build a lot of
[12:48] custom infrastructure ourself and that's
[12:49] the only way we felt that we can make it
[12:52] fast enough we couldn't use carbonet we
[12:54] couldn't use Docker so we have to build
[12:56] a lot of this stuff ourselves and it
[12:58] should be pointed out where standing on
[12:59] shoulders of giants here uh we're using
[13:02] a fantastic container runtime called G
[13:04] viser uh that gives us isolation but we
[13:06] have to build a lot of stuff around it
[13:09] uh we had to build it on scheduler and
[13:11] many other things but we're obviously
[13:12] using a lot of the existing things in
[13:14] Linux and and other systems and using
[13:16] fantastic Cloud tools as
[13:18] well uh in order to deliver the
[13:21] developer experience that we wanted to
[13:22] as I mentioned and the feedback loops
[13:24] that we wanted to we had to figure out
[13:25] container cold start and container cold
[13:28] start starting containers fast in a
[13:30] distributed system is a hard problem so
[13:33] let's talk about what containers are to
[13:35] start with containers are and this is my
[13:37] super crude unfair generalization of
[13:40] what a container is or container image
[13:42] it's basically two things it's a root
[13:44] file system so that's like the slash
[13:46] that you have in in Linux that contains
[13:48] all the data on your drive and then it's
[13:50] a bunch of stuff to is isolate processes
[13:53] so they can't tamper with each
[13:55] other uh there are many inefficiencies
[13:58] with how container images are stored and
[14:02] how container images are transferred in
[14:04] particular one of the issues is that
[14:06] there's a lot of junk there's a lot of
[14:09] stuff we're never going to read like
[14:10] many container images has Pearl
[14:12] installed by default Man pages local
[14:14] information time zone information for
[14:17] usbekistan you're never going to read
[14:19] this stuff so we're sending all this
[14:20] data back and forth and and and the core
[14:22] thing here is we want to start
[14:23] containers on a remote file on a remote
[14:25] worker very very fast we want to
[14:27] minimize the amount of data that has to
[14:28] be transferred
[14:29] we want to do as little as possible the
[14:31] other inefficiency is that there's a lot
[14:33] of redundancy in this a lot of the fils
[14:36] that are being transferred back and
[14:37] forth are actually the same files so if
[14:39] you grab just like three very different
[14:42] container images like I did in this case
[14:44] and you look at the files it actually
[14:46] turns out to be mostly the same files to
[14:47] a very large extent so with those two
[14:50] tricks with those two observations
[14:52] there's a number of Tricks we can do and
[14:53] and we so we built what's called a
[14:56] Content addressed storage and this is
[14:58] not new invention this is not something
[15:00] we came up with but it's RAR used in
[15:02] production systems notably AWS Lambda
[15:05] actually uses the same technique and the
[15:07] idea is that instead of storing the
[15:10] images directly we store the images the
[15:13] container images as just a bunch of
[15:15] metadata that points to blobs and for
[15:19] each blob we compute a check sum or hash
[15:23] value and then we use that to D
[15:25] duplicate all the blobs because there's
[15:26] enormous amount of redundancy in these
[15:29] blobs and this means the container
[15:32] images themselves are actually just
[15:33] little pieces of metadata and in many
[15:36] cases we can cash a very large
[15:39] percentage of the container images and
[15:41] we can also avoid pulling data that we
[15:44] we're not going to need by lazy loading
[15:47] a lot of the data on axess uh this is
[15:50] tricky because container call start in
[15:53] particular with python is very latency
[15:57] sensitive because we end up doing a lot
[15:59] of very sequential file aises so in many
[16:02] cases when a container starts up in
[16:03] model or or in any in Python in any case
[16:07] uh it requires reading every single
[16:09] module every single python module which
[16:11] is many in many cases ends up being
[16:14] several thousand python modules each one
[16:17] of them requires accessing the file
[16:18] system and so what we can't allow is
[16:22] that to take several milliseconds
[16:23] because if you're doing something that
[16:25] takes several milliseconds and you're
[16:26] doing it a thousand times it and I'm
[16:29] taking several seconds and we want to
[16:31] avoid that so there's a lot of tricks
[16:33] that we have to do in order to basically
[16:35] get this down below a second we do a lot
[16:38] of prefetching we do a lot of task
[16:40] tracing we look at you know historical
[16:42] runs and see what types of files was
[16:44] access last time it ran and then
[16:47] building these containers is is
[16:49] obviously also another whole challenge
[16:51] we we basically built it on container
[16:53] image
[16:54] Builders uh another technique that we
[16:56] also more recently started leveraging is
[16:58] we can snapshot this CPU memory so we
[17:01] talked about how we snapshot the
[17:03] container images and we we we we cache a
[17:05] lot of the data which means like when
[17:07] you're loading it you don't have to
[17:09] fetch a lot of data but what if you can
[17:10] avoid loading the data in the first
[17:12] place what if you can just like revert
[17:13] to the the memory State the CPU memory
[17:16] the ram of of uh a container and as it
[17:20] turns out gvisor actually supports this
[17:22] and that's another way that arguably
[17:24] supersedes a lot of the previous stuff
[17:27] uh in practice they end up kind of both
[17:29] reinforcing this this container coal
[17:30] start but this lets us cut down even
[17:32] more dramatically uh things like stable
[17:35] diffusion we can now start in in a
[17:37] couple of seconds even though it
[17:39] involves loading very very large uh
[17:41] model weights like you know five or 10
[17:43] gigabytes uh we're also looking at GPU
[17:46] snapshotting which will make things even
[17:48] more even faster which is very exciting
[17:52] um and so doing all these things you
[17:55] know owning the entire stack owning the
[17:57] file system you know you know building a
[17:59] storage system I didn't talk about the
[18:00] storage system we basically use R2 and
[18:03] we run in many different regions and so
[18:05] we use both the CDN and the the R2 and
[18:09] and and so all these optimizations
[18:11] together means we kind of solve the
[18:15] problem of container call start and
[18:17] let's remember what why did we
[18:19] originally set out to start this thing
[18:20] is because we want to deliver good
[18:22] developer experience as it turns out
[18:26] it's good for other things too so
[18:28] container call start is also good
[18:30] because it enables serverless so what
[18:32] does serverless mean uh it means a lot
[18:34] of different things I think part of why
[18:37] sometimes I avoid the term seress is
[18:39] that has so many different definitions
[18:41] but the the promise of serverless was
[18:43] always don't provision more than you
[18:45] actually need just just you know
[18:48] only pay for capacitor you're actually
[18:51] using and so especially with gpus which
[18:54] are very expensive as it turns out you
[18:57] can pack take a lot of different users
[19:00] pull them together and give people
[19:03] dynamically the resources they need and
[19:06] get dramatically better
[19:08] utilization and so that in turn means we
[19:12] can get lower cost it means there's no
[19:14] capacity planning it it also because we
[19:17] can pull a lot of these users the the
[19:19] variance the the total variance goes
[19:21] down the relative variance uh which
[19:23] means we can run a much more predictable
[19:25] set of of resource pools the the total
[19:28] cap capacity that we run uh which is
[19:31] another problem by the way so we need to
[19:33] run thousands of gpus we use a lot of
[19:35] different Cloud vendors we use a lot of
[19:36] different regions we scale up and down
[19:38] continuously uh in fact we actually end
[19:40] up solving a mixed iner programming
[19:42] problem to to do this uh minimizing the
[19:45] total cost spend uh and and this is some
[19:48] of the stuff we have to do for for our
[19:49] customers so they don't have to think
[19:51] about it so through model you can come
[19:52] in and you can request 100 gpus under
[19:55] the hood there's enormous amount of work
[19:56] that we have to put in in order to get
[19:58] the capacity somewhere in the world uh
[20:01] you know spinning up gpus if needed uh
[20:04] but in many cases it happens
[20:05] instantaneously because we can maintain
[20:06] a buffer that makes it very fast to get
[20:08] access to these compute resources for
[20:10] any
[20:11] customer
[20:12] um this was very technical but just to
[20:15] kind of go back and look at a high level
[20:17] again uh why do people like modal people
[20:21] pick modal in because they can run their
[20:24] own code we're not an AI API so to speak
[20:27] you can run almost anything with modal
[20:30] uh we make it possible to iterate very
[20:31] quickly we're fully usage based so when
[20:34] you run things in modal you only pay for
[20:35] the time the containers are actually
[20:37] active you have to never think about
[20:39] capacity you don't have to you know go
[20:41] out and buy you know hundreds of gpus or
[20:44] thousands of gpus we can get you that
[20:46] within you know seconds or at least
[20:47] minutes uh so there's a lot of things
[20:49] the sort of burden of infrastructure
[20:52] building your own internal platform
[20:53] setting up kubernetes setting up you
[20:55] know Docker and all these things you
[20:57] don't have to think about this with
[20:59] model um how do you try model it's
[21:02] actually very simple uh you go to your
[21:03] terminal you do pip install model the
[21:05] the python client automatically you know
[21:08] configures itself to connect to uh modal
[21:11] and you can immediately start running
[21:12] stuff because we give everyone $30 a
[21:14] month uh per per month of free credits
[21:17] if you are a startup uh we can give you
[21:20] up to $50,000 in credits in order for
[21:22] you to get
[21:24] started thank you and I really hope you
[21:27] enjoy this
[21:29] and if you have any questions feel free
[21:30] to reach out Eric oto.com uh you can
[21:33] also follow me on Twitter bernhardson or
[21:35] check out my blog here at burn.com
