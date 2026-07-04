#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "verdict": r"Verdict:\s*(PASS|REVISE|HOLD)",
    "artifact reviewed": r"Artifact reviewed:",
    "main failure mode": r"Main failure mode:",
    "decision nodes checked": r"Decision nodes checked:",
    "evidence architecture judgment": r"Evidence architecture judgment:",
    "direct evidence vs inference": r"Direct evidence vs inference:",
    "statistical unit and confounding": r"Statistical unit and confounding:",
    "validation hierarchy": r"Validation hierarchy:",
    "minimum sufficient route": r"Minimum sufficient route:",
    "chinese academic quality": r"Chinese academic quality:",
    "required revisions": r"Required revisions:",
    "next action": r"Next action:",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a Research Action Guide supervision report.")
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text, re.I):
            errors.append(f"missing {name}")

    if "生命科学学术性" not in text and "life-science academic Chinese" not in text:
        errors.append("missing life-science academic Chinese standard")
    if not re.search(r"confounding factor|混杂", text, re.I):
        errors.append("missing confounding factor judgment")
    if not re.search(r"patient-level|患者层面|statistical unit", text, re.I):
        errors.append("missing statistical unit judgment")

    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)

    print(f"PASS: {path}")


if __name__ == "__main__":
    main()
