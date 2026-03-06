# Skill: vendor-assessment

## Purpose
Evaluate a new vendor or third-party integration for delivery readiness — before committing to include them in a release plan.

## When to Use
- Onboarding a new vendor or SaaS integration
- Evaluating a third-party API for use in production
- Before including a vendor dependency in a release timeline

## Framework: Vendor Assessment

### Assessment Dimensions

**1. Technical Readiness** (Score 1–5)
- Is their API/product stable and production-ready?
- Is documentation complete and up to date?
- Do they have a sandbox or test environment?
- What are their uptime SLAs?

**2. Integration Effort** (Score 1–5)
- How complex is the integration? (days, not weeks = better)
- Do they have SDKs for our tech stack?
- Have other teams integrated with them before?

**3. Support Quality** (Score 1–5)
- What is their support response time SLA?
- Do they have a dedicated integration support contact?
- What is their escalation path for critical issues?

**4. Risk Profile** (Score 1–5, 5 = lowest risk)
- How long have they been in production?
- What is their customer base size?
- Are there known outages or reliability issues?
- What is their data security posture?

**5. Commercial / Legal** (Score 1–5)
- Is pricing clear and contractually locked?
- Are data processing agreements (DPAs) in place?
- What are the termination and portability clauses?

### Vendor Assessment Scorecard

| Dimension | Score /5 | Notes |
|-----------|---------|-------|
| Technical Readiness | | |
| Integration Effort | | |
| Support Quality | | |
| Risk Profile | | |
| Commercial / Legal | | |
| **Total** | **/25** | |

### Recommendation Thresholds
- 20–25: ✅ Proceed — low risk vendor
- 14–19: ⚠️ Proceed with conditions — list conditions
- < 14: ❌ Do not proceed — too risky for current release

## Output Format
1. Completed vendor scorecard
2. Recommendation with conditions (if applicable)
3. Risk mitigation plan for any scores < 3
4. Suggested next command: `/third-party-risk` or `/dependency-map`
