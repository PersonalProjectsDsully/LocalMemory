---
type: youtube
title: Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer
author: AI Engineer
video_id: pPvoLjYj_mY
video_url: https://www.youtube.com/watch?v=pPvoLjYj_mY
thumbnail_url: https://img.youtube.com/vi/pPvoLjYj_mY/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI Model Evaluation', 'Language Models', 'Hallucination in AI', 'Model Grounding', 'Thinking Models', 'AI Development', 'Natural Language Processing', 'Model Robustness', 'AI Research', 'Machine Learning']
entities: ['o1', 'O3', 'B fan', 'Domain Specific Tasks', 'Hallucination', 'Grounding', 'Thinking Models', 'Language Models', 'Chain of Thought', 'Text Generation']
concepts: ['Model Evaluation', 'AI Grounding', 'Hallucination Mitigation', 'Thinking Models vs. General Models', 'Robustness in AI', 'Task Performance Metrics', 'Contextual Understanding', 'AI Development Challenges', 'Model Accuracy', 'Domain-Specific Tasks']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI models', 'Knowledge of language model evaluation', 'Familiarity with AI terminology like hallucination and grounding']
related_topics: ['AI Model Evaluation', 'Natural Language Processing', 'Machine Learning Ethics', 'AI Hallucination Mitigation', 'Model Robustness', 'AI Development Challenges', 'Contextual Understanding in AI', 'Language Model Performance Metrics']
authority_signals: ['we still have a lot work to do to build those model and better performance', 'the data we have in domain specific task those model not thinking at that stage']
confidence_score: 0.8
---

# Evaluating Domain Specific LLMs for Real World Finance — Waseem Alshikh, Writer

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=pPvoLjYj_mY)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai research, financial modeling, llm evaluation, domain specific models, machine learning, nlp applications, model accuracy  

## Summary

# Summary of "Evaluating Domain Specific LLMs for Real World Finance"  

## Overview  
Waseem Alshikh, co-founder and CTO of Writer, discusses the evaluation of domain-specific large language models (LLMs) versus general-purpose models in real-world financial applications. The talk highlights the limitations of "thinking" models in handling context-specific tasks, the creation of an open-source framework (FAIL) to test robustness, and findings that smaller models often outperform larger ones in grounding accuracy.  

## Key Points  
- **Company Background**: Writer has developed a range of LLMs, including chat and "thinking" models, and tested them against domain-specific challenges in finance.  
- **Trend in General Models**: General-purpose LLMs have achieved high accuracy in tasks like text generation but struggle with context grounding, leading to hallucinations.  
- **FAIL Framework**: A framework (Failure Analysis for Language Models) was created to evaluate robustness through two categories:  
  - **Query Failure**: Misspelled, incomplete, or out-of-domain queries.  
  - **Context Failure**: Incorrect or misleading context/data.  
- **Results**:  
  - General models excel at generating answers but fail to adhere to context, increasing hallucination risks.  
  - "Thinking" models (e.g., O1, O3, B fan) perform worse in grounding tasks, with up to 60% failure rates.  
  - Smaller models often outperform larger ones in context adherence.  
- **Open-Source Data**: The evaluation metrics and datasets are publicly available for further research.  

## Key Quotes/Insights  
- "Thinking models don’t refuse to answer, but they fail to follow context, leading to higher hallucination rates."  
- "Smaller models sometimes outperform larger ones in grounding tasks, challenging assumptions about model size and capability."  
- "There’s a significant gap between robustness and accuracy in domain-specific tasks."  

## Actionable Takeaways  
- **Prioritize Context Grounding**: Domain-specific models need stronger mechanisms to adhere to context, especially in high-stakes fields like finance.  
- **Reevaluate "Thinking" Models**: Larger models may not always improve performance; their hallucination risks require careful mitigation.  
- **Leverage Open-Source Tools**: The FAIL framework can help researchers and developers test and improve model robustness.  

---  
*Note: The transcript ends abruptly, so some details (e.g., specific model names) may be incomplete.*

## Full Transcript

