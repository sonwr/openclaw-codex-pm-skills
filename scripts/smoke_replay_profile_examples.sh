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
assert payload['report_metadata']['qa_inventory_missing_check_refs'] == ['O2'], payload
PYJSON

echo 'replay profile smoke: PASS'
