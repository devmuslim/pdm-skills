# Skill: pi-planning

## Purpose
Facilitate or prepare for a Program Increment (PI) Planning event in SAFe environments — aligning multiple Agile Release Trains (ARTs) around shared objectives.

## When to Use
- Every 8–12 weeks in SAFe organizations
- When multiple teams need to align on a shared delivery quarter
- When dependencies between teams need to be surfaced and resolved

## Framework: PI Planning

### What is a PI?
A Program Increment is a 8–12 week delivery cycle (typically 4–5 sprints) used in SAFe. PI Planning is the face-to-face (or virtual) event where all teams plan together.

### Step 1 — Pre-PI Planning Preparation (2 weeks before)
- [ ] Product Vision updated (Executive / Business Owner)
- [ ] Top 10 Program Backlog items refined and prioritized
- [ ] Architecture briefing prepared (System Architect)
- [ ] Team capacity confirmed for each squad
- [ ] Tools ready (Jira, Miro, or physical board)

### Step 2 — PI Planning Agenda (2 Days)

**Day 1**
- Business context and vision (45 min)
- Architecture vision (30 min)
- Team breakouts: Draft PI objectives + Sprint 1 plan (4 hrs)
- Draft plan review (30 min)
- Risk identification and ROAM (45 min)

**Day 2**
- Adjustments to draft plans (2 hrs)
- Final plan review per team (1 hr)
- ART risk review and PI Objectives vote (1 hr)
- Confidence vote — Fist of Five (15 min)
- Retrospective (30 min)

### Step 3 — ROAM Risks
Classify PI-level risks:

| Risk | Classification | Action |
|------|---------------|--------|
| API not ready from Team B | Resolved | Team B commits to Sprint 2 delivery |
| Vendor contract not signed | Owned | PDM tracks weekly, escalates if unsigned by Sprint 1 |
| Regulatory approval unclear | Accepted | Business accepts risk and monitors |
| Dependency on legacy system | Mitigated | Architecture team adds spike in Sprint 1 |

### Step 4 — PI Objectives Template

Per team:
- **Committed Objectives**: What we will deliver (high confidence)
- **Stretch Objectives**: What we might deliver (lower confidence)
- **Business Value**: Score assigned by Business Owners (1–10)

### Step 5 — Confidence Vote (Fist of Five)
Team votes 1–5 on confidence in delivering PI objectives:
- 5 (all fingers): Fully confident
- 3: Conditional confidence
- 1–2: Serious concerns — must be addressed before PI starts

## Output Format
1. Pre-PI checklist
2. PI Planning agenda
3. ROAM risk table
4. PI Objectives template per team
5. Suggested next command: `/milestone-plan` or `/dependency-map`
