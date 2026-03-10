# WEB QA Playwright next-action rerun artifact check

Use this note when validation already passes, the hotspot is known, and you need to decide whether the next action names enough rerun evidence to hand off safely.

## Quick check

Confirm that the next-action sentence names all three items below:

1. the failed check id or blocked lane,
2. the artifact or evidence that must be refreshed,
3. the rerun scope that should stay narrow.

## Ready wording pattern

Use a compact sentence like:

> Rerun `F2` after refreshing `artifacts/f2-failure.png` and keep scope limited to the login spinner path.

## Hold wording pattern

Do not call the handoff rerun-ready when the sentence only says to "rerun" without naming the failed lane and replacement evidence.

## Why this exists

A validator-clean report can still create replay drift when the next action omits the artifact to refresh. This check keeps rerun instructions specific enough for a second operator to follow without reopening the whole report.
