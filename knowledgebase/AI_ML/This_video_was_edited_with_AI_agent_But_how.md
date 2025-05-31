---
type: youtube
title: This video was edited with AI agent. But how?
author: Channel Video
video_id: r0AG44qYKsI
video_url: https://www.youtube.com/watch?v=r0AG44qYKsI
thumbnail_url: https://img.youtube.com/vi/r0AG44qYKsI/mqdefault.jpg
date_added: 2025-05-26
category: AI and Video Editing
tags: ['AI video editing', 'LLM code generation', 'browser automation', 'video processing APIs', 'AI agent architecture', 'code-based tooling', 'machine learning integration', 'web development']
entities: ['Attention is all you need', 'Haskell', "VA's Open-Source Video Editing Agent", 'FFMpeg', 'Remotion', 'Core library from Diffusion Studio', 'Playwright', 'WebCodeX API', 'Chromium Dev Tool Protocol', 'Lm.txt']
concepts: ['AI in video editing', 'LLM code generation', 'browser automation', 'API integration', 'AI agent architecture', 'tool calling in code', 'video processing pipelines', 'cross-environment file transfer', 'machine learning tooling', 'agent-based automation']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of NLP concepts', 'Familiarity with programming languages (Python/TypeScript)', 'Knowledge of video editing tools', 'Experience with API integrations', 'Understanding of AI agent architectures']
related_topics: ['AI video editing tools', 'LLM-powered automation', 'browser-based video processing', 'code generation techniques', 'AI agent development', 'multi-modal AI systems', 'cloud-based video rendering', 'machine learning toolchains']
authority_signals: ['we met with the author of the library and decided to collaborate', 'multiple research papers have shown', 'this is a first open-source video editing agent']
confidence_score: 0.85
---

# This video was edited with AI agent. But how?

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=r0AG44qYKsI)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai, video-editing, code-generation, machine-learning, javascript, typescript, ai-agent  

## Summary

# Comprehensive Summary of YouTube Video Transcript

## Overview  
This video explores the development of an AI-powered video editing agent created through a collaboration between Diffusion Studio and Rkill. The agent leverages tools like Playwright, the Core library, and large language models (LLMs) to automate video editing workflows. It emphasizes code-based interactions, browser-based rendering, and flexible deployment options for improved efficiency and customization.

---

## Key Points  
- **Problem Statement**: Existing tools like FFMpeg and Remotion had limitations in flexibility and reliability, prompting the need for a more intuitive AI-driven solution.  
- **Core Architecture**:  
  - Uses **Playwright** to launch browser sessions and interact with a custom video editing UI.  
  - Relies on the **Core library** (from Diffusion Studio) for complex video compositions via JavaScript/TypeScript.  
  - Integrates **LLMs** to generate code for video editing tasks, enabling programmatic control.  
- **Workflow**:  
  - Video editing tool generates code from user prompts.  
  - **Doc Search tool** (using RCK) retrieves context if needed.  
  - **Visual feedback tool** (inspired by GAN architectures) evaluates compositions.  
- **Remote Capabilities**:  
  - Agents can connect to remote browser sessions via **WebSocket** and utilize GPU acceleration.  
  - A **load balancer** ensures scalability.  
- **lm.txt**: A "robots.txt"-like file for agents to define constraints and guidelines.  
- **Future Plans**: Transition from Python to **TypeScript** for broader adoption, aligning with the adage: *"Any application that can be written in TypeScript will be written in TypeScript."*  

---

## Important Quotes/Insights  
- *"Code is the best possible way to express actions performed by a computer."*  
- *"Multiple research papers have shown that having LLM tool calling in code is much better than in JSON."*  
- *"The first version of the agent is in Python, but a TypeScript implementation is underway."*  

---

## Actionable Items  
- **Adopt Playwright and Core Library**: For browser-based video editing with programmatic control.  
- **Leverage LLM Code Generation**: Use LLMs to write code for video editing tasks instead of relying on JSON-based APIs.  
- **Implement lm.txt**: Define agent-specific rules and constraints for ethical or operational guidance.  
- **Enable Remote Browser Sessions**: Use WebSocket for scalable, GPU-accelerated rendering.  
- **Transition to TypeScript**: For improved maintainability and developer experience.  

