# Governance Sandbox Web Demo Checkpoint Rule

Use this note when the governance-sandbox web demo changes the scenario form, result card, or report download flow.

## Rule

Keep the first browser proof scoped to one deterministic path:

1. load one stable scenario fixture,
2. submit the form once,
3. confirm one visible result card,
4. confirm the generated report artifact links,
5. rerun the same path before widening UI scope.

## Why

This keeps UI work aligned with the same stability-first browser-proof principles used in Playwright-style interactive checks: deterministic inputs, step-by-step verification, and explicit recovery boundaries.

## Review cue

If the demo needs more than one form path or more than one result-card state to explain the change, split the work before merge.
