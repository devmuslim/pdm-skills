# Skill: decision-log

## Purpose
Document delivery decisions with full context — what was decided, why, who decided, and what alternatives were considered — so decisions can be understood, defended, and revisited.

## When to Use
- After any significant delivery decision
- When a decision may be questioned later
- As a handover artifact for new team members or PDMs

## Framework: Decision Log

### Decision Log Entry Template

**Decision ID**: D-[number]
**Date**: [Date]
**Decision**: [What was decided — one clear sentence]
**Made By**: [Name / Role]
**Context**: [Why this decision was needed — 2–3 sentences]

**Options Considered**:
| Option | Pros | Cons |
|--------|------|------|
| A — [description] | [pros] | [cons] |
| B — [description] | [pros] | [cons] |
| C — [description] | [pros] | [cons] |

**Rationale**: Why option [X] was chosen.

**Assumptions**: What must be true for this to be the right decision.

**Reversibility**: 
- ✅ Easily reversible — can change if new information emerges
- ⚠️ Reversible with cost — significant rework if changed
- ❌ Irreversible — one-way door, proceed with extra care

**Review Date**: [When to revisit if assumptions change]

---

### Decision Log Table (Master List)

| ID | Date | Decision | Made By | Status |
|----|------|---------|---------|--------|
| D-001 | [date] | Use phased rollout for v3.0 | PDM | ✅ Active |
| D-002 | [date] | Defer multi-language to v3.1 | PDM + PO | ✅ Active |
| D-003 | [date] | Replace Vendor A with Vendor B | PDM + Procurement | ✅ Active |

## Output Format
1. Completed decision log entry
2. Updated master log table
3. Suggested next command: `/status-update` or `/steering-deck`
