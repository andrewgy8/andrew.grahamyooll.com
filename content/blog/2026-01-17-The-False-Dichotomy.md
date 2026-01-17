---
title: Stop Separating People Problems from Engineering Problems
tags:
  - EngineeringManagement
  - career
---
In response to my recent post on [moving away from engineering management to individual contributor roles](../Try-to-Take-My-Position), someone asked me whether I'll miss solving people problems and only solving the technical engineer problems.

Judging by the look on their face, I think my answer surprised them. 

From my experience, there is no meaningful distinction between the two, at least not in any way that matters when you're actually trying to solve real problems.

The belief that you can specialize in one or the other, or that certain engineers are "people-focused" while others are "technically-focused," is one of the most persistent and counterproductive myths in software engineering.

# Engineering Problems Are People Problems

Consider this common scenario. 

Your service is experiencing performance degradation. The metrics are clearly saying database queries are the bottleneck. Testing confirms it and the technical diagnosis seems straightforward.

But when you dig deeper, you discover the real issue is someone chose a particular indexing strategy three years ago, optimizing for a use case that was later deprioritized and never shipped. The schema reflects assumptions that are no longer valid. The queries reflect constraints that no longer exist.

You will have to address this technically by throwing more hardware at it, rewrite the queries, migrate to a different database technology. But none of these solutions address the actual problem that architectural decisions were made under different constraints with different information.

The sustainable solution requires understanding why those decisions were made, who the stakeholders were, what constraints they were operating under, and how to prevent similar misalignments in the future. It requires building consensus around current priorities, communicating trade-offs clearly, and ensuring the right people are involved in future architectural decisions.

**The "technical" problem was always a coordination and communication problem in disguise.**

You don't solve this with more sophisticated technology. You solve it by being able to navigate organizational context, build alignment, and change minds. These are the skills typically categorized as "people skills."

# People Problems Require Engineering Solutions

Now let's take another scenario. 

Your engineering team is firefighting production incidents every week. On-call rotations are brutal. Engineers are burnt out. The team is starting to see retention issues. Team morale is deteriorating.

This looks like a classic people problem, and it is, in part. You need psychological safety, sustainable work practices, and support for your team. These are necessary interventions to keep the team afloat.

But if you stop there, you're treating symptoms while ignoring the underlying cause.

The sustainable solution requires engineering. Better observability so you catch issues before they become incidents, automated rollback mechanisms, feature flags, etc.

**You solve the people problem by engineering away the conditions that created it.**

Happy engineers need more than supportive culture. They need robust, well-designed systems that don't demand constant firefighting. Preventing burnout isn't just about work-life balance; it's about building technical systems that enable sustainable operations.

# Why This Matters

The distinction between "people problems" and "engineering problems" isn't just academic. It actively prevents effective problem-solving.

When you categorize a problem as purely technical, you miss the organizational and communication work required to solve it sustainably. When you categorize a problem as purely interpersonal, you miss the technical interventions that could eliminate it entirely.

The most effective engineers I've worked with don't choose between solving for people or solving for systems. They recognize that:

- **Technical excellence requires collaboration.** The best architecture in the world fails if you can't build consensus around it, communicate its trade-offs, or bring the right people along.
- **Healthy teams require solid technical foundations.** Culture alone can't compensate for systems that require constant heroics to keep running.
- **Most problems require both lenses.** The incident response problem needs better engineering _and_ better coordination. The architectural decision needs technical rigor _and_ stakeholder alignment.

# It's Both :)

If you believe you can specialize exclusively in "people problems" or "engineering problems," you'll consistently deliver incomplete solutions.

The database performance issue gets a band-aid fix instead of addressing the decision-making process that caused it. The burnout problem gets motivational talks instead of leading systemic improvements that would eliminate the root cause.

This doesn't mean every engineer needs to be equally strong in all dimensions. People have different strengths, and that's valuable. But it does mean that **recognizing when a problem requires both technical and interpersonal solutions is a core engineering skill**, not an optional specialization.

The best solutions almost always require both.