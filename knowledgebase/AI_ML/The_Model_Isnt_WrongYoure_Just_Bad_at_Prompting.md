---
type: youtube
title: The Model Isn’t Wrong—You’re Just Bad at Prompting
author: AI Engineer
video_id: Hp4MzVTXcKw
video_url: https://www.youtube.com/watch?v=Hp4MzVTXcKw
thumbnail_url: https://img.youtube.com/vi/Hp4MzVTXcKw/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['Prompt Engineering', 'AI', 'LLM', 'Meta Prompting', 'Few Shot Prompting', 'Content Generation', 'AI Tools', 'Model Optimization', 'Tutorial', 'Explanation', 'Discussion', 'Opinion']
entities: ['Promptu', 'Tech grad', 'Open AI', 'Anthropic', 'Microsoft', 'Med prompt framework', 'LLM', 'AI', 'prompt engineering', 'Meta prompting']
concepts: ['Prompt Engineering', 'Few Shot Prompting', 'Meta Prompting', 'Reasoning Models', 'Tutorial/How-to', 'Overview/Explanation', 'Discussion/Opinion', 'AI Tools', 'Content Generation', 'Model Optimization']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI and LLMs', 'Familiarity with prompt engineering concepts', 'Experience with AI tools like Open AI or Anthropic']
related_topics: ['AI and Machine Learning', 'Natural Language Processing', 'Content Generation', 'Model Optimization', 'Prompt Frameworks', 'Machine Learning Tools', 'AI Ethics', 'Deep Learning Techniques']
authority_signals: ["I think it'd be silly as some people who are working with LMS to not use LMS for this part of the process", 'we tailor it a little bit for you as well', 'Microsoft released a paper earlier this year about their Med prompt framework']
confidence_score: 0.8
---

# The Model Isn’t Wrong—You’re Just Bad at Prompting

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=Hp4MzVTXcKw)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: prompt engineering, chain of thought, llm optimization, ai techniques, model prompting, reasoning models, nlp  

## Summary

# Summary of "The Model Isn’t Wrong—You’re Just Bad at Prompting"

## **Overview**  
Dan, co-founder of **Prompt Hub** (a platform for prompt engineering), emphasizes the importance of **prompt engineering** in maximizing the performance of large language models (LLMs). He argues that models aren’t at fault for suboptimal outputs—poor prompts are. The video covers techniques like **Chain of Thought**, **Few Shot Prompting**, and **Meta Prompting**, along with tools to streamline the process.

---

## **Key Points**  

### **1. Why Prompt Engineering Matters**  
- **Misconception**: Many assume LLMs are "broken" when outputs are poor.  
- **Reality**: The issue lies in how prompts are structured.  
- **Goal**: Tailor prompts to guide models effectively, leveraging their capabilities.  

### **2. Core Techniques**  
#### **Chain of Thought (CoT) Prompting**  
- **Purpose**: Break down complex tasks into logical steps.  
- **Methods**:  
  - Use reasoning chains (e.g., "Let’s think step by step").  
  - Examples: Math problems, logical deductions.  
  - Tools: Prompt Hub’s free CoT generator.  
- **Benefits**: Improves accuracy for complex or abstract tasks.  

#### **Few Shot Prompting**  
- **Approach**: Provide 1–2 examples of desired output.  
- **Key Insight**: Most gains come from 1–2 examples; additional examples may degrade performance.  
- **Best Practices**:  
  - Use diverse examples to cover edge cases.  
  - Avoid overloading the model with too many examples.  

#### **Meta Prompting**  
- **Definition**: Use LLMs to generate, refine, or optimize prompts.  
- **Tools**:  
  - OpenAI Playground, Anthropic, and **Prompt Hub**.  
  - Prompt Hub’s meta-prompting allows customization for different model providers (e.g., OpenAI vs. Anthropic).  
- **Advantage**: Automates prompt iteration and optimization.  

### **3. Reasoning Models & New Frameworks**  
- **Microsoft’s Med Prompt Framework**: A recent approach to structuring prompts for reasoning models.  
- **Key Takeaway**: Reasoning models require different prompting strategies than traditional LLMs.  

