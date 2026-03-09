# Skill: risk-register

## Purpose
Build and maintain a structured delivery risk register with probability, impact ratings, mitigation plans, and ownership.

## When to Use
- At the start of release planning
- After dependency mapping reveals new risks
- During weekly delivery reviews

## Framework: Delivery Risk Register

### Step 1 — Risk Identification
Prompt the user to brainstorm risks across these categories:
- **Technical** — Architecture unknowns, integrations, technical debt
- **Resource** — Team availability, skill gaps, attrition
- **External** — Vendor delays, third-party APIs, regulatory changes
- **Scope** — Requirement changes, stakeholder misalignment
- **Timeline** — Unrealistic estimates, holiday periods, dependencies
- **Quality** — Test coverage gaps, insufficient UAT time

### Step 2 — Risk Scoring
Rate each risk:
- **Probability**: Low (1) / Medium (2) / High (3)
- **Impact**: Low (1) / Medium (2) / High (3)
- **Score** = Probability × Impact (1–9)

### Step 3 — Risk Register Table

| # | Risk Description | Category | Probability | Impact | Score | Status | Owner | Mitigation Plan | Contingency |
|---|-----------------|----------|-------------|--------|-------|--------|-------|----------------|-------------|
| R1 | ... | Technical | High | High | 9 | 🔴 Open | ... | ... | ... |

Status icons:
- 🔴 Open — Active risk, not mitigated
- 🟡 Monitoring — Mitigation in progress
- 🟢 Closed — Risk resolved or no longer relevant

### Step 4 — Risk Summary
- Total risks by category
- Top 3 risks requiring immediate action
- Recommended escalations (Score 7–9 should go to steering committee)

## Output Format
1. Risk register table (sorted by score descending)
2. Risk summary and top priorities
3. Escalation recommendations
4. Suggested next command: `/assess-readiness` or `/plan-release`
