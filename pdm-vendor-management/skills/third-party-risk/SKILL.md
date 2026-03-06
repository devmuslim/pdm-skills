# Skill: third-party-risk

## Purpose
Assess the delivery risk posed by a third-party dependency — and build contingency plans for when external parties don't deliver on time.

## When to Use
- When a release depends on a vendor or external team
- During risk register creation
- When a vendor signals potential delays

## Framework: Third-Party Risk Assessment

### Risk Dimensions

**Availability Risk** — Will they deliver on time?
- Do they have a track record of on-time delivery?
- Are there competing demands on their capacity?
- Is there a contractual commitment with penalties?

**Quality Risk** — Will their output meet our standards?
- Have we reviewed their test strategy?
- Will they provide documentation and support?
- Do we have acceptance criteria for their deliverable?

**Dependency Risk** — What happens if they're late?
- How many of our stories depend on their output?
- Can we decouple or mock their dependency?
- What is the cost of a 1-week / 2-week delay?

### Third-Party Risk Table

| Vendor / External | Dependency | Risk Level | Contingency Plan | Monitoring Cadence |
|-------------------|-----------|-----------|-----------------|-------------------|
| Payment Gateway API | Checkout feature | 🔴 High | Build mock for dev; parallelize QA using mock | Weekly check-in |
| App Store Review | Mobile release | 🟡 Medium | Submit 2 weeks early; prepare hotfix process | At submission |
| Legal (DPA sign-off) | Go-live | 🟡 Medium | Start review 4 weeks early; escalate at 2 weeks | Weekly |

### Contingency Strategies

| Strategy | When to Use |
|----------|------------|
| **Mock / Stub** | Build internal mock of external API to unblock development |
| **Early submission** | Submit to external parties earlier than needed |
| **Parallel workstream** | Continue development with mock while waiting |
| **Scope isolation** | Isolate dependent features — release rest without them |
| **Escalation agreement** | Agree in advance who escalates and when |

## Output Format
1. Third-party risk table
2. Contingency plans per vendor
3. Monitoring cadence
4. Suggested next command: `/risk-register` or `/dependency-map`
