# Skill: definition-of-done

## Purpose
Create a clear, team-agreed Definition of Done (DoD) that ensures consistent quality across all delivered work.

## When to Use
- Team formation or onboarding
- When quality issues are found in production (DoD too weak)
- When working agreements are being established

## Framework: Definition of Done

### Levels of Done

**Story Level DoD** — Applied to every user story:
- [ ] Code written and meets coding standards
- [ ] Unit tests written and passing (coverage > 80%)
- [ ] Code reviewed and approved by at least one peer
- [ ] No known P0 or P1 bugs introduced
- [ ] Acceptance criteria tested and passed
- [ ] Feature tested in staging environment
- [ ] Product Owner / PDM has accepted the story
- [ ] Documentation updated (if applicable)

**Sprint Level DoD** — Applied to the sprint as a whole:
- [ ] All sprint stories meet Story DoD
- [ ] Regression tests passing
- [ ] No unresolved blockers carried into next sprint
- [ ] Sprint review conducted
- [ ] Retrospective actions captured

**Release Level DoD** — Applied before any production deployment:
- [ ] All sprint DoDs satisfied
- [ ] Full regression suite passed
- [ ] Performance testing completed
- [ ] Security scan completed and reviewed
- [ ] UAT sign-off received
- [ ] Rollback plan tested
- [ ] Release notes published
- [ ] Monitoring and alerts configured

### Customization
Ask the team:
- What type of system are we building? (web, mobile, data pipeline, API)
- What compliance or regulatory requirements apply?
- What is our current test coverage baseline?

## Output Format
1. Three-level DoD (Story / Sprint / Release)
2. Customized for team context
3. Suggested next command: `/working-agreements` or `/launch-checklist`
