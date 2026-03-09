# Skill: quality-gates

## Purpose
Define formal quality gates between delivery phases — so teams don't proceed to the next phase until the current one meets agreed standards.

## When to Use
- Setting up a new delivery process
- When bugs keep escaping to production
- When UAT or release keeps failing due to upstream quality issues

## Framework: Quality Gates

### Standard Delivery Gates

**Gate 1: Dev → QA (Code Ready)**
Criteria to pass:
- [ ] All unit tests passing (>80% coverage)
- [ ] Code reviewed and merged
- [ ] No known P0 bugs
- [ ] Feature available in staging environment
- [ ] Developer has tested their own code

**Gate 2: QA → UAT (QA Complete)**
Criteria to pass:
- [ ] All acceptance criteria tested
- [ ] No open P0 or P1 bugs
- [ ] Regression suite > 95% pass rate
- [ ] Performance within SLA (if applicable)
- [ ] QA Lead sign-off

**Gate 3: UAT → Release Candidate (Business Approval)**
Criteria to pass:
- [ ] All UAT scenarios passed
- [ ] Business Owner sign-off received
- [ ] Legal/compliance approval (if required)
- [ ] No new P0/P1 bugs since QA sign-off

**Gate 4: Release Candidate → Production (Go-Live)**
Criteria to pass:
- [ ] All prior gates passed
- [ ] Rollback plan tested
- [ ] Monitoring and alerts configured
- [ ] On-call rotation confirmed
- [ ] Deployment window confirmed with stakeholders

### Gate Failure Protocol
If a gate is not passed:
1. Document which criteria failed
2. Return to previous phase for remediation
3. Re-test only failed criteria (not full regression unless P0 fix)
4. Gate re-evaluation within 24 hours

## Output Format
1. Four-gate quality framework with criteria
2. Gate failure protocol
3. Gate status tracker template
4. Suggested next command: `/launch-checklist` or `/assess-readiness`
