---
type: youtube
title: BotDojo Launch: Enhancing AI Assistants with Evaluations and Synthetic Data
author: AI Engineer
video_id: PNjMwdCo_YM
video_url: https://www.youtube.com/watch?v=PNjMwdCo_YM
thumbnail_url: https://img.youtube.com/vi/PNjMwdCo_YM/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI development', 'BotDojo', 'LLM optimization', 'synthetic data', 'chatbot development', 'vector databases', 'AI evaluations', 'low-code AI', 'AI deployment', 'debugging AI', 'AI engineering', 'machine learning tools']
entities: ['BotDojo', 'Paul Henry', 'vector database', 'LLM', 'Grok', 'Claude', 'synthetic data', 'evaluations', 'batches', 'vector index']
concepts: ['AI enablement', 'synthetic data generation', 'chatbot optimization', 'vector indexes', 'low-code development', 'hallucination detection', 'AI deployment', 'debugging AI applications', 'AI engineer roles', 'evaluation methodologies']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Experience with LLMs (Large Language Models)', 'Familiarity with vector databases', 'Knowledge of low-code development tools', 'Basic coding skills (Python/Tie script)']
related_topics: ['AI deployment strategies', 'Synthetic data creation', 'Chatbot development', 'Evaluation metrics for AI', 'Vector database optimization', 'Low-code AI platforms', 'AI hallucination mitigation', 'AI engineering practices']
authority_signals: ["I'm the founder and have worked with teams deploying LLMs", 'We are an AI enablement company', 'This is battle tested']
confidence_score: 0.8
---

# BotDojo Launch: Enhancing AI Assistants with Evaluations and Synthetic Data

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=PNjMwdCo_YM)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai assistants, synthetic data, llm evaluation, vector database, ai deployment, chatbot testing, machine learning  

## Summary

# BotDojo Launch: Enhancing AI Assistants with Evaluations and Synthetic Data Summary

## Overview  
Paul Henry, founder of BotDojo, discusses how his company helps businesses deploy AI assistants reliably by combining synthetic data generation and evaluations. The video demonstrates a live demo of improving chatbot performance through vector databases, low-code tools, and automated testing.

---

## Key Points  
- **Challenges in AI Deployment**: Deploying LLMs for production is easy in theory but hard in practice, requiring robust tools for debugging and optimization.  
- **Synthetic Data & Evaluations**: BotDojo uses synthetic data to test and improve AI assistants, paired with evaluations to detect issues like hallucinations and data gaps.  
- **Vector Indexing**: The platform creates vector indexes to retrieve relevant data for chatbots, with real-time debugging capabilities.  
- **Low-Code Editor**: Supports JSON schema outputs (e.g., GPT-3, Claude) and allows tracing of each AI interaction for debugging.  
- **Batch Evaluations**: Enables testing of AI flows with large datasets, identifying performance bottlenecks and improving accuracy.  
- **Customizable Workflows**: Users can generate synthetic data, adjust models, and refine prompts to optimize chatbot responses.  

---

## Important Quotes/Insights  
- *"It's super easy to hook up a vector database with an LLM the weekend but really hard to get it production ready."*  
- *"Synthetic data is a trick that's been working well for customers—extracting questions and answers from support tickets to test chatbots."*  
- *"Evaluations check for hallucinations and data gaps, ensuring the AI provides accurate, relevant responses."*  

---

## Actionable Items  
- **Generate Synthetic Data**: Use customer interactions (e.g., support tickets) to create test datasets for AI training.  
- **Implement Batch Evaluations**: Run large-scale tests to identify and fix issues like hallucinations or data retrieval gaps.  
- **Leverage Low-Code Tools**: Utilize BotDojo’s editor for JSON schema support and real-time debugging of AI workflows.  
- **Optimize Vector Indexes**: Ensure vector databases are well-structured to improve retrieval accuracy.  

--- 

## Additional Notes  
The demo highlights the importance of iterative testing and synthetic data in refining AI assistants, with a focus on scalability and reliability for enterprise use.

## Full Transcript

