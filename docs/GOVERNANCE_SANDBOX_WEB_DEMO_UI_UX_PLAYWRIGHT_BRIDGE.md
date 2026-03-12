# Governance Sandbox Web Demo UI/UX + Playwright Bridge

Use this note when the next governance-sandbox slice touches the first web demo.

Keep the scope narrow and reproducible:
- one scenario input form
- one result card
- one report-download proof

Apply UI/UX review rules first so the screen hierarchy stays obvious, then apply Playwright replay rules so the same slice is stable under automation. Do not widen scope until the same scenario fixture can drive both the visible card state and the saved report artifact path without flaky selectors or hidden copy.
