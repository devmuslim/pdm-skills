# PDM Skills Marketplace: The AI Operating System for Product Delivery Managers

> 61 PDM skills and 26 chained workflows across 8 plugins. From release planning to stakeholder communication, agile delivery, quality, and cross-team coordination.

Designed for Claude Code and Cowork. Skills compatible with other AI assistants.

---

## Start Here

Planning a release? → `/plan-release`  
Communicating a delay? → `/handle-delay`  
Steering committee meeting? → `/steering-deck`  
Bug triage needed? → `/bug-triage`  
Cross-team conflict? → `/resolve-conflict`  
Post-release review? → `/post-mortem`

If this project helps you, ⭐ the repo.

---

## Why PDM Skills Marketplace?

Generic AI gives you text. PDM Skills Marketplace gives you delivery structure.

Each skill encodes a proven delivery framework — release readiness, dependency mapping, risk registers, DORA metrics — and walks you through it step by step. You get the rigor of industry-standard delivery practices (SAFe, Scrum, Kanban, DORA) built into your daily workflow.

The result: predictable delivery, not just faster documents.

---

## How It Works (Skills, Commands, Plugins)

**Skills** are the building blocks. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific delivery task. Skills load automatically when relevant — no explicit invocation needed.

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process. For example, `/plan-release` chains: scope-definition → dependency-map → risk-register → milestone-plan → launch-checklist.

**Plugins** group related skills and commands by delivery domain. Installing the marketplace gives you all 8 plugins at once.

Commands suggest relevant next commands after completion — just follow the prompts.

---

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **Browse plugins → Personal → +**
3. Select **Add marketplace from GitHub**
4. Enter: `your-github-username/pdm-skills`

### Claude Code (CLI)

```bash
claude plugin add --marketplace your-github-username/pdm-skills
```

### Other AI assistants (skills only)

Copy `skills/*/SKILL.md` files to your tool's skills folder:

