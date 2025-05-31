---
type: youtube
title: Creating and scaling your own custom copilots with Azure AI Studio: Hanchi Wang
author: AI Engineer
video_id: NjNEdjDvKu8
video_url: https://www.youtube.com/watch?v=NjNEdjDvKu8
thumbnail_url: https://img.youtube.com/vi/NjNEdjDvKu8/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning Tools
tags: ['AI Development', 'Prompt Flow', 'Assistant API', 'Code Tracing', 'Model Monitoring', 'Python', 'Cloud Integration', 'OpenAI', 'Software Development', 'AI Tools', 'Machine Learning', 'Azure']
entities: ['Anshul', 'Microsoft', 'Prompt Flow', 'Assistant API', 'OpenAI', 'Python', 'GitHub', 'Azure']
concepts: ['AI Development', 'Code Tracing', 'Model Evaluation', 'Monitoring', 'Tool Integration', 'Natural Language Processing', 'Cloud Computing', 'Software Development']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic Python programming skills', 'Familiarity with AI/ML concepts', 'Experience with cloud platforms like Azure']
related_topics: ['Machine Learning', 'Cloud Computing', 'Software Development', 'AI Ethics', 'Data Analysis', 'System Monitoring', 'API Integration', 'Open Source Tools']
authority_signals: ['as a engineer you might be wondering what is the best way to test this application', 'critical for developers to understand how the code really runs', "this is a public interface of the chat bot and it's just a typical function"]
confidence_score: 0.85
---

# Creating and scaling your own custom copilots with Azure AI Studio: Hanchi Wang

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=NjNEdjDvKu8)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: azure ai, ai development, machine learning, devops, cloud computing, ai integration, application monitoring  

## Summary

# Summary of "Creating and Scaling Your Own Custom Copilots with Azure AI Studio"

## Overview  
Hanchi Wang, a software engineer lead at Microsoft, discusses the development and scaling of custom copilots using **Azure AI Studio** and **Prompt Flow**. The talk emphasizes tools for building, testing, and monitoring AI-driven applications, with a focus on real-world examples like a chatbot for sales data analysis.

---

## Key Points  
- **Azure AI Studio** and **Prompt Flow** are central to building and scaling AI copilots.  
- **AI is not a plug-and-play solution**: Requires integration of tools, evaluation, and monitoring.  
- **Three core superpowers** enabled by Prompt Flow:  
  1. **Tracing/Instrumentation**: Capture inputs, outputs, and interactions with LLMs (e.g., OpenAI).  
  2. **Evaluation**: Assess model performance (e.g., identifying incorrect outputs like negative sales numbers).  
  3. **Monitoring**: Track application behavior in real time.  
- **Real-world example**: A chatbot app with two tools:  
  - A data fetcher (converts natural language to SQL queries).  
  - A code interpreter (executes Python code for analysis).  
- **Local testing**: Prompt Flow provides a UI for testing traces without cloud dependencies.  
- **GitHub repository**: Code examples are publicly available for experimentation.  

---

## Quotes  
- *"AI is not just a plug-and-play solution. It requires integration of tools, evaluation, and monitoring."*  
- *"Prompt Flow enables superpowers like tracing, monitoring, and evaluation."*  
- *"The chat history in the context allows the model to answer follow-up questions without re-stating previous inputs."*  

---

## Actionable Insights  
1. **Use Azure AI Studio** for building and scaling copilots with built-in tools.  
2. **Integrate Prompt Flow** for tracing, evaluation, and monitoring of AI workflows.  
3. **Implement tracing** with decorators to capture function interactions and LLM behavior.  
4. **Test locally** using Prompt Flow’s UI to debug and analyze traces.  
5. **Leverage GitHub** for code examples and experimentation.  

---

## Additional Notes  
- Azure AI Studio supports 20,000+ monthly enterprise customers.  
- Prompt Flow is open-source, enabling customization and local execution.  
- The chatbot example highlights the importance of evaluation to catch errors (e.g., incorrect data visualization).

## Full Transcript

