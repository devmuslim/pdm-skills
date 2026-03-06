# Skill: shared-roadmap

## Purpose
Build a unified, multi-team delivery roadmap that surfaces dependencies, aligns timelines, and gives all stakeholders a single source of truth.

## When to Use
- Multiple teams are shipping to a shared release
- Stakeholders are getting conflicting roadmap information from different teams
- Quarterly planning requires cross-team alignment

## Framework: Shared Roadmap

### Principle
One roadmap. Multiple team swim lanes. Shared milestones and dependencies visible to all.

### Step 1 — Gather Inputs
Ask for:
- Participating teams and their current sprint/release plans
- Shared milestones (code freeze, UAT, release date)
- Known cross-team dependencies

### Step 2 — Roadmap Format

**Quarterly View (Now / Next / Later)**

| Team | Now (This Quarter) | Next (Next Quarter) | Later (Future) |
|------|-------------------|---------------------|---------------|
| Team A | Feature X, Feature Y | Feature Z | Platform migration |
| Team B | API v2 | Reporting dashboard | — |
| Team C | Infrastructure upgrade | — | Real-time pipeline |

**Milestone Overlay**
| Milestone | Date | Teams Involved |
|-----------|------|---------------|
| Code Freeze | Week 8 | All |
| UAT | Week 9–10 | Team A, Team B |
| Release v3.0 | Week 11 | All |

**Dependency Callouts**
- Team A's Feature X depends on Team B's API v2 (due Week 4)
- Team C's infra upgrade must complete before Team B's Reporting Dashboard

### Step 3 — Roadmap Health Check
- Are all dependencies represented and dated?
- Do all teams have realistic capacity for their roadmap items?
- Are there timeline conflicts between teams?

### Step 4 — Communication Cadence
Roadmap reviewed at:
- Weekly: Dependency status only
- Monthly: Full team sync with updates
- Quarterly: Full roadmap refresh

## Output Format
1. Shared roadmap table (Now/Next/Later per team)
2. Milestone overlay
3. Dependency callouts
4. Review cadence
5. Suggested next command: `/dependency-map` or `/steering-deck`
