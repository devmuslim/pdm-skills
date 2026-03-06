# Skill: capacity-planning

## Purpose
Calculate realistic team capacity and distribute work across sprints, accounting for meetings, leave, and overhead — so commitments are grounded in reality.

## When to Use
- At the start of release planning
- When a new team member joins or leaves
- When scope is being negotiated against timeline

## Framework: Capacity Planning

### Step 1 — Gather Team Data
For each team member, ask:
- Role (Dev, QA, Designer, etc.)
- Available days in the release window
- Planned leave or part-time allocation
- % allocated to this release (vs. other projects)

### Step 2 — Capacity Formula

**Gross Capacity** = Working days in release window × Hours per day

**Net Capacity** = Gross Capacity
  − Meeting overhead (typically 20%)
  − BAU / support tasks (ask team, typically 10–20%)
  − Leave days

**Story Point Capacity** = Net Capacity in days × Team velocity per day

### Step 3 — Capacity Table per Sprint

| Sprint | Dev Capacity (days) | QA Capacity (days) | Design Capacity (days) | Notes |
|--------|--------------------|--------------------|----------------------|-------|
| Sprint 1 | 35 | 15 | 10 | Design lead on leave day 3 |
| Sprint 2 | 40 | 20 | 5 | Full team |
| Sprint 3 | 30 | 25 | 0 | Code freeze week |
| **Total** | **105** | **60** | **15** | |

### Step 4 — Scope vs Capacity Check

| Item | Estimated Effort | Priority | Fits in Capacity? |
|------|-----------------|----------|------------------|
| Feature A | 20 dev days | Must Have | ✅ Yes |
| Feature B | 15 dev days | Must Have | ✅ Yes |
| Feature C | 40 dev days | Should Have | ⚠️ Tight |
| Feature D | 25 dev days | Could Have | ❌ No — defer |

### Step 5 — Recommendation
State clearly:
- What fits within capacity
- What needs to be cut or deferred
- Where risk of overcommitment exists

## Output Format
1. Capacity table per sprint
2. Scope vs capacity check
3. Recommendation on what to cut or defer
4. Suggested next command: `/milestone-plan` or `/cut-scope`
