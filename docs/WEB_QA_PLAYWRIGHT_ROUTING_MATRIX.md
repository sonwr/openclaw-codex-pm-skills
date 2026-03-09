# Web QA Playwright routing matrix

Use this guide when a strict report is blocked and you need to decide who should take the next repair loop.

## Why this exists

Playwright-interactive work is more stable when the handoff names the failure class, evidence gap, and recovery owner before anyone retries the scenario.
That keeps reruns deterministic instead of bouncing a broken report between people.

## Routing rule

1. Read the failed-check classification (`selector`, `runtime`, `product`).
2. Read the recovery owner attached to the failed or unresolved check.
3. Confirm the next action includes both a stable `ref=` target and an artifact path when possible.
4. Retry only the smallest affected section after the owner confirms the fix.

## Matrix

| Failure classification | Typical owner | What to verify before rerun |
| --- | --- | --- |
| `selector` | QA automation / test owner | selector changed intentionally, stable target refs updated, screenshots or trace attached |
| `runtime` | app/frontend/backend owner | runtime error reproduced once, logs/trace attached, blocking dependency noted |
| `product` | product/design/feature owner | expected behavior clarified, acceptance decision documented, visual proof attached |

## Replay checklist

- Prefer rerunning only the failed section, not the whole scenario.
- Keep timestamps monotonic and attach the new artifact path.
- If the owner changes, update the handoff summary instead of leaving stale ownership in the report.
- If no owner is known yet, mark the report blocked and avoid optimistic replay language.
