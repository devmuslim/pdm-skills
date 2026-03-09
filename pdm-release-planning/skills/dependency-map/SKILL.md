# Skill: dependency-map

## Purpose
Map all delivery dependencies — between teams, systems, and external parties — to surface the critical path and flag risks before they become blockers.

## When to Use
- Early in release planning
- When multiple teams are shipping together
- When integrating with third-party systems or vendors

## Framework: Dependency Mapping

### Step 1 — Gather Inputs
Ask for:
- Teams involved in the release
- External systems or APIs being integrated
- Third-party vendors or approval bodies (App Store, Legal, etc.)
- Known handoff points between teams

### Step 2 — Classify Dependencies

| Type | Definition | Example |
|------|-----------|---------|
| **Technical** | Code or API dependency between teams | Backend API needed by Mobile |
| **Data** | Data or schema dependency | Data team migration needed before Backend |
| **Infrastructure** | Shared infra dependency | DevOps environment needed by QA |
| **External** | Outside the organization | App Store review, vendor API |
| **Approval** | Sign-off or gate required | Legal, Compliance, Business UAT |

### Step 3 — Dependency Table

| # | From | To | Type | Description | Due Date | Risk Level |
|---|------|-----|------|-------------|----------|-----------|
| D1 | Backend | Mobile | Technical | WebSocket API contract finalized | Week 2 | 🔴 High |
| D2 | DevOps | QA | Infrastructure | Staging env with production data | Week 3 | 🟡 Medium |
| D3 | Mobile | Apple | External | App Store review submission | Week 4 | 🔴 High |
| D4 | QA | Business | Approval | UAT sign-off | Week 5 | 🟡 Medium |

### Step 4 — Critical Path
Identify the sequence of dependencies that determines the earliest possible release date.

Critical Path: D1 → D3 → D4

Earliest release date based on critical path: [calculated date]

### Step 5 — Dependency Risk Summary
- 🔴 High risk dependencies: [list] — Require immediate owner assignment
- 🟡 Medium risk: [list] — Monitor weekly
- External dependencies: Flag for Steering Committee

## Output Format
1. Dependency table
2. Critical path narrative
3. Risk summary with recommended actions
4. Suggested next command: `/risk-register` or `/plan-release`
