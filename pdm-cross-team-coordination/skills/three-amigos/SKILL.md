# Skill: three-amigos

## Purpose
Facilitate a Three Amigos session — a structured conversation between Product (PM/PDM), Development, and QA to align on scope, approach, and edge cases before a story enters the sprint.

## When to Use
- Before sprint planning for complex stories
- When a story has unclear acceptance criteria
- When Dev and QA have different understandings of scope

## Framework: Three Amigos Session

### The Three Perspectives

| Role | Primary Question | Focus |
|------|----------------|-------|
| **Product (PDM/PM)** | What problem are we solving? | Business value, user need |
| **Development** | How will we build this? | Technical approach, feasibility |
| **QA** | How could this go wrong? | Edge cases, failure modes |

### Session Structure (30–45 Minutes)

**5 min — Story Read-Through**
PDM reads the story and acceptance criteria aloud.
No discussion yet.

**10 min — Dev Perspective**
- How would you approach building this?
- What technical risks or unknowns exist?
- Are there dependencies or constraints?

**10 min — QA Perspective**
- What edge cases should we test?
- What could break for users?
- What data variations need testing?

**10 min — Product Clarifications**
- Does the Dev approach match the intent?
- Are the edge cases in or out of scope?
- Update acceptance criteria based on discussion

**5 min — Agree and Close**
- Confirm: story is Ready (or needs more work)
- Capture: any new acceptance criteria, risks, or tasks added
- Estimate: update story points if complexity changed

### Three Amigos Output

| Item | Before Session | After Session |
|------|---------------|--------------|
| Acceptance Criteria | 2 scenarios | 5 scenarios (3 added) |
| Story Points | 5 | 8 (complexity discovered) |
| New Tasks | — | Add spike for null-state handling |
| Status | Not Ready | ✅ Ready |

## Output Format
1. Three Amigos session agenda
2. Updated acceptance criteria
3. New tasks or risks identified
4. Story Ready status
5. Suggested next command: `/acceptance-criteria` or `/backlog-grooming`
