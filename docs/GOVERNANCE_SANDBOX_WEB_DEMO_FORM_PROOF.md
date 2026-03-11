# Governance Sandbox Web Demo Form Proof

Use this note when the governance-sandbox web demo changes its input form, result cards, or report download flow.

## Proof loop

1. Load one known-good scenario fixture before editing copy or layout.
2. Confirm the proposal field, stakeholder input, and run action are all visible without scrolling on a laptop-width viewport.
3. Submit the scenario and verify the result cards show the recommendation, stakeholder stance mix, and report artifact links or labels.
4. Refresh and replay the same scenario once to confirm the flow stays deterministic.
5. If browser automation exists for the slice, keep selectors role-based and verify each user-visible checkpoint step by step.

## Hold the change if

- the form requires hidden knowledge to complete,
- the run button can be triggered before required fields are ready,
- the result cards hide the recommendation or stakeholder count,
- or the replay path depends on brittle timing instead of visible UI state.
