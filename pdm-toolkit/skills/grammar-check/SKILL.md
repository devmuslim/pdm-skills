# Skill: grammar-check

## Purpose
Review delivery documents for grammar, clarity, logic, and professional tone — so communications are polished before they reach stakeholders.

## When to Use
- Before sending status reports, delay communications, or executive summaries
- Before publishing release notes or change requests
- When writing in a second language

## Framework: Document Review

### Review Dimensions

**1. Grammar and Spelling**
- Correct tense usage (delivery documents: mostly past for done, future for planned)
- Subject-verb agreement
- No spelling errors
- Punctuation consistency

**2. Clarity**
- Is each sentence saying one thing?
- Are acronyms defined on first use?
- Would a non-technical stakeholder understand it?
- Are there any ambiguous pronouns (this, it, they) with unclear referents?

**3. Logic and Structure**
- Does the document flow logically?
- Are there contradictions between sections?
- Does each paragraph have a clear main point?
- Does the conclusion follow from the content?

**4. Tone**
- Is the tone appropriate for the audience (executive, team, vendor)?
- Is it professional without being cold?
- Are there any phrases that could be misread as blaming or defensive?
- Does it avoid jargon for non-technical readers?

**5. Delivery-Specific Checks**
- Are all dates specific (not "next week" or "soon")?
- Are all owners named (not "the team")?
- Are actions specific (not "address the issue")?
- Is the RAG status clearly stated if applicable?

### Review Output Format

For each issue found:
- **Location**: [Section or sentence]
- **Issue**: [What's wrong]
- **Suggestion**: [Corrected version]

### Severity Classification
- 🔴 Must fix: Changes meaning or creates confusion
- 🟡 Should fix: Reduces clarity or professionalism
- 🟢 Optional: Minor style improvement

## Output Format
1. List of issues by severity
2. Corrected document (if short enough to reproduce)
3. Overall readiness: Ready to send / Needs minor fixes / Needs significant rework
