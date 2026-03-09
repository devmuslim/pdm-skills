# Skill: lessons-learned

## Purpose
Document and share lessons learned after a release — so the team and organization benefit from experience, and the same mistakes aren't repeated.

## When to Use
- Within 2 weeks after every major release
- After a failed or significantly delayed delivery
- As input to the next release planning cycle

## Framework: Lessons Learned Document

### Step 1 — Gather Input
Collect from: retrospective outputs, post-mortem reports, PDM notes, team feedback.

### Step 2 — Lessons Learned Document

**Release / Programme**: [Name]
**Period**: [Start date] – [End date]
**Prepared By**: [PDM Name]
**Date**: [Date]

---

**What Went Well** ✅
Document practices to repeat:
- [Example: Early dependency mapping prevented 3 integration issues]
- [Example: Three Amigos sessions reduced bug count by 30%]

---

**What Didn't Go Well** ❌
Document issues without blame:
- [Example: App Store review timeline underestimated — caused 2-week delay]
- [Example: UAT environment was not stable — slowed business testing]

---

**Lessons Learned**

| # | Lesson | Category | Recommendation | Owner | Apply From |
|---|--------|----------|---------------|-------|-----------|
| L1 | App Store review takes 10–14 days, not 5 | Planning | Add 2-week buffer for all mobile releases | PDM | Next release |
| L2 | UAT env needs dedicated infra — shared env caused conflicts | Quality | Provision dedicated UAT environment | DevOps | Q3 |
| L3 | Weekly stakeholder pulse caught concerns early | Comms | Continue monthly pulse surveys | PDM | Ongoing |

---

**Metrics Comparison**

| Metric | Planned | Actual | Variance |
|--------|---------|--------|---------|
| Release date | Jun 30 | Jul 14 | +14 days |
| Scope delivered | 100% | 87% | -13% |
| P0 bugs post-launch | 0 | 2 | +2 |
| Team NPS | — | 7.2/10 | — |

---

**Recommendations for Next Release**
1. [Specific change to planning process]
2. [Specific change to quality process]
3. [Specific change to stakeholder management]

## Output Format
1. Full lessons learned document (ready for Confluence)
2. Action items for next release planning
3. Suggested next command: `/plan-release` or `/risk-register`
