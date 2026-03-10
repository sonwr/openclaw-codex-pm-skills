# Web QA Playwright Repair Stop Rules

Use these stop rules when deciding whether to keep repairing a failing run or hand it off.

## Stop repairing when

- the same blocker survives two verified reruns
- the next fix requires product or content approval instead of test repair
- evidence is incomplete and you cannot reproduce the failing checkpoint
- a new fix would hide the regression instead of explaining it

## Keep repairing when

- the failure is isolated to one selector, assertion, or environment assumption
- the replay confirms the same checkpoint and owner lane
- the next action can be validated in one short rerun

## Handoff note template

Record:

- failing checkpoint
- owner lane
- blocker summary
- proof from the latest rerun
- explicit next action (`repair`, `rerun`, or `handoff`)
