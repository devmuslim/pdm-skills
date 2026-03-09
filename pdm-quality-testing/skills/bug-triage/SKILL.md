# Skill: bug-triage

## Purpose
Systematically classify, prioritize, and assign bugs using a structured triage framework. Ensures the right bugs are fixed before launch and nothing critical slips through.

## When to Use
- Before a release — clearing the bug backlog
- After a test cycle — processing QA findings
- During production — triaging live incidents

## Framework: Bug Triage

### Priority Classification (P0–P4)

| Priority | Definition | SLA to Fix | Examples |
|----------|-----------|------------|---------|
| **P0 — Critical** | System down, data loss, security breach | Immediate (hours) | Login broken, payments failing, data corruption |
| **P1 — High** | Major feature broken, no workaround | 1–2 days | Key user flow fails, major performance degradation |
| **P2 — Medium** | Feature degraded, workaround exists | Current sprint | Form validation issue, minor UI breakage |
| **P3 — Low** | Minor issue, cosmetic, edge case | Next sprint | Typo, minor layout issue, rare edge case |
| **P4 — Deferred** | Nice to fix, no user impact | Backlog | Code quality, minor inconsistency |

### Step 1 — Gather Bug List
Ask user to provide:
- Bug title / description
- Steps to reproduce (if available)
- Environment (dev, staging, prod)
- Reported by (user, QA, monitoring)

### Step 2 — Triage Each Bug

For each bug, assess:
1. **Severity**: What breaks? Data? Flow? UI only?
2. **Frequency**: How often does it happen? (always / sometimes / rarely)
3. **Affected Users**: All users? Specific segment? Internal only?
4. **Workaround**: Does one exist?
5. **Release Blocker?**: Would you ship with this bug?

### Step 3 — Triage Output Table

| # | Bug Title | Priority | Severity | Frequency | Release Blocker? | Assignee | Notes |
|---|-----------|----------|----------|-----------|-----------------|----------|-------|
| 1 | ... | P1 | High | Always | Yes | Dev Team | Blocks checkout |
| 2 | ... | P3 | Low | Rarely | No | — | Defer to next sprint |

### Step 4 — Release Decision Summary
- **P0 bugs**: X → Must fix before any release
- **P1 bugs**: X → Must fix before planned release date
- **P2 bugs**: X → Fix in sprint or accept with monitoring
- **P3/P4 bugs**: X → Defer

**Release Recommendation:**
- ✅ Ready to release (0 P0s, 0 P1s)
- ⚠️ Release at risk (P1s remain)
- ❌ Do not release (P0s remain)

## Output Format
1. Triage table sorted by priority
2. Release decision summary
3. List of release blockers with owners
4. Suggested next command: `/test-plan` or `/assess-readiness`
