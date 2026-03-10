# Web QA Playwright replay blocker triage

Use this guide when a run reports blocker-heavy failures and you need a short, consistent triage pass before replaying.

## Triage order

1. Group failed checks by the blocker they share.
2. Confirm whether the blocker is product behavior, selector drift, environment instability, or missing evidence.
3. Name the smallest rerun that can prove the blocker is cleared.
4. Record the owner and the expected evidence for signoff.

## Blocker prompts

### Product behavior blocker

- Which user-visible behavior is still wrong?
- What is the smallest path that proves the fix?
- Which failed check ids should disappear after replay?

### Selector drift blocker

- Is the page stable but the locator outdated?
- Can a deterministic replay prove the locator fix without broad exploratory reruns?
- Which screenshots or traces should be captured again?

### Environment blocker

- Is the failure tied to auth, seed data, network, or flaky setup?
- Can the runner repair the environment before replay?
- What one-line note should explain why the replay is trustworthy after repair?

### Missing evidence blocker

- Did the run fail because the evidence was absent rather than the behavior being wrong?
- Which artifact is missing: screenshot, trace, console log, or assertion payload?
- Should the next step be capture-first instead of fix-first?

## Good replay blocker summary

- `Checkout blockers: F1/F3 are selector drift, owned by qa-ui, rerun checkout trace + screenshot evidence after locator repair.`

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_SECTION_RERUN_CHECKLIST.md`
