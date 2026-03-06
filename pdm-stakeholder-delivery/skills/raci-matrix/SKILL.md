# Skill: raci-matrix

## Purpose
Build a clear RACI matrix for a delivery initiative — eliminating ambiguity about who does what, who decides, and who needs to be informed.

## When to Use
- At the start of a release with multiple teams
- When roles and responsibilities are unclear or contested
- When handoffs between teams are causing delays

## Framework: RACI Matrix

### Definitions
- **R — Responsible**: Does the work. Can be multiple people.
- **A — Accountable**: Owns the outcome. Signs off. Only ONE person per activity.
- **C — Consulted**: Provides input before the decision. Two-way communication.
- **I — Informed**: Notified of outcomes. One-way communication.

### Rules
- Every row must have exactly ONE A
- Too many R's = unclear ownership
- Too many C's = slow decisions
- I's should receive information, not be asked for approval

### Step 1 — Define Activities
Common delivery activities to include:
- Requirements definition
- Technical design
- Development
- Code review
- QA / Testing
- UAT
- Release approval
- Deployment
- Post-launch monitoring
- Stakeholder communication

### Step 2 — Build the Matrix

| Activity | PDM | Tech Lead | Dev Team | QA Lead | Business Owner | Exec Sponsor |
|----------|-----|-----------|----------|---------|---------------|-------------|
| Requirements | A | C | I | C | R | I |
| Technical Design | I | A | R | C | I | — |
| Development | I | A | R | I | — | — |
| QA Sign-off | C | I | I | A | R | I |
| UAT | C | I | — | C | A | I |
| Go/No-Go Decision | R | C | — | C | C | A |
| Deployment | C | A | R | I | I | I |

### Step 3 — RACI Health Check
Flag issues:
- ❌ No A defined → Decision bottleneck
- ❌ Multiple A's → Unclear accountability
- ⚠️ PDM is A for everything → Overloaded
- ⚠️ Exec is C on everything → Meeting overload risk

## Output Format
1. Completed RACI matrix
2. Health check flags
3. Recommended changes with rationale
4. Suggested next command: `/stakeholder-pulse` or `/steering-deck`
