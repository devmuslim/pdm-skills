# Skill: cut-scope

## Purpose
Analyze what can be deferred from a release without compromising its core value — and communicate those decisions clearly to stakeholders.

## When to Use
- Timeline is at risk and scope must be reduced
- Capacity is less than originally planned
- A blocker makes full delivery impossible

## Framework: Scope Cut Decision

### Principle
> "Cut scope, not corners. Never sacrifice quality to ship more. Ship less, ship well."

### Step 1 — Gather Current State
Ask for:
- Full list of items in scope
- Current MoSCoW classification
- Days/sprints remaining
- Current velocity vs planned velocity

### Step 2 — Scope Cut Criteria
Evaluate each item against:

| Criterion | Question |
|-----------|---------|
| **User Impact** | How many users does this affect? How severely? |
| **Business Commitment** | Is this promised to a customer, partner, or contractually required? |
| **Technical Dependency** | Does another Must Have depend on this? |
| **Effort Remaining** | How much work is left? Is it 20% or 80% done? |
| **Deferability** | Can it ship in the next release without significant rework? |

### Step 3 — Cut Decision Table

| Item | MoSCoW | % Done | User Impact | Deferrable? | Decision | Reason |
|------|--------|--------|------------|-------------|---------|--------|
| Feature A | Must | 90% | High | No | ✅ Keep | Nearly done, committed |
| Feature B | Should | 30% | Medium | Yes | ✂️ Cut | Low completion, high effort |
| Feature C | Could | 10% | Low | Yes | ✂️ Cut | Not started, defers cleanly |
| Feature D | Must | 60% | High | No | ⚠️ Escalate | Committed but at risk |

### Step 4 — Scope Cut Statement (Stakeholder Communication)
> "To protect the quality and timeline of [Release Name], we are deferring [Feature B] and [Feature C] to [Next Release]. These items are [X% complete / not started] and their deferral does not affect [core user flow / contractual commitments]. The remaining scope — [list Must Haves] — will deliver [core value statement] as planned on [date]."

### Step 5 — Deferred Items Backlog
Create a holding list for deferred items with:
- Reason for deferral
- Target release
- Owner for follow-up

## Output Format
1. Cut decision table
2. Items to keep vs cut vs escalate
3. Stakeholder communication statement
4. Deferred items backlog
5. Suggested next command: `/status-update` or `/handle-delay`
