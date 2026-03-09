# Skill: integration-plan

## Purpose
Build a structured integration plan for features or systems spanning multiple teams — with clear interfaces, milestones, testing strategy, and escalation paths.

## When to Use
- Two or more teams must ship together
- A new service or API integration is required
- A platform team is providing capabilities to product teams

## Framework: Integration Plan

### Step 1 — Integration Summary
- What is being integrated?
- Which teams are involved?
- What is the target integration date?
- What depends on this integration?

### Step 2 — Interface Definition

| Interface | Provider Team | Consumer Team | Type | Contract Format | Due Date |
|-----------|--------------|---------------|------|----------------|----------|
| Payment API v2 | Payments | Checkout | REST API | OpenAPI spec | Week 2 |
| User events stream | Platform | Analytics | Kafka | Avro schema | Week 3 |
| Feature flags | DevOps | All teams | SDK | Documentation | Week 1 |

### Step 3 — Integration Milestones

| Milestone | Date | Owner | Done When |
|-----------|------|-------|-----------|
| API contract agreed | Week 1 | Tech Leads | Both teams sign off on spec |
| Mock server available | Week 2 | Provider | Consumer can test against mock |
| Integration in staging | Week 3 | Both teams | E2E test passes in staging |
| Integration testing complete | Week 4 | QA | No P0/P1 integration bugs |
| Production ready | Week 5 | PDM | All gates passed |

### Step 4 — Integration Testing Plan
- Who writes the integration tests? (Usually provider or shared QA)
- Which environment? (Staging minimum)
- What are the success criteria?

### Step 5 — Escalation Path
If integration is blocked:
- Day 1–2: Teams resolve between Tech Leads
- Day 3+: PDM escalates to both team PDMs
- Week+: Programme-level escalation

## Output Format
1. Integration summary
2. Interface definition table
3. Milestone plan
4. Testing plan
5. Suggested next command: `/dependency-map` or `/sync-meeting`