### **4. Practical Tools & Platforms**  
- **Prompt Hub**:  
  - Free platform with pre-built prompts (CoT, verification methods, etc.).  
  - Features: Meta-prompting, co-pilot feedback, and model-specific customization.  
- **OpenAI/Anthropic Tools**: Built-in meta-prompting capabilities.  

---

## **Important Quotes/Insights**  
- *"The model isn’t wrong—it’s the prompt that’s at fault."*  
- *"Few shot prompting gives most of the gains with just 1–2 examples."*  
- *"Meta prompting is using LLMs to improve prompts, which is a no-brainer."*  
- *"Reasoning models require different frameworks—don’t treat them like traditional LLMs."*  

---

## **Actionable Takeaways**  
1. **Leverage Chain of Thought**: Use reasoning steps for complex tasks.  
2. **Use Few Shot Prompting**: Provide 1–2 diverse examples to guide the model.  
3. **Experiment with Meta Prompting**: Let LLMs refine your prompts.  
4. **Utilize Tools**: Explore platforms like **Prompt Hub** for pre-built prompts and meta-prompting.  
5. **Iterate**: Use feedback loops (e.g., Prompt Hub’s co-pilot) to refine prompts.  

--- 

## **Final Thoughts**  
Prompt engineering is a critical skill for maximizing LLM performance. By understanding techniques like CoT, Few Shot, and Meta Prompting, and using tools like Prompt Hub, developers can unlock the full potential of AI models.

## Full Transcript

