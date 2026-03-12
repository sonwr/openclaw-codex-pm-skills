from pathlib import Path


def test_readme_governance_sandbox_scenario_workshop_bundle_note():
    path = Path("docs/GOVERNANCE_SANDBOX_SCENARIO_WORKSHOP_BUNDLE_NOTE.md")
    text = path.read_text(encoding="utf-8")

    assert "scenario_workshop_bundle" in text
    assert "JSON/Markdown/HTML report bundle" in text
