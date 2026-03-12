from pathlib import Path


def test_readme_governance_sandbox_scenario_lab_note():
    path = Path("docs/GOVERNANCE_SANDBOX_SCENARIO_LAB_NOTE.md")
    text = path.read_text(encoding="utf-8")

    assert "scenario_lab" in text
    assert "wrapper alias" in text
