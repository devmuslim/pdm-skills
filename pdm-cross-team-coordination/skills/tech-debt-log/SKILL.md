# Skill: tech-debt-log

## Purpose
Maintain a structured technical debt log that makes hidden delivery risk visible — and helps the team negotiate time to address it.

## When to Use
- When tech debt is slowing delivery velocity
- Sprint retrospective reveals recurring technical issues
- When presenting capacity trade-offs to stakeholders

## Framework: Technical Debt Log

### What Counts as Tech Debt?
- Code that works but is hard to change or extend
- Missing or inadequate test coverage
- Outdated dependencies or deprecated libraries
- Architecture shortcuts taken under time pressure
- Missing documentation for critical systems
- Fragile manual processes that should be automated

### Tech Debt Log Table

| # | Description | Area | Impact on Delivery | Estimated Effort | Priority | Added Date | Owner |
|---|------------|------|-------------------|-----------------|----------|-----------|-------|
| TD1 | Auth service has no unit tests | Auth | Any change to auth is risky | 5 days | High | [date] | Backend Lead |
| TD2 | Payment module uses deprecated API | Payments | Will break in 6 months | 3 days | Critical | [date] | Payments Team |
| TD3 | Deployment is manual, no CI/CD | DevOps | Slow releases, human error risk | 10 days | High | [date] | DevOps |

### Priority Classification

| Priority | Criteria |
|----------|---------|
| **Critical** | Will cause failure or security issue within 3 months |
| **High** | Slowing delivery by >20% or blocking new features |
| **Medium** | Causes friction but manageable |
| **Low** | Cosmetic or minor, no delivery impact |

### Negotiating Tech Debt Time
Use the "20% rule" recommendation:
> "We recommend allocating 20% of each sprint capacity to tech debt reduction — this is the minimum to prevent debt from growing faster than we pay it down."

Frame debt as delivery risk: "TD2 will break payments in 6 months. We recommend addressing it in the next 2 sprints."

## Output Format
1. Completed tech debt log
2. Top 3 priority items with business case
3. Recommended allocation (% of sprint)
4. Suggested next command: `/capacity-planning` or `/sprint-health`
