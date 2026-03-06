# Skill: release-readiness

## Purpose
Assess team and product readiness for launch across 6 dimensions and produce a clear Go / No-Go recommendation.

## When to Use
- 1–2 weeks before planned release date
- After a delay or scope change
- As part of the Steering Committee update

## Framework: 6-Dimension Readiness Assessment

### Dimension 1 — Technical Readiness
Questions to ask:
- Is code freeze enforced?
- Has regression testing passed (target: >95%)?
- Is the rollback plan documented and tested?
- Are monitoring and alerts configured?

Score: 0–10

### Dimension 2 — Quality Readiness
- Are all P0 and P1 bugs resolved?
- Has UAT been completed and signed off?
- Has performance testing been run?

Score: 0–10

### Dimension 3 — Operational Readiness
- Is the runbook updated?
- Is the on-call rotation confirmed?
- Has the deployment pipeline been validated in staging?

Score: 0–10

### Dimension 4 — Communications Readiness
- Are release notes written and reviewed?
- Has the support team been briefed?
- Is the customer announcement ready?

Score: 0–10

### Dimension 5 — Business Readiness
- Is UAT sign-off received from business owners?
- Are legal/compliance approvals obtained?
- Is training material prepared?

Score: 0–10

### Dimension 6 — Team Readiness
- Is the team aware of launch responsibilities?
- Are key people available during launch window?
- Is there a clear incident commander for launch day?

Score: 0–10

---

## Readiness Scorecard

| Dimension | Score /10 | Status | Blockers |
|-----------|-----------|--------|---------|
| Technical | | ✅/⚠️/❌ | |
| Quality | | ✅/⚠️/❌ | |
| Operational | | ✅/⚠️/❌ | |
| Communications | | ✅/⚠️/❌ | |
| Business | | ✅/⚠️/❌ | |
| Team | | ✅/⚠️/❌ | |
| **Overall** | **/60** | | |

### Scoring Thresholds
- 54–60: ✅ **Go** — Ready to launch
- 42–53: ⚠️ **Conditional Go** — Launch with named conditions
- < 42: ❌ **No-Go** — Must resolve blockers first

## Output Format
1. Completed scorecard with scores and blockers
2. Go / No-Go recommendation with rationale
3. Conditions list (if Conditional Go)
4. Suggested next command: `/launch-checklist` or `/handle-delay`
