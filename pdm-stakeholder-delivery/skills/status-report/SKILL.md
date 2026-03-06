# Skill: status-report

## Purpose
Generate professional delivery status reports (weekly, monthly, or executive level) that communicate progress, risks, and decisions needed — without noise.

## When to Use
- Weekly team/stakeholder updates
- Monthly portfolio reviews
- Executive briefings on delivery health

## Framework: Structured Status Report

### Report Levels

#### Weekly Status Report
Audience: Team leads, direct stakeholders
Length: 1 page / ~300 words

Structure:
**1. Summary Line**
One sentence: overall RAG status + key message.
Example: "🟡 At Risk — Sprint 14 delivered 67% of planned scope; API integration delayed by 2 weeks."

**2. Progress (What we did)**
- 3–5 bullet points: what was completed this week
- Reference specific features, tickets, or milestones

**3. Planned (What's next)**
- 3–5 bullet points: what's planned for next week
- Include owners where relevant

**4. Risks & Blockers**
- List active blockers with owner and ETA to resolve
- List risks that escalated or are newly identified

**5. Decisions Needed**
- Explicit asks from stakeholders (approvals, prioritization calls, resource decisions)

**6. Metrics Snapshot**
| Metric | This Week | Last Week | Target |
|--------|-----------|-----------|--------|
| Velocity | 28 pts | 35 pts | 40 pts |
| Open Blockers | 3 | 5 | 0 |
| Test Pass Rate | 91% | 88% | >95% |

---

#### Executive Summary
Audience: C-suite, steering committee
Length: Half page / ~150 words

Structure:
- **Status**: 🟢 On Track / 🟡 At Risk / 🔴 Off Track
- **Release Date**: Confirmed / At Risk (new date: X)
- **Budget**: On Budget / Over by X%
- **Top Risk**: One sentence
- **Decision Needed**: One ask (if any)

---

### RAG Status Definitions
- 🟢 **On Track** — Delivery within plan, no major blockers
- 🟡 **At Risk** — Issues identified, recovery plan in place
- 🔴 **Off Track** — Significant delay or blocker without resolution

## Output Format
1. Formatted status report (ready to paste into email or Confluence)
2. RAG summary
3. Decisions needed (highlighted)
4. Suggested next command: `/handle-delay` (if 🟡/🔴) or `/steering-deck`
