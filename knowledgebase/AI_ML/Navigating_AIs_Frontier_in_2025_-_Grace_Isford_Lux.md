---
type: youtube
title: Navigating AI’s Frontier in 2025 - Grace Isford, Lux Capital
author: AI Engineer
video_id: HS5a8VIKsvA
video_url: https://www.youtube.com/watch?v=HS5a8VIKsvA
thumbnail_url: https://img.youtube.com/vi/HS5a8VIKsvA/mqdefault.jpg
date_added: 2025-05-26
category: AI Challenges in Practical Applications
tags: ['AI agents', 'flight booking', 'error types', 'AI challenges', 'integration issues', 'user preferences', 'travel technology', 'AI limitations', 'decision-making errors', 'software development challenges']
entities: ['OpenAI', 'Kayak', 'Skyscanner', 'United Airlines', 'JetBlue', 'American Airlines', 'San Francisco', 'JFK', 'Boeing 737 Max']
concepts: ['AI agent capabilities', 'flight booking complexities', 'decision errors', 'implementation errors', 'heuristic errors', 'taste errors', 'cumulative errors', 'AI hallucinations', 'integration challenges', 'personal preferences in AI']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI systems', 'Familiarity with flight booking processes', 'Knowledge of API integrations']
related_topics: ['AI error handling', 'User experience design', 'Integration challenges in software', 'AI ethics in travel industry', 'Flight data analysis', 'Natural language processing applications']
authority_signals: ["I think we so often talk about hallucinations and fabrications and AI models kind of going sideways we don't talk enough about these tiny cumulative errors that add up", 'the model could overthink or exaggerate and do a few other things as well']
confidence_score: 0.85
---

# Navigating AI’s Frontier in 2025 - Grace Isford, Lux Capital

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=HS5a8VIKsvA)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: ai frontier, machine learning, ai trends, deep learning, ai investments, artificial intelligence, ai research  

## Summary

```markdown
# Summary of "Navigating AI’s Frontier in 2025 - Grace Isford, Lux Capital"

## Overview
Grace Isford from Lux Capital discusses the rapid growth of AI in 2025, highlighting investments in frontier technologies and the challenges of realizing fully autonomous AI agents. She emphasizes the potential of AI agents but underscores current limitations, using a flight-booking example to illustrate gaps in reliability and decision-making.

## Key Points
- **Lux Capital’s Focus**: Invests in AI startups like OpenAI, Kayak, and Skyscanner, focusing on "frontier tech" with a strong presence in New York City.
- **AI Growth**: AI models are advancing exponentially, with projects like the Stargate initiative and the France AI Summit signaling global momentum.
- **AI Agents**: Defined as fully autonomous systems where LLMs direct their own actions, but current implementations face significant hurdles.
- **Challenges in AI Agents**:
  - **Decision Errors**: Choosing incorrect facts (e.g., booking a flight to the wrong destination).
  - **Implementation Errors**: Integration flaws (e.g., incorrect API access or user interface issues).
  - **Heuristic Errors**: Ignoring critical constraints (e.g., traffic patterns or user-specific preferences).
  - **Taste Errors**: Overlooking personal preferences (e.g., avoiding specific aircraft models).
  - **Token Limit Errors**: Limitations in processing due to input size constraints.

## Quotes
- **Definition of AI Agents**: "An AI agent is a fully autonomous system where LLMs direct their own actions."
- **Flight-Booking Example**: "The AI agent couldn’t avoid rush hour traffic or select the right airline, highlighting systemic flaws."
- **"Perfect Storm"**: "We’ve seen a lot of thunder and momentum, but we haven’t seen the lightning strike yet."

## Actionable Items
1. **Address Decision Errors**: Improve fact-checking and context-awareness in AI systems.
2. **Enhance Integration**: Ensure seamless access to tools (e.g., APIs, databases) without workflow disruptions.
3. **Refine Heuristics**: Incorporate domain-specific best practices (e.g., traffic patterns, user preferences).
4. **Personalize Preferences**: Allow AI agents to adapt to user-specific constraints (e.g., avoiding certain aircraft).
5. **Optimize Token Usage**: Develop strategies to handle input size limitations without compromising performance.
6. **Prioritize Autonomy**: Build systems that can autonomously resolve errors and adapt to dynamic environments.
```

