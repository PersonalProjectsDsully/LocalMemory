---
type: youtube
title: Fine tune 20 Llama Models in 5 Minutes: Santosh Radha
author: AI Engineer
video_id: zHYQZFy0UVk
video_url: https://www.youtube.com/watch?v=zHYQZFy0UVk
thumbnail_url: https://img.youtube.com/vi/zHYQZFy0UVk/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['model fine-tuning', 'Python automation', 'Covalent', 'machine learning', 'AI training', 'GPU optimization', 'cloud computing', 'ML pipelines', 'Llama models', 'AI deployment', 'resource management', 'Python scripting']
entities: ['Santosh Radha', 'Channel Video', 'Covalent', 'Llama Models', 'H100', 'L4', 'V00', 'Docker', 'Kubernetes', 'Python']
concepts: ['model fine-tuning', 'Pythonic workflow', 'cloud computing', 'machine learning optimization', 'automated model deployment', 'resource allocation', 'AI training', 'GPU utilization', 'machine learning pipelines']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Python programming skills', 'basic machine learning knowledge', 'familiarity with cloud computing concepts']
related_topics: ['machine learning', 'AI development', 'cloud computing', 'Python automation', 'GPU optimization', 'ML model deployment', 'AI training pipelines', 'devops for AI']
authority_signals: ['this is completely pythonic and once you dispatch this to our server', 'we have a booth over there do visit us and we can have more chat over there']
confidence_score: 0.8
---

# Fine tune 20 Llama Models in 5 Minutes: Santosh Radha

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=zHYQZFy0UVk)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: python, machine-learning, ai, deep-learning, fine-tuning, gpu, cloud-computing  

## Summary

# Summary of "Fine tune 20 Llama Models in 5 Minutes: Santosh Radha"

## Overview  
The video introduces **Covalent**, a tool designed to simplify fine-tuning machine learning models (e.g., Llama) directly from Python. It eliminates the need for complex infrastructure like Docker or Kubernetes, enabling users to run tasks on local or cloud resources with a Pythonic interface. The speaker demonstrates a workflow for fine-tuning, evaluating, and deploying models efficiently while emphasizing cost-effectiveness and scalability.

---

## Key Points  
- **Pythonic Workflow**: Users define tasks using decorators to specify compute resources (e.g., CPU, GPU types, memory) and orchestrate workflows with simple Python code.  
- **No Infrastructure Overhead**: Avoids Docker, Kubernetes, or manual resource management; tasks run on specified devices (e.g., H100, L4) with automated job scheduling.  
- **Cost Efficiency**: Charges based on actual usage (e.g., $0.87 for a 6-minute evaluation).  
- **Auto-Scaling & Deployment**: Supports dynamic scaling for inferences and deploys models via endpoints (e.g., `SL generate`).  
- **Example Workflow**:  
  - Loop through models, fine-tune, evaluate accuracy, sort results, and deploy the best model.  
  - Separates compute-intensive steps (e.g., fine-tuning) from CPU-based tasks (e.g., sorting).  

---

## Key Quotes/Insights  
- *"You don't dockerize, you don't run Kubernetes cluster."*  
- *"Cost is based on actual usage, not fixed resources."*  
- *"Deploy the best model without complex pipelines."*  

---

## Actionable Items  
1. **Use Decorators**: Specify compute requirements (e.g., GPU type, memory) for tasks.  
2. **Deploy with a Single Command**: Automate workflows for fine-tuning, evaluation, and deployment.  
3. **Define Auto-Scaling Rules**: Configure scaling for inference endpoints based on load.  
4. **Explore Examples**: Visit the provided link for use cases like time series analysis and LLM fine-tuning.  

--- 

