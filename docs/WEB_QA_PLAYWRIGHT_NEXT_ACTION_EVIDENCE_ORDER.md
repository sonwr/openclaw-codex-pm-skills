# Web QA Playwright next-action evidence order

Use this quick rule when several failed checks compete for the next replay or repair pass.

## Order of evidence strength

1. **Target ref + artifact ref + timestamp** — strongest replay handoff; the failed check can usually be retraced immediately.
2. **Target ref + artifact ref** — good replay handoff; add timestamp on the next rerun if possible.
3. **Target ref only** — selector or UI location is recoverable, but proof is still thin.
4. **Artifact ref only** — visual proof exists, but the replay path is weak.
5. **Narrative only** — treat as the lowest-confidence handoff and enrich it before signoff.

## Practical tie-break

When two failed checks share the same priority, replay the one with weaker evidence first:

- narrative only beats artifact-only for urgency,
- artifact-only beats target-only when the failure class is selector or runtime,
- target-only beats fully referenced checks because the next run should focus on evidence completion.

## Maintenance note

Pair this card with `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_CARD.md` and `docs/WEB_QA_PLAYWRIGHT_CHECKPOINT_EVIDENCE_LADDER.md` so triage uses the same vocabulary for replay readiness.