## Full Transcript

[00:00] [Music]
[00:16] thank you so much Peter to swix to all
[00:19] of the AI engineer Summit for having me
[00:21] I am so thrilled to be here I'm Grace
[00:24] again a partner at Lux capital and it's
[00:26] a pleasure to really kick off this
[00:28] conference and tackle a pretty tough but
[00:31] exciting task the state of the AI
[00:33] Frontier and how we navigate that in
[00:37] 2025 so a little bit about Lux as we get
[00:39] started here right Lux likes to say we
[00:41] believe before others understand we
[00:44] invest in Frontier Tech ideas that seem
[00:47] crazy right uh and we really like to
[00:49] bring sci-fi to SCI fact in fact we've
[00:53] been lucky to partner at the earliest
[00:54] stages with some top AI companies
[00:57] hugging face I'm sure several folks know
[00:59] it the GitHub for machine learning
[01:02] together AI The open- Source AI Cloud
[01:05] physical intelligence that's like a
[01:06] robotics software brain and S AI That's
[01:10] a research lab actually in Tokyo Japan
[01:12] doing really cool evolutionary nature
[01:14] inspired algorithms they just launched a
[01:16] pretty cool AI Cuda scientist last night
[01:19] so go check it out moving a little bit
[01:21] forward as we think about New York City
[01:24] I get my clicker working
[01:27] here there we go Lu is really excited to
[01:31] double down in New York City and AI Lux
[01:34] was founded in New York City our first
[01:36] AI investment was here in 2013 and a
[01:39] majority of the Lux AI portfolio is
[01:41] actually headquartered here or as a
[01:43] major Hub as you can kind of see in the
[01:45] graph behind me it's also home to many
[01:47] of you right state-of-the-art research
[01:49] and Engineering leaders and many 4 500
[01:52] companies several of whom you're going
[01:54] to hear from over the next few days we
[01:57] are really bullish on the New York City
[01:58] opportunity and we're really excited you
[02:00] guys all came to share this opportunity
[02:02] with
[02:05] us so when I was creating this
[02:07] presentation I went back and looked at
[02:09] the last few years of AI right and all
[02:11] the way back really to stable diffusion
[02:13] August 2022 and wow I mean look at this
[02:16] hockey stick right the last two and a
[02:17] half years have been crazy the last 18
[02:20] months have been even more exponential
[02:22] the progress is getting more aggressive
[02:24] it's getting more impressive and really
[02:26] it's getting more spread right it's not
[02:28] just open Ai and anthropics publishing
[02:30] these models it's xai we just saw the
[02:32] grock launch this past week it's mistal
[02:35] it's deep seek it's many many more and
[02:37] the models are getting more performant
[02:39] they're also getting more compute
[02:43] efficient and as we zoom in to the
[02:46] current state of the world in
[02:48] 2025 it's off to an even Wilder start
[02:51] right if you thought the last few years
[02:52] were crazy 2025 is even Wilder we saw
[02:55] the 500 billion Stargate project
[02:57] announced between the US government open
[02:59] AI soft bank and Oracle we saw 03 open
[03:03] eyes 03 right before the start of the
[03:05] Year where they actually exceeded C
[03:08] performance and the arc AGI challenge we
[03:10] saw the Deep seek Mania right with deep
[03:13] seeks R1 model launching earlier this
[03:16] year sending you know Nvidia shares
[03:19] tumbling down we also saw deep SE go to
[03:21] number one uh in the app store and then
[03:24] of course just last week we saw the
[03:26] France AI Summit where macron actually
[03:28] launched a whole new AI initiative with
[03:31] France and Europe back in the
[03:34] game so you may be saying and I think a
[03:36] lot of us are thinking right this is the
[03:38] AI agent moment in 2025 and I'd go as
[03:41] far as say this is the perfect storm for
[03:44] for AI agents and frankly it's easy to
[03:47] see why right uh several reasoning
[03:49] models starting with open a eyes 01 then
[03:51] 03 deep sees R1 grock's latest reasoning
[03:54] model this past week are outperforming
[03:56] human ability and in some cases even
[03:59] having more capabilities that we've
[04:01] never even seen before we've seen the
[04:04] rise of test time compute right that's
[04:06] more compute appi at INF frence instead
[04:07] of at training that's increasing this
[04:09] model performance as well we' seen
[04:12] further engineering and harder
[04:14] optimizations right whatever you think
[04:16] it cost to actually train that deep seek
[04:18] model you cannot deny it was a feat of
[04:21] engineering and Hardware efficiency
[04:24] inference is getting cheaper Hardware is
[04:26] getting cheaper the open source close
[04:28] Source Gap is getting Clos closed
[04:30] between deep seek and llama models
[04:32] getting more and more performant and of
[04:34] course billions of infrastructure
[04:36] powering all this data center and
[04:37] compute we just talked about the US
[04:39] Stargate we talked about macron and
[04:41] Europe and also Japan with sopig and
[04:44] Nvidia has been doubling down on their
[04:46] data set of efforts so all this is
[04:48] setting this exciting groundwork for the
[04:49] aonomus name of our conference agents at
[04:52] work and it really does feel like an
[04:54] exciting
[04:56] moment but in reality these AI agents
[05:00] aren't really working just yet right
[05:02] people are saying it's a perfect storm
[05:03] and I'm seen a lot of Thunder I'm seen a
[05:05] lot of great momentum but we haven't
[05:07] seen that lightning strike uh and
[05:09] everyone I know has different definition
[05:10] of Agents so for the purposes of this
[05:12] presentation I'm going to Define my
[05:14] definition as an AI agent that is a
[05:16] fully autonomous system where llms
[05:19] direct their own
[05:22] actions so let's give a little example
[05:24] of what I mean when I say an AI agent
[05:26] isn't working just yet here's a
[05:28] seemingly simple query on open a ey
[05:30] operator I'm sure everyone here knows
[05:32] what it is I asked it to book a flight
[05:34] for me to New York to San Francisco on
[05:35] Monday I'm sure it's also a route and
[05:38] something that many people in this room
[05:39] are familiar with and in reality it's
[05:42] actually kind of a complex problem right
[05:45] I need to leave after 3 on Monday but I
[05:47] want to avoid rush hour traffic I want
[05:49] to fly United JetBlue or American to
[05:51] maximize my chance of an upgrade from
[05:53] economy I want to keep it under $500 to
[05:56] keep under my work expense policy I also
[05:59] want to aisle seat that's not too close
[06:01] to the bathroom um and I want to get
[06:03] there you know before midnight so I put
[06:06] this in to open AI
[06:07] operator and the first thing it did with
[06:10] all this information is go to kayak
[06:11] which if anyone has booked a flight
[06:13] before that's a pretty frustrating
[06:15] experience and unfortunately it did not
[06:17] find a flight uh it wasn't able um it
[06:19] couldn't find one it didn't even seem to
[06:20] look for United or American second try
[06:23] try it again uh this is Skys scanner
[06:25] this time which is slightly better um
[06:28] and it did actually find a flight but it
[06:29] found one that had a lot of traffic uh
[06:32] 5:30 JFK for those who live in New York
[06:34] that is a tough traffic time um and
[06:37] ultimately I also couldn't even pick my
[06:38] seat so didn't really work out based on
[06:40] my prompts uh
[06:42] earlier so what does this all mean right
[06:45] why these AI agents not work I think we
[06:47] so often talk about hallucinations and
[06:50] fabrications and AI models kind of going
[06:52] sideways we don't talk enough about
[06:54] these tiny cumulative errors that add up
[06:57] right uh there's a lot of little that we
[07:00] see with this old model and I'm going to
[07:02] go through a few it's not an exhaustive
[07:04] list but it's a sense of some of the
[07:05] things you might run into as you're
[07:06] building these AI agents first decision
[07:10] error it chooses the wrong fact right I
[07:13] may book a flight with AI but it may
[07:15] book it to San Francisco Peru instead of
[07:17] San Francisco
[07:18] California the model could overthink or
[07:21] exaggerate and do a few other things as
[07:23] well second implementation error the
[07:26] wrong access or integration on the prior
[07:29] slide with my Skys scanner I actually
[07:31] had to enter capture and that messed up
[07:33] a little bit of the flow you also could
[07:35] get locked out of a critical access to
[07:37] an important database and ultimately
[07:39] that AI agent isn't going to work
[07:41] anymore third heuristic error the wrong
[07:44] criteria unfortunately the model didn't
[07:47] acknowledge best practice of allowing
[07:49] enough time for JFK in fact I didn't
[07:51] even ask where I was coming from
[07:52] Manhattan Brooklyn or Beyond and that
[07:55] could really affect the traffic you're
[07:57] going to get and ultimately if I even
[07:58] make that at 5:30 p.m. and fourth taste
[08:03] error the wrong personal preferences for
[08:06] those who know me well I'm actually a
[08:07] pretty spooked flyer and I do not like
[08:09] flying Boeing 737 Maxes if AI booked
[08:12] that you know I did not put it in the
[08:13] prompt earlier but if it did book that I
[08:15] will be very unhappy and I would not get
[08:17] on that
[08:20] plane and then there's kind of a fifth
[08:22] more nebulous error right it's a little
[08:23] bit of this Perfection Paradox right we
[08:26] are doing things so magical with AI
[08:28] right now yet we're getting frustrated
[08:30] when o1 thinks too long or when operator
[08:33] moves at the speed of a
[08:35] human even if the agent gets it right on
[08:38] the first try often they're inconsistent
[08:41] and unreliable leading to really
[08:43] underwhelming our human expectations
[08:45] about the whole
[08:46] experience here's another visual of kind
[08:49] of these complex systems where each of
[08:51] these cumulative errors really compound
[08:53] right two simple agents one that's 99%
[08:56] accuracy one that's 95% accuracy to
[08:58] start pretty impressive agents at the
[09:00] beginning but over 50 consecutive steps
[09:03] you actually realize a pretty big
[09:04] disparity here there's actually a 50%
[09:07] difference after 50 tasks between the 95
[09:09] and the 99 and that 99% agents actually
[09:12] down to 60% the point here is that
[09:15] something simple like booking a flight
[09:17] is actually really complex in nature
[09:19] when all these tiny cumulative errors
[09:21] add up and they get even more Amplified
[09:23] in a complex multi-agent system with
[09:26] multi-step
[09:28] tasks so how do you as all these amazing
[09:30] VPS of AI these leaders of AI in the
[09:33] room optimize a complex agent taking
[09:36] into account all of these really
[09:38] difficult queries to consistently and
[09:40] reliably make the right
[09:43] decision the truth
[09:45] is it's
[09:48] hard but that hasn't stopped us before
[09:51] and there is hope so I thought I would
[09:53] run through some of the best practices
[09:55] that we're seeing building AI agents
[09:57] today and five strategies
[09:59] we can all think about to help mitigate
[10:01] a lot of these cumulative errors let's
[10:04] Dive In First Data curation how do we
[10:09] make sure an AI agent has the
[10:11] information it needs data is messy it's
[10:14] unstructured it's in silos it's
[10:16] everywhere it's not just web and text
[10:17] data now too it's design data it's image
[10:20] data it's video data it's audio data
[10:22] it's a data in your sensors and your
[10:23] Warehouse if you're in the manufacturing
[10:25] world it's even the agent data that your
[10:27] data your agent is producing in real
[10:29] real time think about curating
[10:32] proprietary data the data the AI agent
[10:35] generates and ultimately even the data
[10:37] you're using in your model workflow for
[10:39] Quality Control Data is your best asset
[10:42] and curation is key to making it more
[10:45] effective data also isn't static anymore
[10:49] how do you design an agent data flywheel
[10:51] from day one so every time a user uses
[10:54] the product it automatically improves in
[10:57] real time and at scale
[10:59] a simple example back to our flight
[11:01] example is getting a curated data set of
[11:03] all of Grace's travel preferences
[11:05] including the 737 Max and all my Airline
[11:08] preferences or even say we run that
[11:10] agent over time and book many flights
[11:12] how do we recycle back that content and
[11:15] adapt to my own preferences in real time
[11:19] second the importance of evals how do we
[11:22] collect and measure a model's response
[11:25] how do we choose the correct answer this
[11:28] is long but important in machine
[11:29] learning and Ai and really understanding
[11:31] what's right versus wrong you know it's
[11:33] pretty simple in verifiable domains
[11:35] where there's a clear yes or no answer
[11:39] like math like science here's actually
[11:41] the grock three benchmarks just up here
[11:43] where you saw they did all verifiable
[11:45] benchmarks in math and sciences but how
[11:47] do we set up evaluations for
[11:50] non-verifiable systems where there
[11:52] aren't clear yes or no answers like well
[11:56] Grace like this plan seat based on her
[11:58] preferences and how do we collect those
[12:00] signals
[12:01] too we also saw another examples of an
[12:03] eval debate over the weekend with deep
[12:05] research right we have an open ey deep
[12:07] research product one from perplexity one
[12:09] from Gemini as well and there are
[12:11] multiple versions of the same product
[12:13] The evals here really depend on the eye
[12:15] of the beholder right which one is
[12:17] better for everyday research versus VC
[12:19] market research versus scientific or
[12:22] academic research we have to keep an eye
[12:25] on collecting those signals we need to
[12:27] know and collect human preferences and
[12:29] we need to build evals in a way that is
[12:32] truly
[12:33] personal Sometimes the best eval is just
[12:35] trying out the agent yourself and Vibes
[12:38] based on your needs with no number or
[12:40] leaderboard telling you what to
[12:42] do third Scaffolding Systems how do we
[12:45] ensure when one error occurs it doesn't
[12:47] have a cascading effect throughout the
[12:49] organization ramp a portfolio company
[12:51] has done a great job with this and I
[12:52] know Rahul is speaking tomorrow so go
[12:54] check him out when ramp launches a new
[12:56] applied AI feature and it fails there's
[12:59] infrastructure logic to ensure that
[13:00] doesn't have a cascading effect across
[13:01] the agentic system and also across all
[13:04] of ramp production infrastructure we can
[13:06] mitigate scaffolding by building a
[13:08] complex compound system of how all these
[13:10] things work together and sometimes even
[13:12] bringing a human back in the loop for
[13:15] reasoning models get this gets even more
[13:16] interesting and important how do we
[13:18] adapt the scaffold to Stronger agents
[13:20] that self-heal and grow an agent that
[13:23] realizes they're wrong and actually
[13:24] tries to correct their own path or an
[13:27] agent that's not sure and then needs
[13:29] bring break execution to get it back on
[13:30] track back to our travel example again
[13:33] could we add a checkpoint for this AI
[13:35] agent to verify the Trine for traffic or
[13:37] maybe steer it back in the right
[13:41] direction fourth user experience or ux
[13:44] is the m that matters and that's how our
[13:47] AI agents become better co-pilots AI
[13:49] apps today are all using the same models
[13:53] Foundation models are the fastest
[13:54] depreciating asset class on the market
[13:56] right now gbt rappers are cool ux really
[14:00] does make a difference for those who
[14:02] reimagine product experiences and really
[14:04] deeply understand the user workflow and
[14:07] really promote that beautiful elegant
[14:08] human machine collaboration right here's
[14:11] a few concrete examples back to the Deep
[14:13] research right asking clarifying
[14:15] questions to make sure it fully got the
[14:17] picture of what I'm trying to accomplish
[14:20] like Wier from codium understanding the
[14:22] ux or the psyche of that developer
[14:24] really on a more fundamental level to
[14:25] predict their next step like Harvey in
[14:29] the legal World integrating seamlessly
[14:31] with the Legacy systems to really create
[14:33] real Roi for a practicing
[14:36] lawyer if you think about all the major
[14:38] AI apps today and categories like coding
[14:40] like customer support like sales these
[14:43] all are using the same models again
[14:45] right and it's truly the ux and the
[14:47] product quality that makes any one
[14:49] company stand out at Lux we're really
[14:52] excited about the new AI Frontier
[14:55] companies who have proprietary data
[14:57] sources and who know the workflow flow
[14:59] of their user really well like robotics
[15:01] like Hardware like defense and
[15:03] Manufacturing like the life sciences you
[15:06] know how do we take a company where they
[15:08] take their proprietary data source they
[15:10] know the workflow of a biologist or a
[15:11] defense contractor or a chemist and
[15:13] truly create a magical experience for
[15:16] that end
[15:18] user Fifth and finally how do we build
[15:22] multimodally you know we're not just
[15:24] multimodal anymore we're
[15:26] multimodal there's new modalities where
[15:28] we can Tru reimagine and create a 10x
[15:31] user personalized experience I am so
[15:34] sick and tired of the chatbot as an
[15:36] interface and I know there's so many
[15:37] more exciting things we can do with our
[15:40] AI agents to really make them more human
[15:43] right how do we make AI more human how
[15:45] do we add eyes and ears nose a voice
[15:49] we've seen really incredible
[15:50] improvements in voice over the last year
[15:52] it's getting pretty scary good Lux
[15:54] actually has an investment in the smell
[15:55] space called osmo that's digitizing the
[15:58] sense of smell
[15:59] and what about touch right how do we
[16:01] instill a more human feeling and sense
[16:03] of embodiment with
[16:05] robotics I'll go as far to even talk
[16:07] about memories right how do we make AI
[16:11] truly personal and know you on a much
[16:13] deeper level than it does
[16:15] today doing all of this reframes what
[16:18] Perfection is to a human and even if
[16:20] that agent is inconsistent it's
[16:21] unreliable the Visionary nature of the
[16:23] product exceeds all expectations it's
[16:25] something new and on the slide behind me
[16:28] you'll see tlop that's an amazing Lux
[16:29] portfolio company and I think they've
[16:31] done a great job really reimagining the
[16:33] visual canvas right implementing AI
[16:35] through breast Strokes they have a cool
[16:37] thing called he jaw computer where you
[16:38] can actually combine a bunch of these
[16:40] cool AI models in Tandem and not even
[16:42] know you're working with a large
[16:44] language model in the background so
[16:46] really strive to build
[16:49] multimodally so in summary we tackled a
[16:51] lot today but we're at the perfect storm
[16:53] today for AI agents but unfortunately
[16:55] that lightning hasn't struck yet and AI
[16:57] agents are not going to happen
[16:59] overnight cumulative errors add up we
[17:02] see wrong answers wrong preferences
[17:03] wrong criteria all these wrong human
[17:05] expectations that abound when you're
[17:06] building these systems data curation
[17:10] evals and Scaffolding are all tools you
[17:12] can use to help mitigate a lot of these
[17:14] challenges and really please think
[17:17] bigger ux multimodality Innovative
[17:20] product experience that truly set the
[17:23] workflow and the vision apart and I'm so
[17:25] excited to see what all of you build and
[17:27] really excited to this conversation over
[17:30] the next few days thank you guys so much
[17:32] and look forward to talking to you
[17:34] throughout the conference thank you
[17:40] [Music]
