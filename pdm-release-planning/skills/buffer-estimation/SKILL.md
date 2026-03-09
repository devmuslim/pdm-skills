# Skill: buffer-estimation

## Purpose
Calculate the right time buffer for a release based on delivery complexity, team history, and risk profile — so timelines are honest and defensible.

## When to Use
- When committing to a release date
- When scope or team composition is uncertain
- When presenting timelines to stakeholders

## Framework: Buffer Estimation

### Step 1 — Assess Complexity Factors

Score each factor 1 (low) to 3 (high):

| Factor | 1 — Low | 2 — Medium | 3 — High | Your Score |
|--------|---------|-----------|---------|-----------|
| Technical complexity | Known tech, small changes | Some new patterns | New architecture, integrations | |
| Team experience | Team has done this before | Mixed experience | New team or new domain | |
| Dependency count | 0–2 dependencies | 3–5 dependencies | 6+ dependencies | |
| External dependencies | None | 1–2 external | 3+ external (vendors, App Store) | |
| Requirement stability | Fully defined | Some unknowns | Frequently changing | |
| Team size | 1–3 people | 4–8 people | 9+ people | |

**Total Score**: X / 18

### Step 2 — Buffer Recommendation

| Total Score | Buffer | Rationale |
|-------------|--------|-----------|
| 6–9 | **10%** | Low complexity, high confidence |
| 10–13 | **20%** | Moderate risk, manageable unknowns |
| 14–16 | **30%** | High complexity or dependency risk |
| 17–18 | **40%+ or split release** | Too risky to commit as single release |

### Step 3 — Apply Buffer to Timeline

Example:
- Raw estimate: 6 weeks
- Complexity score: 13 → 20% buffer
- Buffered timeline: 6 × 1.2 = **7.2 weeks → commit to 7.5 weeks**

### Step 4 — How to Communicate Buffer to Stakeholders
> "Our engineering estimate is 6 weeks. Based on the integration complexity and external vendor dependency, we're committing to 7.5 weeks, which gives us a target date of [date]. This is the date we're confident delivering to, not a worst-case."

Never call it "padding." Call it "delivery confidence buffer."

## Output Format
1. Complexity scoring table
2. Buffer recommendation with rationale
3. Buffered timeline calculation
4. Stakeholder-ready explanation of the buffer
5. Suggested next command: `/milestone-plan`
