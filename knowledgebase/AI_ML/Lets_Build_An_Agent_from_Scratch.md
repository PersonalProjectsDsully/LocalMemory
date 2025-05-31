---
type: youtube
title: Lets Build An Agent from Scratch
author: AI Engineer
video_id: xzXdLRUyjUg
video_url: https://www.youtube.com/watch?v=xzXdLRUyjUg
thumbnail_url: https://img.youtube.com/vi/xzXdLRUyjUg/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: []
entities: ['OpenAI', 'GPT-3', 'LLM', 'AI', 'search API', 'tool calls', 'Time Square', 'Furlin hoodie', 'utils folder']
concepts: ['Large Language Models (LLMs)', 'AI', 'tool calls', 'parallel processing', 'text transformations', 'deterministic processes', 'refactoring', 'AI as judge', 'LLM as critic', 'API integration']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Programming fundamentals', 'APIs and web services', 'AI/ML basics', 'Python or similar language', 'OpenAI API experience']
related_topics: ['Machine Learning', 'Natural Language Processing', 'API Development', 'Software Architecture', 'AI Ethics', 'Data Processing', 'Cloud Computing', 'Algorithm Design']
authority_signals: ['"this feels very deterministic"', '"we are asking the same llm to go and evaluate"']
confidence_score: 0.7
---

# Lets Build An Agent from Scratch

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=xzXdLRUyjUg)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai agent development, llm integration, code experimentation, agent frameworks, tool integration, machine learning, software development  

## Summary

```markdown
# Summary of "Let's Build An Agent from Scratch"

## Overview
This video walks through the process of building a simple agent using a combination of language models (LLMs), memory, planning, and a while loop. The goal is to demonstrate how to create a deterministic, mechanistic system that can interact with external tools (e.g., APIs) and evaluate results. The speaker emphasizes hands-on learning by encouraging viewers to run and modify the code, while highlighting the importance of understanding the underlying components of agents.

## Key Points
1. **Defining an Agent**  
   - An agent is composed of:  
     - **LLM** (for decision-making and planning).  
     - **Memory** (to store and retrieve context).  
     - **Planning** (to break tasks into steps).  
     - **While loop** (for iterative processing).  

2. **Core Components**  
   - **Memory as Read/Write**: Stores and updates information during interactions.  
   - **While Loop as Conditional Loop**: Continues processing until a task is resolved.  

3. **Step-by-Step Process**  
   - **LLM Call**: Initial prompt to the model for task execution.  
   - **Condition Check**: LLM acts as a "judge" to validate if the current output meets requirements.  
   - **Tool Integration**: Example: Using a Google search API to fetch real-world data.  
   - **Tool Handling**:  
     - Parsing and validating tool inputs (e.g., location constraints).  
     - Recursing through tool calls until the LLM is satisfied with the result.  
   - **Parallel Tool Calls**: Refactored to handle multiple simultaneous tool requests.  

4. **Deterministic Nature**  
   - The system is designed to be predictable and rule-based, with the LLM making decisions based on predefined logic.  
   - Example: Evaluating if a search API result answers a query (e.g., "Where to buy a fur-lined hoodie near Times Square").  

5. **Code Refactoring**  
   - Separating `complete_with_tools` into a utility file for modularity.  
   - Supporting parallel tool calls with unique IDs to trace responses.  

6. **Tools as Text Transformations**  
   - Tools are treated as functions that convert input text to output text (e.g., search queries to results).  

## Important Quotes/Insights
- "The process feels very deterministic... the LLM acts as a judge to evaluate tool responses."  
- "Tools are best handled by thinking of them as text transformations."  
- "The goal is to understand the building blocks of agents, not just abstract concepts."  
- "The LLM is both the planner and the evaluator, ensuring the system iterates until it meets the task requirements."  
```

## Full Transcript

