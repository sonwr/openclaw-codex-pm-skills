from pathlib import Path


def test_readme_mentions_governance_sandbox_scenario_report_outputs_alias_note() -> None:
    readme = Path('README.md').read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUTS_ALIAS_NOTE.md' in readme
    assert Path('docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUTS_ALIAS_NOTE.md').exists()
