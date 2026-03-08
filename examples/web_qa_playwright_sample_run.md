# Web QA Playwright — Sample Interactive Run

This sample demonstrates a deterministic QA run with inventory + checklist flow.

## Scope

- Product area: Login
- URL: `https://example.test/login`
- Viewport: `1366x768`
- Test account: `qa.user@example.test`

## 1) QA Inventory (condensed)

### Requirements and claims
- Requested requirements:
  - User can log in with valid credentials.
  - Error is shown for invalid credentials.
- Implemented user-visible behavior:
  - Login form renders email/password controls and submit button.
  - Auth success redirects to dashboard.
  - Invalid auth shows inline error message.
- Claims to sign off:
  - Login happy path works.
  - Error handling path is visible and recoverable.

### Control/state coverage map

| Control or behavior | Trigger/action | Expected state change | Functional check id | Visual check id | Evidence |
|---|---|---|---|---|---|
| Email + password submit | Click "Sign in" with valid creds | Redirect `/dashboard` | F1 | V1 | `shots/f1-dashboard.png` |
| Inline error panel | Submit invalid password | Error text appears, stay on `/login` | F2 | V2 | `shots/f2-error.png` |

### Off-happy-path scenarios
- O1:
  - Setup: valid email + wrong password
  - Action: submit form
  - Expected resilient behavior: inline error appears, no redirect
- O2:
  - Setup: missing password
  - Action: submit form
  - Expected resilient behavior: client validation message, submit blocked

## 2) Checklist execution summary

- Functional checks (5/5 pass)
  - F1: Valid login redirects to dashboard (PASS)
  - F2: Invalid password shows inline error (PASS)
  - F3: Missing password blocks submit (PASS)
  - F4: Keyboard Enter submits form (PASS)
  - F5: Logout returns to login (PASS)
- Visual checks (3/3 pass)
  - V1: Login form baseline layout stable (PASS) `shots/v1-login-layout.png`
  - V2: Error panel spacing and contrast acceptable (PASS) `shots/v2-error-panel.png`
  - V3: Dashboard hero card visible after login (PASS) `shots/v3-dashboard-hero.png`
- Off-happy-path checks (2/2 pass)
  - O1: Wrong password path (PASS)
  - O2: Empty password path (PASS)

## 3) Failure recovery note (template example)

- First failure timestamp: `2026-03-07T00:11:43Z`
- Step: F2 click submit with invalid password
- Expected: inline error panel visible
- Observed: no error panel rendered
- Single retry: page reload + repeat F2
- Retry result: PASS
- Isolation: transient runtime timing issue (not selector/product)

## 4) Execution log

- F1 checkpoint: Redirect confirmed to `/dashboard`; profile menu visible.
- F2 checkpoint: Inline auth error rendered after invalid credential submit.
- F3 checkpoint: Empty password blocked submit with client-side validation.
- F4 checkpoint: Enter key submit triggered auth request exactly once.
- F5 checkpoint: Logout returned session to `/login` and cleared auth cookie.
- V1 checkpoint: Captured baseline layout shot for login form alignment.
- V2 checkpoint: Captured error-state shot and verified contrast/spacing.
- V3 checkpoint: Captured dashboard hero shot after successful login.
- O1 checkpoint: Wrong-password scenario remained on `/login` with error feedback.
- O2 checkpoint: Empty-password scenario showed required-field validation.

## 5) Signoff

- Regressions: 0
- Merge recommendation: **APPROVE**
