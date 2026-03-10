# Web QA Playwright strict-plus fail fixture map

Use this quick map when you need to pick the smallest strict-plus failure fixture for a validator replay or triage note.

## Fast picker

- **Artifact ref reuse drift** → `examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md`
- **Monotonic timestamp drift** → `examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md`
- **Status inconsistency drift** → `examples/web_qa_playwright_strict_fail_status_inconsistency_only.md`
- **Missing target refs** → `examples/web_qa_playwright_strict_fail_missing_target_refs.md`
- **Target-ref reuse drift** → `examples/web_qa_playwright_strict_fail_target_ref_reuse_only.md`
- **Missing artifact paths** → `examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md`

## How to use it

1. Pick the fixture that matches the broken checkpoint.
2. Run `python3 scripts/validate_web_qa_report.py --file <fixture> --strict-plus`.
3. Copy the failing checkpoint label into the PR or handoff note.

## Why this exists

The strict-plus fixtures are intentionally tiny and overlap in vocabulary.
This card keeps reviewers from opening the wrong repro artifact when they only need one isolated validator failure.
