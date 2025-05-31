---
type: youtube
title: Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen
author: Channel Video
video_id: fiXjTif1nS4
video_url: https://www.youtube.com/watch?v=fiXjTif1nS4
thumbnail_url: https://img.youtube.com/vi/fiXjTif1nS4/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['LLM evaluation', 'model testing', 'AI tools', 'machine learning', 'NLP evaluation', 'human feedback in AI', 'model-based assessment', 'AI development practices', 'Python for AI', 'bias mitigation in AI']
entities: ['llmeval', 'Niklas Nielsen', 'lock10', 'Large Language Models (LLMs)', 'mermaid diagrams', 'Python code', 'model-based evaluation', 'human feedback integration']
concepts: ['evaluating LLM applications', 'model-based evaluation methodologies', 'human-AI feedback integration', 'testing with other models', 'bias mitigation in AI evaluation', 'best practices for LLM evaluation', 'AI-generated feedback systems', 'tutorial on llmeval tool']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic understanding of large language models', 'Familiarity with Python programming', 'Experience with AI model evaluation techniques']
related_topics: ['AI model evaluation frameworks', 'Machine learning testing strategies', 'Human-in-the-loop AI systems', 'Bias detection in AI models', 'Natural language processing evaluation', 'AI feedback loop optimization', 'Model comparison techniques']
authority_signals: ["we've been working on this where you basically start bridging between model based and human feedback", 'you can find me at Nicholas cord on X or forly forly known as Twitter', 'this is all I had today']
confidence_score: 0.85
---

# Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=fiXjTif1nS4)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llm evaluation, large language models, ai tools, prompt engineering, model testing, machine learning, ai development  

## Summary

# Summary of "Best Practices for Evaluating Large Language Model Applications with llmeval"

## Overview  
Niklas Nielsen, CTO of Log 10, introduces **llmeval**, a tool designed to evaluate and improve the reliability of large language model (LLM) applications. The video highlights challenges in defining "good" performance for LLMs, emphasizes the need for structured testing, and demonstrates llmeval’s capabilities for prompt engineering, model-based evaluation, and hybrid AI-human feedback.

---

## Key Points  
- **llmeval Features**:  
  - A command-line interface (CLI) tool using **Hydra** for configuration.  
  - Supports test case creation, metric tracking, and report generation.  
  - Enables model-based evaluation, where one model acts as a "judge" for another.  
- **Challenges in Evaluation**:  
  - LLMs are "fuzzy," requiring probabilistic success metrics (e.g., 3/5 passing tests).  
  - Manual test setup is time-consuming, but llmeval streamlines this process.  
- **Examples**:  
  - Testing math problem solutions, Python code generation, and Mermaid diagram quality.  
  - Using model-based evaluation for nuanced feedback (e.g., scoring 1–5 or preferences).  
- **Hybrid Feedback**:  
  - Combines AI-generated feedback with prior human input to reduce bias.  

---

## Key Quotes & Insights  
- *"Without knowing what 'good' means, it’s hard to evolve applications."*  
- *"Models are fuzzy—3 out of 5 tests should pass."*  
- *"Model-based evaluation allows nuanced feedback (e.g., grades, preferences) but has pitfalls like self-bias."*  
- *"We bridge AI and human feedback to improve accuracy."*  

---

## Actionable Recommendations  
1. **Use llmeval’s CLI** for structured testing and reporting.  
2. **Implement prompt engineering** to refine test cases (e.g., ensuring Python code output).  
3. **Leverage model-based evaluation** for nuanced grading (e.g., scoring diagrams).  
4. **Combine AI and human feedback** to mitigate model bias.  
5. **Customize metrics** to align with specific application goals (e.g., code correctness, explainability).  
6. **Explore documentation** and examples provided by Log 10 for setup.  

---  
*For more details, visit Log 10’s documentation or contact Niklas Nielsen via X (Twitter) or email.*

## Full Transcript

