# Skill: milestone-plan

## Purpose
Convert release scope and dependencies into a structured milestone plan with owners, dates, and buffer recommendations.

## When to Use
- After scope and dependencies are defined
- When creating a release timeline for stakeholders
- When managing a multi-team delivery

## Framework: Milestone Planning

### Step 1 — Gather Inputs
Ask for:
- Release scope (Must Haves from release-scope)
- Team size and sprint length
- Known constraints (holidays, freeze periods, external deadlines)
- Target release date

### Step 2 — Define Milestone Types

| Type | Purpose |
|------|---------|
| **Design Complete** | All UX/specs signed off, ready for development |
| **Development Complete** | All Must Have features merged to main |
| **Code Freeze** | No new features; only bug fixes allowed |
| **QA Complete** | All P0/P1 bugs resolved, regression passed |
| **UAT Sign-off** | Business approval received |
| **Release Candidate** | Build ready for production |
| **Go-Live** | Production deployment |
| **Stabilization End** | Monitoring period complete, team stands down |

### Step 3 — Milestone Table

| # | Milestone | Target Date | Owner | Dependencies | Status |
|---|-----------|-------------|-------|-------------|--------|
| M1 | Design Complete | Week 1 | Design Lead | Requirements finalized | ⬜ Pending |
| M2 | Dev Complete | Week 3 | Tech Lead | M1 + D1 | ⬜ Pending |
| M3 | Code Freeze | Week 4 | PDM | M2 | ⬜ Pending |
| M4 | QA Complete | Week 5 | QA Lead | M3 | ⬜ Pending |
| M5 | UAT Sign-off | Week 5 | Business Owner | M4 | ⬜ Pending |
| M6 | Go-Live | Week 6 | PDM + DevOps | M5 | ⬜ Pending |

### Step 4 — Buffer Recommendation
Based on risk register score:
- Low risk (score < 15): Add 10% buffer
- Medium risk (score 15–30): Add 20% buffer
- High risk (score > 30): Add 30% buffer or split release

### Step 5 — Text-Based Timeline
```
Week 1  ████ Design Complete
Week 2  ████████ Dev Sprint 1
Week 3  ████████ Dev Sprint 2 → Dev Complete
Week 4  ████ Code Freeze | QA Begins
Week 5  ████████ QA Complete → UAT Sign-off
Week 6  ██ Go-Live → Stabilization
```

## Output Format
1. Milestone table with owners and dates
2. Buffer recommendation with rationale
3. Text timeline
4. Suggested next command: `/launch-checklist` or `/assess-readiness`