[00:01] hi I'm Cam and I welcome you to my talk
[00:05] on how to build an agent so I have three
[00:08] goals for this talk I want you to
[00:10] experience the simplest version of what
[00:13] an agent could be um and I want you to
[00:16] feel comfortable in running and breaking
[00:19] the included code um I think the the
[00:22] running and breaking is very very
[00:24] important part to the learning um and I
[00:27] also want you to take away uh an
[00:29] intuition
[00:30] for how agents work or how other
[00:33] Frameworks work if you choose to go with
[00:35] some agent framework that's great um I
[00:38] want you to have some understanding of
[00:40] maybe the underlying the underpinning
[00:43] building blocks that they used to make
[00:45] it work so with that let's get to some
[00:47] slides okay great this is where you can
[00:50] find me on LinkedIn this is where you
[00:52] can find the slides for this talk and
[00:54] the code I really encourage you to go
[00:56] and grab the code try it run it break it
[01:00] see where this code begins to turn from
[01:04] deterministic outcomes to a feeling that
[01:07] you're starting to starting to play with
[01:09] an agent so what is an agent uh I really
[01:12] like both of these definitions uh agent
[01:14] llm memory planning tools and a while
[01:17] loop um so let's break that down a
[01:19] little bit more so mathematically we
[01:20] could uh take memory and say oh actually
[01:23] this is a both a read and a write
[01:25] operation and also on the while loop um
[01:28] it's really a conditional and the loop
[01:29] looping so we can uh break those apart
[01:32] reorder them a little bit and come up
[01:34] with the plan for what we're going to do
[01:36] and so with all of that out of the way
[01:38] let's jump in and get to the code
[01:40] finally all righty so let's Jump Right
[01:43] In so the first step here is uh calling
[01:46] an llm this is straight from the open AI
[01:50] uh hello world docs right uh standard
[01:54] chat completion and we can run it
[01:57] here Step Zero okay
[02:02] um this should be pretty standard for
[02:05] most people so far okay great um then
[02:08] let's jump to the step one the condition
[02:11] so um here we're going to have the same
[02:14] completion
[02:16] call um checking for the prompt but then
[02:20] once we get the answer back we're going
[02:22] to make another llm call that's going to
[02:25] work as an llm as judge right we are
[02:27] going to ask your strict critic give the
[02:30] following question determine if the
[02:31] answer is a full answer to the question
[02:35] question answer okay um and then we give
[02:38] it a forced um Json strict response of
[02:44] um whether it's done or not and you can
[02:46] see the object here is whether it's done
[02:48] it's going to be a Boolean and the
[02:50] original question is what is the average
[02:52] Wing speed of a swallow so we can go in
[02:55] and we can run step one to see how it
[02:59] works with a
[03:01] condition so um it gives me llm is judge
[03:05] gives me a thumbs up that's great here's
[03:07] the answer coming back from the LM so so
[03:10] far very deterministic very mechanistic
[03:13] in its uh outputs and then the judgment
[03:16] and then the response to the to the user
[03:19] so um The Next Step here is tools um and
[03:23] we are incorporating Ser AI I think I'm
[03:25] pronouncing that correctly this is a
[03:27] Google search API uh service um and they
[03:32] basically make Google search API easy
[03:36] Json um API versus dealing with whatever
[03:39] the the Google API nonsense
[03:42] is so I'm asking about buying a hoodie
[03:45] and New York and um near Time Square and
[03:48] the like again going to have the same
[03:50] conditional I'm going to now have this
[03:53] search Google tool right and you can see
[03:55] the Ser um get Json call here engine is
[04:00] Google passing in the API key with a
[04:04] query um anal loation I'm defaulting to
[04:07] Philadelphia from the location of where
[04:10] to start the query
[04:12] from and then I'm going to print the
[04:14] results um the tool config going into
[04:18] open AI looks like this and so I'm I'm
[04:22] handwriting out this Json so that we can
[04:24] inspect it a little bit um we're
[04:26] defining the name of the function we're
[04:28] going to call giving it descriptions um
[04:31] strict whether it uh strictly adheres to
[04:34] the the schema here um and then the
[04:36] parameters into the tool call so there's
[04:38] a query and a location um and which
[04:41] elements are required and if there's any
[04:44] additional ones so this is the Json that
[04:46] gets generated and passed in um when we
[04:49] make our call um the other thing to note
[04:52] with tool
[04:53] calls is that we call the llm the tool
[04:56] call kicks back and tells our local code
[04:59] what
[05:00] tool to call or which tools to call and
[05:03] what uh parameters are included in there
[05:06] so we need to handle that that's not
[05:08] handled by the open AI SDK um and we
[05:11] need to look into the tool call if there
[05:13] are tool calls in this case we're only
[05:15] doing a single one we'll get to parallel
[05:17] uh in a few minutes um and then we go
[05:21] and we make that tool call um off of uh
[05:26] an array here on tools which includes
[05:28] the search Google um passing in the args
[05:32] and then we uh push those both the tool
[05:36] call and the response from the tool call
[05:38] back to the conversation and then we can
[05:41] um complete with tools again meaning in
[05:44] this case we are recursing through and
[05:47] calling uh back to the llm with those
[05:50] responses passed in as those args which
[05:53] it'll then make another determination so
[05:55] um so main Loop here um complete with
[05:58] tools The Prompt search Google tool
[06:02] config and then um it responds back and
[06:06] then it'll see It'll internally loop on
[06:10] tool calls until it is satisfied and the
[06:12] llm is satisfied and then result come
[06:15] back out and then here the critic will
[06:19] come and perform uh condition again so
[06:22] let us go here let us
[06:25] run step two on the tool
[06:31] unhandled rejection uh
[06:39] oh okay it looks like we failed there
[06:42] due to um validation constraint on the
[06:45] location parameter it doesn't take just
[06:47] any string it takes a specific set of
[06:49] strings um in this case the llm as judge
[06:52] gave us a thumbs up again um again this
[06:55] feels very deterministic we are um
[06:58] asking an llm to determine that it needs
[07:00] to call a search API and we're asking
[07:04] the same llm to go and evaluate whether
[07:07] that search API returned text that was a
[07:11] reasonable answer to where I could buy a
[07:13] furlin hoodie near Time Square so um of
[07:17] course still very mechanistic very um
[07:20] deterministic very um straightforward in
[07:24] its in its
[07:25] outcomes um okay but then let's take the
[07:28] next step let's go to step three and in
[07:30] this case um a little refactoring is in
[07:32] order um so same prompt around um
[07:36] wanting to buy a a hoodie fur lined
[07:38] hoodie um we've pushed the complete with
[07:42] tools into a other into a utils folder
[07:47] so into another file um just to get it
[07:50] out of that main this still has that
[07:53] same looping but in this case we've
[07:55] written this so that it can do the
[07:57] parallel tool calling um these tool
[07:59] calls could come back with multiple
[08:03] right this could be an array of tool
[08:04] calls that the llm is asking the the US
[08:08] to perform the client to perform and so
[08:11] we're uh promising all over the tool
[08:14] calls and we are um passing in the
[08:18] function Arguments for each of the tool
[08:20] calls um
[08:23] into the tool functions um here and then
[08:27] we are then pushing the response
[08:30] from this local function that we've
[08:33] called back into uh the conversation and
[08:37] this will have a tool call ID so that
[08:39] the llm is able to trace um I asked for
[08:42] this tool to be called and here's the ID
[08:45] and then here's the response of that
[08:46] tool call so sometimes it asks for the
[08:48] same tool to be called multiple times
[08:50] with different input parameters right so
[08:53] that's how that works um the tools um
[08:57] are configured so for example in the
[08:59] search Google
[09:01] example we're passing in this
[09:04] query um as an object and it's
[09:07] performing the query and it's returning
[09:09] a string result um in my mental model uh
[09:13] the tools are are best handled by
[09:17] thinking of them as text Transformations
[09:19] you might have a couple of different
[09:21] parameters going in but usually string
[09:23] to string is sort of the core of what uh
[09:26] these tools are performing um so that
[09:30] was the AI and the the completions uh
[09:34] the sorry the complete with tools on the
[09:37] refactor um and so that is here and then
[09:41] we are outputting the result um and then
[09:44] we are running the same llm as judge so
[09:49] we can run that again that'll give us
[09:52] the step three um that'll give us some
[09:56] additional looping and parallel tool
[09:59] comp
[10:07] in all righty llm is Judge thumbs up
[10:10] again okay great here are a couple of
[10:12] those sites again though still feels
[10:15] very deterministic we just reshuffled
[10:16] things around shouldn't have been too
[10:18] big of a difference this is where we are
[10:20] going to really feel an inflection here
[10:23] so um the biggest change on step four
[10:26] for planning is creating a to-do list
[10:29] and this now solves both the read the
[10:33] write and the planning aspect um the
[10:37] while looping aspect that we talked
[10:39] about is covered by the llm itself right
[10:43] in making a tool call and then having us
[10:47] reply back with the result of that tool
[10:49] call the llm is able to keep iterating
[10:53] and keep um operating on the code that
[10:57] we are or the prompt that we gave it and
[11:00] keep working through towards a solution
[11:03] um there are cases when that llm can
[11:06] just iterate forever calling tools and
[11:09] never converging is particularly if we
[11:12] keep pruning the context window and we
[11:14] never hit some error or boundary
[11:17] condition um some guardrails I've seen
[11:20] get put on or the number of uh iterative
[11:22] Loops that they're able to go through
[11:25] before um client code kind of cuts them
[11:28] off and says like okay L uh you're drunk
[11:31] go home um so in this case though we
[11:34] don't have that set up um but we have
[11:37] added this to-do list which has what you
[11:40] would expect from a standard hello world
[11:44] to-do list right you can add things to
[11:45] your to-do list and in this case we have
[11:48] the also the tool config for the to-do
[11:50] list of adding new to-dos that's an
[11:53] array of to-dos right there'll be an
[11:54] array of to-dos and we'll have array of
[11:56] done um so you can add new to-do and
[11:59] they get pushed onto the to-do list and
[12:01] then we're just printing it out and then
[12:03] we're returning the to-dos that were
[12:06] added to the to-do list um then we can
[12:10] also Mark to-dos as done um and so if a
[12:15] to-do is included in the to-do list um
[12:18] Market is done and pull it out of the um
[12:23] to-dos that are there um so that we
[12:26] don't have to do it again um as well as
[12:29] the config for that um and then the
[12:32] check done we can see if uh we have
[12:36] completed all of the to-dos um if the
[12:41] length is zero then it'll say no tasks
[12:43] have been marked done um and then the
[12:46] config for that as well and then check
[12:49] to-dos so it's able to get all the
[12:51] to-dos that are on the to-do list so
[12:54] again sort of standard to-do list um and
[12:57] now with all of the those tools the the
[13:02] LM is Judge the search Google I guess I
[13:05] should cover this this brows web very
[13:08] similar to the search Google right it
[13:09] takes in a
[13:10] URL um it's using Cheerio and turn down
[13:14] and we are uh requesting that URL here
[13:18] um and if the response comes back uh 200
[13:21] then it's just taking the
[13:23] text using turn down to turn it into
[13:26] markdown and returning that mark down um
[13:30] out of the tool so very simple operation
[13:33] given that URL right so given that the
[13:36] planning will then take the to-do list
[13:39] that is generated based on the prompt
[13:42] right so this is where the programming
[13:44] of the agent begins to take over right
[13:47] you're helpful assistant working for a
[13:48] busy executive your tone is friendly but
[13:50] direct they prefer short clear and
[13:52] direct writing you try to accomplish
[13:54] specific task you given you can use any
[13:56] of the tools available to you before do
[13:59] any of your work you always make a plan
[14:01] to use your to-do list right so that's
[14:03] driving the planning towards the to-do
[14:05] list uh you can mark to-dos off of your
[14:07] to-do list after they've been complete
[14:09] you summarize the actions you took by
[14:10] checking the to-do list then create a
[14:11] report you always ask your assistant to
[14:15] check goal done that drives towards llm
[14:18] as judge if you say you are done you
[14:20] send the report to the user if your
[14:21] assistant has feedback you add it to
[14:23] your to-do list and then I've added it
[14:25] to today's date because sometimes the
[14:27] llm doesn't quite know when in time it
[14:30] is which is quite amusing and in this
[14:32] case since we've pushed llm as judge as
[14:35] a tool right the condition can be a tool
[14:37] itself the loop is handled by the LM
[14:40] itself then this main function is just a
[14:43] single call to this complete with the
[14:45] tools and then we're going to respond
[14:47] with our answer so um oh and the the
[14:51] default here is I want to learn about
[14:52] building agents without a framework so
[14:55] let us try that we can mpm run
[15:00] step
[15:01] four and see how it goes I want to learn
[15:04] about building agents without a
[15:05] framework okay it's calling the ad
[15:07] to-dos so here it came up with a plan
[15:10] these are the news to-dos right um
[15:12] search for information about building
[15:14] agents without a framework summarize key
[15:15] points from the search results and then
[15:17] you ask the assistant to check if the ex
[15:19] explanation is sufficient um it's
[15:22] calling check todos calling search
[15:25] Google about this it's browsing this
[15:28] blog post it's
[15:30] browsing this Pond data browsing the web
[15:34] browsing the web here's a bunch of
[15:36] markdown from that
[15:38] website um it's marking done summarizing
[15:43] key points from the search results it's
[15:46] checking to-dos it's checking gold
[15:49] done it's giving it uh LL as judge gives
[15:52] it a thumbs up okay great thumbs up
[15:54] we're we are done oh so here is a
[15:56] summary of building an agent without
[15:58] using a framework to build an agents
[16:00] without framework follow these steps
[16:01] unstore core components recognize that
[16:03] an AI agent is a language model capable
[16:05] of tool use and maintaining
[16:06] conversational context Define tools
[16:09] tools are functions for environmental
[16:11] interaction um like database queries web
[16:13] search okay that's tools that's
[16:17] memory um a loop uh input processing
[16:21] tool decision execution response
[16:23] formulation prompt engineering direct
[16:26] API calls uh this is a good one instead
[16:29] of trying to pass through the llm but
[16:31] just directly store State and call it
[16:32] for yourself um so I feel like this is
[16:34] pretty decent um you know where I've
[16:37] started to see
[16:39] some um real interest in this LM uh or
[16:44] this agent that I've built is uh doing
[16:46] some things like uh I am planning a date
[16:51] with my wife this
[16:57] Saturday um
[16:59] here more
[17:02] yay please
[17:04] help help
[17:07] me
[17:10] find some
[17:12] activities and
[17:18] dinner 6m and 11
[17:22] p.m. um let's see how it does um
[17:29] so searching for local activities here's
[17:31] the plan again finding a good dinner
[17:34] option uh searching
[17:37] Google best restaurants browsing the
[17:42] web lots of
[17:45] markdown marking things as
[17:47] done checking the
[17:49] [Music]
[17:53] goal
[17:55] okay here are some of the activities
[17:59] ities here are the some of the dinner
[18:01] options and hopes that I have a lovely
[18:04] evening so it's not that this uh this
[18:08] agent is perfect by any means but
[18:11] hopefully you can see how adding each of
[18:14] these components from the llm call the
[18:17] conditional the tool use um adding some
[18:21] planning some read write in that to-do
[18:23] list and how we can really leverage some
[18:26] of those things coming together and
[18:27] start to produce something that's that's
[18:29] quite interesting you could see how next
[18:31] steps could be adding a vector database
[18:34] or injecting these um browsed um web
[18:38] pages into um you know a chroma DB in
[18:42] memory or into something into a more rag
[18:45] likee system so hopefully this was
[18:47] really helpful and uh hopefully this
[18:50] gives you some interest or excitement in
[18:53] how to dive in and uh do this
[18:57] yourself okay great
[18:59] thanks for coming to my talk uh again
[19:02] I'm cam Lasser you can find me on
[19:03] LinkedIn here the slides are up on my
[19:06] personal site and the code is up on
[19:08] GitHub I encourage you to take it for a
[19:11] spin uh let me know what you think let
[19:13] me know if uh there's some improvements
[19:14] you could make or if uh something like
[19:17] this is exciting we're always uh
[19:19] building and looking for people who are
[19:21] interested to build uh agents for for
[19:25] our customers so again see you online
[19:27] cheers
