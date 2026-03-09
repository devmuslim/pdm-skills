# Skill: rollout-strategy

## Purpose
Select and design the right rollout strategy for a release — balancing speed, risk, and user impact.

## When to Use
- During release planning
- When releasing to a large or sensitive user base
- When the feature has high technical or business risk

## Framework: Rollout Strategy Selection

### Step 1 — Understand the Context
Ask for:
- User base size and type (internal, B2B, B2C)
- Feature risk level (high / medium / low)
- Rollback complexity (easy / hard / very hard)
- Monitoring capability (robust / basic / none)

### Step 2 — Strategy Options

#### Option A: Big Bang
**Description**: Deploy to 100% of users at once.
**Best for**: Low-risk changes, internal tools, hotfixes, small user bases.
**Risk**: High — if something breaks, everyone is affected.
**Rollback**: Redeploy previous version.

#### Option B: Phased Rollout (Percentage-Based)
**Description**: Release to 5% → 25% → 50% → 100% over days/weeks.
**Best for**: B2C products, large user bases, medium-risk features.
**Risk**: Medium — issues caught early affect small % of users.
**Rollback**: Reduce percentage to 0%.

#### Option C: Canary Release
**Description**: Release to a small "canary" group (e.g., internal employees or power users) before general availability.
**Best for**: High-risk features, new infrastructure, major architecture changes.
**Risk**: Low — issues are caught before wide exposure.
**Rollback**: Simple — revert canary group.

#### Option D: Feature Flags
**Description**: Deploy code to all users but hide behind a flag. Enable selectively.
**Best for**: When you want zero-downtime deploys and gradual enablement.
**Risk**: Low — can toggle off instantly.
**Rollback**: Disable flag (seconds).

#### Option E: Blue/Green Deployment
**Description**: Run two identical environments; switch traffic from Blue (old) to Green (new).
**Best for**: Zero-downtime deployments, critical infrastructure.
**Risk**: Low — instant rollback by switching back to Blue.
**Rollback**: Redirect traffic to Blue (seconds).

### Step 3 — Strategy Recommendation Matrix

| Context | Recommended Strategy |
|---------|---------------------|
| Low risk, small user base | Big Bang |
| Medium risk, large B2C | Phased Rollout |
| High risk, unknown stability | Canary + Feature Flags |
| Critical infrastructure | Blue/Green |
| Gradual feature adoption | Feature Flags |

### Step 4 — Rollout Plan
Based on selected strategy, produce:

**Phased Rollout Example:**
| Phase | % Users | Duration | Success Criteria | Rollback Trigger |
|-------|---------|----------|-----------------|-----------------|
| Phase 1 | 5% | 24 hours | Error rate < 0.5%, p95 latency < 300ms | Error rate > 1% |
| Phase 2 | 25% | 48 hours | Same + no P0 bugs | Any P0 bug |
| Phase 3 | 100% | — | Stable for 72 hours | — |

## Output Format
1. Strategy recommendation with rationale
2. Rollout plan table with success criteria and rollback triggers
3. Monitoring checklist for launch day
4. Suggested next command: `/launch-checklist` or `/assess-readiness`
