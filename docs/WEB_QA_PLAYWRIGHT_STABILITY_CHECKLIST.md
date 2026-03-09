# WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST

A short operator checklist for replay-ready interactive browser QA.

This note complements:

- `docs/WEB_QA_PLAYWRIGHT_EXECUTION_LOOP.md`
- `docs/WEB_QA_PLAYWRIGHT_REPLAY_PROFILE.md`
- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`

## Why this exists

When a browser QA run flakes, teams often rerun too broadly and lose the original failure shape.
This checklist keeps reruns narrow, comparable, and easier to recover.

## Stability checklist

1. **Freeze the run profile first**
   - Keep the same preset (`--playwright-interactive-profile` or `--strict-plus`).
   - Reuse the same viewport, URL seed, and account fixture.
2. **Preserve stable references**
   - Do not rename checkpoint ids mid-triage.
   - Keep `ref=<id>` target refs and artifact naming stable across retries.
3. **Verify one layer at a time**
   - Fix selector drift before evidence drift.
   - Fix evidence drift before chronology drift.
   - Fix chronology drift before signoff wording.
4. **Capture proof immediately after each recovery step**
   - Re-run the isolated failing fixture first.
   - Save JSON output so the repaired invariant is machine-verifiable.
5. **Promote only after the isolated fixture passes**
   - Re-run the canonical PASS fixture after the narrow repair.
   - Update docs only after PASS and FAIL paths both stay reproducible.

## Recovery order

Use this order for blocked interactive runs:

1. target refs / selector stability
2. artifact paths / evidence capture
3. checkpoint timestamps / replay chronology
4. status consistency between checklist and execution log
5. signoff + next action handoff

## Copy-paste smoke loop

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_fail_missing_target_refs.md \
  --strict-plus \
  --json-out .tmp/web-qa-missing-target-refs.json

python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-pass.json
```

## Intended outcome

The first command should fail for exactly one isolated replay invariant.
The second command should pass and confirm that the broader handoff contract is still intact.
