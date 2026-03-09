# Sample

## Scope
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

## 2) Checklist execution summary
- Functional checks (4/5 pass)
  - F1: PASS
  - F2: FAIL
    - Expected: Inline error panel renders after invalid submit
    - Observed: Locator never resolved after submit
    - First failure timestamp: 2026-03-09T17:30:00Z
    - Retry: FAIL
    - Failure classification: selector
    - Evidence: `artifacts/f2-failure.png`
  - F3: PASS
  - F4: PASS
  - F5: PASS
- Visual checks (3/3 pass)
  - V1: PASS `shots/v1.png`
  - V2: PASS `shots/v2.png`
  - V3: PASS `shots/v3.png`
- Off-happy-path checks (2/2 pass)
  - O1: PASS
  - O2: PASS

## 3) Execution log
- F1 checkpoint: PASS ref=e12 `artifacts/f1-pass.png` 2026-03-09T17:25:00Z
- F2 checkpoint: FAIL ref=e13 `artifacts/f2-failure.png` 2026-03-09T17:30:00Z
- F3 checkpoint: PASS ref=e14 `artifacts/f3-pass.png` 2026-03-09T17:31:00Z
- F4 checkpoint: PASS ref=e15 `artifacts/f4-pass.png` 2026-03-09T17:32:00Z
- F5 checkpoint: PASS ref=e16 `artifacts/f5-pass.png` 2026-03-09T17:33:00Z
- V1 checkpoint: PASS ref=e17 `artifacts/v1-pass.png` 2026-03-09T17:34:00Z
- V2 checkpoint: PASS ref=e18 `artifacts/v2-pass.png` 2026-03-09T17:35:00Z
- V3 checkpoint: PASS ref=e19 `artifacts/v3-pass.png` 2026-03-09T17:36:00Z
- O1 checkpoint: PASS ref=e20 `artifacts/o1-pass.png` 2026-03-09T17:37:00Z
- O2 checkpoint: PASS ref=e21 `artifacts/o2-pass.png` 2026-03-09T17:38:00Z

## 4) Signoff
- Regressions: 1
- Merge recommendation: **BLOCK**
- Replay readiness: **BLOCKED**
- Next action: Assign the selector failure, capture owner-confirmed rerun evidence, and retry F2 before signoff
