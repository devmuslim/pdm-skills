# Command: /plan-release

## Description
Full release planning workflow: scope definition → dependency mapping → risk register → milestone plan → launch checklist.

## Usage
```
/plan-release [describe your release]
```

## Examples
```
/plan-release Mobile app v3.0 — adding real-time chat and push notifications
/plan-release Platform migration from monolith to microservices — Q3 target
/plan-release Regulatory compliance update — GDPR changes — mandatory by June 1
```

## Workflow

This command chains the following skills in order:

1. **release-scope** — Clarify and structure what's in and out of scope
2. **dependency-map** — Identify team and system dependencies
3. **risk-register** — Build the delivery risk register
4. **milestone-plan** — Convert scope into milestones with dates and owners
5. **launch-checklist** — Generate the pre-launch readiness checklist

## Step-by-Step Execution

### Phase 1: Scope Definition
Run `release-scope` skill.
Ask the user for:
- Full list of features/requirements
- Target date or sprint count
- Non-negotiable items

Output: MoSCoW table + scope statement.

### Phase 2: Dependency Mapping
Run `dependency-map` skill.
Ask for:
- Teams involved
- External systems or vendors
- Known integration points

Output: Dependency table + critical path flags.

### Phase 3: Risk Register
Run `risk-register` skill.
Auto-generate risks based on scope and dependencies identified above.
Ask user to add any known risks.

Output: Risk register with scores and mitigation plans.

### Phase 4: Milestone Plan
Run `milestone-plan` skill.
Based on scope and risks, generate:
- Key milestones with target dates
- Owners per milestone
- Buffer recommendations

Output: Milestone table + Gantt-style timeline (text).

### Phase 5: Launch Checklist
Run `launch-checklist` skill.
Generate domain-specific checklist for this release type.

Output: Full checklist + Go/No-Go summary.

---

## After Completion
Suggest next commands:
- `/assess-readiness` — When approaching launch
- `/status-update` — For weekly progress reporting
- `/handle-delay` — If timeline is at risk
