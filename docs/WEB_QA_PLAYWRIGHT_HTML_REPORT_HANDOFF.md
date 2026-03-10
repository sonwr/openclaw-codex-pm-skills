# WEB_QA_PLAYWRIGHT_HTML_REPORT_HANDOFF

Use this note when a Playwright QA run needs an HTML-ready handoff instead of a raw JSON dump.

## Why this matters

- reviewers can skim the headline result, blocker hotspot, and next action without opening a parser
- a stable HTML summary is easier to archive in CI artifacts and attach to review threads
- the HTML view should mirror, not replace, the structured JSON source of truth

## Minimum HTML handoff sections

1. Scenario name and run timestamp
2. Pass/fail summary with strict-mode context
3. Effective replay hotspot and affected checkpoint refs
4. Top unresolved blockers with owner-ready language
5. Recommended next action and rerun scope

## Guardrails

- keep field names aligned with the JSON report so handoff cards stay reproducible
- do not invent new blocker classes only in the HTML layer
- prefer one compact card per hotspot rather than long narrative walls
- if signoff data is incomplete, state the missing field explicitly in the HTML summary
