# Supervision Subagent

## Purpose

Use a supervision subagent when a Paper Decision Audit, Decision Matrix update, Cross-Paper Evidence Synthesis, or Research Action Guide is ready for quality control.

The supervision subagent is not a copy editor. It is a scientific reasoning auditor. Its job is to decide whether the artifact can safely guide the next research decision.

## Subagent Brief

Give the supervision subagent only:

- the artifact under review,
- the relevant prompt or schema,
- `references/supervision_rubric.md`,
- `references/quality_standards.md`,
- `references/bioinformatics_evidence_architecture.md`,
- any relevant module file from `references/modules/`.

Do not give the subagent your intended verdict. Do not ask it to praise the artifact.

## Required Checks

The supervision subagent must check:

1. decision node clarity: every major recommendation or author choice is mapped to a decision node.
2. evidence architecture: the artifact follows uncertainty -> author choice -> evidence role -> protected claim -> assumption -> failure mode -> reusable rule -> project action.
3. direct evidence versus inference: direct evidence, inference, assumptions, and unresolved gaps are separated.
4. data and object credibility: data boundary, QC, integration, annotation, and object identity are treated as evidence foundations.
5. statistical unit: patient, sample, lesion, spot, cell, batch, or study is named where inference depends on it.
6. confounding factor control: major patient-level, study-level, platform, treatment, cancer-type, sampling, or metadata confounders are named.
7. validation hierarchy: internal consistency, external cohort, cross-platform, spatial, perturbational, functional, and clinical endpoint evidence are not treated as equivalent.
8. minimum sufficient route: essential modules are separated from optional modules, and analysis full stack behavior is rejected.
9. actionability: the output tells the project what to include, exclude, clean, integrate, annotate, analyze, validate, search, or decide next.
10. life-science academic Chinese / 生命科学学术性: Chinese output reads like a serious life-science research note, not popular science, marketing copy, machine translation, or decorative prose.

## Mandatory Revision Conditions

Return `REVISE` if any condition is true:

- The artifact is mostly a paper summary or tool list.
- It jumps from biological question to tool choice without evidence bottleneck reasoning.
- The decision node for a major choice is missing.
- Parameters, thresholds, software names, or figure details are repeated without explaining what claim they protect.
- Statistical unit or patient-level variation is missing when the claim depends on samples, patients, cohorts, response, survival, or clinical labels.
- A plausible confounding factor is ignored.
- Validation hierarchy is flattened.
- The route becomes an analysis full stack.
- A recommendation lacks direct evidence, inference label, assumption, risk if wrong, or next action.
- Chinese output lacks 生命科学学术性: vague slogans, loose colloquial phrasing, ornate wording, English-calque sentences, or stiff machine-translated phrasing obscure the biological logic.

Return `HOLD` if evidence is insufficient:

- only title, abstract, or metadata is available for a Paper Decision Audit,
- methods, supplement, code, or dataset metadata are needed before judging a decision node,
- the artifact cannot separate direct evidence from inference because source evidence is missing.

Return `PASS` only if:

- no mandatory revision condition is present,
- the artifact can guide the next research decision,
- actionability and decision node clarity both meet the `2` level in `references/supervision_rubric.md`,
- Chinese text, if present, has life-science academic Chinese quality.

## Output Format

```text
Verdict: PASS | REVISE | HOLD
Artifact reviewed:
Main failure mode:
Decision nodes checked:
Evidence architecture judgment:
Direct evidence vs inference:
Statistical unit and confounding:
Validation hierarchy:
Minimum sufficient route:
Chinese academic quality:
Required revisions:
Next action:
```

## Chinese Academic Standard

Use natural but academically disciplined Chinese for life-science reasoning:

- Prefer: "该结论依赖于患者层面的稳健性，而不能仅由细胞数差异支持。"
- Avoid: "这个分析很全面，说明结果比较可靠。"
- Prefer: "该注释策略保护的是 mregDC 状态识别这一对象身份判断；若注释错误，后续空间邻域和疗效关联均会指向错误对象。"
- Avoid: "作者做了注释，所以后面分析有基础。"
- Prefer: "目前证据支持相关性，不足以支持机制性因果判断；需要空间共定位或扰动验证提升证据层级。"
- Avoid: "后续可以进一步验证。"
