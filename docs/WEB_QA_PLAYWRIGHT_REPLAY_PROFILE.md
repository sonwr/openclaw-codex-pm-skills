# Web QA Playwright replay profile

This note explains how the repository's `web-qa-playwright` validator profile maps to practical browser-testing discipline.

## Why this exists

Interactive browser QA tends to drift unless reports are:

- stable enough to replay,
- explicit about failure state,
- and strict about evidence capture.

The repo's strict replay profile is intentionally opinionated so CI can reject reports that are hard to audit later.

## Applied principles

These rules align with Playwright-style interactive testing guidance:

1. **Stability first** — keep deterministic checkpoints, timestamps, and explicit PASS/FAIL tokens.
2. **Reproducibility first** — require concrete artifact paths and target refs so another reviewer can follow the same trail.
3. **Stepwise verification** — keep checklist counts, execution log steps, and signoff numbers in sync.
4. **Failure recovery visibility** — when a check fails, capture classification, evidence, owner, and recovery plan.

## What the strict replay profile enforces

When contributors use the stricter replay aliases (`--playwright-interactive-profile`, `--deterministic-replay-profile`, `--strict-replay-profile`, or `--ci-replay-profile`), validation expects:

- normalized checkpoint timestamps,
- monotonic checkpoint order,
- explicit checkpoint status tokens,
- artifact references for failures and evidence capture,
- target refs for replayable UI targeting,
- signoff metadata that matches the checklist outcome.
- QA inventory bullets that map each claim to explicit checklist ids via `Checks:` for plan-to-execution traceability.

## Recommended report-writing loop

1. Capture the test scope (`URL`, viewport, account).
2. Execute checks in numbered order without skipping the execution log.
3. Attach screenshot/log/trace references inline as soon as they are created.
4. For failed checks, record classification + recovery details before signoff.
5. Re-run the validator before publishing the report to CI or PR comments.

## Stepwise replay recovery order

When a strict replay report fails, repair it in this order so the next rerun stays deterministic instead of introducing new drift:

1. **Restore stable target identity first** — fix missing/reused `ref=<id>` markers before touching screenshots or signoff text.
2. **Restore per-step evidence second** — make sure each failed or asserted checkpoint still points to the matching screenshot/log/trace artifact.
3. **Reconcile checkpoint chronology third** — verify timestamps remain monotonic and the execution log still accounts for the same F/V/O step set.
4. **Refresh failure recovery metadata last** — update classification, recovery owner, recovery plan, and next action only after the replay path is stable again.

Why this order matters:
- broken target refs make later screenshots ambiguous,
- missing artifacts hide whether the step actually reproduced,
- and editing recovery prose before the replay path is stable often creates misleading handoff notes.

This mirrors Playwright-interactive discipline: stabilize selectors/targets first, verify step-by-step evidence second, then publish the human-facing recovery plan.

When JSON automation drives the rerun, prefer `report_metadata.effective_replay_readiness_hotspot_checkpoint_ids` first. It gives one flattened, deterministic checkpoint list for the current hotspot section(s), so a bot or reviewer can paste the exact F/V/O ids to rerun before drilling into the per-section map.

## Practical use

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_pass.md \
  --ci-replay-profile \
  --json
```

Use the JSON payload when downstream automation needs machine-readable gating, and keep the markdown report readable enough for human triage.


JSON payloads also expose `active_profile_preset` (`strict-plus`, `playwright-interactive-profile`, `deterministic-replay-profile`, `strict-replay-profile`, or `ci-replay-profile`) so downstream CI can branch on one stable preset label instead of recomputing it from several booleans.

## QA inventory mapping contract examples

Use these snippets when you enable `--require-qa-inventory-check-refs` and want CI to compare the parser-facing shape directly.

### PASS vs FAIL smoke commands (copy/paste)

Use these paired commands when you want the Playwright-interactive traceability rule to show both the green path and the recovery path side-by-side.

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-check-refs-pass.json

python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_fail_missing_check_refs_only.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-missing-check-refs.json || true
```

