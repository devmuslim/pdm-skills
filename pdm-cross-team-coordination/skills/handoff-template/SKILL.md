# Skill: handoff-template

## Purpose
Produce a structured handoff document when work moves from one phase or team to the next — ensuring nothing is lost in translation.

## When to Use
- Dev → QA handoff
- QA → UAT handoff
- Feature team → Platform team handoff
- Old PDM → New PDM handoff

## Framework: Handoff Document

### Handoff Document Template

**Handoff**: [From] → [To]
**Date**: [Date]
**Feature / Release**: [Name]
**Handoff Owner**: [Name]
**Receiving Owner**: [Name]

---

**What is being handed off**
Brief description of the feature or work, and its purpose.

---

**What's complete**
- [List of completed items]
- Link to: Code repo / branch, Jira tickets, Design files

---

**What's NOT complete** (known gaps)
- [Item 1] — Reason / expected completion
- [Item 2] — Reason / expected completion

---

**Known Issues / Risks**
| Issue | Severity | Notes |
|-------|----------|-------|
| Edge case with null user data | P2 | Low priority, workaround documented |

---

**Environment Details**
- Feature available at: [URL / branch]
- Test credentials: [location of credentials]
- Test data: [description or link]

---

**What the receiving team needs to do**
1. [Step 1]
2. [Step 2]
3. [Step 3]

---

**Questions / Dependencies**
- [Open question 1] — Owner: [Name]
- [Dependency on Team X] — Status: [status]

---

**Handoff Accepted By**: _________________ Date: _______

## Output Format
1. Completed handoff document (ready for Confluence or email)
2. Checklist for receiving team
3. Suggested next command: `/test-plan` or `/uat-plan`
