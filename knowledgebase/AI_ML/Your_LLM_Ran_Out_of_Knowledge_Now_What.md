---
type: youtube
title: Your LLM Ran Out of Knowledge — Now What?
author: AI Engineer
video_id: ya_9_niq2as
video_url: https://www.youtube.com/watch?v=ya_9_niq2as
thumbnail_url: https://img.youtube.com/vi/ya_9_niq2as/mqdefault.jpg
date_added: 2025-05-26
category: AI and Decision Making
tags: ['LLM', 'rule-based systems', 'negotiation strategy', 'simulation', 'AI ethics', 'prompt engineering', 'heuristics', 'geopolitical strategy', 'corporate negotiations', 'structured data', 'AI applications', 'decision support systems']
entities: ['LLM', 'geopolitics', 'corporate negotiations', 'simulator', 'prompt', 'rules', 'heuristics', 'CR critical resources']
concepts: ['rule-based decision making', 'structured formatting', 'heuristics', 'simulation consistency', 'scenario parsing', 'prompt engineering', 'geopolitical strategy', 'corporate negotiations']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['familiarity with LLMs', 'negotiation strategy basics', 'simulation tools', 'prompt engineering', 'structured data formatting']
related_topics: ['AI ethics', 'negotiation tactics', 'simulation modeling', 'NLP techniques', 'decision support systems', 'rule-based systems', 'strategic planning', 'machine learning applications']
authority_signals: ["I've taken a little bit more of a long-winded way of doing it", 'we want to make it nice and straightforward rather than having sort of abstract vague rules', "it's a little easier to go in and edit these"]
confidence_score: 0.8
---

# Your LLM Ran Out of Knowledge — Now What?

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=ya_9_niq2as)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: large language models, knowledge gaps, training data limitations, domain specific knowledge, ai reasoning, model training techniques, data scarcity  

## Summary

# Summary of "Your LLM Ran Out of Knowledge — Now What?"

## Overview  
The video addresses the challenge of LLMs lacking domain-specific knowledge in unstructured fields (e.g., corporate negotiations, geopolitics) and proposes a solution: **using structured heuristics and rules** to guide LLMs, mirroring how humans are trained. It emphasizes standardization, rule-based frameworks, and adaptability to improve performance in complex scenarios.

---

## Key Points  
- **Structured vs. Unstructured Knowledge**:  
  - LLMs excel in math/coding due to structured data but struggle with unstructured domains (e.g., negotiations) where knowledge is tacit or undocumented.  
  - **"The fault of the practitioners"**: Many professionals don’t document their expertise, creating gaps in training data.  

- **Proposed Solution**:  
  - **Heuristics/Rule-Based Systems**: Replace vague instructions with clear, binary rules (e.g., "must prioritize agreements with highest combined value").  
  - **Standardization**: Format inputs consistently to improve model performance.  

- **Technique Demonstrated**:  
  - **Rule Matching**: The model identifies applicable rules based on user input.  
  - **Scenario Structuring**: Parses and reformats scenarios into a standard format for consistency.  
  - **Domain-Specific Rules**: Separate rule sets for negotiations/geopolitics, with flexibility to adjust scenarios.  

- **Limitations of Tool Use**:  
  - Direct tool integration may not work well; a more manual, rule-driven approach is preferred.  

---

## Important Quotes/Insights  
- *"The only reason these are split out [into negotiation/geopolitics rules] is to avoid the prompt becoming too unwieldy."*  
- *"We want to make it nice and straightforward rather than abstract vague rules."*  
- *"Standardization really helps these models work most effectively."*  

---

## Actionable Takeaways  
1. **Adopt Heuristics**: Replace ambiguous instructions with clear, binary rules for specific domains.  
2. **Standardize Inputs**: Format user queries to ensure consistency and improve model accuracy.  
3. **Create Domain-Specific Rule Sets**: Develop modular rules for different scenarios (e.g., negotiations, strategy).  
4. **Combine with Reasoning**: Use structured rules to augment LLMs’ inherent reasoning capabilities.  
5. **Iterate and Refine**: Adjust rules dynamically based on scenario complexity and feedback.  

--- 

This approach bridges the gap between LLMs’ general knowledge and the nuanced demands of specialized fields, enabling more reliable and adaptable AI systems.

## Full Transcript

