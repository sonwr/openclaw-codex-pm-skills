#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PASS_FIXTURE="examples/web_qa_playwright_strict_plus_with_check_refs_pass.md"
FAIL_FIXTURE="examples/web_qa_playwright_strict_fail_missing_check_refs_only.md"
PARTIAL_FAIL_FIXTURE="examples/web_qa_playwright_strict_fail_partial_check_refs_only.md"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

profiles=(
  "--playwright-interactive-profile"
  "--deterministic-replay-profile"
  "--strict-replay-profile"
  "--ci-replay-profile"
)

for profile in "${profiles[@]}"; do
  out="$TMP_DIR/$(echo "$profile" | tr -d '-' | tr ' ' '_').json"
  python3 scripts/validate_web_qa_report.py     --file "$PASS_FIXTURE"     "$profile"     --require-qa-inventory-check-refs     --require-qa-inventory-full-coverage     --json-out "$out" >/dev/null
  python3 - "$out" <<'PYJSON'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert payload['status'] == 'PASS', payload
assert payload['report_metadata']['qa_inventory_check_refs'] == ['F1','F2','F3','F4','F5','V1','V2','V3','O1','O2'], payload
assert payload['report_metadata']['qa_inventory_check_ref_count'] == 10, payload
assert payload['report_metadata']['checkpoint_section_counts'] == {'functional': 5, 'visual': 3, 'off_happy': 2}, payload
assert payload['report_metadata']['signoff_field_coverage_rate'] == 0.75, payload
assert payload['report_metadata']['missing_signoff_fields'] == ['next_action'], payload
assert payload['report_metadata']['unresolved_failed_check_ids'] == [], payload
PYJSON
done

set +e
python3 scripts/validate_web_qa_report.py   --file "$FAIL_FIXTURE"   --strict-plus   --require-qa-inventory-check-refs   --json > "$TMP_DIR/fail.json"
status=$?
set -e
if [[ "$status" -eq 0 ]]; then
  echo "expected FAIL fixture to fail validation" >&2
  exit 1
fi
python3 - "$TMP_DIR/fail.json" <<'PYJSON'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert payload['status'] == 'FAIL', payload
assert payload['error_count'] == 1, payload
assert 'qa inventory check refs' in payload['errors'][0], payload
assert payload['report_metadata']['qa_inventory_check_ref_count'] == 10, payload
assert payload['report_metadata']['qa_inventory_missing_check_ref_count'] == 0, payload
assert payload['report_metadata']['qa_inventory_check_ref_coverage_rate'] == 1.0, payload
assert payload['report_metadata']['checkpoint_section_counts'] == {'functional': 5, 'visual': 3, 'off_happy': 2}, payload
PYJSON

set +e
python3 scripts/validate_web_qa_report.py   --file "$PARTIAL_FAIL_FIXTURE"   --strict-plus   --require-qa-inventory-check-refs   --json > "$TMP_DIR/partial-fail.json"
partial_status=$?
set -e
if [[ "$partial_status" -eq 0 ]]; then
  echo "expected partial coverage fixture to fail validation" >&2
  exit 1
fi
python3 - "$TMP_DIR/partial-fail.json" <<'PYJSON'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert payload['status'] == 'FAIL', payload
assert payload['error_count'] == 1, payload
assert 'missing: O2' in payload['errors'][0], payload
assert payload['report_metadata']['qa_inventory_check_ref_count'] == 9, payload
assert payload['report_metadata']['qa_inventory_missing_check_ref_count'] == 1, payload
assert payload['report_metadata']['qa_inventory_check_ref_coverage_rate'] == 0.9, payload
assert payload['report_metadata']['qa_inventory_missing_check_refs'] == ['O2'], payload
PYJSON

python3 - "$TMP_DIR/fail.json" "$TMP_DIR/partial-fail.json" <<'PYJSON'
import json
import sys
from pathlib import Path
malformed = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
partial = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
assert malformed['report_metadata']['qa_inventory_check_ref_count'] == 10, malformed
assert malformed['report_metadata']['qa_inventory_missing_check_ref_count'] == 0, malformed
assert partial['report_metadata']['qa_inventory_check_ref_count'] == 9, partial
assert partial['report_metadata']['qa_inventory_missing_check_ref_count'] == 1, partial
assert malformed['report_metadata']['next_action_failed_check_refs'] == [], malformed
assert partial['report_metadata']['next_action_failed_check_refs'] == [], partial
print('qa inventory malformed-vs-partial triage smoke: PASS')
PYJSON

echo 'replay profile smoke: PASS'


