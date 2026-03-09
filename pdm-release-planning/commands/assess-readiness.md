# Command: /assess-readiness

## Description
Launch readiness assessment across 6 dimensions with a Go / No-Go recommendation.

## Usage
```
/assess-readiness [describe current release state]
```

## Workflow
1. Run `release-readiness` skill — score all 6 dimensions
2. Run `launch-checklist` skill — verify checklist status
3. Produce Go / No-Go recommendation

## After Completion
- If Go: → `/status-update` to communicate readiness
- If No-Go: → `/handle-delay` or `/cut-scope`
