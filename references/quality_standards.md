# Quality Standards

## Scientific Reasoning

Good output should show how evidence turns into a biological claim:

uncertainty -> data choice -> data credibility -> object identity -> discovery -> validation -> inference boundary -> project action

For bioinformatics work, this should read as an evidence architecture rather than a tool catalog:

falsifiable biological judgment -> decision node -> author choice -> evidence role -> protected claim -> assumption -> failure mode -> reusable rule -> project action

Bioinformatics best-practice outputs must explicitly check statistical unit, patient-level variation, confounding factor risks, validation hierarchy, and minimum sufficient route.

## Language

For Chinese output, write as a life-science research note. Prefer direct scientific language:

Chinese output must have 生命科学学术性: name the biological object, evidence bottleneck, claim strength, inference boundary, and validation requirement with precise research language. Avoid popular-science tone, casual praise, decorative rhetoric, and machine-translated English syntax.

| Avoid | Prefer |
|---|---|
| 空泛地说“不同问题对应不同路线” | 说明具体证据瓶颈如何迫使作者选择某种数据和分析路线 |
| 堆砌工具名 | 解释工具选择保护了哪个结论、牺牲了什么 |
| 覆盖图、地图、语料、主张 | 证据支持与缺口、文献集合、核心结论、研究背景 |
| 车轱辘话 | 可执行标准、风险、下一步 |
| 结果比较可靠 | 该结论在患者层面是否稳健、是否存在队列或平台混杂、需要哪一级验证 |
| 后续可以进一步验证 | 需要外部队列、跨平台、空间、扰动、功能实验或临床终点中的哪一级验证 |

## Red Flags

- The output is mostly a paper summary.
- Data selection is reported only as sample count.
- QC and annotation are treated as routine preprocessing rather than evidence foundations.
- Downstream analyses are listed by tool name rather than evidence role.
- Parameters, thresholds, or software names are preserved without explaining the decision node they served.
- The statistical unit is unclear, or cells/spots are treated as independent without patient/sample-level justification.
- Patient-level variation or a major confounding factor is ignored.
- Validation hierarchy is flattened, as if internal consistency, external cohort, cross-platform evidence, spatial evidence, functional validation, and clinical endpoint support were equivalent.
- The output runs common modules without identifying a minimum sufficient route.
- The output becomes an analysis full stack instead of a claim-centered evidence route.
- The final guide does not tell the project what to include, exclude, clean, integrate, annotate, analyze, validate, or search next.
- The user's final biological question appears inside a single-paper audit.
- A recommendation lacks literature support, risk, or next action.
- Chinese output lacks 生命科学学术性 and does not name the biological object, evidence boundary, claim strength, or validation requirement.

## Supervision Verdict

Use `PASS` only when the artifact can guide the next decision. Use `REVISE` if it is descriptive, generic, unsupported, or not actionable.
