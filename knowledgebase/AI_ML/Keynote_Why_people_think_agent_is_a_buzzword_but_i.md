---
type: youtube
title: Keynote: Why people think "agent" is a buzzword but it isn't
author: Channel Video
video_id: D6v5rlqUIc8
video_url: https://www.youtube.com/watch?v=D6v5rlqUIc8
thumbnail_url: https://img.youtube.com/vi/D6v5rlqUIc8/mqdefault.jpg
date_added: 2025-05-26
category: General
tags: ['tutorial', 'general']
entities: ['Keynote: Why people think "agent" is a buzzword but it isn\'t']
concepts: []
content_structure: tutorial
difficulty_level: intermediate
prerequisites: []
related_topics: []
authority_signals: []
confidence_score: 0.3
---

# Keynote: Why people think "agent" is a buzzword but it isn't

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=D6v5rlqUIc8)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai agents, machine learning, artificial intelligence, agent systems, ai research, coding agents, agent definition  

## Summary

# Summary of "Why 'Agent' Is a Buzzword (But Not Really)" by Chip

## Overview  
Chip, an AI infrastructure expert and author of a book on agents, discusses the potential and challenges of AI agents. He argues that while "agent" is a buzzword, its true value lies in solving complex, multi-step tasks. However, building reliable agents is difficult due to task complexity, failure rates, and the need for robust tooling. The talk emphasizes the importance of addressing these challenges to unlock new use cases.

---

## Key Points  
- **Definition of an Agent**:  
  An agent is a system capable of performing tasks autonomously, often through a sequence of steps. Chip references the definition from Stuart Russell and Peter Norvig, emphasizing that agents must interact with environments and make decisions.  

- **Challenges in Building Agents**:  
  - **Task Complexity**: The likelihood of failure increases with task complexity. For example, a 2% error rate per step can lead to an 80% failure rate over 10 steps.  
  - **Multi-Step Dependencies**: Even simple tasks (e.g., "How many people bought product X last week?") may require 4+ steps, increasing the risk of errors.  
  - **Limited Scalability**: Most agents struggle with tasks requiring more than 5 steps, limiting their practical use.  

- **Importance of Actions/Tools**:  
  Agents must leverage tools (e.g., APIs, databases) to handle complex tasks. For instance, a chess agent requires access to game rules and move databases.  

- **Why Agents Aren’t Widely Used**:  
  Despite potential, agents are hard to implement due to the difficulty of managing complexity, ensuring reliability, and aligning with economic value. Simple tasks often don’t justify agent use.  

---

## Key Quotes  
- *"The more steps there are, the more complex queries, the higher number of steps, and the more likely the agent is going to fail."*  
- *"Agents are not widely used because doing agents is really really hard."*  
- *"Enabling agents to handle more complexity will unlock many new use cases."*  

---

## Actionable Takeaways  
1. **Address Task Complexity**: Focus on tasks with the right level of complexity to avoid failure.  
2. **Expand Agent Environments**: Provide agents with access to tools and data to handle multi-step tasks.  
3. **Benchmark Complexity**: Use synthetic benchmarks (e.g., CTIC dataset) to evaluate agent capabilities.  
4. **Prioritize High-Value Tasks**: Target tasks with significant economic or practical value to justify agent deployment.  

--- 

This summary highlights the nuanced challenges and opportunities in AI agent development, emphasizing the need for careful design and tooling to realize their potential.

## Full Transcript

