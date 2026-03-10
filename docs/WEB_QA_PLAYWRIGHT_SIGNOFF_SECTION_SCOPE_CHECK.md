# Web QA Playwright signoff section-scope check

Use this one-screen check after validation passes but before you claim the entire run is signoff-ready.

## Ask these three questions

1. **Which section is actually ready?**
   - Name the ready lane explicitly (`functional`, `visual`, or `off_happy`).
2. **Which lane is still blocked?**
   - Keep the blocked lane visible instead of letting a passing validator imply whole-run readiness.
3. **Does the handoff sentence preserve that boundary?**
   - Prefer wording like `functional is signoff-ready; visual remains blocked on V2 evidence refresh`.

## Safe wording pattern

`<ready section> is signoff-ready for handoff; <blocked section> remains blocked on <failed check ids or missing artifact>.`

## Avoid

- `The report is fully signoff-ready.`
- `Everything is ready to hand off.`
- Any summary that hides a still-blocked lane after a validator PASS.

## Exit signal

If the sentence still makes a reviewer ask `ready for which section?`, keep the handoff section-scoped and do not flatten it into whole-run readiness.
