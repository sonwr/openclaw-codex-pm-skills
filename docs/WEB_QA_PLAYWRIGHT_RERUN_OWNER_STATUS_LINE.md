# Web QA Playwright rerun owner status line

Use this when validation already passes but the artifact still needs a focused rerun handoff.

## Status line template

`Rerun owner: <owner> replays <lane/section> for <failed-check-id(s)> using <target/artifact>, then updates <proof output>.`

## Required fields

- **owner** — the person or lane that should act next
- **lane/section** — the narrowest replay scope that still covers the blocker
- **failed-check-id(s)** — the unresolved checks that justify the rerun
- **target/artifact** — the selector, page, fixture, or report asset needed for replay
- **proof output** — the report, screenshot, trace, or updated artifact expected after rerun

## Good example

`Rerun owner: checkout-qa replays payment-submit lane for failed-check ids checkout-submit-visible and checkout-success-toast using checkout trace + report fixture, then updates strict-plus report evidence.`

## Quick rule

If the sentence does not make the next owner, rerun scope, and expected proof obvious, it is not handoff-ready yet.