[00:00] [Music]
[00:13] hello everyone my name is heni Wong I'm
[00:15] a software engineer lead at er AI of
[00:19] Microsoft and welcome to this talk um if
[00:23] 2023 is the year when the world
[00:26] discovered the Gen T AI then 2024 is the
[00:29] year or organizations truly began using
[00:31] and deriving basis values from this new
[00:34] technology and um I can actually go
[00:38] quick on some of the slides because
[00:39] satri showed some of them already but uh
[00:42] at at micro at Microsoft at AI is um
[00:47] helping a lot of customers and we
[00:49] definitely saw the E adoption
[00:52] accelerating um and our customers
[00:54] Enterprise customers arear lending their
[00:56] AI Solutions at the same time many other
[00:59] companies are just starting to explore
[01:01] what AI can do for them and um but like
[01:05] as AI Engineers you and I know that AI
[01:08] is not just a plug andplay Solutions uh
[01:12] it cannot be just tugged onto existing
[01:14] applications large language models need
[01:16] to integrate with domain specific
[01:19] knowledge and
[01:20] tools outputs of these models must be
[01:23] carefully filtered for Content safety
[01:26] and Sly
[01:27] evaluated moreover once the AI
[01:29] application is deployed Engineers must
[01:31] continuously monitor its performance to
[01:34] ensure it operates effectively um and
[01:37] Microsoft my team has developed a suite
[01:40] of comprehensive tools that enable
[01:43] Engineers to build their AI applications
[01:47] efficiently and today I'll introduce to
[01:49] you two of our products a studio and prf
[01:53] flow and describe how they help
[01:55] Engineers to build their own AI powered
[01:58] applications um Cedric show this a
[02:00] little bit already um and AI a AI
[02:04] portfolio is hosted on a AI Studio the
[02:07] development top for building AI
[02:09] applications within studio you'll find
[02:12] AI services like models cognitive
[02:14] capabilities and search giving you
[02:17] pre-trained API so that you can get into
[02:20] production faster we offer a machine
[02:22] learning for advanced the data science
[02:25] model training and full lrm Ops
[02:27] management we also have an to end Suite
[02:31] of tools to make AI systems trustworthy
[02:34] safe and secure and obviously last month
[02:38] at Microsoft build SAA announced the
[02:40] general availability of a AI Studio
[02:42] which is a big milestone uh we now have
[02:46] more than 20,000 monthly Enterprise
[02:48] customers using the
[02:49] platform and prf flow on the other hand
[02:54] uh complimenting the a studio provides
[02:57] SDK CI West code EX ension other
[03:00] developer tools to streamline endtoend
[03:03] development cycle of a applications it
[03:06] helps developers to build test trace and
[03:09] evaluate their applications with ease
[03:12] prf flow is 100% open source and free
[03:15] you can use it purely in a local setup
[03:18] without the need of an Adder account but
[03:21] it tast more powerful when used together
[03:23] with ADD Studio where you can track your
[03:26] assets traces service connections and
[03:28] Run results in the
[03:34] cloud and uh AI studio and the prom flu
[03:38] have so many amazing features I like to
[03:40] highlight three of their superpowers in
[03:42] this talk tracing and instrumentation
[03:45] allot developers to capture events from
[03:47] their applications and gain insights
[03:50] into what might have went wrong
[03:52] evaluation capabilities give you ways to
[03:55] improve your application for quality and
[03:58] safety and monitoring Ables developers
[04:00] to be proactive and have visibility into
[04:03] production
[04:05] workloads to show you a real world
[04:07] example here's an application my
[04:10] colleagues and I have built using add as
[04:12] studio and prom
[04:16] flow okay um it's a basically a chatbot
[04:20] app that helps to answer SE data
[04:23] questions for a outdoor equipment
[04:26] company I have some question questions
[04:30] prepared here
[04:32] already so that you don't need to see my
[04:34] awkward typing um but this app is using
[04:39] the assistant API and assistant API has
[04:42] access to two tools the first tool knows
[04:45] how to translate natural language
[04:46] question into SQ cury and fetch
[04:50] data uh and the second tool is a code
[04:53] interpreter tool which knows how to make
[04:57] use of that data and draw charts right
[05:00] and so this is the result of the first
[05:03] question and you can see it helps to it
[05:06] like it draw the chart and also
[05:08] explained what it is doing and we can
[05:11] also ask a followup question
[05:14] like oh oh okay sorry about that what's
[05:18] going
[05:22] on um
[05:42] do I need to duplicate it's either on
[05:44] mirror or extended mode if it's an
[05:46] extended mode you would have to move
[05:48] your item over oh okay maybe that will
[05:52] be
[05:53] easier where's that okay yeah you could
[05:57] do duplicate as well okay I'll do
[06:02] this
[06:05] um
[06:09] yeah name display
[06:21] here mirror
[06:25] okay okay cool and do I switch back once
[06:29] I I go back to my
[06:31] slides no because it's just mirroring
[06:33] from here to here okay okay cool that's
[06:36] good thank you cool um so yeah you can
[06:39] see that the question I asked is the
[06:41] show the sales data in 2024 by Mouse and
[06:44] ask you to draw a line chart right it
[06:45] just did that and I can ask a follow-up
[06:48] question like uh overlay that the bar
[06:52] chart with a line showing the percentage
[06:55] difference comparing to
[06:57] 2023 and what's cool about the assistant
[06:59] API is that it always has a chat history
[07:03] in the context so that I don't need to
[07:05] restate the previous question it has
[07:08] like everything um in the context right
[07:11] so that it hopefully will be able to um
[07:15] like answer that in a little
[07:18] bit
[07:22] okay thinking about this
[07:30] okay um this um and it did draw a line
[07:35] chart but like it's incorrect and uh it
[07:39] does happen from in my preparation so I
[07:41] had a backup plan which is like um this
[07:44] is actually the line chart and that's
[07:46] why actually it is important to do
[07:48] evaluation monitoring which is something
[07:50] I'll show next right but this is a
[07:51] correct line chart um unfortunately the
[07:55] numbers are all negative so looks like
[07:57] this company is not where doing not
[07:58] doing wor currently
[08:01] unfortunately um
[08:05] okay now going back to my
[08:08] slides okay
[08:12] cool and here's the sequence diagram of
[08:15] the app with the assistant API it has
[08:18] access to two tools the first one knows
[08:20] how to fetch data using the curate
[08:23] generate from a natural language
[08:25] question and second tool is a code
[08:27] interpreter and by adding prompt flow as
[08:30] a out layer of the application it
[08:33] enables superpowers like tasing
[08:36] monitoring as we will
[08:39] see okay uh before I show you the code
[08:44] uh can you guys see this link you can
[08:46] right a little bit Yeah so all the code
[08:49] I will show you can find it from this
[08:51] GitHub repository and you can like uh
[08:54] clone it and try it out
[08:57] yourselves tracing and instrument ation
[08:59] are top priorities for developers let's
[09:02] face it the code way developers right
[09:04] doesn't always run the way we expect
[09:06] right um so that's why it's critical for
[09:08] developers to understand how the code
[09:10] really runs let me show you the code of
[09:12] the chatbot app
[09:14] now if
[09:20] I
[09:23] okay
[09:25] oh um
[09:32] okay you don't see it
[09:34] right still
[09:38] in okay
[09:43] um okay so this is a public interface of
[09:46] the chat bot and it's just a typical
[09:49] function it takes a question from the
[09:51] user and returns a chat output here the
[09:55] only thing special here is the trace
[09:57] decator oh sorry about that provided by
[10:00] um prong flow and the trace decorator
[10:03] helps um to
[10:06] emate uh events uh emit traces to
[10:09] capture inputs outputs and events of
[10:12] Pyon function and also automatically
[10:15] captures any interactions with LM like
[10:18] Ed open
[10:19] Ai and I can also quickly show you the
[10:22] code for the sales data inside
[10:25] tool again it's nothing but the typical
[10:28] callable python class
[10:29] with the trace decorator here and with
[10:34] the um and for the second tool is a code
[10:37] interpreter which is the buil-in tool
[10:39] from the assistant API so there's no
[10:41] code for that and uh as a engineer you
[10:44] might be wondering what is the best way
[10:46] to test this application and look at
[10:49] traces prf flow provides a local UI just
[10:53] for that
[10:56] okay and to
[11:02] okay to start the UI this is a command
[11:06] you would run and it PF flow test and
[11:10] you point at point it at the chat
[11:13] completion function we were looking at
[11:16] earlier and I have already ran the
[11:19] command earlier so um here is the UI you
[11:23] can see it's running purely on my local
[11:25] machine and we can ask it a question
[11:32] like
[11:38] oops like the same question we were
[11:40] asking the chatbot
[11:42] app while this while this is
[11:46] running I can look at the
[11:49] traces already that is coming up it's
[11:52] still thinking about it so I can click
[11:56] fresh to see the upcoming traces
[12:01] um now looks like it has completed let's
[12:04] dig into the trace a little
[12:06] bit from the high level this is the out
[12:11] layer of the chatbot app you can see the
[12:13] input and output from the chat and uh we
[12:17] can look dig into the sales data inside
[12:20] tool a little bit and see that the
[12:22] assistant API actually modified the
[12:25] question a little bit and the the tool
[12:27] was able to apply the right output and
[12:31] if we really want to understand how the
[12:33] L was able to do that we can drill down
[12:37] even one layer deeper to see oh this is
[12:40] the question from the customer and this
[12:42] is autogenerated SQL
[12:46] query and lastly this is the code
[12:50] interpreter tool which writes some Pyon
[12:53] function and eventually draw the chart
[12:56] we were looking at
[13:00] here okay and what what I should point
[13:03] out is that all the instrumentation
[13:05] emitted by prom flow are open open
[13:08] Telemetry traces and events uh and open
[13:12] Telemetry is obviously uh industry
[13:14] standard that means you can configure
[13:17] your collectors to send the traces to
[13:20] your preferred destination like a
[13:22] monitor and it also means that if you
[13:25] have other part of your application
[13:27] already sending open dietry traces you
[13:29] can look at that and the traces sent by
[13:32] prompt flow at the single
[13:35] place and um you may also wondering like
[13:39] if I want to like collaborate with a
[13:41] colleague how do I do that on a local UI
[13:44] right and other AI Studio has that
[13:47] covered uh in my local environment I
[13:50] have configured
[13:52] my traces to go to
[13:55] the um er Studio already and that's how
[13:59] I got to this page and you can see it's
[14:02] the same Trace view on ER AI studio and
[14:05] I can simply copy and paste this URL and
[14:09] share with share it with
[14:12] someone
[14:15] okay coming back to
[14:20] this yeah that wraps up the first super
[14:23] power tracing uh the trace decorator can
[14:26] be added to any apps from single LM C to
[14:29] Rack function calling or single multi
[14:32] work agent workflows and it's framework
[14:36] agnostic prom flow provides a local UI
[14:39] for testing with Trace views to keep the
[14:41] traces for longer time or share with a
[14:44] colleague I can view the traces in ER
[14:48] studio now let's talk about evaluation
[14:51] focusing on application quality LM based
[14:55] application can be unpredictable uh a
[14:57] map fabric data or give incorrect
[14:59] responses impacting the application
[15:03] quality um and often like folks may want
[15:07] to like try out different models compare
[15:09] the pros and cons and see which one is
[15:11] the best for their application in terms
[15:14] of accuracy cost or performance um and
[15:17] if you recall the a lot of the Magic in
[15:20] the chatbot app happened in a single
[15:22] tool called sales data inside tool and
[15:24] that was able to kind of translate
[15:26] natural language questions into SQ cury
[15:29] using our MS let's see how we can
[15:31] evaluate
[15:33] that
[15:38] okay
[15:42] okay
[15:46] cool
[15:49] so the
[15:53] okay okay um due to the
[15:57] non-deterministic nature of our M it's
[16:00] running evaluation regularly is
[16:02] definitely critical and what's equally
[16:05] important is to have high quality test
[16:07] data set if you don't um proml has a
[16:11] suite of tools to help you to generate a
[16:13] synthetic test data set in my case here
[16:16] I have already prepared a test data set
[16:19] and the question column is what a user
[16:22] would ask the chatbot app and the ground
[16:26] choose column is what the sales data
[16:29] inside tool would generate based on that
[16:33] question okay let's also take a look at
[16:35] the evaluation
[16:36] code I'm using the evaluate function
[16:40] provided by prom flow for the
[16:42] evaluation uh sorry I'm using the
[16:44] evaluate function um provided by PR
[16:48] flow from this names space for the um
[16:52] evaluation evaluation logic here and
[16:55] theal function you can consider that as
[16:57] an execution engine that links the test
[17:02] data set and the target evaluation
[17:05] Target and evaluators together I like to
[17:09] focus on the evaluators here the first
[17:13] evaluator here is a Content safety
[17:16] evaluator that comes with a prf flow SDK
[17:18] it helps to act as a safeguard to make
[17:21] sure the cury and generated output are
[17:24] free of any harmful hateful or um uh
[17:29] violent content and the evalu the three
[17:32] evaluators following are customer
[17:34] evaluators which give me execution time
[17:37] error rate and S SEO similarity scores
[17:41] the S similarity scores is calculated
[17:44] based on how similar the gened S Cur is
[17:47] to the ground
[17:48] truths
[17:51] okay I have pre I have run a evaluation
[17:56] previously uh before this talk
[17:59] and I can look at the evaluation results
[18:02] briefly from the
[18:06] terminal but what is even better is that
[18:09] I can look at the evaluation result on
[18:12] either as studio for a better
[18:26] view okay
[18:30] I can see the aggregate Matrix at the
[18:33] top
[18:34] and
[18:36] okay if I
[18:39] refresh okay uh I can see the aggregated
[18:42] results at the top I can see my content
[18:44] safety Matrix here looks like I'm golden
[18:47] for that and parole level result below
[18:50] what's really cool about this page is
[18:52] that I can also look at traces for the
[18:56] evaluation in case I wonder how of the
[18:59] metrics might have be
[19:03] calculated okay uh Cedric in his talk
[19:06] showed the model cat log so I don't need
[19:10] to like talk too much about that but
[19:12] another scenario that um evaluation
[19:15] really shines is to compare across
[19:17] different models right obviously like
[19:19] you there are like more than 1600 models
[19:22] on other um a studio for the model
[19:25] catalog and I can look at like
[19:28] benchmarks right but what is even better
[19:31] like in my case is that I have a custom
[19:34] data set and I want to evaluate the same
[19:37] data set across different
[19:39] models I did just that earlier this week
[19:43] and here is the result I found a couple
[19:46] of popular models on the model catalog
[19:49] uh you can see the Cod here here three p
[19:51] 5 three mro uh llama and
[19:55] GPT and I uh in a list View
[20:01] I can pick a couple of them to compare
[20:03] for example I can pick the jpt 35 turbo
[20:07] G4 turbo and maybe Mr
[20:14] Large okay in this comparison view you
[20:16] can see that if I if we use the GPT 35
[20:19] turbo as the
[20:21] Baseline um M large has higher execution
[20:25] time which means it's slower but it has
[20:28] better error rate and higher SQL
[20:30] similarity
[20:32] score if we pull gp4 turbo into picture
[20:36] gp4 turo has the highest execution time
[20:38] which means it's the slowest am the
[20:40] three it has the same error rate
[20:42] compared to Mr Large and it has the
[20:45] highest c c similarity score so this is
[20:49] telling me that if speed is not a
[20:51] concern then GT4 turbo is still the best
[20:54] choice for my situation
[21:04] okay with the second uh super power I
[21:07] just showed you the evaluate function
[21:10] and the builtin evaluators like the
[21:13] content safety evaluator and also you
[21:16] can write your own customer evaluators
[21:19] using python
[21:21] function for the final superpow I like
[21:24] to concentrate on moving to production
[21:27] uh applic de deployment does not mean
[21:30] the job is done for an engineer on the
[21:32] contr it's the start of a New Journey
[21:35] it's a developers responsibility to
[21:37] continuously monitor the application to
[21:39] ensure the application always runs as
[21:42] expected and the developer needs to look
[21:44] at uh both the details for each
[21:47] individual request and also the overall
[21:50] Telemetry for the whole
[21:53] system and prf flow uh tracing since
[21:56] open Telemetry spans and events which
[21:59] can be collected by multiple tools
[22:01] including add application
[22:03] insights we deploy the chatbot app and
[22:06] started to collect traces in an
[22:08] application inser resource and build a
[22:11] dashboard here is the
[22:14] dashboard oops
[22:26] sorry okay um you can see there are
[22:30] performance metrix usage metrix and
[22:32] feure Metric on this dashboard and there
[22:35] are so many interesting insights we can
[22:37] draw from here I'll just highlight a
[22:38] couple uh for example the model duration
[22:42] is like basically the speed of the model
[22:44] right and GPT 4 Turbo has the highest
[22:46] number compared to other models which
[22:49] aligns with the evaluation result we
[22:50] were looking at
[22:52] earlier and for the token usage we can
[22:55] see majority of the tokens are actually
[22:57] used for the prompt uh and only a few
[22:59] are for the completion so if we are
[23:04] concerned about the cost then maybe we
[23:06] need to uh short The Prompt templates a
[23:09] little bit and the feure tells me like
[23:12] how many of the costs field and some of
[23:14] the specs may come from um some of the
[23:17] rehearsal I did earlier this week uh and
[23:20] if something really went wrong we can
[23:21] also like dig into a specific Trace to
[23:24] look at the same Trace View and the
[23:26] stack Trace
[23:29] okay
[23:31] and final slide uh this is just a
[23:35] glimpse of what's possible with eror AI
[23:37] studio and prom flow my team at eror AI
[23:41] is dedicated to provide an endtoend
[23:43] Suite of tools to make AI application
[23:46] building easy and efficient at the same
[23:49] time we also always have responsible AI
[23:52] in mind and provide Enterprise great uh
[23:55] scalability and Security account way to
[23:58] see what you do with a AI studio and PR
[24:01] flow thank you all
[24:04] [Music]
