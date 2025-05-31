---
type: youtube
title: Vercel AI SDK Masterclass: From Fundamentals to Deep Research
author: AI Engineer
video_id: kDlqpN1JyIw
video_url: https://www.youtube.com/watch?v=kDlqpN1JyIw
thumbnail_url: https://img.youtube.com/vi/kDlqpN1JyIw/mqdefault.jpg
date_added: 2025-05-26
category: AI Development and Tool Integration
tags: ['AI SDK', 'JavaScript', 'Function Calling', 'Tool Integration', 'Language Models', 'Type Safety', 'Model Interaction', 'Tool Utility Functions', 'AI Tutorials', 'Code Execution', 'Intermediate Level', 'Tutorial']
entities: ['AI SDK', 'GPT40', 'add numbers', 'tool call', 'JavaScript', 'function calling', 'language models', 'tools', 'generate text', 'stream text']
concepts: ['Generating text from language models', 'Function calling', 'Tool calls', 'Type safety in tool parameters', 'AI SDK usage', 'Conversation context', 'JavaScript code execution', 'Model interaction with external tools', 'Tool utility functions', 'Parsing tool calls']
content_structure: tutorial/how-to
difficulty_level: intermediate
prerequisites: ['JavaScript programming', 'Basic understanding of AI models', 'Familiarity with tools and function calling concepts']
related_topics: ['AI SDKs', 'Function calling', 'Tool integration', 'JavaScript programming', 'Language models', 'Type safety in code', 'Model interaction with external systems', 'Tool utility functions']
authority_signals: ["'very simple idea'", "'completely unnecessary but is a really nice DX improvement'"]
confidence_score: 0.8
---

# Vercel AI SDK Masterclass: From Fundamentals to Deep Research

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=kDlqpN1JyIw)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: vercel ai sdk, ai agents, node js, language models, sdk development, ai programming, deep research  

## Summary

# Vercel AI SDK Masterclass Summary

## Overview
This tutorial by Vercel explores the **Vercel AI SDK**, focusing on two core primitives: **text generation** and **tool integration**. It demonstrates how to leverage language models (LLMs) for tasks like answering queries with web search capabilities, interacting with external tools, and handling sources for transparency. The session also covers integrating providers like Perplexity, Google Gemini, and OpenAI, with practical examples in Node.js.

---

## Key Points

### 1. **Text Generation with LLMs**
- **Basic Text Generation**:  
  Use `generateText` to fetch responses from LLMs (e.g., OpenAI, Perplexity).  
  Example:  
  ```js
  await generateText({ model: "gpt-4", prompt: "What is 10 + 5?" });
  ```

- **Enhanced Responses with Sources**:  
  Providers like **Perplexity** and **Google Gemini** include **sources** in responses.  
  Access sources via the `sources` property:  
  ```js
  const response = await generateText({ ... });
  console.log(response.sources); // Displays cited sources
  ```

- **Provider Flexibility**:  
  Support for multiple providers (e.g., Google, OpenAI, Perplexity) via the SDK.  
  Example:  
  ```js
  import { GoogleProvider } from "@vercel/ai";
  const response = await generateText({ model: "gemini-flash", searchGrounding: true });
  ```

---

### 2. **Tool Integration and Function Calling**
- **Core Concept**:  
  Allow LLMs to interact with external tools by providing a list of available tools.  
  Tools require:  
  - **Name**  
  - **Description** (for model to decide when to use the tool)  
  - **Parameters** (data needed for the tool)  
  - **Execute Function** (code to run when the tool is called)  

- **Example: Adding Numbers**  
  Define a tool for arithmetic:  
  ```js
  const tools = {
    "add-numbers": {
      description: "Adds two numbers",
      parameters: { a: "number", b: "number" },
      execute: async ({ a, b }) => a + b,
    },
  };
  ```

- **Tool Call Workflow**:  
  1. Model generates a **tool call** (e.g., `add-numbers(10, 5)`).  
  2. Developer parses the call and executes the corresponding function.  
  3. Results are returned to the user.

---

### 3. **Type Safety and Developer Experience**
- The SDK includes a `tool` utility function for **type safety**:  
  ```js
  import { tool } from "@vercel/ai";
  const addNumbers = tool({
    name: "add-numbers",
    description: "Adds two numbers",
    parameters: { a: "number", b: "number" },
    execute: async ({ a, b }) => a + b,
  });
  ```
- Ensures consistency between tool definitions and execution parameters.

---

## Quotes
- **"The AI SDK makes this accessible with the sources property."**  
  (Highlighting how sources are integrated into responses for transparency.)  
