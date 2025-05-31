---
type: youtube
title: Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks
author: AI Engineer
video_id: zuMw0pkPXpU
video_url: https://www.youtube.com/watch?v=zuMw0pkPXpU
thumbnail_url: https://img.youtube.com/vi/zuMw0pkPXpU/mqdefault.jpg
date_added: 2025-05-26
category: AI Development
tags: ['AI agents', 'tool definitions', 'API integration', 'system prompts', 'structured data', 'JavaScript', 'Python', 'dynamic tools', 'agentic frameworks', 'type safety', 'LLM tooling', 'API design']
entities: ['GraphQL', 'JavaScript', 'Agentic Tools', 'Tool Definitions', 'WFR Alpha', 'LangChain', 'Crei', 'SQL']
concepts: ['defining tools for AI agents', 'tool descriptions as system prompts', 'input parameters and output schemas', 'type-safe tool design', 'dynamic tools', 'agentic frameworks', 'structured outputs', 'tool calling sequences', 'API integration']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of AI agents', 'familiarity with APIs and external data sources', 'knowledge of programming languages like JavaScript/Python']
related_topics: ['API design', 'AI agent frameworks', 'system prompt engineering', 'structured data modeling', 'tool orchestration', 'type-safe programming', 'dynamic API integration', 'LLM tool development']
authority_signals: ["I'm a big RQL guy at least I was before I started to work a lot with agents", 'I see this more and more in agentic Frameworks', 'this will help you to make tools type safe']
confidence_score: 0.8
---

# Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=zuMw0pkPXpU)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai agents, tool calling, agent frameworks, reusable tools, llm, agentic frameworks, tool platforms  

## Summary

```markdown
# Summary of "Tool Calling Is Not Just Plumbing for AI Agents" by Roy Derks

## Overview
Roy Derks emphasizes that **tool calling** is a critical, often underestimated component of AI agent development. While much attention is given to refining agents themselves, the focus should shift to creating **reusable, robust, and framework-agnostic tools**. These tools act as the "plumbing" of AI systems but require careful design to ensure flexibility, accuracy, and scalability. Derks highlights the importance of structured tool definitions, dynamic capabilities, and output schemas to enable complex agent workflows.

---

## Key Points
- **Tool Calling as a Core Component**: 
  - Tool calling is not just a technical necessity but a strategic design choice. It enables agents to interact with external data, APIs, and systems.
  - Overlooking tool design can limit an agent’s effectiveness, even if the agent itself is advanced.

- **Reusability and Robustness**:
  - Tools must be **framework-agnostic** (e.g., work across different agent platforms) and **robust** to handle diverse inputs and edge cases.
  - Example: A tool calculating distances between locations should abstract away complexities like time zones or airport logistics.

- **Tool Definition Best Practices**:
  - **Tool Description**: Acts as a "system prompt" for the LLM, guiding how the tool should be used (e.g., "Calculate the number of moon orbits based on distance data").
  - **Input/Output Schemas**: 
    - Inputs must be clearly defined (e.g., "country filter" for customer data).
    - Outputs should be **structured** (e.g., JSON, SQL) to enable chaining of tool calls and reduce ambiguity.

- **Dynamic Tools**:
  - Tools should adapt to varying use cases. For example, a "web search" tool might dynamically switch between APIs or data sources based on context.

- **Analogies and Shift in Focus**:
  - **Plumbing Analogy**: Just as plumbers build custom systems or use pre-made parts, developers can either build tools from scratch or leverage existing platforms.
  - **Agent vs. Tools**: The effectiveness of an agent depends on its tools, not just its architecture. Derks quotes, *"The agent is only as good as their tools."*

---

## Important Quotes
- *"The agent is only as good as their tools."*
- *"A man is only as good as his tools."* (paraphrased)
- *"Tool descriptions almost feel like system prompts for the LLM."*
- *"Output schemas are becoming more important for structured outputs and complex agent workflows."*

---

## Actionable Takeaways
1. **Prioritize Tool Design**: 
   - Focus on creating tools that are reusable across frameworks and adaptable to different tasks.
2. **Structure Tool Definitions**:
   - Use clear, descriptive tool names, detailed descriptions, and well-defined input/output schemas.
3. **Leverage Dynamic Capabilities**:
   - Implement tools that can switch between APIs or data sources based on context.
4. **Embrace Structured Outputs**:
   - Use JSON, SQL, or other structured formats to enable chaining of tool calls and reduce ambiguity in results.
5. **Test and Iterate**:
   - Experiment with tools like GraphQL, external APIs, or scripting languages (e.g., Python, JavaScript) to find the best fit for your agent’s needs.
```

