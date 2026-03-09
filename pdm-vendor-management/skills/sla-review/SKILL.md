# Skill: sla-review

## Purpose
Review a vendor's SLA performance against contractual commitments — and determine what actions to take when breaches occur.

## When to Use
- Monthly or quarterly vendor review
- After a production incident involving a vendor
- Before renewing a vendor contract

## Framework: SLA Review

### Step 1 — Gather Data
Ask for:
- SLA document or commitments
- Actual performance data for the review period
- Incident reports involving the vendor

### Step 2 — SLA Performance Table

| SLA Metric | Committed | Actual | Met? | Incidents |
|-----------|-----------|--------|------|-----------|
| Uptime | 99.9% | 99.6% | ❌ | 2 outages |
| P1 Response Time | < 1 hour | 2.3 hours avg | ❌ | 4 breaches |
| P2 Response Time | < 4 hours | 3.8 hours avg | ✅ | 0 breaches |
| Deployment notification | 48 hrs notice | 24 hrs avg | ❌ | 3 breaches |

### Step 3 — Breach Classification
- **Minor breach**: 1 incident, < 10% variance → Log and monitor
- **Moderate breach**: 2–3 incidents or 10–25% variance → Formal notice
- **Critical breach**: 4+ incidents or > 25% variance → Escalate to contract management, consider remedies

### Step 4 — Recommended Actions

| Breach Level | Action |
|-------------|--------|
| Minor | Document and include in next QBR |
| Moderate | Send formal breach notice, request remediation plan |
| Critical | Invoke SLA credits, request executive escalation, review contract exit clauses |

### Step 5 — Vendor Review Meeting Agenda
1. Present performance data (objective, not accusatory)
2. Acknowledge any mitigating factors
3. Request vendor's root cause and remediation plan
4. Agree improvement targets for next period
5. Document commitments

## Output Format
1. SLA performance table
2. Breach classification and severity
3. Recommended actions
4. Vendor review meeting agenda
5. Suggested next command: `/vendor-communication` or `/risk-register`
