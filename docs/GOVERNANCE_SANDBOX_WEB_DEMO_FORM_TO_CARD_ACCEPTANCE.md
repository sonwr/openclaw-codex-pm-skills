# Governance Sandbox Web Demo Form-to-Card Acceptance

Use this note when the first governance-sandbox web demo should stay in one narrow lane: one scenario input form, one submit action, one result card, and one reproducible acceptance check.

Keep the slice stable:
- preserve one clear primary action on the form
- keep the result card readable without opening secondary tabs
- verify the same card content through a deterministic Playwright replay
- recover by trimming scope back to the last passing form-to-card path before widening UI polish
