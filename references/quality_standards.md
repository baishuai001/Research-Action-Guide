# Quality Standards

## Scientific Reasoning

Good output should show how evidence turns into a biological claim:

uncertainty -> data choice -> data credibility -> object identity -> discovery -> validation -> inference boundary -> project action

## Language

For Chinese output, write as a life-science research note. Prefer direct scientific language:

| Avoid | Prefer |
|---|---|
| 空泛地说“不同问题对应不同路线” | 说明具体证据瓶颈如何迫使作者选择某种数据和分析路线 |
| 堆砌工具名 | 解释工具选择保护了哪个结论、牺牲了什么 |
| 覆盖图、地图、语料、主张 | 证据支持与缺口、文献集合、核心结论、研究背景 |
| 车轱辘话 | 可执行标准、风险、下一步 |

## Red Flags

- The output is mostly a paper summary.
- Data selection is reported only as sample count.
- QC and annotation are treated as routine preprocessing rather than evidence foundations.
- Downstream analyses are listed by tool name rather than evidence role.
- The final guide does not tell the project what to include, exclude, clean, integrate, annotate, analyze, validate, or search next.
- The user's final biological question appears inside a single-paper audit.
- A recommendation lacks literature support, risk, or next action.

## Supervision Verdict

Use `PASS` only when the artifact can guide the next decision. Use `REVISE` if it is descriptive, generic, unsupported, or not actionable.
