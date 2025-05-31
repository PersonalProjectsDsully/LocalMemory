---
type: youtube
title: GitHub's AI Powered Security Platform: Sarah Khalife
author: Channel Video
video_id: utTqdQpe39A
video_url: https://www.youtube.com/watch?v=utTqdQpe39A
thumbnail_url: https://img.youtube.com/vi/utTqdQpe39A/mqdefault.jpg
date_added: 2025-05-26
category: Software Security
tags: ['GitHub Security', 'CodeQL', 'SAST', 'DevSecOps', 'vulnerability scanning', 'AI in Security', 'open-source tools', 'software development', 'security integration', 'CI/CD security']
entities: ['GitHub Advanced Security', 'CodeQL', 'SAST', 'container scanning', 'Microsoft', 'Google', 'Uber', 'SIIF inputs', 'P request', 'code scanning']
concepts: ['code scanning', 'security integration', 'vulnerability detection', 'AI in security', 'community collaboration', 'third-party integrations', 'developer platforms', 'SAST (Static Application Security Testing)']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of software development', 'Familiarity with GitHub', 'Knowledge of security concepts', 'Experience with code scanning tools']
related_topics: ['DevSecOps', 'SAST tools', 'CI/CD security', 'open-source collaboration', 'vulnerability management', 'software development lifecycle', 'security automation', 'threat detection']
authority_signals: ['we have the context and we have that information in there', 'anything that we do is community backed']
confidence_score: 0.8
---

# GitHub's AI Powered Security Platform: Sarah Khalife

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=utTqdQpe39A)  
**Published**: 3 months ago  
**Category**: Security  
**Tags**: github, ai, security, cybersecurity, developer-tools, ai-security, github-platform  

## Summary

# Comprehensive Summary of "GitHub's AI Powered Security Platform: Sarah Khalife"

## Overview  
Sarah Khalife, a Principal Solutions Engineer at GitHub, discusses how AI is being integrated into GitHub's security tools, particularly **GitHub Advanced Security (GHAS)**. The talk emphasizes leveraging AI to enhance code scanning, vulnerability detection, and developer workflows while highlighting community collaboration, third-party integrations, and scalability.

---

## Key Points  
1. **AI Integration Beyond Copilot**  
   - GitHub is expanding AI capabilities across its platform, not just in Copilot. AI is being applied to security workflows to improve vulnerability detection and remediation.  
   - Focus on **GitHub Advanced Security (GHAS)**, which includes tools like code scanning, container scanning, and third-party integrations.  

2. **Code Scanning & CodeQL**  
   - **Code scanning** uses **CodeQL** (an open-source analysis engine) to detect vulnerabilities in code. It identifies data flows and exploits, enabling faster remediation.  
   - CodeQL queries are community-driven, incorporating contributions from Microsoft, Google, Uber, and others.  

3. **Third-Party Integrations**  
   - GHAS supports integrations with external tools (e.g., container scanning) via APIs, allowing results to be fed back into pull requests for real-time feedback.  

4. **Community & Collaboration**  
   - GitHub emphasizes community-backed security solutions, acknowledging that no single entity can address all vulnerabilities.  
   - Partnerships with vendors and open-source contributors strengthen security capabilities.  

5. **Scale & Live Demos**  
   - GitHub serves 100+ million developers, with 90% of Fortune 500 companies using its platform.  
   - Live demos are a key part of GitHub’s approach to showcasing tools, even if they occasionally fail.  

---

## Key Quotes/Insights  
- "Security hasn’t been as discussed as other AI aspects, but it’s critical for developers."  
- "CodeQL isn’t just GitHub’s queries—it’s community-driven, including Microsoft, Google, and Uber."  
- "Third-party integrations allow results to be fed back into pull requests, enabling faster feedback."  

---

## Actionable Takeaways  
- **Adopt AI-driven security tools** like CodeQL for proactive vulnerability detection.  
- **Engage with the community** to contribute and benefit from shared security queries.  
- **Leverage third-party integrations** to enhance GHAS with external tools (e.g., container scanning).  
- **Participate in live demos** to understand real-world applications of GitHub’s security features.  

