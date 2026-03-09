# Skill: portfolio-dashboard

## Purpose
Design a portfolio-level delivery dashboard that gives leadership a single view of all active programmes and releases — with RAG status, dates, and risks.

## When to Use
- Managing multiple simultaneous releases
- Monthly leadership reporting
- When executives ask "how are all our programmes doing?"

## Framework: Portfolio Dashboard

### Step 1 — Gather Programme List
For each active programme/release:
- Name and description
- Target date
- Current forecast
- Overall RAG status
- Top risk
- Budget status (if tracked)

### Step 2 — Portfolio Summary Table

| Programme | Owner | Target Date | Forecast | RAG | Top Risk | Budget |
|-----------|-------|-------------|----------|-----|---------|--------|
| Mobile App v3.0 | [Name] | Jun 30 | Jul 14 | 🟡 | App Store delay | On track |
| Platform Migration | [Name] | Sep 30 | Sep 30 | 🟢 | None | On track |
| Compliance Update | [Name] | Mar 31 | Apr 14 | 🔴 | Regulatory approval | Over 10% |
| Data Pipeline v2 | [Name] | Dec 31 | Dec 31 | 🟢 | None | On track |

### Step 3 — Portfolio Health Summary
- 🟢 On Track: X programmes
- 🟡 At Risk: X programmes
- 🔴 Off Track: X programmes

### Step 4 — Resource Hotspots
Flag any teams or individuals stretched across too many programmes:
- [Person/Team] is contributing to [N] active programmes → risk of context switching

### Step 5 — Decisions Needed at Portfolio Level
- Programme A: Needs budget decision by [date]
- Programme B: Competing priority with Programme C — needs resolution

## Output Format
1. Portfolio summary table
2. Health summary counts
3. Resource hotspots
4. Portfolio-level decisions needed
5. Suggested next command: `/executive-summary` or `/steering-deck`
