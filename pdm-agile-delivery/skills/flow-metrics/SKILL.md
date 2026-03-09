# Skill: flow-metrics

## Purpose
Measure and improve delivery flow using Cycle Time, Lead Time, Throughput, and WIP — the four core flow metrics for any delivery team.

## When to Use
- Monthly delivery review
- When delivery feels slow but cause is unclear
- When moving from output metrics (velocity) to outcome metrics (flow)

## Framework: Flow Metrics

### The Four Flow Metrics

**1. Cycle Time**
Definition: Time from "work started" to "work done"
Measures: How fast the team executes once work begins
Target: < 3 days for stories, < 1 day for bugs

**2. Lead Time**
Definition: Time from "request created" to "work done"
Measures: End-to-end responsiveness including wait time
Target: < 2 weeks for features, < 5 days for bugs

**3. Throughput**
Definition: Number of items completed per sprint/week
Measures: Team output rate
Target: Stable or improving trend

**4. WIP (Work In Progress)**
Definition: Number of items actively in progress at any time
Measures: Multi-tasking and focus
Target: WIP ≤ team size (ideally WIP ≤ team size × 0.5)

### Step 1 — Gather Data
Ask for Jira/Azure DevOps export or manual data:
- Item ID, start date, completion date, type (story/bug/task)

### Step 2 — Calculate Metrics

| Metric | Formula | Last Period | Trend |
|--------|---------|-------------|-------|
| Avg Cycle Time | Sum of (done - started) / count | X days | ↗/→/↘ |
| Avg Lead Time | Sum of (done - created) / count | X days | ↗/→/↘ |
| Throughput | Items completed / weeks | X items/week | ↗/→/↘ |
| Avg WIP | Daily WIP snapshots averaged | X items | ↗/→/↘ |

### Step 3 — Flow Efficiency
Flow Efficiency = Active Time / Lead Time × 100%
- > 40%: Good flow
- 15–40%: Typical, room to improve
- < 15%: High wait time — investigate queues

### Step 4 — Diagnosis
| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| High lead time, low cycle time | Long wait in queue | Reduce batch size, limit WIP |
| High cycle time | Work is too large or complex | Split stories, improve specs |
| Low throughput | Too much WIP, blockers | WIP limits, blocker triage |
| Declining flow efficiency | Process overhead | Remove unnecessary approvals |

## Output Format
1. Metrics table with trend indicators
2. Flow efficiency score
3. Top 2 improvement recommendations
4. Suggested next command: `/delivery-report` or `/wip-limits`
