#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


REQUIRED = {
    "evidence architecture": r"evidence architecture|证据结构",
    "decision node": r"decision node|决策节点",
    "evidence bottleneck": r"evidence bottleneck|证据瓶颈",
    "data choice": r"data choice|data selection|数据选择",
    "qc": r"\bQC\b|quality control|质控",
    "annotation": r"annotation|object identity|注释|对象身份",
    "statistical unit": r"statistical unit|统计单位",
    "confounding factor": r"confounding factor|混杂",
    "validation hierarchy": r"validation hierarchy|验证层级",
    "minimum sufficient route": r"minimum sufficient route|最小充分路线",
    "failure mode": r"failure mode|失败模式",
    "reusable rule": r"reusable rule|可复用",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a Paper Decision Audit for decision-node completeness.")
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    errors = [name for name, pattern in REQUIRED.items() if not re.search(pattern, text, re.I)]

    if errors:
        for name in errors:
            print(f"ERROR: missing {name}")
        sys.exit(1)
    print(f"PASS: {args.file}")


if __name__ == "__main__":
    main()
