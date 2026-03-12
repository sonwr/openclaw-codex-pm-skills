# Governance sandbox scenario artifact proof rule

Keep governance-sandbox progress evidence scoped to one imported scenario plus one regenerated JSON/Markdown/HTML report bundle in the same review pass.

Proof order:

1. Replay one JSON or YAML scenario file.
2. Regenerate the matching report bundle.
3. Verify the scenario source path and artifact paths are visible in the output payload or report metadata.
4. Only widen scope after that smallest replay stays green.