- **"This isn't just limited to Perplexity. We support a ton of providers..."**  
  (Emphasizing the SDK's flexibility and extensibility.)

---

## Actionable Items
1. **Set Up the SDK**:  
   Install the Vercel AI SDK and configure providers (e.g., Google, Perplexity).  
   ```bash
   npm install @vercel/ai
   ```

2. **Leverage Sources**:  
   Use `response.sources` to cite external data in generated responses.

3. **Implement Tools**:  
   Define custom tools for tasks like arithmetic, API calls, or data processing.  
   Example: Create a `get-weather` tool using a third-party API.

4. **Test with Multiple Providers**:  
   Experiment with different LLMs (e.g., OpenAI, Gemini) to compare outputs and capabilities.

5. **Ensure Type Safety**:  
   Use the `tool` utility function to enforce consistent parameter handling.  

---

## Conclusion
The Vercel AI SDK empowers developers to build LLM-powered applications with **text generation**, **tool integration**, and **source transparency**. By combining these primitives, developers can create dynamic, interactive systems that leverage the strengths of multiple LLMs and external tools.

## Full Transcript

[00:00] Hey folks, my name is Nico. I work on
[00:02] the AI SDK at Verscell. And in this
[00:05] session today, we're going to be looking
[00:07] at building agents with the AI SDK. Now,
[00:11] this session is roughly divided into two
[00:13] sections. We're going to start with a
[00:15] fundamental section. This is going to
[00:17] introduce you to the building blocks
[00:18] that you need to understand about using
[00:20] the AI SDK before we jump into building
[00:23] agents. And then we're going to be
[00:25] building a deep research clone uh in
[00:28] Node.js. JS. So without further ado,
[00:31] let's get right into it. To follow
[00:34] along, the first thing that you're going
[00:35] to have to do is clone the repository
[00:38] here, install the dependencies, copy
[00:40] over uh any environment variables, um
[00:43] and then you'll be ready to go. In this
[00:46] project, we have just one file,
[00:48] index.ts. And you can run this file by
[00:51] just running pmpp
[00:53] rundev. I have this alias to just pd. So
[00:57] if you see me typing that, that's just
[00:59] running the script. Great. So let's
[01:02] start with the first primitive that
[01:04] we're going to be looking at, the
[01:06] generate text function. Now, this is, as
[01:08] it sounds, a way for you to call a
[01:11] larger language model and generate some
[01:13] text. So let's take a look. In this
[01:15] session, rather than typing everything
[01:17] out line by line, I'm going to be
[01:19] copying over snippets so we can get
[01:21] through things a little bit faster and
[01:22] focus on the core concepts rather than
[01:24] necessarily remembering to type
[01:26] everything out properly. So, let's start
[01:28] with the first
[01:33] snippet. What we've got here is a single
[01:35] function called main. It's asynchronous.
[01:37] And inside this function, we call
[01:39] generate text, which we import from the
[01:41] AI SDK. We specify the model we want to
[01:44] use. in this case, OpenAI's GPT40 mini.
[01:48] Um, and then we pass in a prompt, hello
[01:50] world. Finally, we log out the resulting
[01:54] text that is generated and call the
[01:56] function. So, we can head into the
[01:59] terminal, run pmppm rundev, and we
[02:02] should see a message back from GPT4
[02:04] mini. Hello, how can I assist you today?
[02:07] Now each of these generate text
[02:09] functions and uh stream text and
[02:12] generate object and stream object as
[02:14] we'll see later uh can take in either a
[02:16] prompt as input or messages and in this
[02:19] case messages is just an array of
[02:21] messages where a message has a role and
[02:24] then some content. So this would be the
[02:27] same as we had before if we change this
[02:31] to user.
[02:33] For the rest of this session, we'll be
[02:34] using mostly the prompt key. So, one of
[02:37] the core features of the AI SDK is its
[02:41] unified interface. And what that means
[02:43] is that we're able to switch between
[02:45] language models by just changing one
[02:47] single line of code. Now, there are many
[02:50] reasons why you might want to do this.
[02:51] It might be because a model is cheaper,
[02:54] faster, um, better at your specific use
[02:58] case. Um, and speaking of better, one
[03:01] thing that we can try asking this model
[03:04] in particular is uh something that we
[03:08] know it might struggle with, like when
[03:10] was the AI engineer summit in
[03:16] 2025. Now, I know for a fact that GPT40
[03:20] Mini is not going to be able to do this
[03:22] because it doesn't have access to the
[03:24] web and its training data cutoff is
[03:27] somewhere in 2024. So, we can see I'm
[03:30] sorry, but I don't have information
[03:32] about events scheduled for 2025,
[03:34] including the AI engineer summit. So,
[03:37] how could we solve this? Well, we could,
[03:40] and we'll look into later, add a tool,
[03:42] and that tool could call the web and
[03:45] return those results and pipe those into
[03:47] the context of the conversation, and
[03:48] then the language model can deduce from
[03:50] there. But we could also just pick a
[03:53] model that has web search built in,
[03:56] something like perplexity. So, how do we
[03:59] change to a different model? Well, all
[04:01] we have to do
[04:04] is change the model that we specify here
[04:07] to
[04:08] perplexity, invoke that model provider
[04:11] instance, and then select the model that
[04:13] we want to use. So, in this case, we've
[04:15] imported a new uh provider this time
[04:18] from
[04:20] AISDK/perplexity. Uh, and then we
[04:22] specify we want to use sonar pro. So if
[04:24] we run this again
[04:28] now the model will come back. The AI
[04:30] engineer summit in 2025 took place from
[04:33] February 19th to February 22nd 2025 in
[04:36] New York City. This is
[04:38] right. One thing that's interesting here
[04:40] is that unlike the OpenAI response
[04:43] because Perplexity is using sources,
[04:45] it's actually named them or referenced
[04:48] them in its response. How do we access
[04:51] them? Well, the AI SDK makes this
[04:54] accessible with
[04:57] the sources property. So, we can save,
[05:00] run the script
[05:03] again, and we'll see the sources in
[05:07] line. Very, very, very cool. And this
[05:10] isn't just limited to perplexity. We
[05:12] support a ton of providers, and you can
[05:13] check all of them out at our
[05:15] documentation. If you head to a uh
[05:17] SDK.forell.ai AI and head to our
[05:20] providers page. You can see we have a
[05:22] whole host of providers here. Um many of
[05:25] which support web search as well. So if
[05:28] for example you wanted to use let's
[05:33] say Google's Gemini. So we can import
[05:36] the Google provider here and use Gemini
[05:38] flash uh 1.5 and then specify that we
[05:41] want to use search
[05:43] grounding. Save. Run the script again
[05:47] and we'll see this same prompt with the
[05:50] same configuration going off to a
[05:52] different model at a different provider
[05:54] and getting what we hope is a similar
[05:57] accurate answer. AI engineer summit took
[05:59] place from February 19th to 2025 and a
[06:02] bunch of sources in line to confirm this
[06:05] really really cool and really powerful
[06:07] stuff. So that was the first primitive
[06:09] that we looked at something as basic and
[06:11] simple as just generating text from a
[06:13] language model. But what if we want to
[06:15] go beyond generating text and use
[06:17] language models to interact with the
[06:19] outside world and to perform actions?
[06:22] This is where tools or function calling
[06:25] comes in. While tools may seem
[06:26] complicated, at the core, it's a very
[06:29] simple idea. We give the model a prompt
[06:31] and then we also pass as part of the
[06:34] conversation context a list of tools
[06:36] that it has available to it. Each of
[06:38] these tools will be provided with the
[06:40] name of the tool as well as a
[06:42] description of what the tool does so the
[06:44] model knows when to use it. And finally,
[06:47] any data that it requires in order to
[06:50] use those tools. Let's say the model
[06:53] decides it needs to use one of the tools
[06:55] to solve the user's query. Rather than
[06:58] generating some text as a response, it
[07:01] would generate a tool call. Meaning it
[07:03] would generate the the name of the tool
[07:05] it wants to use and any arguments or
[07:07] data that it can parse from the context
[07:11] of the conversation necessary to run
[07:13] those tools. It's then on you, the
[07:16] developer, to parse that tool call, run
[07:19] that code, and then do with that as you
[07:23] please. So, how do we do this with the
[07:25] AI SDK? Well, let's check out a very
[07:27] simple example. And when I say simple, I
[07:29] mean simple. We're going to ask a
[07:31] language model to add two numbers
[07:33] together. So, copy in some code here.
[07:37] We've got our same main function as
[07:38] before. We're calling generate text
[07:40] again. We're specifying our our model as
[07:42] GPT40. Our prompt this time is what's 10
[07:46] + 5? Very difficult question, but this
[07:48] time we are passing a tool. Now to pass
[07:51] tools to the generate text or stream
[07:53] text function, you pass a tools object.
[07:57] Within that object, you specify a key or
[07:59] the name of the tool. In this case, add
[08:02] numbers. Then you can as the value use
[08:06] this tool utility function which I'll
[08:08] explain in a second to then uh define
[08:11] what the tool should be. So the tool is
[08:13] going to have a description. This is
[08:14] what the tool does and this is really
[08:16] important because this is what the
[08:17] language model uses to decide whether it
[08:19] should invoke that tool. Uh parameters,
[08:22] this is the data necessary for the
[08:25] language model to run this tool. And
[08:27] this is what the language model is going
[08:28] to have to parse from the conversation
[08:31] context in order to use the tool. And
[08:33] then you have the execute function. This
[08:34] can be any arbitrary asynchronous
[08:37] JavaScript code that will be run when
[08:40] the language model generates a tool
[08:42] call. And what this tool function does
[08:46] here is this is completely unnecessary
[08:48] but is a really nice DX um improvement
[08:52] here. And what it does is that it
[08:54] provides tape type safety between the
[08:56] parameters that you define here and the
[08:59] arguments that uh come into your execute
[09:02] function. So to showcase this, if we
[09:04] change this to string, if I can spell,
[09:06] you can see I can't spell. Um, but we
[09:10] can see that num one is still a number
[09:11] where num two is a string. Uh, so again,
[09:14] this is not necessary at all. Um, but it
[09:18] does make building and uh, working with
[09:20] these tools a lot easier. Now, what's
[09:23] going on behind the scenes is that the
[09:24] AI SDK is going to parse any tool calls
[09:28] and then it's going to automatically
[09:30] invoke the execute function and return
[09:33] that in a tool results array as we can
[09:37] see right here. And that's what we're
[09:39] logging out to the console. So, if we
[09:41] head to the console, clear it out, and
[09:43] run the script, we should see a tool
[09:46] result logged out to the console. And
[09:48] that indeed we do. We see tool result uh
[09:51] add numbers. We see the arguments that
[09:54] are parsed from the conversation context
[09:56] and then we see the result
[09:59] itself. But notice that we have logged
[10:03] out the tool results this time and
[10:05] instead of instead of the the text
[10:08] generated and and I had said before it's
[10:11] kind of a nuanced thing here but the
[10:13] language model isn't generating text
[10:15] anymore. It's generating a tool call.
[10:17] And we can see that if we said
[10:18] console.log actually we just delete this
[10:20] al together and we log out the resulting
[10:24] text we won't see anything in the
[10:27] console. It's completely empty. So how
[10:29] can we get the model to actually
[10:31] incorporate the tool results into a
[10:34] generated text answer right? We want it
[10:36] to synthesize this action whatever it's
[10:39] performed and communicate that back to
[10:42] the user.
[10:44] We
[10:45] could look at the last tool result. So
[10:49] con's last tool result equals
[10:53] result.tool results. And we pop we take
[10:56] that last one. And then we say if last
[10:59] tool
[11:01] result equal uh dot dot name dot tool
[11:07] name uh equals. And it's cool. We've got
[11:09] full type safety here. Um, and then we
[11:12] can say, oh, maybe we want to await and
[11:15] and generate text further and return
[11:17] that to the user. But as you can see,
[11:20] this is errorprone. I've made like three
[11:22] mistakes already. But also, it doesn't
[11:24] scale, right? If we add 10, 15, 20, 100
[11:27] tools in here. We don't want to write
[11:29] out 100 of these conditional statements.
[11:32] So, what we can do instead is use a
[11:35] property called max
[11:38] steps. And we're going to set this to a
[11:40] number. Now max steps can seem again a
[11:43] little bit confusing but what it is at
[11:46] its core is that if the language model
[11:50] decides to generate a tool call and
[11:52] therefore there is a tool result we are
[11:55] going to send that tool result alongside
[11:58] the previous conversation context back
[12:01] to the model and trigger another
[12:03] generation and the model will continue
[12:05] doing this until it either generates
[12:08] just plain text i.e. there's no tool
[12:11] result or we reach the threshold for the
[12:14] maximum number of steps. So this is
[12:16] quite a um a a simple but powerful way
[12:21] to allow the model to keep running
[12:23] autonomously picking the next step in
[12:26] the process um without necessarily
[12:29] having to add any logic or rerouting
[12:34] repiping output here. So if we run this
[12:38] code now and and what we're going to do
[12:40] is we're actually going to log out the
[12:44] result.steps.length and actually we
[12:46] could even log out the
[12:49] whole steps so we can see what's really
[12:51] happening. And we're going to stringify
[12:54] this so it looks nice. uh we should see
[12:56] that the language model is going to
[12:58] respond to
[13:00] our if we go up all of the the crux uh
[13:04] we can see 10 + 5 equals 15. So it
[13:07] responded with plain text and now we can
[13:09] see the different steps. We've got the
[13:10] initial step which generated a tool call
[13:13] add numbers 10 and five and then we can
[13:16] see the the the tool result that we had
[13:19] logged out to the console. A bunch of uh
[13:22] stuff here. Uh cool note that you can
[13:24] tap into literally the the raw request
[13:27] and response body with the AIS SDK so
[13:29] you can see exactly what's being sent to
[13:31] language models if you ever need to
[13:33] debug. But that's aside
[13:35] um and then we should see the second
[13:38] step. Uh and the second step was step
[13:40] type tool result. Um and we can see that
[13:43] there is text actually in this uh
[13:48] generation. So cool. We've now seen how
[13:50] we can build what we're going to call a
[13:52] multi-step agent because that's what
[13:54] this is. This this language model has
[13:56] been given the ability to choose the
[13:58] number of steps that it wants to use and
[14:00] choose the the tools or the direction it
[14:02] wants to go down. But obviously having
[14:05] just one tool here doesn't show doesn't
[14:07] showcase this very well. So why don't we
[14:10] add another tool here to see this
[14:12] agentic behavior in action. What we're
[14:15] going to do is again I'm going to just
[14:17] copy over some code. We are going to add
[14:21] a tool that has the ability to get
[14:24] weather description here kind of
[14:27] obvious. Get the current weather at a
[14:29] location. The parameters here we need
[14:31] the latitude, longitude and city. Um and
[14:35] then finally in the execute function
[14:36] we're going to make a fetch request
[14:38] passing in the latitude and longitude.
[14:40] And then we are going to unwrap the
[14:42] weather data and return it in the in the
[14:45] tool result. Now a lot of people might
[14:48] be uh thinking in their
[14:50] head we're not providing the latitude
[14:53] and we're not providing the longitude
[14:54] like is this going to fail? And this
[14:57] taps into a really cool uh inference
[15:00] capability that we can use uh in these
[15:03] parameters in that we can let the
[15:05] language model infer these parameters
[15:08] from the context of the conversation. So
[15:11] we're fairly certain that the user is
[15:12] going to give city as as part of their
[15:16] prompt. And in this case we're going to
[15:18] be asking for the weather in two cities
[15:21] and then we're going to want to add them
[15:22] together. So we'll know that we'll have
[15:24] the city and we'll let the the language
[15:27] model use its training data to
[15:29] effectively infer what these might be.
[15:31] Now I wouldn't suggest doing this
[15:33] particular example in production but
[15:36] there are a lot of really cool use cases
[15:38] that you can use this pattern with. So I
[15:43] foreshadowed a little bit our prompt
[15:45] here is going to be get the weather in
[15:46] San Francisco and New York and then add
[15:48] them together. So we have two tools
[15:50] available here. Get weather and add
[15:52] numbers. And we have a maximum number of
[15:54] steps of three. So we'd expect probably
[15:57] well actually let's not even guess.
[15:58] Let's see. We can
[16:02] um print out the steps the length of the
[16:05] steps uh the steps themselves and then
[16:08] uh the resulting text generation. So I
[16:11] save run the
[16:15] script and we'll see a response. The
[16:17] current temperature in San Francisco is
[16:19] 12.3° C. In New York, it's 15.2. When
[16:23] you add these temperatures together, you
[16:25] get 27.5 degrees CC. So, let's see how
[16:28] many steps we had. Three steps. We had
[16:31] an initial step, which was a tool call
[16:34] step. Uh, we didn't unwrap this in the
[16:36] in the in the console log, but I know
[16:39] exactly what these are because I have
[16:40] done this demo before. Uh, and this is
[16:42] cool. We're using parallel tool calls
[16:44] here. Um, so the actually we can see in
[16:47] the body. We can see in the body right
[16:49] here. Um, uh, or it's probably going to
[16:52] be in the in the response actually,
[16:54] which is also wrapped in in here, not
[16:57] unwrapped. Uh, but what's happening here
[16:59] is that we're doing our get weather our
[17:02] our get weather call twice. We're doing
[17:04] for New York and then San Francisco. And
[17:07] then in our second step, we're going to
[17:09] be doing our add two numbers together.
[17:12] And then for our final step, we actually
[17:15] uh have the the text generation itself.
[17:18] Um and I can even if we do it again here
[17:22] just to show you. Uh let's stringify
[17:25] this out. Um just in case people don't
[17:29] believe me, we'll do it one more time.
[17:31] And this time we'll see exactly what is
[17:34] what is coming out.
[17:38] So if we jump, it's good good sign that
[17:40] we're getting exactly the same response.
[17:42] It means that the data is correct. Um
[17:45] and if we scroll up to the where are we
[17:48] the first
[17:50] step? So three steps here. And yeah, you
[17:53] can see so we've got two tool tool
[17:55] calls. We've got get weather for uh the
[17:57] latitude and longitude and the city of
[18:00] San Francisco. The same for oops
[18:03] scrolled too fast for New York. And then
[18:06] we have the add to numbers
[18:11] step. If we get
[18:14] there, let's scroll
[18:17] down. There we go. Add numbers. Number
[18:20] one. Number two. We get our result. And
[18:23] then finally, we have
[18:26] our actual text generation which comes
[18:29] at the very end. So awesome. That's two
[18:32] major fundamental building blocks out of
[18:34] the way. Generating text and using tool
[18:36] calls. The final thing that we're going
[18:38] to look at is generating structured
[18:40] data, also known as structured outputs.
[18:43] There are two ways to generate
[18:44] structured outputs with the AI SDK. We
[18:46] can one use generate text with its
[18:49] experimental output option which we'll
[18:50] look at first and two which we'll be
[18:52] using more later in the session using
[18:55] the generate object function which is a
[18:57] function dedicated to structured
[18:58] outputs. The generate object function I
[19:01] will I will tell you is my favorite
[19:03] function in the entire AI SDK. Absolute
[19:06] workhorse of a function and we'll see it
[19:08] later. So let's take a look at our
[19:10] existing tool calling example where
[19:11] we're getting the weather in two
[19:12] locations and then finally getting the
[19:14] sum of those two numbers added together
[19:18] and see how we could add structured
[19:20] outputs to make the eventual output
[19:23] easier to use maybe later on in our
[19:26] program. So the way that we're going to
[19:27] introduce structured outputs here is
[19:30] using the experimental I think we have
[19:32] to head up here the experimental outputs
[19:36] um output key. We can pull in
[19:40] output.object from AI um and then we
[19:43] define in here our
[19:46] schema. We're going to be using ZOD to
[19:48] define our schema. And if you've never
[19:50] used Zod before, it's a TypeScript
[19:52] validation library that is super
[19:55] powerful and particularly paired with
[19:57] the AI SDK seems like a match made in
[19:59] heaven. We'll be looking at it a lot in
[20:02] this session and it makes working with
[20:05] structured outputs an absolute breeze.
[20:07] So let's define what we want our output
[20:09] to actually be. In this case, we know we
[20:11] want the sum, which is going to be a
[20:13] number. So let's define a key of sum and
[20:16] make it a zumber. Finally, we add our
[20:20] comma. And now, instead of logging out
[20:25] all of this, all of the steps, and
[20:26] instead of logging out the text, I'm
[20:28] just going to log out the experimental
[20:30] output. And let's run the script and see
[20:33] what we
[20:35] get. So, this time, instead of getting
[20:38] all of that extra text, which we maybe
[20:40] could have prompted away, we just have a
[20:42] simple type-S safe object that we can
[20:45] access. In this case, we've got
[20:47] experimental output sum, which we know
[20:50] is going to be a number, otherwise it
[20:52] will throw an error. So, you can combine
[20:54] tool calling with structured output to
[20:56] build out some really, really awesome uh
[20:58] use cases. Now, let's very quickly look
[21:00] at the generate object function. So, I'm
[21:03] going to delete everything in our main
[21:05] function uh and copy over a generate
[21:09] object example. So, we'll save, we'll
[21:11] clear everything away. And in this case,
[21:15] uh, we're going to be looking and seeing
[21:17] if AI can help us with a very invogue
[21:21] problem, and that is defining what an AI
[21:24] agent is. I know Simon um had had posted
[21:29] a a survey on Twitter asking for
[21:33] definitions and had crowdsourced
[21:35] something like 250 different
[21:38] definitions, which ended up being six
[21:40] categories of different definitions.
[21:42] Anyway, nobody can can agree on it. And
[21:44] so let's see if AI can help us. Uh
[21:47] spoiler alert, I don't think it will.
[21:49] But so what we've got here is our main
[21:51] function as per usual. We're importing
[21:53] generate object from the AI SDK. Uh we
[21:56] specify our model as GPT4 mini. This
[21:59] should start to look quite uh similar to
[22:02] how we've been doing it previously. Pass
[22:04] in a prompt. Please come up with 10
[22:06] definitions for AI agents. And now with
[22:09] generate object, we can define a schema.
[22:11] In this case, our schema is going to
[22:13] have one key. It's going to be an
[22:14] object. That key is definitions. Every
[22:17] um and this is defined as an array of
[22:20] strings. And then that will give us a
[22:22] type- safe resulting object that has our
[22:25] definitions key on it, which is an array
[22:27] of strings. So, if we run the script,
[22:30] wait a second, we should see 10 probably
[22:34] pretty bad definitions of what an AI
[22:36] agent is. An AI agent is a software
[22:39] entity that uses artificial intelligence
[22:42] techniques to perform tasks autonomously
[22:45] or
[22:47] semiautonomously. Not as bad as I
[22:49] thought, but why don't we see if we can
[22:53] alter this slightly? And and the way I
[22:55] want to do this is provide some more
[22:59] details to the language model of exactly
[23:01] what I want it to do for each of the
[23:03] strings in this array. Now, we could
[23:06] jump into the prompt and say each of
[23:09] these definitions should be X. But one
[23:12] of the really, really cool features we
[23:14] can tap into with ZOD is the dotescribe
[23:17] function. And with dotescribe, we can,
[23:20] as it sounds, go to any key or any
[23:23] value, sorry, and we can chain on
[23:25] this.escribe function. And in here, we
[23:28] can describe exactly what we want for
[23:30] that exact value. So, I'm going to say
[23:33] something uh kind of cheeky and I'm
[23:37] going to say
[23:38] um I'm just going to paste this in. I
[23:42] want the language model to use as much
[23:44] jargon as possible. It should be
[23:46] completely incoherent. So, let's see
[23:48] what this can do. Spoiler alert, this is
[23:51] how I spend a lot of my time hacking on
[23:53] on language model stuff, just like
[23:56] asking really ridiculous stuff. And so,
[23:58] let's see what we got here. autonomous
[24:00] entities that leverage algorithmic
[24:02] huristics to optimize decision-making
[24:04] processes in dynamic
[24:06] environments. That is complete BS. Um,
[24:10] and we've got 10 of them. So, um, so
[24:13] this is a really cool thing about
[24:15] working with uh structured outputs with
[24:18] the AI SDK and particularly with that
[24:20] SOD integration. It makes defining these
[24:23] schemas and providing context super
[24:26] simple and really easy to maintain as
[24:29] well. Great. And with that, we've gone
[24:31] through the fundamentals of building
[24:33] agents with the AI SDK. Now, we're going
[24:37] to move on to a more practical project.
[24:39] We're going to be trying to build a deep
[24:42] research clone. Now, obviously, this
[24:44] isn't going to be a full crazy
[24:47] application implementation. We're just
[24:49] going to be doing it in node. So, we're
[24:50] going to have a terminal script that
[24:51] we're going to build. We're going to
[24:52] pass a query, and then we're going to
[24:55] conduct a bunch of deep research and
[24:56] write a a markdown report into our file
[25:00] system. But in doing this, this should
[25:03] introduce us to a few things. It should
[25:05] introduce us to one, how we would break
[25:07] down this idea of of deep research into
[25:10] like a structured workflow. Um, and
[25:12] within this workflow, uh, we're going to
[25:14] have some autonomous agentic elements.
[25:17] So, we'll see what a production AI
[25:19] system might look like. Um, and we'll
[25:22] also look at how we can combine
[25:24] different AI SDK functions together to
[25:26] build these more complex AI systems that
[25:30] can really cater to interesting and
[25:35] honestly cool use cases that you can use
[25:38] in production to help build cool stuff.
[25:41] I don't know how how better to to to say
[25:44] it than that. So without further ado,
[25:47] I'm going to head to the deep research
[25:49] section of the companion site because
[25:51] I've provided a nice explanation of how
[25:53] the workflow is going to work in in
[25:56] natural language and also a nice diagram
[25:58] to explain exactly what's going to be
[26:01] happening. Now also if you haven't used
[26:03] deep research before one, I highly
[26:05] suggest you check it out. Um, OpenAI has
[26:08] a version, Deep Research, uh, Gemini has
[26:10] a version as well. But roughly speaking,
[26:12] what's happening is you give these
[26:14] products a topic to think about and it
[26:17] will go off for an extended period of
[26:19] time searching the web, aggregating
[26:21] resources, going down like webs of
[26:24] thought and then it will aggregate all
[26:26] of that information together and finally
[26:28] return it into a report to hopefully
[26:31] solve your query. And the cool thing is
[26:33] this really taps into a fundamental a
[26:39] fundamentally strong part of of language
[26:41] models of this like
[26:43] synthesizing troves and troves of of
[26:46] information. Um so yeah let's look at
[26:50] how this workflow is going to look like.
[26:52] So the rough steps are going to be we're
[26:53] going to take an input a rough query a
[26:57] prompt. We're then going to for that
[26:58] prompt generate a bunch of subqueries.
[27:00] So let's think about like we want to do
[27:03] research on electric cars. Uh the
[27:05] queries or the search queries that we
[27:07] might generate are like what is an
[27:09] electric car? Who are the biggest
[27:11] electric car producers and so on. Then
[27:15] for each of those queries, we're going
[27:17] to search the web for relevant result.
[27:19] And then we're going to analyze that
[27:20] result for learnings and follow-up
[27:23] questions. And then if we want to go
[27:26] into more depth, which we'll look at in
[27:28] a second, how that works, uh we will
[27:31] take those follow-up questions as well
[27:33] as like the existing research, generate
[27:35] a new query and like completely
[27:38] recursively complete that process.
[27:40] Meaning like we basically start again
[27:43] while keeping all of the accumulated
[27:45] research. And in this way we can go down
[27:47] these like these webs of of thought and
[27:51] of questions and and and build a
[27:55] comprehensive
[27:56] aggregated a comprehensive set of
[27:59] information about a a given topic. So
[28:02] what this might look like in theory I
[28:04] like this little explanation. Uh so
[28:06] let's say we have electric cars. We're
[28:08] calling this level zero just like this
[28:09] is the initial query. And at level one
[28:12] uh we're going to have a breadth. Now
[28:14] breadth is just like how many different
[28:18] uh queries do we want at each step. So
[28:20] let's say we're at we're at level one um
[28:23] and we're doing electric cars and the
[28:24] three search queries that we generate
[28:26] are Tesla Model 3 specification electric
[28:30] car charging infrastructure and electric
[28:32] vehicle battery technology. And then for
[28:35] each of those different queries, we'd
[28:37] complete the research and maybe for
[28:40] Tesla Model 3, we would then start
[28:42] generating uh go down the web have two
[28:46] breadth. Uh like we want to generate two
[28:49] different u lines of inquiry to go down
[28:53] and then we go down. Okay, we want to
[28:55] know Model 3 range capacity and model 3
[28:57] pricing. And then for electric char car
[29:00] charging infrastructure, we want to know
[29:02] fast charging stations in the US and
[29:03] home charging installation and so on.
[29:06] And so depending on what depth and
[29:09] breadth settings we set um we're able
[29:13] to control the level of information um
[29:18] and the depth of information that we
[29:21] gather. So that was a lot. Let's uh
[29:25] let's jump into actually trying to build
[29:27] this. And the first thing that we're
[29:28] going to look at is building a function
[29:31] that can generate some search queries.
[29:34] So I'm going to dive back into
[29:37] the back into the code editor. We're
[29:40] going to clear out this file and we are
[29:43] going to copy in our first function. So
[29:46] the first thing like we said we want to
[29:48] generate a bunch of search queries. This
[29:50] is going to be a single function called
[29:52] generate search queries. I'm very
[29:54] creative. Uh it's going to take in a
[29:56] query uh which is of type string and the
[29:58] number of search queries that we
[30:00] actually want to generate. We're going
[30:01] to set this to be three just as default.
[30:03] This is for you to play around with
[30:05] later if you'd like. Um then we use the
[30:08] generate object function. We're
[30:11] specifying a main model so that we can
[30:13] just uh set it once, reference it
[30:16] everywhere, and if we want to update it
[30:17] later, we can in just one place. So
[30:19] that's why we're doing that. We have a
[30:21] prompt here. uh we we use template
[30:24] strings all over the place in this and
[30:25] you'll probably end up using them a ton.
[30:27] Super helpful uh for this use case. So
[30:30] we say generate n number of search
[30:32] queries for the following query passing
[30:34] in the the search query and then we ask
[30:38] for a structured output which should
[30:40] have a uh an array of strings minimum of
[30:44] one maximum of five although we're
[30:46] setting it kind of loosely here at uh
[30:48] three and then we return those queries.
[30:52] So that's our generate search queries
[30:54] function. If we go back to our companion
[30:57] site, we see the next thing that we have
[30:58] to do is map through each of those
[31:01] queries and search the web for relevant
[31:03] results. Analyze the result for learning
[31:06] and follow-up questions and then follow
[31:08] up with new queries. So, let's go one at
[31:10] a time. The first thing actually we
[31:12] we'll want to do is have a main function
[31:15] so that we can actually uh specify a
[31:18] prompt and then call this generate
[31:20] search queries. So our prompt is going
[31:21] to be if you were at the AI engineer
[31:23] summit there's an awesome talk and
[31:25] actually it's I think it's available
[31:26] online from the Gemini team where they
[31:28] walked through uh how they went about
[31:31] building deep research. It was a really
[31:33] really good talk and one of my favorite
[31:34] things from it was hearing the the
[31:37] prompt that they used as like the the
[31:40] kind of the gold standard to evaluate
[31:42] the progress of the the product and that
[31:46] was what do you need to be a D1 shot put
[31:49] athlete. So in that similar vein, we're
[31:52] going to be using that
[31:53] today. So we take that prompt and then
[31:55] we pass it into our generate search
[31:57] queries function. Uh because we
[32:00] specified a default number of search
[32:02] queries as three, we we don't need to
[32:04] specify one here. Uh and then that's
[32:07] going to return our queries. So we can
[32:09] do just a little checkin to see what's
[32:11] happening here and log out our queries.
[32:15] run the script and we should see fairly
[32:18] quickly we've got three potential search
[32:20] queries for our prompt of what do you
[32:23] need to be a D1 shotput athlete. These
[32:25] are obviously geared for a search
[32:27] engine. So like requirements to become a
[32:29] D1 shotput athlete, training regiment
[32:31] for D1 shotput athlete, qualifications
[32:33] for NCAA division one shot put. So three
[32:37] pretty good queries that I think would
[32:38] make sense to to look for if you wanted
[32:41] to learn more about this. All right,
[32:44] back to our companion site. We'll see
[32:47] the next thing that we need to do, map
[32:48] through these queries and search the web
[32:50] for a relevant result. First thing that
[32:52] we're going to implement now is a
[32:53] function to actually search the web for
[32:56] relevant results. And the service we're
[32:59] actually going to use today to do this
[33:00] is called Exa. Uh if you haven't used it
[33:03] before, highly rate it. Um
[33:06] uh really enjoy using it. It's fast,
[33:09] cheap.
[33:10] Um, but judge for yourself like we'll
[33:12] use it now and uh I think they've got a
[33:15] great API and so yeah, let's build a
[33:18] function to search the web with
[33:22] Excel. So I'm going to copy over some
[33:24] code. We'll head back to uh our codebase
[33:27] and we're going to make a few new lines
[33:29] here. Uh so what we're going to do is
[33:31] we're going to import XA from the XAJS
[33:33] package. We're going to instantiate XA
[33:36] extra XA passing in our XA API key. Uh
[33:41] we're going to define a type which we're
[33:42] going to be using heavily later. And
[33:44] then finally we are going to actually
[33:47] search the web. So our search web
[33:49] function takes in a query which is a
[33:51] type string and then it's going to use
[33:53] the excess search and contents function
[33:57] uh passing in our query and then
[33:59] specifying some optional config. Two
[34:02] optional config we have here is one the
[34:04] number of results we want. I've left
[34:06] this as one just as this is a simple
[34:08] demo, but you'd probably want to set
[34:10] this as configurable and allow the
[34:11] language model to infer what is
[34:13] necessary based on maybe like how
[34:16] complicated something might be. I don't
[34:18] know that's something for you to
[34:20] experiment with. Um and then the second
[34:22] option is live crawl. Um and live crawl
[34:25] is kind of as it sound allows you to or
[34:28] ensures that the results that you're
[34:30] getting are live. uh rather than
[34:32] something that's in their cache. So you
[34:34] obviously take a little bit of a hit on
[34:36] performance or time for this uh result
[34:40] to be executed, but you're sure that
[34:42] everything that is executed is is is
[34:45] live is up to
[34:46] date. Now the other thing that I'm doing
[34:49] here is that I'm actually mapping
[34:50] through the results and only returning
[34:54] the information that I feel is relevant
[34:57] or necessary for completing this
[35:00] process. And there are a few reasons for
[35:02] doing this, but the main reason is to
[35:04] reduce the number of tokens that I'm
[35:06] sending to OpenAI. Um, two reasons for
[35:09] that. One is that it's cheaper. Fewer
[35:13] tokens just going to be cheaper. Um, but
[35:16] second, and more important, I found that
[35:18] the language model is so much more
[35:20] effective when you trim away all of the
[35:22] irrelevant information. So, um, things
[35:25] like a favicon, favicon link is going to
[35:28] take up a decent amount of space. not
[35:30] necessary at all for the language model
[35:32] to actually use these resources. So I
[35:35] tend to do this a lot whenever I have
[35:37] tool calls or or building out tools for
[35:39] working with language models ensuring
[35:41] that the information that I'm returning
[35:43] or providing as part of the context is
[35:46] entirely relevant to the generation or
[35:50] to to the task at hand we should
[35:53] say. Cool. So that's our search web
[35:56] function. And now if we go back to again
[36:00] our we can think of this a bit like a
[36:02] checklist. The next thing that we're
[36:03] going to have to do is analyze the
[36:05] results um the search results for
[36:08] learnings and follow-up questions. Now
[36:10] this is going to be the most complicated
[36:12] part of the entire workflow. And this is
[36:14] also going to be the agentic part of the
[36:16] workflow. And so what we're going to do
[36:18] is we're going to use generate text as
[36:20] we did before giving it two tools. We're
[36:22] going to have a tool for searching the
[36:24] web and then we're going to have a tool
[36:26] for evaluating the relevance of that
[36:28] tool call. And this is kind of I I say
[36:32] this is the most interesting and equally
[36:35] also the the agentic part um because
[36:38] it's going to continue doing that flow
[36:41] for as long as it takes to get a a
[36:43] relevant search result. So let's see how
[36:46] we can implement this. I'm going to copy
[36:49] over this code and bear with me because
[36:51] there's a lot there's a a decent amount
[36:54] of code here. Uh but we'll walk through
[36:56] all of it and see how it works. So I'm
[36:59] going to also uh make sure that we've
[37:01] got our imports all good. I'm going to
[37:04] close off uh some of our tools and now
[37:08] we're ready to go. So this function is
[37:10] called search and process. It is going
[37:12] to search and process. It's going to
[37:14] take in our query. Again remember search
[37:17] the web for a relevant result and
[37:19] analyze uh search the web for map
[37:22] through each query and search the web
[37:23] for a relevant result. So we're taking
[37:25] in that query. Uh we're going to take
[37:28] we're going to create two local
[37:29] variables for this for this function uh
[37:32] pending search results. And if you can
[37:34] think about it like this process of
[37:37] searching the web and trying to figure
[37:38] out if it's relevant when you search the
[37:40] web you're going to add that result to
[37:41] the pending search results array. And
[37:44] then for evaluate, you're going to pull
[37:46] out whatever the most recent uh pending
[37:49] result is. Check if it's relevant. If it
[37:51] is, pop it into the final search results
[37:54] array. If it's not, just discard it. Um,
[37:57] so that's the rough flow that we're
[37:58] going to be building here. We use our
[38:00] main model as the model here. Our prompt
[38:03] is very complicated. Search the web for
[38:06] information about our query. Uh, we give
[38:08] it a system prompt. You are a
[38:10] researcher. For each query, search the
[38:12] web and then evaluate if the results are
[38:15] relevant and will help answer the
[38:17] following query. We then pass in the
[38:22] query which is right here. I was looking
[38:25] for it below. It's right above. Um, we
[38:27] set our max steps. So, we want this
[38:29] agentic loop to run up to five times.
[38:33] You could set this higher and we can set
[38:35] this higher for now. Um, and that will
[38:37] just allow that process of finding a
[38:39] relevant link to continue onwards and
[38:42] onwards. I like to keep these relatively
[38:44] low just to ensure that it doesn't go
[38:46] off the deep end, but experiment
[38:49] experiment experiment is my like main
[38:51] advice for building with with these
[38:54] tools. Our first tool that we have here,
[38:57] I'm saying tool a lot, uh, is the search
[38:59] web. This searches the web for
[39:00] information about a given query. We take
[39:02] in a query which is a string. uh our
[39:05] string uh we then pass into the search
[39:08] web function that we just created
[39:09] earlier. Uh we get back some search
[39:11] results that type we declared uh at the
[39:14] beginning which I can show you here this
[39:17] type right there. Um, and then finally,
[39:21] as I was saying, we we take this local
[39:24] variable, this pending search results,
[39:26] and we push whatever these new uh
[39:30] searched web results that we get, and we
[39:32] also add those to the uh conversation
[39:35] context by returning them from the tool.
[39:38] And then we have the evaluate tool. And
[39:41] this is to evaluate the search results.
[39:42] It doesn't take in any parameters. Um
[39:45] and in the execute function we are going
[39:48] to pull out the latest pending result.
[39:50] Uh then run it through generate object
[39:52] asking it to evaluate whether the search
[39:54] results are relevant and will help
[39:56] answer the following query. Uh and then
[39:59] we pass in with this XML syntax our
[40:02] stringified pending
[40:04] result. Now uh the final thing here with
[40:08] this generate object rather than
[40:09] specifying the schema with zod because
[40:12] we just want to know whether it's
[40:13] relevant or irrelevant we can actually
[40:15] use generate objects enum mode to
[40:18] specify just the two values that we
[40:20] need. Something's either going to be
[40:21] relevant or irrelevant. Uh this is super
[40:25] ergonomic. You could use zod here. I
[40:27] just find this very easy particularly if
[40:28] you have just two values. Um and it's
[40:31] also easier for the language model when
[40:33] it's literally restricted to two model
[40:35] to two values rather than generating a
[40:37] full structured
[40:39] object. Uh then if the evaluation is
[40:42] relevant uh we will push the pending
[40:45] result to the final result because we
[40:48] know that it's now relevant. So that's
[40:50] going to be a good sorts that we want to
[40:51] keep. Uh we have some logs here. And
[40:54] then this is interesting here. We say if
[40:56] the evaluation is irrelevant, we return
[40:59] the following string from this tool
[41:01] call. Search results are irrelevant,
[41:03] please search again with a more specific
[41:05] query. So when max steps triggers the
[41:09] next generation, the language model is
[41:11] going to see the most recent step that
[41:13] took and the last part of that most
[41:15] recent step i.e. the tool result was
[41:17] please search again with a more specific
[41:20] query. So we have this system that is
[41:22] repeating um but with feedback based on
[41:26] what's going on. The last thing to
[41:28] mention here is the fact that I did not
[41:30] use the parameters here to parse out the
[41:33] search result. And uh there's a very uh
[41:36] specific reason for doing that. Search
[41:39] result can be super long, right? This
[41:41] could be a whole entire crawled web page
[41:43] that could be I don't know 10,000
[41:45] tokens. And we don't want the model to
[41:47] have to actually parse that out. It's
[41:50] literally generating the text that
[41:52] already exists in the context above.
[41:56] One, costs money. Two, it takes a long
[41:59] time. Three, it's probably errorprone
[42:01] because it's literally just writing out
[42:03] stuff that's above. It's not referencing
[42:05] it. And that's why I like to do this um
[42:09] these local variables within this
[42:11] function faster, cheaper, more accurate,
[42:14] and so on. So this is the search and
[42:17] process function and we can add it to
[42:20] our main function and see how it works.
[42:25] So we're going to
[42:27] console.log our search results and see
[42:30] see what we got. So we'll clear this
[42:33] out, run the function
[42:35] again. Searching the web for
[42:37] requirements to become a D1 shotput
[42:39] athlete.
[42:41] Found throws university benchmark lifts
[42:44] to throw 50 ft from school shotput.
[42:48] Evaluation completed. It's
[42:52] irrelevant. So it found a new
[42:55] one. Considered it irrelevant.
[43:06] found another one men's track recruiting
[43:08] standards and considered that irrelevant
[43:10] or considered that relevant sorry and
[43:12] then it returned a bunch of oh boy we
[43:16] returned the whole result. So this is
[43:17] like the whole scraped uh web page in
[43:20] here. So we can see very cool it is
[43:23] working great. So let's move on to the
[43:27] next step. And what is the next step? Uh
[43:29] the next step is to analyze the results
[43:32] for learnings and follow-up questions.
[43:36] So to do this, we're going to again
[43:39] create a new function. This new function
[43:41] is going to be called generate
[43:42] learnings. It's going to take in a query
[43:45] which is a string and then uh the search
[43:48] result itself. So this is like the the
[43:50] web page in the scripted content. We're
[43:52] then going to use uh surprise surprise
[43:55] my favorite function generate object
[43:57] using our main model again and providing
[44:00] a prompt here. This time the user is
[44:01] researching query. the following search
[44:03] results were deemed relevant. Generate a
[44:06] learning and a follow-up question from
[44:08] the following search result. We use
[44:10] those XML tags again to nest in our
[44:13] search result that is stringified. And
[44:15] then finally, we specify as our schema
[44:17] we want uh a a string which is the
[44:20] learning itself, the insight we could
[44:22] probably call it. and then uh any
[44:24] follow-up questions which are an array
[44:26] of strings and we return that object
[44:29] which is this type safe uh structured
[44:33] output. Cool. So we can incorporate that
[44:36] into our main function again. Let's
[44:39] replace all of that. And we can see now
[44:42] that we are we have our prompt, we have
[44:44] our queries. We we for each query we're
[44:48] going to search the web search and
[44:50] process. So we're searching and making
[44:52] sure that the the result is relevant.
[44:54] And then for each of the results that
[44:56] are returned, we're then going to pass
[44:57] it to our generate learnings function,
[44:59] passing in that original query and then
[45:02] the um the search result. So we could
[45:06] again test to see how things are
[45:10] looking. Run the
[45:12] script. Searching the web for
[45:14] requirements to become a D1 shop.
[45:16] athlete. Let's see how many times uh I
[45:18] have said that in um in this
[45:24] video. So, it's deemed that this is
[45:26] irrelevant, but the next link that it
[45:28] finds is relevant. So, it's now
[45:30] processing this search result and then
[45:33] we're going to get a learning. So, what
[45:34] do we have here? To become a D1 shop at
[45:37] athlete, high school athletes typically
[45:38] need to have four years of varsity
[45:40] experience, achieve highstate finishes
[45:42] or be state champions, and participate
[45:44] in national events like USATF National
[45:47] Junior Olympic Outdoor Track and Field
[45:50] Championships. They should also aim for
[45:52] shot put distance of around I think
[45:54] that's 60 feet um for tier one recruits.
[45:58] Um and then we've got some follow-up
[45:59] questions. What are the specific
[46:01] training regimens for shot put athletes?
[46:03] How do division one recruiting standards
[46:05] differ from division two and three? Some
[46:07] like really interesting threads to to go
[46:11] down. So, what we're going to have to do
[46:13] naturally now is introduce recursion to
[46:16] this whole process. Meaning now that we
[46:18] have our learnings, we effectively want
[46:20] to take the follow-up questions, create
[46:22] a new query, and call the entire process
[46:25] again until uh effectively we we are
[46:30] happy with the the depth of information
[46:33] that we've gathered. So there are going
[46:35] to be a few things that we need to do.
[46:36] One, we need to probably create a new
[46:38] function that can handle this recursion
[46:41] rather than doing it all in the main
[46:42] function.
[46:44] two, we're going to have to we're not
[46:47] going to be able to track all of our uh
[46:50] accumulated research in in the local
[46:53] function anymore. We're going to have to
[46:54] create some state or a variable outside
[46:57] in in the global state to be able to
[46:59] track this as we go through. And then
[47:01] we're probably going to need some types
[47:02] as well just to help make this all a bit
[47:05] easier. So, let's add those. Now, first
[47:07] things first, we're going to create a
[47:10] new function uh called uh deep research
[47:14] to um to actually that will be able to
[47:17] handle our recursion. So all we've done
[47:19] here is taken our previous logic that
[47:21] was within the main function and put it
[47:23] into a new function called deep
[47:25] research. Um so as you can see we we're
[47:28] generating search queries, we are then
[47:31] searching and process then we're
[47:33] generating learning. So, same as before.
[47:35] And then in our main function, this time
[47:36] we define our prompt and then we um call
[47:40] that deep research function. So, what
[47:43] we're going to have to do now is
[47:44] actually call this function recursively.
[47:47] But first things first, we're going to
[47:49] need to create
[47:52] uh a place to store our accumulated
[47:54] research
[47:57] state. So, I'm going to copy in some
[47:59] code here. Uh we're defining two types.
[48:02] Uh a learning type which we've seen
[48:03] before. This was the the the learning
[48:06] the insight from the research and then
[48:08] follow-up questions. Um and then
[48:10] research. This is the core accumulated
[48:12] research object um or store um and we
[48:16] store in like our original query, the
[48:18] queries that have been performed um or
[48:21] the queries the active queries right now
[48:24] the search results and accumulation of
[48:26] all of them uh learnings all the
[48:28] insights and then completed queries. And
[48:31] at the very end, as this develops, we're
[48:33] going to pass all of that state, that
[48:36] store of information to one large model
[48:39] that can synthesize all of that and
[48:40] generate our report. But first, we need
[48:43] to update our deep research function to
[48:45] actually update the store as it's
[48:48] iterating through these levels of
[48:51] recursion. So, let's head to our deep
[48:54] research function. I'm going to copy all
[48:56] of this and we'll look at what we've
[48:58] updated here. So the first thing that
[49:00] we've done um is we we've changed the
[49:03] name of one uh parameter from query to
[49:06] prompt just so you know uh we've also
[49:09] updated our depth and breadth uh
[49:11] numbers. So depth remember are the
[49:13] levels deep that we go into the the the
[49:15] the strands that will or the levels of
[49:18] the strands that will go down and then
[49:20] breadth are those like individual forks
[49:23] how many of them will go down at each
[49:25] level. So we first check to see if a
[49:27] query is undefined. That will be on the
[49:30] first time we're ever running this. Um
[49:32] and if it is, we'll set it to the the
[49:35] prompt. We then like last time we
[49:37] generate the search queries. This time
[49:39] we update our queries to be that that uh
[49:42] whatever is returned from the search
[49:44] queries. Um and that's a theme as we go
[49:46] through here. We're going to update our
[49:48] accumulated research to take in our our
[49:50] search results, our learnings, and our
[49:52] completed queries. And now that we have
[49:54] this all out of the way, we can actually
[49:56] call deep research recursively. Um, and
[49:59] at the same time, we're going to
[50:01] decrement the depth and breadth so that
[50:03] we can eventually get to a resolution.
[50:06] Uh, so this doesn't run forever and we
[50:08] don't run out of all of our API credits
[50:10] and leave the user waiting for for way
[50:13] too long. So, let's add that final
[50:16] recursion. I'm going to replace the
[50:19] entire function again um just so I don't
[50:22] make any mistakes here. We've added two
[50:24] things here. First, we've said uh if the
[50:26] depth is is zero, uh just return
[50:29] effectively like recursion is done at
[50:31] this point uh return the accumulated
[50:34] research. Um and now for the new stuff
[50:38] where before we had the comments saying
[50:40] perform the deep research now instead we
[50:43] create a new query saying the overall
[50:45] research goal is this. These are the
[50:47] previous search queries that have been
[50:49] performed. Here are some follow-up
[50:51] questions. Um and then we pass that back
[50:55] and call the entire function again with
[50:57] that new prompt. uh again decrementing
[51:00] the depth and the breadth at a more
[51:03] exponential
[51:07] rate. So I think that's a good as good a
[51:11] time as any to to run the function again
[51:14] and and kind of see what's happening. We
[51:16] should see it now going into various
[51:18] levels of depth. Again I'm saying
[51:21] requirements to become a D1 shotput
[51:23] athlete. So this uh source is deemed
[51:27] irrelevant. It keeps liking to use that
[51:31] one. Instead, the track recruiting
[51:34] standards is deemed relevant. We're now
[51:36] processing the search result. We're
[51:37] going to be generating some
[51:40] learnings. We're now searching the web
[51:42] for what physical and technical skills
[51:44] are essential for a D1 shot athlete. So,
[51:46] we're going a level of depth
[51:48] here. We found uh some some relevant
[51:55] Now we're searching again training and
[51:57] skills needed for D1 shotput
[51:59] athletes and so on and so forth. So we
[52:02] can see that it is indeed working.
[52:09] One thing though that we haven't done
[52:11] yet is that we haven't incorporated into
[52:14] and funny enough we didn't see this in
[52:16] this example but the way that our logic
[52:19] works right now when the model is trying
[52:22] to decide whether a link is relevant it
[52:24] doesn't have context as to the links
[52:26] that have already been used in other
[52:28] steps and naturally we've been talking
[52:30] about context length price speed we
[52:34] don't we we surely do not want to
[52:37] provide the same source course twice,
[52:39] particularly if it's taking up 10 20,000
[52:42] tokens in length. So what we're going to
[52:44] do is we're going to go to our search
[52:47] and process function. We're going to
[52:50] head into our evaluate tool and in this
[52:52] evaluate tool, we're also going to pass
[52:54] in previously used search results. And
[52:57] if the search result exists in that
[53:00] previously used search results, we're
[53:02] going to say that's an irrelevant source
[53:04] and and try again.
[53:07] So I'm going to copy the entire
[53:10] function, replace the entire function
[53:12] here. Um, this time we're taking in a
[53:15] new parameter here, accumulated sources.
[53:18] Um, and if we scroll down, we should see
[53:20] our updated prompt. We say if the page
[53:23] already exists in the existing results,
[53:25] mark it as irrelevant. And we can see
[53:27] we're passing it in in XML tags existing
[53:30] results and stringifying through passing
[53:33] just the URL because also we don't need
[53:35] all the content from the page here. We
[53:37] literally just need the URL. We have one
[53:40] error here and that's because we added a
[53:42] new argument but we haven't passed it in
[53:44] here. So I'm going to just pass that in
[53:47] here. Uh this will be the accumulated
[53:49] research dot um I think this is the
[53:55] search results. Yeah, search results.
[54:00] Perfect. Uh, so if we were to to run
[54:03] this again, what we would see, we didn't
[54:05] see it in the previous example before,
[54:07] but if it reused a source or if Exa
[54:11] returned a source that it had already
[54:14] used in a previous step, that would now
[54:16] be marked as irrelevant and that agentic
[54:18] process would continue on in a loop. The
[54:21] last thing that we're going to want to
[54:22] do, which I actually don't have in in
[54:25] this process, is that now that we have
[54:26] all this accumulated research, we want
[54:28] to give it to a big model, I I prefer a
[54:32] reasoning model in this case to
[54:34] synthesize all of this information and
[54:36] put it into a report that we can consume
[54:39] to hopefully solve our query. So, let's
[54:42] create a new function. This function is
[54:45] going to be called a very creative name
[54:47] as per usual uh generate report. It's
[54:51] going to take in that accumulated
[54:53] research which is typed as such. Um and
[54:55] then we're going to call generate texts.
[54:57] This time we're using 03 mini rather
[55:00] than our main model. Uh again play
[55:02] around with this clone this and and see
[55:04] which models uh you like best for this
[55:07] kind of thing. I found 03 mini very good
[55:09] at this. And then our prompt here, we're
[55:10] saying generate a report based on the
[55:12] following research data. We've got two
[55:14] new lines and then we stringify the
[55:16] report returning the final generated
[55:20] text. So let's actually refactor our
[55:24] main function very quickly to use this
[55:27] new
[55:29] uh this new function. So what we're
[55:31] doing here uh we've just inlined our
[55:33] prompt. So we say uh what do you need to
[55:36] to be a D1 shop athlete? We log out some
[55:39] status updates and then we pass that
[55:41] research into the generate report
[55:45] function await it and get out a report
[55:47] which will finally write to the file
[55:49] system to a markdown file. So I'm going
[55:51] to import fs from fs and then we're
[55:55] ready to go.
[55:56] So let's see let's see what this does.
[56:12] Great. So, after about a minute, we've
[56:14] got our report. Below is an integrated
[56:18] report summarizing the research findings
[56:19] on what it takes to become a division
[56:22] one shotput athlete along with a with
[56:24] related insights on technique, training,
[56:26] and common beginner pitfalls. So, okay,
[56:28] we've got our our entire report here.
[56:32] Um, and to be honest, given all of the
[56:35] information that we gave it, it's it's
[56:38] pretty it's pretty great. But one thing
[56:41] that we'll note here is that we didn't
[56:43] give the model any guidance on what
[56:45] exactly we wanted this report to look
[56:47] like. And so the model had to infer. Um,
[56:51] and when when you're working with
[56:52] language models, in order to get the
[56:54] best response, you want to leave as
[56:56] little up to the model to infer as
[57:00] possible. So, one thing, I want this to
[57:02] be in a markdown format. Two, I'd like
[57:05] it to to form a bit more of a structure
[57:08] um that I want to specify. And so, what
[57:10] we're going to do here is we're going to
[57:11] head back to our uh generate research
[57:15] function. And we're going to do two
[57:16] things. We're going to actually just one
[57:19] thing, sorry. We're going to create a
[57:22] system prompt. We're going to tell it
[57:23] give it a persona. You are an expert
[57:25] researcher. We're going to give it
[57:26] today's date. We're going to tell it to
[57:28] follow these instructions exactly. Um,
[57:31] and a few key things in here. We're
[57:32] going to say use markdown
[57:34] formatting. You may use high levels of
[57:37] speculation or prediction. Just flag it.
[57:40] Um, and and in general, we just give it
[57:43] these these uh guidelines that are very
[57:47] research uh analyst oriented. So, I'm
[57:50] going to run this entire thing again,
[57:52] and we're going to see the difference in
[57:54] the output.
[58:12] And here it is. We have our new report.
[58:14] So, let's jump into it. And what can we
[58:16] notice right off the bat? We're using
[58:18] markdown, which is awesome. Much more
[58:21] structured. Uh we can see that we've got
[58:24] date and line kind of helpful to have.
[58:26] Um but like the the level of quality of
[58:31] this kind of report even just with this
[58:33] basic workflow really astounds me. So
[58:36] you can see to be considered like right
[58:38] at the top level to be considered a
[58:40] division one shot pro prospect athletes
[58:42] are expected to demonstrate a high level
[58:44] of competitive success varsity
[58:46] experience um typically four years of
[58:48] varsity participation competitive
[58:51] exposure. Uh we have performance
[58:53] benchmarks a benchmark throw of 55 ft.
[58:56] elite or top tier recruits tend to have
[58:58] distances around 60 feet and 18 inches.
[59:00] Like this is uh and the difference
[59:03] between men's and women. It it is so so
[59:06] so cool how uh we were able to build
[59:08] this in just 218 lines of code. Um so
[59:14] yeah this is this is it. This is a
[59:16] session. I hope you enjoyed this. If you
[59:18] have any questions, you can reach me on
[59:22] um X the everything platform at niko
[59:26] albanese10. Uh feel free to send me a
[59:29] DM. Uh if you have any questions on
[59:31] building with the SDK, head to
[59:35] SDK.purcell.ai, check out our docs. We
[59:37] got some awesome uh guides in the
[59:39] cookbook as well. Um and yeah, I hope
[59:41] you enjoyed this. I want to thank Swix
[59:43] for asking me to to do this uh session
[59:47] and I really hope you enjoyed it and
[59:49] hope to see you at the next one. Take
[59:50] care.