```bash
# Example: copy all skills for Gemini CLI
for plugin in pdm-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## Available Plugins

### 1. pdm-release-planning

Release planning from scope to launch: dependency mapping, risk registers, capacity planning, rollout strategies, and launch checklists.

**Skills (10):**
- `release-scope` — Define release scope from a requirements list with MoSCoW prioritization
- `release-readiness` — Assess team and product readiness for launch across 6 dimensions
- `dependency-map` — Map dependencies between teams, components, and external systems
- `milestone-plan` — Convert goals into measurable milestones with owners and dates
- `capacity-planning` — Calculate team capacity and distribute across sprints
- `risk-register` — Risk register with probability, impact, and mitigation plans
- `buffer-estimation` — Calculate time buffers based on delivery complexity and team history
- `launch-checklist` — Comprehensive pre-launch checklist across tech, comms, and ops
- `rollout-strategy` — Rollout strategies: phased, canary, feature flags, big bang
- `cut-scope` — Analyze what to defer without compromising release value

**Commands (3):**
- `/plan-release` — Full release plan: scope → dependencies → risks → milestones → checklist
- `/assess-readiness` — Launch readiness assessment with go/no-go recommendation
- `/map-dependencies` — Team and system dependency map for the current release

**Examples:**

```
What's the safest rollout strategy for our payments module?
Assess readiness for our Q2 release [attach release plan]
Map dependencies for the platform migration project
```

```
/plan-release Mobile app v3.0 — adding real-time chat and push notifications
/assess-readiness [attach current sprint status and open items]
/map-dependencies Three teams: Frontend, Backend, and Data — shipping together in 6 weeks
```

---

### 2. pdm-stakeholder-delivery

Stakeholder communication across all levels: status reports, delay handling, executive summaries, steering decks, and expectations management.

**Skills (8):**
- `status-report` — Weekly/monthly delivery status report (concise and professional)
- `escalation-framework` — Framework for escalating issues at the right level
- `executive-summary` — Executive summary of delivery health (1-page format)
- `delay-communication` — Communicate delays professionally with recovery plan
- `steering-deck` — Slides for steering committee review
- `expectations-reset` — Reset stakeholder expectations after scope or timeline changes
- `raci-matrix` — RACI matrix for delivery responsibilities
- `stakeholder-pulse` — Quick survey to measure stakeholder satisfaction and trust

**Commands (3):**
- `/status-update` — Generate a status report `weekly|monthly|executive`
- `/handle-delay` — Craft professional delay communication with recovery plan
- `/steering-deck` — Prepare steering committee slides

**Examples:**

```
Write a weekly status for a release that's 2 weeks behind schedule
How do I reset expectations after we had to cut 30% of scope?
Create a RACI for our three-team integration project
```

```
/status-update weekly — Sprint 14 ended with 3 stories carried over, 2 blockers resolved
/handle-delay Our API integration is 3 weeks delayed due to third-party unavailability
/steering-deck Q2 delivery review — 70% complete, 2 risks flagged
```

---

### 3. pdm-agile-delivery

Day-to-day agile delivery: sprint health, backlog grooming, definition of done, blocker triage, velocity analysis, PI planning, and flow metrics.

**Skills (12):**
- `sprint-health` — Sprint health assessment (velocity, burndown, blockers, morale)
- `backlog-grooming` — Structured backlog grooming for the next sprint
- `definition-of-done` — Definition of Done tailored to the team's delivery context
- `blocker-triage` — Classify and assign ownership of delivery blockers
- `sprint-review-template` — Sprint review presentation for stakeholders
- `velocity-analysis` — Analyze team velocity and forecast delivery dates
- `pi-planning` — Program Increment planning for SAFe environments
- `team-health-check` — Team health assessment (motivation, communication, process)
- `impediment-log` — Impediment log with tracking and resolution status
- `working-agreements` — Team working agreements for delivery cadence
- `wip-limits` — WIP limits to improve flow and reduce context switching
- `flow-metrics` — Flow metrics: cycle time, lead time, throughput, WIP

**Commands (3):**
- `/sprint-health` — Sprint health report for the current sprint
- `/groom-backlog` — Structured backlog grooming session
- `/flow-report` — Flow metrics report with improvement recommendations

**Examples:**

```
Our velocity dropped 40% this sprint — what should I investigate?
Set WIP limits for a team of 6 across 3 swim lanes
What flow metrics should I track for a Kanban team?
```

```
/sprint-health Sprint 14: planned 42 points, delivered 28, 4 blockers, 2 carry-overs
/groom-backlog [attach backlog items] — prepare top 20 for next sprint
/flow-report [attach Jira export] — analyze last 8 sprints
```

---

### 4. pdm-quality-testing

Delivery quality from test strategy to post-launch monitoring: acceptance criteria, bug triage, regression plans, UAT, and quality gates.

**Skills (7):**
- `test-strategy` — End-to-end test strategy for the release (unit, integration, E2E, UAT)
- `acceptance-criteria` — Acceptance criteria in Given/When/Then format
- `bug-triage` — Bug triage and prioritization (P0–P4) with resolution SLAs
- `regression-plan` — Regression test plan before launch
- `uat-plan` — User Acceptance Testing plan with scenarios and sign-off criteria
- `quality-gates` — Quality gates between delivery phases
- `post-launch-monitoring` — Post-launch monitoring plan with alerts and escalation

**Commands (3):**
- `/test-plan` — Create a full test strategy for the release
- `/bug-triage` — Triage a list of bugs with priorities and owners
- `/uat-plan` — Build a UAT plan with scenarios and acceptance criteria

**Examples:**

```
What quality gates should I set between Dev, QA, and UAT?
Triage these 25 bugs for our release [attach list]
Build a UAT plan for our new reporting module
```

```
/test-plan Payment processing feature — 3 teams, 6-week timeline
/bug-triage [attach bug list] — release in 2 weeks
/uat-plan [attach PRD] — business users will test next week
```

---

### 5. pdm-cross-team-coordination

Multi-team coordination: sync meetings, integration plans, API contracts, handoff templates, Three Amigos, and conflict resolution.

**Skills (8):**
- `team-sync-agenda` — Structured agenda for multi-team sync meetings
- `integration-plan` — Integration plan for features spanning multiple teams
- `api-contract` — API contract documentation between teams
- `handoff-template` — Handoff template from Dev to QA or Ops
- `three-amigos` — Facilitate a Three Amigos session (PM, Dev, QA alignment)
- `tech-debt-log` — Technical debt log with delivery impact assessment
- `shared-roadmap` — Unified roadmap view across multiple teams
- `conflict-resolution` — Framework for resolving cross-team priority conflicts

**Commands (3):**
- `/sync-meeting` — Prepare a multi-team sync meeting agenda
- `/integration-plan` — Build an integration plan for two or more teams
- `/resolve-conflict` — Framework for resolving a cross-team priority conflict

**Examples:**

```
How do I run a Three Amigos session for a feature three teams are building?
Create an API contract template between the mobile and backend teams
We have a priority conflict between the Platform and Product teams — how do I resolve it?
```

```
/sync-meeting 3 teams shipping together — Frontend, Backend, Data — weekly touchpoint
/integration-plan [attach team charters] — two teams integrating their modules in sprint 16
/resolve-conflict Platform team says API changes need 4 weeks, Product needs 2 weeks
```

---

### 6. pdm-metrics-reporting

Delivery metrics and retrospectives: DORA metrics, delivery forecasting, portfolio dashboards, post-mortems, and lessons learned.

**Skills (6):**
- `delivery-kpis` — Delivery KPIs and DORA metrics (deployment frequency, lead time, MTTR, change failure rate)
- `forecast-report` — Delivery forecast based on current velocity and backlog
- `portfolio-dashboard` — Portfolio-level delivery dashboard for multiple projects
- `post-mortem` — Blameless post-mortem for incidents or missed deliveries
- `retrospective` — Delivery-level retrospective (beyond the sprint level)
- `lessons-learned` — Lessons learned documentation after a release

**Commands (3):**
- `/delivery-report` — Delivery metrics report `weekly|sprint|release`
- `/post-mortem` — Blameless post-mortem after an incident or delay
- `/lessons-learned` — Document lessons learned after a release

**Examples:**

```
What DORA metrics should I report to leadership?
We missed our release date by 3 weeks — facilitate a post-mortem
Forecast our Q3 release based on current velocity [attach data]
```

```
/delivery-report sprint — Sprint 14 summary for three teams
/post-mortem Production incident on March 3rd caused 4-hour outage
/lessons-learned [attach release notes and retrospective data]
```

---

### 7. pdm-vendor-management

Vendor and third-party dependency management: assessments, SLA reviews, procurement timelines, and risk management.

**Skills (5):**
- `vendor-assessment` — Assess new vendors for integration readiness
- `sla-review` — Review SLA performance against contractual commitments
- `procurement-timeline` — Procurement timeline aligned to delivery plan
- `third-party-risk` — Risk assessment for third-party dependencies
- `vendor-communication` — Professional communication templates for vendors

**Commands (2):**
- `/vendor-assessment` — Assess a vendor for integration into the delivery plan
- `/sla-review` — Review SLA performance and flag violations

**Examples:**

```
We're onboarding a new payment gateway — assess readiness for Q2 release
Our cloud provider SLA was breached twice this quarter — what should I do?
Map procurement steps for a 3-month vendor integration
```

```
/vendor-assessment Stripe integration — 8-week timeline, two engineering teams
/sla-review [attach SLA doc and incident log] — 3 breaches in Q1
```

---

### 8. pdm-toolkit

General delivery manager utilities: decision logs, change requests, meeting facilitation, onboarding plans, and proofreading.

**Skills (5):**
- `meeting-facilitator` — Facilitate delivery meetings with structure and outcomes
- `decision-log` — Decision log with context, alternatives, and rationale
- `change-request` — Formal change request template
- `onboarding-plan` — Onboarding plan for a new team member in a delivery role
- `grammar-check` — Grammar, logic, and clarity check for delivery documents

**Commands (2):**
- `/decision-log` — Document a key decision with context and alternatives
- `/change-request` — Generate a formal change request
- `/proofread` — Review a delivery document for clarity and accuracy

**Examples:**

```
Document our decision to use feature flags for the v3 rollout
We need to add 2 weeks to the timeline — draft a change request
Review this release communication for clarity [attach draft]
```

```
/decision-log We decided to delay the API migration to Q3 — here's why
/change-request Adding 3 weeks to release timeline due to vendor delay
/proofread [attach status report draft]
```

---

## About

This marketplace is built for the realities of product delivery management: coordinating across teams, managing stakeholders, maintaining quality, and shipping predictably.

Frameworks and practices from:

- **DORA Research** — *Accelerate* (Forsgren, Humble, Kim)
- **SAFe** — Scaled Agile Framework (PI Planning, ART coordination)
- **Scrum** — Sprint ceremonies, Definition of Done, velocity
- **Kanban** — Flow metrics, WIP limits, cycle time
- **ITIL** — Incident management, change management, SLA reviews
- **Lean** — Waste reduction, value stream mapping

---

## License

MIT — see [LICENSE](./LICENSE).
