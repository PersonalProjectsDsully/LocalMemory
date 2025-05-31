---
type: youtube
title: Mission-Critical Evals at Scale (Learnings from 100k medical decisions)
author: Channel Video
video_id: cZ5ZJy19KMo
video_url: https://www.youtube.com/watch?v=cZ5ZJy19KMo
thumbnail_url: https://img.youtube.com/vi/cZ5ZJy19KMo/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence / Machine Learning
tags: ['AI evaluation', 'real-time systems', 'confidence scoring', 'edge case handling', 'medical data AI', 'LLM evaluation', 'scalability challenges', 'iterative pipeline improvement', 'label-free learning', 'AI confidence estimation']
entities: ['Anterior', 'LLM as judge', 'scalable evaluation system', 'reference-free evaluation', 'confidence estimation', 'human reviews', 'offline eval datasets', 'medical records']
concepts: ['real-time evaluation systems', 'binary output classification', 'confidence levels', 'edge case handling in AI', 'scalability challenges', 'label-free evaluation', 'iterative AI pipeline improvements', 'medical data heterogeneity']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['familiarity with machine learning pipelines', 'understanding of evaluation metrics', 'knowledge of LLMs and confidence scoring']
related_topics: ['AI evaluation methodologies', 'real-time system design', 'confidence estimation techniques', 'edge case detection in AI', 'scalability of AI systems', 'medical data processing', 'label-free learning', 'iterative model improvement']
authority_signals: ["we saw we had these two questions which cases should we review and secondly of all the cases that we didn't review what how did we perform", 'the solution for that for these two problems is realtime reference-free evaluation system']
confidence_score: 0.8
---

# Mission-Critical Evals at Scale (Learnings from 100k medical decisions)

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=cZ5ZJy19KMo)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai, machine-learning, healthcare, medical-decisions, ai-automation, scaling-ai, real-time-ai  

## Summary

# Summary of "Mission-Critical Evals at Scale (Learnings from 100k medical decisions)"

## Overview  
Christopher Ljy, a medical doctor turned AI engineer, discusses the challenges of scaling AI evaluation systems for mission-critical healthcare decisions. The talk highlights the need for robust, real-time evaluation frameworks to handle high-volume, high-stakes scenarios like prior authorization decisions. Key solutions include human-in-the-loop reviews, offline datasets, and real-time reference-free evaluations to address the limitations of traditional methods.

---

## Key Points  
1. **Scaling Challenges**:  
   - Transitioning from MVP to handling 100k+ daily decisions exposes limitations in human review scalability and offline dataset relevance.  
   - Example: A medical error occurred due to missing nuance in a diagnosis (e.g., misclassifying an MS case), underscoring the "no room for error" requirement in healthcare.  

2. **Human Reviews & Dashboards**:  
   - A dedicated review dashboard enables human reviewers to label critiques, generating ground truths for training.  
   - However, scaling human reviews becomes impractical as volume grows (e.g., 50k+ daily decisions require 50+ reviewers).  

3. **Offline Datasets**:  
   - Offline datasets (e.g., gold standards, complex cases) help track performance over time but lag in capturing new edge cases.  
   - Reliance on offline data alone is risky due to the high heterogeneity of medical records.  

4. **Real-Time Reference-Free Evaluations**:  
   - A critical solution: **reference-free (label-free)** evaluations that assess outputs without waiting for human validation.  
   - Uses LLMs as "judges" to score outputs (e.g., confidence levels, conciseness, tone) and flag issues in real time.  

5. **Hybrid Approach**:  
   - Combines human reviews, offline datasets, and real-time LLM-based evaluations to balance accuracy, scalability, and responsiveness.  

---

## Key Quotes/Insights  
- *"No room for error in healthcare"*: The stakes demand rigorous, real-time validation.  
- *"Relying only on offline evals is playing with fire"*: New edge cases emerge continuously, making static datasets insufficient.  
- *"Real-time reference-free evaluations are the special source for trust."*  

