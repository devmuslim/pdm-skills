# Skill: post-mortem

## Purpose
Facilitate a blameless post-mortem after a delivery incident, missed release, or production outage. Focus on systemic causes and preventive actions, not individual blame.

## When to Use
- After a production incident
- After a missed release date
- After a quality failure reaches production
- After a major scope cut under pressure

## Framework: Blameless Post-Mortem

### Principle: Systems Thinking
> "The goal is not to find who is at fault. The goal is to understand what in the system allowed this to happen — and how to fix it."

### Step 1 — Gather Incident Data
Ask for:
- What happened? (brief description)
- When was it detected?
- What was the customer/business impact?
- How long did it last?
- How was it resolved?
- Who was involved in the response?

### Step 2 — Timeline Reconstruction
Build a factual timeline:

| Time | Event | Who Noticed | Action Taken |
|------|-------|-------------|--------------|
| T+0 | Incident begins | Monitoring alert | ... |
| T+15m | Team notified | On-call engineer | ... |
| T+45m | Root cause identified | ... | ... |
| T+2h | Fix deployed | ... | ... |
| T+2h30m | Incident resolved | ... | ... |

### Step 3 — Five Whys Analysis
Start with the symptom and ask "Why?" five times:
1. Why did X happen?
2. Why did Y allow X?
3. Why was Y not prevented?
4. Why did the process not catch Y?
5. Why does the process have this gap?

Root cause = the answer to the 5th Why.

### Step 4 — Contributing Factors
Classify contributing factors:
- **Process** — Gaps in how we work
- **Technical** — System or tooling failures
- **Communication** — Information that didn't reach the right people in time
- **Knowledge** — Skills or awareness gaps

### Step 5 — Action Items

| Action | Owner | Due Date | Priority |
|--------|-------|----------|----------|
| ... | ... | ... | P0/P1/P2 |

Each action should be:
- Specific and measurable
- Assigned to one person
- Have a clear deadline
- Directly address a root cause or contributing factor

### Step 6 — Post-Mortem Summary (shareable)
- **Incident**: One sentence
- **Impact**: Duration, users affected, business impact
- **Root Cause**: One sentence
- **Resolution**: What fixed it
- **Key Actions**: Top 3 action items

## Output Format
1. Timeline table
2. Five Whys analysis
3. Action items table
4. Shareable summary (suitable for Confluence or Slack)
5. Suggested next command: `/lessons-learned` or `/risk-register`
