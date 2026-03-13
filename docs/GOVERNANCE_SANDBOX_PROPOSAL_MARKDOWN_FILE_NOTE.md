# governance-sandbox proposal markdown file note

When governance-sandbox scenario fixtures need longer proposal copy, keep the scenario metadata in JSON/YAML and move the proposal body into a neighboring markdown file.

Why this helps:
- Scenario files stay compact for replay and review.
- Proposal copy can be edited like a memo without reshaping stakeholder or report metadata.
- The same scenario replay still lands in the scenario-file-first + markdown/html/json report lane.

Recommended proof:
- Put the scenario fixture and proposal markdown file side by side.
- Run the scenario replay command that generates the report bundle.
- Confirm the rendered markdown/html outputs show the imported proposal body.