## Full Transcript

[00:04] tool calling is not just Plumbing for AI
[00:06] agents this talk I'm going to show you
[00:07] why tool calling is more important than
[00:09] some people think and how you can use
[00:11] tool calling with your AG gentic
[00:13] Frameworks we'll be looking at some of
[00:15] the techniques for Tool calling as
[00:17] regular tool calling or meta tool
[00:19] calling how this works with agent
[00:21] Frameworks and also some other
[00:23] considerations like do you need a
[00:26] separate tool platform or can you look
[00:28] at different types of tools where than
[00:30] the tools we today your own if you think
[00:33] about Plumbing uh some people say you
[00:35] should do your own Plumbing some other
[00:36] people say you should always hire a
[00:38] professional I hope at the end of this
[00:40] talk you'll be feeling like I can build
[00:42] my own tools I know how to create tools
[00:45] separate from My AG gentic Frameworks
[00:46] and bring them in and thereby get a lot
[00:48] of flexibility like changing agentic
[00:50] Frameworks or whatsoever if you think
[00:53] about agents in general I feel we spend
[00:55] a lot of time on improving the agents
[00:58] but we don't seem to spend a lot of time
[00:59] on building the tools that are reusable
[01:02] robust and can be put into different
[01:04] Frameworks I feel it's changing slightly
[01:06] there are tons of tool platforms popping
[01:08] up there are more libraries to build
[01:09] tools and I also feel the the pressure
[01:12] is sort of off the agents people know
[01:14] agents can do certain things and now
[01:16] they're all trying to improve the tools
[01:18] these
[01:20] have so my name is Roy I always worked
[01:24] for startups or founded my own startups
[01:26] uh a few years ago I ended up at IBM
[01:29] after an acquis position I've been doing
[01:32] tons of talks on graphql and web
[01:34] development and uh also react so you can
[01:37] find some of my books or previous talks
[01:39] on the internet
[01:41] um also feel free to connect with me
[01:44] social media in case you you want to
[01:46] know
[01:48] more as I mentioned in the beginning
[01:50] everyone is talking about agents but not
[01:52] so many people are talking about the
[01:53] tools these agents need you look at a
[01:56] typical agent Loop there's always a user
[01:58] asking a question or are sending a
[02:00] prompt here's the agent itself which
[02:02] needs large language models which need
[02:05] bit of memory and then of course there
[02:07] are
[02:11] tools but way less people are talking
[02:13] about these tools so everyone is talking
[02:15] about the agents what agent framework
[02:17] should I use they're probably using the
[02:19] tools that are provided by the agent
[02:20] framework or they're writing the tools
[02:22] directly inside of the agent framework
[02:24] by extending some of the functions they
[02:27] have or interfaces they have to create
[02:29] tools
[02:31] why are people not really talking about
[02:32] the tool I always feel like every time
[02:35] I'm building an agent first thing that
[02:37] breaks is the tools either the large
[02:39] language model is not able to call the
[02:41] tool correctly the large language model
[02:43] uses the wrong Tool uh maybe something
[02:46] inside my tool breaks didn't set up
[02:48] something properly the agent feels like
[02:50] like a closed circuit where the tools
[02:52] are more
[02:54] Dynamic so at the end of this talk I
[02:56] hope you you feel like the agent is only
[02:59] as good as their tools Frameworks do so
[03:02] much for you but they don't do that much
[03:04] for you in terms of building the tool
[03:06] someone once said a man is only as good
[03:08] as your tools uh so let's make that the
[03:11] agent is only as good as your tool make
[03:13] sure you have tools that are reusable
[03:15] and robust and you can bring these into
[03:17] any other agent
[03:20] framework the LMS Advance a lot over the
[03:24] last few years and that's why I also
[03:25] feel the application layer especially
[03:27] the bar where you build your tools
[03:29] deserves more attention if you look at
[03:31] some of the things people are saying on
[03:32] the internet uh it's actually saying
[03:34] like the rappers around the gpts or
[03:37] rappers around models rappers around the
[03:39] chat interfaces they're way more um they
[03:44] provide way more options for improvement
[03:46] later on and I also feel that's where we
[03:48] can do a lot more by writing software by
[03:50] coming up with smart Solutions and doing
[03:53] things on top of the models some point
[03:54] the models are going to well they are
[03:57] going to coming increasingly better but
[03:59] at some point we need to have the
[04:01] application layer catch up as
[04:03] well so let's quickly recap tool
[04:06] callings to make sure we're all on the
[04:07] same level here
[04:10] um for example imagine you're asking a
[04:12] question to an agent like how far does
[04:15] the moon orbit Express as the number of
[04:17] trips between Amsterdam and San
[04:19] Francisco so half a year ago so I moved
[04:22] from Amsterdam to San Francisco so I was
[04:24] actually kind of interested in the
[04:25] answer to question if you look it up on
[04:28] your favorite chat application
[04:30] you will find the moon's orbit is about
[04:32] 44 round trips between Amsterdam and San
[04:35] Francisco so sometimes the model might
[04:38] be able to come up if the answer itself
[04:40] because there is training data which
[04:41] includes a distance between uh the Moon
[04:44] and the Earth and then a distance
[04:45] between Amsterdam and San Francisco and
[04:48] it's able to find the answer for you
[04:50] more probably it's going to do a set of
[04:51] tool calls so going to search for the
[04:53] distance between the Earth moon going to
[04:56] search for the distance between those
[04:57] two airports and then it's going to do
[04:59] some calculations calculations maybe it
[05:01] needs a tool maybe it can do it on its
[05:03] own this question is fairly simple but
[05:06] maybe you can make more complex by
[05:08] asking how long does it take me in
[05:10] number of days or is it quicker to have
[05:13] a moon or orbit um or do those 44 round
[05:17] trips one trip is like 10 to 12 hours
[05:20] you need to wait at the airport you need
[05:22] uh fly back every time so you probably
[05:25] need a bit more than this simplified
[05:27] example
[05:30] of course you can come up with the the
[05:32] answers for these by doing tool calling
[05:33] or looking at training data if it's
[05:35] doing tool calling it's most probably
[05:37] looking at external apis so it's going
[05:39] to do a web search or it's going to go
[05:41] to some database with geographical data
[05:44] if you do the calculate maybe it's using
[05:47] JavaScript function or python or maybe
[05:50] it's going to an external API like wfr
[05:52] Alpha all of this needs to be
[05:54] implemented but how you define the tools
[05:56] matters a lot as well so before I'm
[05:58] going to show you implementation
[06:00] let me tell you why defining the tool
[06:02] matters a lot if you look at a typical
[06:04] tool definition you have your tool name
[06:06] I always advise to keep this simple you
[06:09] have your tool description and this to
[06:10] me almost feels like a system prompt for
[06:12] the large language model so your tool
[06:15] description typically it doesn't just
[06:17] say calculate something based on two
[06:19] incoming variables if you look at some
[06:21] of the bigger tools almost like agentic
[06:24] tools you can see that the tool
[06:26] descriptions are fairly long they're
[06:27] almost like system prompts some times
[06:29] you see people duplicating system
[06:32] prompts duplicating tool descriptions
[06:35] prompts so there's a lot of things you
[06:36] can do there but the tool description
[06:38] really is important then you have the
[06:40] input parameters of course model needs
[06:42] to know what is needed in order to call
[06:44] this tool and then something I really
[06:46] like and I see this more and more in
[06:48] agentic Frameworks is the output schema
[06:50] has become input variable as
[06:53] well this will make you help this will
[06:56] help you to make tools type safe as I
[06:59] mentioned I'm a big rql guy at least I
[07:01] was before I started to work a lot with
[07:04] agents if you don't have an output
[07:06] schema how's the model going to know
[07:08] what data is being returned um it's
[07:10] always a string though but if you're
[07:12] building sequence of tool callings if
[07:14] you're building more complex agents you
[07:16] probably want an output schema so you
[07:18] can for structured outputs or you can
[07:20] chain tool calls the output schema on my
[07:22] feeling is getting more and more
[07:24] important later
[07:25] on and then to will look something like
[07:28] this I believe believe this is length
[07:30] chain um could be crei as well so you
[07:33] would have your tool definition whenever
[07:35] the tool is being called it needs the
[07:37] name and that it needs the arguments say
[07:39] you want to get account of customers
[07:41] probably need to have filter like a
[07:42] country then the customer count will
[07:44] return a string which includes customer
[07:47] might also be um a string which is just
[07:50] Json that
[07:53] decode and this also works for other
[07:56] languages uh like SQL so I'm going to
[07:58] show you a bit about Dynamic tools later
[08:00] on so we've did some tests with graphql
[08:02] and SQL and using those to create
[08:04] Dynamic tools so instead of getting the
[08:06] count of a customer you could also give
[08:08] it access to a database give it access
[08:10] to an API then have the model create the
[08:12] query like query or
[08:16] graphql let's also look at where the
[08:18] tool is being called from because this
[08:20] is getting more important as well as I
[08:22] mentioned people are building their
[08:23] tools at the same place where they're
[08:24] building their agents usually so if you
[08:27] look at where the tools being called
[08:28] from you would have your agent Loop
[08:30] which has the model which has tools
[08:32] which has app some memory where do you
[08:34] implement the logic to Define which
[08:36] tools being call
[08:39] when I think it was in a blog from
[08:41] cloudfare where I saw them introducing
[08:44] their workers API and they mentioned we
[08:46] have traditional tool calling and then
[08:48] we have another form of tool kind of
[08:50] like they put traditional in there
[08:52] because I don't know we've been doing
[08:54] this for like two years maybe three so
[08:56] it all already feels like weird to call
[08:58] something traditional while time is
[09:00] moving so fast the traditional tool
[09:02] calling is I don't mind the chaos on
[09:05] this screen you would have your client
[09:07] application you would have your
[09:09] application which has the the agent
[09:12] where you have find find your tools
[09:13] where you're doing your server side
[09:15] logic so assum you have my question like
[09:18] how far does the moon orbit expresses
[09:20] trips between Amsterdam and San if you
[09:23] would type this from your client app
[09:24] which might be a chat interface goes to
[09:27] your agent or AI application
[09:29] it's going to put this in a prompt it's
[09:31] going to send it over to the model
[09:33] together with
[09:35] some model is going to tell call so
[09:39] somewhere between your client app and
[09:40] server app you're going to
[09:42] Define tool calls so you're going to
[09:44] look at the incoming recommendation from
[09:47] the large language model you're going to
[09:48] call those tools based on the have to
[09:51] find in your server app or your agent in
[09:54] here you would have some call back
[09:55] function call them and then you give
[09:57] back to Tool response model
[09:59] and at some point the model is going to
[10:01] do this a couple of times
[10:03] because calls finally you will have your
[10:06] answer which you can display Client app
[10:08] there's a lot of back and forth between
[10:10] the application where you implement
[10:12] logic and the large language model and
[10:14] then between your client up in the agent
[10:16] there's a lot of logic in there as well
[10:17] because it's not a closed system it's
[10:20] the agent and within the agent you need
[10:22] to Define tool calling logic this is
[10:25] what is called be being traditional tool
[10:27] calling um if you you implement this in
[10:30] something like lank chain like this you
[10:33] will Define your tools then you set the
[10:35] call back function for a tool you can
[10:37] see we have your models here from IBM's
[10:40] whaton next system and then you set you
[10:43] look at the answer so you look at the
[10:44] return from the large language model
[10:47] there you're going to filter the tool
[10:48] call messages so you need to explicitly
[10:50] look for a message that has the right
[10:52] role and you need to make sure that
[10:54] whatever is in there is being parsed and
[10:56] it's being executed based on the
[10:58] Callback function have then you need to
[11:01] handle all sorts of things like cuting
[11:04] the tool calls handle retries handling
[11:06] errors all these kind of things that you
[11:07] need when you're building
[11:09] any so this is how it all started this
[11:11] is what atic looked like two years ago
[11:14] maybe
[11:17] three if you look at what it looks like
[11:19] today for most most Frameworks it's
[11:22] something people like to call embedded
[11:24] tool calling so this is where the system
[11:25] is a closed closed system you pass your
[11:28] tools almost like a black box and comes
[11:31] out is the
[11:32] answer if you look at this example again
[11:34] you would have your agent this time your
[11:36] client app will only ask a question like
[11:40] how far does the moon orbit going to go
[11:42] to your agent your agent is a close
[11:44] system it has the tools it's connecting
[11:47] with the large language model it's
[11:49] connecting with the tools it's doing the
[11:50] tool calls finally you get the answer
[11:53] back like the moon or moon's orbit is
[11:55] about 44 GPS between Amsterdam and San
[11:58] Francisco
[12:00] it is what's being called embedded tool
[12:01] calling because it all is executing on
[12:03] the right side of this screen declin app
[12:06] or the application logic URI doesn't
[12:09] include any of the tool calling logic
[12:11] it's all being handled by the agent
[12:13] framework or wherever you have your
[12:15] component running and the tools in there
[12:17] they're all defined in the same agent as
[12:19] well and this is all doing the logic so
[12:21] it's really is a black box send in your
[12:24] question with a prompt and a tool and
[12:26] what comes out is the answer no control
[12:28] over whatever going on inside of
[12:31] it if you look at Leng chain again uh so
[12:34] stick to the Leng chain examples for now
[12:36] you import all the different L chain
[12:38] interfaces you import your model you
[12:41] connect to the model find your tools set
[12:44] a prompt and then you pass it into this
[12:46] create react agent function this will
[12:48] take your tools model on the prompt and
[12:51] then agent executor is going to make
[12:52] sure it's execut if you compare this to
[12:55] the previous screen it's the same
[12:56] functionality but this time it's all
[12:58] haded it's all hidden within that create
[13:00] agent function this is what people like
[13:02] to call a beta tool calling because it
[13:04] really is a black box where tools come
[13:06] in and the answer comes
[13:10] out let's say this is easy to implement
[13:13] if you're getting started building
[13:14] agents you don't need to worry about
[13:16] errors retries any of that stuff uh but
[13:19] you don't have any control over the tool
[13:20] calling process don't really know how
[13:23] the tools are being executed you don't
[13:25] know how any of the decisions are being
[13:26] made you don't really control any of the
[13:28] format
[13:29] other than that callback function you
[13:31] provide together with your tool
[13:33] definition which of course has the
[13:35] description with sort of system prompt
[13:37] for the agent to understand how to use
[13:39] the
[13:41] tool as a longtime developer I'm always
[13:44] looking for separation ofs uh I'm not
[13:47] saying you should build microservices or
[13:49] micro front ends but I do want to keep
[13:51] some systems a little bit more separated
[13:54] I I started developing at one point in
[13:56] PHP and then tools like like um all
[14:00] tools it's really a framework like larl
[14:02] and everything was sort of connected
[14:03] there you had your uh your sort of
[14:05] backend code you had your front end code
[14:07] the front end code had ways to to render
[14:10] view I believe it was few or maybe it
[14:12] was even jQuery in the beginning it was
[14:14] all a close system which I didn't really
[14:16] like so at some point I started to
[14:18] attach my back end for my front end I
[14:21] used LEL to build the apis and then I
[14:23] connected it to front end like angular
[14:26] or react maybe it was jQuery I don't
[14:28] really remember um so there's a lot of
[14:30] thing you can do to separate concerns
[14:32] without making things too big you don't
[14:34] need microservices micr France per se
[14:37] some separation between different parts
[14:39] of your system is something I always
[14:41] like to prefer and you can keep it all
[14:43] in the same
[14:44] repository put it in different different
[14:47] big
[14:48] repository the mCP is one good step in
[14:51] this direction so if you didn't hear
[14:53] about mCP yet it's a protocol introduced
[14:57] by anthropic and now being adopted by by
[14:59] uh many more people in the industry as a
[15:01] way to separate the client side and the
[15:05] server side of building atic
[15:07] applications mCP stands for model
[15:10] context protocal and this is where you
[15:12] have your host which also has a client
[15:14] in there so the host could be Cloud
[15:16] desktop it has a client in there that's
[15:18] able to connect to servers and the
[15:20] servers think of a server as a back end
[15:23] that has access tools or assets like
[15:26] data files so the server is the only
[15:29] thing the the host and the client see
[15:31] doesn't really see the tools per se
[15:33] because the tools are made available
[15:34] through the server so think of these
[15:36] server as a small back end that is able
[15:38] to give you any results from tools so I
[15:41] really like this separation of concern
[15:43] because now there's a clear distinction
[15:44] between the front side of the house and
[15:46] the back side and the mCP server is
[15:48] where you handle the logic you define
[15:50] your tools import your tools and then
[15:53] the mCP host and client they understand
[15:56] how to call these servers I wrote a
[15:58] small block post on how you can get
[15:59] started building these mCP servers using
[16:02] typescript so feel free to uh to check
[16:05] that out the link is probably a bit too
[16:06] long so if you go to my website you can
[16:09] find the uh blog section there mCP is
[16:12] really exciting I guess it's a good step
[16:14] in the direction of making uh tool
[16:16] calling really separate from the agentic
[16:18] framework there's much more you can do
[16:20] there are also other considerations and
[16:22] I hinted at this in the beginning uh you
[16:25] can for example look at a standalone
[16:27] tool platform
[16:30] and this is something that's getting
[16:31] more attention in the market I think
[16:33] there are a couple of Y combinator
[16:34] startups as well that are jumping into
[16:37] this space so a standalone tool platform
[16:39] means that instead of having a closed
[16:42] agent Loop where you define your tools
[16:44] inside of the agentic framework you
[16:46] define them separately and then inside
[16:48] of your agentic framework you can import
[16:50] those tools by writing an SDK or by
[16:52] doing an API call your tools are on
[16:54] remote servers the tool creation and the
[16:57] tool tool hosting execution is really
[17:00] being done separately the only thing the
[17:02] agent does it it takes in the tool
[17:04] definition it uses the LM to decide what
[17:07] tool to call and then it just passes
[17:09] this on to the tool platform where being
[17:11] executed tools might be chained there
[17:14] tools be abstracted away there's a lot
[17:16] of things you can do in such a platform
[17:18] as I mentioned as a developer I really
[17:20] like to separate concerns the tool
[17:23] platforms allow you to easily create
[17:26] tools out of apis or databases the
[17:28] typically these platforms of of two
[17:31] things can call them it framework as
[17:33] well I don't really mind they consist of
[17:35] two things they have a place to create
[17:37] the tool then they have a place to to
[17:40] execute the tool and the tool creation
[17:43] is usually done bya code or via clis and
[17:46] then the tool execution or the tool
[17:49] surfacing is being done via sdks that
[17:52] you connect to L chain or crew AI or
[17:54] whatever agentic framework you might be
[17:57] using in there you can also do things
[17:59] like chaining tools so sometimes you can
[18:02] see repetitive patterns in agents if you
[18:04] want to get the number of customers in a
[18:06] certain country maybe you need to do a
[18:08] tool call first to retrieve the country
[18:10] of the person asking the question based
[18:12] on their IP or whatever uh then you want
[18:14] to chain that to another tool call to
[18:16] get the actual customers out of your
[18:18] database or CRM system but this chaining
[18:21] of tool calls is something you can do in
[18:22] these platforms or Frameworks and this
[18:25] is also where you can handle
[18:26] authorization and errors and these kind
[18:28] of things
[18:29] if you think about tool calling and and
[18:31] authorization and authentication um you
[18:33] can easily imagine that you have
[18:35] different systems you're connecting
[18:37] let's say it's a CRM or let's say it's a
[18:39] database they require different sort of
[18:41] credentials uh where you set those
[18:43] credentials and how you pass them to
[18:45] these allying systems it's um well it
[18:48] could get messy quite fast and the
[18:50] question is do you want
[18:51] to do you want to put all of this in
[18:54] your agentic framework or do you want to
[18:55] separate it into a different systems
[18:58] this separ also allow you allows you to
[19:00] be flexible so imagine you have a tool
[19:02] platform where you build your tools so
[19:04] building the tools usually is the thing
[19:06] that takes me the longest for all the
[19:09] reasons I mentioned you want to take
[19:11] these tools and bring them into L chain
[19:13] or L graph if there is if it's as easy
[19:16] to bring those into crew AI or bring
[19:17] them into autogen then it really becomes
[19:20] easier for you to switch those different
[19:21] Frameworks build your tools once and
[19:23] bring them into different tic Frameworks
[19:25] so you get all of this flexibility
[19:29] as I mentioned there is a couple of tool
[19:31] Platforms in the market I'm a bit biased
[19:33] here because at IBM I'm actually
[19:35] building one but there are other great
[19:36] ones as well like compos tool house
[19:39] arcade AI which is run by a couple of
[19:42] people I met and then Wild Card which
[19:44] recently got into combinator if you look
[19:47] on the right you can see what the
[19:49] surfacing part of a tool platform might
[19:51] look like so I'm bringing in my model in
[19:53] this case uh what's the next models from
[19:55] IBM I'm then creating a l graph react
[19:58] agent I'm bringing in my tool platform
[20:00] which is called WX flow you can see
[20:02] there is a specific s thek integration
[20:04] for L chain I'm connecting to the tool
[20:06] platform so I build my tools in one
[20:08] place and then I'm connecting two these
[20:10] tools from my agent framework so I need
[20:12] an endpoint an API key but you can also
[20:14] run this locally and then just pull in
[20:17] the uh the functions or interfaces that
[20:19] way you retrieve the tools so you need
[20:21] to get the tools from one place and
[20:23] whatever you pass to that agent that
[20:25] black box is still the tools it's model
[20:28] but this time the tool execution is
[20:30] being done on that remote end so instead
[20:32] of passing in call back function you
[20:34] pass in a way for the model or in this
[20:36] case the agent actually call these tools
[20:39] so now you have separation of concerns
[20:40] you have your tools in one place and the
[20:42] agent in the other you're still doing a
[20:44] meta tool calling where the agent making
[20:47] sure the tools are being called and are
[20:49] working as expected it's calling
[20:51] subsequent tools the entire execution is
[20:54] now being put on the tool platform or
[20:56] framework so I really like this because
[20:58] now I've
[20:59] pull the two pieces apart and I can
[21:01] easily substitute Lang graph with
[21:03] something else or I can use different
[21:05] interfaces let's say langra is going to
[21:08] create different ways to create those
[21:10] blackbox agent just react maybe also
[21:13] other patterns or I can use their graph
[21:15] based approach it all works in the same
[21:17] way I still have tools in one place and
[21:19] agents in other
[21:22] place and then I hinted at this in the
[21:24] beginning what about Dynamic tools so I
[21:26] did some tests with burning graphql SQL
[21:29] with some of our clients and one thing
[21:31] we really saw is you can spend a lot of
[21:34] time creating all your tools but you
[21:35] also don't want to create a million
[21:37] tools let's say you have a CRM you don't
[21:40] want a different tool for each of the
[21:42] different components of this you can get
[21:44] your customers you don't have customers
[21:47] based per country you want to have
[21:49] customers based on I don't know whatever
[21:51] search filters you might have thanks to
[21:53] customers you also have orders maybe in
[21:56] the CRM have contracts have employee
[22:00] details whatever you can have in a CRM
[22:02] or in a database so let's say you have a
[22:04] database with have product data or order
[22:06] data or payment data you don't want to
[22:09] create all these different tools you if
[22:11] you run some tests if you put in like 10
[22:13] tools it's probably fine if you're going
[22:15] to paste in a 100 tools to the agent
[22:17] it's get really confused so you're going
[22:19] to need routers and all these things on
[22:21] top of your your tool definitions these
[22:23] tool platforms might be able to handle
[22:25] it maybe some agentic Frameworks are
[22:27] able to but another option is looking at
[22:29] Dynamic tools and I'm a big rql guy or I
[22:33] used to be mostly let's say you can also
[22:36] create a dynamic tool this is where you
[22:38] create a tool that's able to connect fql
[22:41] schema and then instead of passing in
[22:43] arguments that are sort of fixed like
[22:46] filter like get me the customers from
[22:48] from Europe and your filter would be
[22:49] Europe instead of doing this you pass in
[22:52] a graph kill
[22:53] query or you didn't really pass it in
[22:55] yourself you have the large language
[22:57] model create this for you so what you
[22:59] give to the model is you give the model
[23:01] tool and you say this is graphql you
[23:03] need to generate valid graphql to do
[23:05] so then you pass in schema so the
[23:08] graphic schema it's usually it's kind of
[23:10] small and it's easy to read for humans
[23:12] and thereby easy to understand for
[23:14] models which has your your type
[23:16] definition so it knows what's coming out
[23:19] and then it also has a list of all the
[23:20] available operations get customers or
[23:23] get orders or get customers buy
[23:26] whatever we found out by testing this
[23:29] with models like Llama Or open AI open
[23:33] AI models but also cloud is really good
[23:35] at this it's really good at generating
[23:37] graphql as long as you pass in the
[23:39] graphql schema and you don't do too
[23:42] complex things so if you want to have
[23:43] your custom scholars in graphql you want
[23:45] to get rid of those because it gets
[23:47] confused you don't want to Nest data too
[23:49] deeply so maybe nesting at one level
[23:51] deep is fine nesting like five levels
[23:53] deep is be really confusing and this is
[23:56] kind of cool because most models
[23:58] actually understand how to use graphql
[24:00] they understand things like fragments
[24:02] and I can probably spend like an hour
[24:03] talking about just building these kind
[24:05] of dynamic tools on graphql or SQL or
[24:08] query
[24:09] languages but it's a really easy way to
[24:12] bring in existing apis and databases
[24:15] your agent
[24:16] Frameworks you have less
[24:18] implementation uh in the downstream
[24:20] implementation so where you connect your
[24:22] tools where you bring your tools into
[24:23] the framework you don't need to Define
[24:25] 20 different tools and duplicate your
[24:27] business logic
[24:29] that you can take the existing business
[24:31] logic and put it directly in here so
[24:33] this allows for more flexibility but it
[24:36] also comes at a cost because there are
[24:37] trade-offs LMS might hallucinate
[24:40] sometimes it could do graphql really
[24:42] well and any other time it does really
[24:44] poorly and messes up all the different
[24:46] syntaxes so there are some trade-offs
[24:48] here but I I see a real Fe future for
[24:50] building Dynamic tools rather than the
[24:53] static tools that we
[24:55] today so in short as we're all building
[24:58] a agents let's make sure we don't forget
[25:00] the tools are as important as the agents
[25:02] we're building um so thank you for
[25:04] listening to my talk if you're at the
[25:06] conference I hope to see you if you
[25:08] aren't and you're watching this live
[25:10] make sure to follow me on social media
[25:12] and connect there so thanks again and I
[25:15] hope to see you later at some
