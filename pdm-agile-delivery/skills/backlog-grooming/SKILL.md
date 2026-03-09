# Skill: backlog-grooming

## Purpose
Facilitate a structured backlog grooming session to ensure the top items are well-defined, estimated, and ready for the next sprint.

## When to Use
- 2–3 days before sprint planning
- When backlog items lack acceptance criteria or estimates
- When the team is unsure what to pick next sprint

## Framework: Backlog Grooming Session

### Step 1 — Pre-Grooming Preparation
Before the session:
- Filter backlog to top 20–30 items by priority
- Remove duplicates and stale items (no activity in 90+ days)
- Ensure each item has at minimum: title, description, priority

### Step 2 — For Each Item, Check the 3 R's

**Ready** — Is the item ready for development?
- [ ] Clear description of what needs to be built
- [ ] Acceptance criteria defined (Given/When/Then)
- [ ] Dependencies identified
- [ ] Design/mockups available (if needed)
- [ ] Estimated (story points or T-shirt size)

**Right** — Is the priority right?
- Does it align with the sprint goal?
- Is the business value clear?

**Realistic** — Is the scope realistic for one sprint?
- If > 8 story points → split the story

### Step 3 — Grooming Output Table

| # | Item Title | Ready? | Size (SP) | Priority | Action Needed |
|---|-----------|--------|-----------|----------|--------------|
| 1 | Login with SSO | ✅ Yes | 5 | P1 | Ready for sprint |
| 2 | Export to CSV | ⚠️ Partial | 3 | P2 | Needs AC written |
| 3 | Dashboard redesign | ❌ No | 13 | P1 | Split into 3 stories |

### Step 4 — Items to Split
For any item > 8 SP, suggest splits:

Original: "Dashboard redesign" (13 SP)
→ Story 1: Dashboard layout and navigation (5 SP)
→ Story 2: Widget data integration (5 SP)
→ Story 3: Filters and date range (3 SP)

### Step 5 — Grooming Health Check
- % of top 10 items marked Ready: target > 80%
- Average SP of items: target < 8
- Items with no AC: must be fixed before sprint planning

## Output Format
1. Grooming output table
2. Items to split with suggested breakdown
3. Action list before sprint planning
4. Suggested next command: `/sprint-health` or `/velocity-analysis`
