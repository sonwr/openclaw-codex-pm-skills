# Governance Sandbox Scenario Case Wrapper Note

Keep `scenario_case` in the same delivery lane as existing scenario-file wrapper aliases.
Treat it as another small authoring convenience only when the replay still proves three things together:

1. the proposal and stakeholder payload load from one JSON/YAML scenario file,
2. the run emits the same JSON/Markdown/HTML report bundle, and
3. the wrapper growth does not bypass the current scenario-file-first priority.

This keeps wrapper alias expansion useful instead of turning into schema drift.
