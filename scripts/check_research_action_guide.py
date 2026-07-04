#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "executive decision": r"(?i)executive decision|执行决策|总体决策",
    "scientific premise": r"(?i)scientific premise|科学前提|生物学模型",
    "dataset screening": r"(?i)dataset screening|数据筛选",
    "inclusion exclusion": r"(?i)inclusion|exclusion|纳入|排除|降级|暂缓",
    "qc": r"(?i)\bQC\b|quality control|质控|清洗",
    "integration": r"(?i)integration|batch|整合|批次",
    "annotation": r"(?i)annotation|identity|注释|身份",
    "downstream": r"(?i)downstream|module|下游|分析模块",
    "decision rationale": r"(?i)decision rationale|决策依据",
    "literature support": r"(?i)literature support|文献支持",
    "roadmap": r"(?i)roadmap|mermaid|技术路线",
    "next actions": r"(?i)next action|下一步|行动",
}

GENERIC_RED_FLAGS = [
    "more data are needed",
    "further study is needed",
    "different questions need different",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text):
            errors.append(f"missing required section or concept: {name}")

    if text.count("|") < 30:
        errors.append("too few decision tables for an actionable guide")

    lower = text.lower()
    for phrase in GENERIC_RED_FLAGS:
        if phrase in lower:
            errors.append(f"generic red-flag phrase found: {phrase}")

    if not re.search(r"(?i)risk if wrong|风险", text):
        errors.append("missing risk-if-wrong reasoning")
    if not re.search(r"(?i)direct evidence|inference|直接证据|推断", text):
        errors.append("missing evidence-versus-inference separation")

    if errors:
        for error in errors:
            print("ERROR:", error)
        sys.exit(1)
    print(f"PASS: {path}")


if __name__ == "__main__":
    main()
