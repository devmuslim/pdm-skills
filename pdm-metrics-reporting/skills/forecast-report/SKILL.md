# Skill: forecast-report

## Purpose
Generate a data-driven delivery forecast based on current velocity and remaining backlog — giving stakeholders a realistic, honest view of when things will be done.

## When to Use
- When asked "when will the release be done?"
- During quarterly planning
- When timeline commitments are being challenged

## Framework: Delivery Forecast

### Step 1 — Gather Inputs
- Remaining story points in release backlog
- Team velocity (last 3–6 sprints)
- Sprint length
- Any planned capacity changes (holidays, hiring, departures)

### Step 2 — Calculate Scenarios

**Formula**: Sprints Remaining = Remaining SP / Velocity

| Scenario | Velocity | Sprints Remaining | Forecast Date |
|----------|----------|------------------|--------------|
| Optimistic | Max velocity (45 SP) | X | [date] |
| Realistic | Average velocity (36 SP) | X | [date] |
| Conservative | 80% of average (29 SP) | X | [date] |

### Step 3 — Forecast Confidence Statement
> "Based on our last 6 sprints averaging 36 story points, and with 180 story points remaining, our realistic forecast is 5 sprints — a target date of [date]. Under conservative assumptions (accounting for risk and uncertainty), we would complete by [date+2 weeks]."

### Step 4 — Forecast vs Commitment
| | Committed Date | Realistic Forecast | Gap |
|--|---------------|-------------------|-----|
| Release date | [date] | [forecast date] | [+/- days] |

If gap exists, flag it and recommend scope cut or date negotiation.

### Step 5 — What Would Accelerate Delivery?
Options to explore:
- Reduce scope (cut Could Haves)
- Add team capacity
- Reduce WIP and improve flow
- Parallelize work across more team members

## Output Format
1. Three-scenario forecast table
2. Confidence statement
3. Forecast vs commitment comparison
4. Acceleration options if behind
5. Suggested next command: `/cut-scope` or `/status-update`