[00:01] [Music]
[00:15] hi this is Nicholas I'm the CTO and
[00:17] co-founder of log 10 and we want to talk
[00:21] about how you can scale the liability of
[00:24] LM applications using um a new tool that
[00:27] we've built during this year I think we
[00:29] all can agree that there's been like
[00:31] this kind of craze in the industry and
[00:34] we've been rolling out a ton of
[00:36] intelligence features based on
[00:38] gbt and we kind of finding ourselves in
[00:40] a now what
[00:42] moment because without knowing what good
[00:44] means in a generative setting it's
[00:46] really really hard and risky to evolve
[00:49] your applications like changing your
[00:51] prompts configurations let alone
[00:53] considering going from one model
[00:55] provider to another to more advanced use
[00:59] cases like self posting or
[01:01] fine-tuning we wanted to introduce a new
[01:03] tool today called llm
[01:05] eal that enables uh teams to ship
[01:08] reliable llm
[01:12] products it it is command line tool that
[01:15] you can run locally and with these four
[01:18] uh lines of code uh you should be good
[01:21] to
[01:22] go um the initialization creates a
[01:27] folder
[01:28] structure um and best practices for
[01:30] storing prompts and and
[01:32] tests and then this is based on a super
[01:36] configurable system from meta called
[01:39] Hydra so you could basically extend it
[01:42] to your heart's desire and the metrics
[01:45] that we have wired up are in Python so
[01:49] they could be any logic could be called
[01:51] out to all the llms whatever you want
[01:54] and after these evaluations have been
[01:56] run you can generate some reports that
[01:59] that basically gives you like a brief
[02:01] overview of how the entire app and all
[02:04] the tests are looking but still supports
[02:07] flexible test criteria because like
[02:09] these models are very fuzzy it's very
[02:12] hard to sit with a guarantee that it's
[02:13] going to be one or the other but it's
[02:15] fairly safe to say that the majority
[02:17] cases or say three out of five should
[02:21] pass and we're going to jump
[02:24] into command line and taking a
[02:27] look we're just going to create a
[02:30] directory for
[02:34] today and go into this directory and
[02:36] create ourselves a virtual
[02:41] environment from here we going to
[02:44] install LM
[02:49] eval and initialize the folder structure
[02:53] what we should be able to see here
[02:57] is a directory structure where we have
[03:01] our prompts let see a simple case could
[03:03] be this where we have this message
[03:06] template saying like what is a plus b
[03:08] only return the answer without any
[03:10] explanation so in this case we know that
[03:14] we have to prompt engineer further in
[03:15] order to get an exact output cuz let's
[03:19] take a look at how the test looks like
[03:21] in this case we're taking like the
[03:23] actual output from the llm and comparing
[03:27] it with the expected and this is like a
[03:30] comparison what we had taken the Liberty
[03:33] to do is to strip any spaces that might
[03:36] be come from from the left and that's
[03:39] because some models in this case claw
[03:41] tends to preent spaces and so it's
[03:44] things like that that you have to watch
[03:46] out for then we have the metric which
[03:49] could be any metric that you want to
[03:50] surface in the report and then the
[03:52] result which is then pass or fail and in
[03:56] this case we want to add four and five
[03:58] and we expect it to be nine
[04:01] and I just going to try to run this test
[04:03] here and try to revert some of the promp
[04:07] engineering that we did earlier so I'm
[04:09] going to
[04:11] remove only return the answer without
[04:14] any
[04:18] explanation and the way you can start it
[04:21] is LM eval
[04:23] run but if you want to overwrite
[04:25] anything if you just do L EV run it runs
[04:28] everything but if you do like prompts
[04:30] equals math then it's only going to run
[04:32] the math example if you do n
[04:36] tries one then it's just going to do one
[04:40] sample by default we do five
[04:44] samples so so we get like a better read
[04:46] on the stability of of each test but it
[04:48] might be too much for you but you can
[04:50] override anything you can find
[04:53] these default settings here in the LM
[04:56] eval
[04:57] yaml and but let's try try to run this
[05:00] and see what happens and so this ran
[05:02] across CLA gbt 4 and and gbt 3.5 once so
[05:07] we can go in and generate a
[05:11] report and say like actually something
[05:13] failed what was the failed so let's take
[05:16] a look at the output here and in this
[05:18] case because we removed our prompt
[05:21] engineering gbt 3.5 starts being a bit
[05:24] chatty and says like 4.5 equals 9 Claud
[05:27] does something similar it comes right
[05:29] out the wres out the
[05:31] equation and now I'm going to try to
[05:35] revert and see let's let's get this
[05:38] in and we try to run one more
[05:44] time great now when we CH the report I
[05:47] can say some test failed but the most
[05:49] recent test that ran passed so when you
[05:52] do the report it's going to generate
[05:54] like a summary going to generate a
[05:55] report per per run but then also say
[05:59] overall all was there anything that that
[06:00] failed out of these
[06:03] reports if you want to go a bit more
[06:05] advanced let's say you want to use tools
[06:09] we we have an example here where we are
[06:11] generating some python code and again we
[06:14] had to add a number of different um
[06:16] Clauses to make sure that it only
[06:18] outputs python it tends to be very happy
[06:20] generating um surrounding
[06:23] explanations uh so in this case we are
[06:26] going to see whether or not um
[06:30] it returns an actual Python program that
[06:32] could be that be parsed so let's try to
[06:34] run
[06:36] that if you go in and take a look at
[06:38] this
[06:40] report you can see that these tests
[06:42] actually end end up passing our tool
[06:45] use and to to round
[06:47] up we have model based evaluation as
[06:50] well where you can test using other
[06:54] models and so in this case say with
[06:57] grading we can go in and to find like a
[07:00] full set of criteria here we're
[07:03] evaluating mermaid diagrams giving a
[07:05] score between 1 and five and the reason
[07:09] and that that is also supported in LM
[07:11] eval one thing about the previous
[07:14] approach is that it takes quite an AM
[07:16] amount of work to set up these tests and
[07:19] gather your test cases and one really
[07:22] compelling answer to evaluation has been
[07:24] model based
[07:25] evaluation and it's uh it's a setting
[07:28] where you have typically a larger model
[07:31] discriminate or kind of grade or be a
[07:33] judge over the output from another llm
[07:36] and that makes it so you can get more
[07:38] nuanced output like pass fail or a grade
[07:42] from 1 to five or preferences between
[07:44] different options and it's reasoning
[07:46] behind it there's a number of pitfalls
[07:49] unfortunately around this approach
[07:52] around biases towards the output from
[07:55] the model itself if you're sweeping
[07:56] different models they tend to prefer
[07:58] their own output
[07:59] then I'm very good at giving Point
[08:01] scores saying I think between 0 and one
[08:05] or larger scores between Z 0 and
[08:08] 100 but there are different ways where
[08:11] you can start increasing the accuracy of
[08:14] the kind of feedback that's been
[08:16] generated and we've been working on this
[08:19] where you basically start bridging
[08:21] between model based and human feedback
[08:24] so instead of removing the human
[08:26] completely from the feedback you start
[08:28] taking in all feedback that might have
[08:30] been given prior and start modeling it
[08:33] and say like if you have all the
[08:35] feedback from John then we create an
[08:37] autog John that will start create
[08:39] generating feedback for review um for
[08:42] any incoming completions and so in this
[08:44] case here we have two pieces of feedback
[08:46] that's been already given by human see
[08:48] here it was overall just score five or
[08:53] here just like a bit more
[08:54] nuanced but here we are kind of pending
[08:57] feedback and if you click this
[09:00] we have ai suggested an answer to to
[09:05] this and that's all I had today um if
[09:08] you want to get started on um llm e we
[09:11] have our documentation at our usual
[09:13] documentation site and you can find me
[09:16] at Nicholas cord on X or forly forly
[09:20] known as Twitter or should be an email
[09:22] at Nick atlock 10. thank
[09:26] [Music]
[09:28] you
