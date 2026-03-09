# Skill: uat-plan

## Purpose
Design a structured User Acceptance Testing (UAT) plan with scenarios, participants, timelines, and sign-off criteria — so business approval is earned, not assumed.

## When to Use
- 1–2 weeks before planned release
- When building features for specific business users
- When regulatory or contractual sign-off is required

## Framework: UAT Plan

### Step 1 — Define UAT Scope
Ask for: which features require business validation this release?

### Step 2 — Participant Selection

| Role | Name | Area to Test | Availability |
|------|------|-------------|-------------|
| Business Owner | [Name] | End-to-end flow | Week 5, Mon–Wed |
| Power User | [Name] | Edge cases | Week 5, Tue–Thu |
| Compliance | [Name] | Regulatory requirements | Week 5, Mon |

### Step 3 — UAT Scenarios

For each feature, write business-language scenarios (not technical):

**Feature: New Reporting Dashboard**

| # | Scenario | Steps | Expected Result | Pass/Fail | Tester | Date |
|---|----------|-------|----------------|-----------|--------|------|
| U1 | View monthly sales report | Log in → Reports → Monthly → Select March | Table shows correct data, downloadable | | | |
| U2 | Filter by region | Apply "EMEA" filter | Data filtered to EMEA only | | | |
| U3 | Export to Excel | Click Export → Excel | File downloads with correct data | | | |

### Step 4 — UAT Environment
- Use production-like data (anonymized)
- Dedicated UAT environment — no dev changes during UAT
- Clear test data setup and cleanup plan

### Step 5 — Sign-Off Criteria
UAT passes when:
- All P0 scenarios: ✅ Pass
- All P1 scenarios: ✅ Pass or documented accepted risk
- Business Owner signs the UAT sign-off document

### Step 6 — Sign-Off Document Template

> "I, [Name], as [Role], confirm that I have tested the following features in the UAT environment:
> [Feature list]
> All critical scenarios have been validated and I approve this release to proceed to production.
> Signed: _______________ Date: _______________"

## Output Format
1. UAT plan with scenarios and sign-off table
2. Environment setup checklist
3. Sign-off document template
4. Suggested next command: `/assess-readiness` or `/launch-checklist`
