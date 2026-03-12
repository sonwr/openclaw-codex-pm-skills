from pathlib import Path


def test_governance_sandbox_scenario_lab_bundle_note():
    path = Path('docs/GOVERNANCE_SANDBOX_SCENARIO_LAB_BUNDLE_NOTE.md')
    text = path.read_text(encoding='utf-8')

    assert 'scenario_lab_bundle' in text
    assert 'JSON/Markdown/HTML report bundle' in text
