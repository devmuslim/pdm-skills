# Skill: blocker-triage

## Purpose
Classify, assign, and track delivery blockers systematically — so they are resolved quickly and don't accumulate silently.

## When to Use
- Daily standup preparation
- When sprint is falling behind due to blockers
- Weekly blocker review with team leads

## Framework: Blocker Triage

### Step 1 — Classify the Blocker

| Type | Definition | Resolution Owner |
|------|-----------|-----------------|
| **Technical** | Code, environment, or tooling issue | Tech Lead / Dev |
| **Dependency** | Waiting on another team's output | PDM (cross-team) |
| **Decision** | Needs a call that hasn't been made | Accountable party |
| **Resource** | Missing skill, person, or access | PDM / Manager |
| **External** | Vendor, legal, third-party | PDM / Escalate |

### Step 2 — Blocker Severity

| Severity | Impact | SLA to Resolve |
|----------|--------|----------------|
| 🔴 Critical | Stops sprint goal | Same day |
| 🟡 High | Slows 2+ team members | 24 hours |
| 🟢 Medium | Slows 1 person | 48 hours |

### Step 3 — Blocker Log

| # | Description | Type | Severity | Raised By | Owner | Raised Date | Target Resolution | Status |
|---|------------|------|----------|-----------|-------|-------------|------------------|--------|
| B1 | API docs unavailable from vendor | External | 🔴 | Dev | PDM | [date] | [date] | 🔄 In Progress |

### Step 4 — Escalation Trigger
If a blocker is:
- Open for > 2 days without progress → escalate to L2 (PDM)
- Open for > 4 days → escalate to L3 (Manager)
- Blocking the sprint goal → immediate escalation

## Output Format
1. Blocker log (ready for Confluence or Jira)
2. Escalation actions needed
3. Suggested next command: `/sprint-health` or `/escalation-framework`