[00:00] [Music]
[00:17] hello everyone my name is Wasim I'm one
[00:20] of the co-founder and CTO
[00:22] ater today I'm going to just tell you a
[00:25] quick story about actually what we
[00:27] building a trer what we doing but before
[00:29] we dive in I would love just to give you
[00:32] quick history of writer so writers we
[00:35] start the company in 2020 we love to say
[00:38] the story of writer is the story of the
[00:40] Transformer we started building those
[00:43] decoder encoder model in the early days
[00:46] and we start we kept building those
[00:47] model and build a lot of them today we
[00:50] have a family of
[00:51] models I believe around 16 we published
[00:56] we have another 20 coming in the way and
[00:58] we keep building those models and you're
[01:00] going to see from this list those model
[01:02] com in two categories General model like
[01:05] p x p 3 4 if you have a b 5 coming soon
[01:10] and we have a lot of what's called
[01:12] domain specific model Creative Financial
[01:15] Services pal
[01:18] medical
[01:20] now early 2024 basically last year
[01:24] almost we start seeing this trend with
[01:26] all the LM
[01:28] basically get very high accuracy in
[01:32] general the any punish Mark we're see
[01:34] the accuracy moving and just the growing
[01:36] and I believe everyone noticing this
[01:38] accuracy today average accuracy for a
[01:41] good General models between 80 maybe
[01:44] close to
[01:47] 90
[01:49] so that basically make a bring a
[01:53] question inside the company saying is it
[01:56] worth it for us to start building and
[01:58] keep building domain specifically models
[02:00] if the accuracy today with General model
[02:03] achieving around
[02:04] 90% And we have domain specific model
[02:07] should we just keep building General
[02:08] models find tunit maybe go Direction
[02:12] with what you call reasoning or thinking
[02:14] models and that will be more than enough
[02:16] actually and we don't need those
[02:19] financial or what call doain specific
[02:21] model now to answer this questions we
[02:24] need
[02:26] data so whatever we're going to present
[02:29] next she could be applicable to
[02:31] financial services domain specific model
[02:33] sorry to Medical specific model customer
[02:36] support domain specific model and all
[02:38] different doain specific model today I'm
[02:41] going to talk specifically about the
[02:43] financial spe uh what's called the
[02:45] financial punchmark for domain specific
[02:47] model uh we have something similar for
[02:50] medical but we believe we are but we
[02:53] start seeing similar result now let me
[02:56] dive
[02:57] in just to remind you we're trying to
[03:00] answer this questions General model the
[03:03] speciic model should we keep build them
[03:05] where we actually going from here we
[03:07] start actually saying great we don't
[03:10] know the answer let's actually do the
[03:12] evaluation let's create the data and we
[03:15] created something called
[03:17] fail the idea behind it let's create
[03:19] real word scenario to evaluate those
[03:22] model and let's see actually of those
[03:24] new model can really give you the
[03:27] accuracy that we promise or the accuracy
[03:30] that we see today from the punch marking
[03:32] on domain
[03:34] specific we created two type of
[03:37] categories in this evaluation something
[03:40] called query failure in query failure
[03:43] basically we introduce three type of
[03:46] subcategories something called Miss
[03:48] spelling queries you know when you go
[03:51] ask the llm questions but you do some
[03:53] spelling error segment error you do some
[03:56] com comment type of issues weu that to
[04:00] the eval set we introduce something in
[04:03] like what called incomplete
[04:06] queries you're missing some keyword some
[04:09] stuff not clear we introduce what's
[04:11] called out of domain queries if you're
[04:14] not expert in the field or you decide to
[04:17] copy paste some general answer try to
[04:19] answer about something very specific and
[04:22] also intru the second category is what
[04:23] we call the context failure and the
[04:26] context failure basically and this get
[04:28] very interesting we we introduce three
[04:31] subcategories what called basically
[04:33] messing context we basically ask the LM
[04:36] question about context not exist in the
[04:41] the quest itself in the BR we introduce
[04:44] what called OCR error today when we do
[04:48] any kind of OCR or convert physical do
[04:52] document to text we introduce a lot of
[04:54] Errors like you know character issues
[04:58] distance between them the word between
[05:00] when you do the OCR could be merged
[05:02] together so we introduce that type of
[05:04] errors and also we did what call
[05:06] unrelevant
[05:08] context let's say you want to ask
[05:11] question about specific document and you
[05:13] end up basically uploading completely
[05:15] wrong document does lm going to still
[05:17] answer is LM just actually figure out
[05:20] you have a completely irrelevant
[05:22] context now when you put all this data
[05:25] together in domain in financial specific
[05:28] Financial Service specific you need some
[05:30] kind of diversity just a quick
[05:33] screenshot just tell you what amount of
[05:35] data how much token something worth
[05:37] mentioning the white paper the data the
[05:40] evaluation set the leaderboard all
[05:43] actually open source today available in
[05:45] GitHub and huging face so anyone please
[05:48] check it out and we introduce very
[05:52] simple what you call it evaluation key
[05:54] Matrix basically we need to look to two
[05:57] things and the model give the correct
[05:59] answer can the model actually give good
[06:03] follow to the grounding or context
[06:05] grounding or basically what you call it
[06:08] here the context this is quick or high
[06:11] level way of how we do the
[06:14] calculation so to
[06:17] evaluate we selected a group of models
[06:21] today we can see a lot of chat model and
[06:24] also thinking models this is basically
[06:26] the two list we have here I'm sure you
[06:29] get familiar with this list and then we
[06:32] onun the evaluation and we start seeing
[06:34] very interesting results I'm going to
[06:37] dive in directly to the result and
[06:39] basically we start getting something
[06:42] Fancy with all this color let me switch
[06:45] to the more what basically
[06:48] see what's start getting very
[06:50] interesting we're saying really good
[06:52] behavior and all thinking models
[06:55] actually they don't refuse to answer
[06:59] this sound good most of the time but in
[07:02] reality when you give something those
[07:05] llms wrong context when you give them
[07:07] wrong data when you have a complete
[07:09] different grounding those model actually
[07:11] fail fail to follow this part and they
[07:14] still give you an answer and that
[07:16] basically get you way higher
[07:20] hallucination if you start focusing on
[07:22] the answer itself can the model give me
[07:24] answer or not you can Fe basically
[07:27] almost every model from the domain
[07:29] specific spef the general model they
[07:31] give you some kind of answer all them
[07:33] close to each other actually reasoning
[07:35] or thinking model they get to even
[07:38] higher score a little bit from there but
[07:41] when get to the grounding and cona
[07:43] grounding this is when stuff get more
[07:46] interesting you can see specifically in
[07:48] task like text generation or question
[07:52] answering it's just not performing well
[07:55] now all does the chart look great what I
[07:57] prefer is the numb
[08:00] this is the same data we use to generate
[08:02] the chart we can go through this really
[08:05] quick and if you look at this number
[08:06] here especially for example like the o1
[08:08] or O3 or B fan you can start noticing
[08:12] the stuff those model doing amazingly
[08:15] and basically when you ask with it
[08:17] misspelled when you got stuff uncomplete
[08:20] out of domain the numbers look amazing
[08:23] the model can take a query with mess
[08:26] spelling wrong grammars or even out of
[08:29] domain and still can give you the answer
[08:33] but when you start going to grounding
[08:35] this is going to startu get very
[08:37] interesting I'm going to hold this slide
[08:39] for a second here if did you notice
[08:41] something
[08:46] different yep and also those bigger more
[08:50] thinking give you the worst result
[08:53] you're getting almost
[08:55] 70 50% to
[08:58] 60% uh worse in the grounding meaning
[09:01] the model is just not following you
[09:03] attach in context you ask the questions
[09:06] and the answers exist outside the
[09:08] context completely same thing coming to
[09:11] stuff around it anal context so you can
[09:14] look at the data and see smaller model
[09:17] actually performing better than all this
[09:19] model overthinking at that side and this
[09:23] is basically it get us about is this
[09:26] thinking or just a Chain of Thought you
[09:28] know this could be a lot of argument at
[09:31] least from the data we have in domain
[09:34] specific task those model not thinking
[09:37] at that stage meaning Hallucination is
[09:41] really high causing a lot of a lot of
[09:44] issues especially in this fin in this uh
[09:48] Benchmark we run here in fin Financial
[09:50] use cases also we can see there's a huge
[09:54] gap between what call robustness and the
[09:58] holin
[10:00] and getting the answer correct so
[10:02] definitely we still have a lot work to
[10:05] do to build those model and better
[10:07] performance but also that get me to you
[10:10] know to the main idea if you go back
[10:14] real quick here even with the best model
[10:17] between all this line we're still not
[10:19] getting between robustness and cont
[10:22] grounding more than
[10:23] 81% sounds a great number if you think
[10:27] in the reality you saying every request
[10:30] 20 of them it's just completely wrong so
[10:33] that basically what we start seeing
[10:36] believe at least today with the
[10:38] technology we have with the current
[10:40] model we have until we have something
[10:42] completely different we're seeing you
[10:44] need full stack you need the rock system
[10:48] you need
[10:49] the grounding you need everything from
[10:52] guard rails and the build around the
[10:55] system itself to actually have something
[10:58] relable utilize today in the same
[11:02] time I would love to go back and answer
[11:05] the first questions and our first
[11:07] question
[11:09] here do you still need to build the
[11:11] models at least today from the data we
[11:13] have from run those punch Mark the
[11:16] answer simply yes we still need to build
[11:19] and continue domain specific model at
[11:22] least with the today implementation even
[11:24] accuracy is keep growing but the
[11:27] grounding the context for following all
[11:30] the context correctly it's still way way
[11:33] way behind from everything we see today
[11:35] in the
[11:37] market thank you so much guys
[11:41] [Music]
[11:42] [Applause]
[11:47] [Music]
