---
type: youtube
title: Prompt Engineering Tactics: Dan Cleary
author: AI Engineer
video_id: 7AYUCAuFYeA
video_url: https://www.youtube.com/watch?v=7AYUCAuFYeA
thumbnail_url: https://img.youtube.com/vi/7AYUCAuFYeA/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['Prompt Engineering', 'AI Techniques', 'Chat GPT', 'Multi-Persona Prompting', 'According to Method', 'Motion Prompt', 'AI Integration', 'User Experience', 'Natural Language Processing', 'AI Ethics', 'Machine Learning', 'Content Optimization']
entities: ['Dan Cleary', 'Prompt Tub', 'Chat GPT', 'University of Illinois', 'Johns Hopkins University', 'Microsoft', 'Wikipedia', 'AI features', 'LLMs']
concepts: ['Prompt Engineering', 'Multi-Persona Prompting', 'According to Method', 'Motion Prompt', 'Hallucinations', 'AI Integration', 'User Experience', 'Natural Language Processing', 'Collaborative Brainstorming']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI models', 'Familiarity with prompt engineering concepts', 'Experience with tools like Chat GPT']
related_topics: ['AI Ethics', 'Natural Language Processing', 'Machine Learning', 'User Experience Design', 'Content Generation', 'AI Tools', 'Human-Computer Interaction']
authority_signals: ["I'm co-founder of Prompt Tub", "I've seen that having little changes...", 'This is a proven methodology']
confidence_score: 0.85
---

# Prompt Engineering Tactics: Dan Cleary

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=7AYUCAuFYeA)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: prompt engineering, llm optimization, ai integration, nlp, machine learning, chatgpt, hallucination reduction  

## Summary

# Summary of "Prompt Engineering Tactics: Dan Cleary"  

## Overview  
Dan Cleary, co-founder of Prompt Hub, discusses three actionable tactics to improve AI model responses through prompt engineering. He emphasizes the importance of refining prompts to enhance accuracy, reduce hallucinations, and align outputs with user expectations, particularly for product integrations.  

## Key Points  
- **Multi-Persona Prompting**: Uses multiple agents (e.g., author, publicist) to collaborate on a task, ideal for complex or creative work.  
- **"According To" Method**: Grounds prompts in specific sources (e.g., Wikipedia) to reduce hallucinations by up to 20%.  
- **Motion Prompts**: Adds emotional stimuli (e.g., "this is critical for a big client") to improve response quality by 8–115%.  
- **Non-Deterministic Nature of Models**: Small prompt changes can drastically alter outputs, making engineering critical for reliability.  
- **User Expectations**: Users demand crisp, accurate, and fast AI responses, with tolerance for errors decreasing over time.  

## Important Quotes/Insights  
- *"Small changes in a prompt can have outsize effects on the outputs."*  
- *"Users expect outputs to be crisp, exactly what they wanted, with no hallucinations."*  
- *"Motion prompts tie into human cognitive behavior, leading to better accuracy."*  
- *"The 'according to' method reduces hallucinations by 20% when using consistent data sources."*  

## Actionable Items  
- Implement **multi-persona prompting** for complex tasks by assigning roles to AI agents.  
- Use the **"according to" method** with trusted sources (e.g., Wikipedia) to improve reliability.  
- Test **motion prompts** by adding emotional context (e.g., urgency, importance) to enhance output quality.  
- Explore **Prompt Hub templates** for pre-built prompts and collaboration tools.  
- Continuously test and iterate prompts to align with user expectations and model behavior.

## Full Transcript