Expected recovery signal:
- PASS fixture restores `qa_inventory_check_ref_count == 10`.
- FAIL fixture stays at `qa_inventory_check_ref_count == 0` until each QA inventory bullet carries `Checks:` ids again.

### PASS shape (`examples/web_qa_playwright_strict_plus_with_check_refs_pass.md`)

```json
{
  "status": "PASS",
  "active_profile_preset": "strict-plus",
  "require_qa_inventory_check_refs": true,
  "report_metadata": {
    "qa_inventory_check_refs": ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"],
    "qa_inventory_check_ref_count": 10,
    "missing_checkpoint_ids": [],
    "next_action_failed_check_refs": []
  }
}
```

### FAIL shape (same flag against a report without `Checks:` mappings)

```json
{
  "status": "FAIL",
  "active_profile_preset": "strict-plus",
  "require_qa_inventory_check_refs": true,
  "errors": [
    "qa inventory check refs: every QA inventory bullet must include 'Checks:' mapping"
  ],
  "report_metadata": {
    "qa_inventory_check_refs": [],
    "qa_inventory_check_ref_count": 0,
    "next_action_failed_check_refs": []
  }
}
```

Recovery rule: first compare `status`, then `require_qa_inventory_check_refs`, then the `report_metadata.qa_inventory_check_refs` list/count before reading the rest of the payload.

### Copy-paste CI smoke for the PASS mapping fixture

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-check-refs-pass.json
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path('.tmp/web-qa-check-refs-pass.json').read_text(encoding='utf-8'))
metadata = payload['report_metadata']
assert payload['status'] == 'PASS'
assert payload['require_qa_inventory_check_refs'] is True
assert metadata['qa_inventory_check_ref_count'] == 10
assert metadata['qa_inventory_check_refs'] == ['F1', 'F2', 'F3', 'F4', 'F5', 'V1', 'V2', 'V3', 'O1', 'O2']
assert metadata['next_action_failed_check_ref_count'] == 0
print('qa inventory PASS payload smoke: PASS')
PY
```

Use this when you want a parser-facing guard that the QA plan still maps every inventory bullet back to explicit checklist ids before signoff.

### Copy-paste CI smoke for the isolated missing-`Checks:` FAIL fixture

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_fail_missing_check_refs_only.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-missing-check-refs.json || true
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path('.tmp/web-qa-missing-check-refs.json').read_text(encoding='utf-8'))
assert payload['status'] == 'FAIL'
assert payload['error_count'] == 1
assert "qa inventory check refs" in payload['errors'][0]
assert "Checks:" in payload['errors'][0]
print('qa inventory FAIL payload smoke: PASS')
PY
```

Use this when replay metadata is otherwise healthy and you want one deterministic example that fails only the QA inventory `Checks:` mapping rule.

Recovery checklist: confirm `report_metadata.qa_inventory_check_ref_count == 0`, add `Checks:` mappings to each QA inventory bullet, then rerun the same fixture until the count returns to `10` for the canonical pass example.

