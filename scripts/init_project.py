#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path


CORPUS_COLUMNS = [
    "paper_id",
    "title",
    "year",
    "doi_or_pmid",
    "source",
    "screening_status",
    "evidence_role",
    "evidence_depth",
    "next_action",
    "notes",
]

MATRIX_COLUMNS = [
    "paper_id",
    "title",
    "year",
    "doi_or_pmid",
    "evidence_depth",
    "biological_question_type",
    "evidence_bottleneck",
    "data_selection_logic",
    "qc_integration_logic",
    "annotation_logic",
    "downstream_selection_logic",
    "validation_logic",
    "technical_tradeoff",
    "reusable_rule",
    "limitation",
    "audit_path",
]

TRANSLATION_COLUMNS = [
    "file_path",
    "source_language",
    "output_order",
    "literal_translation_status",
    "glossary_status",
    "qc_status",
    "last_checked",
    "notes",
]


def ensure_csv(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow(columns)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default="./research_action_guide")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    for folder in [
        "paper_decision_audits",
        "synthesis",
        "action_guides",
        "supervision",
    ]:
        (root / folder).mkdir(exist_ok=True)

    ensure_csv(root / "literature_corpus.csv", CORPUS_COLUMNS)
    ensure_csv(root / "decision_matrix.csv", MATRIX_COLUMNS)
    ensure_csv(root / "translation_manifest.csv", TRANSLATION_COLUMNS)

    config = root / "config.yaml"
    if not config.exists():
        config.write_text(
            "\n".join(
                [
                    f'project_root: "{root}"',
                    f'corpus_path: "{root / "literature_corpus.csv"}"',
                    f'decision_matrix_path: "{root / "decision_matrix.csv"}"',
                    f'audit_folder: "{root / "paper_decision_audits"}"',
                    f'synthesis_folder: "{root / "synthesis"}"',
                    f'action_guide_folder: "{root / "action_guides"}"',
                    f'supervision_folder: "{root / "supervision"}"',
                    f'translation_manifest_path: "{root / "translation_manifest.csv"}"',
                    "",
                ]
            ),
            encoding="utf-8",
        )

    print(root)


if __name__ == "__main__":
    main()
