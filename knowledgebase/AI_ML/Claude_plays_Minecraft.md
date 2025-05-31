---
type: youtube
title: Claude plays Minecraft!
author: Channel Video
video_id: 1B9i7FBsRVQ
video_url: https://www.youtube.com/watch?v=1B9i7FBsRVQ
thumbnail_url: https://img.youtube.com/vi/1B9i7FBsRVQ/mqdefault.jpg
date_added: 2025-05-26
category: AI Agent Development and Cloud Integration
tags: ['Amazon Bedrock', 'Minecraft AI', 'RAG (Retrieval-Augmented Generation)', 'Cloud AI Services', 'Containerization', 'AI Agent Orchestration', 'AWS Integration', 'Machine Learning Workflows', 'Server-Client Architecture', 'Prompt Engineering', 'Managed AI Platforms', 'AI Development Tools']
entities: ['Amazon Bedrock', 'Minecraft', 'MineFlare', 'LangChain', 'Claude Haiku', 'Amazon ECS', 'Amazon Lambda', 'SageMaker', 'RAG (Retrieval-Augmented Generation)', 'Agents for Amazon Bedrock']
concepts: ['agentic workflows', 'model hosting', 'agent orchestration', 'Retrieval-Augmented Generation (RAG)', 'state management', 'containerization', 'server-client architecture', 'prompt engineering', 'traceability in AI', 'managed AI services']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AWS services', 'Familiarity with containerization (Docker)', 'Knowledge of Python programming', 'Experience with AI/ML frameworks', 'Understanding of Minecraft bot development']
related_topics: ['AI agent development', 'Cloud computing architectures', 'Retrieval-Augmented Generation (RAG)', 'Containerized application deployment', 'Machine learning model integration', 'Server-client system design', 'Prompt engineering techniques', 'Managed AI service platforms']
authority_signals: ['I am an engineer but not really with Python', 'We started off with LangChain on Lambda to build this like most people when they do start building agents', 'Amazon Bedrock is all about facading one or more models']
confidence_score: 0.8
---

# Claude plays Minecraft!

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=1B9i7FBsRVQ)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: minecraft, ai-agent, llm, open-source, game-automation, agent-workflow, machine-learning  

## Summary

# Summary of "Claude plays Minecraft!" Video Transcript

## Overview  
The video discusses the development of an AI agent named **Rocky** to interact with the game *Minecraft* using a **managed agentic workflow**. The speaker explains the technical architecture, challenges in integrating AI models (like Claude Haiku via Amazon Bedrock), and the demonstration of Rocky's behaviors, such as digging, moving, and interacting with the game environment.

---

## Key Points  
1. **Agent Workflow in Minecraft**  
   - Rocky is an AI agent designed to perform actions in *Minecraft* (e.g., digging, jumping, navigating).  
   - The agent uses **Amazon Bedrock** to orchestrate tasks, leveraging models like **Claude Haiku** for its speed and efficiency.  

2. **Technical Architecture**  
   - **Initial Setup**: The project started with containers for Minecraft and MineFlare (a bot framework), later migrating to **Amazon ECS** and **Bedrock** for scalability.  
   - **Challenges**:  
     - AWS Lambda couldn’t handle state management required by MineFlare.  
     - Complexity increased with more actions/tools for Rocky, necessitating a managed solution.  
   - **Amazon Bedrock**: Facades multiple LLMs (e.g., Claude, Cohere, Llama) and supports features like **RAG (Retrieval-Augmented Generation)**, **guardrails**, and **traceability** for agent workflows.  

3. **Rocky’s Capabilities**  
   - Demonstrated actions: digging holes, navigating environments, and unexpectedly digging out of holes.  
   - **Unintended Behavior**: The agent’s autonomy led to unexpected but functional outcomes (e.g., digging out of a hole).  

4. **Tools and Services**  
   - **LangChain** and **SageMaker** were initially used but became complex as the project scaled.  
   - **Bedrock** simplified the workflow by managing LLMs, agents, and knowledge bases in a unified platform.  

5. **Key Takeaways**  
   - **Managed Agentic Workflows**: Amazon Bedrock streamlines AI integration, reducing complexity.  
   - **LLM Selection**: Claude Haiku was chosen for its speed, critical for real-time interactions in *Minecraft*.  

---

