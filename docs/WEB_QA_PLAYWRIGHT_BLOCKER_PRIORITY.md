# Web QA Playwright blocker-priority handoff

Use this note when a strict-plus run is BLOCKED and you need to choose the first repair lane without widening scope.

## Priority order
1. Repair missing stable target refs first.
2. Repair missing artifact/evidence refs second.
3. Repair timestamp/order gaps third.
4. Repair owner/next-action prose last.

## Why this order
- Stable refs make replay deterministic.
- Artifact refs make failures reviewable.
- Timestamp order keeps step-by-step verification trustworthy.
- Owner/next-action prose matters, but only after the blocked checkpoint can actually be replayed.

## Stepwise repair loop
1. Read `effective_replay_readiness_hotspot_primary_blocker` and section-scoped hotspot summaries from strict-plus JSON.
2. Fix one blocker family for one hotspot section.
3. Re-run the same preset/profile.
4. Confirm blocker counts and hotspot checkpoint IDs shrink before touching another section.

## Copy-ready operator cue
- First lane: repair the hotspot's primary blocker on the hottest blocked section.
- Do not widen to adjacent sections until blocker counts drop in the current lane.
