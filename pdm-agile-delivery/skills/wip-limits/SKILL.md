# Skill: wip-limits

## Purpose
Define WIP limits for a team's workflow to reduce multitasking, improve focus, and increase throughput.

## When to Use
- Team is working on too many things simultaneously
- Cycle time is high and items sit idle waiting
- Setting up or improving a Kanban board

## Framework: WIP Limit Setting

### Why WIP Limits Matter
Little's Law: Lead Time = WIP / Throughput
More WIP → longer lead time. Fewer items in progress → faster completion.

### Step 1 — Map the Workflow
Common stages: Backlog → Ready → In Progress → In Review → Testing → Done

### Step 2 — Set WIP Limits per Stage

| Stage | Recommended WIP Limit |
|-------|----------------------|
| Ready (refined, not started) | 2× sprint capacity |
| In Progress | Team size (e.g., 6 devs = max 6 in progress) |
| In Review (PR/code review) | Team size × 0.5 |
| Testing | QA team size × 1.5 |
| Awaiting Deployment | ≤ 3 |

### Step 3 — When WIP Limit is Hit
Rule: "Stop starting, start finishing."
When a column is full:
1. Help unblock an existing item
2. Pair with someone to complete an in-progress item
3. Do not pull new work until a slot opens

### Step 4 — WIP Limit Board Configuration
Show the team's board with WIP limits applied:

```
[Backlog] → [Ready: 8] → [In Progress: 6] → [Review: 3] → [Testing: 4] → [Done]
```

## Output Format
1. Recommended WIP limits per stage
2. Board configuration
3. Team agreement statement for working agreements
4. Suggested next command: `/working-agreements` or `/flow-metrics`
