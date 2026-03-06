# Skill: launch-checklist

## Purpose
Generate a comprehensive pre-launch checklist covering technical, communications, operations, and business readiness.

## When to Use
- 2–4 weeks before a planned release
- As part of release readiness assessment
- For go/no-go decision meetings

## Framework: Launch Readiness Checklist

### Step 1 — Gather Context
Ask for:
- Type of release (feature, hotfix, major version, platform migration)
- Audience (internal, external, B2B, B2C)
- Deployment environment (cloud, on-prem, mobile app store)
- Rollout strategy (big bang, phased, canary)

### Step 2 — Generate Checklist by Domain

#### 🛠 Technical Readiness
- [ ] All Must Have items completed and merged
- [ ] Code freeze enforced
- [ ] Regression test suite passed (>95% pass rate)
- [ ] Performance testing completed (load, stress)
- [ ] Security scan completed and vulnerabilities resolved
- [ ] Feature flags configured correctly
- [ ] Rollback plan documented and tested
- [ ] Database migrations tested in staging
- [ ] Monitoring and alerting configured
- [ ] On-call rotation confirmed for launch week

#### 📢 Communications Readiness
- [ ] Release notes written and reviewed
- [ ] Stakeholder announcement drafted
- [ ] Customer-facing changelog updated
- [ ] Support team briefed on new features
- [ ] Known issues documented

#### ⚙️ Operations Readiness
- [ ] Runbook updated
- [ ] Deployment pipeline validated in staging
- [ ] Deployment schedule confirmed
- [ ] Maintenance window communicated (if needed)
- [ ] SLA impact assessed

#### 👥 Business Readiness
- [ ] UAT sign-off received
- [ ] Legal/compliance approval obtained (if required)
- [ ] Training materials prepared
- [ ] Go/No-Go meeting scheduled

### Step 3 — Go / No-Go Assessment
For each domain, rate readiness:
- ✅ Ready
- ⚠️ At Risk (condition to meet before launch)
- ❌ Not Ready (blocker — must resolve before launch)

### Step 4 — Checklist Owner Assignment
Map each section to a responsible owner and deadline.

## Output Format
1. Full checklist by domain with checkboxes
2. Go/No-Go summary table
3. Blocker list (❌ items) with owners and deadlines
4. Suggested next command: `/assess-readiness` or `/plan-release`
