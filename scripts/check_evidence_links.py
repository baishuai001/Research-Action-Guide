#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Check that Decision Matrix audit_path values resolve inside a project.")
    parser.add_argument("--project-root", default="./research_action_guide")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    matrix = root / "decision_matrix.csv"
    if not matrix.exists():
        print(f"ERROR: missing decision matrix: {matrix}")
        sys.exit(1)

    errors = []
    with matrix.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if "audit_path" not in (reader.fieldnames or []):
            print("ERROR: missing audit_path column")
            sys.exit(1)
        for i, row in enumerate(reader, start=2):
            audit_path = row.get("audit_path", "").strip()
            if not audit_path:
                continue
            candidate = Path(audit_path)
            if not candidate.is_absolute():
                candidate = root / candidate
            try:
                candidate.resolve().relative_to(root)
            except ValueError:
                errors.append(f"row {i}: audit_path outside project root: {audit_path}")
                continue
            if not candidate.exists():
                errors.append(f"row {i}: audit_path not found: {audit_path}")

    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)
    print(f"PASS: {root}")


if __name__ == "__main__":
    main()
