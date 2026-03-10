# WEB_QA_PLAYWRIGHT_RERUN_OWNER_BOUNDARY

Use this note when a Playwright validation artifact passes, but the next action still needs to stay tightly scoped to one blocked lane and one owner.

## Use this when

- the validator already passed,
- one blocked lane clearly owns the next rerun, and
- you do **not** want the handoff to sound like a full-run replay request.

## One-line owner-aware boundary

> Keep the rerun scoped to the highest-blocker lane, name the owner, and cite the exact artifact or selector needed for that single repair pass.

## Quick check

Before posting the handoff, confirm all three stay visible:

1. **lane** — which failed lane gets the rerun first
2. **owner** — who should take that rerun
3. **evidence target** — which artifact, selector, or proof file anchors the rerun

If any of those are missing, the note is still validator-clean but not owner-ready.
