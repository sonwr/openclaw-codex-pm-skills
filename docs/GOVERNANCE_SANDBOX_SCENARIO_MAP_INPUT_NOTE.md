# Governance Sandbox scenario map input note

When authoring a small scenario file, you can declare `stakeholders` as a YAML or JSON object map from stakeholder name to preset.

Example:

```yaml
stakeholders:
  DAO council: dao
  Delegate cohort: delegates
  Builder circle: contributors
```

Use this short form when you want scenario-file input to stay readable while still producing preset-backed stakeholder responses in the JSON, markdown, and HTML report bundle.
