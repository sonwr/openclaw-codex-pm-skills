# GOVERNANCE_SANDBOX_WEB_DEMO_ENTRY_CHECK

Use this before expanding the governance-sandbox web demo.

## Entry bar

Confirm all four are true:

- one scenario file can replay the current demo input
- one report bundle command still emits JSON, Markdown, and HTML artifacts
- the form shows a single primary task instead of multiple competing actions
- the result view keeps recommendation, stakeholder snapshot, and download/report actions on the first screen

## Why this exists

The web demo should feel deterministic and reviewable before it feels feature-rich.
That keeps UI work aligned with scenario-file proof, report-output proof, and stable browser testing.
