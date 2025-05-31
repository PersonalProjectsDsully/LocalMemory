---
type: youtube
title: Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic
author: Channel Video
video_id: kQmXtrmQ5Zg
video_url: https://www.youtube.com/watch?v=kQmXtrmQ5Zg
thumbnail_url: https://img.youtube.com/vi/kQmXtrmQ5Zg/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['mCP', 'AI integration', 'vector databases', 'RAG systems', 'microservices', 'context-aware AI', 'API development', 'IDE tools', 'AI applications', 'technical framework']
entities: ['mCP', 'GitHub', 'vector DB', 'RAG system', 'IDEs', 'Curser', 'Windsurf', 'Anthropic', 'microservices']
concepts: ['mCP framework', 'AI applications', 'external system integration', 'microservices architecture', 'vector databases', 'RAG (Retrieval-Augmented Generation)', 'prompting', 'chunking logic', 'context-rich AI']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with APIs and microservices', 'Experience with vector databases or RAG systems']
related_topics: ['AI integration', 'API development', 'microservices architecture', 'RAG systems', 'context-aware AI', 'vector databases', 'IDE tools', 'AI application development']
authority_signals: ['this this slide covers a few different personas', 'we saw a lot of the N times M problem where there are a ton of different permutations', 'mCP aims to flatten that and be the layer in between']
confidence_score: 0.8
---

# Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: ai agents, model context protocol, api integration, machine learning, software development  

## Summary

# Summary of "Building Agents with Model Context Protocol" Workshop

## Overview  
Mahesh Murag of Anthropic discusses the **Model Context Protocol (mCP)**, a framework designed to enable AI agents to interact seamlessly with external systems, tools, and data. The workshop explores mCP's philosophy, its role in addressing fragmentation in AI development, and its growing adoption across applications, enterprises, and the broader ecosystem. Key themes include improving context-rich AI interactions, streamlining integration between developers and tool providers, and fostering collaboration through standardized protocols.

---

## Key Points  

### **1. Motivation for mCP**  
- **Context is critical**: "Models are only as good as the context we provide to them."  
- **Problem before mCP**: Fragmentation in AI development, where teams built custom, incompatible solutions for accessing data (e.g., vector databases, APIs).  
- **Goal of mCP**: Flatten the "N times M problem" (complex permutations of client-server interactions) by acting as a standardized layer between application developers and tool/API providers.  

### **2. mCP's Architecture**  
- **Three core interfaces**:  
  - **Prompts**: Contextual input for AI agents.  
  - **Tools**: External systems (e.g., GitHub, documentation sites).  
  - **Resources**: Data sources (e.g., local files, vector databases).  
- **Flexibility**: Supports both cloud-based and local systems (e.g., Git, version control).  

### **3. Benefits for Ecosystems**  
- **For Developers**:  
  - Once an app is mCP-compatible, it can connect to any server with zero additional work.  
  - Tool providers can build a single mCP server, enabling widespread adoption across AI apps.  
- **For Enterprises**:  
  - Centralized access to shared resources (e.g., vector databases) reduces redundancy.  
  - Teams can specialize in owning and maintaining specific services (microservices-like model).  
- **For End Users**:  
  - AI applications become more context-aware and capable of real-world actions (e.g., demos with Curser and Windsurf).  

### **4. Adoption & Growth**  
- **Community-driven**: Over 1,100 open-source mCP servers built by developers.  
- **IDE Integration**: Excitement around using mCP in code editors to provide real-time context (e.g., GitHub, documentation).  
- **Enterprise Use Cases**: Streamlined workflows for teams managing infrastructure, data, and AI applications.  

### **5. Roadmap & Future Vision**  
- Expand mCP's capabilities to support more complex interactions (e.g., multi-agent systems).  
- Foster a collaborative ecosystem by documenting APIs, encouraging open-source contributions, and enabling cross-team collaboration.  

---

## Key Quotes & Insights  
- "mCP aims to be the layer in between application developers and tool/API developers."  
- "Before mCP, every team built their own way to access the same vector database."  
- "It’s like microservices for AI—different teams own specific services, and the entire company moves faster."  

---

## Conclusion  
mCP represents a significant step toward unifying AI development by standardizing how agents interact with external systems. By reducing fragmentation and enabling scalable, centralized access to data and tools, it empowers developers, enterprises, and end-users to build more powerful, context-aware AI applications. The growing community adoption and enterprise focus suggest a promising future for mCP as a foundational protocol in the AI ecosystem.

## Full Transcript

