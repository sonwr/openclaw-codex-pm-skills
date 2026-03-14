from pathlib import Path


def test_validate_openclaw_pm_repo45_stakeholder_types_wrapper_note() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / 'README.md').read_text(encoding='utf-8')
    note = (root / 'docs' / 'OPENCLAW_PM_REPO45_STAKEHOLDER_TYPES_WRAPPER_NOTE.md').read_text(encoding='utf-8')

    assert 'docs/OPENCLAW_PM_REPO45_STAKEHOLDER_TYPES_WRAPPER_NOTE.md' in readme
    assert 'stakeholder_types' in note
    assert 'five-line report' in note
