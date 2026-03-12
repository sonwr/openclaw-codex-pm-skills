from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioArtifactProofRuleTests(unittest.TestCase):
    def test_readme_mentions_scenario_artifact_proof_rule(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_ARTIFACT_PROOF_RULE.md', readme)

    def test_rule_doc_mentions_single_scenario_and_report_bundle(self) -> None:
        doc = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_ARTIFACT_PROOF_RULE.md').read_text(encoding='utf-8')
        self.assertIn('one imported scenario', doc)
        self.assertIn('JSON/Markdown/HTML report bundle', doc)


if __name__ == '__main__':
    unittest.main()
