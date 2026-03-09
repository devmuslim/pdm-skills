# Skill: regression-plan

## Purpose
Build a targeted regression test plan that validates existing functionality is not broken by new changes — without testing everything every time.

## When to Use
- Before every release
- After a major code merge
- When a critical bug was found in production

## Framework: Risk-Based Regression

### Principle
Test everything would take forever. Test the right things based on risk.

### Step 1 — Identify Regression Scope
Ask for: what areas of the system were changed in this release?

### Step 2 — Risk-Based Area Selection

| Area | Change? | Risk Level | Include in Regression? |
|------|---------|-----------|----------------------|
| Authentication | No | High (always) | ✅ Always |
| Payments / Checkout | Yes | Critical | ✅ Full regression |
| User Profile | No | Medium | ✅ Smoke test only |
| Reporting | Yes | Medium | ✅ Targeted regression |
| Admin Panel | No | Low | ⚠️ Smoke test |
| Email notifications | No | Low | ❌ Skip this cycle |

### Step 3 — Regression Test Plan Table

| # | Test Area | Test Case | Priority | Type | Owner | Est. Time |
|---|-----------|-----------|----------|------|-------|----------|
| T1 | Login | SSO login success | P0 | Automated | QA | 5 min |
| T2 | Payments | Complete checkout flow | P0 | Manual | QA | 20 min |
| T3 | Search | Search with filters | P1 | Automated | QA | 10 min |

### Step 4 — Entry / Exit
- Start regression after: code freeze + smoke test passed
- Regression complete when: all P0 and P1 tests passed, no new P0/P1 bugs

## Output Format
1. Risk-based area selection table
2. Regression test plan
3. Time estimate for full regression run
4. Suggested next command: `/bug-triage` or `/assess-readiness`
