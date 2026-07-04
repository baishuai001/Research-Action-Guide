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


if __name__ == "__main__":
    unittest.main()
