# WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_REPAIR_DECIDER

Use this card after the validator already passes but the report is still not ready to hand off as a clean rerun request.

## Choose focused rerun when
- the blocked lane is already explicit,
- the failing check ids are already named,
- the stable target or page area is already present,
- and the next proof artifact is obvious to the receiver.

## Choose repair before rerun when
- the blocker sentence still hides which lane is hottest,
- multiple failed lanes still compete for attention,
- owner routing is still ambiguous,
- or the next action does not say what proof must be produced.

## Fast wording rule
- If a teammate can rerun one lane without reopening the full report, ask for a rerun.
- If they still need to interpret the report structure first, ask for repair.

## Output pattern
- **Rerun-ready:** "Validator PASS. Keep scope on <lane>; rerun against <target> and attach <proof artifact>."
- **Repair-first:** "Validator PASS, but the handoff still needs one clearer lane, target, or proof artifact before rerun."