[00:01] [Music]
[00:14] how's it going I'm Dan I'm co-founder of
[00:16] promp tuub a prompt management tool
[00:18] designed for teams to make it easy to
[00:20] test collaborate and deploy
[00:23] prompts today I want to talk to you a
[00:25] little bit about prompt engineering
[00:26] including over three easy to implement
[00:28] tactics to get better and more accurate
[00:30] responses from
[00:32] llms but first why prompt engineering
[00:36] can't I just say what I want to the
[00:38] model and I get something pretty good
[00:39] back and while for the most case that's
[00:42] true additional techniques can go a long
[00:45] ways in terms of making sure that your
[00:46] responses are always better the
[00:48] non-deterministic nature of these models
[00:50] makes it really hard to predict and I've
[00:53] seen that having little changes in a
[00:55] prompt can have outsize effect on the
[00:58] outputs and this this is especially
[01:00] important for anyone who's integrating
[01:01] AI into their product because one bad
[01:04] user experience or one time the model
[01:06] decides to go off the rails can result
[01:08] in disaster for your brand or your
[01:11] product resulting in a loss of
[01:14] trust additionally users now that we all
[01:17] have access to chat gbt and can really
[01:19] easily access these models we have very
[01:21] high expectations when we're using AI
[01:23] features inside of products we expect
[01:25] outputs to be crisp exactly what we
[01:28] wanted we expect to see never see
[01:30] hallucinations and in general it should
[01:32] be fast and
[01:35] accurate and so I want to go over three
[01:37] easy to implement tactics to get better
[01:40] and safer responses and like I said
[01:42] these can be used in your everyday when
[01:43] you're just using chat GPT or if you're
[01:46] integrating AI onto your product these
[01:48] will help go a long way to making sure
[01:49] that your outputs are better and that
[01:51] users are
[01:53] happier the first are called multia
[01:56] prompting this comes out of a research
[01:58] study from the University of ill anoy
[02:01] essentially what this method does is it
[02:02] calls on various agents to work on a
[02:06] specific task when you prompt it and
[02:08] those agents are designed for that
[02:10] specific task so for example if I was to
[02:13] prompt a model to help me write a book
[02:15] multip Persona prompting would lead the
[02:17] model to get a publicist an author um
[02:22] maybe the intended target audience of my
[02:24] book and they would work hand inand in
[02:27] kind of a brainstorm mechanism with the
[02:29] AI leading this brainstorm they' go back
[02:32] and forth throwing ideas off the wall
[02:34] collaborating till they came to a final
[02:36] answer and this prompting method is
[02:39] really cool it's because you get to see
[02:40] the whole collaboration process and so
[02:42] it's very helpful in cases where you
[02:44] have complex task at hand or it requires
[02:47] additional logic I personally like using
[02:49] it for generative
[02:52] tasks next up is the according to Method
[02:56] what this does is it grounds prompts to
[02:58] a specific source
[03:00] so instead of just asking you know what
[03:02] part of the digestive tube do you expect
[03:04] uh stars to be digested you can say that
[03:07] and then just add to the end according
[03:09] to Wikipedia so adding according to
[03:12] specified Source will increase the
[03:14] chance that the model goes to that
[03:16] specific source to retrieve the
[03:17] information this can help reduce
[03:19] hallucinations by up to 20% so this is
[03:22] really good if you have a fine-tuned
[03:23] model or a general model that you know
[03:25] that you're reaching to a very uh
[03:28] consistent data source for your answers
[03:31] this is out of Johns Hopkins University
[03:34] was published very
[03:36] recently and last up and arguably my
[03:38] favorite is called the motion prompt
[03:41] this was done by Microsoft and a few
[03:43] other universities and what it basically
[03:45] looked at was how llms would react to
[03:49] emotional stimuli at the end of prompts
[03:51] so for example if your boss tells you
[03:53] that this product is really important
[03:55] for your career for for a big client
[03:57] you're probably going to take it much
[03:59] more seriously ious ly and this
[04:01] prompting method tries to tie into that
[04:03] cognitive behavior of humans and it's
[04:06] really simple all you have to do is add
[04:08] one of these emotional stimuli to the
[04:09] end of your normal prompt and I'm sure
[04:11] you'll actually get better outputs I've
[04:12] seen it done time and time again from
[04:15] everything from cover letters to
[04:18] generating change logs the output just
[04:20] seem to get better and more accurate and
[04:22] the experiment show that this can lead
[04:24] to anywhere from an 8% increase to 115%
[04:28] increase depending on the task it
[04:32] and and so those are three really quick
[04:34] easy hit methods that you can use in
[04:37] chat GPT or in the um AI features in
[04:40] your product we have all these available
[04:42] as templates um in promp tub you can
[04:44] just go there and copy them um it's
[04:46] promp hub. us um you can use them there
[04:49] run them through our playground share
[04:50] them with your team or you can have them
[04:53] via the
[04:54] links and so thanks for taking the time
[04:56] to watch this I hope that you've walked
[04:58] away with a couple new methods so you
[04:59] can try out in your everyday if you have
[05:01] any questions feel free to reach out and
[05:02] be happy to chat about this stuff
[05:05] [Music]
[05:10] thanks