### Copy-paste CI smoke for the isolated partial-coverage FAIL fixture

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_fail_partial_check_refs_only.md \
  --strict-plus \
  --require-qa-inventory-check-refs \
  --json-out .tmp/web-qa-partial-check-refs.json || true
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path('.tmp/web-qa-partial-check-refs.json').read_text(encoding='utf-8'))
metadata = payload['report_metadata']
assert payload['status'] == 'FAIL'
assert payload['error_count'] == 1
assert 'missing: O2' in payload['errors'][0]
assert metadata['qa_inventory_check_ref_count'] == 9
assert metadata['qa_inventory_missing_check_ref_count'] == 1
assert metadata['qa_inventory_missing_check_refs'] == ['O2']
print('qa inventory partial-coverage FAIL payload smoke: PASS')
PY
```

Use this when you need one deterministic fixture that proves the difference between malformed `Checks:` lines and incomplete coverage.

Recovery checklist: confirm `report_metadata.qa_inventory_missing_check_refs == ['O2']`, add the missing coverage back into the QA inventory bullets, then rerun until the count returns to `10`.

### Parser-facing QA inventory drift triage cheat sheet

- **Malformed mapping drift / 잘못된 `Checks:` 형식**
  - Expected signal: `error_count == 1` and `"Checks:" in errors[0]`
  - Metadata shape: `qa_inventory_check_ref_count == 10`, `qa_inventory_missing_check_ref_count == 0`
  - Meaning: the full QA universe is still present, but at least one inventory bullet omitted the required `Checks:` label.
- **Partial coverage drift / 일부 체크 누락**
  - Expected signal: `error_count == 1` and `"missing: O2" in errors[0]`
  - Metadata shape: `qa_inventory_check_ref_count == 9`, `qa_inventory_missing_check_ref_count == 1`, `qa_inventory_missing_check_refs == ['O2']`
  - Meaning: the mapping format is valid, but one checklist id dropped out of the QA inventory coverage graph.

Use this quick distinction when downstream CI or machine parsers need to decide whether to repair formatting or restore missing checklist coverage first.

### Isolated checkpoint-evidence drift cues

Use the isolated strict-plus fixtures when you need deterministic evidence about *which replay reference class drifted* before opening the full markdown report.

- Missing target refs (`examples/web_qa_playwright_strict_fail_missing_target_refs.md`) -> expect `report_metadata.missing_checkpoint_target_ref_ids` to list all 10 checks and `checkpoint_evidence_ref_coverage_rate == 0.0`.
- Reused target refs (`examples/web_qa_playwright_strict_fail_target_ref_reuse_only.md`) -> expect one uniqueness error while `checkpoint_target_ref_count == 9`, meaning coverage exists but stable target refs are no longer one-to-one.
- Missing artifact paths (`examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md`) -> expect `missing_checkpoint_artifact_ref_ids == ['F3']` and `checkpoint_evidence_ref_coverage_rate == 0.9`, which signals partial evidence capture drift rather than total replay-evidence loss.

Keep this split visible in CI so failure recovery can choose the right fix order: restore target identity first, then restore artifact completeness, then rerun the report.

### Parser-facing JSON snippets for QA inventory triage

Use these minimal payload shapes when downstream CI needs a quick fixture-to-parser contract reference without rerunning the full walkthroughs.

**Malformed mapping drift (`examples/web_qa_playwright_strict_fail_missing_check_refs_only.md`)**

```json
{
  "status": "FAIL",
  "error_count": 1,
  "errors": [
    "QA inventory check refs are required; add `Checks:` mappings to each QA inventory bullet."
  ],
  "report_metadata": {
    "qa_inventory_check_ref_count": 10,
    "qa_inventory_missing_check_ref_count": 0
  }
}
```

**Partial coverage drift (`examples/web_qa_playwright_strict_fail_partial_check_refs_only.md`)**

```json
{
  "status": "FAIL",
  "error_count": 1,
  "errors": [
    "QA inventory check refs are incomplete; missing: O2"
  ],
  "report_metadata": {
    "qa_inventory_check_ref_count": 9,
    "qa_inventory_missing_check_ref_count": 1,
    "qa_inventory_missing_check_refs": ["O2"]
  }
}
```

**Recovered PASS mapping (`examples/web_qa_playwright_strict_plus_with_check_refs_pass.md`)**

```json
{
  "status": "PASS",
  "require_qa_inventory_check_refs": true,
  "report_metadata": {
    "qa_inventory_check_ref_count": 10,
    "qa_inventory_missing_check_ref_count": 0,
    "next_action_failed_check_ref_count": 0
  }
}
```

## Alias smoke commands

Use one deterministic PASS fixture to prove every replay-profile alias still resolves to the same Playwright-interactive contract.

```bash
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md --playwright-interactive-profile --json-out .tmp/playwright-interactive-profile.json
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md --deterministic-replay-profile --json-out .tmp/deterministic-replay-profile.json
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md --strict-replay-profile --json-out .tmp/strict-replay-profile.json
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md --ci-replay-profile --json-out .tmp/ci-replay-profile.json
```

Check that each artifact reports the expected `active_profile_preset` value while preserving the same strict-plus validation surface.
