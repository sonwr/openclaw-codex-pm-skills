# governance-sandbox report tag string note

Use newline-separated or comma-separated string tags in governance-sandbox scenario fixtures when a PM handoff needs lightweight metadata without switching to a list.

## Why it matters

- Keeps small YAML or JSON fixtures readable during PM review.
- Lets scenario authors reuse one compact tag field across CLI, report, and demo handoff notes.
- Avoids widening fixture structure just to carry a few memo labels.

## Preferred proof

1. Author one scenario fixture with `report_tags` as a short string.
2. Run the scenario-file replay that generates the JSON/Markdown/HTML bundle.
3. Confirm the generated report metadata still shows each tag as a separate label.

## PM handoff line

`report_tags` can stay as one comma-separated or newline-separated string when the scenario file should remain compact but report metadata still needs distinct labels.
