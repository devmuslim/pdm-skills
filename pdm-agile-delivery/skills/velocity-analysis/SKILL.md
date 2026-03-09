# Skill: velocity-analysis

## Purpose
Analyze team velocity trends to produce data-driven delivery forecasts and identify improvement opportunities.

## When to Use
- Release planning (how much can we deliver?)
- When stakeholders ask "when will it be done?"
- After a significant velocity drop

## Framework: Velocity Analysis

### Step 1 — Gather Velocity Data
Ask for: story points completed per sprint for the last 6–8 sprints.

Example input:
Sprint 8: 42, Sprint 9: 38, Sprint 10: 45, Sprint 11: 28, Sprint 12: 31, Sprint 13: 35

### Step 2 — Calculate Key Metrics

**Average Velocity** = Sum / Number of sprints
Example: (42+38+45+28+31+35) / 6 = **36.5 SP/sprint**

**Velocity Range** = Min to Max
Example: 28–45 SP/sprint

**Trend**: Is velocity increasing, stable, or declining?
Plot last 6 sprints mentally:
- If last 3 avg > first 3 avg → improving
- If last 3 avg < first 3 avg → declining
- Otherwise → stable

### Step 3 — Remove Outliers
If one sprint is > 2x standard deviation from mean, flag it and explain (team was short-staffed, holiday sprint, etc.)

### Step 4 — Delivery Forecast

Given remaining backlog size:
- **Optimistic forecast** (using max velocity): Backlog / Max = X sprints
- **Realistic forecast** (using average): Backlog / Average = X sprints
- **Conservative forecast** (using min): Backlog / Min = X sprints

| Scenario | Velocity Used | Sprints Needed | Target Date |
|----------|--------------|----------------|------------|
| Optimistic | 45 SP | X | [date] |
| Realistic | 36.5 SP | X | [date] |
| Conservative | 28 SP | X | [date] |

**Recommendation**: Commit to realistic; communicate conservative as risk scenario.

### Step 5 — Velocity Drop Investigation
If velocity dropped > 20% for 2+ consecutive sprints:
- Ask about team composition changes
- Check blocker history
- Check scope creep
- Check meeting load

## Output Format
1. Velocity summary (avg, range, trend)
2. Forecast table (optimistic / realistic / conservative)
3. Velocity drop flags and investigation prompts
4. Suggested next command: `/sprint-health` or `/delivery-report`