[00:00] hey everyone how's it going Dan here so
[00:01] excited that you're joining today um
[00:03] we're going to be talking about all
[00:04] things related to prompt engineering and
[00:05] so some very quick background on myself
[00:08] I'm the co-founder of prompt Hub the
[00:09] GitHub for prompts based in New York I'm
[00:12] a Lakers fan more specifically a LeBron
[00:13] fan but that just means February has
[00:15] been a great month for me um and I'm a
[00:17] marathon runner and so today we'll be
[00:19] covering a lot of ground a lot of
[00:21] templates a lot of free stuff um that
[00:23] should be hopefully pretty helpful that
[00:24] you can go and take and start messing
[00:26] around with and so we'll talk about why
[00:27] prompt engineering is still important
[00:30] why Chain of Thought PR uh prompting has
[00:32] been so revolutionary especially when it
[00:34] comes to test time compute P shot
[00:36] prompting using LMS to help you write
[00:38] prompts via meta prompting how prompt
[00:40] engineering with reasoning models is
[00:41] actually very different um but a bunch
[00:43] of fre resource templates got so I
[00:46] usually include a slide like this in any
[00:48] of my talks and I I waver from doubling
[00:50] down and including more of these and
[00:52] completely removing it but you know I
[00:54] think the meme in the beginning was that
[00:55] you know why do you even why it's p
[00:57] engineering even a term you can just
[00:59] tell the model to do but I think anyone
[01:00] who's ever actually shipped an Al based
[01:03] feature has known it it's much more
[01:05] nuanced from that even just trying to
[01:07] understand what you want the model to do
[01:09] is
[01:10] challenge and I think it's just a really
[01:12] good starting point for folks of course
[01:15] um it's the easiest and most accessible
[01:16] way to get better outputs from llms and
[01:19] it's a part of the med a greater system
[01:22] right we all have access to the same
[01:23] models um but the prompts the
[01:25] architecture everything around that is
[01:27] how we can also have a competitive
[01:28] advantage in our product whatever we're
[01:31] building I think you know something that
[01:33] was mentioned in anthropics recent paper
[01:35] blog post about agents is that going for
[01:38] the simplest solution I think is really
[01:40] key to keep in mind it's really easy to
[01:42] kind of run away with these things when
[01:44] you're working with llm think about
[01:46] everything you can do and that's great
[01:48] um but you know just spending an hour
[01:50] trying to mess around with the prompt
[01:51] and then determining that you know it's
[01:53] impossible to solve whatever you're
[01:54] trying to do via prompt engineering and
[01:56] you need to do a complex rag or things
[01:58] along those lines I think is it's not
[02:00] super smart you need to give some time
[02:01] here because if you can do it it's much
[02:04] simpler to
[02:05] manage so I'll cover just two main
[02:08] methods Chain of Thought F prompting
[02:09] just because I think they're the most
[02:10] effective and most topical there are a
[02:12] bajillion more a lot of them fall
[02:14] underneath the umbrella of General
[02:16] reasoning prompts um we've covered most
[02:18] if not all of these and they're all
[02:21] available as templates in promp tub as
[02:22] well you can check out for
[02:25] free so what is streen of thought
[02:27] prompting specially when you instruct
[02:28] the model to
[02:31] reason or think about the problem or a
[02:33] solution before actually jumping into
[02:35] whatever that that answer is so it
[02:38] breaks down problems into sub problems
[02:41] um you get a glimpse into how the model
[02:43] is thinking which can be helpful for for
[02:45] trouble studing it's widely applicable
[02:48] of course you can use it kind of with
[02:49] any model um it's easy to implement as
[02:52] well and it's so powerful that is now
[02:53] kind of being built into these reasoning
[02:55] models and so you don't even really need
[02:56] to do it for those reasoning models it's
[02:58] so the classic kind of zero shot way to
[03:00] do this is just to add something to your
[03:02] prompt that will make the model think a
[03:04] little bit before just giving you the
[03:06] output yeah you want it to just generate
[03:07] some sort of kind of reasoning token
[03:08] beforehand and think step by step was a
[03:10] classic one you take a breath and take
[03:12] it through things along those lines
[03:14] another very popular way to do this is
[03:17] by having few shot examples of those
[03:19] reasoning steps and so if I'm having a
[03:22] prompt to solve math problems I can
[03:23] include another math problem in the
[03:25] prompt and show the reasoning steps I
[03:27] wanted to solving
[03:28] that and of course you can use llms to
[03:31] generate these reasoning chains as well
[03:32] so there's something called just
[03:33] automatic Chain of Thought which is a
[03:35] framework um that's a little bit more
[03:38] involved um there's another one called
[03:39] Auto reason which is just a single
[03:41] prompt here where you pass your task or
[03:43] question and it will generate um
[03:45] reasoning chains actually has few shot
[03:47] examples of reasoning chain in there as
[03:49] well you can try this out prop
[03:51] tub and even the training template that
[03:53] deeps used for its R1 model um basically
[03:57] did this it had to generate it's
[03:59] thinking process within think tags and
[04:02] then use all these outputs these
[04:03] generated reasoning chain to train the
[04:05] model to be really good at Chain of
[04:07] Thought So this is also available inside
[04:10] promptu you can input your task get a
[04:11] reasoning chain um C be on your way and
[04:14] that's totally free if you want try it
[04:15] out as I mentioned we have a ton of
[04:18] these um in the platform a ton of
[04:20] reasoning chains that you can go and
[04:21] check out some of them are Chain of
[04:23] Thought some of them are other type of
[04:25] um reasoning or verification methods as
[04:28] well but they're all pretty helpful I
[04:31] would say especially you want to use
[04:32] them when you're dealing with like
[04:33] complex
[04:35] problems so moving on to few shot
[04:37] prompting um that's generally when you
[04:39] include examples of what you want the
[04:41] model to kind of mimic or do or to
[04:44] understand about your problem and
[04:45] essentially you're doing a show rather
[04:47] than tell and so in this example here
[04:50] I'm telling um the model that I have
[04:52] this client we need to like generate
[04:54] some content for it here's a brief
[04:56] here's a related content here's a brief
[04:58] here's the related content and then I
[05:00] say here's the brief and then the model
[05:01] will fill in this this content here and
[05:04] so rather than trying to encapsulate my
[05:06] client's tone or Style by sending an
[05:09] input and output example a brief and a
[05:11] piece of content I can kind of teach the
[05:12] model uh exactly what I
[05:15] want the great part of this is that you
[05:17] get most of the gains from just like an
[05:19] example or two um almost all the graphs
[05:21] kind of look like this when you're
[05:22] looking at number number of examples
[05:24] versus uh performance and sometimes
[05:28] performance can even degraded once you
[05:29] have like a
[05:30] um but it's great for Builders because
[05:32] you only need I say one or two you want
[05:33] kind of want to have them be diverse and
[05:34] cover your basis of different inputs you
[05:37] could expect that model to handle um but
[05:39] yeah you don't need many of
[05:41] them so next up is meta prompting um you
[05:45] know I think it'd be silly as some
[05:47] people who are working with LMS to not
[05:48] use LMS for this part of the process So
[05:50] Meta prompting is basically just using
[05:51] llm either to create a prompt ref find a
[05:54] prompt improve a prompt whatever that
[05:55] might be there are a ton of Frameworks
[05:58] for this out there um some of them are
[06:01] require you to have voting knowledge
[06:02] some of them don't there are a bunch of
[06:04] free tools as well which of course
[06:06] they're very user friendly and thropic
[06:07] that's a great one open AI has one
[06:09] inside of their playground and then we
[06:11] also have one in promptu um the
[06:14] difference with ours is you can select
[06:15] which model provider you are using and
[06:17] it will run a different meta prompt
[06:19] because a prompt that is good for
[06:20] opening ey models might not be the same
[06:22] as anthropic and so we we tailor it a
[06:25] little bit for you as well and then we
[06:28] also have a way that you can kind of
[06:29] iterate work with a um kind of like a
[06:31] co-pilot inside promptu it's built off
[06:34] very similar things to Tech grad where
[06:35] you can run prompts give feedback so
[06:37] this is another free tool that you have
[06:39] to your disposal as well because comp
[06:42] engineering is something that we can use
[06:43] help with so when I leverage
[06:46] LMS so moving on to go say stuff that's
[06:48] much more apparent now and more recent
[06:51] is that reasoning models are very
[06:54] different both in terms of how they work
[06:56] and how you prompt them so Microsoft
[06:58] released a paper earlier this year
[07:00] about their Med prompt framework it's
[07:02] not super important but basically they
[07:03] ran a prompt engineering framework with
[07:06] 01 and found that adding examples led to
[07:10] worse
[07:11] performance and the researchers at Deep
[07:13] seek when building R1 found this as well
[07:16] uh the F shop degraded
[07:18] performance in opening I kind of
[07:20] mentioned this when they first released
[07:21] a one preview saying that you need to be
[07:24] careful when providing additional
[07:25] context because it can kind of over
[07:27] complicate things and confuse the model
[07:31] and so you got to be careful with
[07:32] examples but if you need to want to
[07:34] increase performance there's been a lot
[07:35] of research that has shown that the more
[07:38] reasoning a model does the better the
[07:40] output could be so in that same prompt
[07:42] paper they had a prompt that was you
[07:44] know quick response and then I prompted
[07:46] prompted the model to think more um and
[07:49] they saw that better result when the
[07:51] model was thinking more from extended
[07:52] reasoning and the folks deep seeks saw
[07:55] this as well so as they continue to
[07:56] train the model the length of the
[07:58] response to the thought process
[08:00] increased and then also this will in
[08:03] turn um increased accuracy and
[08:05] performance as
[08:07] well so overall when you're using
[08:09] reasoning model specifically minimal
[08:12] prompting nothing can really be like a
[08:14] really good clear task description want
[08:17] to encourage more reasoning if you're
[08:18] having trouble kind of getting maybe
[08:20] that last bit of performance having
[08:21] encouraging the model to reason more
[08:22] could be helpful avoid fre shot
[08:24] prompting if you're going to do it start
[08:26] with like one one maybe only two
[08:28] examples
[08:30] and then you don't really need to
[08:32] instruct the model on how to reason it's
[08:34] kind of built in there so doing that can
[08:36] actually um hurt performance as well and
[08:39] so as I mentioned lot of free resources
[08:41] we run a substack called PRP enging
[08:42] substack we write on our blog um there's
[08:45] a bunch of prompts in the community from
[08:47] us and from other people and so I hope
[08:49] this was helpful I hope you have a great
[08:51] time at the summit and have a great day
