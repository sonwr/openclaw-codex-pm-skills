# GOVERNANCE_SANDBOX_UI_UX_PRO_MAX_BRIDGE

Use this note when shaping the `governance-sandbox` web demo surface.

## Core bridge
- Lead with a single primary task: input scenario, run simulation, inspect decision cards.
- Keep the first screen focused on one happy path before adding governance-heavy explanation.
- Show proposal, stakeholders, and report outputs as separate cards so state changes stay obvious.
- Prefer progressive disclosure: advanced knobs belong below the fold or behind details panels.
- Preserve reproducibility: every visible state in the demo should map back to a scenario file or CLI artifact.

## Playwright-friendly UI rules
- Stable labels for form fields and result cards.
- Deterministic submit action and explicit success state.
- Report cards should expose scenario name, recommendation, and stakeholder count without scrolling.
- Error states should tell the operator exactly which input field is incomplete.
