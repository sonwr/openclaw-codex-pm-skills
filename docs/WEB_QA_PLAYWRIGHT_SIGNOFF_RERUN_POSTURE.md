# Web QA Playwright signoff rerun posture

Use this micro-format when a signoff update needs to say whether a rerun is truly ready, still blocked, or intentionally waiting for a human owner.

## Status line

```text
Signoff rerun posture: <ready|blocked|waiting_on_owner> because <single gating fact>, next move <single rerun or handoff action>.
```

## Examples

- `Signoff rerun posture: ready because all failed checks now have fresh artifact paths, next move rerun the isolated blocked section.`
- `Signoff rerun posture: blocked because the visual evidence path is still missing, next move capture the screenshot bundle before retry.`
- `Signoff rerun posture: waiting_on_owner because checkout access needs a product decision, next move hand the unresolved check list to the owner.`

## When to use it

Use this line after the stricter signoff status summary when the reader also needs to know whether another rerun should happen immediately or stay parked behind a single blocker.
