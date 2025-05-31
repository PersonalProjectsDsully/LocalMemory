---
type: youtube
title: OpenLLMetry is all you need
author: Channel Video
video_id: KVgbERRPU4M
video_url: https://www.youtube.com/watch?v=KVgbERRPU4M
thumbnail_url: https://img.youtube.com/vi/KVgbERRPU4M/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['OpenTelemetry', 'Observability', 'AI Frameworks', 'LLM Integration', 'Vector Databases', 'Open Source', 'DataDog', 'Grafana', 'Sentry', 'DinoTrace', 'Instrumentation', 'GenTech']
entities: ['Open Telemetry', 'Open Elemetry', 'Pine Con', 'Chroma', 'Data Dog', 'Sentry', 'Grafana Tempo', 'Dino Trace', 'L chain', 'Lama index']
concepts: ['Observability', 'Instrumentation', 'Standard Protocol', 'Open Source', 'Integration', 'Logs', 'Metrics', 'Traces', 'Gen Frameworks', 'Foundation Models']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of Open Telemetry', 'Familiarity with Gen frameworks', 'Knowledge of observability concepts']
related_topics: ['Observability in AI', 'Open Source Observability Tools', 'AI Frameworks', 'Vector Databases', 'LLM Integration', 'Data Privacy', 'Cloud Monitoring']
authority_signals: ['"we\'ve worked a lot on building instrumentations with our community"', '"you can easily switch between platforms"']
confidence_score: 0.8
---

# OpenLLMetry is all you need

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=KVgbERRPU4M)  
**Published**: 3 months ago  
**Category**: DevOps  
**Tags**: open-telemetry, cloud-observability, devops, logging, metrics, traces, observability  

## Summary

```markdown
# Summary of "OpenLLMetry is all you need" Video

## Overview
The video introduces **OpenLLMetry**, an open-source project built on **OpenTelemetry**, designed to provide observability for generative AI (Gen AI) applications. It extends OpenTelemetry's capabilities to support frameworks, foundation models, and vector databases, enabling seamless integration with any observability platform.

---

## Key Points
- **OpenTelemetry** is a framework for cloud observability, offering:
  - **Logging**: Capturing system and application events.
  - **Metrics**: Real-time performance data (e.g., latency, error rates).
  - **Traces**: End-to-end request tracking across distributed systems.
- **Ecosystem Components**:
  - **SDKs**: Libraries for instrumenting code.
  - **Instrumentations**: Pre-built modules that automatically collect data (e.g., for Pinecone, LangChain).
  - **Collectors**: Self-deployable components for preprocessing data (e.g., filtering, anonymization).
- **OpenLLMetry Extensions**:
  - Supports **40+ providers**, including foundation models (e.g., OpenAI, Gemini), vector databases (e.g., Pinecone, Chroma), and frameworks (e.g., Llama Index, Hugging Face).
  - Enables automatic collection of logs, metrics, and traces for Gen AI workflows.
  - Ensures platform flexibility: Data can be sent to any observability tool (e.g., DataDog, Grafana Tempo).

---

## Key Quotes/Insights
- "OpenLLMetry allows you to use any observability platform without being tied to a specific one."
- "Instrumentations automatically emit data, making it 'magic' for developers."
- Example: Pinecone instrumentation tracks queries, indexing, and vector distances/scores in standard OpenTelemetry format.

---

## Actionable Items
1. **Adopt OpenLLMetry** for Gen AI applications to gain observability across frameworks and models.
2. **Leverage existing instrumentations** (e.g., for Pinecone, LangChain) to automatically collect data.
3. **Use collectors** for preprocessing (e.g., anonymizing PII, filtering data) before sending to observability platforms.
4. **Switch platforms effortlessly** by configuring OpenLLMetry, as it uses a standard protocol.
```

## Full Transcript