## Notable Quotes  
- *"The state is stored in MineFlare, but we couldn’t run it on Lambda because of state management."*  
- *"Rocky digging out of a hole just works—it’s fascinating."*  
- *"Amazon Bedrock is a managed agentic workflow, handling RAG, agents, and guardrails in one spot."*  

---

## Actionable Insights  
1. **Leverage Amazon Bedrock** for managed agentic workflows, especially for real-time AI interactions.  
2. **Use Claude Haiku** for speed-critical applications (e.g., game AI).  
3. **Migrate to ECS** for stateful services like Minecraft servers.  
4. **Explore RAG and Guardrails** in Bedrock to enhance AI safety and context-awareness.  

--- 

## Conclusion  
The video highlights the intersection of AI agents and gaming environments, showcasing how tools like Amazon Bedrock enable scalable, managed workflows. Rocky’s demo underscores the potential of autonomous AI in dynamic, unstructured tasks like *Minecraft*.

## Full Transcript

[00:00] [Music]
[00:13] today I'm going to um show you how I
[00:17] built an agent to play Minecraft right
[00:20] so this talk in a nutshell if I could um
[00:24] sum it up is all about a gentic workflow
[00:27] so I'm sure some of you here have have
[00:30] build agents you're in this track maybe
[00:32] some of you have not um so I'm going to
[00:34] start with a bit of a bit of a level set
[00:37] on agent workflow an agentic workflow
[00:40] and then I'll show you how that maps to
[00:43] the agent uh we built with with
[00:47] Minecraft so this flow diagram is
[00:49] probably familiar to some of you where
[00:52] an agent will take inputs uh like chat
[00:55] or some in in unstructured data uh it'll
[00:59] consume that and then it will use a set
[01:02] of tools one or many tools to satisfy
[01:05] the requests uh from the chat so it can
[01:08] fulfill its Destiny and its um its
[01:11] actions and also it uses an llm and it
[01:15] may then orchestrate one or many times
[01:17] through the llm the tools and then
[01:20] return uh
[01:22] response pretty well understood n but
[01:25] very
[01:26] cool so if we take that into a Minecraft
[01:30] world where does the chat come from well
[01:33] if anybody anybody here played
[01:35] Minecraft a few people a few people
[01:38] great so if you've played Minecraft
[01:40] you'll know there's a chat function
[01:42] where you can interact uh with the world
[01:45] and other people in the world and so
[01:47] that's where the chat comes for this
[01:50] agent the tools in Minecraft are many
[01:55] and that's why we built this in
[01:57] Minecraft you can do many things you can
[01:59] build you can dig you can Farm you can
[02:04] slay a pig if you so
[02:06] desire um but you can do a few
[02:10] things and so the agent itself becomes
[02:14] the bot so we tell it via chat what we
[02:18] want it to do it uses the tools and
[02:21] hopefully fulfills our requests now
[02:24] remembering that our requests are
[02:26] probably indeterminant and the output is
[02:29] also determinant so today I'm going to
[02:32] live demo uh what you should never do so
[02:34] they say you should never live demo with
[02:37] kids animals and an llm so I'm going to
[02:40] do that
[02:41] today the llm itself of course is
[02:45] Magic it is it's
[02:47] magic and then the responses the agent
[02:50] will um do Wonder many um thoughts and
[02:55] then return the response to Minecraft so
[02:57] that's that's the flow in a nutshell
[03:01] and of course we have our friendly bot
[03:04] and so our bot's name is is Rocky uh and
[03:07] short for uh bedrock and um we'll see
[03:10] what Rocky if Rocky behaves
[03:13] today and the tools we're going to use
[03:16] with Rocky and the actions that those
[03:18] tools will will um uh jump on is Jump
[03:22] move to position locate a player and a
[03:24] few more more actions that we've
[03:27] built and at this stage I'll also
[03:29] mention that this demo that I'm going to
[03:32] show is open source uh and you can all
[03:35] have a play with it at the end all you
[03:36] need is a Minecraft
[03:40] client so this is Rocky and I'm going to
[03:42] give you a quick recording that I did
[03:44] yesterday at the booth we're at the AWS
[03:45] Booth if you want to come and chat to me
[03:48] I am am not scary uh I am from Australia
[03:51] but I'm not scary um so Rocky does a
[03:54] number of things so this is what Rocky
[03:56] will look like at the minute it's Runing
[03:58] in Rocky land Rocky is a very friendly
[04:00] bot and so you can ask Rocky questions
[04:03] in the chat I hope you can all see that
[04:05] so what's the weather so uh Rocky being
[04:09] friendly will know my name uh and then
[04:12] also tell you what the weather weather's
[04:13] like so it's R in your area you might to
[04:15] want to take some
[04:17] shelter Rocky can also do some actions
[04:20] so this is how we send the actions to
[04:21] the agent via chat so Rocky jumps for
[04:25] us also Rocky can do other things so I'm
[04:29] going to hide behind this Rocky
[04:30] constructed building and I'm going to
[04:33] ask Rocky can he come and find me or can
[04:36] they come and find me actually Rocky is
[04:38] neither male nor
[04:39] female um Rocky says on my way and there
[04:43] there comes
[04:44] Rocky and Rocky's find us but what else
[04:48] can Rocky do so what else did I do here
[04:52] oh he can find things in the world so
[04:55] Rocky here I've asked it to find a pig
[04:57] so Rocky knows based on um the plug-in
[05:02] that we're using for Minecraft where
[05:03] everything is and it says yep I found a
[05:06] pig this is the location and I then ask
[05:08] it go find go go to that pig so off
[05:11] Rocky runs to the pig and uh finds the
[05:14] pig so we've made we've demonstrated
[05:18] this at a lot of conferences and the
[05:20] biggest thing we've seen is people try
[05:21] to hit the pig so I asked to hit the pig
[05:25] and uh there it goes Rocky hits the pig
[05:28] uh you can do that multiple times and
[05:30] lots of people have observed do don't
[05:31] know why but hey human behavior is even
[05:34] more fascinating than
[05:36] LMS um so now um going to get Rocky to
[05:39] come here and I'll probably finish with
[05:41] the Dig action
[05:44] so I'll ask Rocky to dig a hole notice
[05:48] um when I say dig a hole there's a
[05:50] parameter that I that I add so I think
[05:53] in this instance I yeah a 2X two hole so
[05:56] this is a parameter that I'm sending to
[05:58] to the action I'll show you how all that
[05:59] works when I do a bit of a deep dive
[06:01] into the into the um the back end so
[06:04] Rocky um digging a hole and also Rocky
[06:09] can come find us out of that hole and
[06:11] dig their way out of the hole uh this is
[06:14] behavior that we didn't expect and it
[06:16] just just works which is um really
[06:20] fascinating so that's that's a bit of a
[06:22] three minute uh demo of Rocky I'm going
[06:24] to live demo Rocky once I go through how
[06:26] I built it so the architecture so we
[06:29] built this for a serverless conference
[06:32] so our um constraint wear needs to run
[06:36] in a manage environment a service
[06:39] environment uh and be cool so we started
[06:42] off with running it in a container so
[06:44] Minecraft you can run in a container and
[06:47] you can also run mine flare which is the
[06:50] bot framework that works with Minecraft
[06:52] and those two run side by side nicely on
[06:55] the container we can't run mine flare on
[06:58] Lambda which is serous because we need
[07:00] state right so the state is stored in
[07:03] mine
[07:04] flare we started off with Lang chain on
[07:07] on Lambda to build this like most people
[07:09] when they do start building agents they
[07:11] probably start with langin uh I'm not a
[07:13] big python developer uh I am an engineer
[07:16] but not really with python um but we we
[07:19] got a working to a state but then as we
[07:21] had a complexity and more and more
[07:23] actions and tools for Rocky to use uh it
[07:26] got really really um complex and then we
[07:29] also used Amazon sagemaker to host the
[07:31] llm which in this in this case uh we
[07:34] were using the coher
[07:36] llms and
[07:38] then we decided okay so that's not
[07:41] service enough uh let's use uh agents
[07:44] for Amazon Bedrock keep the Minecraft
[07:47] server and client which is um mine flare
[07:49] on Amazon ECS and build that agent up on
[07:53] Amazon
[07:56] bedrock and then for architecture so
[07:59] what we're doing and what I'm
[08:00] demonstrating today um it is it's
[08:03] running on my local machine so both
[08:05] Minecraft and the mind FL a client and
[08:08] then it's into calling out to agents for
[08:11] Amazon bedrock and may the internet
[08:13] always be favorable over the next couple
[08:15] of
[08:17] minutes so if you haven't come across
[08:19] agents for Amazon Bedrock let me do a
[08:21] quick uh overview again ad Booth is
[08:24] there come and talk to me I'll go a deep
[08:25] dive for you but in a nutshell uh Amazon
[08:28] bedrock is all about
[08:30] facading uh one or more models so what
[08:34] it does is it produces a common API that
[08:36] then you can use uh as an engineer to
[08:39] build out your application and add add
[08:41] features so we host as well as Amazon
[08:44] models we host anthropic models we host
[08:47] cahir models as I mentioned Lama models
[08:50] um and a whole host of other models so
[08:53] when building out Rocky n using agents
[08:56] for Amazon Bedrock you'll see that I
[08:58] used the Claude uh models and I'll go
[09:01] through that as well why I did that
[09:04] Claud in in particular Claude Haiku
[09:06] because it's it's
[09:08] fast and so as well as hosting models
[09:10] not hosting models but providing a
[09:12] facade into models um everything you can
[09:16] also build uh additions to that and one
[09:19] of those additions is Agents as well as
[09:21] knowledge bases where you can uh do rag
[09:24] and also guard rails and EV valves so
[09:26] all of these things are riged into
[09:28] Amazon uh bed Rock and it's think of it
[09:31] more as a sort of a a managed agentic
[09:34] workflow right so you can manage um Rag
[09:38] and you manage agents as well so it's
[09:40] all in one spot so it also helps you
[09:43] with prompt creation it obviously as
[09:45] it's an agent orchestrates multiple
[09:47] tasks and also allows you to trace
[09:49] through the Chain of Thought of the
[09:51] agent so you can either do that in the
[09:53] console or it will spit it out to
[09:55] logs and of course it also and what was
[09:58] very key for this demo it has Return Of
[10:01] Control okay so that's the slides Let's
[10:04] uh let's jump into what we've
[10:08] got so let me see if I can just instead
[10:12] of doing
[10:14] that
[10:19] uh mirror no not
[10:26] that oh dear
[10:30] stop
[10:35] mirroring okay there always
[10:39] so me in
[10:43] display extend display me and this play
[10:46] I want a mirror and it's not it's not
[10:47] letting
[10:53] me
[10:55] apologies got this got this i got this
[10:58] this refresh right
[11:05] here and
[11:08] Mirror
[11:10] Mirror there we go yay okay
[11:15] so okay so this is that's mine flare so
[11:19] it's all open source let's first of all
[11:20] start with the good stuff so open source
[11:22] uh mine flare you can use and then this
[11:25] is uh the um what we've built n I'll
[11:29] share this at the end QR code everything
[11:31] don't worry about it so this is Amazon
[11:34] Bedrock so this is agents and this is
[11:36] the um the console page so what it'll do
[11:40] um you can go down here uh into agents
[11:43] if you haven't seen Bedrock before it'll
[11:45] show you the model access and what
[11:47] models you've got access to but I'm
[11:48] really talking about agents which is
[11:50] down here on the left so here I've got a
[11:52] Minecraft Agent apology if you can't see
[11:54] this too well let see if I can make it a
[11:56] little bit better um you've got
[11:58] Minecraft the mcraft agent so I've
[12:00] defined this in here now for all the
[12:02] real engineers in the room you don't
[12:04] have to build it via click Ops so you
[12:06] can build it all as infrastructures code
[12:08] and if you check out the GitHub repo you
[12:09] will see it all in Cloud information and
[12:11] cdk um so once I've got into the agent
[12:14] you can see that here I can select my
[12:16] model so at the minute this agent is
[12:19] using Cloud CLA 3 hiu and here is the
[12:22] prompt so this is the system prompt for
[12:23] that agent you're a playful friendly and
[12:25] creative Minecraft Agent called Rocky uh
[12:28] and your goal is the entertain players
[12:30] and collaborate with them in a fun
[12:31] gaming experience and it goes on so this
[12:34] prompt we uh built over over time
[12:35] there's a bit of prompt engineering
[12:37] going on in this demo um and then if I
[12:40] go into the actions you can see all of
[12:42] the actions so you notice all of the
[12:45] actions have defined all have return
[12:47] control because we we want them to
[12:49] return uh the the their output so we've
[12:52] got
[12:53] jump uh we' got other actions dig dig
[12:57] you'll see this is where the parameters
[12:58] come in so I've got a depth and a width
[13:01] so you remember when I specified a hole
[13:03] I said 2 by two also if I say small hole
[13:06] it will go it's a one by one hole so
[13:08] we'll infer that uh using the
[13:10] model uh also there's the action is at
[13:13] reing so all of these actions are
[13:15] defined in
[13:16] here and also I've got another action
[13:19] set that I'm going to share with you and
[13:21] going to demo is
[13:26] called it's called Minecraft experiment
[13:29] Al right and what this does this has one
[13:32] action called build which is a very
[13:35] complex thing to do in Minecraft uh
[13:37] believe it or not because it's a 3D
[13:39] space and so the action for build all I
[13:43] do is build a structure and um that
[13:45] returns back to the client um and I'll
[13:48] show you how that prompts actually
[13:49] created um when I do the build so that's
[13:52] that's how it's built and the
[13:54] actual source code itself is here and
[13:58] the Cent is stopped so I'm going
[14:00] to so this is Rocky itself so I'm going
[14:03] to start
[14:05] Rocky going to start
[14:09] and B bot has spawned going to go over
[14:12] to Minecraft we've got running here back
[14:15] to game Rocky has joined the game
[14:17] there's Rocky let me just go
[14:20] set
[14:21] time time it's time set time set uh noon
[14:25] so you can see it better
[14:29] okay okay so there's Rocky so you can
[14:31] let's just test the rocky working so T
[14:35] please come
[14:40] here uh Rocky will make the first
[14:42] request and there we go so rocky rocky
[14:45] is working for us um so let's make sure
[14:48] that Rocky can do something so we go
[14:51] Rocky please please dig a small
[14:57] small B
[15:00] okay so it'll Rocky will dig a small
[15:02] hole so now I am going to use the
[15:04] experimental feature which is build what
[15:07] do you want Rocky to
[15:10] build what a Col the
[15:13] Coliseum okay I could even spell that um
[15:18] some something that I can spell
[15:23] please double de couch a double decker
[15:26] couch okay I like that um
[15:29] please come here so yesterday I I built
[15:31] um a rocket ship which was quite
[15:33] interesting but a double decker couch so
[15:37] let's let's um get Rocky the hole so
[15:39] let's give it some space okay
[15:44] Rocky
[15:46] please build can I just say
[15:49] coach double that's
[15:52] TR never do live double decker cach
[15:55] please build double decker cach a one
[15:58] just one
[16:00] I'm just going to just going to make it
[16:02] so what happens Rocky then that prompt
[16:04] goes off and so if I look at the code
[16:08] which I've
[16:09] lost yeah so there's the prompt so what
[16:12] we've done we've said to Rocky you're
[16:15] claw an expert Minecraft builder
[16:17] creating by anthropic when given a
[16:20] structure description which will be the
[16:21] input uh then output valid Json so this
[16:24] Json is how M flare builds objects so
[16:27] you give that as part of the pro PP so
[16:29] that the model will understand how to
[16:31] build Minecraft
[16:32] objects uh then you'll go strictly adere
[16:35] to the following rules because if you we
[16:36] didn't do that it goes bananas uh and
[16:39] builds just nonsense uh and so all
[16:42] blocks are placed to each other these
[16:43] are the blocks you can use and then
[16:45] responds with the what it thinks a c
[16:47] looks like so this is the XY coordinates
[16:50] and so it started to build so let's see
[16:52] what Rocky's
[16:54] doing and there Rocky has built a double
[16:59] decker coach thank you very
[17:02] much
[17:05] um I'm going to sit on the couch um so
[17:09] this obviously is the interpretation of
[17:11] what a double- deer couch looks like uh
[17:13] to Claude And in the 3D space and then
[17:16] it's been interpreted into XY
[17:18] coordinates and Rocky has built it so
[17:21] that that is that is Rocky obviously we
[17:23] are here uh at the AWS Booth all day
[17:26] could you please I also put a q code I
[17:29] promised before let's fly to
[17:34] that so scan the QR code and please fill
[17:37] in the session um feedback form also if
[17:41] you fill it in I'll give you ads credit
[17:43] codes for everybody who fills it in and
[17:45] a link to the GitHub website so please
[17:48] do that and uh hopefully you enjoyed the
[17:50] session hope hanging out with Rocky and
[17:53] come ask me any questions at the booth
[17:55] when you can thank you very much thank
[17:56] you
[18:00] [Music]
[18:14] e
