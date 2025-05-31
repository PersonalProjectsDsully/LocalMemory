---
type: youtube
title: LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella
author: Channel Video
video_id: 2Wtq2GvUicw
video_url: https://www.youtube.com/watch?v=2Wtq2GvUicw
thumbnail_url: https://img.youtube.com/vi/2Wtq2GvUicw/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['LLM fine-tuning', 'cost optimization', 'prompt engineering', 'model deployment', 'AI scalability', 'retrieval augmented generation', 'open-source models', 'machine learning optimization', 'AI tooling', 'large language models', 'model efficiency', 'AI deployment']
entities: ['Open Pipe', 'Octo AI', 'LLM', 'GPT-4 Turbo', 'Llama 3', 'prompt engineering', 'retrieval augmented generation', 'model optimization', 'crawl-walk-run', 'cost efficiency']
concepts: ['fine-tuning', 'prompt engineering', 'retrieval augmented generation', 'cost efficiency', 'model optimization', 'crawl-walk-run approach', 'large language models', 'deployment scalability', 'accuracy improvement', 'open-source models']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic understanding of large language models (LLMs)', 'Familiarity with prompt engineering techniques', 'Knowledge of AI model deployment concepts']
related_topics: ['Machine Learning Optimization', 'Natural Language Processing', 'AI Deployment Strategies', 'Cost Reduction in AI', 'Model Training Techniques', 'Open Source AI Tools', 'Prompt Engineering Best Practices', 'AI Infrastructure Scaling']
authority_signals: ['I work at Octo AI here for the llm deployment', "we're going to be able to show that we can achieve 47% better accuracy", '99.5% reduction in cost this is really a 200x reduction in cost']
confidence_score: 0.8
---

# LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=2Wtq2GvUicw)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llm fine-tuning, ai engineering, model optimization, machine learning, deep learning, deployment, model training  

## Summary

```markdown
# LLM Quality Optimization Bootcamp Summary

## Overview
This session, led by Thierry Moreau (co-founder at Octo AAI), addresses two critical pain points in LLM fine-tuning: high generation costs and difficulty meeting quality thresholds for production. The talk emphasizes a structured approach to quality optimization, highlighting the **crawl-walk-run** framework and a continuous deployment cycle. It also showcases practical tools and results for improving accuracy and cost efficiency.

---

## Key Points

### 1. **Crawl-Walk-Run Framework**
   - **Crawl**: Start with **prompt engineering** (e.g., specificity, few-shot prompting, Chain of Thought) to optimize model outputs without code changes.
   - **Walk**: Introduce **Retrieval-Augmented Generation (RAG)** to enhance context and accuracy.
   - **Run**: Use **fine-tuning** as a final step for significant quality improvements, but only after exhausting simpler methods.

### 2. **Continuous Deployment Cycle**
   - **Data Collection**: Curate and preprocess datasets for fine-tuning.
   - **Fine-Tuning**: Use tools like **OpenPipe** (SaaS for low-barrier fine-tuning) to improve model performance.
   - **Deployment**: Leverage **Octo AI** for scalable, cost-efficient model serving.
   - **Evaluation**: Continuously test and iterate on results.

### 3. **Use Case: PII Redaction**
   - Demonstrated a **47% accuracy improvement** using OpenPipe fine-tuning.
   - Achieved **99.5% cost reduction** (200x) by deploying on Octo AI, leveraging a smaller open-source model optimized for scale.

### 4. **Key Takeaways**
   - Fine-tuning is **not a silver bullet** but a critical tool in the optimization pipeline.
   - Prioritize prompt engineering and RAG before investing in fine-tuning.
   - Tools like OpenPipe and Octo AI enable accessible, cost-effective solutions for production-grade LLMs.

---

## Tools & Results
- **OpenPipe**: SaaS for fine-tuning, eliminating the need for hardware/cloud instances.
- **Octo AI**: Optimized for large-scale model deployment, reducing costs significantly.
- **Results**: 
  - 47% accuracy improvement on PII redaction.
  - 99.5% cost reduction (from GP4 Turbo to Llama 3) via smaller, optimized models.
```

## Full Transcript

