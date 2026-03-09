# Skill: test-strategy

## Purpose
Design a comprehensive test strategy for a release — covering test types, ownership, environments, entry/exit criteria, and tooling.

## When to Use
- Start of release planning
- When QA is being onboarded to a new feature
- When test coverage gaps are causing production bugs

## Framework: Test Strategy

### Step 1 — Test Pyramid

Define coverage targets:

| Layer | Type | Who | When | Coverage Target |
|-------|------|-----|------|----------------|
| Unit | Automated | Dev | During development | > 80% |
| Integration | Automated | Dev / QA | After unit tests pass | Key integration points |
| E2E / Functional | Automated + Manual | QA | After integration | Critical user journeys |
| UAT | Manual | Business Users | Before release | All Must Have features |
| Performance | Automated | QA / DevOps | Before code freeze | Peak load scenarios |
| Security | Automated scan | Security / DevOps | Before release | OWASP Top 10 |

### Step 2 — Test Environments

| Environment | Purpose | Refresh Cadence |
|-------------|---------|----------------|
| Dev | Developer testing | On demand |
| Staging | Integration + E2E | Daily |
| UAT | Business acceptance | Weekly |
| Pre-prod | Final validation | Per release |

### Step 3 — Entry and Exit Criteria

**Entry Criteria** (before QA begins):
- Story passes Developer's own testing
- Code reviewed and merged
- Feature available in staging

**Exit Criteria** (before release):
- All P0 and P1 bugs resolved
- Regression suite > 95% pass rate
- UAT sign-off received
- Performance tests within SLA

### Step 4 — Test Ownership Matrix

| Test Type | Owner | Reviewer |
|-----------|-------|---------|
| Unit | Dev | Tech Lead |
| Integration | Dev + QA | QA Lead |
| E2E | QA | PDM |
| UAT | Business | PDM |
| Performance | QA + DevOps | Tech Lead |

## Output Format
1. Test pyramid coverage plan
2. Environment setup table
3. Entry/exit criteria
4. Test ownership matrix
5. Suggested next command: `/uat-plan` or `/bug-triage`