---

## Actionable Takeaways  
1. **Implement a Review Dashboard**: Streamline human critiques and ground truth generation.  
2. **Balance Human & Automated Reviews**: Use human reviews for critical cases and automate with LLMs for scalability.  
3. **Build Hybrid Evaluation Systems**: Combine offline datasets (for known cases) with real-time reference-free evaluations (for emerging edge cases).  
4. **Leverage LLMs as Judges**: Use confidence scoring, tone analysis, and logic-based methods to assess outputs in real time.  
5. **Monitor Performance Over Time**: Segment datasets by complexity (e.g., ambiguous outcomes, rare conditions) to track AI improvements.

## Full Transcript

[00:00] hi my name is Christopher ljy and I'm a
[00:02] medical doctor turned AI engineer and in
[00:04] this talk I'm going to consider what it
[00:05] means to build an eval system that works
[00:07] at scale and in particular one that
[00:09] supports Mission critical decisions like
[00:11] in healthcare where there's no room for
[00:13] error now this is something we've had to
[00:14] figure out at anterior as we've scaled
[00:16] to now serve insurance providers
[00:18] covering 50 million American lives so
[00:20] I'll share what we've learned in the
[00:21] last 18 months why real-time
[00:23] reference-free evals can be the special
[00:25] source that enables customer trust and
[00:27] how you can build them for your company
[00:30] so we've all seen that it's pretty easy
[00:31] to create an MVP product powered by llms
[00:34] and it's getting even easier as models
[00:36] get more and more powerful but what
[00:38] about going from MVP to serving
[00:39] customers at scale now there are a lot
[00:41] of problems that you just won't see
[00:42] until you hit scale and as request
[00:44] volume increases so does a number of
[00:46] edge cases that you've never seen
[00:48] before so let's look at an example from
[00:50] the medical industry at anterior our
[00:52] core product supports prior
[00:53] authorization decisions around whether a
[00:55] treatment request should be approved or
[00:57] reviewed by a clinician we receive
[01:00] medical records and guidelines which
[01:01] contain various questions so an example
[01:04] question might be whether a patient has
[01:05] had a previous brain MRI suspicious for
[01:08] multiple sclerosis and this is then
[01:10] being used to determine whether the
[01:11] patient should receive an MRI of their
[01:13] cervical spine so our AI may show
[01:15] something like this that the medical
[01:17] record shows a brain MRI from this date
[01:19] that demonstrates hyperintensity in the
[01:22] infratentorial DRX theortical and per
[01:24] ventricular white matter which is noted
[01:26] to be consistent with multiple sclerosis
[01:28] and this confirms prior brain m findings
[01:30] suspicious for MS and on the surface
[01:32] this looks pretty reasonable but the
[01:34] problem is that this is missing some key
[01:36] medical Nuance now in a medical context
[01:39] if I as a doctor say that something is
[01:41] suspicious I'm implying that the patient
[01:43] doesn't already have a confirmed
[01:44] diagnosis but in this case the patient
[01:46] actually did have an existing diagnosis
[01:48] and therefore this is not just
[01:49] suspicious it's confirmed which means
[01:51] that this answer is actually wrong now
[01:54] this kind of mistake might happen every
[01:55] thousand cases or even every 10,000
[01:57] cases but if you're processing more than
[01:59] 100 ,000 cases every day then that's a
[02:01] lot of mistakes that you need to pick up
[02:04] and the problem is we just can't make
[02:05] mistakes like this there are many
[02:07] organizations in US Healthcare that are
[02:09] being sued right now for using AI
[02:10] automation inappropriately so how do you
[02:13] identify and handle failure cases well
[02:16] the first thing you should consider is
[02:17] performing human reviews of AI outputs
[02:21] and interior we've built out an internal
[02:22] clinical team and created internal
[02:24] tooling to make this as easy and
[02:26] effective as possible so this is our
[02:28] review dashboard which we've called
[02:29] scalp
[02:30] and on the right hand side here we have
[02:32] all of the context that our reviewer
[02:33] needs surfaced in an accessible way
[02:35] without any scrolling required so they
[02:37] can see the medical record and they can
[02:39] also see the guideline and on the left
[02:41] hand side we have the question that
[02:43] we're answering and the required context
[02:46] and this empowers our reviewers to
[02:47] review a high number of questions very
[02:49] quickly so continuing our example from
[02:50] before we can ask our reviewers to add a
[02:53] critique saying why this is wrong and
[02:55] label it as Incorrect and then save that
[02:58] into our system and one thing we can do
[03:00] with these critiques which are a
[03:01] statement of what's wrong is we can
[03:03] generate ground truths which are a
[03:05] statement a description of what the
[03:06] correct answer is so using that critique
[03:09] and the original answer we can then
[03:11] generate these ground truths and we can
[03:13] use those ground truths in offline
[03:14] evaluations which I'll talk about
[03:17] shortly but there's a problem with human
[03:19] reviews and it's the following let's say
[03:21] we've created an MVP we have our first
[03:23] customer and we're making around a th000
[03:25] medical decisions per day well we want
[03:27] to know how we're doing so let's say
[03:28] we'll review half of those cases to give
[03:30] us a good
[03:32] estimat um now reviewing half of those
[03:35] means 500 human reviews per day and if
[03:37] every clinician on our team can do about
[03:39] 100 reviews per day that means we need
[03:40] five clinicians to do all of these
[03:42] reviews and that's okay that can work
[03:46] but the problem is when we go beyond MVP
[03:48] and we you know we start doing 10,000
[03:50] medical decisions a day to maintain the
[03:52] same percentage we would now have to do
[03:53] 5,000 human reviews every day so
[03:55] maintaining the same ratio we now need
[03:57] 50 clinicians and that's bigger than our
[04:00] entire companies at the moment okay so
[04:02] what we might do is say well maybe let's
[04:04] you know review a smaller subset of
[04:06] cases let's only review 5% that gets us
[04:09] back down to 500 human reviews a day
[04:11] which can be done by five clinicians but
[04:13] the problem comes as we scale even
[04:14] further let's say we now grow to 100,000
[04:17] medical decisions per day which is still
[04:18] a very conservative number again we're
[04:21] back at 5,000 human reviews and 50
[04:23] clinicians so the problem here is clear
[04:25] this just doesn't scale and we're left
[04:28] with these two questions which which is
[04:30] firstly which cases should we review and
[04:33] secondly of all the cases that we didn't
[04:34] review what how did we
[04:36] perform so another component of this is
[04:39] offline eval data sets and by offline
[04:42] here I'm referring to data sets that we
[04:44] build that live outside of our product
[04:46] and we can keep on running evals against
[04:48] them and getting scores so we can take
[04:50] the ground truths that we generated from
[04:51] our human reviews to build these data
[04:53] sets and this can be helpful we can
[04:55] Define some gold standard data sets we
[04:57] can segment them by Enterprise by uh
[05:00] specific medical type medical conditions
[05:03] you know tough questions complex cases
[05:04] ambiguous outcomes and we can plot those
[05:06] performances over time we can use them
[05:08] for iterating our our AI pipelines
[05:10] against and and it's helpful but the
[05:11] problem is that if you wait until New
[05:14] edge cases are represented in this data
[05:16] set which You're Building kind of
[05:17] Downstream of actually giving this to
[05:19] the customer it could be too late so
[05:21] relying only on offline evals is playing
[05:24] with fire um and the input space of
[05:27] medical records is huge there's very
[05:29] high heterogeneity so at scale you're
[05:32] continually going to see new edge cases
[05:34] that you need to identify and respond
[05:37] to and the solution for that for these
[05:40] two problems is realtime reference-free
[05:42] evaluation system so reference free also
[05:45] known as label free means that you
[05:47] evaluate before you know the true
[05:49] outcome I.E before you have done a human
[05:51] review and that enables the system to be
[05:53] real time it enables you to respond to
[05:55] issues immediately as they
[05:57] arise so we saw we had these two
[06:00] questions which cases should we review
[06:02] and how do we do on the cases that we
[06:04] couldn't do a human review on well a
[06:07] great starting point here is using an
[06:08] llm as judge the way this works is the
[06:10] following so we have our inputs they go
[06:12] into our llm pipeline that we're
[06:14] evaluating and it gives some kind of
[06:15] outputs we then feed that output into an
[06:18] llm as judge along with a scoring system
[06:21] and this scoring system can be many
[06:23] different things it could be uh how
[06:25] helpful is the output how concise is the
[06:27] output is the tone of the output on
[06:29] brand it could be how confident are we
[06:31] that the output is correct if our if our
[06:33] output is a binary or multiclass
[06:35] classification we can give that
[06:36] confidence level so in our case at
[06:38] anterior we do have a binary output our
[06:41] generated output is either approval that
[06:44] we think this treatment should be
[06:45] approved or it's an escalation for
[06:46] review and we can take that we can put
[06:49] that into our reference free eval which
[06:51] could be an llm as judge but can also be
[06:53] other methods such as confidence
[06:55] estimation using logic based methods and
[06:58] using those methods either alone or in
[07:00] combination we can then give an output
[07:02] and in our case we use it to give us a
[07:03] confidence grading how confident are we
[07:05] that our llm outputs from our actual
[07:08] pipeline here is correct we can go all
[07:10] the way from high confidence that it's
[07:12] correct down to such low confidence that
[07:15] we actively think this is wrong and then
[07:16] we can use that score and use a
[07:17] threshold to convert that into what the
[07:19] predicted correct output is so what do
[07:21] we think the the right answer is and
[07:23] these are two pieces of information that
[07:24] we can then use in different
[07:27] ways the first thing we can do is we can
[07:29] predict the estimated performance on all
[07:32] of the cases real time as we're
[07:33] processing them so we get our medical
[07:35] decisions coming in we put them through
[07:37] our reference for evals and we get our
[07:38] predicted correct outputs we can then
[07:40] see across all of these cases not just
[07:42] the ones that we're doing human reviews
[07:43] on how do we think we performed and
[07:45] that's useful because we can then
[07:46] respond to that and we can feed that
[07:48] back to customers we can then take our
[07:50] cases where we did do human reviews as
[07:52] well as reference free evals and we can
[07:54] compare those outputs based on that we
[07:56] can compute an alignment and see how
[07:58] well is our system doing and how much
[07:59] can we trust
[08:01] it and another thing that we can do is
[08:03] we can take our confidence grading
[08:05] rather than our predicted outputs from
[08:06] our reference evals and we can combine
[08:09] those with contextual factors things
[08:11] like the cost of procedure the risk of
[08:12] bias the previous error rates and we can
[08:14] use those to dynamically prioritize the
[08:16] order for cases so we can identify the
[08:19] most relevant cases with the highest
[08:21] probability of error to then prioritize
[08:23] those for human
[08:24] review and this creates this virtuous
[08:27] cycle where we can keep on using human
[08:29] reviews to validate and improve our
[08:31] performance and then we can prioritize
[08:33] cases dynamically and keep on feeding
[08:35] that back so our reference free evals
[08:37] surface the cases and then our human
[08:38] review determines the accuracy and we
[08:40] can keep on doing this in a process
[08:41] that's often described as validating the
[08:43] validator and over time the number of
[08:45] edge cases that we've never seen before
[08:47] get smaller and smaller and our ability
[08:48] to detect them improves and now we've
[08:50] built something that's really hard to
[08:51] replicate so while a competitor may be
[08:53] able to make a similar product you can
[08:55] only build this system by processing
[08:57] High volumes of real data and going
[08:58] through a number number of datadriven
[09:00] iterations and once we're confident in
[09:01] the performance of our system we can
[09:03] then actually incorporate it into the
[09:04] pipeline itself so now it looks like the
[09:06] following we have our inputs we pass it
[09:09] through our original Pipeline and we
[09:10] generate our outputs and we then pass it
[09:12] into our reference free evals and
[09:14] depending on what the reference free
[09:15] eval output is we can either give it
[09:17] back to the customer because we're
[09:18] confident in the response that we're
[09:19] giving or we can decide to take a
[09:21] further action and this further action
[09:23] might be that we send it off to another
[09:24] llm pipeline perhaps with more expensive
[09:26] models it might be that we want to do a
[09:28] human internally and give it to an on
[09:31] call clinician to review it and then
[09:33] return it to the customer or it might be
[09:34] that we want to actually surface it into
[09:35] the customer's review dashboard so that
[09:37] their team can review it but Al together
[09:38] this becomes a powerful mechanism for us
[09:40] to really ensure that our customer can
[09:43] trust the outputs that we're giving to
[09:44] them so what's the impact been for us at
[09:46] anterior how has this helped us well the
[09:49] first thing that's enabled us to not do
[09:51] is to hire out an ever expanding team of
[09:52] expert contians to review these cases
[09:55] one of our biggest competitors has hired
[09:56] over 800 nurses to perform reviews now
[09:59] we haven't needed to do this instead
[10:01] we're able to review tens of thousands
[10:03] of cases with a review team of less than
[10:06] 10 clinical
[10:08] experts we've been able to achieve very
[10:10] strong alignment after several
[10:11] iterations between our Ai and human
[10:13] reviews to a level that is comparable
[10:15] with the alignment we see between our
[10:16] human
[10:18] reviewers and we're now able to quickly
[10:20] identify and respond to errors so using
[10:22] this example from earlier we can quickly
[10:24] go from this incorrect answer to a
[10:26] correct answer this means we're able to
[10:28] respond quickly and still still meet
[10:29] customer slas around time expectations
[10:32] and we can be confident in the results
[10:33] that we're returning to them and the
[10:35] ultimate impact of this is that we now
[10:37] have provably industry-leading
[10:38] performance at prior authorization with
[10:40] an F1 score of nearly 96% in a recent
[10:43] study and this has enabled us to gain
[10:45] customer trust and Beyond even customer
[10:48] trust this has led customers to love our
[10:51] product in a recent case study we saw
[10:53] that one of the nurses after they were
[10:55] told they could keep on using Florence R
[10:57] AI said Thank God with lucky
[11:01] ones so the principles that we followed
[11:04] for building our system and what we
[11:05] would recommend is firstly make sure you
[11:08] build a system you know think big don't
[11:10] just use review data to to audit your
[11:12] performance use it to build audit and
[11:15] improve your auditing system your
[11:17] evaluation system the second thing is
[11:19] evaluating on live production data don't
[11:21] rely on offline evals identify problems
[11:24] immediately so that you can respond to
[11:25] them quickly and thirdly get the best
[11:28] reviewers and empowers them prioritize
[11:30] the quality of reviews over quantity and
[11:32] build your own tooling if that helps you
[11:34] to move
[11:35] faster this is how we built an
[11:37] evaluation system that gives real-time
[11:39] performance estimates enabling us to
[11:41] respond is accurate that can scale to
[11:44] meet demand while maintaining a low cost
[11:46] all powered by a small focused team of
[11:49] experts and it's enabled us to go from
[11:51] our MVP to now serving customers and
[11:54] maintaining their trust at scale and
[11:56] it's how we think you can too so thank
[11:58] you for your attention um we' love to
[12:00] talk more about this if you have any
[12:01] thoughts or ideas please reach out to me
[12:03] my email here is is Chris an.com and
[12:05] we're also hiring at the moment so if
[12:07] you want to be The Cutting Edge of LM
[12:08] application in healthcare then check out
[12:10] our open posts at ani.com
[12:12] compan thank you
