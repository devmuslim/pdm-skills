# Skill: delivery-kpis

## Purpose
Define and track the right delivery KPIs, including DORA metrics, for a product delivery team. Helps PDMs speak the language of engineering excellence and business value.

## When to Use
- Setting up delivery metrics for a new team
- Preparing a metrics report for leadership
- Evaluating team delivery performance

## Framework: Delivery KPIs

### Tier 1: DORA Metrics (Engineering Excellence)
Research-backed indicators of software delivery performance.

| Metric | Definition | Elite | High | Medium | Low |
|--------|-----------|-------|------|--------|-----|
| **Deployment Frequency** | How often code is deployed to production | On-demand (multiple/day) | Daily–weekly | Weekly–monthly | < Monthly |
| **Lead Time for Changes** | Time from code commit to production | < 1 hour | 1 day–1 week | 1 week–1 month | > 1 month |
| **Change Failure Rate** | % of deployments causing failures | < 5% | 5–10% | 10–15% | > 15% |
| **MTTR** (Mean Time to Restore) | Time to restore service after incident | < 1 hour | < 1 day | < 1 week | > 1 week |

### Tier 2: Flow Metrics (Delivery Efficiency)
| Metric | Definition | What It Tells You |
|--------|-----------|-------------------|
| **Cycle Time** | Time from "In Progress" to "Done" | Team execution speed |
| **Lead Time** | Time from request to delivery | End-to-end responsiveness |
| **Throughput** | Items completed per sprint/week | Team output rate |
| **WIP** | Items in progress at any time | Focus and multitasking risk |
| **Flow Efficiency** | Active time / total lead time | Waste in the process |

### Tier 3: Release Metrics (Delivery Outcomes)
| Metric | Definition | Target |
|--------|-----------|--------|
| **Release Predictability** | % of releases shipped on planned date | > 80% |
| **Scope Completion Rate** | % of committed scope delivered | > 90% |
| **Defect Escape Rate** | % of bugs found by users (not QA) | < 10% |
| **Rollback Rate** | % of deployments requiring rollback | < 5% |

### Step 1 — Select Right Metrics for Context
Ask:
- Is the team in startup mode or scaling mode?
- Is reliability or speed the bigger concern?
- What does leadership care most about?

Recommend 4–6 metrics based on context.

### Step 2 — Current Baseline
Prompt user for current values. Calculate performance tier.

### Step 3 — Dashboard Design

| Metric | Current | Target | Trend | Status |
|--------|---------|--------|-------|--------|
| Deployment Frequency | 2/week | Daily | ↗ | 🟡 |
| Lead Time | 8 days | 3 days | → | 🔴 |
| MTTR | 45 min | < 1hr | ↘ | ✅ |

### Step 4 — Improvement Recommendations
For each 🔴 or 🟡 metric, suggest 1–2 specific improvements.

## Output Format
1. Recommended metrics set for the team's context
2. Current vs target table with trend and status
3. Top 2 improvement recommendations
4. Suggested next command: `/delivery-report` or `/forecast-report`
