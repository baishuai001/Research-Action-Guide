#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


REQUIRED_FOLDERS = [
    "paper_decision_audits",
    "synthesis",
    "action_guides",
    "supervision",
]

REQUIRED_FILES = [
    "config.yaml",
    "literature_corpus.csv",
    "decision_matrix.csv",
    "translation_manifest.csv",
]

REQUIRED_MATRIX_COLUMNS = {
    "paper_id",
    "title",
    "evidence_depth",
    "evidence_bottleneck",
    "data_selection_logic",
    "qc_integration_logic",
    "annotation_logic",
    "statistical_unit_logic",
    "confounding_factor_logic",
    "downstream_selection_logic",
    "validation_hierarchy",
    "minimum_sufficient_route",
    "reusable_rule",
    "audit_path",
}


def read_header(path: Path) -> set[str]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return set(next(csv.reader(f), []))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default="./research_action_guide")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors: list[str] = []

    if not root.exists():
        errors.append(f"missing project root: {root}")
    for folder in REQUIRED_FOLDERS:
        if not (root / folder).is_dir():
            errors.append(f"missing folder: {folder}")
    for file_name in REQUIRED_FILES:
        if not (root / file_name).is_file():
            errors.append(f"missing file: {file_name}")

    matrix = root / "decision_matrix.csv"
    if matrix.exists():
        missing = REQUIRED_MATRIX_COLUMNS - read_header(matrix)
        if missing:
            errors.append("decision_matrix.csv missing columns: " + ", ".join(sorted(missing)))

    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)
    print(f"Validation passed: {root}")


if __name__ == "__main__":
    main()