[00:00] [Music]
[00:13] so welcome everyone thanks for making it
[00:15] to this lunch and learn uh my goal today
[00:18] is to make sure that I get to uh share
[00:21] my knowledge and experience on llm
[00:24] fine-tuning uh just to get a quick sort
[00:28] of pull from the audience here
[00:30] how many of you are have heard of the
[00:33] concept of fine-tuning here okay so
[00:36] quite a few people how many of you have
[00:37] actually had hands-on experience in
[00:39] fine-tuning
[00:41] llms okay all right that's pretty good
[00:44] uh that's more than I'm usually used to
[00:46] I mean this is quite a fantastic that in
[00:48] this conference the makeup of AI
[00:50] engineer is close to 100% that's not a
[00:53] something I'm generally used to when
[00:55] presenting at other you know hackathons
[00:58] and conferences so I feel like I'm I'm
[01:00] speaking to the right crowd so just to
[01:04] kind of contextualize this talk really
[01:06] I'm trying to address two pains that a
[01:10] lot of gen Engineers face and to get a
[01:14] sense of where you are in your journey
[01:16] how many really identify and can relate
[01:18] to the first one which is my gen spin
[01:21] has gone through the
[01:23] roof okay yeah all right and how many of
[01:26] you are in this other segment of this
[01:29] journey which is is you know you've
[01:31] built pcc's it's showing promise but you
[01:34] haven't yet quite met this quality bar
[01:37] to go to production can I get a sense of
[01:40] all right so so I think you know we have
[01:43] a good amount of a good fraction of the
[01:45] audience that can relate to one of these
[01:46] two problems uh myself I'm a co-founder
[01:49] at octo aai and I'm going to talk a
[01:52] little bit more about what we do but the
[01:54] customers I've been working with they
[01:56] feel those pains in very real way or
[01:59] talking about 10 of thousands if not
[02:01] hundreds of thousands of dollars in
[02:02] monthly
[02:04] bills and perhaps even having issues
[02:08] trying to go to production because the
[02:09] quality bar hasn't yet been
[02:11] met so the overview of this uh 50-minute
[02:14] talk uh is going to be spent on
[02:17] understanding the why of fine tuning
[02:19] really try to understand when to use
[02:21] fine-tuning it's not really a silver
[02:23] bullet for all the problems you're going
[02:24] to face but one used right in the right
[02:27] context for the right problem it can
[02:29] really deliver results I'm also going to
[02:32] try to contextualize this notion of
[02:33] fine-tuning within the crawl walk and
[02:36] run of llm quality optimization because
[02:39] there's different techniques that you
[02:41] should attempt before trying to do fine
[02:42] tuning but finally when you're convinced
[02:45] that this is the right thing for you I'm
[02:47] going to talk about this continuous
[02:48] deployment cycle of fine-tuned llms so
[02:52] we're going to go through today over a
[02:54] whole crank of that wheel of this
[02:56] deployment cycle composed of you know
[02:59] model uh you know data set collection
[03:01] model fine-tuning deployment and
[03:04] evaluation and really I'm trying to
[03:06] demystify this whole journey to you all
[03:09] because in the next 15 minutes we're
[03:10] actually going to go through this whole
[03:11] process and hopefully that's something
[03:12] that you're going to feel comfortable
[03:13] going through and you know applying to
[03:16] your own data set to your own problems
[03:18] and so for illustrating today's use case
[03:20] we're going to use this uh personally
[03:23] identifiable information redaction use
[03:25] case now that's a pretty traditional
[03:27] sort of data scrubbing type of uh
[03:29] application but we're going to use llms
[03:31] and we're going to see that we can
[03:32] essentially achieve stateof VR accuracy
[03:35] while keeping efficiency at at the
[03:39] highest uh using essentially very
[03:41] compact very lightweight models that
[03:43] have been fine-tuned for that very task
[03:46] so again trying to motivate this talk
[03:49] what limits gen adoption in most
[03:51] businesses today based on the
[03:52] conversations that I've had in the field
[03:54] discussion I've had with customers and
[03:56] developers the first one is there's a
[03:58] limited availability
[04:00] of gpus I think we're all familiar with
[04:02] this problem it's one of the reasons why
[04:04] Nvidia is so successful lately I mean
[04:07] everyone wants to have access to those
[04:10] precious resources that allow us to run
[04:12] gen at scale and that can also Drive
[04:15] costs up right so we have to be smart
[04:17] about how to use those GPU
[04:19] resources and also uh when people build
[04:22] poc's it displays and shows promise but
[04:26] sometimes you don't reach the expected
[04:28] quality bar to go to production
[04:30] and so on this XY axis you know on this
[04:33] chart where y AIS is cost and the x-axis
[04:37] symbolizes quality maybe many people
[04:41] start uh on that Green Cross here right
[04:43] on this upper quadrant of very high cost
[04:47] maybe not having met the quality bar
[04:48] that's your first po but really to go to
[04:51] production you need to end on the
[04:53] opposite quadrant right lower cost
[04:55] higher quality where you met the bar
[04:57] you're able to run this in a way that
[05:00] essentially is margin positive and many
[05:03] of us are on this journey to reach that
[05:05] point of uh you know
[05:07] profitability so we're going to learn
[05:10] today how to use and how to fine-tune an
[05:13] llm now fine-tuning is a method that
[05:15] we're going to use to improve the llm
[05:17] quality but as a bonus we're going to be
[05:20] also showing how to improve quality
[05:23] significantly and I use quality as the
[05:25] title of this talk because really I
[05:27] think many of us AI Engineers really
[05:29] care about reaching the high quality bar
[05:32] when we're using llms and hopefully I'm
[05:34] you know the goal of today's talk is to
[05:36] instill you some knowledge on how to
[05:38] tackle this journey and so in terms of
[05:41] tools that we're going to use today
[05:42] we're going to use open pipe which is a
[05:45] SAS solution for fine-tuning that really
[05:48] lowers the bar of entry for people to
[05:50] run their own fine tunes uh you don't
[05:52] need Hardware or Cloud instances to get
[05:54] started and we're going to use this to
[05:57] deliver quality improvements over stere
[05:59] ofthe art llms and of course since I
[06:01] work at octo aai I'm going to also be
[06:03] using octo AI here for the llm
[06:05] deployment and that's going to be the
[06:07] solution that we're going to use to
[06:09] achieve cost efficiency at scale and
[06:13] really the the key here is to be able to
[06:15] build on a solution that is designed to
[06:18] serve models at production scale
[06:22] volumes and just to give you a little
[06:24] bit of a sneak peek in terms of the
[06:26] results that we're going to Showcase
[06:27] today after you go through this whole
[06:29] tutorial and this is something that
[06:31] you're going to be able to reproduce
[06:32] independently so you know all the code
[06:34] is there for you to go through we're
[06:36] going to be able to show that we can
[06:37] achieve 47% better accuracy at the task
[06:41] that I'm going to Showcase today using
[06:43] this open pipe fine-tuning and by
[06:45] deploying the model on octo AI we're
[06:48] going to achieve this I mean it seems
[06:50] kind of ridiculous
[06:52] 99.5% reduction in cost this is really a
[06:55] 200x reduction in cost here from a gp4
[06:58] turbo to llama three and mostly because
[07:01] this is a much smaller model it's open
[07:03] source and we've optimized the hell of
[07:05] this model to serve it cheaply on ooto
[07:07] AI so I'm going to explain how this is
[07:09] achieved but I hope your interest at
[07:11] least has been peaked on those results
[07:13] that you yourself can
[07:15] reproduce so when to use fine-tuning uh
[07:19] again it's not really a silver bullet
[07:21] for all your quality problems it has its
[07:23] right place and time so I like to
[07:25] contextualize it within the crawl walk
[07:27] run of quality optim ization right and
[07:30] as gen Engineers uh many of us have
[07:33] embarked on this journey we're at
[07:35] different stages of this journey and
[07:37] really it should always start with
[07:39] prompt engineering right and many of you
[07:40] are familiar with this concept you start
[07:43] with a model you're trying to have it
[07:45] accomplish a task and sometimes you
[07:47] don't really manage to see the result
[07:48] you expect to see so you're going to try
[07:51] prompt engineering and there's different
[07:52] techniques of varying levels of
[07:54] sophistication uh this talk is not about
[07:56] prompt engineering so you know you can
[07:58] improve prompt specificity there's few
[08:00] shots prompting where you can provide
[08:02] examples uh to improve essentially the
[08:05] quality of your output there's also
[08:06] Chain of Thought prompting I mean some
[08:08] of you probably have heard these
[08:09] Concepts but this is where you should
[08:11] get started right make sure that given
[08:12] the model given those weights you just
[08:14] try to improve the prompt to get the
[08:16] right results sometimes that's not
[08:18] enough and uh there's a second class of
[08:21] solutions which I like to map to the
[08:23] walk stage um retrieval augmented
[08:26] generation right we've probably seen a
[08:27] lot of talks on rag today and throughout
[08:30] this conference so you know there's
[08:32] hallucinated results sometimes the
[08:34] answer is not truthful well why is that
[08:36] it's because the um the weights of the
[08:39] model that is really the parametric
[08:41] memory of your model is limited to you
[08:45] know the point and time at which the
[08:46] model was trained so when you try to ask
[08:49] questions on data it hasn't seen or
[08:52] information that's more recent than when
[08:53] the model was trained it's not going to
[08:55] know how to respond right so the key
[08:57] here is to provide the right amount of
[08:58] context
[09:00] and so this is achieved through uh
[09:02] similarity search for instance in a
[09:03] vector database through function calling
[09:05] to bring the right context by invoking
[09:07] an API through search uh through
[09:10] creating a database and so this is
[09:12] something that I think many of us a
[09:13] Engineers have been dabbing in in order
[09:16] to provide the right context to generate
[09:18] truthful answer right complement the
[09:20] parametric memory of your model with
[09:21] non-parametric information and that's
[09:24] rag in a nutshell right so you've tried
[09:26] prompt engineering you've tried rag
[09:27] you've eliminated quality problems and
[09:29] hallucinations but that's still not
[09:31] enough right so what do you try next
[09:34] well fine tuning I think is uh the next
[09:37] stage and again I'm generalizing a very
[09:39] complicated and complex Journey but in
[09:41] spite of your best efforts you've tried
[09:43] these techniques for maybe days weeks or
[09:45] even months and you still don't get to
[09:47] where you need to be to hit production
[09:50] and we're going to talk about this
[09:51] journey today right fine tuning so when
[09:54] should you f tun a model uh again after
[09:58] you spend a lot of time in the first two
[09:59] phases of this journey so spending time
[10:02] on prompt engineering spending time on
[10:04] retrieval augmented generation and you
[10:06] don't see the results improve and
[10:10] generally what helps is whenever you use
[10:12] an llm for a very specific task
[10:14] something that's very focused for
[10:16] instance classification information
[10:18] extraction uh trying to format a prompt
[10:20] using it for function calling if you can
[10:23] narrow the use case uh to something that
[10:26] is highly specific then you have an
[10:28] interesting use case for for um for
[10:30] applying fine-tuning here and another
[10:33] requirement is to have a lot of your own
[10:35] high quality data to work with because
[10:37] that's going to be our fine-tuning data
[10:38] set that goes without saying but a model
[10:41] is only as good as the data that it that
[10:43] the model was trained on and we're going
[10:45] to apply this principle here in this
[10:47] tutorial and finally I think as an added
[10:49] incentive oftentimes we're all driven by
[10:51] economic incentive in the work we do for
[10:54] those of you who are feeling the Pains
[10:56] of uh High gen bill whether it is with
[11:00] open AI or with a cloud vendor or a
[11:03] third party well this is generally a
[11:05] good reason to explore fine tuning so
[11:08] we're going to go over all the steps now
[11:10] that we've kind of contextualized why
[11:12] fine tuning and when to consider fine
[11:14] tuning we're going to consider all the
[11:16] steps here in this continuous deployment
[11:19] cycle it starts with building your data
[11:21] set then running the fine-tuning of the
[11:24] model deploying that fine-tuned llm into
[11:27] production so you can achieve scale and
[11:29] serve your your you know your customer
[11:32] needs or internal needs add High volumes
[11:35] and also evaluate quality and this is an
[11:38] iterative process there's not a single
[11:39] crank of the wheel this is not a fire
[11:41] and forget situation because data that
[11:45] your model sees in production is going
[11:46] to drift and evolve and so this is
[11:48] something that you're going to have to
[11:49] monitor you're going to have to update
[11:50] your data set you're going to have to
[11:52] fine-tune your model and I don't want to
[11:54] scare you away from doing this because
[11:55] it sounds fairly daunting and so by the
[11:58] end of this talk will have gone through
[12:01] a full crank of that wheel and hopefully
[12:04] you know it through these SAS toolings
[12:07] I'm going to introduce you to is going
[12:08] to feel a lot more approachable and
[12:10] hopefully I'll demystify the whole
[12:12] process of fine-tuning models so let's
[12:15] start with step one which is to build a
[12:17] fine-tuning data set now the data of the
[12:20] model has to be trained on ideally real
[12:23] world uh data right it has to be as
[12:26] close as possible to what you're going
[12:27] to see in production so kind of a
[12:29] spectrum of ways to build and generate a
[12:31] data set ideally you build a data set
[12:35] out of real world prompts and real world
[12:37] generated uh real world human responses
[12:40] so for instance you have customer
[12:42] service you've loged calls with a
[12:43] customer agent you have an interaction
[12:45] between two humans that's a very good
[12:47] data set to work with right because it's
[12:49] human generated on both ends this is
[12:51] very high quality but not everyone has
[12:53] the ability to acquire this data set
[12:56] sometimes you're starting from scratch
[12:57] so not everyone has a luxury to start
[13:00] there there's also kind of an
[13:01] intermediary between real world and
[13:03] synthetic where you have real world
[13:05] prompts but AI generated responses and
[13:08] so this is kind of a good middle ground
[13:09] between cost and quality because you're
[13:11] starting from actual uh ground troof
[13:14] information that is derived from real
[13:17] data but the responses are generated by
[13:20] a highquality llm say gp4 or clawed and
[13:24] actually open pipe is a solution that
[13:26] allows you to log the inputs and outputs
[13:28] of an El M like gp4 to build your data
[13:31] set for fine-tuning an llm so this is
[13:34] something that you know a lot of
[13:36] practitioners use and finally there's a
[13:38] fully synthetic data set using fully AI
[13:42] generated labels and often times when
[13:45] you go on hugging face or kaggle you'll
[13:47] encounter data sets that have been built
[13:49] entirely synthetically and that's a
[13:51] great way to kind of get started on this
[13:53] journey and actually one of the data
[13:54] sets we're going to use today is uh from
[13:57] that latter category
[14:00] and of course I mean it probably goes
[14:01] without saying but in case people are
[14:03] not fully uh familiar with this notion
[14:05] you want to split your data set into a
[14:07] training and validation um set because
[14:10] you don't want to evaluate your model on
[14:12] data that your um fine-tune has seen
[14:16] right and so many of you who are ML and
[14:19] AI Engineers are already familiar with
[14:21] this but I just want to reiterate that
[14:22] this is important and finally you know
[14:24] this is used for hyperparameter tuning
[14:26] and when you're deploying it and
[14:27] actually testing it on real examples you
[14:29] want to have a third set outside of
[14:32] training and validation which is your
[14:34] test
[14:34] set now you've built your data set
[14:37] you're ready to fine-tune your model and
[14:39] there's a lot of decisions that we need
[14:40] to make at this point and the first one
[14:43] is going to be open source versus closed
[14:44] Source right and so who here just like
[14:47] raise of hands is using proprietary llms
[14:50] or gen models today from open AI
[14:53] anthropic mstr AI okay good amount of
[14:57] crowd who here has been using
[14:59] open-source llms like llama some of the
[15:02] free mraw AI models okay so maybe a
[15:06] smaller crowd right and maybe that's
[15:08] because these models are not as capable
[15:10] and
[15:11] sophisticated and but I'm going to walk
[15:14] you through how you can achieve better
[15:17] results if you do fine tuning right so
[15:20] of course the benefit of Open Source and
[15:22] this is why you know I'm I'm obviously
[15:23] biased but I'm an open source Advocate
[15:26] is that you have to you get to have
[15:28] ownership over model weights so when
[15:30] once you've done the fine tuning you are
[15:33] the proprietor of the weights that are
[15:35] the result of this fine tuning process
[15:38] which means that you can choose how you
[15:39] deploy it how you serve it this is part
[15:40] of your IP and I find that this is a
[15:42] great thing for anyone who wants to
[15:45] Embark in this fine-tuning journey with
[15:47] proprietary Solutions you're not quite
[15:49] the owner or you don't have the
[15:51] flexibility to decide to go with another
[15:53] vendor to host the the the models
[15:55] yourself and so you're kind of locked
[15:57] into an ecosystem some people are
[15:59] comfortable with that others are less
[16:01] comfortable with it and many of the
[16:02] customers that we talk to they're very
[16:04] eager to jump on the open source train
[16:06] but they don't really know how to get
[16:08] started or uh you know where to start on
[16:11] this journey so hopefully this can this
[16:13] can help inform you how to take your
[16:15] first steps here into the world of Open
[16:17] Source then there's a question of like
[16:19] do I use a small model or a large model
[16:22] because for instance even in the world
[16:23] of Open Source you have models that are
[16:25] in the order of8 billion parameters like
[16:27] llama
[16:27] 38b and then you have the large models
[16:30] with a mix draw 8X 22b so this is a
[16:33] mixture of expert model with over 100
[16:35] billion parameters uh very different
[16:37] beasts and we're going to see even
[16:39] larger models from meta and generally my
[16:42] recommendations here is well look the
[16:44] large models are amazing they have
[16:46] broader Contex Windows they have higher
[16:49] capabilities at reasoning but they're
[16:52] also more expensive to fine tune and
[16:53] more expensive to serve and typically
[16:56] when you have to do a deployment you're
[16:57] going to have to acquire resources like
[16:59] h100s to run these models so generally
[17:02] start with a smaller model like a llama
[17:03] 3B and sometimes you'll be surprised by
[17:06] its ability to learn specific problems
[17:09] so that's my recommendation start with a
[17:13] smaller Llama 38b Or mistol 7B and if
[17:17] that doesn't work out for you then move
[17:18] towards uh larger and larger models and
[17:21] today we're going to be using this llama
[17:22] 38 billon parameter
[17:24] model there's also different techniques
[17:27] for fine-tuning and I'm going to go over
[17:28] this one fairly quickly but there's two
[17:31] classes of of fine-tuning techniques one
[17:34] which is parameter efficient fine-tuning
[17:37] it produces a Laura and the other one is
[17:39] a full parameter fine tuning which
[17:41] produces a checkpoint a Laura is much
[17:44] more much smaller and efficient in terms
[17:46] of memory footprint we're talking about
[17:48] 50 megabytes versus a checkpoint that is
[17:51] 15 gigabytes and so you can guess that
[17:55] because of its more compact
[17:57] representation
[17:59] you're able to serve it on a
[18:01] GPU that doesn't require as much onboard
[18:03] memory and you can even serve multiple
[18:06] lauras at the same time so multiple fine
[18:09] tunes on a GPU for inference as opposed
[18:13] to the checkpoints which require
[18:14] dedicated GPU for every single fine tune
[18:18] so there's more flexibility in
[18:19] deployment and we're going to use that
[18:20] today we're actually going to serve
[18:22] these luras which are the result of
[18:24] parameter efficient fine tuning on a
[18:26] shirt tendency endpoint with other users
[18:29] who have their own luras all running on
[18:31] the same server and that allows us to
[18:34] really reduce the cost of inference and
[18:38] there is a benefit to checkpoints though
[18:40] and full parameter fine tuning which is
[18:42] that there are more parameters to tune
[18:44] so it's a more flexible uh fine-tuning
[18:47] technique it allows the model to have
[18:50] essentially achieve uh better results at
[18:53] more expensive tasks like logical
[18:56] reasoning but for very specialized task
[18:58] which is we going to look at today like
[19:00] classification or labeling or function
[19:02] calling a Laura is just fine so we're
[19:04] going to use parameter efficient fine
[19:06] tuning and also when you're doing fine
[19:09] tuning you have to decide am I going to
[19:11] DIY it or am I going to use SAS so I'm
[19:13] sure some of you only like to diy things
[19:16] others like the convenience of SAS and
[19:18] here I'm not going to take a side I
[19:20] think there's some great tools right now
[19:21] to DIY your own fine-tuning uh for
[19:24] instance the open source uh project Axel
[19:27] and actually at the conference there's
[19:29] the the Creator behind Axel AEL who you
[19:31] might be able to catch um and you know
[19:35] the challenge here is that you have to
[19:36] find your own GPU resources you have to
[19:39] understand how to use these libraries
[19:41] even though they're they're they're
[19:42] easier than ever uh to to adopt and you
[19:45] have to tune and Tinker uh you know
[19:48] settings and hyperparameters then
[19:50] there's SAS which really aim to make it
[19:52] easy to embark on this journey companies
[19:54] like open pipe and there's U many folks
[19:57] from the open pipe at this conference
[19:59] today so if you can catch them please do
[20:01] talk to them and they're trying to lower
[20:03] the be of Entry to F tuning right to
[20:05] make it easy and they bring all this
[20:07] tooling all these libraries to make it
[20:08] as seamless as possible to for instance
[20:10] move from a gbd4 model to a fine-tune
[20:13] with as the least amount of steps in in
[20:15] collecting your data fine-tuning Etc and
[20:17] so we're going to use SAS today but if
[20:19] you feel more comfortable in this
[20:21] journey uh you might want to start with
[20:23] SAS and then evolve into diying
[20:26] it when it comes to deployment you have
[20:28] to navigate the same options right once
[20:30] you have the fine tune model now you
[20:31] need to decide well how am I going to
[20:32] serve it right because I need to
[20:34] generate maybe thousands millions or
[20:37] billions of tokens a day and so you need
[20:39] infrastructure you need gpus you need
[20:41] inference libraries some people like to
[20:43] DIY it using libraries like VM MLM
[20:47] tensor
[20:48] rtlm hogging face TGI if these are all
[20:52] things that you might have heard of uh
[20:54] these are all solutions to
[20:56] run models on your own on your own
[21:00] infrastructure but you need to provision
[21:02] the resources you need to build the
[21:04] infrastructure to scale with demand and
[21:06] that can get tricky especially achieving
[21:09] High reliability under load that's a
[21:11] challenge that many people face as they
[21:13] scale their business up with SAS you can
[21:16] essentially work with a third party like
[21:18] octo aai and obviously I'm a bit biased
[21:20] again I work there so I'm going to
[21:23] insert a Shameless plug for octo AI
[21:25] which allows users to get these fine
[21:28] deployed on SAS based endpoints so
[21:32] endpoints very similar to the ones from
[21:33] open AI for instance if you're familiar
[21:35] with that or
[21:37] Claude and uh it offers the ability to
[21:40] serve different kinds of customizations
[21:42] as well and so very quickly I want to go
[21:45] over the advantages of octo AI here
[21:48] first of all you get speed so llama 38
[21:51] billion peret model you get achieve
[21:53] around 150 tokens per second and we keep
[21:55] on improving that number because we've
[21:57] been applying our own in-house
[21:58] optimizations to the model serving layer
[22:01] it also has a significant cost Advantage
[22:04] because it costs about 15 cents per
[22:06] million tokens compared to say gp4 which
[22:09] cost $30 per million tokens so that's
[22:11] where the 200x comes from and we don't
[22:13] charge a tax for customization so
[22:15] whether you're serving the base model or
[22:17] a fine tune it's the same cost there's
[22:20] customization as I mentioned you can
[22:22] load your own Laura and serve it and
[22:25] finally scale our customer some of our
[22:27] customers generate up to to uh billions
[22:29] of tokens per day on our endpoints I
[22:31] think we're serving around over 20
[22:33] billion tokens per day and so we've
[22:36] focused and spent a lot of time on
[22:38] improving robustness and also worth
[22:41] mentioning if SAS doesn't cut it for you
[22:45] you are working for a Fortune 500
[22:48] company or you know a Healthcare Company
[22:51] a banking sector government you need to
[22:53] deploy your llms inside of your
[22:55] environment either on Prem or in VPC we
[22:58] also have a solution called octo stack
[23:00] come talk to us at the boof so that's it
[23:03] for the Shameless uh plug section let's
[23:05] go over to section four which is
[23:07] evaluating quality right we've talked
[23:09] about data set collection fine-tuning
[23:11] deployment now quality evaluation and we
[23:14] could have an entire conference just
[23:15] dedicated on that I'm going to try to
[23:17] summarize it into kind of two classes of
[23:20] evaluation techniques that I've
[23:22] seen first of all you know can your
[23:25] quality be evaluated in a precise way
[23:28] that can be automated for instance
[23:29] you're generating a program or SQL
[23:31] command that can run uh can you for
[23:34] instance label or extract information or
[23:37] classify information in an accurate way
[23:39] that's a kind of pass orfill scenario
[23:41] right or formatting the output into a
[23:44] specific Json formatting this is
[23:46] something that you can easily test as a
[23:48] pass or fail test and then there's more
[23:50] of the soft evaluation for instance if I
[23:52] were to take an answer and say well
[23:55] which output is written in a more polite
[23:56] or professional way you can't really
[23:59] write a program to evaluate this unless
[24:01] you're using an llm of course right but
[24:03] you have to put yourself into maybe 2
[24:06] 200 sorry 2020 2021 mindset before GPT
[24:10] was around well it' be hard to build a
[24:13] program that can assess this right so
[24:15] generally you need a human in the loop
[24:16] to say which out of out of a or b is a
[24:19] better
[24:20] answer thankfully today we can use llms
[24:23] to automate that evaluation but keep in
[24:25] mind that for instance if you're using
[24:27] gp4 to evaluate two answers well if
[24:30] you're compare against GPT 4 it might
[24:32] favor its own answer and people have
[24:34] seen that in these kind of evaluations
[24:36] so this is a whole science I mean we
[24:38] could have a whole conference just on
[24:39] this I just wanted to present the
[24:41] highlevel uh guidelines of this whole
[24:44] cycle of deploying fine-tune llms and so
[24:48] really there is no Finish Line that's
[24:49] what I want to convey to you all that
[24:53] going through a single iteration is
[24:55] something that you might have to do on a
[24:56] regular basis Maybe once a week maybe
[24:59] once a year it all depends on your use
[25:02] case and
[25:04] constraints now let's get a bit more
[25:07] practical let's switch over to our demo
[25:10] and so for those of you who came uh a
[25:12] little bit late there's a QR code here
[25:15] that you can scan and that will point
[25:17] you to our Google collab and we also
[25:21] have under
[25:23] slack let me see if I can pull it if
[25:26] you're in the slack channel for AI
[25:29] Engineers World Fair there is this uh
[25:31] quality optimization boot camp where you
[25:33] can ask questions here if you want to
[25:35] follow along and so we're going to go
[25:37] we're going to try to go over the uh
[25:39] practical component in the next 25
[25:41] minutes I just want to provide some
[25:44] context here the use case is uh
[25:46] personally identifiable information
[25:49] redaction we've taken this from a data
[25:52] set composed by AI for privacy called Pi
[25:55] masking 200k it's one of the largest
[25:57] data sets of its kind it has 54
[26:01] different pii classes so different kinds
[26:03] of sensitive data like the name the uh
[26:06] email address ad you know address of
[26:09] physical address of someone uh their
[26:11] credit card information etc etc across
[26:15] 229 discussion subjects so that includes
[26:18] conversations from customer ticket
[26:20] resolution conversations with a banker
[26:23] conversations between individuals Etc
[26:26] what this data set looks like is as
[26:28] follows you're going to have a message
[26:31] an email uh here we have you know
[26:34] something that looks like it came out of
[26:35] an email that contains credit card
[26:38] information IP address maybe even a
[26:41] mention of a role or or anything that is
[26:43] essentially personally personally
[26:46] identifiable and I've highlighted those
[26:48] in red because they will need to be
[26:51] redacted and after redaction we should
[26:53] get the following text that shows look
[26:56] here is this information that is now red
[26:58] rected anonymize but instead of just
[27:00] masking it we're actually telling it
[27:02] what kind of category this information
[27:04] belongs to right a credit card number an
[27:07] IP address or job title and this is how
[27:09] we're going to redact this text so where
[27:12] do llms come in the way we would use it
[27:15] is through function calling who here has
[27:18] used llms with tool calls or function
[27:21] calls okay so quite a few people you
[27:24] know and um as as many of us are aware
[27:26] this kind of what a lot of the agentic
[27:30] applications so this is a great use case
[27:32] for people who want to do function
[27:33] calling and are not seeing the results
[27:36] you know out of the box from say
[27:38] gp4 uh that they would like to to to see
[27:41] and in this case we're actually going to
[27:42] see that that these kind of state of the
[27:44] models are doing quite well at fairly
[27:46] large uh and complex function call use
[27:49] cases uh so to achieve this a redaction
[27:52] use case we're going to pass in a system
[27:54] prompt we're going to also pass in a
[27:57] tool specification the system prompt
[27:59] says look you're an expert model trained
[28:00] to do redaction and you can call this
[28:02] function here are all the sensitive uh
[28:05] pii categories for you to
[28:07] redact and then as a user prompt we're
[28:09] going to pass in that email or that
[28:12] message and then the output is a tools
[28:14] call so it's not the redacted text it's
[28:18] actually a tools call to that redact
[28:20] function that's going to contain all the
[28:22] arguments for us to perform the
[28:24] redaction why am I doing this as opposed
[28:26] to spitting out the redactive test well
[28:28] that gives us flexibility in terms of
[28:30] how we want to redact this text we could
[28:32] choose to just replace that information
[28:35] with the pii class we could also
[28:38] completely aisc it or we could choose to
[28:41] use for instance a database that Maps
[28:44] each pii entry to a fake substitute so
[28:48] that we have an email that kind of reads
[28:50] normally except the credit card the the
[28:53] the names the addresses are all made up
[28:56] but they will always map to the same
[28:58] individual and so that allows us to do
[29:00] then more interesting processing on our
[29:01] data set right so that's why we're going
[29:04] to use function calling here and let's
[29:07] start to build the data set so I'm going
[29:08] to switch over to our notebook here uh
[29:11] this notebook is meant to be sort of uh
[29:13] self explainable so there's a bit of
[29:15] redundance redundant context as part of
[29:18] the prerequisites you're going to have
[29:20] to get an account on octo and open pipe
[29:23] um and and these are the tools that
[29:25] we're going to use and if you want to
[29:26] run the evaluation function also provide
[29:28] your open AI key because we're going to
[29:31] compare against
[29:32] gp4 so we're going to install the python
[29:35] packages initially only open Ai and data
[29:37] sets from hugging face you can ignore
[29:39] this uh pip dependency error here uh
[29:42] which happens when you pip install data
[29:44] sets in a collab notebook but that's
[29:47] okay we can get past that you can enter
[29:49] your octo AI token and open AI API key
[29:52] at the beginning and I've already done
[29:55] this so we're going to start with the
[29:56] first phase which is to build a
[29:58] fine-tuning data set so we have this Pi
[30:01] masking data set I'm going to show it
[30:03] from hugging face so Pi uh masking and
[30:07] you can see what the data set looks like
[30:09] it has the source text information as
[30:12] you can see these are you know exchange
[30:14] you know Snippets from emails for
[30:16] instance you have the target text that
[30:18] is redacted and the Privacy mask that
[30:20] contains each one of the pii and the
[30:23] classes Associated to it so this
[30:25] contains all the data all the
[30:27] information in put and labels that we
[30:29] need to build our uh our data set for
[30:32] fine tuning and so really what we're
[30:35] going to
[30:36] do is that we're going to use the system
[30:40] prompt here we're going to Define our
[30:42] system prompt here which is again
[30:44] telling the model you're an expert model
[30:46] trained to redact information and here
[30:49] are the 56 categories explaining next to
[30:52] each category what that corresponds to
[30:55] and this is really the beauty of llm and
[30:57] sort of natural language entry is that
[31:00] in the old world when we were doing Pi
[31:02] redaction we had to write complex
[31:04] regular expressions and here this is all
[31:06] done through just providing a category
[31:09] and a bit of a description here and the
[31:11] llm will naturally infer how to do the
[31:13] re redaction we're also going to uh
[31:17] Define the tool to call right and so
[31:19] this is done as a uh essentially a
[31:21] dictionary adjacent object and as you
[31:24] can see there is an array that contains
[31:27] uh dictionaries containing a string and
[31:30] a pi type and the string is the pi
[31:33] information the type is essentially one
[31:35] of 56 categories that we provide as an
[31:37] enum so right off the bat you can see
[31:40] that this tool call is um you know a bit
[31:42] of a large function uh
[31:45] specification and so let's load our data
[31:47] set from hugging face in this case it's
[31:50] going to take maybe a few seconds to
[31:52] load in that data set of 200,000 entries
[31:55] and then what I have in the next cell
[31:57] when I'm downloading this uh data set is
[32:01] what I'm going to use to build my
[32:04] fine-tuning training data set and here's
[32:07] the thing about fine-tuning is that to
[32:09] build your data set you need to make it
[32:11] seem like you've essentially logged
[32:14] conversations with an llm right you're
[32:16] logging the prompts and the responses
[32:18] because that's how you're going to
[32:19] fine-tune it you need to tell it this is
[32:21] the input with system prompt uh tools
[32:24] specification user prompt and here's the
[32:28] uh tools call response that I expect to
[32:31] see and so this cell here just sets it
[32:34] up so that we essentially have each
[32:36] training sample as a message from an nlm
[32:39] that's been logged we're going to see
[32:41] what that looks like in a
[32:42] second so we're going to build a 10,000
[32:46] entry training data set for open
[32:50] pipe and that's going to be downloaded
[32:52] as this open pip data set.
[32:55] jonl and so as I run the cell it's going
[32:58] to download this uh from
[33:01] collab and now when you switch over to
[33:04] open pipe we're going to create a new
[33:06] data set so once you're on open pipe
[33:09] console you have a project here I've
[33:11] generically named IT project one you can
[33:14] access data sets and I already as you
[33:17] can see I already have built a few data
[33:19] sets uh before but if you're a
[33:22] first-time user you're not going to see
[33:23] anything under data sets so you can
[33:25] create a new data set here by clicking
[33:26] on this button
[33:29] and if you go under settings we can name
[33:31] our data set so I'm going to call
[33:33] it uh lunch and
[33:36] learn and today is uh June
[33:40] 26 all right so this is today's lunch
[33:42] and learn I'm going to I'm going to call
[33:44] this my data set and under General I can
[33:47] upload the data that I just downloaded
[33:49] from my notebook open pipe data set.
[33:53] jonl so this upload operation is going
[33:55] to take a few
[33:58] seconds or maybe a couple of minutes
[34:00] because what's going to happen on open
[34:02] PB is not only we're uploading this data
[34:04] set but it's GNA do some uh
[34:06] pre-processing here to split it into uh
[34:09] training and validation set it's also
[34:11] going to get it all formatted in a nice
[34:14] way so we can essentially look into the
[34:16] data
[34:17] set uh so you can see there's this
[34:19] little window here that shows that
[34:21] you're uploading the data set and that
[34:22] it is essentially being
[34:24] processed so while this is happening
[34:28] right we've prepared our data set and
[34:30] we're going to take a look at it in a
[34:31] second while it's being processed on
[34:33] open pipe but let's see how we're going
[34:35] to do the fine-tuning in the next stage
[34:37] right so once we have our data set
[34:40] uploaded we're going to have this view
[34:42] on the data set that shows every single
[34:44] entry that we can Peak into and how it's
[34:46] split into training and test set
[34:48] generally a 90 10%
[34:51] split and from that UI we can launch a
[34:54] finetune and this is where we get to
[34:56] choose our base model model and what
[34:58] we're going to choose is a llama 3 8
[35:00] billion parameter model with
[35:02] 32k Contex width which is a uh fine tune
[35:07] from news research called the Theta
[35:10] model and you can see that there's
[35:13] essentially a pricing here that is being
[35:14] estimated for this fine tune we have a
[35:17] substantial training set because it can
[35:20] range from say hundreds of samples to
[35:22] thousands to hundreds of
[35:23] thousands and the cost can scale up as
[35:27] you um as you feed in more training
[35:30] samples but it will improve the accuracy
[35:32] and it also provides an estimated
[35:34] training price of $40 now that might
[35:36] seem like a lot especially when you're
[35:37] tinkering with fine-tuning but keep in
[35:39] mind some of the people that we work
[35:41] with they tend to spend tens of
[35:43] thousands or maybe hundreds of thousands
[35:44] of dollars a month on gen I spend so
[35:47] this is absolutely something that you
[35:48] can do up front that will pay off and I
[35:51] believe that on open pipe if you get
[35:52] started you get $100 credit uh so that
[35:56] allows you to to run some fine tunes off
[35:58] the bat uh without having to necessarily
[36:01] uh have to to pay so um let's go over to
[36:06] open
[36:07] pipe and it is still uploading I think
[36:09] maybe the network is uh is a bit slow
[36:13] but we're going to essentially start
[36:16] training at this point and once the
[36:18] training is happening we're going to
[36:20] then deploy the fine tun llm uh when
[36:23] training is done and what happens on
[36:25] open pipe is when you're done with
[36:27] training you're going to get an email
[36:28] when that training job is done it can
[36:30] take a few minutes so I'm going to pull
[36:32] a jewelia child here I'm going to stick
[36:33] the you know the turkey in the oven and
[36:36] in the second oven I'm going to have a a
[36:38] pre-baked turkey just so that we don't
[36:40] lose time but as you're going through
[36:41] this on your own keep in mind it's going
[36:43] to take a little bit of time to just
[36:45] kick off that whole fine-tuning process
[36:47] but it's not that long because um you
[36:49] know you're training a fairly small
[36:51] model
[36:52] here all right so this is still uh
[36:56] saving but let let's kind of take a look
[36:58] at what we've done so far right so we've
[36:59] built our data set using a synthetic
[37:01] data set from hugging face uh we format
[37:04] each input output pair from the data set
[37:06] as logged llm messages and this is
[37:09] essentially stored as a jonl file that
[37:12] we upload to open pipe and we produce
[37:14] 10,000 training samples we're
[37:16] fine-tuning a model from open pipe and
[37:18] we're open pipe uses a parameter
[37:20] efficient fine-tuning which produces
[37:22] aora and we choose llama 38 billon
[37:25] parameter model as the base
[37:27] and when we deploy what we're going to
[37:29] use here is octo
[37:30] AI so let's see this didn't finish
[37:34] uploading so I'm going to go into the
[37:35] one that I uploaded just a couple days
[37:38] ago just to essentially show you what
[37:40] you should see on the uh user
[37:43] interface so as you peruse through the
[37:47] training samples what you're going to
[37:49] see is an input column and output column
[37:52] and so on the left you have the input
[37:53] with the system prompt as you can see
[37:55] it's a it's a big boy uh big because it
[37:57] has all these different categories right
[37:59] that it needs to classify it also has
[38:02] the user prompt which is the message
[38:04] that we need to redact the tool choice
[38:07] and the tool specification here with all
[38:08] the different categories of pii types
[38:11] and then the output will be will be this
[38:13] tools call from the assistance response
[38:16] and that will have this redact call
[38:19] along with these arguments field to
[38:21] redact as a list of dictionary entries
[38:24] containing string and Pi type
[38:25] information right and so this is what
[38:28] we've passed into our
[38:31] fine-tuning data set into open
[38:34] pipe and this is still saving so I'm
[38:37] just going to go ahead and go to the
[38:39] model
[38:41] so once you have the data set uploaded
[38:43] again you hit this fine-tune button and
[38:46] this is what's going to allow you to
[38:47] launch a fine-tuning job right I can
[38:49] call this
[38:50] blah and this is where you select under
[38:52] this drop down the model that you want
[38:54] to
[38:55] fine-tune uh this is again what we saw
[38:57] four training size is substantial I'm
[38:59] not going to hit start training because
[39:00] I already have a trained model but when
[39:02] you do that it's going to kick off the
[39:03] training and when it's done you'll get
[39:05] notified by
[39:06] email now let's fast forward let's
[39:08] assume I've already trained my model so
[39:10] I'm going to have this model here that's
[39:12] been fine tuned from this data set I'm
[39:15] going to click on it as we can see it's
[39:17] an llama 38b model it's been fine-tuned
[39:21] over these 10,000 data sets split into
[39:24] 9,000 uh training samples and a00 test
[39:28] samples we can even look at the
[39:32] evaluation but going back to the
[39:36] model and the nice thing is that it's
[39:38] taking care of the hyperparameter like
[39:40] learning rate number of appbox It kind
[39:42] of figures it out for you so you don't
[39:44] really have to tweak those settings and
[39:46] I find that to be very convenient
[39:47] especially for people who haven't yet
[39:48] built an understanding of how to tweak
[39:50] those
[39:51] values and the beauty of using open pipe
[39:55] is that you can now export the weights
[39:56] and be the owner of those weights right
[39:58] remember when we talked about open
[40:00] source it's really important to own the
[40:01] result of the fine-tuning so you can
[40:04] download the weights in any format you
[40:05] want you have luras but also merg
[40:08] checkpoints so you can have a a a
[40:10] parameter efficient representation as
[40:12] well as a checkpoint and so we've
[40:14] selected to export our model as a fb16
[40:17] Laura which is what we're going to use
[40:18] to upload our model on octo AI which is
[40:21] where we're going to use to deploy the
[40:22] model so now I can download the weights
[40:24] as a zip file and it's Prett fairly
[40:27] small only 50 megabytes but I can also
[40:30] copy the link copy the URL and this is
[40:33] what we're going to need to do in this
[40:35] tutorial so to deploy the model what we
[40:38] need to do is copy this URL I'm going to
[40:42] download in the cell the otoi CLI this
[40:46] is a command line interface for users to
[40:49] upload their own fine tunes to what we
[40:51] call our asset Library so this is a
[40:53] place where you can store your own
[40:55] checkpoints your own luras for not just
[40:56] l but also models like stable diffusion
[40:59] if some of you are developers who also
[41:01] work in the image gen space and so we
[41:04] can serve these customized models uh on
[41:08] our
[41:08] platform and so we're going to upload
[41:11] this Laura from open pipe to octo AI so
[41:16] we're going to log in just to make sure
[41:18] credentials are good and here we have
[41:21] confirmation that our token is valid and
[41:24] in the cell we have to replace the Laura
[41:27] URL from set me to that URL that I just
[41:29] copied here from download
[41:31] weights and keep in mind this might take
[41:33] a couple minutes to get the link to
[41:36] appear but once you have that link and
[41:39] again I'm kind of skipping ahead because
[41:41] when you're going to run this at your
[41:42] own time it might take a you know a few
[41:44] minutes to run the fine tune it might
[41:45] take a few minutes to download the
[41:47] weights but everything that I'm running
[41:48] here is essentially the steps that
[41:50] you'll take yourself and what I'm doing
[41:52] here is uh passing in this URL here and
[41:56] set setting a Laura asset name in my
[42:00] octo asset Library so I can then create
[42:03] this asset from this Laura as a safe
[42:07] tensor file and uh based on the Llama
[42:12] 38b model I'm going to name it uh let's
[42:18] see seems like something has failed here
[42:22] so let's try to run it again
[42:38] and so what this is doing is uh let's
[42:46] see usually that that uh that should
[42:48] have
[42:49] worked so what's uh what should happen
[42:53] here is at this point once you've taken
[42:56] the uh URL of your finetune
[43:00] asset should be able to host it on our
[43:03] asset library and then from there serve
[43:05] it to start running some inferences so
[43:10] this
[43:11] uh this this Laura upload step didn't
[43:15] quite work here so Pedro are you're able
[43:17] to maybe double check with product
[43:19] whether this capability is
[43:22] working this isn't a good demo unless
[43:24] something fails and so so uh yeah you
[43:28] know I just tested it earlier today and
[43:29] it was working
[43:31] flawlessly
[43:34] so uh let's see I might have to list my
[43:37] assets so I can pull an old
[43:40] one um
[43:42] actually one second Pedro can you can
[43:45] you tell me what the uh commend is to to
[43:49] list the assets that are on I think it
[43:52] might be octo octo asset list all right
[43:56] let's
[44:04] okay there we go so I'm going to pull
[44:06] from an asset that I uploaded
[44:11] earlier the third
[44:15] one all
[44:20] right yeah
[44:22] because all right so I'm going to take
[44:24] an asset that I uploaded earlier I'm
[44:26] going to have to look into why that step
[44:28] failed but uh
[44:33] let's let's try
[44:36] this okay so I'm going to use an asset
[44:38] that I uploaded earlier I'm not sure why
[44:40] this didn't work but I'll make sure that
[44:41] this is working for you all to reproduce
[44:43] the
[44:44] step and I'm going to set Laura asset
[44:50] name equals this all right so these
[44:54] other luras I uploaded using the exact
[44:56] same steps as as I use for this uh
[44:58] tutorial so we'll make sure to get to
[45:00] the bottom of this and uh we'll use the
[45:02] slack channel here for folks who want to
[45:04] run through this uh step but I'm just
[45:06] going to run an example inference here
[45:09] on this asset that I pulled from open
[45:12] pipe and so again we have our system
[45:15] prompt we're going to pass in this uh ex
[45:19] you know this message this email as our
[45:21] test prompt and then when we're invoking
[45:24] this octo endpoint we're using the
[45:26] standard chat completions uh from open
[45:30] Ai and what we're passing here is this
[45:32] open pipe Lama 3 8B 32k model and we
[45:36] pass in this argument for parameter
[45:39] efficient
[45:40] fine-tune and pass in the Laura asset
[45:43] name that we just uploaded to the asset
[45:46] library and as we can see the response
[45:48] here contains the tool calls and the
[45:50] call to the function that will do the
[45:53] redaction so this is behaving exactly as
[45:55] we intended to so now we can move on to
[45:58] the Quality evaluation for Quality
[46:00] evaluation what we've done is use
[46:04] essentially an accuracy metric
[46:06] thankfully we have a ground proof right
[46:07] from our data set all the
[46:10] exchanges have been labeled with privacy
[46:13] mask information that we can use as
[46:14] ground truth so that makes evaluating
[46:16] scoring or results fairly easy we don't
[46:19] have to use an llm for instance for that
[46:21] we can actually use more traditional
[46:23] techniques of accuracy evaluation and so
[46:26] we have a metric that we've built it
[46:27] assigns a score that can be penalized
[46:31] when pi information was missed or
[46:34] mistakenly added I.E false negative
[46:36] false positive and then we use a similar
[46:38] distance metric to kind of match the
[46:41] responses from the llms compared to our
[46:43] ground Troth so for illustration
[46:45] purposes we have for instance this Pi
[46:49] information that's been redacted that's
[46:51] a score of 1.0 because it's the perfect
[46:53] match or fine tune my for instance miss
[46:56] the fact that Billy was the middle name
[46:58] and my interpreted as first name in that
[47:01] case we're still attributing a high
[47:02] score because it's close enough and
[47:04] probably for a practical use case that
[47:06] would be good enough but for instance
[47:08] upon calling gbd4 it fails to identify
[47:11] two out of the three information that we
[47:13] had to redact and so the score is about
[47:15] a third here right so in this case what
[47:19] we're going to do here I'm just going to
[47:20] reduce the test size to 100
[47:23] samples and I am going to run this
[47:25] evaluation inside of this cell it's GNA
[47:30] bring us a 100 test samples that we can
[47:35] then run our evaluation metric and get
[47:37] our overall scoring out of uh so if we
[47:42] look at you know the uh output from the
[47:47] cell essentially we're just invoke
[47:49] invoking backto back the fine-tune
[47:52] running octo Ai and we're invoking gp4
[47:54] on open AI to do the results collection
[47:59] so we're going to collect some results
[48:01] here and uh once we've collected the
[48:04] results once we get to 100 I think we're
[48:06] getting pretty close here we can run the
[48:08] quality valuation metric and of course I
[48:10] invite you to run it on more samples
[48:12] maybe a th000 or 10,000 uh it just gets
[48:15] more expensive as you're using gp4 you
[48:18] know to run a 100 samples it cost about
[48:20] a dollar in inference so uh then a th000
[48:24] samples cost $10
[48:26] and now we're going to score it all
[48:28] right so we're going to go through every
[48:30] single entry we have our ground proof
[48:32] information we have
[48:34] our eval and labels from gp4 and our
[48:38] eval and labels from our fine tune and
[48:41] we can see that right off the bat the
[48:43] fine tune is actually better at finding
[48:45] the pi to redact here gbd4 scored only a
[48:48] score of 0.49 whereas our fine tune
[48:52] achieved
[48:53] 0.85 and here 0.3 for GPT 4 1 .04 the
[48:57] fine tune so the fine tune overall is
[48:59] performing better and once we Aggregate
[49:01] and average the score gp4 achieved
[49:06] 0.68 out of one whereas our fine tune
[49:09] achieve
[49:11] 0.97 and so that's a difference between
[49:13] prototype and production right you're
[49:15] expected to achieve somewhere in the
[49:17] single nine or two nines of accuracy and
[49:19] this is what this technique shows allows
[49:22] you to achieve and again I want to
[49:23] reiterate that in terms of cost GPD 4
[49:27] costs upward to $30 per million tokens
[49:30] generated whereas llama 38b on octo cost
[49:33] just 15 cents that's a 200x difference
[49:36] right so with that I just want to
[49:40] conclude with some takeaways on fine on
[49:44] fine tuning right fine tuning is a
[49:46] journey but a very rewarding Journey
[49:48] there's truly no Finish Line here you
[49:51] need to attempt fine tuning after you
[49:53] already tried other techniques like
[49:54] prompt engineering retrieval augmented
[49:56] generation
[49:57] but once you decide to Embark data is
[50:00] very important collecting your data set
[50:02] because your model is only as good as a
[50:04] data it's trained on you need to make
[50:06] sure to continuously monitor quality to
[50:08] retune your model as needed you also
[50:11] need to um you know thankfully we have
[50:14] Solutions like octo and open pipe to
[50:16] really make this more approachable and
[50:18] easy to do and it's easier than ever
[50:21] it's only going to get easier but maybe
[50:23] a year ago was only reserved for the
[50:25] most adventurous and sophisticated users
[50:27] and now we really lower the barrier of
[50:29] entry and when you do it right you can
[50:31] achieve really significant improvements
[50:33] in accuracy as well as great reduction
[50:35] in
[50:35] costs I wanted to thank you for sitting
[50:38] here with me over the last 50 minutes I
[50:41] want to reiterate a few calls to action
[50:43] so go to oo. Cloud to learn how to use
[50:46] our Solutions and endpoints but also
[50:49] come to our booth and uh so we're
[50:51] located at this G7 booth and we're going
[50:55] to be here today and tomorrow if if you
[50:56] want to chat about our SAS endpoints
[50:59] about our ability to deploy in an
[51:01] Enterprise
[51:03] environment and also I want to give a
[51:04] shout out to my colleague here Pedro if
[51:06] you're curious about all the knowhow
[51:08] that goes behind how we optimize our
[51:10] model and production because our
[51:11] background is in compiler optimization
[51:13] is is in system optimization
[51:15] infrastructure optimization we've
[51:17] applied all of this to be able to server
[51:19] models you know with positive margins
[51:23] we're not doing this at a loss right
[51:24] we're not wasting our VC money here
[51:26] we're actually building all this knoow
[51:29] into making sure that AI inference is as
[51:32] efficient as it could be so there's
[51:33] going to be a talk on that and also make
[51:36] sure if you if you get a chance assuming
[51:40] you've joined
[51:41] our our uh slack Channel which is the
[51:46] following one so if you're on the
[51:48] slack org for the event go to llm
[51:51] Quality optimization boot camp you can
[51:54] ask us any questions and if you fill out
[51:57] the survey that Pedro is going to post
[51:59] we're going to give you an additional
[52:01] $10 in credits uh so that doesn't seem
[52:04] like a lot but that's a ton you know if
[52:06] it's 15 cents per million tokens that's
[52:08] a lot of uh tokens that you can generate
[52:11] for free so we can give you an
[52:12] additional 10 uh dollars for uh filling
[52:15] out the survey which which should take
[52:16] about you know 20 to 30 seconds so I'm
[52:19] going to be around and also you can find
[52:21] me at the booth this afternoon in case
[52:23] you have any questions but I like you
[52:24] all uh to thank you for sitting through
[52:26] this talk and hopefully hopefully you've
[52:28] learned something from this and
[52:30] hopefully you feel like I've I've
[52:31] demystified this idea of trying fine
[52:33] tuning on your own give this notebook a
[52:36] try assuming of course we fixed this
[52:38] laowa upload issue and uh yeah thank you
[52:41] all and maybe ask me some questions
[52:42] after this uh after this talk thanks
[52:48] [Music]