ISOLATED_FAIL_FIXTURES=(
  "examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md|artifact_ref_reuse|checkpoint artifact ref uniqueness|checkpoint_artifact_ref_count|9"
  "examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md|monotonic_timestamp|checkpoint timestamp order|checkpoint_timestamp_count|10"
  "examples/web_qa_playwright_strict_fail_missing_timestamp_only.md|missing_timestamp|checkpoint timestamps|checkpoint_timestamp_count|9"
  "examples/web_qa_playwright_strict_fail_status_inconsistency_only.md|status_inconsistency|checkpoint/check status consistency|checkpoint_target_ref_count|10"
  "examples/web_qa_playwright_strict_fail_missing_target_refs.md|missing_target_refs|checkpoint target refs|checkpoint_target_ref_count|0"
  "examples/web_qa_playwright_strict_fail_target_ref_reuse_only.md|target_ref_reuse|checkpoint target ref uniqueness|checkpoint_target_ref_count|9"
  "examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md|missing_artifact_paths|checkpoint artifact paths|checkpoint_artifact_ref_count|9"
)

for fixture_spec in "${ISOLATED_FAIL_FIXTURES[@]}"; do
  IFS='|' read -r fixture slug expected_error metadata_key metadata_expected <<<"$fixture_spec"
  out="$TMP_DIR/${slug}.json"
  set +e
  python3 scripts/validate_web_qa_report.py     --file "$fixture"     --strict-plus     --json-out "$out" >/dev/null
  status=$?
  set -e
  if [[ "$status" -eq 0 ]]; then
    echo "expected isolated strict-plus fixture to fail validation: $fixture" >&2
    exit 1
  fi
  python3 - "$out" "$expected_error" "$metadata_key" "$metadata_expected" "$slug" <<'PYJSON'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert payload['status'] == 'FAIL', payload
slug = sys.argv[5]
expected_error_count = 2 if slug == 'missing_timestamp' else 1
assert payload['error_count'] == expected_error_count, payload
assert sys.argv[2] in payload['errors'][0], payload
metadata = payload['report_metadata']
key = sys.argv[3]
expected = int(sys.argv[4])
assert metadata[key] == expected, (key, metadata.get(key), expected)
if slug == 'missing_target_refs':
    assert metadata['missing_checkpoint_target_ref_ids'] == ['F1', 'F2', 'F3', 'F4', 'F5', 'V1', 'V2', 'V3', 'O1', 'O2'], metadata
    assert metadata['checkpoint_evidence_ref_coverage_rate'] == 0.0, metadata
    assert metadata['missing_checkpoint_evidence_ref_count_by_section'] == {'functional': 5, 'visual': 3, 'off_happy': 2}, metadata
    assert metadata['replay_readiness_blocker_count_by_section'] == {'functional': 10, 'visual': 6, 'off_happy': 4}, metadata
    assert metadata['replay_readiness_blocker_coverage_rate_by_section'] == {'functional': 2.0, 'visual': 2.0, 'off_happy': 2.0}, metadata
    assert metadata['effective_replay_readiness'] == 'BLOCKED', metadata
    assert metadata['replay_readiness_effective_changed'] is True, metadata
    assert metadata['effective_replay_readiness_added_blocker_keys_by_section'] == {'functional': [], 'visual': [], 'off_happy': []}, metadata
    assert metadata['effective_replay_readiness_blocker_delta_by_section'] == {'functional': 0, 'visual': 0, 'off_happy': 0}, metadata
if slug == 'missing_artifact_paths':
    assert metadata['missing_checkpoint_artifact_ref_ids'] == ['F3'], metadata
    assert metadata['checkpoint_evidence_ref_coverage_rate'] == 0.9, metadata
    assert metadata['missing_checkpoint_evidence_ref_ids'] == ['F3'], metadata
if slug == 'missing_timestamp':
    assert metadata['missing_checkpoint_timestamp_ids'] == ['O2'], metadata
    assert metadata['missing_checkpoint_timestamp_count_by_section'] == {'functional': 0, 'visual': 0, 'off_happy': 1}, metadata
    assert metadata['missing_checkpoint_timestamp_coverage_rate_by_section'] == {'functional': 0.0, 'visual': 0.0, 'off_happy': 0.5}, metadata
    assert metadata['replay_readiness_blocker_keys_by_section'] == {'functional': [], 'visual': [], 'off_happy': ['missing_timestamps']}, metadata
if slug == 'artifact_ref_reuse':
    assert metadata['checkpoint_reused_artifact_ref_count_by_section'] == {'functional': 0, 'visual': 1, 'off_happy': 0}, metadata
if slug == 'target_ref_reuse':
    assert metadata['checkpoint_reused_target_ref_count_by_section'] == {'functional': 1, 'visual': 0, 'off_happy': 0}, metadata
PYJSON
  if [[ "$slug" == "missing_target_refs" || "$slug" == "missing_artifact_paths" ]]; then
    python3 - "$out" "$slug" <<'PYNEXT'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
metadata = payload['report_metadata']
slug = sys.argv[2]
if slug in {'missing_target_refs', 'missing_artifact_paths'}:
    assert metadata['replay_readiness'] == 'READY', metadata
    assert metadata['effective_replay_readiness'] == 'BLOCKED', metadata
else:
    assert metadata['effective_replay_readiness'] == 'BLOCKED', metadata
print('next-action recovery smoke: PASS')
PYNEXT
  fi
done
