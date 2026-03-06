# Skill: post-launch-monitoring

## Purpose
Define a structured monitoring plan for the 72 hours after a release — with clear metrics, alert thresholds, escalation paths, and a stabilization criteria.

## When to Use
- During launch planning
- As part of the launch checklist
- After every production deployment

## Framework: Post-Launch Monitoring Plan

### Step 1 — Define Monitoring Window
- **Hyper-care period**: First 72 hours after launch
- **Extended monitoring**: Days 4–14 for gradual rollouts

### Step 2 — Key Metrics to Monitor

| Metric | Normal Baseline | Alert Threshold | Escalation Threshold |
|--------|----------------|-----------------|---------------------|
| Error rate | < 0.5% | > 1% | > 2% |
| p95 Response time | < 300ms | > 500ms | > 1000ms |
| Throughput | 1000 req/min | < 700 req/min | < 500 req/min |
| CPU / Memory | < 60% | > 80% | > 90% |
| Failed logins | < 5/min | > 20/min | > 50/min |
| Support tickets | Baseline | 2× baseline | 3× baseline |

### Step 3 — Monitoring Cadence

| Period | Check Frequency | Who |
|--------|----------------|-----|
| First 2 hours | Every 15 minutes | PDM + On-call Dev |
| Hours 2–24 | Every hour | On-call Dev |
| Day 2–3 | Every 4 hours | On-call Dev |
| Day 4–14 | Daily | PDM |

### Step 4 — Escalation Path
- Alert triggered → On-call Dev investigates (15 min)
- Cannot resolve in 15 min → Escalate to Tech Lead
- P0 confirmed → PDM notified, Incident declared
- Business impact → Stakeholder communication within 30 min

### Step 5 — Rollback Decision Criteria
Initiate rollback if:
- Error rate > 2% for > 10 minutes
- Any P0 data loss or security incident
- Service unavailable for > 5 minutes

### Step 6 — Stabilization Sign-Off
Release is stable when:
- 72 hours with no alerts triggered
- Error rate back to baseline
- No open P0/P1 bugs from the release
- Support tickets normalized

## Output Format
1. Monitoring metrics table with thresholds
2. Monitoring cadence schedule
3. Escalation path
4. Rollback decision criteria
5. Stabilization sign-off checklist
6. Suggested next command: `/lessons-learned` or `/delivery-report`
