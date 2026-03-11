# Governance Sandbox nested scenario inputs note

Use nested `scenario.inputs` when a fixture should keep scenario metadata and runnable proposal/stakeholder input in one block.

Small replay rule:
- keep `scenario.name` and `scenario.context` beside `scenario.inputs`
- store runnable `proposal` plus `stakeholders`/`stakeholder_map` under `scenario.inputs`
- rerun one CLI smoke check before widening aliases or report output changes