[00:00] [Music]
[00:14] hey everyone hello thank you all for
[00:17] coming uh my name is mahes and I'm on
[00:20] the applied AI team at anthropic um
[00:23] really excited to see a very full room
[00:26] and very excited that you chose me over
[00:28] open AI
[00:30] thank you very
[00:34] much so today we're going to be talking
[00:36] about mCP model context protocol um this
[00:40] is more of a talk than a workshop but
[00:43] I'll do my best to keep it interactive
[00:44] if you want to ask questions uh feel
[00:46] free to do so and I'll do my best to
[00:48] answer them um today we're going to talk
[00:51] about the philosophy behind mCP and why
[00:54] we at anthropic thought that it was an
[00:56] important thing to launch and build uh
[00:58] we're going to talk about some of the
[01:00] traction about uh of mCP in the last
[01:02] couple of months um and then some of the
[01:05] patterns that allow mCP to be adopted
[01:07] for AI applications for agents um and
[01:11] then the road map and where we're going
[01:12] from
[01:14] here cool so our motivation behind mCP
[01:18] was the core concept that models are
[01:20] only as good as the context we provide
[01:23] to them um this is a pretty obvious
[01:26] thing to us now but I think a year ago
[01:27] when most AI uh assistant or
[01:30] applications or chatbots uh you would
[01:33] bring in the context to these chatbots
[01:35] by copy pasting or by typing um or uh
[01:38] kind of pasting context from other
[01:40] systems that you're using but over the
[01:42] past few months and the past year we've
[01:43] seen these evolve into uh systems where
[01:46] that the model actually has hooks into
[01:49] your data and your context which makes
[01:50] it more powerful and more
[01:53] personalized and so we saw the
[01:55] opportunity to launch mCP which is a an
[02:00] open protocol that enables seamless
[02:02] seamless integration between AI apps and
[02:04] agents and your tools and data sources
[02:08] the way to think about mCP uh is by
[02:10] first thinking about the protocols and
[02:12] systems that preceded it apis became a
[02:16] thing um a while ago to standardize how
[02:19] web apps interact between the front end
[02:22] and the back end it's a a kind of
[02:25] protocol or layer in between them that
[02:27] allows them to translate requests uh
[02:29] from the back end to the front end and
[02:31] vice versa and this allows the front end
[02:34] to get access to things like servers and
[02:36] databases and
[02:37] services LSP came later and that
[02:40] standardizes how idees interact with
[02:43] language specific tools uh LSP is a big
[02:46] part of our inspiration um and it's
[02:48] called language server protocol and
[02:50] allows an IDE that's LSP compatible to
[02:53] go and uh talk to and figure out the
[02:55] right ways to interact with different
[02:57] features of coding languages you could
[02:59] build a go LSP server once and any IDE
[03:03] that is LSP compatible can hook into all
[03:05] the things about go when you're you're
[03:07] coding in go so that's where mCP was
[03:10] born mCP standardizes how AI
[03:12] applications interact with external
[03:14] systems and it does so in three primary
[03:17] ways um and three interfaces that are
[03:20] part of the protocol which are prompts
[03:22] tools and
[03:26] resources so here was the The Land
[03:29] Before the of a land before mCP that
[03:31] anthropic was seeing um we spend a lot
[03:33] of time with customers and people trying
[03:36] to use our API to build these agents and
[03:38] AI applications and what we were seeing
[03:41] is across the industry but also even
[03:44] inside of the companies that we were
[03:45] speaking to there was a ton of
[03:47] fragmentation about how to build AI
[03:49] systems in the right way one team would
[03:53] uh kind of create this AI app that hooks
[03:55] into their context with this custom
[03:57] implementation that has its own cust
[04:00] prompt logic with different ways of
[04:02] bringing in tools and data and then
[04:03] different ways of federating access to
[04:05] those tools and data to the agents and
[04:08] if different teams inside of a company
[04:09] are doing this you can imagine that the
[04:11] entire industry is probably doing this
[04:14] as
[04:15] well the world with mCP is a world of
[04:18] standardized AI development you can see
[04:22] in the left box um which is the the
[04:24] world of an mCP client and there's some
[04:26] client examples here like our own
[04:28] first-party application ations um
[04:31] recently applications like perser and
[04:33] windsurf uh agents like Goose which was
[04:36] launched by block all of those are mCP
[04:39] clients and there's now a standard
[04:41] interface for any of those client
[04:42] applications to connect to any mCP
[04:46] server with zero additional
[04:48] work an mCP server on the right side uh
[04:52] is any uh it's a wrapper or a a way of
[04:55] federating access to various systems and
[04:57] tools that are relevant uh to to the AI
[05:00] application so it could be a database to
[05:03] query and fetch data and to give the LM
[05:06] access to databases and Records could be
[05:09] a CRM like Salesforce where you want to
[05:11] read and write to something that is
[05:13] hosted on a remote server uh but you
[05:16] want the LM to have access to it it
[05:18] could even be things on your local
[05:20] laptop or your your local system uh like
[05:22] Version Control and git where you want
[05:24] the LM to be able to connect to the apis
[05:27] that run on your computer itself
[05:32] so we can talk about the the value that
[05:33] we've seen for different parts of the
[05:35] ecosystem over the the past few months
[05:39] the value for application developers is
[05:42] once your client is mCP compatible you
[05:44] can connect it to any server with zero
[05:47] additional work if you're a tool or API
[05:51] provider or someone that wants to give
[05:53] llms access to the data that matters you
[05:56] can build your mCP server once and see
[05:58] adoption of it every everywhere across
[06:00] all of these different AI
[06:02] applications and just a quick aside the
[06:04] way I like to frame this is uh before
[06:06] mCP we we saw a lot of the N times M
[06:09] problem where there are a ton of
[06:11] different permutations for how these
[06:12] folks interact with each other how
[06:14] client applications talk to servers um
[06:17] and mCP aims to flatten that and be the
[06:19] layer in between the application
[06:20] developers and the tool and API
[06:22] developers that want to give lm's access
[06:24] to these data for end users obviously
[06:28] this leads to more powerful and
[06:30] context-rich AI applications um if
[06:32] you've seen any of the demos on uh on
[06:35] Twitter with curser and windsurf um
[06:37] either our own first-party applications
[06:38] you've seen that these systems are um uh
[06:41] kind of context-rich and they actually
[06:43] know things about you and can go and
[06:45] take action in the real world and for
[06:48] Enterprises there's now a clear way to
[06:50] separate concerns between different
[06:52] teams that are building different things
[06:54] on the road map you might imagine that
[06:57] one team uh that owns the infrastructure
[07:00] layer has a vector DB or a rag system
[07:03] that they want to give access to to
[07:05] other teams building aifs in a pmcp
[07:08] world what we saw was every single
[07:10] individual team would build their own
[07:12] different way of accessing that Vector
[07:14] database um and deal with the the
[07:17] prompting and the actual chunking logic
[07:19] that goes behind all of this but with
[07:21] mCP an Enterprise can have a team that
[07:24] actually owns the the vector DB
[07:26] interface and turns it into an mCP
[07:28] server they can can own and maintain and
[07:30] improve that publish a set of apis um
[07:33] they can document it and then all of the
[07:35] other teams inside their company can now
[07:37] build these AI apps in a centralized way
[07:39] where they're moving a lot faster
[07:41] without needing to go and talk to that
[07:42] team every time that they need access to
[07:45] it or or need a way to get that data and
[07:48] so you can kind of Imagine This is like
[07:49] a world with microservices as well where
[07:52] uh different people different teams can
[07:54] own their specific Service uh and the
[07:56] entire company and the road map can move
[07:58] a lot faster
[08:02] cool so let's talk about adoption um
[08:05] this is something that's been really
[08:06] exciting over the past couple of months
[08:08] um it kind of comes up in almost every
[08:10] anthropic conversation with uh people
[08:12] that we work with and a lot of our
[08:14] customers um this this slide covers a
[08:17] few different personas um but we can
[08:19] start with the the applications and the
[08:21] idees um this has been really
[08:24] exciting recently and it provides this
[08:27] really nice way for people that are
[08:28] coding in IDE to provide context to that
[08:32] ID while they're working um and the
[08:34] Agents inside those IDs go and talk to
[08:36] these external systems uh like GitHub
[08:39] like documentation sites Etc we've also
[08:42] seen a lot of development on the the
[08:44] server side um I think to date there are
[08:47] something like 1100 Community built
[08:49] servers uh that folks have built um and
[08:52] published open source there are also a
[08:54] bunch of servers built by companies
[08:56] themselves I just built one as an
[08:58] example uh there are folks like uh and a
[09:01] bunch of others that have published
[09:02] official Integrations for ways to hook
[09:05] into their systems there's also a ton of
[09:07] adoption uh on the open source uh side
[09:10] as well so people that are actually
[09:11] contributing to the core protocol and
[09:14] the infrastructure layer around it so
[09:16] those
[09:39] bit about what it actually means to
[09:41] build with mCP and some of the Core
[09:43] Concepts uh that are part of the
[09:45] protocol
[09:48] itself here's kind of a view of the the
[09:51] world uh of of how to actually buildt
[09:53] with mCP so on the the left side you
[09:56] have the mCP client that invokes tools
[09:59] that queries for resources and
[10:02] interpolates prompts um and and kind of
[10:04] fills prompts with useful context for
[10:07] for the model on the server side the
[10:10] server Builder exposes each of these
[10:12] things they expose the tools the
[10:13] resources and the prompts in a way
[10:15] that's consumable by any client that
[10:17] connects to
[10:18] it so let's talk about each of these
[10:21] components a tool is maybe the most
[10:23] intuitive and and the thing that's
[10:25] developed the most over the past few
[10:27] months a tool is model control
[10:29] and what that means is the server will
[10:32] expose tools to the client application
[10:35] and the model within the client
[10:37] application the llm can actually choose
[10:39] when the best time to invoke those tools
[10:42] is so if you use cloud for desktop or
[10:44] any of these agent systems that are mCP
[10:46] compatible uh usually the way this works
[10:48] is you'll interpolate various tools into
[10:51] the prompt uh you'll give descriptions
[10:53] about how those tools are used as part
[10:54] of the server definition and the model
[10:57] inside the application will choose when
[10:59] the best time to invoke those tools are
[11:02] and these tools are are kind of uh the
[11:04] POS possibilities are kind of endless I
[11:05] mean it's read tools to retrieve data
[11:08] it's write tools to go and send data to
[11:11] applications or or kind of uh take
[11:13] actions in various systems uh it's tools
[11:15] to update databases to write files on
[11:17] your local file system uh it's kind of
[11:20] anything now we get to to resources um
[11:23] resources are data exposed to the
[11:27] application and they're application
[11:28] control controled what that means is the
[11:31] server could Define uh or create images
[11:33] it could create text files um Json maybe
[11:37] it's keeping track of you know the
[11:39] actions that you've taken with the
[11:40] server within a Json file and it exposes
[11:43] that to the application and then it's up
[11:45] to the application how to actually use
[11:47] that resource resources provide this
[11:50] Rich interface for applications and
[11:52] servers to interact that go just beyond
[11:55] you talking to a chatbot using
[11:58] text so so some of some of the use cases
[12:00] we've seen for this are files where the
[12:03] server either uh surfaces a static
[12:06] resource or static file or a dynamic
[12:08] resource where the client application
[12:11] can send the server some information
[12:13] about the user about the file system
[12:15] that they're working in and the server
[12:17] can interpolate that into this more
[12:19] complex data structure and send that
[12:21] back to the client application inside
[12:24] Cloud for desktop uh resources manifest
[12:27] as attachments so we let people when
[12:30] they're interacting with a server uh go
[12:32] and click into our UI and then select a
[12:34] resource and it gets attached to the
[12:36] chat and optionally sent to the model uh
[12:39] for whatever the the user is working on
[12:41] the resources could also be
[12:43] automatically attached you could have
[12:45] the model decide hey I see that there's
[12:47] this list of resources this one is super
[12:49] relevant to the task we're working on
[12:50] right now let me automatically attach
[12:52] this to the chat or send it to the model
[12:54] uh and then proceed from
[12:56] there and finally prompts promps are
[12:59] user controlled we like to think of them
[13:01] as the tools that the user invokes as
[13:04] opposed to something that the model
[13:05] invokes um these are predefined
[13:08] templates for common interactions that
[13:10] you might have with the specific server
[13:13] a really good manifestation of this I've
[13:14] seen is in the IDE called Zed where you
[13:17] have the concept of Slash commands where
[13:19] you're talking to the llm to the agent
[13:21] and you say hey I'm working on this PR
[13:24] can you uh go and summarize the the work
[13:27] that I've done so far and you just type
[13:29] SL GPR uh you give it the pr ID and it
[13:33] actually will interpolate this longer
[13:35] prompt that's predefined by Zed inside
[13:37] of the the MTP server and it gets sent
[13:39] to the llm um and you generate this
[13:41] really nice full data structure uh or
[13:44] full prompt uh that you can then send to
[13:46] the LM itself a few other common use
[13:49] cases uh that we've seen are different
[13:51] teams have these standardized ways of uh
[13:53] let's say doing document Q&A uh maybe
[13:55] they have formatting rules they have you
[13:58] know uh inside of a transcript they'll
[14:00] have a different speakers and different
[14:02] ways they want the data to be presented
[14:04] they can service that or Surface that
[14:07] inside the Ser uh server as a prompt and
[14:09] then the user can choose when it makes
[14:11] the most sense to
[14:14] invoke cool I'll pause there any
[14:16] questions so far about these various
[14:18] things and how they they all fit
[14:19] together yeah in the back
[14:34] yeah I I think we a big part of mCP Sor
[14:37] the question is why aren't resources uh
[14:40] modeled in the same way as tools why
[14:41] couldn't they have just been tools um a
[14:44] big part of the thinking behind mCP
[14:45] broadly is it's not just about making
[14:48] the model better it's about actually uh
[14:50] defining the ways that the application
[14:52] itself can kind of interact with the the
[14:55] server in these richer ways and so tools
[14:58] are are typically model controlled and
[15:00] we want to create a clean separation
[15:02] between what's model controlled and
[15:04] application controlled so you could
[15:06] actually imagine an application that's
[15:07] mCP compatible decides uh when it wants
[15:10] to put a resource into context maybe
[15:12] that's based on predefined rules uh
[15:14] maybe that's based on it makes an llm
[15:16] call and makes that decision but we
[15:18] wanted to create a clean separation for
[15:20] the client Builder and the server
[15:22] builder for what should be invoked by
[15:24] the the model and what should be invoked
[15:26] by the application
[15:29] I saw you go first yeah
[15:48] glasses yeah um the question is are
[15:51] tools the right way to expose let's say
[15:53] a vector database to to model um the
[15:56] answer is kind of up to you uh
[15:59] we think that these are really good to
[16:02] use when it's kind of ambiguous when a
[16:04] tool should be invoked um so maybe the
[16:07] LM sometimes should go and call a vector
[16:10] DB uh maybe sometimes it already has the
[16:12] information in context and sometimes it
[16:14] needs to go talk to uh maybe you need to
[16:16] go ask the user for more information
[16:18] before it does a search um so that's
[16:19] probably how we think about it if if
[16:21] it's predetermined then you probably
[16:23] don't need to use a tool you just always
[16:25] call that Vector
[16:27] DB uh sorry second
[16:29] so the most things NCP is able to
[16:34] more
[16:35] authentication
[16:44] how I'm going to get to that one later
[16:47] um because it's very relevant and we
[16:48] have a lot to
[16:51] say so I may have miss this on that um
[16:54] but so have you gone down the route of
[16:57] using a gentle framework tool calling um
[17:01] as you progressed would you just WRA the
[17:03] mCP with a tool if you had a
[17:10] Sy yeah I think that it sounds like the
[17:12] broader question is how does mCP fit in
[17:15] with agent Frameworks um cool yeah I
[17:18] mean the aners they they kind of
[17:20] complement each other um actually Lang
[17:22] graph just this week released a bunch of
[17:24] connectors for or I think they're called
[17:26] adapters for langra agen to connect to
[17:29] mCP so if you already have a system
[17:31] built inside Lang graph or another agent
[17:33] framework uh if it has this connector to
[17:36] mCP servers you can expose those servers
[17:38] to the agent uh without having to change
[17:40] your system itself as long as that
[17:42] adapter is installed so we don't think
[17:44] mCP is going to replace agent Frameworks
[17:47] uh we just think it makes it a lot
[17:48] easier to hook into servers tool prompts
[17:51] and resources uh in a standardized way
[17:54] okay so I
[17:55] can the framework a tool the tool mCP so
[17:59] going forward many of the tools would
[18:01] just be a W for
[18:04] mCP yeah the the framework could call a
[18:08] tool and that tool could be exposed to
[18:09] that framework from an mCP server if the
[18:12] adapter exists does that make
[18:15] sense cool I'll take one more if there
[18:18] are yeah
[18:36] so the the question is kind of does mCP
[18:38] Rel replace an agent framework and why
[18:41] still use one um I don't think it
[18:43] replaces them um I think parts of it it
[18:46] might replace the parts uh related to
[18:48] Bringing context into the agent and
[18:51] calling tools uh and invoking these
[18:53] things but uh a lot of the agent
[18:55] Frameworks value I think is in the
[18:57] Knowledge Management and the the agentic
[19:00] loop um and how the agent actually
[19:03] responds to the data that's brought in
[19:05] by tools um and so I would think that
[19:09] there is still a lot of value in
[19:10] something where the agent framework
[19:12] defines how the llm is running in the
[19:14] loop and how it actually uh decides when
[19:17] to invoke the tools uh and reach out to
[19:19] other other systems but I don't think
[19:22] mCP as a protocol itself fully replaces
[19:24] it mCP is more focused on being the
[19:26] standard layer to bring that context to
[19:28] the the agent or to the agent
[19:31] framework yeah I don't know if that's
[19:33] the the most clear answer but uh that
[19:35] that's the one that we've at least seen
[19:36] so far uh that might change as mCP
[19:40] involves cool sorry I saw one more which
[19:42] I'll take and then I will move on if
[19:44] that exists yeah
[20:22] for
[20:23] me for I know
[20:30] yeah so the question is why do resources
[20:33] and prompts exist and why isn't this all
[20:36] baked into tools because you can serve a
[20:38] lot of the same context via tools
[20:40] themselves um so I think we we touched
[20:42] on this a little bit but uh there's
[20:44] actually a lot more protocol
[20:46] capabilities built around resources and
[20:48] prompts uh than what I'm talking about
[20:50] here so part of your question was aren't
[20:52] resources in prompt static can't they
[20:54] just be served as static data as part of
[20:56] a tool uh in reality resource ources and
[20:58] prompts in mCP can also be dynamic they
[21:01] can be interpolated with context that's
[21:03] coming in from uh from the the user or
[21:06] from the application uh and then the the
[21:08] server can return a dynamic or kind of
[21:11] customized resource or customized prompt
[21:13] based on the task at hand another kind
[21:16] of really valuable thing we've seen is
[21:17] resource notifications where the client
[21:19] can actually subscribe to a resource and
[21:22] anytime that resource gets updated by
[21:24] the server with new information with new
[21:26] context the server can actually notify
[21:28] the client and tell the client hey you
[21:30] need to go update the state of your
[21:32] system or Surface new information to the
[21:35] user but the the broader answer to your
[21:37] question is yes you can do a lot of
[21:40] things with just tools but mCP isn't
[21:43] just about giving the model more context
[21:45] it's about giving the application richer
[21:47] ways to interact with the the various
[21:50] capabilities the server wants to provide
[21:52] so it's not just you want to give a
[21:55] standard way to invoke tools it's also
[21:57] if I'm server Builder
[21:59] and I want there to be a standard way
[22:00] for people to talk to my application uh
[22:03] maybe that's a prompt maybe I uh you
[22:06] know I have a a prompt that's like a
[22:09] five-step plan for how someone should uh
[22:12] invoke my server and I want the client
[22:15] applications or the users to have access
[22:17] to that that's a different Paradigm
[22:19] because it's me giving the user access
[22:21] to something as opposed to me giving the
[22:23] tool access to something um and so I I
[22:26] kind of tried to write this out as model
[22:28] control application controlled and user
[22:30] controlled the point of mCP is to give
[22:32] more control to each of these different
[22:35] parts of the system as opposed to only
[22:37] just the model
[22:39] itself yeah I hope that that kind of
[22:41] makes
[22:44] sense Co all right um let's see what
[22:48] this actually looks like the the Wi-Fi
[22:50] is a bit weird hopefully this works cool
[22:52] so what we're looking at is cloud for
[22:55] desktop which is an mCP client um let me
[22:59] try to pause as this goes through so
[23:01] Cloud for desktop which is on the left
[23:02] side an mCP client and on the right side
[23:04] I'm working inside of a GitHub
[23:06] application um let's say I'm a repo
[23:09] maintainer for the anthropic python SDK
[23:12] I need to get some work done what I'm
[23:13] doing here is I give the cloud for
[23:16] desktop app the URL of the the uh repo
[23:19] I'm working in and I say can you go and
[23:22] pull in the issues from this GitHub repo
[23:24] and help me triage them or help suggest
[23:26] the ones that that sound most important
[23:27] to you
[23:29] the model Claude automatically decides
[23:32] to invoke the list issues tool which it
[23:34] thinks is the most relevant here uh and
[23:36] actually pulls calls that and and pulls
[23:38] these into context and start summarizing
[23:40] it for me you'll also notice that I told
[23:43] it to triage them so it's automatically
[23:45] using what it knows about me from my
[23:47] previous interactions with Claude maybe
[23:49] other things in this chat or in this
[23:51] project to uh kind of intelligently
[23:54] decide here are the top five that sound
[23:56] most important to you based on what what
[23:58] I know about you and so that's where the
[23:59] interplay between just giving models
[24:02] tools and actually the application
[24:04] itself having other context about who I
[24:06] am what I'm working on the types of ways
[24:08] I like to interact with it um and and
[24:11] those things interplay with each
[24:12] other the next thing I do is can you I I
[24:15] ask it can you triage the top three
[24:17] highest priority issues and add them to
[24:19] my ASA project um I don't give it the
[24:22] name of the as project but uh Claude
[24:25] knows that it needs to go and find that
[24:26] information a autonomously so I've also
[24:29] installed an ASA server and has that has
[24:32] like 30 tools it first decides to use
[24:34] list workspaces then search projects it
[24:37] finds the projects and then it starts
[24:40] invoking tools to start adding these as
[24:42] as tasks inside of so this might be a
[24:45] pretty common application that you like
[24:47] to use but the the things I want to call
[24:49] out are one I didn't build the Asana
[24:52] server or the GitHub server these were
[24:53] built by the community each of them are
[24:56] just a couple hundred lines of code um
[24:58] primarily it's a way of surfacing tools
[25:00] to the server and so uh it's not a ton
[25:02] of additional logic to build I would
[25:04] expect they could be built in an hour um
[25:07] and they're all kind of playing together
[25:10] with Claud for desktop being the central
[25:12] interface it's really powerful to have
[25:14] these various tools that someone else
[25:16] built for systems that I care about all
[25:18] interplaying on this application that I
[25:21] like to use every single day Claud uh
[25:23] Claude for desktop kind of becomes the
[25:25] central dashboard for how I bring in
[25:28] cont context from my life and I actually
[25:30] like run my dayto day um and so ins side
[25:33] anthropic we've been using things like
[25:34] this a ton to go and reach out to you
[25:36] know our our git repos to uh even make
[25:39] PRS or to bring in context from PRS and
[25:42] MTP is the standard layer across all of
[25:49] this cool and so just to close that out
[25:52] um here's wind Surf and it's an example
[25:55] with using different servers but it's
[25:57] wind surf own application layer for
[25:59] connecting to mCP they have their own
[26:02] kind of UI inside of their agent uh
[26:04] their own way of talking to the mCP
[26:06] tools um other applications don't even
[26:08] call them mCP tools for example Goose
[26:10] calls them extensions um it's really up
[26:13] to the application Builder how to
[26:14] actually bring this context into the
[26:16] application the point is that there's a
[26:18] standard way to do this uh across all of
[26:20] these
[26:23] applications awesome so so far we've
[26:26] talked about um how to bring context in
[26:30] how mCP brings context into a lot of AI
[26:33] applications that you might already be
[26:34] familiar with but the thing that we are
[26:36] most excited about and starting to see
[26:38] signs of is that MTP will be the
[26:40] foundational protocol for agents
[26:44] broadly um and there's a few reasons for
[26:46] this one is the the actual protocol
[26:49] features and the capabilities that we're
[26:50] going to talk about in just a second um
[26:53] but it's also the the fact that these
[26:54] agent systems are becoming better the
[26:57] the models themselves are becoming
[26:58] better and they use the data you can
[27:00] bring to them uh in increasingly
[27:02] effective ways and so we think that
[27:04] there's some really nice Tailwinds here
[27:06] um and and let's talk about how or why
[27:08] we think that this is going to be the
[27:12] case so um you might be familiar with
[27:15] the the blog that we put out uh my
[27:17] friends Barry and Eric put out a couple
[27:18] months ago called building effective
[27:20] agents and one of the core things in the
[27:23] blog um that one of the first ideas that
[27:25] was introduced is this idea of an mented
[27:29] llm it's an llm uh in the the
[27:31] traditional way that it takes inputs it
[27:33] takes outputs um and it it kind of uses
[27:37] its intelligence to decide on some
[27:38] actions but the augmentation piece are
[27:41] those arrows that you see going to
[27:43] things like retrieval systems to tools
[27:46] and to memory um so those are the things
[27:49] that allow the llm to query and write
[27:51] data to various systems it allows the
[27:54] llm to go and invoke tools and respond
[27:56] to the results of those tools in
[27:58] intelligent ways and it allows the the
[28:00] llm to actually have some kind of state
[28:02] such that every interaction with it
[28:04] isn't a brand new Fresh Start it
[28:06] actually kind of keeps track of the
[28:08] progress It's Made as it goes on and so
[28:10] mCP fits in as basically that entire
[28:14] bottom layer um mCP can Federate and
[28:17] make it easier for these llms to talk to
[28:19] retrieval systems to invoke tools to
[28:22] bring in memory and it does so in a
[28:25] standardized way it means that you don't
[28:27] need to pre-build um all of these
[28:31] capabilities into the agent when you're
[28:33] actually building it it means that
[28:34] agents can expand after they've been uh
[28:38] programmed even after they've been
[28:39] initialized and they're starting to run
[28:41] to start discovering different
[28:43] capabilities uh and different
[28:45] interactions with the world even if they
[28:47] weren't programmed or built in to
[28:49] start um and and the the court thing in
[28:52] the blog or one of the simpler ideas in
[28:54] the blog is Agent systems at its core
[28:57] aren't that complicated they are this
[29:00] augmented llm concept running in a loop
[29:03] where the augmented llm goes and does a
[29:06] task it kind of works towards some kind
[29:08] of goal it uh invokes a tool looks at
[29:11] the response and then does that again
[29:13] and again and again until it's done with
[29:15] the task and so where mCP fits in is it
[29:18] gives the llm the augmented llm these
[29:21] capabilities in an open way uh what that
[29:24] means is even if you as an agent Builder
[29:27] don't know every everything that the
[29:28] agent needs to do from the time at the
[29:30] time that you're building it uh that's
[29:32] okay the the agent can go and discover
[29:34] these things uh as it's interacting with
[29:36] the system and as it's interacting with
[29:38] the real world you can let the users of
[29:40] the agent go and customize this and
[29:41] bring in their own context and their own
[29:43] ways that they want the agent to touch
[29:45] their data and you as the agent Builder
[29:47] can focus on the core Loop you can focus
[29:50] on context management uh you can focus
[29:52] on how it actually uses the memory what
[29:54] kind of model it uses the agent can be
[29:57] very focused on the actual interaction
[29:59] with the llm at its
[30:02] core um so I want to talk about a little
[30:05] bit about what this actually looks like
[30:06] in practice um let me switch over to
[30:10] screen sharing my
[30:15] screen cool so to talk about this um
[30:19] we're going to be talking about this
[30:21] framework this open source framework
[30:22] called mCP agent that was built by our
[30:24] friends at Last Mile AI I'm just using
[30:26] it as a really clean and simple example
[30:29] of how we've seen some of these agent
[30:31] systems uh kind of play in with mCP so
[30:35] I'm switching over to my code editor U
[30:38] make this bigger and what you see here
[30:41] is a pretty simple application um the
[30:43] entire thing is maybe 80 lines of code
[30:46] um and I'm defining a a set of Agents
[30:49] inside of this python file the the
[30:52] overall task that I want this agent to
[30:54] achieve is defined in this uh this task.
[30:57] MD and and uh basically I wanted to go
[31:00] and do research about Quantum Computing
[31:02] uh I wanted to give me a research report
[31:05] about quantum's computing's impact on
[31:06] cyber security and I tell it a few
[31:08] things I want I want to go look at the
[31:09] internet synthesize that information and
[31:11] then give that back to me in this nicely
[31:13] formatted
[31:14] file and so what mCP agent the framework
[31:17] lets us do is Define these different sub
[31:20] agents the first one I'm defining is
[31:22] what's called a research agent where I
[31:25] give it the task that it's an expert web
[31:27] researcher um it's its role is to uh you
[31:30] know go look on the internet to go visit
[31:32] some nice URLs and to give that data
[31:34] back in a nice instructed way in my uh
[31:37] file system and you'll see on the bottom
[31:39] is I've given it access to a few
[31:41] different mCP servers I've gave it
[31:43] access to Brave for uh searching the web
[31:46] I've given it a fetch tool to actually
[31:47] go and pull in data from the internet
[31:49] and I've given access to my file system
[31:52] I did not build any of those MTP servers
[31:55] um and I'm just telling it name and it's
[31:58] going to go and invoke them and install
[32:00] them and making sure make sure that the
[32:01] agent actually has access to
[32:03] them the next one similarly uh is a fact
[32:06] Checker agent it's going to go and
[32:07] verify the information that's coming in
[32:09] from the research agent um and it's
[32:11] using the same tools Brave Fetch and
[32:13] file system um and these are just mCP
[32:17] servers that I'm giving it access
[32:19] to and finally there's the research
[32:21] report uh writer agent and that actually
[32:23] synthesizes all the data uh looks at all
[32:26] the references and the factchecking and
[32:28] then produces a report for me in this
[32:29] nice format this time I'm only giving it
[32:32] the file system and fetch tools or
[32:33] servers um I don't need it to go look at
[32:36] the internet I just needed to process
[32:37] all the data uh that it has
[32:55] here um and it knows what servers each
[32:58] of them have access to and then once I
[33:00] kick it off the first thing it's going
[33:02] to do is go and form a plan uh a plan is
[33:05] just a series of steps for how it should
[33:08] go and interact with all these systems
[33:09] and the various steps you should take uh
[33:11] until it can call the task done so as an
[33:14] example the the first step it's going to
[33:16] go and look at authorative sources on
[33:18] Quantum Computing um and it's going to
[33:20] invoke the Searcher agent in in various
[33:23] different ways it knows uh it creates
[33:26] this plan based on the context about the
[33:28] agent's task about the servers it has
[33:30] access to uh and so on the next step is
[33:33] maybe it goes and verifies that
[33:35] information uh by focusing on the fact
[33:37] treer agent specifically and then
[33:39] finally it intends to use the writer
[33:41] agent to go and synthesize all of
[33:44] this the kind of uh core piece of this
[33:48] is mCP becomes this abstraction layer
[33:51] where the agent Builder can really just
[33:53] focus on the task specifically and the
[33:55] way that the agent should interact with
[33:57] the systems around it as opposed to the
[34:00] agent Builder having to focus on the
[34:02] actual servers themselves or the tools
[34:04] or the data it just gives uh it kind of
[34:07] declares this in this really nice
[34:08] declarative way of this is what your
[34:10] task is supposed to be and here are the
[34:12] servers or tools that you have available
[34:14] to you to go and accomplish that task
[34:17] and so just to close out that part of
[34:20] demo I'm just going to kick this off um
[34:22] and what's going to be going on in the
[34:24] background is it's going to start doing
[34:25] some research uh it's invoking the
[34:27] search Tool uh the search agent and it's
[34:30] going to invoke the fact checking agent
[34:32] and you'll start to see these outputs uh
[34:35] appear on the left side of the screen um
[34:38] and so this is a pretty simple demo but
[34:39] I think it's a very powerful thing for
[34:42] agent Builders because you can now Focus
[34:45] specifically on the agent Loop and on
[34:47] the actual core capabilities of the
[34:48] agent itself and the tasks that the the
[34:51] sub agents are working on as opposed to
[34:53] on the server capabilities and the ways
[34:55] to provide context to those agents
[34:58] the other really nice piece of this
[34:59] which is obvious is we didn't write
[35:01] those servers uh someone else in the
[35:03] community built them maybe uh the the
[35:06] most authoritative you know source of
[35:08] research papers on Quantum Computing
[35:09] wrote them um but all we're doing is
[35:12] telling our agents to go and uh
[35:14] interface with them in a specific way
[35:17] and so you start to see the the outputs
[35:19] form the it looks like the Searcher
[35:20] agent put a bunch of sources in here um
[35:23] it's already started to draft the uh the
[35:25] actual final report and it's going to
[35:27] continue to rate in the
[35:30] background
[35:33] cool try to ad
[35:40] something definitely yeah um so the
[35:43] question is have we seen Agent systems
[35:45] uh also working for proprietary data uh
[35:48] the really nice thing about mCP again is
[35:50] that it's open and so you can actually
[35:52] run MTP servers uh on inside your own
[35:55] VPC um you can run it on top of on your
[35:58] your employees individual systems or
[36:01] laptops themselves so the answer is
[36:03] definitely
[36:21] no I'm just sep
[36:32] yeah so uh the question is what does it
[36:34] mean to separate uh the agent itself and
[36:37] now the capabilities uh that other folks
[36:39] uh kind of give to it I I think the
[36:41] answer kind of varies um some of the
[36:44] ways that we've seen to improve agent
[36:46] systems are uh you know what kind of
[36:48] model do you use is it actually the
[36:49] right model for the specific task if
[36:51] you're building a coding agent or
[36:52] probably you should use use CLA um and
[36:56] there's also things like Conta
[36:57] management or Knowledge Management how
[36:59] do you store the the context and
[37:02] summarize it or compress that context as
[37:04] the context window gets larger there's
[37:06] orchestration systems like if you're
[37:08] using multi-agent are they uh in series
[37:11] are they in parallel and so there's a
[37:12] lot more that you can focus on based on
[37:14] your task uh in that sense as well as uh
[37:17] the interface itself like how is the
[37:19] surfaced to the user and the separation
[37:22] is then uh maybe you build a bunch of
[37:25] your own mCP servers for your agent that
[37:28] are really really customized to what you
[37:29] want to do but when you want to expand
[37:31] the context to what the rest of the
[37:33] world is also working on or the systems
[37:35] that exist in the rest of the world
[37:37] that's where mCP fits in like you don't
[37:38] need to go and figure out how to hook
[37:40] into those systems that's all pre-built
[37:42] for
[37:46] you uh let's do yeah that most of the
[37:50] what tool
[37:58] people
[38:03] AG
[38:18] don't yes uh there's a slide that we'll
[38:21] get to um which is exactly that um no
[38:25] you're good that's great uh really good
[38:27] questions let's I'm going to do this
[38:28] side of the room because I didn't
[38:50] yeah yeah um not a ton of this is
[38:53] specific to Last Mile I think it's a
[38:55] really great framework um
[38:58] it's called mCP D agent and specifically
[39:01] what they worked on is they saw these
[39:03] things come out one one was the agents
[39:05] framework there's really simple ways to
[39:06] think about agents and they saw mCP
[39:09] which is there are really simple ways to
[39:10] think about bringing context to agents
[39:12] um and so they built this framework
[39:14] which allows you to implement the
[39:16] various workflows that were defined in
[39:18] the agent blog post using mCP and using
[39:21] these really nice declarative Frameworks
[39:23] so what's specific to mCP agent the the
[39:25] framework is uh these these different
[39:28] components or building blocks for
[39:30] building agents so one is the concept of
[39:33] an agent and an agent as we've talked
[39:36] about is an augmented llm running in a
[39:38] loop so when you invoke an agent you
[39:40] give it a task you give it tools that it
[39:43] has access to and the framework takes
[39:46] care of running that in a loop it takes
[39:47] care of the llm that's under the hood
[39:49] and all those interactions and then
[39:51] using these building blocks you go a
[39:53] layer above and you hook those agents
[39:55] together uh in different ways that are
[39:57] more identic and those are described in
[39:59] the paper but one of the things in the
[40:01] in the blog post was this orchestrator
[40:03] workflow uh example so that's what I've
[40:05] implemented here which is I've
[40:07] initialized an orchestrator agent which
[40:09] is the one in charge of planning and
[40:10] keeping track of everything and then I
[40:12] give it to uh give it access to these
[40:14] various sub agents uh using all these
[40:16] nice things that are part of MTP agent
[40:19] that being said it's open source like
[40:21] it's not that I'm blessing this is the
[40:22] right way to do it necessarily but it's
[40:24] a really simple and elegant way of doing
[40:26] it uh sorry there a lot
[40:51] yeah yeah uh so the question is how do
[40:54] resources and prompts fit in in this
[40:56] case uh the answer is they don't um this
[40:59] example was more focused on the agentic
[41:00] loop and giving tools to them I would
[41:02] say resources and prompts come in more
[41:04] where uh the user is within the loop so
[41:07] you might imagine instead of me just
[41:09] kicking this off as a python script I
[41:11] have this nice UI where I'm talking to
[41:13] the agent and then it goes and does some
[41:15] asynchronous work in the background and
[41:17] it's a chat interface like what you
[41:19] might see with Claude in that case the
[41:22] chat interface the application could uh
[41:25] you know take this plan that I just
[41:26] showed you and surface this to me as a
[41:29] resource the application could have this
[41:31] nice UI on the side that says here's the
[41:33] the first step the Second Step third
[41:35] step and it's getting that as the server
[41:38] surfaces it to uh surface is the plan to
[41:41] it as as this kind of for line uh
[41:44] prompts could come in if um there's a
[41:47] few examples but you could say uh a
[41:50] slash command to summarize all of the
[41:52] steps that have occurred already you
[41:54] could say slash summarize uh and there's
[41:57] a predefined prompt inside of the server
[41:59] that says here's the right way to give
[42:01] the user a summary here's what you
[42:02] should uh provide to the llm when you go
[42:04] and invoke the summarization prpt uh so
[42:07] the answer your question is it doesn't
[42:08] fit in here but there are ways it could
[42:10] yeah okay I'll take like two more let
[42:13] good with you does this introduce any
[42:16] like new workflows as it relates to like
[42:21] evaluations in
[42:24] this if you're surfing a bunch of
[42:26] different tools
[42:35] the
[42:42] right I think the answer so the question
[42:45] is how does this fit into evaluations uh
[42:47] in particular evals related to uh
[42:50] assessing tool calls and and that's
[42:51] being done the right way I think um
[42:55] largely it should be the same as it is
[42:57] right now um there is potential to have
[43:02] mCP be even a standard layer inside
[43:05] evals themselves I I probably need to
[43:06] think this through but uh you can
[43:08] imagine that uh there's an mCP server
[43:11] that surfaces you know the same five
[43:14] tools and you give that server to one
[43:16] set of evals you also uh let's say you
[43:19] have one eval system running somewhere
[43:21] to evaluate these five different use
[43:23] cases they have a different eval system
[43:25] the mCP server could be the standard way
[43:27] to surface the tools that are relevant
[43:29] to your company to both of them um but
[43:30] largely I think it's similar to how it's
[43:32] been done already yeah uh the white
[44:05] um I'll get to that
[44:37] yeah um I can address part of this so
[44:40] the the question is where what is the
[44:42] separation between a lot of the uh the
[44:45] logic that you need to implement in
[44:46] these systems where should it sit should
[44:48] it sit with the client or the server and
[44:49] the specific examples are things like
[44:51] retry logic authentication um I'll get
[44:54] to O in a bit but on things like retry
[44:56] logic
[44:57] um I think my personal opinion and I
[45:00] think this remains to see be seen how it
[45:02] shakes out is a lot of that should
[45:04] happen on the server side um the server
[45:06] is closer to the end application and to
[45:09] the end system that's actually uh
[45:11] running somewhere and therefore the
[45:13] server should have more control over the
[45:15] interactions with that system a big part
[45:17] of the design principle is ideally mCP
[45:20] supports clients uh that have never seen
[45:23] a server before they don't know anything
[45:25] about that server before the first time
[45:26] it connected and therefore they
[45:28] shouldn't have to uh know the right ways
[45:31] to do retries they shouldn't have to
[45:32] know you know how to do logging in the
[45:34] exact way that the server wants uh and
[45:36] things like that so the server is
[45:38] ideally closer to the end application
[45:40] and and it's the one that's the end to
[45:42] service and it's the one that's
[45:43] implementing a lot of that business
[45:53] logic it depends um I don't have a a
[45:57] really strong opinion I take on on where
[45:59] the agent Frameworks themselves go um I
[46:02] could see one counterargument being that
[46:05] you don't always want the server
[46:07] Builders to have to deal with that logic
[46:09] either um like maybe the server Builders
[46:11] want to just focus on exposing their
[46:13] apis and like letting all the agents do
[46:15] the work
[46:17] um and yeah honestly I don't have a
[46:20] really strong take on that yeah
[46:29] yeah that's a a really good question
[46:30] why'd you ask that um so a lot of the
[46:32] questions that we get so sorry the
[46:34] question here is is there a Best
[46:36] practice or a limit to the number of
[46:37] servers that you expose to an LM um in
[46:40] practice the models of today I think are
[46:43] uh good up to like 50 or 100 tools like
[46:46] Claud is good up to a couple hundred in
[46:48] my experience um but beyond that I think
[46:51] the the the question becomes how do you
[46:54] search through or expose tools in the
[46:56] right way without over overwhelming the
[46:57] context with especially if you have
[46:58] thousands um and I think there are a few
[47:00] different ways like one of the ones
[47:01] that's exciting is a tool to search
[47:04] tools um and so you can imagine a tool
[47:06] abstraction that uh implements rag over
[47:09] tools uh it implements fuzzy search or
[47:11] keyword search um based on you know the
[47:14] entire library of tools that's available
[47:16] um that's one way um we've also seen
[47:18] like hierarchical systems of tools so
[47:20] maybe you have a group of tools that's
[47:23] uh you know Finance tools you have like
[47:25] read data then you have a group of tools
[47:27] that's for writing data and you can uh
[47:29] progressively expose those groups of
[47:31] tools based on the current task at hand
[47:33] as opposed to putting them all in the
[47:35] system from for example so there are a
[47:37] few ways to do it I don't think
[47:38] everyone's landed on one way um but the
[47:41] answer is there's technically No Limit
[47:42] if you implement it the right
[47:44] way
[47:49] okay methodology or best practice of
[47:52] like I
[47:53] have the steps take like first server
[48:03] St you have that documented yeah I'm not
[48:07] going to go through it yet but um we do
[48:10] have that documented so the question is
[48:11] like what are the right steps to
[48:13] approach building an mCP server what's
[48:14] the order of operations um we actually
[48:17] have this entire docs page that's like
[48:19] how do you build an mCP server using
[48:21] Claud or using llms um all the servers
[48:24] that we launched with in November um I
[48:26] there were like 15 of them I wrote all
[48:28] of those in like 45 minutes each with
[48:31] Claude um and so it's like really easy
[48:33] to approach it and I think tools are
[48:35] typically the best way for people to
[48:37] start grocking what a server is uh and
[48:39] then going to prompts and resources from
[48:42] there yeah definitely I'll share links
[48:44] later yeah in the red
[48:59] [Music]
[49:20] yeah
[49:21] so the question is if a lot of these
[49:24] servers are simple can llms just
[49:26] generate the automatically the answer is
[49:28] yes um if you guys have heard of Klein
[49:30] which is one of the most popular idees
[49:32] that's open source it has like 30k stars
[49:34] on GitHub they actually have an mCP
[49:36] autogenerator tool inside the app you
[49:38] can just say hey I want to start talking
[49:40] to gitlab can you make me a server and
[49:42] just autog generates on the Fly
[49:50] umoc that being said I I think that that
[49:54] works for like the simpler servers like
[49:56] the ones that are closer to just
[49:57] exposing an API but there are more
[49:59] complex things that you want to do
[50:00] you'll want to have logging or or logic
[50:02] or data Transformations um but the
[50:04] answer is yeah for the more simple ones
[50:05] I I think that's a pretty normal
[50:09] workflow are talking to
[50:20] any yeah so question is are we talking
[50:22] to the actual owners of the services and
[50:24] the data answer is yes um a lot of them
[50:28] a lot of the servers actually are
[50:30] official and public already so if I just
[50:33] scroll through official Integrations
[50:36] these are like real companies like Cloud
[50:37] flare and stripe that have already built
[50:39] official versions of these um we're also
[50:42] talking to to bigger folks um but I
[50:43] can't speak to that
[50:48] yet they might also host the servers
[50:51] remotely yes yeah like they'll build it
[50:55] and then they'll also maybe provide the
[50:56] infrastructure to expose it yeah in the
[51:06] back uh you're asking about versioning
[51:09] as it relates to the protocol or to
[51:12] servers yeah so uh the question is how
[51:14] do we do best practices or versioning uh
[51:16] all these servers are so far a lot of
[51:19] them are typescript packages or on npm
[51:22] or on pip um therefore they also have
[51:25] version package version associated with
[51:27] them and so there shouldn't generally be
[51:30] uh code breaking changes there should be
[51:32] a pretty clear upgrade path um but yeah
[51:35] I don't think we actually have best
[51:37] practices just yet for what to do when a
[51:39] server itself changes um for something
[51:43] like I mean generally I think it might
[51:45] break the workflow but I don't think it
[51:47] breaks the application if the server
[51:49] changes since uh as long as the the
[51:51] client and server are both following the
[51:53] mCP protocol the the tools that are
[51:55] available might change over time or they
[51:57] might evolve uh but the model can still
[51:59] invoke those in intelligent ways for
[52:01] resources and prompts uh they they might
[52:04] break users workflows if those resources
[52:06] impr prompt changes but like they'll
[52:07] still work um as long as they're being
[52:10] exposed as part of the mCP protocol with
[52:12] the right list tools call tools list
[52:14] resources Etc I don't know if that
[52:16] answers your question though think more
[52:25] fuzzy right um I think using versioning
[52:29] uh of the packages themselves make sense
[52:31] for that and then I'm going to talk a
[52:32] little bit about a registry and uh
[52:35] having a registry mCP registry layer on
[52:38] top of all of this will also help a lot
[52:39] with that yeah okay I'll take one more
[52:42] and then continue
[53:01] Yeah question is how are we thinking
[53:03] about distribution and extension system
[53:05] I'll get there too yeah cool let's let's
[53:08] keep
[53:10] going so
[53:22] um so we've talked about one way to
[53:25] build effect agents and I I showed how
[53:27] to do that using the mCP agent framework
[53:30] now I want to talk about the actual
[53:31] protocol capabilities that relate to
[53:34] agents and Building atic Systems um with
[53:37] a caveat that these are capabilities in
[53:39] the the protocol but uh it's still early
[53:41] days for how people are using these and
[53:43] so I think a lot of this is going to
[53:44] evolve but these are some early ideas so
[53:47] one of the most powerful things that's
[53:49] underutilized about mCP is this uh
[53:52] Paradigm called sampling sampling allows
[53:54] an mCP server to request completions um
[53:58] AKA llm inference calls from the client
[54:02] um instead of the server itself having
[54:04] to go and Implement interaction with an
[54:06] llm or to go you know host an llm or
[54:09] call clad so what this actually means is
[54:12] you know in typical applications the one
[54:13] that we've talked about so far it's a
[54:15] client um where you talk to it and then
[54:18] it goes and invokes
[54:32] server uh to have some kind of
[54:34] capability to get user inputs and then
[54:36] decide hey I actually don't have enough
[54:38] input from the user let me go ask it for
[54:40] more information uh or let me go
[54:42] formulate a question that I need to ask
[54:44] the user to give me more information and
[54:46] so there's a lot of use cases where you
[54:48] actually want the server to have access
[54:50] to intelligence and so sampling allows
[54:52] you to Federate these requests by
[54:55] letting the Cent own all interactions
[54:58] with the llm they can the client can own
[55:00] hosting the llm if it's open source they
[55:02] can own uh you know what kind of models
[55:04] it's actually using under the hood and
[55:07] the server can request inference using a
[55:10] whole bunch of different parameters so
[55:12] things like um model preferences maybe
[55:14] the server says hey I actually really
[55:15] want you know specifically this version
[55:18] of Claude uh or I want a big model or
[55:20] small model uh do your best to to get me
[55:23] one of those um the the server obviously
[55:26] will pass through a system prompt and a
[55:28] task prompt to the client um and then
[55:30] things like temperature max tokens it
[55:32] can and request uh the client doesn't
[55:34] have to listen to any of this the client
[55:36] can say hey uh this looks like a
[55:38] malicious call like I'm just not going
[55:40] to do it and uh the client has full
[55:42] control over things like privacy over
[55:45] the the cost parameters maybe it wants
[55:47] to limit the server to you know a
[55:49] certain number of requests um but the
[55:51] point is this is a really nice
[55:52] interaction because one of the design
[55:54] principles as we talked about is
[55:56] oftentimes these servers are going to be
[55:58] something where the client has never
[55:59] seen them before it knows nothing about
[56:01] them yet it still needs to have some way
[56:03] for that server to request intelligence
[56:06] um and so we're going to talk about how
[56:08] this builds up a little bit to agents
[56:10] but just uh putting this out there is
[56:11] something you should definitely explore
[56:13] uh because I think it's a bit
[56:14] underutilized thus
[56:17] far cool one of the other kind of
[56:19] building blocks of this is the idea of
[56:21] composability so I think someone over
[56:24] there asked about composability which is
[56:26] a client in a server is a logical
[56:30] separation it's not a physical
[56:31] separation and so what that means is any
[56:34] application or API or agent can be both
[56:37] an mCP client and an mCP server so if
[56:40] you look at this this very simple
[56:41] diagram let's say I'm the user talking
[56:44] to Claud for desktop on the very left
[56:46] side and that's where the llm lives and
[56:48] then I go and make a call to an agent I
[56:50] say hey can you go uh you know find me
[56:53] this information I ask the research
[56:54] agent to go do that work and that
[56:56] research agent is an mCP server but it's
[56:58] also an mCP client that research agent
[57:01] can go and invoke other servers uh maybe
[57:05] it decides it wants to call you know the
[57:06] file system server the fetch server the
[57:08] web search server um and it it goes and
[57:11] makes those calls and then brings the
[57:13] data back does something with that data
[57:14] and then brings it back to the user so
[57:17] there's this idea of of chaining and of
[57:20] these interactions kind of hopping from
[57:22] the user to a client server combination
[57:25] to the next client server combination uh
[57:27] and so on and so this allows you to
[57:28] build these really nice complicated or
[57:31] complex architectures um of of different
[57:34] layers of llm systems where each of them
[57:37] specializes in a particular task that's
[57:39] particularly relevant as well any
[57:42] questions about composability I'll touch
[57:44] on uh agents as well so
[58:09] yeah so the question is how do you deal
[58:11] with compounding errors if uh the system
[58:13] itself is is complex and multi-layered I
[58:16] think the answer is the same as it is
[58:18] for complex hierarchical like agent
[58:20] systems as well um I don't think mCP
[58:23] necessarily makes that more or less
[58:25] difficult um but in particular um yeah
[58:30] in
[58:30] particular I think it's up to each
[58:33] successive layer of the the agent system
[58:36] to uh deal with information uh or
[58:39] controlling data as it's structured so
[58:41] like to be more specific you know the
[58:43] third node there the kind of the middle
[58:45] client server node uh should collect
[58:48] data and fan in data from all of the
[58:50] other ones that just reached out to and
[58:52] it should make sure it's up to par or
[58:54] meets whatever data structure dayon
[58:55] inspect
[58:56] it needs to before passing that data to
[58:58] the system right before it um I don't
[59:00] think that's special to mCP I think that
[59:02] is true for uh all these like multi Noe
[59:05] systems um it's just this provides like
[59:08] a nice interface between each of them
[59:10] does that answer your question
[59:13] yeah I saw other hands
[59:45] yeah the question is um why are these
[59:48] why do they have to be mCP servers as
[59:50] opposed to just a regular HTTP server um
[59:53] the the answer in this case for
[59:54] composability and like the layered
[59:56] approach is that each of these can
[59:58] basically be agents um like in in the
[60:01] system that you're kind of talking about
[60:03] here uh it I I think that there's there
[60:07] are there are reasons for a bunch of
[60:09] protocol capabilities like resource
[60:10] notifications like server to client
[60:13] communication the server requesting uh
[60:15] more information from the client that
[60:17] are built into the mCP protocol itself
[60:19] so that each of these interactions are
[60:21] more powerful than just data passing
[60:23] between different nodes like let's say
[60:25] each of these are agents like the first
[60:26] agent can ask the next agent for you
[60:29] know a specific set of data it goes and
[60:31] does does a bunch of asynchronous work
[60:32] talks to the real world brings it back
[60:34] and then sends that back to the first
[60:36] client which um that might be multi-step
[60:39] it might take multiple interactions
[60:40] between each of those two nodes um and
[60:42] that's a more complex interaction that's
[60:45] captured within the mCP protocol that
[60:46] not might not be captured if it were
[60:48] just regular HTTP servers
[60:59] I think that the point I'm trying to
[61:01] make is that uh each of these so you're
[61:05] you're asking like if uh the Google API
[61:08] or the file system things were just apis
[61:10] like regular non mCP service but MC
[61:12] making it an mCP server in this at least
[61:14] in this case allows you to capture those
[61:17] as uh agents as in like they're more
[61:19] intelligent than just you know exposing
[61:21] data to the llm it's like the each of
[61:24] them has autonomy um you can give a task
[61:26] to the second server and it can go and
[61:28] make a bunch of decisions for how to
[61:29] pull in richer data um you could in
[61:32] theory just make them regular apis but
[61:34] you lose out on like these being
[61:36] independent autonomous agents each node
[61:37] in that system and the way it interacts
[61:39] with the the task it's working on yeah
[61:43] so in terms of controlling blows or
[61:45] infin and limits is that just handled by
[61:49] call or is
[61:52] there yeah um kind of depends on on the
[61:55] Builder but I I do think it's Federated
[61:58] uh because the llm is at the application
[62:00] layer um and so that has control over uh
[62:04] how R rate limits work or how it should
[62:06] actually interact with the llm uh it
[62:08] doesn't have to be that way like in
[62:10] theory if the server Builder like the
[62:12] first node wanted to own the interaction
[62:15] with a specific llm maybe it's running
[62:17] open source on that specific server it
[62:19] could be the one that controls the LM
[62:21] interaction but in the example I'm
[62:22] giving here the llm lives at the very
[62:24] base layer and the application layer and
[62:27] it's the one that's controlling rate
[62:28] limits and control flow and things like
[62:30] that so
[62:41] follow uh if it wants user input it does
[62:44] have to go all the way back yeah and mCP
[62:46] does allow you to pass those
[62:48] interactions all the way back and then
[62:50] all the way back forward yeah um I'm
[62:53] going to go on this side first yeah um
[62:56] you have to the
[62:58] primarying out a little bit there's a
[63:01] discrepancy it's
[63:06] thisat uh yeah the question is how do
[63:08] you elect a primary how do you make
[63:09] decisions in network uh the answer is
[63:12] it's kind of up to you I I'm not aining
[63:14] on like Network systems themselves or
[63:17] how uh you know these these like logic
[63:19] requirement it's not a requirement it's
[63:21] not part of the protocol itself it's
[63:23] just that mCP enables this architecture
[63:25] to exist
[63:41] yeah so um I think the idea so the
[63:44] question is how do you do observability
[63:46] how do you know the the other systems
[63:48] that are being invoked uh from a
[63:50] technical perspective there's no
[63:51] specific reason that the application or
[63:53] the user layer would know about those
[63:55] servers um in theory for example like
[63:58] the the first client application or the
[64:00] first MTP server you see there uh is
[64:02] kind of a blackbox like it makes the
[64:04] decisions about if it wants to go invoke
[64:06] other sub agents or other services and I
[64:09] think that's just how like the internet
[64:11] layer like apis work today like you
[64:13] don't exactly know always what's going
[64:14] on behind the hood the protocol doesn't
[64:16] app Pine on how observability should
[64:18] work or enforcing that you need to know
[64:21] the interactions it's really up to the
[64:22] builders and the ecosystem itself
[64:35] not even not even posibility even
[64:37] posibility it's
[64:39] like do you guys have best practices on
[64:42] this where now you don't even know like
[64:44] you're calling a server that's created
[64:45] by somebody else yeah you're right you
[64:47] call it API don't know I call St API I
[64:50] don't know exactly what that API
[64:56] based on the interface how describe dots
[64:59] but the mCP
[65:00] server if it's more than just
[65:04] like that already
[65:07] exist how can you tell how can you
[65:15] debug yeah so the question is how do you
[65:18] actually make mCP servers debuggable um
[65:20] especially if it's more than just a
[65:21] wrapper around an API and it's actually
[65:23] doing more complex things the answer is
[65:25] it
[65:26] uh the protocol itself doesn't enforce
[65:29] like specific observability and and
[65:31] interactions it's kind of like incentive
[65:33] alignment for the server Builder to
[65:35] expose useful data to the client um mCP
[65:38] does of course have ways for you to pass
[65:40] metadata um between the the client and
[65:43] the server and so if you build a good
[65:46] server that has good debugging and and
[65:48] actually provides that data back to the
[65:49] client you're more likely to be useful
[65:51] and actually like have a good ux um but
[65:54] the protocol itself doesn't kind of En
[65:56] enforce that if that's kind of what
[65:58] you're asking um which I think is the
[65:59] same answer for apis like people will
[66:01] use your API if it's ergonomic and it's
[66:03] good and makes sense and provides you
[66:05] debugging and logs um so we think
[66:07] servers should do that I think we do
[66:08] have best practices um I don't know off
[66:10] the top of my head but I can follow up
[66:11] with that so I guess somebody ask but
[66:14] for best practic and building
[66:16] servers kind of goes into that now we're
[66:19] just
[66:21] talking talking resources
[66:29] something what was
[66:35] theour sounds like
[66:38] kind are still
[66:41] develop
[66:43] that's best practices are still emerging
[66:46] are
[66:47] practices yeah I think the answer is we
[66:49] will get there like either anthropic or
[66:51] like mCP Builders themselves or the the
[66:53] community will start to converge on best
[66:55] practices but I agree with you that
[66:56] there needs to be best practices on how
[66:58] to debug and
[67:13] stuff that
[67:22] mics anal to
[67:27] we also want
[67:30] service that's exactly right yeah just
[67:32] comment on like this is very similar to
[67:34] microservices except this time we're
[67:36] bringing in intelligence but there are
[67:37] patterns that exist that we should be
[67:38] drawing from yeah um
[68:07] andar that
[68:16] language yeah the question is um let's
[68:19] say that the client wants some amount of
[68:21] control or influence over the server
[68:23] itself or the tool call like uh limit
[68:25] the number of web pages you go and look
[68:27] like look at how do you do that so yeah
[68:29] one suggestion is by doing that via the
[68:30] prompt like that's an obvious one that
[68:32] you can do uh one thing we're thinking
[68:34] about is something called like tool
[68:36] annotations um these extra parameters or
[68:39] metadata that you can Surface uh in
[68:41] addition to the regular tool call or
[68:43] specifying the tool name to influence
[68:45] something like can you limit the number
[68:47] of tools uh or limit equals five that's
[68:50] something that the server Builder and
[68:51] the tool Builder inside that server
[68:53] would have to expose uh to be invoked by
[68:56] the the client but we're thinking about
[68:58] at least in the protocol a standard uh a
[69:01] couple of standard fields that could
[69:02] could help with this so one example that
[69:04] comes to mind is maybe the server
[69:06] Builder exposes a a tool annotation
[69:09] that's read versus write and so the
[69:11] client actually can now know hey is this
[69:13] tool going to take action or is it only
[69:14] just like read only um and I think the
[69:17] opposite vice versa of that is what
[69:18] you're talking about where uh is there a
[69:20] way for the server to expose more
[69:22] parameters for how to control Its
[69:24] Behavior yeah
[69:31] you
[69:33] have any wrot mCP tool to
[69:41] diagn yeah so question on like on devx
[69:45] and how to actually you know look at the
[69:47] logs and actually respond to them so one
[69:49] um shout out is we have something called
[69:51] inspector in our repo and inspector lets
[69:53] you go look at logs and actually make
[69:55] sure that the connections to servers are
[69:57] making sense so definitely check that
[69:58] out I think your question is uh could
[70:00] you build a server that debugs servers
[70:03] um pretty sure that exists and I've seen
[70:05] it where it goes and looks at the
[70:06] standard iio logs and goes and make
[70:08] changes to to make that work um I've
[70:10] seen servers that go and set up the
[70:12] desktop config to make this work so yeah
[70:14] the answer is definitely you can have
[70:15] loops here I'll take the last one uh and
[70:17] then I'll come back to these at the end
[70:51] should
[70:56] yeah the question is around governance
[70:58] and security and who makes the decisions
[71:00] about what a client gets access to um I
[71:02] think a lot of that should be controlled
[71:05] by the server Builder um we're we're
[71:07] going to talk about oth very shortly but
[71:09] that's a really big part of it like uh
[71:11] there should be a default way in the
[71:13] protocol to there there is a default way
[71:15] in the protocol to do authorization
[71:17] authentication um and that should be a
[71:20] control layer to the end application
[71:21] that the server is connecting to um and
[71:25] yeah I think that's the design principle
[71:26] is like you could have not malicious
[71:28] clients but clients that want to ask you
[71:30] for all the information and it's the
[71:31] server Builder's responsibility to
[71:33] control that
[71:34] flow yeah I'm going to keep going and
[71:36] then I'll make sure to get back to
[71:38] questions in just a sec um so I think we
[71:41] basically have covered this but the com
[71:43] combination of sampling and
[71:45] composability um I think is really
[71:47] exciting for a world with agents um
[71:50] specifically where if I'm an end user
[71:52] talking to my application and chatbot uh
[71:54] I can can just go talk to that and it's
[71:57] a orchestrator agent that orchestrator
[71:59] agent is a server and I can reach out to
[72:01] it from my cloudword desktop but it's
[72:03] also an mCP client and it goes and talks
[72:06] to an analysis agent that's an mCP
[72:08] server a coding agent another mCP server
[72:10] and a research agent as well and the
[72:13] this is composability and sampling comes
[72:15] in where I am talking to Claude from
[72:18] Claude for desktop and the each of these
[72:21] agents and servers here are federating
[72:23] those sampling requests through the
[72:25] layers to get back to my application
[72:28] which actually controls the interaction
[72:29] with Claud um so you get these really
[72:32] nice Hier well they will exist they
[72:34] don't exist yet but you will get these
[72:35] really nice hierarchical systems of
[72:38] agents and sometimes these agents are
[72:40] going to live you know on the public web
[72:42] or they won't be built by you but you'll
[72:44] have this way to connect with them while
[72:46] still getting the privacy and security
[72:48] and control that you actually want when
[72:50] you're building these systems um so in a
[72:52] sec we're about to talk about uh what's
[72:54] next and registry and Discovery um but
[72:57] this is kind of the vision that I
[72:59] personally really want to see and I
[73:00] think we're going to get there um of
[73:02] this like connectivity layer while
[73:04] they're still being guarantees about who
[73:05] has control over the specific
[73:07] interactions in each of
[73:09] these okay I'll get take questions in in
[73:11] a sec I'm just going to keep going so
[73:15] we've talked about a few things we've
[73:16] talked about how people are using mCP
[73:18] today um we've talked about how it fits
[73:20] in with agents um there's a lot of
[73:22] really exciting things that a lot of you
[73:24] have already asked about uh that are on
[73:25] the road map and coming very soon so one
[73:28] uh is remote servers and off so um let
[73:33] me pause this to say what's going on so
[73:35] first um this is inspector uh this is
[73:38] the application I was just talking about
[73:40] where um it lets you you know install a
[73:42] server and then see all the kinds of
[73:43] various interactions uh inspector
[73:46] already actually has Au support so we
[73:49] added off to the protocol about two
[73:51] three weeks ago we then add it to
[73:53] inspector it's about to land in all the
[73:55] DK is uh so you should go and and check
[73:57] for that as soon as it's available but
[73:59] basically what we're doing here is we
[74:00] provide a URL to an mCP server for slack
[74:04] um this is happening over ssse which uh
[74:07] as opposed to standard IO ssse is the
[74:09] the best way to do remote servers um and
[74:12] so I just give it the link uh which is
[74:13] on the left side of the screen there and
[74:15] then I hit
[74:19] connect and what happens now is that the
[74:22] server is orchestrating the handoff
[74:25] between the server and slack it's doing
[74:28] the actual authentication flow and the
[74:31] way it's doing that is uh the protocol
[74:34] now supports oop 2.0 and the server
[74:36] deals with the handshake where it's
[74:38] going out to the slack server getting a
[74:40] callback URL giving it to the client the
[74:43] client opens that in in Chrome the user
[74:46] goes through the flow and clicks yeah
[74:47] this sounds good allow uh and then the
[74:49] server holds the actual uh oaf token
[74:52] itself um and then the server
[74:55] federates the interactions between the
[74:57] user and and the slack application by
[74:59] giving the client a session token for
[75:01] all future
[75:03] interactions um so the Highlight here
[75:05] and I think this is the number one thing
[75:07] we've heard since day one of launch is
[75:09] this will enable remotely hosted servers
[75:12] this means servers that live on a public
[75:14] URL um and can be discoverable by people
[75:17] through mechanisms I'll talk about in a
[75:18] sec but you don't have to mess with
[75:20] standard IO you can have the server
[75:22] fully control those interactions as
[75:24] request and they're all happening
[75:25] remotely the the agent and the llm can
[75:28] live on a completely different system
[75:30] than wherever the server is running uh
[75:32] maybe the server is an agent if you
[75:33] bring in that composability piece we
[75:35] just talked about um but this I think is
[75:37] going to be a big like explosion in the
[75:39] number of servers that you see because
[75:40] it removes the devx friction it removes
[75:43] the fact that you as a user even need to
[75:45] know what mCP is you don't even need to
[75:47] know you know how to host it or how to
[75:49] build it it's just there it exists like
[75:50] a website exists and you just go visit
[75:52] that website so any questions on remote
[75:55] Ser actually because I know a lot of
[75:56] people are interested in
[75:59] this when you're using protocol are you
[76:01] also
[76:03] controlling do an adaptation of it so
[76:07] like to increase level of access that
[76:09] they
[76:14] have yeah I think the question is um
[76:17] does our supportive oth also allow for
[76:20] it sounds like scope change or like
[76:23] again starting off with face basic
[76:25] permissions but allowing people to
[76:27] request elevated permissions and for
[76:30] those to respect it through the surve
[76:32] protoc yeah um like elevating from basic
[76:35] to Advanced permissions I think in the
[76:37] first version of it it does not support
[76:38] it out of the box but we are definitely
[76:40] interested in involving our support for
[76:42] off
[76:57] so uh the question is uh isn't it a bad
[77:01] thing that the server holds the actual
[77:03] token I think if you think about the
[77:05] design principle of the server being the
[77:08] one that actually is closest to the end
[77:10] application of slack or wherever you
[77:12] want the data to exist like let's say
[77:14] slack itself uh builds a public mCP
[77:18] server and decid decides the way that
[77:20] people should op into it uh I think
[77:22] slack will want to control the actual
[77:25] interaction between that server and the
[77:27] slack application um and then the the
[77:30] way that I think the fundamental reason
[77:32] for this is clients and servers don't
[77:34] know anything about each other before
[77:37] they start interacting um and so giving
[77:40] the server more control over how the
[77:42] interaction with the final application
[77:44] exists um I think is what allows there
[77:47] to be a separation do that kind of make
[77:49] sense
[78:06] yes uh you should be judicious about
[78:08] what servers you connect to I think
[78:10] that's true for all web apps today as
[78:11] well
[78:26] what servers they have access to but yes
[78:28] Trust of servers is going to be
[78:29] increasingly important um which we'll
[78:31] talk about with the registry in just a
[78:50] sec don't
[78:54] like a
[78:59] API yeah the question is how does this
[79:01] fit in with restful apis and does it
[79:03] interact I think uh mCP is particularly
[79:05] good when there's uh I don't know data
[79:09] Transformations or some kind of logic
[79:11] that you want to have on top of just the
[79:12] the interaction over rest um maybe that
[79:15] means there are certain things that are
[79:17] better for llm than they would be for
[79:19] just a regular old client application
[79:21] that's talking to a server maybe that's
[79:23] the way that the data is formatted maybe
[79:24] that's the amount of context you give
[79:26] back to the model um you get a request
[79:29] uh you get something back from a server
[79:31] and you say hey Claude like these are
[79:33] the five things you need to pay
[79:34] attention to this is how you should
[79:35] handle this interaction after this the
[79:37] server is controlling all that logic and
[79:39] surfacing it restful is going to still
[79:42] exist forever and that's going to be
[79:44] more for those stateless interactions
[79:45] where you're just going back and forth
[79:46] you just want the data itself
[79:50] yeah Noah
[80:21] yeah um the question is how do we think
[80:24] about regressions as servers change as
[80:27] tool descriptions change how do we do
[80:28] evals um so a couple of things one is
[80:32] we're going to talk about the registry
[80:35] in just a sec but I this probably
[80:36] something we talked about with
[80:37] versioning where you can pin a registry
[80:39] and as it changes you should test that
[80:42] new behavior um I think that this
[80:44] doesn't change too much about the evil
[80:46] eval ecosystem around tools um you might
[80:50] imagine like a lot of the customers that
[80:51] we work with we help them go and build
[80:53] these Frameworks around how their agent
[80:55] talks to tools and that's you know
[80:57] what's the right way what when should
[80:58] you be triggering a tool call how do you
[81:00] handle the response uh these are
[81:02] pre-existing evals that exist or should
[81:04] exist um I think mCP makes it easier for
[81:08] people to build these systems around
[81:10] tool calls but that doesn't change
[81:11] anything about how robust these evals
[81:13] need to be um but it does make it easier
[81:16] right because you could at least the way
[81:17] I think about it is like I have my mCP
[81:19] server 1.0 my Builder my developer
[81:22] publishes 1.1 and then I just run 1.1
[81:25] against the exact same evils framework
[81:26] and it provides this really nice like
[81:28] diff I guess um yeah I don't think it
[81:30] changes too much about the needs of
[81:32] building evals themselves yeah just the
[81:36] ergonomics
[81:40] rights um it's in the draft spec it's in
[81:43] there's an open PR in the sdks so it's
[81:46] like I would say days
[81:49] away yeah it is an inspector though it's
[81:52] like fully implemented in there so check
[81:54] it out
[81:55] cool I want to go to registry because uh
[81:57] a lot of questions about registry so a
[82:00] huge huge thing that we've seen over the
[82:02] past two months is there's no
[82:03] centralized way to discover and pull in
[82:06] uh mCP servers you've probably seen the
[82:08] the servers repo that we launched uh
[82:10] it's kind of a mess there there are like
[82:13] a bunch that we launched there are a
[82:14] bunch that our partners launched uh and
[82:16] then like 1,000 that the community
[82:18] launched and then a whole bunch of
[82:19] different ecosystems have spun up around
[82:21] this um which is pretty fragmented and
[82:23] part of the reason is like we didn't
[82:25] think it would grow this fast um and so
[82:27] we weren't quite ready to to do that but
[82:30] what we are working on is an official
[82:32] mCP registry API this is a unified and
[82:35] hosted metadata Service uh owned by the
[82:38] mCP team itself but built in the the
[82:41] open um that that means the schema is in
[82:43] the open the actual uh development of
[82:45] this is completely in the open uh but it
[82:47] lives on an API that we're we're owning
[82:48] just for the sake of there being
[82:50] something hosted and what allows you to
[82:52] do is have this layer of above the
[82:55] various package systems that already
[82:56] exists where mCP servers already exist
[82:59] and are deployed these are things like
[83:01] npm uh pipie um we've started to see
[83:04] other ones develop as well around Java
[83:06] and rust and go but the the point is a
[83:09] lot of the problems that we've been
[83:10] talking today talking about today like
[83:12] uh you know how do you discover what the
[83:15] protocol for an mCP server is is it
[83:16] standard IO is it ssse does it live
[83:20] locally on a file that I need to go and
[83:22] build and install or does it live at a
[83:23] URL
[83:25] uh who built it are they trusted uh was
[83:27] this verified by you know if Shopify has
[83:30] an official mCP server did Shopify bless
[83:32] this server um and so a lot of these
[83:34] problems I think are going to be solved
[83:36] with a registry um and we're we're going
[83:38] to work to make it as easy as possible
[83:40] for folks to Port over the entire
[83:42] ecosystem that already exists for mCP
[83:44] servers uh but the point is this is
[83:47] coming uh it's going to be great and
[83:49] we're very excited about it because I
[83:50] think a huge problem right now is
[83:52] discoverability and people don't know
[83:53] how to find find mCP servers and people
[83:56] don't know how to publish them uh and
[83:58] and where to put them uh so we're very
[84:00] very excited about this and the last
[84:01] thing I'll touch on is is versioning uh
[84:04] which a lot of people are asking about
[84:05] but you can imagine that this has its
[84:07] own versioning where there's this log of
[84:09] hey what's change between this and this
[84:11] like uh maybe the the apis themselves
[84:14] didn't change but I added a new tool or
[84:16] I added a new tool description or
[84:17] changed it uh and this allows you to
[84:19] capture that within the central
[84:21] ecosystem or metad service
[84:25] when um soon I I it's under development
[84:29] we're actually working with uh block for
[84:32] example like they're one of the open
[84:33] source folks that we work pretty closely
[84:34] with on mCP um but it's coming there's a
[84:37] spec and I've I've read
[84:43] it yeah so question is can companies
[84:45] host their own registry yeah we think of
[84:47] it I think kind of like artifactory
[84:49] where there's a public one there's
[84:51] there's an open registry you can still
[84:52] obviously do your own um the nice
[84:54] artifact of this as well is there are
[84:57] ecosystems like cursor or like BS code
[85:00] where you could hook into if you have an
[85:02] existing application and Marketplace
[85:04] that you work with you just hook into
[85:05] the API as like a second set of servers
[85:08] but we are not going to Aline on what
[85:10] the UI for that necessarily looks like
[85:12] we're just providing the
[85:14] data path to putting something in the
[85:17] registry that's
[85:22] not uh yes
[85:25] yeah uh that's a great point because
[85:26] yeah not all of these need to live on
[85:27] npm I
[85:28] think uh yeah the answer is yes
[85:31] basically we can just let you put in a
[85:32] URL as long as it's like trusted and and
[85:34] you provide morea
[85:38] data oh sorry yeah
[86:00] when you say execution um do you mean
[86:03] like how to actually surface these tools
[86:06] and like let them be built or like can
[86:08] you say more about that you
[86:18] know yeah I mean it could actually just
[86:20] be Docker we like work really closely
[86:22] with Docker themselves and they have a
[86:25] an exact mirror of that reposit the
[86:27] servers repo but it's all Docker images
[86:29] and they've done the whole build system
[86:31] uh so it literally could just be Docker
[86:32] um there's also a world where it's
[86:34] entirely remote servers like maybe you
[86:37] self host and you don't want anyone to
[86:39] deal with building uh so you just
[86:40] publish it at a URL as well
[86:50] yeah payments and permission batteries
[86:53] so haven't thought about payments yet um
[86:57] it's not something we're thinking about
[86:58] right now permission boundaries um what
[87:01] do you mean by that does that mean like
[87:02] who gets to install or like look at one
[87:04] of these servers
[87:31] yeah it's a good question I think we've
[87:32] touched on this a bit and this sounds a
[87:34] little bit separate from the registry
[87:36] API or like maybe parallel um honestly I
[87:40] think best practices are still emerging
[87:42] that that's the real answer like people
[87:43] are still figuring out the right way to
[87:44] do data governance around this um so
[87:47] yeah I don't really have like a like the
[87:48] authorative answer on this just yet
[88:15] um so I think our philosophy or like the
[88:19] principle maybe generally about open
[88:21] source is we built it we launched it and
[88:24] we want our products to be the world's
[88:26] best mCP clients but they're not going
[88:28] to be the world's only mCP clients and
[88:30] we are totally fine with that uh we have
[88:33] and are talking to other foundational
[88:34] model providers can't comment on like
[88:36] who but uh the the point is this is open
[88:39] and we intend for it to be open and if
[88:41] that creates more competition um that's
[88:44] broadly good and I think it's good for
[88:45] users and it's good for developers um so
[88:48] I think there will be periods of time
[88:50] where Claude and our first-party
[88:52] services and apis are the best
[88:54] uh that might always not always be the
[88:56] case and I think that's that's fine and
[88:57] that's a good thing as well but um yeah
[88:59] we we'll talk to other model companies
[89:01] if they're
[89:11] down can I just
[89:14] swap uh there is no specific Advantage
[89:18] Rel relating to mCP uh that requires you
[89:21] to use Claude with mCP Claude is just
[89:24] better for many reasons but like
[89:27] that's I mean it's true uh but that's
[89:30] that's more about like Claud is just
[89:31] really good at tool use and agent of
[89:32] work and that's not about something
[89:34] fundamental with mCP itself at least for
[89:36] now
[90:00] yeah um the question is like how do we
[90:02] think about servers being more proactive
[90:04] or initiating connections to the client
[90:06] so uh there's a lot that we're thinking
[90:08] about here for Server initiated actions
[90:12] so the simplest one that we can think
[90:13] about uh that already is supported is
[90:15] server initiated notifications when a
[90:18] resource changes or the server is
[90:20] maintaining a file or a log list and it
[90:21] wants to tell the client hey I just made
[90:23] an update to this or a new uh a new
[90:25] resources available um when it comes to
[90:27] sampling there isn't something in the
[90:29] protocol just yet for the server
[90:31] initiating sampling from scratch um
[90:34] where maybe it makes some decisions on
[90:36] its own and it's it reaches out uh
[90:38] that's that is something we're going to
[90:39] build um where the server will say hey
[90:42] actually like completely unrelated like
[90:43] you didn't ask me any questions but I
[90:45] want to start this interaction with you
[90:47] um and it reaches out to the client and
[90:48] the client is ready to receive those
[90:50] messages
[91:03] the the server reaching out to the
[91:04] client would happen if like the system
[91:06] itself decides it needs something like
[91:08] deterministically maybe it not not even
[91:11] predefined it could be event driven it
[91:13] could be like it just got a request from
[91:14] a user from some other system got an API
[91:16] request and it initiates the client
[91:18] thing uh also if you think about
[91:19] composability the server could in theory
[91:21] also be a client and have its own llm
[91:23] that controls uh so that's another
[91:25] reason why it could initiate connections
[91:27] yeah
[91:49] [Music]
[91:54] you have any guidelines for
[91:59] that yeah the question is guidelines uh
[92:02] between standard I and SSE the answer is
[92:05] like mCP is transport agnostic um so the
[92:08] actual like Behavior and the
[92:09] interactions between the client and
[92:11] server don't matter about uh you know
[92:13] the fundamental nature of like the
[92:14] underlying transport that being said the
[92:16] divide that we've seen so far is local
[92:19] or inmemory communication happens over
[92:21] standard IO and remote is going to
[92:23] happen over s um and I think that's the
[92:26] pattern that makes most sense but uh
[92:28] again it's it's transport agnostic if
[92:30] you want to build your own transports uh
[92:31] and support them with mCP you can easily
[92:33] do that
[92:45] [Music]
[93:07] Yeah question is does the the model have
[93:09] to be in the loop to interact with the
[93:10] server the answer is no uh the server
[93:12] exposes a standard set of apis or um
[93:15] that's probably the wrong word to use
[93:16] but a standard set of functions so call
[93:18] tools list tools call resources list
[93:20] resources um the the client application
[93:23] can call
[93:24] deterministically
[93:44] um oh interesting are you talking about
[93:46] like server to server communication
[93:48] perhaps as well
[94:05] yes
[94:18] yes I don't think there's a built-in way
[94:21] in the protocol to do this today uh um a
[94:24] lot of the interactions do have to go
[94:25] back to the client before it allows the
[94:28] tools to talk to each other and the main
[94:29] reason for that is servers don't really
[94:32] know that other servers exist for the
[94:34] most part uh that being said it pretty
[94:36] sure it's possible like it's pretty
[94:37] flexible so I think you could make that
[94:39] happen it's just not like a first class
[94:41] thing that we support
[95:17] just mentioned like code approach I
[95:20] generate code say outut on a variable
[95:29] what's your opinion that
[95:38] how to be quite honest I don't know or
[95:41] like I I don't have a strong opinion on
[95:42] this um but yeah Happ to chat with you
[95:44] after if that makes sense okay I'm gonna
[95:46] keep going um I want to talk about real
[95:50] quick why registry is is amazing um
[95:53] besides the reasons of ergonomics and
[95:54] verification all that stuff we've talked
[95:56] about but for agents specifically uh an
[95:59] mCP server registry allows you to make
[96:01] agents self-evolving what that means is
[96:04] you can dynamically discover new
[96:06] capabilities new data on the fly without
[96:09] having to know anything about those from
[96:11] the time that that agent was initialized
[96:14] or programmed in the first place so if
[96:16] you're a user and you have this General
[96:18] coding agent that knows exactly how you
[96:20] work it knows the systems that you
[96:21] usually already have access to and it
[96:23] has a control flow that really works
[96:25] well for you you say can you go check my
[96:27] graffan logs uh I think something's
[96:29] wrong with them and can you go fix this
[96:30] bug the let's say the agent wasn't
[96:32] programmed to know that the grafana uh
[96:34] server existed so it's going to go talk
[96:36] to our registry it's going to do a
[96:37] search for an official verified grafana
[96:40] server uh that has access to the right
[96:42] apis uh and then it's going to install
[96:44] or invoke that server maybe it lives on
[96:47] a remote over ssse uh and then go and do
[96:49] the actual querying and go and fix fix
[96:52] the bug um so this is pretty simple
[96:53] example but the point is as Barry
[96:56] mentioned in his talk a couple days ago
[96:57] at this conference agents are going to
[96:59] become self-evolving by letting them
[97:01] discover and choose their own tools and
[97:04] that makes that augmented llm system
[97:06] that we've talked about even more
[97:08] powerful because you don't have to pre-
[97:09] package these you don't have to
[97:10] predefine these the agent itself will go
[97:12] out and look for them and make itself
[97:15] better it gives itself context um and I
[97:17] just want to close that Loop because I
[97:18] think that's going to be really powerful
[97:20] and and I'm really excited for that
[97:52] yes the question is how do you enforce
[97:54] control over arbitrary servers arbitrary
[97:56] access I think the artifactory example
[97:58] is a really common one like you'll you
[98:00] can self host Registries and ferate
[98:02] which ones are approved or not approved
[98:04] um you could also instead of using let's
[98:06] say if we had a search API you could
[98:08] have a whit list of specific servers and
[98:11] allow there to be a tool in between uh
[98:14] where that agent has to go through that
[98:16] tool and the tool filters which servers
[98:17] it has access to um there's also the
[98:19] concept of verification like we'll in
[98:22] the registry figure out how to do this
[98:23] but uh allowing there to be an official
[98:25] Shopify server an official graffo server
[98:28] um which of course helps with this just
[98:30] a little bit but largely it it will
[98:32] follow similar things to like
[98:33] artifactory and Enterprise tools as they
[98:35] exist
[98:42] today this this is the future yeah not
[98:46] something that I currently am using but
[98:48] I don't think it's very far
[98:52] away trust
[98:56] agents I trust agents to do it correctly
[99:01] from a functional perspective I don't
[99:02] trust yet like the the servers
[99:05] themselves because there isn't like a
[99:07] great registry and all that kind of
[99:08] stuff but the CLA or like again models
[99:11] are are good enough already at like
[99:12] deciding which tools to use among
[99:14] hundreds uh so I do trust that part of
[99:16] it cool um we're getting close to time
[99:18] so I'm going to keep going there's
[99:20] another complement to server Discovery
[99:22] uh that's different from a registry and
[99:24] that is the concept of a wellknown um on
[99:27] the top here this is not a real URL but
[99:30] let's say Shopify had aw wellknown mCP
[99:33] dojon and that provided this this nice
[99:36] interface for you know here's Shopify we
[99:39] have an mCP endpoint that you should
[99:40] know about uh it has the resources and
[99:43] tools capabilities and you off with it
[99:45] uh using oaf 2 and what that means is if
[99:48] I'm a user and I talk to my agent and I
[99:50] say hey help me go manage my store on
[99:52] shopify.com
[100:07] and so this is a really nice compliment
[100:08] to the registry where the registry is
[100:10] focused on Discovery and verification
[100:13] and the ability for people to find tools
[100:15] from scratch but if you also want to go
[100:17] top down approach where you know you
[100:19] want to talk to Shopify or you uh have
[100:22] an agent that's going and looking around
[100:23] around on the internet um it can go and
[100:25] check this uh welln as a verified way of
[100:29] hey these tools do exist and uh this is
[100:31] how you use them and and that's really
[100:32] powerful and a specific thing that I'm
[100:35] particularly excited about is there's a
[100:36] really nice complement to computer use
[100:39] uh anthropic release computer use model
[100:41] in October uh or just our regular model
[100:43] is a computer use model and what it
[100:45] allows you to do is go and click around
[100:46] in these systems and these uis that it's
[100:49] never seen before that don't have apis
[100:51] that it can go and interact with but
[100:52] what if you could have that plus mCP
[100:56] Json there's a predefined way for that
[100:58] agent to go and call the apis that are
[101:01] surfaced by shopify.com but for the
[101:03] longtail where that doesn't work it can
[101:05] use computer use it can click around on
[101:07] the UI it can go login it can go
[101:09] interact with buttons and I think the
[101:11] world where those coexist inside One
[101:14] agent is the future and I think that's
[101:16] something we're thinking about um I'm
[101:18] sure other people are thinking about it
[101:19] as well and I think mCP is going to be a
[101:21] big part of that
[101:25] cool I'm going to keep going and I'll
[101:26] take questions at the end uh actually
[101:27] this is the last slide but uh besides
[101:29] everything that we've talked about today
[101:31] uh there's a lot more things that we're
[101:32] thinking about in the medium term um
[101:35] this is roughly in order of uh how much
[101:37] we're thinking about it right now but uh
[101:39] there's a big discussion this is a bit
[101:41] granular about stateful versus stateless
[101:43] connections right now mCP servers are
[101:46] somewhat stateful they they hold State
[101:48] around the connection between the server
[101:50] and client uh a lot of folks are
[101:52] interested in these more short lived
[101:53] connections where the client can
[101:55] disconnect from an mCP server go offline
[101:57] for a little bit come back later and
[101:59] continue the conversation or the request
[102:01] uh in the same way without having to
[102:03] rovide data so we're working on this um
[102:06] idea around maybe that there's a
[102:08] bifurcation between the more basic
[102:10] capabilities where it's the client
[102:11] asking the server for things versus uh
[102:14] capabilities where the server is asking
[102:16] clients for things and uh I think this
[102:18] is going to be really elegant but uh you
[102:20] can imagine for more advanced
[102:22] capabilities like sampling or server to
[102:24] client notifications they use something
[102:26] like ssse which requires there to be a
[102:28] longlived connection but for shortlived
[102:31] things where it's just say hey can you
[102:32] help me invoke this Tool uh maybe that's
[102:34] a a more shortlived like HTTP or a
[102:36] regular request that doesn't require a
[102:38] Long Live connection streaming big one
[102:41] we're thinking about is um how do we
[102:43] stream data and actually have like chunk
[102:45] multiple chunks of data arrive at the
[102:47] client from the server over time uh how
[102:49] to uh support that first class in the
[102:51] protocol name spacing uh which is also
[102:54] somewhat relevant to agents and and
[102:56] Registries as we've been talking about
[102:57] but right now tools if you install 10
[103:00] servers they have tools of the same name
[103:02] there is conflict uh often and like
[103:04] there isn't a great way right now to
[103:06] separate that other than like appending
[103:08] the server plus the tool name before you
[103:09] surface it I think the registry is going
[103:11] to help a lot with this but we also want
[103:13] to uh kind of allow this to exist first
[103:15] class in the protocol uh and maybe even
[103:17] allow people to create these like
[103:19] logical groups of different tools that
[103:21] are prepackaged into uh a really nice
[103:23] like package of I don't know Finance
[103:25] tools that are specific to these Finance
[103:27] services that people care about and
[103:29] finally I think someone asked about this
[103:31] over there but uh proactive server
[103:33] Behavior Uh elicitation where the server
[103:36] is either event driven or has some kind
[103:38] of deterministic system where it decides
[103:40] it needs to go and ask the user for more
[103:42] information or notify them about
[103:44] something uh we're just trying to figure
[103:45] out better patterns for that existing in
[103:47] the
[103:48] protocol
[103:50] cool that's my talk uh my name is m uh
[103:53] you can reach
[103:55] out LinkedIn I don't really use Twitter
[103:57] but I felt compelled to put it on there
[103:59] I'm not going to respond to you on
[104:00] Twitter though um but yeah thanks so
[104:03] much for listening this is really great
[104:06] [Music]
