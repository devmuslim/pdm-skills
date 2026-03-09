# Skill: acceptance-criteria

## Purpose
Write clear, testable acceptance criteria in Given/When/Then format for delivery stories — so Dev, QA, and Business share the same definition of done.

## When to Use
- During backlog grooming
- When stories are being written or refined
- When QA needs clear test cases

## Framework: Acceptance Criteria

### Format: Given / When / Then (Gherkin Style)
- **Given** — the initial context or state
- **When** — the action taken
- **Then** — the expected outcome

### Example: Login with SSO

```
Scenario 1 — Successful SSO Login
Given the user is on the login page
When the user clicks "Login with Google" and completes Google authentication
Then the user is redirected to the dashboard within 3 seconds
And their name is displayed in the top-right corner

Scenario 2 — SSO Login Failure
Given the user is on the login page
When the Google authentication fails or is cancelled
Then the user remains on the login page
And sees the message: "Login failed. Please try again."

Scenario 3 — Unauthorized User
Given the user is on the login page
When the user authenticates with a Google account not in the allowed domain
Then they are shown: "Access denied. Contact your administrator."
```

### Rules for Good Acceptance Criteria
- One scenario per distinct behaviour
- Avoid vague words: "quickly", "properly", "correctly" → use measurable specifics
- Include: happy path, error path, edge cases
- Each scenario should be independently testable
- Business readable — no technical jargon

### Step 1 — Gather Story Context
Ask for: what the feature does, who uses it, what can go wrong.

### Step 2 — Generate Scenarios
Always write at minimum:
- 1 happy path scenario
- 1 error/failure scenario
- 1 edge case (boundary condition or unusual input)

## Output Format
1. 3+ acceptance criteria scenarios in Given/When/Then format
2. Flag any ambiguities needing clarification before development starts
3. Suggested next command: `/test-strategy` or `/uat-plan`
