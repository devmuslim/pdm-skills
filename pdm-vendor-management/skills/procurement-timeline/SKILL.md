# Skill: procurement-timeline

## Purpose
Build a realistic procurement timeline for vendor onboarding, aligned to the delivery plan — so procurement never becomes the critical path.

## When to Use
- New vendor is required for a release
- Procurement is running in parallel with development
- Legal or security review is in the critical path

## Framework: Procurement Timeline

### Typical Procurement Steps and Durations

| Step | Typical Duration | Owner |
|------|----------------|-------|
| Vendor identification and shortlisting | 1–2 weeks | PDM / Procurement |
| RFP / RFI process (if required) | 3–6 weeks | Procurement |
| Vendor selection and negotiation | 2–4 weeks | Procurement / Legal |
| Contract review (internal legal) | 1–3 weeks | Legal |
| Security / InfoSec review | 1–3 weeks | InfoSec |
| Data Processing Agreement (DPA) | 1–2 weeks | Legal |
| Procurement approval | 1 week | Finance / Management |
| Contract signing | 1 week | Both parties |
| Technical onboarding / sandbox access | 1–2 weeks | Vendor + Dev team |
| **Total (worst case)** | **12–24 weeks** | |

### Step 1 — Calculate Procurement Start Date
Work backwards from when integration must be complete:
- Integration complete date: [date]
- Subtract: integration development time (X weeks)
- Subtract: procurement timeline (worst case from table above)
- = **Procurement must START by: [date]**

### Step 2 — Procurement Milestones Table

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Vendor selected | [date] | PDM | ⬜ |
| Contract to legal | [date] | Procurement | ⬜ |
| Security review complete | [date] | InfoSec | ⬜ |
| Contract signed | [date] | Both | ⬜ |
| Sandbox access granted | [date] | Vendor | ⬜ |
| Integration begins | [date] | Dev | ⬜ |

### Step 3 — Risk Flag
If procurement start date has already passed:
> ⚠️ "Procurement is on the critical path. A delay of more than X weeks will push the release date. Recommend starting procurement immediately and flagging to Steering Committee."

## Output Format
1. Procurement milestone table with start date calculation
2. Risk flag if timeline is tight
3. Escalation recommendation if needed
4. Suggested next command: `/dependency-map` or `/risk-register`
