# Skill: impediment-log

## Purpose
Maintain a structured log of delivery impediments with ownership, aging, and resolution tracking — so nothing falls through the cracks.

## When to Use
- Ongoing delivery tracking
- Weekly blocker review
- Sprint retrospective input

## Framework: Impediment Log

### Log Structure

| # | Description | Raised By | Date Raised | Type | Owner | Target Date | Days Open | Status | Resolution |
|---|------------|-----------|-------------|------|-------|-------------|-----------|--------|-----------|
| I1 | QA env not matching production | QA Lead | [date] | Infrastructure | DevOps | [date] | 5 | 🔄 Open | — |
| I2 | Missing API spec from vendor | Dev | [date] | External | PDM | [date] | 12 | 🔄 Open | Escalated |
| I3 | Sprint planning took 4 hours | Scrum Master | [date] | Process | PDM | [date] | — | ✅ Closed | Timeboxed to 2hrs |

### Aging Alerts
- > 3 days open → Check in with owner daily
- > 7 days open → Escalate one level
- > 14 days open → Steering Committee visibility

### Weekly Review Checklist
- [ ] Review all open impediments
- [ ] Update status and days open
- [ ] Escalate any that exceeded SLA
- [ ] Close resolved impediments with resolution note
- [ ] Identify patterns (same type recurring = process problem)

## Output Format
1. Impediment log (ready for Confluence)
2. Aging alerts
3. Pattern analysis if recurring impediments exist
4. Suggested next command: `/blocker-triage` or `/retrospective`