--- 

This summary captures the technical depth and practical applications of the AI video editing agent discussed in the video.

## Full Transcript

[00:07] [Music]
[00:30] today we're tackling a paper that's
[00:32] basically legendary at least in the
[00:34] world of natural language processing NLP
[00:37] for those in the know right attention is
[00:39] all you need it's not just a catchy
[00:41] title definitely
[00:42] [Music]
[00:50] not o cam a general purpose functional
[00:53] programming language that is also an
[00:55] imperative language and also an
[00:57] objectoriented language it is what
[00:58] hascal which is could
[01:00] [Music]
[01:03] be hey everyone my name is Mam and I'm
[01:06] excited to talk about the va's first
[01:08] open-source video editing
[01:12] agent backstory is that we needed some
[01:14] automatic tool to edit videos for res
[01:17] skill. a platform for personalized
[01:19] learning while doing so we quickly
[01:22] realized limitations of FFM p and
[01:25] started looking for more intuitive and
[01:26] flexible Alternatives remotion was nice
[01:30] but it did unreliable service side
[01:32] rendering after trying out core we
[01:35] really likeed the API as it did not
[01:37] require the separate rendering backend
[01:40] we met with the author of the library
[01:42] and decided to collaborate and build
[01:44] this agent
[01:46] together the core library from diffusion
[01:49] Studio can do complex compositions via
[01:52] JavaScript typescript based programmatic
[01:54] interface meaning we can use llm to
[01:57] generate code to run this
[02:00] and if we take a step further and let
[02:02] our llm write its own action in code
[02:05] it's a perfect match simply because code
[02:08] is the best possible way to express
[02:11] actions performed by a
[02:13] computer lastly multiple research papers
[02:16] have shown that having llm tool calling
[02:19] in code is much better than in
[02:24] Json now let's take a look at current
[02:27] architecture agent starts a browser
[02:30] session using
[02:32] playright and connects to operator UI
[02:35] this web app is video editing UI
[02:38] designed specifically for AI agents it
[02:42] renders video directly in browser using
[02:44] web codex
[02:46] API it also has helper
[02:49] functions for transferring files from
[02:52] python to browser and back via chromium
[02:54] Dev tool protocol
[03:00] this is a typical flow of agent we have
[03:02] three main tools video editing tool doc
[03:04] Search tool and visual feedback tool
[03:08] first a video editing tool generates
[03:11] code based on user prompt and runs it in
[03:14] browser if additional context is needed
[03:17] doc Search tool uses rck to pull the
[03:20] relevant
[03:21] information after each execution step a
[03:25] composition the compositions are sampled
[03:27] currently at one frame per second and
[03:30] they they are fed to visual feedback
[03:33] tool visual feedback tool can be sold as
[03:37] uh generator and discriminator like in
[03:40] famous gun
[03:42] architecture after the visual feedback
[03:44] tool gives green light the agent
[03:47] proceeds to render the
[03:51] composition we also shipped lm. txt
[03:55] which is essentially robots.txt but for
[03:58] agents you can see sample in the screen
[04:00] lm. txt in addition with specific
[04:03] template prompts will take you far in
[04:06] your video editing
[04:11] Journey while while you can bring your
[04:14] own browser and run the agent the
[04:17] current setup is also flexible enough to
[04:20] let the agent connect to a remote
[04:22] browser session via web soet and each
[04:25] agent can get the separate browser
[04:27] session which is GP view accelerated and
[04:31] of course there's a load balance load
[04:33] balancer behind
[04:37] this of course the first version of the
[04:40] agent is in Python but typescript
[04:43] implementation is
[04:45] underway as the F famous saying goes any
[04:49] applications that can be written in
[04:50] typescript will be written in
[04:53] typescript thank you very much this was
[04:56] collaboration between diffusion studio
[04:58] and rkill
