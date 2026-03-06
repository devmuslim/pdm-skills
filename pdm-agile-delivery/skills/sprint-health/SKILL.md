# Skill: sprint-health

## Purpose
Assess the health of a sprint mid-way or at the end using delivery signals: velocity, burndown trend, blockers, morale, and scope changes.

## When to Use
- Mid-sprint check-in
- End of sprint review preparation
- When sprint is showing signs of distress

## Framework: Sprint Health Assessment

### Step 1 — Gather Sprint Data
Ask for:
- Sprint goal
- Planned story points / tickets
- Completed story points / tickets so far
- Days remaining in sprint
- Number of active blockers
- Any scope added after sprint start
- Team size

### Step 2 — Calculate Health Indicators

**Velocity Ratio** = Points Completed / Points Planned
- > 90%: ✅ Healthy
- 70–90%: ⚠️ At Risk
- < 70%: 🔴 Distressed

**Blocker Density** = Active Blockers / Team Size
- 0–0.3: ✅ Healthy
- 0.3–0.6: ⚠️ At Risk
- > 0.6: 🔴 High blocker load

**Scope Creep** = Points Added After Sprint Start / Original Points
- 0–5%: ✅ Stable
- 5–15%: ⚠️ Watch
- > 15%: 🔴 Scope at risk

**Burndown Projection**
Based on current pace, will the sprint complete on time?
- On track: ✅
- 1–3 days late: ⚠️
- 3+ days late or requires scope cut: 🔴

### Step 3 — Sprint Health Scorecard

| Indicator | Value | Status |
|-----------|-------|--------|
| Velocity Ratio | X% | ✅/⚠️/🔴 |
| Blocker Density | X | ✅/⚠️/🔴 |
| Scope Creep | X% | ✅/⚠️/🔴 |
| Burndown | On track / X days late | ✅/⚠️/🔴 |
| **Overall** | | ✅/⚠️/🔴 |

### Step 4 — Recommendations
Based on health indicators:
- If 🔴 Velocity: Identify top 2 items to cut or defer
- If 🔴 Blockers: Escalate top blocker to Scrum Master / PDM
- If 🔴 Scope Creep: Facilitate scope negotiation with PO
- If 🔴 Burndown: Recommend sprint scope adjustment or team discussion

### Step 5 — Sprint Goal At Risk?
Explicitly state: "The sprint goal IS / IS NOT at risk."
If at risk: recommend corrective action.

## Output Format
1. Sprint health scorecard
2. Sprint goal status
3. Top 3 recommended actions
4. Suggested next command: `/groom-backlog` or `/blocker-triage`
