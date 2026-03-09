# PR Merge Policy (Web QA)

Use this policy when a PR changes browser flows, UI states, selectors, screenshots, or signoff evidence.

The goal is simple: **do not merge a web QA change unless the run is replayable, evidence-backed, and easy for the next owner to recover if it fails.**

This policy intentionally mirrors Playwright-interactive-style operating principles:

1. **Stability first** — keep the same target refs, artifact naming, and checklist shape.
2. **Reproducibility first** — attach a deterministic validator command plus JSON artifact.
3. **Step-by-step verification** — require checkpoint-level proof, not only a prose summary.
4. **Failure recovery** — blocked runs must still name the failing checks, owner, and next action.

## Merge-ready checklist

A PR is merge-ready only when **all** conditions below are true.

1. Regression count is **0**.
2. QA checklist is attached and completed with the fixed structure:
   - functional checks: 5
   - visual checks: 3
   - off-happy-path checks: 2
3. Every checkpoint line keeps deterministic replay cues:
   - explicit `PASS`/`FAIL`
   - stable `ref=<id>` target ref
   - inline artifact path
   - timestamp when strict-plus profile requires it
4. Visual claims include screenshot evidence for the related `V*` checks.
5. Signoff is explicit and consistent:
   - reported regressions = actual failed checks
   - merge recommendation is present
   - replay readiness is present
6. The final markdown artifact passes the validator with the replay-oriented contract used by CI.

## Copy-paste validation commands

### Merge-ready PASS check

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --require-qa-inventory-full-coverage \
  --json-out artifacts/validation.json
```

Expected outcome:

- validator exit code `0`
- JSON artifact `status="PASS"`
- `active_profile_preset="strict-plus"`
- `report_metadata.failed_check_ids=[]`

### Blocked-run handoff check

Use this when the run is expected to fail but still needs deterministic recovery metadata.

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_combined_fail.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --require-next-action \
  --require-next-action-failed-check-ref \
  --require-failure-recovery-plan \
  --require-failure-recovery-owner \
  --json-out artifacts/blocked-run.json
```

Expected outcome:

- validator exit code is non-zero
- JSON artifact still exposes the blocked-run handoff fields needed for the next rerun
- failures remain classified instead of disappearing into free-form markdown

## Hard block conditions

Do **not** merge when any of these conditions is true:

- any regression is present
- screenshots are missing for visual claims
- QA inventory/checklist sections are missing
- checkpoint refs or artifact paths are missing under strict-plus policy
- signoff fields disagree with checklist results
- the blocked run lacks `Next action:`, failed-check refs, recovery owner, or recovery plan

## What to attach in the PR description

Keep the PR body lightweight but reproducible:

1. validator command used
2. exit code
3. generated artifact path (`artifacts/*.json`)
4. short statement of status (`PASS` merge-ready / `FAIL` blocked)
5. if blocked, the first failed check id to recover next

## Reviewer shortcut

Ask these questions in order:

1. Can I replay this run with one command?
2. Do the checkpoint refs and evidence paths make the failure reproducible?
3. If it failed, does the next owner know exactly which check to recover first?
4. If it passed, does the signoff clearly justify merge readiness?

If any answer is "no", keep the PR blocked.