[00:00] hello my name is Chip I started an AI
[00:03] infrastructure setup a few years ago and
[00:05] after selling it last year I have been
[00:08] happily unemployed before that I work
[00:10] with Nvidia snug Ai and also taught a
[00:13] couple of courses at
[00:15] Stanford I have uh my uh for today I
[00:17] want to talk about the challenges in
[00:19] building agent or why people think agent
[00:23] is a b word and why I think that is
[00:25] not I had been wanting to come to like
[00:28] the AI engineering Summit for a long
[00:30] time but swix like never invited me
[00:32] until very recently I share the session
[00:35] of Agents from my book engineering it's
[00:38] a very long session it's like 8,000
[00:40] words and people seem to like it so swi
[00:42] invited me here and
[00:44] um I actually like prepare like another
[00:47] talk for uh for for the summit but then
[00:51] after watching a lot of talks yesterday
[00:53] I realize that people have covered a lot
[00:56] of ground so I created a new talk hoping
[00:59] to cover like newer like more exciting
[01:01] topics so this is a new talk created
[01:04] especially for this conference and I
[01:06] hope you like
[01:08] it I heard that if you are to give an
[01:11] agent talk today you obligated to Define
[01:13] what an agent is um I know that a lot of
[01:16] people think uh there a lot of talk
[01:18] about like agans is just hype but I
[01:21] don't think so I think there's a lot of
[01:23] like exciting use cases for Agent B gu
[01:26] I'm like preaching is the choir so agent
[01:29] is not a new term uh when I was working
[01:31] on my book uh I decided to like look at
[01:34] a lot of books from AI books from the '
[01:36] 80s and the '90s and trying to
[01:38] understand like how people defy agent
[01:40] back then and a definition that's like
[01:42] really uh resonate with me uh is from
[01:45] the book by um by Stuart Russell and pet
[01:48] novic so they defined an agent as
[01:51] anything that can perceive the
[01:53] environment and that act on the
[01:55] environment so let's say that you have
[01:57] an agent that play chess that the chess
[01:59] board is its environment and its actions
[02:02] are the chest moves um chbt right chbt
[02:06] can interact with the internet so the
[02:08] internet is its environment and it can
[02:11] do actions like web browsings it can
[02:13] also use calculator it can also like Jed
[02:16] text and images so one of the most
[02:19] popular use cases of Asian nowaday is
[02:21] like coding agents and here is from the
[02:24] paper like sweet um sweet agent paper
[02:27] and as you can see here the environment
[02:29] for three agent is a computer with
[02:32] terminal and file system and the list of
[02:34] actions it can perform include navigate
[02:37] repo search files View files edit
[02:42] light so the environments like
[02:44] determines the kind of actions that the
[02:46] model can perform so if you're in a game
[02:48] if an agent is in the game it can only
[02:50] perform the action that a game allows at
[02:53] the same time giving the model more
[02:56] actions can also have expand its
[02:58] environment so if you give the model the
[03:00] ability to browse the web that now the
[03:02] internet becomes its
[03:04] environment there are many reason why
[03:07] like we would want to give a model
[03:09] access to actions so first actions can
[03:11] help address a model
[03:14] limitations so all the models have the
[03:16] cut off date and that make it like
[03:19] pretty hard to answer questions that
[03:21] require new information by giving some
[03:23] models access to like newer API such as
[03:27] um news or weather web browser the model
[03:30] now can get a relevant reason
[03:32] information to answer questions a very
[03:35] common limitations that people discover
[03:37] very early on with AI is that AI is
[03:40] pretty bad with math so instead of
[03:42] trying to train a model to like be
[03:44] really really good with numbers you can
[03:46] simply like give the model access to a
[03:48] calculator another things a very
[03:50] exciting use case that you can turn a
[03:53] text only or image only models into a
[03:56] multi model model by giving it access uh
[03:58] to tools um or actions so for example um
[04:02] given a language model right a language
[04:04] model can only process text and output
[04:06] text so if you want to model to like
[04:08] also be able to process image you can I
[04:11] can give you access to like say an image
[04:13] cing model so like give an image it can
[04:16] like use this tool to generate captions
[04:18] and then use that caption to generate
[04:20] response now that model can process both
[04:22] text and image it's very cool but so
[04:24] something it's like even more cool so I
[04:26] think is like why agents are so exciting
[04:29] is that like actions allowed you to
[04:31] embed models into the workflow so now
[04:34] for example you can give the model
[04:35] access to the inbox uh just like your
[04:38] calendars or like the code editors so
[04:41] that the models so that you can use a
[04:43] model in day the workflow instead of
[04:45] having to open say like a a web browsers
[04:48] so that you can use
[04:50] AI so when I talking about like agents
[04:54] people will always ask me like okay if
[04:57] agents are so cool so what AR every
[05:00] why isn't everyone using it like tell me
[05:02] like everyone asking me like what what
[05:03] would be like give me one good use cases
[05:06] of like agent so why isn't everyone
[05:09] using it it's because like doing agents
[05:11] is like really really hard so for the
[05:13] rest of the talk I would cover like a
[05:15] few reason why like doing agent is so
[05:17] hard so we to start with the Cur of
[05:22] complexity so we know that like task
[05:24] failure rate increases as the task
[05:27] complexity increases this is true true
[05:29] not not just for AI but also for human
[05:31] as well like if you're given more
[05:33] complex task we would be more likely to
[05:35] fail so let's say that you're building
[05:37] an application for your company and
[05:39] you're okay with a filler rate of like
[05:41] say um one or 2% right and so model
[05:46] makes like makes mistake like 2% of the
[05:49] time for one step so over 10 steps the
[05:52] mistakes the model can make mistake
[05:53] about like 80 18% of the time and that
[05:56] is a lot that might be unacceptable and
[05:58] like if you incre increase your number
[06:00] of steps to like 100 steps some model
[06:02] become like almost like worthless like
[06:05] you can make mistake most of the
[06:07] time for a lot of Asian use cases um a
[06:10] lot of as Asian use cases are pretty
[06:13] complex and might require M multiple
[06:15] steps to Sol uh to Sol them so it's not
[06:19] that you don't want to use agents for
[06:21] like simple task but like simple simple
[06:24] task just don't need don't usually need
[06:27] agent to do and also simple task might
[06:30] have like lower economic value so like
[06:32] they are less exciting for a to
[06:36] S let's let's go through like a very
[06:39] very simple examples like let's say that
[06:41] you want to ask the agent to like how
[06:44] many people bought product from like
[06:46] company X last week so this is a very
[06:48] very simple query but some agent manage
[06:51] to break it out in like in several in
[06:52] several steps like it might first get
[06:55] the product list of the company act and
[06:58] then for each product in this list it
[07:00] would want to get the number of like
[07:01] order from like last week and then given
[07:04] all this number um order CS it would
[07:06] have to Summit up and then given this
[07:08] numbers they have to generate a respond
[07:10] to the users so even with this very very
[07:12] simple query very simple task there like
[07:15] like four steps and the more steps there
[07:17] are like the more complex queries uh the
[07:20] higher number of steps and the more
[07:22] likely the agent is going to
[07:24] fail so in in the uh a vast majority of
[07:28] um agent use cases I'm seeing right now
[07:31] um it's very very rare to see them like
[07:34] consistently being to Sol tasks that
[07:36] involve like more than five steps and I
[07:39] do believe that enabling agent to handle
[07:41] more complexity will unlock many many
[07:44] new use
[07:46] cases um so this is tricky question um
[07:49] how do you know what complexity your
[07:51] agent your agent can solve because you
[07:53] want to give agent um the the task that
[07:57] like as a right level complexity it can
[08:00] Sol so that it doesn't fail and like
[08:02] cause like catastrophic uh business
[08:05] failure so so um different kind of task
[08:08] different use cases have different
[08:10] definitions of complexity a very a very
[08:13] very common way to Define complexity is
[08:15] by the number of steps needed to solve
[08:17] the task so this is by um this is like a
[08:21] synthetic planning Benchmark that I'm
[08:23] working on and I'm hoping to like
[08:25] publish very soon um so I use I use CTIC
[08:28] data set uhic Benchmark because it
[08:31] allows me to like control the level of
[08:33] complexity to study a moral Behavior so
[08:36] now I can ask the motal like Jared like
[08:38] tasks that require like five stat you
[08:41] all so so so with that um um so in in my
[08:45] Benchmark most models per don't perform
[08:48] quite well like most model can only
[08:50] solve um tasks like that have um at most
[08:54] like five that require at most uh five
[08:57] steps and after 10 steps um most models
[09:00] fail and this is like consistent with
[09:03] another studies that I have seen it's an
[09:05] older study now it was um from 2021 so
[09:09] it's in uh it's in coding so the results
[09:11] so the actual Pass rates for the task
[09:15] for models must have increased a lot by
[09:17] by now however the the the learning the
[09:21] inside uh is still like I think still
[09:23] very relevant so in this um in this
[09:26] paper they try to construct like
[09:29] different doctrines and then they ask
[09:32] the model the agent the model Jer code
[09:36] based on the doctrine so they they count
[09:38] the complexity they consider they
[09:40] measure complexity uh of the task based
[09:43] on like how many steps needed in the
[09:45] dark string so for example like for this
[09:48] task like first you want to con you ask
[09:50] a model to con right C to convert the
[09:52] string into lower case and then you ask
[09:54] the model to write code to remove half
[09:57] of the characters in The String so like
[09:59] this are considered like two building
[10:01] blocks or like two steps in the
[10:03] doctoring and they F out the same result
[10:06] like um as as I did is that the success
[10:09] rat the pass rate like decrease rapidly
[10:12] as the number of steps
[10:15] increase um but the good news is that
[10:18] like with newer models um they have
[10:22] actually getting a lot better with
[10:23] planning so here in the same uh result
[10:26] you can see this like here's this three
[10:28] very nice curve
[10:30] they come from a dpck i1 Gemini 2.o
[10:33] flash thinking and A1 preview I didn't
[10:36] test on like A1 and 03 because I didn't
[10:38] have access to this model when I run
[10:40] this test and you can see this like the
[10:42] curves are being pushing upward like the
[10:45] models the newer models are able to Sol
[10:48] like Tas with more complexity and I do
[10:50] believe that this going to increase over
[10:52] time allowing us to like using agent for
[10:54] more practical complex real one
[10:57] task um so here this is another uh reson
[11:00] from my Benchmark so as you can see here
[11:03] it shows the number of task that H model
[11:06] was able to solve and in overall you can
[11:08] see this like there's a pretty big
[11:10] difference between like newer reasoning
[11:13] models such one preview thisa one and
[11:15] gini Flash thinking and non- reasoning
[11:18] model just like uh Sonic 3.5 Gemini 2.0
[11:21] pro or like gbd
[11:26] 4 different use cases might def find uh
[11:30] different um the complexity differently
[11:33] so here is the paper from zebra logic
[11:35] just I just came out like just last
[11:36] month in which uh it's a is a logic task
[11:39] so they defy each problem complexity by
[11:42] its number of like Z3 conflict so you
[11:46] can see this like by the they also got
[11:48] the same reason like the model success
[11:50] rates like decrease rapidly as the
[11:52] number of um as the number of Z3
[11:55] conflicts
[11:57] increase so I think there's several tips
[12:00] to get the agent to handle more
[12:02] complexity first we might want to break
[12:05] task into subtask that agent can Sol so
[12:07] you don't want to give an agent a task
[12:09] more than it can handle so let's say
[12:11] that a task your task like consistently
[12:14] require something like five or six steps
[12:17] to so and so agent can maybe like soon
[12:20] can do at most like three steps then you
[12:22] might want to break the task into like
[12:24] two subtask another way to like have the
[12:27] model deal with more complexity is do
[12:29] like test time compute scaling uh so I I
[12:33] test time Compu uh but I think in the
[12:36] last few years were have been talking a
[12:38] lot about test time compute scaling so
[12:39] it's one of the very one of the new or
[12:41] very exciting Concepts that give rise to
[12:44] like reasoning models and I'm very
[12:45] excited about it so the idea is that
[12:48] that you can have you can give the model
[12:50] more compute during inference so so that
[12:54] um so that it can either J it like uh
[12:57] using more uh more tokens so you can
[13:00] think more or you can also you can you
[13:02] can also use the compute budget to
[13:05] generate more more output so for example
[13:08] given a math problem it can maybe like
[13:12] output 10 different samples 10 different
[13:15] solutions and then pick the one that
[13:17] like the model like most of this I pick
[13:20] the one that's most comeon like most um
[13:22] that's the model things I put most of
[13:24] the
[13:25] time so yeah so it stand like compus
[13:27] scaling you can use stronger models so
[13:31] using stronger models can of so call
[13:33] like uh train train time computer
[13:36] scaling because now you need to invest
[13:38] more compute into like training bigger
[13:41] model okay so we finished the first
[13:44] challenge which is like the curse of
[13:46] complexity the next part we're talking
[13:47] about a challenge video to tun use so
[13:50] tune use is basically like natural
[13:52] language uh to API translations and what
[13:55] does this mean so a lot of time for
[13:57] agent right we have humans using agent
[14:00] and the human gives the agent
[14:02] instruction in natural language so for
[14:05] example an agent a human might give the
[14:06] agent task like hey given this customer
[14:09] email create an order so the agent um
[14:13] will need to translate that into like uh
[14:15] functions that can perform this task so
[14:18] it might first need to go the function
[14:20] to extract the customer ID from the
[14:22] email address and then it might put
[14:24] another function to extract the order ID
[14:26] from the content of the email and then
[14:28] give this customer ID and the order you
[14:31] would need to actually create the order
[14:33] so now you can see that it can trans it
[14:35] need to translate from this natural
[14:37] language to just a set of API calls the
[14:40] challenge with this is that the
[14:42] challenge comes from both sides of the
[14:45] of the translations so for natural
[14:47] language can be extremely ambiguous and
[14:49] at the same time on API site you can
[14:51] have very bad a API and very bad
[14:54] documentations so let's go and choose
[14:56] the first example of like amb ambiguous
[14:58] natural language consider this uh agent
[15:01] with access to very very simple
[15:03] functions like FES top products and FES
[15:05] product info that fesb info can return
[15:08] you like the product price so let's say
[15:11] say the F top product take in like three
[15:14] argument like St date end date and
[15:16] number products right and since users
[15:19] has this query five bestselling products
[15:21] under $10 so now uh the the agent would
[15:25] need know that it need to call the fet
[15:27] top products but what was the start it
[15:29] be what was the number of product be
[15:31] like how many products should it query
[15:33] and what start date what end date should
[15:35] it be like would it be like from like
[15:37] does the user want bestselling products
[15:39] from like yesterday from last week and
[15:42] from last month so this is very
[15:45] ambiguous okay so now we talk about like
[15:47] very very bad API or bad documentations
[15:51] in my cting career I have been like
[15:53] pretty like fortunate or unfortunate you
[15:56] have seen like really really really bad
[15:58] comments
[15:59] um
[16:00] so as an engineer myself uh I know that
[16:04] like people don't usually like writing
[16:06] documentations and if you can't explain
[16:11] the function to the uh to to to the
[16:13] agent it's going to be really really
[16:15] hard for the agent to know how to use
[16:17] this right so I do think this like when
[16:20] you when when you give an agent like
[16:23] access to a tool you will need to
[16:25] provide necessory documentation as a
[16:27] list you need to explain like what the
[16:29] function does what parameters it take in
[16:32] like what is the type of parameter what
[16:33] does the parameter stand for you also
[16:36] need to show like error different error
[16:38] codes for the for the for the functions
[16:40] and also like expected like returned
[16:42] values and the more details the better
[16:46] and that's not all because like with
[16:48] arrow code right you don't just want
[16:49] like okay this model return this Arrow
[16:52] like st99 like it doesn't mean much for
[16:55] the model you might want to like explain
[16:57] to the agent like okay this errow is
[16:59] usually caused by this and if you enter
[17:01] this arrrow if you encounter this arror
[17:03] maybe this is how you should address
[17:05] this and one of the uh one company told
[17:08] me that like one of the very very one of
[17:10] the biggest Improvement they got for
[17:12] their agents is after they explained and
[17:17] add to the documentations like how to
[17:19] interpret uh return values of the
[17:21] functions so let's say that's a function
[17:23] like Returns the value of like one like
[17:25] what does that mean so if you help some
[17:27] model interpret the result the model can
[17:30] the agent can actually be able to
[17:32] perform like cor of functions like a lot
[17:35] better and be able to plan a lot
[17:37] better um another very important thing
[17:40] to think about is that like um it's
[17:43] very T use for agents can be like
[17:46] counterintuitive for us because humans
[17:48] and AI like have fundamentally different
[17:51] ways of like using tools so for example
[17:53] like um humans and a have different like
[17:55] preference so humans might prefer
[17:57] working with like visual thing like with
[17:59] guis whereas like AI might go better
[18:02] with like apis so like if you ask a
[18:04] human to use Salesforce they might go to
[18:06] Salesforce website but if you like
[18:08] asside a task for AI it will like it
[18:10] would perform much better like not
[18:12] having to deal with a lot of visual kill
[18:13] and just like calling straight forward
[18:15] API instead and also like humans and AI
[18:18] operate in different way like humans
[18:21] like at least for me uh I find
[18:23] impossible to perform multiple task at
[18:25] once so I could perform like different
[18:27] step like sequential
[18:29] whereas AI can perform task in like
[18:31] parallel so for example um if you need
[18:34] agent to perform like to browse um if
[18:37] you need to like browse 100 websites um
[18:41] it could be like very very boring for
[18:43] humans like him I did that for my book
[18:46] like I browse like thousand of websites
[18:48] but it was not fun at all however for AI
[18:51] like browsing 100 of website or like a,
[18:53] of websites extremely easy you can just
[18:55] send out like open like a like query
[18:58] like this thousand of websites and get
[19:00] back to summaries and it's pretty
[19:01] straightforward so that is actually a
[19:03] challenge for like training or um
[19:06] creating examples for the model to do to
[19:09] to do planning or t news because given a
[19:13] task what's the human annotator does
[19:16] might not be optimal for AI so that's
[19:19] that's that's the reason why the
[19:20] reinform and learning is so exciting
[19:22] because with supervis fire tooling like
[19:25] uh you
[19:26] teaching AI to like clone human
[19:29] behaviors which might not be optimal for
[19:31] AI whereas with reinforcement learning
[19:34] like you let some the model figure it
[19:36] out like we try and arrow and you can
[19:38] might find way to do it that is optimal
[19:40] for
[19:42] AI so there are several tips like how to
[19:45] make agent better a tune use so the
[19:47] first is that you should create like
[19:49] very very good documentations like with
[19:52] everything not just a function
[19:53] descriptions parameters but like Arrow
[19:56] like return values like we just talk
[19:57] about it should like give agents like
[20:00] very narrow and wealth defied functions
[20:03] so just got up with a friend um working
[20:05] for a very big company I I wouldn't say
[20:08] the name but if you say the search
[20:09] engine you Prett know what it is and he
[20:11] was saying that like for for their use
[20:14] cases uh they give their agents like
[20:16] only three or four very narrow and small
[20:19] wordify tools for their agents like they
[20:22] for their task like the agent just did
[20:24] not work at all with like more than five
[20:26] tools you shouldn't s like uh because of
[20:29] like the ambiguity of natural languages
[20:31] you can help the models understand the
[20:33] task or the use of query better by using
[20:36] technique like query rewriting or using
[20:39] like intent classif classifier to help
[20:41] like classify the user intent you can
[20:44] also like instruct or you should
[20:46] definitely instruct your agent to ask
[20:48] for classifications when it's unsure of
[20:51] what users want so for example like if
[20:53] you ask like five um fight bestelling
[20:57] products until like under $10 you can
[21:00] like mix a random guess like to FES
[21:02] product from yesterday or from last year
[21:04] or I can also like ask user like hey do
[21:06] you want top product bestelling products
[21:09] from yesterday or from last week um you
[21:12] can one pretty exciting or interesting
[21:15] uh Direction I'm seeing is that like a
[21:18] lot of companies are building
[21:19] specialized action models for specific
[21:22] types of queries and apis so when we
[21:25] have like specialized model action
[21:27] models for coding right now we have the
[21:29] model train specially for let's say like
[21:31] vs code or like for coding um so why not
[21:35] have like specialized action models for
[21:37] different environment as well so for
[21:39] example I've seen like a a Salesforce
[21:41] might be interested in like building
[21:43] maybe I shouldn't say like Salesforce
[21:44] like Geral like different companies with
[21:47] very complex like ecosystem might want
[21:50] to train action model for their
[21:53] environment okay true down we got a C of
[21:55] complexity it's a tun you issue with
[21:58] natural language and API translations
[22:00] the last one is context and it's really
[22:03] funny because we have been talking about
[22:04] context for a long time like first for
[22:06] rack and now for agent we just talk
[22:08] about context so models like AI has
[22:12] always requires a lot of informations so
[22:15] before agents like a model has already
[22:17] have to work like system instructions
[22:19] which can be pretty long if you like
[22:21] really want the model really want want
[22:24] the application to perform well and
[22:26] secure so you might want to instruct the
[22:29] the model to like what kind of queries
[22:31] you should respond to what kind of query
[22:32] you should not respond to what kind of T
[22:34] you should carry and they also like use
[22:36] the instructions and examples but with
[22:39] agents like you see a lot more um
[22:41] informations so first you might need to
[22:44] pass documentations about the tools CH
[22:46] the agent and the more tools they are
[22:49] the more documentation will be needed um
[22:52] of course like after you call a tool
[22:54] they can be T output that's the model we
[22:56] need to keep track of as well and this
[22:58] wind growth with more like execution
[23:01] steps and um after getting back like a t
[23:04] outputs right the more minity reasons
[23:05] like okay now I got this reason what do
[23:07] I do next or like after a model gener a
[23:10] plan so the agent might also want to
[23:12] reason like hey is this plan like
[23:15] reasonable should I execute it and all
[23:17] these reasoning tokens like take a lot
[23:18] of time take a lot of like um take a lot
[23:21] of input tokens and this also grows in
[23:24] more complex task so like the
[23:26] information that an agent can work with
[23:28] I can grow very very quickly um and I
[23:31] haven't even mentioned like other kind
[23:33] of like information such as such as like
[23:35] table schema for task like Tex to SQL
[23:38] let's say that you want to do like a Tex
[23:40] to SQL task right and you not just you
[23:42] you don't have you have not just one
[23:44] table but like a thousand of tables so
[23:47] when when you translate a SQL query you
[23:49] might need to figure out like what table
[23:51] to apply the SQL query to and for the
[23:54] model to be able to pick the right table
[23:57] you might need to pass in like on the
[23:58] table schemas and if you have like a
[24:00] thousand like table schemas that going
[24:02] to be a lot of information for the
[24:04] modelship
[24:06] process so so one things that like I
[24:08] have experienced like when I was working
[24:10] with agents I would love to have more
[24:12] research on is like um how to make a
[24:15] model that works well with both planning
[24:18] and long context because in my
[24:20] experience like the models that are good
[24:22] with planning are not necessarily the
[24:24] models that work with long contacts and
[24:26] the reason is that like planning are
[24:28] like reasoning usually like um require a
[24:30] lot of reasonings like it require a lot
[24:32] of generate a lot of thinking of
[24:33] reasoning tokens so this kind of task
[24:37] are like output heavy whereas for long
[24:39] contact it's like input heavy and I have
[24:42] in my Benchmark uh my personal Benchmark
[24:44] I seen this like um models that perform
[24:47] well on my long context benchmarks don't
[24:49] perform as well on the planning
[24:50] Benchmark in Vice
[24:52] Vera um so okay so we talk about like an
[24:55] agents like how to deal with a lot of
[24:57] informations and information might not
[24:59] fit inside a model like affection
[25:01] context so I want to highlight the word
[25:04] like affections here because a model
[25:06] might have very long context but then it
[25:08] might not use that context like
[25:10] affectionally so like a model might be
[25:13] able to fit in like a million tokens but
[25:15] like if you give it anything more than
[25:17] like 30,000 tokens it might get really
[25:19] really really funky and like hallucinate
[25:22] on the to so at least in my in my
[25:24] personal experience um I have like uh
[25:27] yeah so so I have like done a a lot of
[25:29] uh a lot of like um benchmarks
[25:31] evaluations just to see like at what
[25:34] point of the of my documentation does a
[25:37] Mor static hallucinate and making of
[25:40] things um so so like if you can't fit on
[25:43] your information into the model context
[25:46] like affection context you might need to
[25:48] realize on like other form of like
[25:50] information persistence or information
[25:53] uh storage so context you can think of
[25:55] it as like a shortterm memory like you
[25:57] should use this for um it should it
[25:59] should be used to store information
[26:01] relevant to the task at hand and then
[26:03] you can also supplement it with like
[26:05] long-term memory for example like
[26:07] external databases or storage um and
[26:10] it's very common with use case like rack
[26:12] right like so if you connect a model to
[26:14] your external databases then you're
[26:17] connecting it to like um long-term
[26:19] memory so um you can like it in C of
[26:22] agent right um You can't like store less
[26:26] immediate relevant information in like
[26:29] exteral external file so let's say that
[26:32] your task requires like 10 steps so
[26:35] maybe and and the output from this only
[26:37] 10 steps like doesn't don't quite fit
[26:40] into the context so you might want to
[26:42] store the output of the first few steps
[26:45] into externaly and only retrieve the
[26:48] output like when necessary and of course
[26:51] like there so like so shortterm memory
[26:53] uh long-term memory and another level of
[26:56] like memory system is inter internal
[26:59] knowledge which is like the knowledge
[27:00] that the model already has so if you
[27:03] have some information that models like
[27:05] that is essential for like the model to
[27:07] perform like multiple tasks you might
[27:09] want to include that in the Ching data
[27:11] and F tun the model on it so that so
[27:14] that's a model can just use this as part
[27:15] of internal knowledge instead of like
[27:17] having to waste like contact
[27:19] tokens okay so that is pretty much for
[27:22] today uh so I think we talk about like
[27:24] um what is a what is an agent different
[27:28] challenges to building agent including
[27:30] um like first
[27:32] including um trying to like get the
[27:35] model to handle the right the task of
[27:37] right complexity and we talk about tips
[27:40] like how to make the model handle more
[27:41] complexity we talk about two new
[27:43] challenges like how to translate between
[27:45] natural language and API and we talk
[27:47] about like how to how get model to like
[27:50] handle longer context with like a memory
[27:52] system so thank you so much everyone um
[27:56] I do have a website and if you have any
[27:58] questions or if you want to talk about
[28:00] the agian planning Benchmark I'm working
[28:01] on feel free to reach out bye
