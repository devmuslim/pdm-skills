# Skill: change-request

## Purpose
Generate a formal change request document when a delivery commitment needs to change — scope, timeline, or budget — requiring stakeholder approval.

## When to Use
- Release date needs to move
- Significant scope must be added or removed
- Budget overrun requires additional funding approval

## Framework: Change Request

### Change Request Template

**Change Request ID**: CR-[number]
**Date Submitted**: [Date]
**Submitted By**: [PDM Name]
**Approval Required From**: [Name / Role]
**Decision Needed By**: [Date]

---

**Change Summary** (one sentence):
> "Request to [extend timeline by 3 weeks / add Feature X to scope / increase budget by $50K] for [Release Name]."

---

**Current Baseline**:
- Scope: [description]
- Timeline: [committed date]
- Budget: [committed amount]

**Proposed Change**:
- Scope: [new scope description]
- Timeline: [new date]
- Budget: [new amount]

---

**Reason for Change**:
[2–3 sentences explaining what changed and why.]

**Impact of NOT Approving**:
[What happens if this change is rejected — business risk, quality risk, team impact.]

**Impact of Approving**:
[What downstream effects the change has — other projects, teams, customers.]

---

**Options**:
| Option | Description | Impact |
|--------|-------------|--------|
| A | Approve as requested | Timeline extends, quality maintained |
| B | Partial approval (scope only) | Date holds, scope reduced |
| C | Reject | Current plan maintained, quality risk accepted |

**Recommended Option**: [A/B/C with rationale]

---

**Approval**:
Approved / Rejected / Deferred by: _______________ Date: _______________
Comments: _______________

## Output Format
1. Completed change request document (ready for signature)
2. Summary email to accompany the formal document
3. Suggested next command: `/status-update` or `/steering-deck`
