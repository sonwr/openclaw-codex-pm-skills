# Web QA Playwright signoff rerun status line

Use this when the validator already passes but the artifact still needs a narrow rerun before you call it handoff-ready.

## Purpose

Keep the update honest:

- validator-clean,
- blocked lane named,
- rerun scope explicit,
- owner obvious.

## Status line template

`Validator PASS; rerun <lane/checkpoint scope> for <failed-check or hotspot> with <owner> before signoff-ready handoff.`

## Good examples

- `Validator PASS; rerun functional hotspot checkpoints F1-F5 with QA owner before signoff-ready handoff.`
- `Validator PASS; rerun checkout lane for failed check visual.cart-total with frontend owner before signoff-ready handoff.`
- `Validator PASS; rerun section account-settings with product owner + QA reviewer before signoff-ready handoff.`

## Quick review

Before posting the line, confirm:

1. the rerun scope stays narrower than a whole-run replay,
2. the blocked lane or hotspot is named,
3. the owner or owner pair is present,
4. the sentence does not overclaim signoff readiness.