--- 

This summary captures the core themes of AI-driven security, community collaboration, and scalability in GitHub’s approach to developer security.

## Full Transcript

[00:03] [Music]
[00:13] thank you all for joining today thank
[00:15] you for staying a few States from the
[00:16] previous session as well I know there
[00:18] were a bunch of GitHub talks so I'm all
[00:22] uh I'm very excited that you got to hear
[00:24] from all of us from all different places
[00:25] within the company but also from all
[00:27] different teams um so you heard a a lot
[00:30] about co-pilots a lot a lot about
[00:32] co-pilot co-pilot today co-pilot
[00:34] tomorrow co-pilot in the next year maybe
[00:36] in a couple years so from workspaces to
[00:39] get co-pilot Enterprise to co-pilot
[00:41] Futures there's so much more going on
[00:44] with co-pilot itself but what we really
[00:47] want to actually do within GitHub is not
[00:49] only incorporate some of the new
[00:50] features and capabilities within
[00:51] co-pilot only but we also want to
[00:53] incorporated as part of the platform so
[00:56] everything within the platform itself
[00:58] will start having AI in it so today
[01:00] you've heard a lot about co-pilot
[01:02] obviously we're at an AI conference so
[01:04] if you didn't that would have been a bad
[01:05] thing but with collaboration proactivity
[01:08] and security those some of are some of
[01:11] our biggest aspects of the GitHub core
[01:13] platform capabilities there from PO
[01:15] requests as you heard some of the code
[01:16] review things that were happening
[01:17] earlier on but also from a productivity
[01:20] perspective how do you gain momentum and
[01:22] get more developers excited to do their
[01:24] work across their um developer platforms
[01:27] especially if they're using GitHub
[01:28] co-pilots uh how do you get that
[01:30] momentum going from a productivity
[01:32] perspective and then security security I
[01:34] feel like hasn't been talked about as
[01:36] much in terms of how can we improve
[01:38] absec with AI rather than just how do we
[01:42] talk about security around AI security
[01:45] around AI around AI is probably
[01:46] something talked about all the time from
[01:48] legal to privacy to everything in
[01:51] between um but what we want to do at
[01:53] GitHub is to also incorporate AI to make
[01:55] sure that security is also being
[01:57] progressed along with the new cap
[01:59] abilities that we're seeing
[02:01] today and everything that GitHub does we
[02:04] want to do it with scale we want to
[02:05] build our Integrations and our apis so
[02:07] anything that I've talked about today is
[02:09] generally API backed or there's a third
[02:11] partyy integrator that also comes in and
[02:13] helps with a lot of the capabilities
[02:15] there's never One path that solves all
[02:17] the answers so we want to make sure that
[02:18] all of our customers you know have a
[02:20] path way to a solution have a path to
[02:23] that
[02:24] solution today if you didn't know
[02:26] actually this might be not the latest
[02:28] num is actually
[02:30] um but I think the numbers are more I
[02:33] haven't updated the slide in a while but
[02:34] there's over 100 million developers
[02:36] registered on GitHub there's 4 million
[02:39] organizations 90% of the fortune U 100
[02:42] companies which sometimes I'm surprised
[02:44] by the numbers because I know everybody
[02:46] uses GitHub but like 90% of the Fortune
[02:49] 100 is mind-blowing I work with
[02:51] customers day in day out but this is
[02:53] still mind-blowing to see because that
[02:55] is how we get a lot of our feedback
[02:57] that's how we get a lot of our community
[02:59] part of the conversation that's how we
[03:01] build a lot of our features anything
[03:03] that we do we incorporate that Community
[03:05] back into that
[03:07] conversation um by means of
[03:09] introductions I'm Sarah khife I'm a
[03:11] principal Solutions engineer here at
[03:12] GitHub I've been at GitHub for about
[03:15] four and a half years now which is a
[03:17] long time for github's life um and it
[03:21] was pre-pilot pre some of the
[03:24] capabilities pre almost pre actions if
[03:26] you used actions so you know we've seen
[03:28] the platform grow a lot during the last
[03:30] couple of years but like I said the
[03:32] community is what really makes it the
[03:34] biggest better platform across the board
[03:37] our customers our vendors our partners
[03:39] everybody that is part of that
[03:40] conversation um is how we really get
[03:43] into the next iteration of what we're
[03:45] going to build and I'm lucky enough to
[03:47] work with a lot of customers so I'm
[03:48] working on the customer side of things
[03:50] all my customers today are financial
[03:52] services but over the last four and a
[03:54] half years I've been working with all
[03:56] types of customers from all different
[03:57] parts of the industries outside um in
[04:00] this Enterprise world that we live
[04:02] in so I did a quick introduction of what
[04:06] is the GitHub platform today we talked
[04:08] about co-pilot but that's only one
[04:10] aspect we talked a little about
[04:11] collaboration you heard about it earlier
[04:13] on through Christina and Chris's session
[04:16] um you also heard a lot about
[04:17] productivity especially with co-pilot
[04:19] being that in that conversation but
[04:21] today we're going to talk about GitHub
[04:23] Advanced security and how we're
[04:24] incorporating AI into that if you
[04:27] haven't heard of GitHub Advanced
[04:28] security don't worry I'm going to cover
[04:29] what is GitHub Advanced security and
[04:31] then we're going to talk about some of
[04:33] the new features are coming along that
[04:34] are the AI aspects into advanced
[04:36] security and then we'll do a live demo
[04:38] because as you can see all of our GitHub
[04:40] teams here love doing live demos even if
[04:42] they don't work or if they work better
[04:43] than they expect which is a very great
[04:46] example of what happened in the earlier
[04:47] session
[04:49] today so we'll be focusing on one aspect
[04:52] of the platform and then we'll be
[04:54] talking about specifically security so
[04:56] how can we incorporate Security in our
[04:58] day-to-day work and then how can AI
[05:00] improve that experience for our
[05:02] developers who here has used GitHub
[05:05] advaned security anybody nice a couple
[05:08] couple people so what is GitHub Advanced
[05:11] security so ADV GitHub Advanced security
[05:13] allows you to incorporate think of it as
[05:15] the your absec aspects into your
[05:18] developer platform day in day out and
[05:21] has that GitHub experience so when we
[05:22] talk about Advance Security we have code
[05:24] scanning code scanning allows you to do
[05:26] SASS and other types of code scanning
[05:29] within the developer platform within the
[05:30] GitHub ecosystem to find vulnerabilities
[05:33] and detect different patterns that are
[05:34] vulnerable to then help remediate them
[05:36] faster with code scanning today there
[05:38] are two aspects that I would say are the
[05:40] more popular aspects to talk about and
[05:42] we can talk about a lot more if you want
[05:44] to come to the GitHub uh Microsoft and
[05:46] GitHub Booth later on but code scanning
[05:48] today allows you to detect
[05:49] vulnerabilities using Code ql which is
[05:52] our internal or propri language I guess
[05:55] but it's open source so you can actually
[05:57] build it your own queries yourself but
[06:00] with code scanning today it allows you
[06:01] to detect different vulnerable patterns
[06:03] across your code it'll find the data
[06:05] flow and be able to analyze that data
[06:07] flow to understand where the
[06:08] vulnerability is and what type of source
[06:11] and exploits you have within that
[06:13] vulnerability so that makes it super
[06:15] powerful especially when we talk about
[06:16] some of the AI aspects that we're adding
[06:18] to it because we have the context and we
[06:20] have that information in there with code
[06:22] qall today there are more
[06:25] than I don't even know how many query
[06:27] packs that we offer internally or from
[06:29] the GitHub side but we also bring in
[06:31] that community so anything that we do is
[06:33] community backed and sorry I keep
[06:35] hitting the mic but anything that we do
[06:37] is community back so when we talk about
[06:38] code ql it's not just our queries it's
[06:40] Microsoft queries it's Google's queries
[06:42] it's Uber's queries and so forth and we
[06:44] build that aspect of community in even
[06:47] insecurity just because we know there's
[06:49] never going to be GitHub is going to
[06:51] answer every single question that you
[06:52] may have especially for the companies
[06:54] that you work for the other aspect of
[06:56] cod scanning is to incorporate third
[06:58] party Integrations so again this is
[07:00] where our vendor and partnership comes
[07:01] through so if you're using something
[07:03] like container scanning code scanning
[07:05] today code ql specifically is more focus
[07:07] on SAS we're not going to do container
[07:09] scanning today at least not in the near
[07:12] future so why not incorporate some of
[07:13] the results back into your P request and
[07:15] get that information and feedback sooner
[07:18] than later so that's an aspect of
[07:20] thirdparty Integrations code scanning
[07:21] infrastructures code scanning uh sorry
[07:24] um uh container scanning infrastructure
[07:26] as code scanning or any other third
[07:27] parties that you want to integrate with
[07:29] you can do that through siif inputs
[07:31] through code
[07:32] scanning the biggest win which all my
[07:34] customers have loved and I don't know if
[07:36] you felt it if you're doing even open-
[07:38] Source work is secret scanning secret
[07:41] scanning is a lifesaver in many many
[07:44] cases how many times has somebody
[07:47] accidentally left some you know Secrets
[07:50] maybe AWS or azak keys in there in their
[07:53] log file without realizing and you know
[07:56] it happens you do a test file and you
[07:59] forget to chit your get ignore it saves
[08:02] it saves a lot of Bitcoin miners uh
[08:05] being spun up within your environment so
[08:08] secret scanning does a full-blown
[08:09] analysis of Secrets across your
[08:11] repositories from API keys to your own
[08:14] custom secrets and using AI that I'll be
[08:17] talking about in a little bit on how to
[08:19] detect other types of secrets that are
[08:21] just plain text but really hard to
[08:24] reduce the amount of false positives on
[08:25] them AI can really help with that so
[08:27] with secret scanning it's been the
[08:28] biggest win of Ross all of my customers
[08:30] and it's been a big big discussion on
[08:32] how do we prevent things but also how do
[08:35] we reactively and proactively prevent
[08:38] things so proactively what we have
[08:40] Incorporated was push protection so it
[08:42] allows you to block any pushes that are
[08:44] coming to the GI ecosystem before the
[08:47] secret is being exposed or before it
[08:49] goes into your G commit history so then
[08:51] you can you would have to revoke it at
[08:52] that point but what's is in your G
[08:54] commit history we don't recommend
[08:55] deleting anything in your G commit
[08:57] history especially if you work for a
[08:59] regular related industry that goes
[09:00] through Audits and has to maintain a lot
[09:03] of historical aspects very uh precisely
[09:06] that's where we just recommend hey we
[09:08] are able to detect not only your current
[09:10] state but all your G history and other
[09:12] issues pool requests comments and pool
[09:14] requests and so forth if there's any
[09:16] secrets in those and we really recommend
[09:19] revoking them and last but not least
[09:22] supply chain security if you have maybe
[09:25] heard of it as dependabot is one of the
[09:27] tools within the supply chain security
[09:29] aspect of it dependabot allows you to
[09:31] detect dependencies that are vulnerable
[09:33] today so with dependabot it gives you an
[09:36] opportunity to say hey I found
[09:38] vulnerabilities for these dependen or
[09:40] found that these dependencies are
[09:41] vulnerable so maybe we need to upgrade
[09:43] to the latest version there's going to
[09:44] be some additional AI components are
[09:46] being added to that as well but that's
[09:47] something that I won't be covering as
[09:49] much today because that's still early
[09:51] earlier on in the stages
[09:53] there some of our secret scanning
[09:55] partners that we work with today are
[09:58] very much common
[10:00] vendors that you might be working with
[10:01] throughout the your day-to-day but this
[10:04] is where again we talk about the
[10:05] community and the vendors and the
[10:06] partners that we're work with because
[10:08] what we do is for secret scanning is not
[10:10] only incorporate their patterns but we
[10:13] also push them to improve how they're
[10:14] doing their patterns to make sure that
[10:16] their vulnerability their their secrets
[10:18] are in in general are not going to
[10:21] create a lot of false positives so we
[10:23] create a kind of like a mechanism for
[10:25] them to add hashes and more kind of more
[10:27] specific information to be able to to
[10:29] detect these secrets almost at 99% 99.9
[10:33] something per I don't know the exact
[10:35] average that we have today but it's
[10:37] pretty high up there and it reduces the
[10:38] amount of false positives so
[10:40] significantly when you use some of our
[10:42] high U High Fidelity partners that we
[10:44] work
[10:47] with so at any given point in time
[10:50] GitHub really believes security should
[10:51] be part of the day-to-day
[10:53] responsibilities of everybody it's a
[10:55] shared responsibility it's never just
[10:57] absc saying hey you need to to fix these
[11:00] uh these 10 vulnerabilities by tomorrow
[11:03] or else we can't deploy it's never just
[11:05] uh you know the developer trying to
[11:07] figure out how to fix this vulnerability
[11:09] that they've never even heard of or
[11:10] maybe not even understand to then be
[11:13] able to deploy on time so it's should be
[11:15] more of a shared responsibility so our
[11:17] goal is to bridge that Gap and make that
[11:18] conversation a lot easier so anything
[11:20] that we do with Advanced security
[11:21] anything that we're doing with AI allows
[11:23] you to really add that aspect into
[11:26] it so what can AI do for us how can we
[11:30] benefit with sec how can AI benefit
[11:33] security with AI there's so much more
[11:37] that you can do especially with
[11:38] generative AI as you can see with
[11:39] co-pilot with all the new customers
[11:42] vendors partners that you're seeing here
[11:43] at this conference there's just so many
[11:45] aspects to it so the first couple things
[11:47] that we've noticed right off the bat is
[11:49] easier identification how can we help
[11:52] how can AI help us identify
[11:54] vulnerabilities or Secrets much easier
[11:57] how can we have faster REM mediation so
[12:00] when you identify things if you're not
[12:02] fixing them then what's the point of
[12:03] identifying them half the time right if
[12:05] you're not going to fix the
[12:06] vulnerabilities that's where the actual
[12:08] issue is it's easy to find
[12:10] vulnerabilities lately a lot more easier
[12:12] than they were before but fixing them is
[12:15] the actual issue and that's where the
[12:17] productivity aspect also comes into play
[12:19] and last but not least driving that
[12:21] productivity the faster you're able to
[12:22] fix V abilities the faster you're able
[12:24] to be a little more productive increase
[12:26] your like security risk postures of
[12:29] where your company may be today reduce
[12:31] the amount of you know turmoil that you
[12:34] have to hit uh you know by deploying
[12:36] earlier on with the fix rather than
[12:38] waiting till like production or after
[12:40] production or when a customer is using
[12:41] your product already but in general this
[12:44] is where AI we see AI really helping
[12:46] introduce a lot more of that um cap more
[12:51] of those capabilities so first but not
[12:54] the most important but it is probably
[12:56] the biggest one that we are very excited
[12:58] for is code scanning autofix with code
[13:02] scanning autofix not only are we helping
[13:04] detect vulnerabilities with Cod scanning
[13:07] but now we're providing a way to autofix
[13:09] those with AI so in the PO request as
[13:12] you're working actively it will actually
[13:14] provide a response back to say hey maybe
[13:18] you should be fixing this vulnerability
[13:19] this specific way and it'll give you a
[13:22] suggestion obviously it's AI so it's
[13:23] going to give you a suggestion of what
[13:25] it thinks based on the context it has
[13:27] you can always edit it you can always
[13:28] fix it or you can commit and rerun your
[13:30] test and see if it actually fix fixes
[13:32] that vulnerability with code scanning
[13:34] autofix code ql is what's providing a
[13:37] lot of that context so coo is finding
[13:39] the data flow uh of that vulnerability
[13:41] you're getting information of what that
[13:43] vulnerability common fixes are when
[13:45] you're doing code scanning so providing
[13:47] that context and the way that we are
[13:48] doing our backend system to prompt that
[13:51] request it's actually providing really
[13:53] really good autofix result from our
[13:56] customers and from all of my customers
[13:57] that have tested this today
[13:59] they found that autofix has been pretty
[14:01] successful for I don't know maybe 70% of
[14:04] their use cases but again this is going
[14:06] to only get better as we're working with
[14:09] more customers as more people are
[14:11] starting to test this out and it's in
[14:12] public beta today so you can actually
[14:14] test this out yourself you're
[14:16] interested second to this is the secret
[14:20] skinning improvements some of the
[14:22] aspects of creating a custom pattern
[14:24] requires a lot of work I mean I don't
[14:26] know who knows reject to the point where
[14:29] they they can they feel conf confident
[14:32] rolling out a red uh scan across all
[14:35] your repositories right I personally
[14:38] cannot claim that I do uh my Rex I mean
[14:42] it's not bad but it's not the best that
[14:44] it can be so why not help a uh have ai
[14:47] help us custom generate those rexes so
[14:49] with custom pattern generation you can
[14:51] provide AI um capabilities to uh maybe
[14:54] suggest a different way to write some of
[14:56] your rexes so you can provide samples
[14:58] and examples of what you're looking for
[15:00] and then AI or secret SC or secret
[15:03] scanning custom pattern generation will
[15:04] generate a custom pattern for you to at
[15:06] least have a starting point if you don't
[15:09] think that's the full answer just yet
[15:11] but it generates that custom pattern and
[15:13] it makes it so much easier to give more
[15:15] and more examples because the more
[15:16] context it has the better answer it will
[15:18] provide and it will generate a response
[15:20] back so you don't have to figure out how
[15:21] to write this Nuance search for this
[15:24] type of Rex to find a custom pattern
[15:26] this has simplified the process so much
[15:29] and a lot of our customers have loved
[15:30] loved loved having this capability
[15:32] because they were doing that anyway
[15:34] probably on chat gbt or maybe going to
[15:36] copilot in their IDE or maybe they were
[15:39] doing this on Google and trying to
[15:40] figure out a cheat sheet with Rex's like
[15:42] there was so much work that was being
[15:43] done just to generate that now you can
[15:45] just have somebody alongside with you
[15:48] like a co-pilot to help you generate
[15:50] that custom
[15:51] secret and last but not least actually I
[15:54] think this is one of the most important
[15:56] ones from a secret scanning perspective
[15:58] is to detect unstructured passwords how
[16:01] often do you have password equals I mean
[16:04] very uh very often let me tell you let
[16:06] me give you that answer very often how
[16:08] often is that actually vulnerable is
[16:10] that a real password is that actually
[16:12] being exploited uh probably not very
[16:15] often uh probably way less often than
[16:18] how often you have password equals
[16:20] somewhere but there's so many types of
[16:22] unstructured passwords like that where
[16:24] you can define a password of sorts but
[16:26] never know if it's actually being
[16:27] exploited so what what we're doing we're
[16:29] doing an think of it as an AI analysis
[16:31] of the repository to understand if that
[16:33] password is a true positive so what
[16:36] we're doing is finding passwords and we
[16:38] label them today as other because they
[16:40] are definitely going to have some false
[16:43] positive in them in the first iteration
[16:45] of this but it's going to identify those
[16:47] passwords and make it easier for you to
[16:48] say hey these are actually vulnerable
[16:50] passwords that we have exposed in our G
[16:52] history so we need to revoke them rotate
[16:55] them and start storing them in our
[16:56] Hazard Vault or Azure key Vault or
[16:58] wherever we want to this is going to be
[17:01] such a game changer in terms of like
[17:03] passwords that are internal to your
[17:04] company this is going to be a game
[17:06] changer for passwords that aren't really
[17:08] very structured in general that allow
[17:10] you to um do things that you shouldn't
[17:12] be you shouldn't be storing in a in a g
[17:15] Hip git repository um but this is again
[17:18] where it's a way of AI helping finding
[17:23] and discovering easier much more easily
[17:25] than you could have before so the easier
[17:28] uh easier than ification faster
[17:30] remediation so the easier you can
[17:32] identify the faster you can remediate it
[17:35] but let's go into a
[17:38] demo so I have about maybe like 10
[17:41] minutes left here so really quickly I
[17:43] kind of want to just start off with a
[17:45] GitHub repository here or a GitHub
[17:46] organization here you can see there's a
[17:49] security tab at the top of your GitHub
[17:51] organization if you have admin access or
[17:53] if you're a there's a security manager
[17:55] role as well you'll be able to see the
[17:57] security tab if you have get Advance
[17:59] Security on it will actually give you a
[18:00] lot more information if you don't you'll
[18:02] have some dependabot information going
[18:04] on here but this security tab gives you
[18:06] an overview of all the information that
[18:08] you have across this organization so in
[18:10] this example here what you're seeing is
[18:12] that there's so many open alerts this is
[18:14] our demo repository this is a production
[18:16] code so do not worry this is not going
[18:19] to be deployed anywhere in Azure but uh
[18:21] we are we are safe for today but
[18:24] nonetheless 73,000 alerts is uh is a lot
[18:28] but you can identify these alerts and
[18:30] find more patterns of what's going on um
[18:32] based on the secrets if it's if it's
[18:34] Secrets being identified or if it's uh
[18:37] vulnerabilities from your SAS scanning
[18:39] or if it's vulnerabilities from your
[18:40] third party Integrations or if it's
[18:42] dependency vulnerabilities from
[18:44] dependabot so you can see a lot more
[18:46] information and statistics on hey what's
[18:48] the age of some of the alerts these
[18:50] alerts have been living for a long time
[18:52] what's the remediation time FR timeline
[18:54] how often are you remediating these how
[18:57] often are you actually resolving these
[18:59] and then you can understand the impact
[19:01] analysis of all the different
[19:02] repositories this is one of the views so
[19:05] my actual favorite view is the coverage
[19:07] view because the concern for a lot of
[19:10] customers is like how do we know what we
[19:12] don't know so in many cases people
[19:16] believe that they have full coverage of
[19:18] everything but it's usually done in CI
[19:20] in in the CI pipeline so you're not
[19:22] actually getting coverage unless you're
[19:24] going through a CI pipeline but there's
[19:26] so many more repositories that probably
[19:27] are just sitting there for just basic
[19:29] automation something else that you're
[19:31] just running that it's not going through
[19:32] your CI pipeline so you're never
[19:33] actually running security scanning
[19:35] across all of those so in this view here
[19:37] you can get a true identification of how
[19:40] many of your repositories are actually
[19:42] covered so you can see secret scanning
[19:44] code scanning and dependabot in many
[19:46] cases secret scanning is an easy
[19:48] oneclick button on so obviously there's
[19:50] just a lot more coverage across secret
[19:52] scanning 99% here we're hopefully going
[19:54] to get 100 at one point in time but for
[19:56] code scanning it's 57 what do need to do
[19:59] why why is it 57 does it make sense that
[20:01] should we not be scanning more things
[20:03] with code scanning and that's where I
[20:06] think this provides really the best
[20:07] value that's from an organization
[20:10] perspective or an admin or if you're
[20:11] security manager as a developer I want
[20:14] to go into my repository similar to your
[20:16] repository you can see a security tab
[20:18] here this security tab really allows you
[20:20] to understand what's going on across
[20:22] that specific repository so let's go
[20:24] into one of these here so I in my code
[20:27] scanning Repository here or sorry in my
[20:29] repository in the Cod scanning alerts
[20:31] here I can see all of the alerts listed
[20:34] out where I need to start fixing so this
[20:36] is a lot more reactive work we found
[20:38] these vulnerabilities how can we start
[20:40] fixing them we have a big backlog we
[20:41] have some tech de this is a place where
[20:43] I am going to go and understand what's
[20:45] going on so then I can go fix those so
[20:47] when I go into one of them for instance
[20:49] actually let's go into this one here
[20:52] when we go into one of them for instance
[20:54] we can see specifically what the
[20:55] vulnerability is so if we click on show
[20:57] paths you you can see from Source all
[21:00] the way down to the sync of what that
[21:01] vulnerability is so as a developer I can
[21:04] understand that where I need to start
[21:06] fixing these vulnerabilities but in many
[21:09] cases there's more than one way to an
[21:11] exploit there's more than one way to get
[21:14] to that exposure point so how do we
[21:16] under identify that and understand that
[21:18] that's where Cod does really well it
[21:19] identifies all the different paths so if
[21:21] I go into maybe step eight it looks like
[21:23] there's a different Source but it's the
[21:25] same sync in this example so why not fix
[21:29] of vulnerability in Step seven so then I
[21:30] can find the common denominator across
[21:32] all of those so that is the more
[21:35] reactive work what we really want to do
[21:38] with AI is to be more proactive so now I
[21:41] am in a pool request I not me but Mr
[21:45] left right left here actually introduce
[21:47] a vulnerability in this vulnerability he
[21:50] let's see what the vulnerability is
[21:52] cross-site scripting so he introduced on
[21:53] crossy scripting easy mistake to make
[21:55] very common vulnerability usually an
[21:58] easy fix but as a developer I never
[22:00] really knew what it was so I can get a
[22:02] better understanding of what that is so
[22:04] depend uh uh Advanced Security will
[22:05] actually tell you hey this is the
[22:06] vulnerability this is the information
[22:08] around that vulnerability but the
[22:10] autofix aspect actually be very specific
[22:12] so this specific solution is to this
[22:15] vulnerability so now before you even
[22:17] merge your code into your production
[22:20] main branches develop branches you can
[22:22] get results and an answer back on how to
[22:25] resolve that vulnerability so finding
[22:27] that vulnerability and remediating it
[22:29] all within the PO request and that's the
[22:31] power of AI in this case so in this
[22:33] example here it's asking to install the
[22:35] um Escape HTML library and import that
[22:38] in and actually that resolves your
[22:39] vulnerability fairly easily but it could
[22:41] have saved me like a couple minutes a
[22:44] couple hours a couple days depending on
[22:46] how much I knew about this P request or
[22:48] how much I knew about the code or how
[22:49] much I understood from this
[22:50] vulnerability to actually make that fix
[22:52] in this case it took me just reading
[22:55] through this and I want to make sure I
[22:57] obviously I'm still the develop I still
[22:59] want to do my analysis understand if I
[23:01] if it's the right answer but I can then
[23:03] decide to commit that fix and as soon as
[23:05] I commit that fix it will rerun all the
[23:07] scans so we can see if that
[23:08] vulnerability is actually remediated
[23:09] right off the bat so that's our Ai
[23:12] autofix and I know we have a only like
[23:15] one more minute left but at the end of
[23:17] the day what we really want to show is
[23:18] how AI can really improve that
[23:20] experience and this is just one example
[23:22] and the more examples are if we're
[23:24] generating some Secrets I can show that
[23:26] at the Microsoft Booth if you want to
[23:27] stop by later on um generating the
[23:30] secrets with AI detecting other types of
[23:32] secrets with AI I can show all of that
[23:34] at the Microsoft Booth later on awesome
[23:36] thank you
[23:38] [Music]
