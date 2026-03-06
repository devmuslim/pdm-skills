# Skill: escalation-framework

## Purpose
Determine when, how, and to whom to escalate delivery issues — so the right people make decisions at the right time without unnecessary noise.

## When to Use
- A blocker cannot be resolved at team level
- A risk has materialized into an issue
- A decision requires authority beyond the PDM

## Framework: Escalation Decision

### Step 1 — Assess the Issue
Ask:
- What is the issue?
- What is the business impact if unresolved?
- What is the urgency (hours / days / weeks)?
- What has already been tried?
- Who owns the resolution?

### Step 2 — Escalation Levels

| Level | Who | When to Use |
|-------|-----|------------|
| **L1 — Team** | Tech Lead, QA Lead, Team members | Blocker within team's control |
| **L2 — PDM** | You | Cross-team blocker, resource conflict |
| **L3 — Sponsor / Manager** | Your manager, Programme Manager | Budget, headcount, or priority decision |
| **L4 — Steering Committee** | Executives, stakeholders | Release go/no-go, major scope change, budget overrun |
| **L5 — External** | Vendor, legal, regulatory body | Third-party issues outside the org |

### Step 3 — Escalation Decision Tree

```
Is the issue resolvable within the team?
  YES → L1 — resolve at team level
  NO ↓
Does it require cross-team coordination or resource?
  YES → L2 — PDM escalates
  NO ↓
Does it require a priority or budget decision?
  YES → L3 — Manager/Sponsor
  NO ↓
Does it affect the release date or major commitments?
  YES → L4 — Steering Committee
  NO → Monitor and document
```

### Step 4 — Escalation Brief Template
When escalating, always provide:

**Issue**: [One sentence description]
**Impact**: [What happens if not resolved — business, timeline, quality]
**Urgency**: [Decision needed by: date/time]
**What we've tried**: [Actions already taken]
**Options**: [2–3 options with trade-offs]
**Recommended option**: [Your recommendation]
**Ask**: [Explicit decision or action needed from this person]

### Step 5 — After Escalation
- Document the decision in the decision log
- Communicate outcome to relevant teams
- Update risk register status

## Output Format
1. Escalation level recommendation
2. Escalation brief (ready to send)
3. Decision log entry template
4. Suggested next command: `/decision-log` or `/status-update`
