# Web QA Playwright signoff exit criteria

Use this note when a strict-plus report already validates and you want one short exit rule before commit, merge approval, or rerun handoff.

## Exit criteria

1. The report passes `scripts/validate_web_qa_report.py --strict-plus`.
2. The signoff block says whether the run is `READY` or `BLOCKED`.
3. `Next action` names the smallest deterministic rerun or repair scope.
4. Every failed check named in the report is reflected in the handoff path.
5. The owner or routing lane is obvious enough that a different operator can continue without guessing.

## Ready vs blocked

- `READY` means no unresolved blocker is hiding behind vague prose.
- `BLOCKED` is acceptable when the failed checks, owner, and rerun scope are explicit.
- Validation-clean but vague handoff text is not exit-ready.

## Pair with

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_FIRST_LOOK.md`
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`
