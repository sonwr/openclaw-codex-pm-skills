# Strict Fail Fixture — Missing Failure Evidence

## Scope
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

## 2) Checklist execution summary
- Functional checks (4/5 pass)
  - F1: PASS
  - F2: FAIL
    - Expected: Login success toast appears within 2 seconds
    - Observed: Spinner persisted for 10 seconds
    - First failure timestamp: 2026-03-07T04:10:00Z
    - Retry: FAIL
    - Failure classification: product
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
- F1 checkpoint: PASS - Submit valid credentials -> dashboard visible @ 2026-03-07T04:10:01Z `artifacts/f1.log`
- F2 checkpoint: FAIL - Submit valid credentials -> spinner persisted for 10 seconds @ 2026-03-07T04:10:02Z `artifacts/f2.log`
- F3 checkpoint: PASS - Submit empty required fields -> required validation shown @ 2026-03-07T04:10:03Z `artifacts/f3.log`
- F4 checkpoint: PASS - Press Enter on password field -> submit fired @ 2026-03-07T04:10:04Z `artifacts/f4.log`
- F5 checkpoint: PASS - Click logout -> redirected to `/login` @ 2026-03-07T04:10:05Z `artifacts/f5.log`
- V1 checkpoint: PASS - Capture baseline screenshot -> saved @ 2026-03-07T04:10:06Z `shots/v1.png`
- V2 checkpoint: PASS - Capture error-state screenshot -> saved @ 2026-03-07T04:10:07Z `shots/v2.png`
- V3 checkpoint: PASS - Capture dashboard screenshot -> saved @ 2026-03-07T04:10:08Z `shots/v3.png`
- O1 checkpoint: PASS - Submit wrong password -> stayed on `/login` @ 2026-03-07T04:10:09Z `artifacts/o1.trace`
- O2 checkpoint: PASS - Submit empty password -> client-side validation shown @ 2026-03-07T04:10:10Z `artifacts/o2.trace`

## 4) Signoff
- Regressions: 1
- Merge recommendation: **BLOCK**
- Replay readiness: **BLOCKED**
