#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
    "paper_id",
    "title",
    "screening_status",
    "evidence_role",
    "evidence_depth",
    "next_action",
}


VALID_STATUSES = {
    "candidate",
    "title-abstract-screened",
    "needs-full-text",
    "ready-for-audit",
    "audited",
    "matrix-ready",
    "excluded",
    "hold",
    "duplicate",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check literature corpus structure and screening statuses.")
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    errors = []
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: missing header")
            sys.exit(1)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            errors.append("missing columns: " + ", ".join(sorted(missing)))
        for i, row in enumerate(reader, start=2):
            status = row.get("screening_status", "").strip()
            if status and status not in VALID_STATUSES:
                errors.append(f"row {i}: invalid screening_status {status}")
            if status in {"ready-for-audit", "audited", "matrix-ready"} and not row.get("evidence_role", "").strip():
                errors.append(f"row {i}: evidence_role required for {status}")
    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)
    print(f"PASS: {path}")


if __name__ == "__main__":
    main()
