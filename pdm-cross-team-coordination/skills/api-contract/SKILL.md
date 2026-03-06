# Skill: api-contract

## Purpose
Document a clear API contract between teams — setting expectations on endpoints, data formats, SLAs, and versioning before development begins.

## When to Use
- When a team is building an API that another team will consume
- Before integration work starts
- When preventing integration surprises late in the sprint

## Framework: API Contract

### API Contract Template

**Contract Name**: [API Name] v[version]
**Provider Team**: [Team]
**Consumer Teams**: [Teams]
**Agreed Date**: [Date]
**Review Date**: [Date — e.g., before code freeze]

---

**Base URL**: `https://api.example.com/v2/`
**Authentication**: Bearer Token / API Key / OAuth2
**Rate Limits**: 1000 req/min per consumer

---

**Endpoints**

| Method | Endpoint | Description | Response | SLA |
|--------|----------|-------------|----------|-----|
| GET | /users/{id} | Fetch user by ID | User object | < 200ms p95 |
| POST | /orders | Create new order | Order ID | < 500ms p95 |
| DELETE | /orders/{id} | Cancel order | 204 No Content | < 200ms p95 |

---

**Error Codes**

| Code | Meaning | Consumer Action |
|------|---------|----------------|
| 400 | Bad request | Fix request payload |
| 401 | Unauthorized | Refresh token |
| 404 | Not found | Handle gracefully |
| 429 | Rate limited | Retry with backoff |
| 500 | Server error | Alert and retry |

---

**Versioning Policy**
- Breaking changes: new major version (v2 → v3), 3-month notice
- Non-breaking changes: minor version, no notice required

---

**Sandbox / Mock**
Mock server available at: `https://mock-api.example.com/v2/`

## Output Format
1. Completed API contract document
2. Change log section for future updates
3. Suggested next command: `/integration-plan` or `/handoff-template`