[00:01] hey everyone I'm near the CEO of Trace
[00:03] Loop and today I'm going to talk to you
[00:04] a bit about open elemetry which is a
[00:07] nice open source project we'
[00:08] built you can probably hear from the
[00:11] name open elemetry that it originates in
[00:13] another project called open Telemetry
[00:15] and in case you're not familiar with
[00:17] open Telemetry I'm going to spend the
[00:18] next couple of minutes explaining to you
[00:20] what open Telemetry is so you know we're
[00:23] not talking about gen yet we're not
[00:25] talking about llms just plain simple
[00:28] cloud observability open Telemetry is an
[00:31] open source project it's maintained by
[00:33] the cncf it's one of the largest
[00:35] projects out there after
[00:37] kubernetes uh that is maintained by the
[00:40] cncf and it standardizes a way to do
[00:43] cloud
[00:45] observability in your you know Cloud
[00:48] environment currently it's supported by
[00:50] every major avability platform from
[00:52] Spang data dog din Trace new grafana
[00:54] honeycom and many many others so if
[00:57] you're using open Telemetry you can use
[00:59] it in conjunction with any of these
[01:01] platforms pretty
[01:03] easily but what is open Telemetry
[01:05] exactly open Telemetry is a protocol
[01:08] first and foremost that H standardizes
[01:11] the way to do logging metrics and traces
[01:14] H in your uh Cloud
[01:16] application logging I think I don't need
[01:19] to explain to you what is what is
[01:20] logging exactly H because if you've ever
[01:23] written some python you know script and
[01:25] you you've written print then then
[01:27] you've done some logging so logging is
[01:29] an arbitrary event you can send uh
[01:32] anytime you want H in the life cycle
[01:34] lifetime of your application and it just
[01:37] emitted as is and you can view it later
[01:40] on possibly with some
[01:42] metata metrics on the other hand is
[01:44] completely different metric is something
[01:46] you want to see on an aggregate level
[01:47] you want to see how it behaves across
[01:49] days or across users or you know
[01:52] whatever you want and when we're
[01:54] thinking about metrics in the
[01:56] traditional Cloud world we are probably
[01:58] talking about CPU us usage a memory
[02:01] usage or um latency and if you want to
[02:05] you know talk a bit about gen if you're
[02:08] thinking about which metrics we want to
[02:10] see when we are building a gen based
[02:13] applications it's probably things like
[02:14] token usage latency error rate and so
[02:18] on lastly open Tel defines tracing
[02:21] actually this was the first thing that
[02:23] was defined uh with open Telemetry but H
[02:27] it's the I would say the least trivial
[02:29] one
[02:31] so tracing is basically tracking of a
[02:33] multi-step process so again thinking
[02:35] about you know Cloud environments you
[02:37] have microservices they're talking to
[02:38] each other and you want to see some
[02:40] process that spans across multiple
[02:42] microservices you want to use a trace
[02:44] for that and then you can see you know
[02:46] how a certain request coming from the
[02:48] user is processed across these uh
[02:52] microservices H specifically for Gen I
[02:55] think tracing is actually pretty common
[02:57] because we have we are using you know a
[02:59] lot of multi mstep processes whether
[03:01] it's chains or
[03:03] workflows or even you know agents are
[03:06] multi-step processes that me that
[03:09] interact and run
[03:12] tools so yeah logging metrics and traces
[03:15] this is what open Telemetry as a
[03:17] protocol
[03:19] defined but it doesn't stop there
[03:21] because you know what can you do with a
[03:23] protocol so open Telemetry is also an
[03:25] ecosystem and it contains h sdks
[03:28] instrumentations lectors sdks are the
[03:32] way you can you know manually send out
[03:35] these logs metrics and traces from your
[03:37] application it open Telemetry currently
[03:40] has 11 different languages uh supported
[03:43] in 11 different languages of sdks from
[03:47] python typescript go C++ and many others
[03:51] you know every language you're probably
[03:52] using has an open Telemetry
[03:55] SDK instrumentations are a way to do
[03:58] this automatically so remember if you're
[04:00] using an SDK and you you want to send
[04:03] out logs metric and traces you need to
[04:04] do it manually you need to actually send
[04:06] out a log or a Met a trace or a span or
[04:10] a metric but instrumentations can do it
[04:13] automatically and we going we're going
[04:14] to talk about it in a bit and lastly
[04:17] collectors allow you to do some
[04:18] processing to your observability data
[04:21] before you send it out to whatever a
[04:24] observability platform you're
[04:27] using so what are instrumentations
[04:30] instrumentations are a way as I said to
[04:32] automatically get some observability
[04:35] data some visibility into some part of
[04:38] your application let's say you have
[04:40] you're using a an SQL Server then you
[04:43] can use an instrumentation for that SQL
[04:46] Server Like postgress and get some uh
[04:50] logs metrics and traces
[04:52] automatically uh the way these
[04:54] instrumentations work is that they
[04:55] monkey patch the client library that
[04:57] you're using within your application and
[04:59] then emit all the data that is that that
[05:02] you want to probably want to see in your
[05:04] uh in your observability platform
[05:07] everything happens on the application
[05:09] side and they're designed H magnificant
[05:13] you know engineering level so that the
[05:16] latency impact is almost negligible and
[05:20] you get a you know a nice view of
[05:21] everything that's happening in your
[05:22] system without doing
[05:25] anything collectors are a self-
[05:29] Deployable
[05:30] components you can deploy in your own
[05:32] you know Cloud environment on kues or
[05:34] whatever you want and can provide you
[05:36] some pre-processing before you send data
[05:38] out to whatever you know platform you're
[05:40] using for example if you want to filter
[05:43] out some data that is not important for
[05:45] you or you want to obscure pii or
[05:47] obscure sensitive data and hide it you
[05:49] can use the collector to do it and and
[05:52] those you know ready made components
[05:54] that you can just deploy and they're
[05:55] completely open source have a lot of
[05:57] these uh features just built in and
[06:00] lastly if you also want to send this out
[06:02] send the you know the observability data
[06:04] out to multiple providers you can also
[06:05] do it with the
[06:07] collector I think at this point you're
[06:09] probably asking me hey near you you
[06:11] talked a lot about open Tel but we are
[06:13] in a gen conference what what does that
[06:15] has to do with with
[06:16] Gen this is where open elemetry comes in
[06:20] we took this Amazing Project called open
[06:23] Telemetry and extended it to support a
[06:25] lot of you know gen uh Frameworks a
[06:29] foundation models and Vector databases
[06:32] that some of you know you can see some
[06:34] of the logos that of the
[06:36] instrumentations we built here so we
[06:37] extendedly to support all of these you
[06:39] know amazing products and because we
[06:42] relying on open Telemetry you can then
[06:44] get observability in whatever platform
[06:47] you're using you want you want to see
[06:48] you know traces within data dog just use
[06:50] open Elementary you want to see them in
[06:52] Sentry you want to see them in grafana
[06:54] Tempo or in Dino Trace just you know
[06:56] just use open Elementry configure it
[06:58] correctly and that's it you get logs
[07:01] metrics and traces automatically in your
[07:03] favorite platform it's kind of
[07:06] nice um we've worked we've worked a lot
[07:09] on on on building instrumentations with
[07:10] our community and now we have more than
[07:12] 40 different providers so we're talking
[07:16] about Foundation models like open AI
[07:17] entropic coher Gemini bedrock and many
[07:20] others H we're also talking about Vex
[07:23] databases like Pine con chroma and many
[07:25] others and we're also we also have a
[07:28] support for Frameworks like L chain Lama
[07:29] index crew Ai and hstack so you have you
[07:34] know the instrumentations that
[07:36] automatically emit logs metrix and
[07:38] traces and then just connect it to
[07:40] whatever platform you want and you get
[07:41] it out of the
[07:43] box and remember because these are
[07:45] instrumentations it's it's kind of done
[07:47] automatically so uh it's it's pretty
[07:50] cool it's like a
[07:52] magic just just to give you an example
[07:54] what what is what an instrumentation for
[07:56] let's say pinec con would look like so
[07:58] uh if the the pine con instrumentation
[08:01] will contain you know ways to see the
[08:04] queries going out to Pine con see
[08:07] indexing happening within Pine con and
[08:10] also in and also ability to investigate
[08:13] vectors return from Pine con so you want
[08:15] to see you know the data the distances
[08:18] the vector distances that Pine returned
[08:20] or H scores latencies all of these are
[08:23] available in the standard open
[08:25] Elementary
[08:27] format so open El it's it's a great you
[08:31] know way to to connect uh llm based
[08:35] applications to whatever platform you're
[08:38] currently using and because it's a
[08:41] standard protocol you you're never tied
[08:43] to a specific platform you can easily
[08:44] switch between platforms is just a
[08:47] matter of you know a configuration
[08:48] change H because all of the platforms
[08:51] that support open Telemetry H supported
[08:53] with the same with the exact same
[08:56] format H that's it if you have any
[08:58] questions uh I'm available I will be in
[09:01] the conference I'm available in the
[09:02] conference or otherwise at near at
[09:05] tr.com thank you very much