[00:00] [Music]
[00:13] so hello my name is Paul Henry I'm the
[00:15] founder at bot dojo and as a previous
[00:18] CTO I was working with teams deploying
[00:21] llms applications for hundreds of
[00:23] thousands of customers and like many of
[00:25] you guys know it's super easy to hook up
[00:27] a vector database um with an llm the
[00:30] weekend but really hard to get it
[00:32] production ready and so that's what we
[00:34] do we are an AI enablement company and
[00:37] we let companies deploy AI to
[00:40] prod live demo
[00:42] time all right so today I'm going to
[00:44] show you a demo of a product we're going
[00:47] to take uh synthetic data that we're
[00:49] going to generate and we're going to
[00:50] combine it with evaluations to see how
[00:52] we can improve the performance of a
[00:55] chatbot or at least that's what I hope
[00:57] happens all right
[01:00] so I'm going to open up our template of
[01:03] our uh a chatbot and we have customers
[01:05] live that are using this template it's
[01:07] kind of battle tested um and so let's
[01:09] test it
[01:13] out how do I create a vector index in
[01:19] bot
[01:22] Dojo okay and as you can see all the
[01:25] little nodes are lightened up as they
[01:27] execute um we're taking the question
[01:29] we're looking at the chat history we're
[01:30] going to the vector database to retrieve
[01:33] the information and then we're answering
[01:35] it with a AI model so if I pulled this
[01:37] up you can kind of see in our low code
[01:39] uh editor this is the prompt that we're
[01:41] sending to the llm we're getting the
[01:43] results out here and we also support uh
[01:46] J uh Json schema so if the model
[01:50] supports Json output like um grock um
[01:53] Claud and all that stuff then we just
[01:55] conform to that um one key thing is you
[02:00] can pull a trace of each node and see
[02:03] exactly what we sent to the llm what
[02:06] came from the retriever the exact you
[02:08] know data which has been super useful
[02:09] for debugging apps all right and cool we
[02:12] have an image it's got citations we
[02:15] should ship
[02:16] it that was supposed to be a joke but
[02:18] all right um so this is where
[02:22] evaluations come in so I'm going to
[02:24] demonstrate um the valuations that I
[02:27] previously Ran So we have a a feature in
[02:30] bot Dojo uh called batches which allow
[02:32] you to run a whole bunch of questions
[02:33] through your chatbot or your AI flow and
[02:37] um run evaluations to kind of see how
[02:38] things are doing so if you can see this
[02:41] we have a few uh five evaluations that
[02:43] we ran there's a little bit of red um
[02:46] that's because uh we don't have enough
[02:47] information from our Vector database um
[02:49] it also checks for things like
[02:51] hallucinations so let's try to fix that
[02:54] and so I'm going to clone this batch I'm
[02:57] going to rename it with
[03:00] generated data I'm going to increase the
[03:03] throughput a little bit because of time
[03:06] and um I had I don't have enough time to
[03:09] generate all the data for this demo so
[03:11] um the previous ran was filtering out
[03:14] the generated data and so I'm going to
[03:15] remove the filter that we're passing
[03:17] into the uh flow so it takes in the
[03:20] generated data you can also change the
[03:22] model and all that kind of stuff to see
[03:24] how it
[03:25] performs all right so why that guy is
[03:29] running I'm going to open up another
[03:31] flow and so this is the actual flow that
[03:35] we uh generated that uh synthetic data
[03:37] and so let me
[03:38] uh let me run this one real
[03:42] quick and so this particular flow takes
[03:45] in multiple inputs and so I'm going to
[03:47] paste in uh some Jon from a previous
[03:51] run and what this is going to do is it's
[03:54] kind of a trick that's been working well
[03:55] for customers is where you take um you
[03:58] extract questions and answers from
[03:59] support tickets so these are live agents
[04:01] talking with customers and you use this
[04:04] as a test data to send it through your
[04:07] chatbot and um we take relevant
[04:09] information from the existing index and
[04:11] we have it write a document um and so it
[04:14] it uses the same writing style and it um
[04:17] you know and then we do an inline CIT uh
[04:20] evaluation to where we check to see if
[04:22] the document has enough information to
[04:23] answer the question and then we also
[04:25] have a code node here where you know a
[04:27] lot of times when you're using these low
[04:29] codes editors there's like situations
[04:31] where you have 40,000 different um boxes
[04:34] and so when you have to do write code we
[04:36] support um ties script and and soon uh
[04:39] python but you can see that hey we're
[04:41] getting the information and we're right
[04:42] into the vector
[04:44] index all right running out of time okay
[04:48] let me go back to the support chat bot a
[04:51] moment of truth so I'm going to compare
[04:54] um the the batch that we ran before with
[04:56] the new
[04:57] stuff and 27
[05:00] seconds
[05:03] oh you do it you do it 15 times and it
[05:06] doesn't
[05:09] work 10 n we're also hiring so if you're
[05:12] an AI
[05:13] engineer help help us fix this all right
[05:16] there he comes okay all right one second
[05:19] left it's all green so it improved the
[05:21] uh you know measely improved something
[05:23] so uh thank you um bot dojo.com check us
[05:26] out thanks
[05:30] [Music]
