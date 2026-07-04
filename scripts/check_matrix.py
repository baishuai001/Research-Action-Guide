#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
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
    "limitation",
    "audit_path",
}


DISALLOWED_DEPTHS = {"metadata-only", "abstract-only"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check Decision Matrix headers and evidence-eligible rows.")
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: missing header")
            sys.exit(1)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        errors = []
        if missing:
            errors.append("missing columns: " + ", ".join(sorted(missing)))
        for i, row in enumerate(reader, start=2):
            if row.get("evidence_depth", "").strip().lower() in DISALLOWED_DEPTHS:
                errors.append(f"row {i}: metadata-only or abstract-only paper cannot enter matrix")
            for col in ["paper_id", "title", "evidence_bottleneck", "reusable_rule", "audit_path"]:
                if not row.get(col, "").strip():
                    errors.append(f"row {i}: empty {col}")
    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)
    print(f"PASS: {path}")


if __name__ == "__main__":
    main()