*Note: The tool mentioned in the transcript appears to be **Covalent** (likely a typo in the speaker's name as "Calent").*

## Full Transcript

[00:03] [Music]
[00:13] so the talk is actually going to be
[00:15] about um uh how you run things extremely
[00:18] easy directly from Python and the
[00:21] example that I'm going to show you here
[00:22] is obviously I just have five minutes
[00:24] and on my end but I'm going to try my
[00:26] best to Showcase how you can fine tune
[00:28] pretty much 20 is an arbitrary number
[00:29] here but hundreds of models that you can
[00:31] do right from python without needing
[00:33] anything like kubernetes joer or
[00:35] anything on your side and uh so before
[00:37] that you can find the talk and the
[00:39] actual code for what I'm going to do in
[00:40] this QR code and you'll find lot more
[00:43] interesting examples over there to try
[00:45] out on run as well um okay so what do we
[00:48] do um so calent is an open source slop
[00:52] core uh product on its end and what we
[00:55] do is we help people write python
[00:58] locally and ship the code to any kind of
[01:00] compute backend that you need to send it
[01:02] to so what that means is hey you have a
[01:05] python function that you want to run on
[01:06] a GPU um in your local laptop open up a
[01:09] jupyter notebook add a single decorator
[01:11] on top to say hey I want to run this on
[01:13] h00 with 36 gigs of memory for 2 days
[01:16] maximum time limit and press shift enter
[01:18] in your Jupiter notebook and that's it
[01:21] the code gets shipped to a back end in a
[01:23] GPU and you get back the result on your
[01:25] side in in the open source case it sends
[01:27] it to your own compute you can attach
[01:29] your own compute class cluster and it
[01:30] runs over there in the cloud case it
[01:32] runs in our GPU cluster and you just pay
[01:34] for the GPU time that it runs in so it
[01:36] runs for 5 minutes you pay for 5 minutes
[01:38] of h00 it runs for 10 seconds you pay
[01:40] for 10 seconds of hunds on your side and
[01:42] you can also bring your own Compu and
[01:44] attached to us and we'll help you
[01:45] orchestrate the entire Compu that you're
[01:46] handling on your side be it your own
[01:48] cloud or on-prem systems or whatever it
[01:51] is on your end
[01:52] then okay so covalent basically has a
[01:55] bunch of perimeters that you define in
[01:57] you can submit in jobs which are called
[01:59] single functions so essentially all you
[02:01] need to do is as I said add a single
[02:03] decorator on top and say what is the
[02:05] computer that you need to ship it to it
[02:07] goes there it runs and you get back the
[02:09] python object back and you just pay for
[02:11] the function that you are running
[02:12] in we also let you run inferences and
[02:15] again it's completely pythonic you don't
[02:17] dockerize you don't run kubernetes
[02:19] cluster you don't do anything you just
[02:21] say hey I have an initializer function
[02:24] and I have a I need an endpoint called
[02:25] SL generate and you define your python
[02:28] functions you click a single cc. deploy
[02:31] command uh in your jupyter notebook the
[02:33] entire service gets shipped to us and we
[02:35] scale you get back an API endpoint that
[02:37] scales to zero or scales in its request
[02:39] as and when your new request comes in
[02:41] you can Define your Custom Auto scaling
[02:43] mechanism like hey I want to Auto scale
[02:45] it to 10 gpus exactly at 9:00 every day
[02:48] or I want to Auto scale whenever my GPU
[02:50] utilization hits in 80% or I want to
[02:52] Auto scale whenever the number of
[02:53] request I get in is thousand U so you
[02:56] can Define whatever Auto scaling you
[02:57] want you can Define authentication and
[02:59] everything and everything happens in the
[03:00] background for you you don't even touch
[03:02] a single code of kubernetes or Docker or
[03:04] anything on your
[03:06] side and the talk I'm going to give in
[03:09] is a very tiny example um of what we do
[03:12] from our side but if you go to this
[03:14] Linkin there's a whole host of examples
[03:17] uh that you can run in right from Real
[03:19] Time Time series analysis to uh you know
[03:23] using inverter Transformers for time
[03:24] series which is like a state-ofthe-art u
[03:26] time series Transformer on its end uh
[03:29] running inar systems um large language
[03:32] models on your serving uh systems and
[03:34] even building an entire AI model Foundry
[03:36] out of our just pure pythonic code on
[03:38] your side and so without further Ado
[03:41] I'll quickly run through the code
[03:44] example of how you do essentially
[03:46] fine-tune a bunch of huge set of models
[03:49] uh directly just from python on your end
[03:51] and I'll also show you how it looks like
[03:53] uh from the front side as well so um
[03:56] it's rather simple all you do is I have
[03:59] written a un of U normal pythonic
[04:02] training functions in my local package
[04:03] called fine tune and evaluate on our end
[04:06] and what we going to do is hey I'm going
[04:08] to define a python task which
[04:10] essentially calls in my fine tune
[04:11] function which is going to accept a
[04:12] model and data and return back a fine
[04:14] tune model so this is a simple python
[04:16] function and I'm going to say I want to
[04:18] run it on a 24 core CPU with one GPU in
[04:21] it of type h 100 with 48 gigs of memory
[04:24] and going to give a Max limit of 18
[04:26] hours on it and then I'm going to say
[04:28] I'm going to once the model is done I'm
[04:29] I'm going to accept the model and then
[04:30] evaluate its accuracy on its hand and
[04:33] finally I'm going to just sort the model
[04:36] among all the best models and then pick
[04:38] the best model in it and I want this to
[04:39] run on a CPU based machion I don't want
[04:41] to waste GPU for my sorting or whatever
[04:43] I'm going to do in on my end and finally
[04:46] I'm going to deploy the best model that
[04:48] I figured um and it's that has performed
[04:50] well on my end and this is again a
[04:52] simple decorative say hey this is my
[04:54] initialization service and I'm going to
[04:56] create a endpoint called SL generate um
[04:59] and and I'm going to generate the text
[05:01] and give back the
[05:03] prediction and finally this is where the
[05:05] magic happens to tie together all of
[05:07] these things what I do is I'm going to
[05:08] create a workflow where I'm pretty much
[05:10] just going to Simply Loop over a bunch
[05:12] of models to finetune call the fine tune
[05:15] function evaluate the task and get the
[05:17] accuracy make a list of all the models
[05:19] and accuracy sort the best models and
[05:22] then deploy the model from my end and
[05:24] this is completely pythonic and once you
[05:26] dispatch this to our server which is
[05:28] essentially calling single line over
[05:30] here what you will go back and see is a
[05:34] new job that creates in our application
[05:37] and all of the functions that you called
[05:39] will run in the respective devices that
[05:41] you just defined so for instance here is
[05:44] uh one of the evaluation step that ran
[05:46] in and it has its own machine that we
[05:48] ran in it ran in L4 it ran for 6 minutes
[05:53] and you get back just 87 cents to
[05:55] evaluate your model in another model ran
[05:57] in v00 on its end and it ran for 6
[06:01] minutes again it cost 11 cents to do it
[06:03] in and in total you finally have
[06:06] deployed try fine tuned untrained
[06:08] completely in Python without needing
[06:10] anything like Docker or kubernetes on
[06:12] your end and we have a booth over there
[06:14] do visit us and we can have more chat
[06:16] over there thank you guys
[06:19] [Music]
