import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ResearchActionGuideArchitectureTests(unittest.TestCase):
    def test_skill_has_new_identity(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: research-action-guide", text)
        self.assertIn("Research Action Guide", text)
        legacy_terms = [
            "zo" + "tero",
            "Workflow " + "Card",
            "Workflow " + "Matrix",
            "workflow" + "_card",
        ]
        for term in legacy_terms:
            self.assertNotIn(term, text)

    def test_no_legacy_library_term_anywhere(self):
        needle = ("zo" + "tero").lower()
        offenders = []
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".py", ".yaml", ".csv"}:
                if needle in path.read_text(encoding="utf-8").lower():
                    offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual([], offenders)

    def test_init_project_creates_new_structure(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "rag"
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "init_project.py"), "--project-root", str(project)],
                check=True,
                text=True,
                capture_output=True,
            )
            for folder in ["paper_decision_audits", "synthesis", "action_guides", "supervision"]:
                self.assertTrue((project / folder).is_dir())
            with (project / "decision_matrix.csv").open(encoding="utf-8", newline="") as f:
                header = next(csv.reader(f))
            self.assertIn("data_selection_logic", header)
            self.assertIn("annotation_logic", header)

    def test_validate_project_passes_initialized_project(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / "rag"
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "init_project.py"), "--project-root", str(project)],
                check=True,
                capture_output=True,
                text=True,
            )
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "validate_project.py"), "--project-root", str(project)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_bioinformatics_evidence_architecture_is_explicit(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        principle_path = ROOT / "references" / "bioinformatics_evidence_architecture.md"
        self.assertTrue(principle_path.is_file())

        principle_text = principle_path.read_text(encoding="utf-8")
        for phrase in [
            "not a catalog of common analyses",
            "falsifiable biological judgment",
            "Data selection defines the boundary",
            "object identity",
            "minimum sufficient route",
        ]:
            self.assertIn(phrase, principle_text)

        self.assertIn("Bioinformatics evidence architecture", skill_text)
        self.assertIn("references/bioinformatics_evidence_architecture.md", skill_text)

        for relative_path in [
            "references/paper_decision_audit_prompt.md",
            "references/cross_paper_evidence_synthesis_prompt.md",
            "references/research_action_guide_prompt.md",
            "references/quality_standards.md",
        ]:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("evidence architecture", text)
            self.assertIn("decision node", text)

    def test_bioinformatics_best_practice_guards_are_explicit(self):
        combined_text = "\n".join(
            [
                (ROOT / "SKILL.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "bioinformatics_evidence_architecture.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "paper_decision_audit_prompt.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "cross_paper_evidence_synthesis_prompt.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "research_action_guide_prompt.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "quality_standards.md").read_text(encoding="utf-8"),
                (ROOT / "references" / "decision_matrix_schema.md").read_text(encoding="utf-8"),
            ]
        )
        for phrase in [
            "statistical unit",
            "patient-level variation",
            "confounding factor",
            "validation hierarchy",
            "external cohort",
            "cross-platform",
            "functional validation",
            "minimum sufficient route",
            "analysis full stack",
        ]:
            self.assertIn(phrase, combined_text)

    def test_five_priority_assets_are_present_and_discoverable(self):
        required_files = [
            "references/bioinformatics_decision_ontology.md",
            "references/modules/single_cell_rna.md",
            "references/modules/spatial_transcriptomics.md",
            "references/modules/bulk_pan_cancer.md",
            "references/modules/clinical_survival.md",
            "references/supervision_rubric.md",
            "examples/golden_paper_decision_audit.md",
            "examples/weak_paper_decision_audit.md",
            "examples/golden_research_action_guide.md",
            "scripts/check_audit.py",
            "scripts/check_matrix.py",
            "scripts/check_corpus.py",
            "scripts/check_evidence_links.py",
        ]
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for relative_path in required_files:
            path = ROOT / relative_path
            self.assertTrue(path.is_file(), relative_path)
            self.assertIn(relative_path.replace("\\", "/"), skill_text)

        for relative_path in [
            "references/bioinformatics_decision_ontology.md",
            "references/supervision_rubric.md",
        ]:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("decision node", text)
            self.assertIn("failure mode", text)

    def test_new_validator_scripts_have_help(self):
        for script in [
            "check_audit.py",
            "check_matrix.py",
            "check_corpus.py",
            "check_evidence_links.py",
        ]:
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / script), "--help"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn("usage:", result.stdout.lower())

    def test_audit_examples_exercise_validator(self):
        golden = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check_audit.py"),
                "--file",
                str(ROOT / "examples" / "golden_paper_decision_audit.md"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, golden.returncode, golden.stdout + golden.stderr)

        weak = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check_audit.py"),
                "--file",
                str(ROOT / "examples" / "weak_paper_decision_audit.md"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, weak.returncode)

    def test_golden_action_guide_passes_validator(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check_research_action_guide.py"),
                "--file",
                str(ROOT / "examples" / "golden_research_action_guide.md"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_supervision_subagent_assets_are_present(self):
        required_files = [
            "references/supervision_subagent.md",
            "examples/golden_supervision_report.md",
            "scripts/check_supervision_report.py",
        ]
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for relative_path in required_files:
            path = ROOT / relative_path
            self.assertTrue(path.is_file(), relative_path)
            self.assertIn(relative_path.replace("\\", "/"), skill_text)

        supervisor_text = (ROOT / "references" / "supervision_subagent.md").read_text(encoding="utf-8")
        for phrase in [
            "supervision subagent",
            "REVISE",
            "HOLD",
            "life-science academic Chinese",
            "生命科学学术性",
            "direct evidence",
            "decision node",
            "minimum sufficient route",
        ]:
            self.assertIn(phrase, supervisor_text)

    def test_supervision_report_validator(self):
        help_result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_supervision_report.py"), "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, help_result.returncode, help_result.stdout + help_result.stderr)

        report_result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check_supervision_report.py"),
                "--file",
                str(ROOT / "examples" / "golden_supervision_report.md"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, report_result.returncode, report_result.stdout + report_result.stderr)

    def test_skill_engineering_protocol_is_discoverable(self):
        protocol_path = ROOT / "references" / "skill_engineering_protocol.md"
        self.assertTrue(protocol_path.is_file())

        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/skill_engineering_protocol.md", skill_text)

        protocol_text = protocol_path.read_text(encoding="utf-8")
        for phrase in [
            "science-superpowers",
            "observed baseline failure",
            "RED",
            "GREEN",
            "REFACTOR",
            "rationalization",
            "forward-test",
            "supervision",
            "Research-Action-Guide",
        ]:
            self.assertIn(phrase, protocol_text)

    def test_skill_engineering_protocol_defines_tiered_supervision(self):
        protocol_text = (ROOT / "references" / "skill_engineering_protocol.md").read_text(encoding="utf-8")
        for phrase in [
            "Tiered Supervision",
            "supervision intensity",
            "future agent reasons, decides, audits, supervises, or writes",
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "mechanical tests only",
            "skill-engineering supervisor",
            "red-team",
            "multi-role supervision",
            "No supervision subagent is required",
        ]:
            self.assertIn(phrase, protocol_text)


if __name__ == "__main__":
    unittest.main()
