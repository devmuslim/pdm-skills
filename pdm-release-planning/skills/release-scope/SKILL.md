# Skill: release-scope

## Purpose
Define and structure the scope of an upcoming release using MoSCoW prioritization. Helps delivery managers align teams around what's in, what's out, and what's deferred.

## When to Use
- Starting a new release planning cycle
- Scope is unclear or contested across teams
- Need to communicate scope decisions to stakeholders

## Framework: Structured Scope Definition

### Step 1 — Gather Inputs
Ask for:
- List of features/requirements proposed for the release
- Target release date or sprint count
- Team size and composition
- Any non-negotiable items (regulatory, contractual, dependencies)

### Step 2 — Apply MoSCoW
Classify each item:
- **Must Have** — Release fails without this. Non-negotiable.
- **Should Have** — High value, but workarounds exist. Include if capacity allows.
- **Could Have** — Nice-to-have. First to cut under pressure.
- **Won't Have (this time)** — Explicitly out of scope for this release.

### Step 3 — Scope Summary Table
Output a table:

| Item | Category | Rationale | Owner | Estimated Effort |
|------|----------|-----------|-------|-----------------|
| ... | Must | ... | ... | ... |

### Step 4 — Scope Risks
Flag items where:
- Effort is uncertain (spike needed)
- External dependency exists
- Two teams need to coordinate

### Step 5 — Scope Statement
Write a 2-sentence scope statement suitable for stakeholder communication:
> "Release X will deliver [Must Haves] enabling [business outcome]. The following items are explicitly deferred to Release Y: [Won't Haves]."

## Output Format
1. MoSCoW table
2. Scope risks list
3. Scope statement (stakeholder-ready)
4. Suggested next command: `/map-dependencies` or `/assess-readiness`