[00:01] so it wasn't that long ago that we were
[00:02] all talking about chat Bots And It Felt
[00:05] Like Only Yesterday that we were excited
[00:07] about agents but today all we're talking
[00:10] about is reasoning and how these models
[00:13] can now reason through complex problems
[00:16] but how is a model going to solve a
[00:17] problem when we haven't been able to
[00:19] give it any training data or knowledge
[00:21] in that specific domain
[00:26] [Music]
[00:42] so what I want to do here is share a
[00:45] technique that you might want to try in
[00:48] one of these low knowledge domains so
[00:50] what do I mean by that well we know that
[00:52] the models are great at coding and the
[00:54] models are great at math and that's not
[00:56] surprising because we have large bodies
[01:00] of trainable material well structured
[01:03] information and data that we can give to
[01:05] the models to train them for Math and
[01:07] coding and the law and physics because
[01:10] everything is structured in a consistent
[01:12] way and it's in a format where we can
[01:14] easily convert that into training data
[01:16] and give it to a model the problem that
[01:19] we have is that we also have other areas
[01:21] where we don't have well structured
[01:23] information so as an example think about
[01:26] uh corporate negotiations we know what
[01:28] the start point was because there was a
[01:30] story in the Wall Street Journal that
[01:32] company a wants to acquire Company B and
[01:34] we know what the end point was because
[01:36] CNBC or the financial times had a
[01:39] headline explaining what the outcome was
[01:42] but what we don't know is what happened
[01:44] in the room what did those negotiations
[01:46] actually look like we might have some
[01:47] rules or guidelines that come from an
[01:50] MBA course but we don't know what those
[01:52] discussions were so there a lot of
[01:54] domains where that specific knowledge
[01:56] that wisdom is locked away it's in
[01:58] people's mind it's never written down
[02:00] and where this is taking us or where
[02:02] this could take us is that we still have
[02:04] these areas where this knowledge Gap is
[02:06] not being filled so actually we have uh
[02:09] sectors or professions who are becoming
[02:13] um better served by these models who
[02:16] have more powerful models at their
[02:17] disposal they can do more and more but
[02:19] then we have other domains who are
[02:21] almost being left behind
[02:32] they don't have models that understand
[02:34] what they do uh and aren't able to apply
[02:37] them to the problems that they come
[02:38] across so what we want to do is actually
[02:40] close that Gap how can we close that Gap
[02:43] where we do have this lack of knowledge
[02:45] and as practitioners in the sect I'm
[02:47] from risk and Security Management it is
[02:49] the fault of the practitioners we don't
[02:51] write things down so this is not the
[02:53] fault of the people training the models
[02:54] and this is nobody's particular fault
[02:56] but the sheer fact is we don't write
[02:59] things down and therefore there won't be
[03:01] there isn't and there won't be the
[03:02] material to train a model so what do we
[03:05] do to overcome that how can we overcome
[03:07] this knowledge Gap uh in order to make
[03:09] sure that we have models that can work
[03:11] in all of the domains where we want to
[03:13] apply their expertise skill and ability
[03:16] well one of the things we can do is we
[03:18] can use a technique that we already use
[03:19] we already used this in the workplace
[03:21] someone who has just left College
[03:23] they're recent graduate highly
[03:25] intelligent but probably lower in wisdom
[03:27] they haven't had the experience now
[03:29] there are lots of things we can do but
[03:30] one of the things that works really well
[03:32] is giving them guidelines giving them
[03:34] rules of thumb heuristics whatever you
[03:36] want to call them we can give them some
[03:38] guidelines to apply in specific
[03:41] domains what that then means is they can
[03:43] use their intelligence apply these rules
[03:46] for that domain in order to solve
[03:48] problems in order to understand what's
[03:50] happening and start to work through
[03:52] things in that specific domain while
[03:54] they build up their personal knowledge
[03:56] and so the technique that I'm talking
[03:58] about today takes that same approach
[04:01] except we do that with the llms with the
[04:03] models we're going to give them a set of
[04:05] rules to follow for specific domains and
[04:08] ask them to apply those on top of the
[04:11] very powerful reasoning capabilities
[04:13] that they now have and that's going to
[04:15] give us the benefit of the powerful llm
[04:18] the benefit of the reasoning but
[04:20] overcome these wisdom gaps and give them
[04:22] the subject matter expertise they need
[04:25] to start working in these other
[04:27] domains all right so let's see what this
[04:29] look looks like in practice so I'm going
[04:31] to toggle between this front end which
[04:33] is just an easier way to show the the
[04:35] the inputs and outputs and uh we'll go
[04:38] and look at the back end as well and see
[04:40] what's happening behind the scenes and
[04:41] how the logic's working but this is an
[04:43] easy way just to show the process so I'm
[04:45] going to drop in a prompt and right away
[04:48] you'll see this is quite a long prompt
[04:49] it concerns an intelligence estimate and
[04:52] so what's happening in the background
[04:54] now is it's trying to figure out what
[04:55] kind of problem do I have and what rules
[04:57] should I apply and we'll see how that
[04:59] works in a second the other thing it's
[05:02] going to do it's going to reformat the
[05:04] uh question that I give it and it's
[05:06] going to put it into a standard format
[05:08] because again what I found uh is that
[05:11] standardization really helps these
[05:13] models work most effectively okay so
[05:16] here's what's going on behind the scenes
[05:19] um theistic match this is basically the
[05:21] same as tool use um I found that tool
[05:24] use wasn't working out uh as well as I
[05:26] would hope um and so I've taken a little
[05:29] bit more more of a long-winded way of
[05:31] doing it so there's a specific llm
[05:33] specific prompt um that is going to
[05:35] match up um the user input and look for
[05:40] a match with one of theistic and you'll
[05:41] see that these are listed um down here
[05:43] it's analyzing for those and so that's
[05:46] the first thing that it's doing whatever
[05:48] you've presented to this model it's
[05:51] looking for a match for the specific
[05:53] rules that you want it to apply we want
[05:56] it to be consistent in the way it's
[05:58] presenting the information to the actual
[06:00] simulation so we haven't got to the
[06:01] simulation yet when we get there though
[06:03] we want to make things as consistent as
[06:05] possible and make sure that they're
[06:07] formatted so that the kind of material
[06:10] the um this the simulator needs is is
[06:13] contained in the prompt and so we've
[06:15] asked it to parse the scenario and
[06:17] return it in the structured format and
[06:19] you'll see at the front end you actually
[06:21] have the opportunity to go in and edit
[06:22] it if necessary but we're just trying to
[06:24] make things consistent so that each time
[06:27] it gets a scenario it's in this standard
[06:29] format so the first two things it's
[06:31] doing is looking for a match
[06:33] standardizing the
[06:35] format so once we have a match we're now
[06:38] going to come over to the rule Set uh
[06:40] and find the appropriate rules and
[06:41] behavior for that particular type of
[06:44] problem so we have two uh different
[06:47] types of scenario rules in the uh in the
[06:50] demo negotiations geopolitics so these
[06:53] are the rules um these are written in a
[06:55] fairly binary way you must do must not
[06:58] do they're provable it's provable if you
[07:00] have prioritized agreements that create
[07:02] highest combined value it's provable if
[07:05] you've got these um three plus
[07:06] independent P for CR critical resources
[07:09] and that's deliberate because we want to
[07:10] make it nice and straightforward rather
[07:12] than having sort of abstract vague rules
[07:14] we want to give it quite clear rules but
[07:16] by the time you combine these together
[07:18] you quite a sophisticated model for uh
[07:20] these are corporate negotiations or
[07:22] geopolitical strategy so these are the
[07:24] rules these are the same heuristics we
[07:26] might give to our consultant that we
[07:28] were imagining before for and then we
[07:30] have this heuristics list which is a
[07:33] higher level prompt a sort of system
[07:35] level prompt how you wanted to behave
[07:37] and you can see at the end and it then
[07:39] pulls in uh the rules either for
[07:41] negotiations or geopolitical strategy
[07:44] and the only reason these are split out
[07:45] it's just because it it helps avoid the
[07:47] prompt becoming too unwieldy it's a
[07:49] little easier to go in and edit these
[07:51] and so you would have these rules for
[07:53] the rules you want to apply you might
[07:55] want to adjust these in different
[07:56] scenarios and different situations so
[07:58] you quite a lot of flexibility around
[08:00] here but what this gives you is this
[08:02] high level uh very comprehensive prompt
[08:05] set of rules and guides that really
[08:07] focus the model in on how you want it to
[08:10] behave Okay so we've now got the results
[08:13] so here's my original um my original
[08:16] question and you can see it's done two
[08:18] things first it's identified the type of
[08:20] problem as a geopolitics and now it's re
[08:23] uh reformatted the question into a
[08:26] specific format and this is just so
[08:28] we've got consistent input to the actual
[08:31] uh reasoning or planning model so a lot
[08:34] of Works happened up front to take
[08:35] everything that the user has presented
[08:37] to it identify what that is package it
[08:40] up correctly and then it's going to send
[08:42] it off to the model for
[08:44] analysis so as far as the models
[08:46] concerned you can send it to whichever
[08:47] model you're comfortable with whichever
[08:49] model you think will perform best in
[08:51] this case it's actually going to
[08:53] anthropic because I'm running this world
[08:55] Sim and um this is something you know I
[08:58] owe a great deal to uh new research and
[09:01] Karen because I first saw this um uh
[09:04] from one of his demos and so it's
[09:06] running this world Sim version to give
[09:08] it this sort of realistic view of what
[09:10] the world looks like because we're
[09:11] dealing with geopolitics so it's
[09:13] particularly relevant to this particular
[09:15] example and that's just going to add on
[09:17] more realism and give it some additional
[09:19] uh constraints to think about so the the
[09:21] physical geography of the world uh
[09:24] things like the UN and the WTO need to
[09:26] be considered where appropriate so we're
[09:28] just sort of very quickly giving it a a
[09:30] whole set of other parameters to
[09:32] consider or or to lean upon and so
[09:35] particularly as I said for this example
[09:37] of geopolitics this is useful but at
[09:40] this stage you could point it towards
[09:41] whichever model um you see fit uh and
[09:44] whichever one you're comfortable with so
[09:47] when we come back and look at the
[09:48] results obviously we've got these in a
[09:50] in a presentable format they're easy to
[09:52] read we can see right away it's
[09:54] following the structure that we've given
[09:55] it so we know that it's obeying the
[09:57] general rules and as we go go down and
[09:59] look at the output you'll see that it's
[10:02] starting to reference two times leverage
[10:04] greater than 50% control and those are
[10:06] all rules that it was given in that
[10:08] large uh rule set for uh geopolitics so
[10:12] we can see that it's applying those in
[10:14] our thinking we know it's applied the
[10:15] rules that we asked it to in the
[10:17] considerations and then when you come
[10:19] down to examples like scenario 5 it
[10:21] would breach one of the rules and
[10:23] therefore it's being eliminated and so
[10:25] not to get into the detail of whether
[10:27] this is the best approach or not for us
[10:29] semiconductor development um the point
[10:32] is we can see now that it is not only
[10:34] using its reasoning ability the
[10:36] intelligence that we know the model has
[10:39] but it's also overcoming perhaps domain
[10:42] expertise or a lack of insight into how
[10:45] these decisions might be made but it's
[10:47] overcoming that by applying the rules
[10:48] that we gave it and we can see that the
[10:50] the rules are being applied so by this
[10:54] point I'm hoping that it's given you a
[10:55] sense of one other approach um it is an
[10:58] approach I'm still working through
[11:00] however so far the first results are
[11:02] very positive it is able to identify the
[11:05] type of problem and using a a larger
[11:08] prompt instead of just tool use gives us
[11:10] a lot more granularity there we're able
[11:13] to then work with a subject matter
[11:15] expert to give us really tight rules and
[11:17] heuristics to follow and then it can
[11:19] apply those on top of these powerful
[11:21] reasoning tools and things like the
[11:23] world Sim to start to iterate through
[11:25] lots and lots of different options and
[11:27] come up with the optimum solution ution
[11:29] or give us multiple scenarios and again
[11:32] I would always want a human in the loop
[11:34] I would want a subject matter expert to
[11:36] be part of this discussion but obviously
[11:39] these machines are able to work so much
[11:40] more quickly that a human expert could
[11:43] generate dozens of scenarios to review
[11:45] in a fraction of the time it would take
[11:47] them normally and that allows us to
[11:49] either challenge um problems or take on
[11:51] more challenging problems to work
[11:54] through uh many more options in in a
[11:56] finite amount of time where time is at
[11:58] an essence or even look for new uh
[12:01] approaches that we might not have
[12:02] thought about so if you come across one
[12:04] of these areas I'm hoping this technique
[12:06] this approach will help you where you're
[12:08] using the parsing engine you're using
[12:11] the rules of thumb and uh applying those
[12:15] in that problem solving in addition to
[12:17] using all of the llms and I hope that
[12:20] that helps uh us move these models into
[12:23] other areas uh that are currently a
[12:25] little uh underexplored
[12:29] for
