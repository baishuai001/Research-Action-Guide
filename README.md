# Research Action Guide / 课题行动指南

Research Action Guide is a Codex skill for turning literature evidence into an executable bioinformatics research plan.

它的目标不是整理文献、总结方法、收集工具名，而是从文献细节中理解作者的“选择”：为什么选择这些数据，为什么这样质控和整合，为什么这样定义生物学对象，为什么这些下游分析和验证足以支撑主结论。最终产物是能指导下一轮文献筛选、公共数据筛选、分析设计和验证路线的 **Research Action Guide / 课题行动指南**。

## Core Philosophy / 核心思想

好的生信技术路线不是把常用分析都跑一遍，而是围绕一个可证伪的生物学判断组织证据。

This skill uses the following evidence-architecture chain:

```text
biological judgment -> evidence bottleneck -> data boundary -> trusted difference -> object identity -> statistical unit and confounding factor -> downstream validation -> falsifiable conclusion
```

Author choices are treated as reusable research-design evidence:

| Author choice | What it decides |
|---|---|
| Data selection | What question boundary the paper can answer. |
| QC and integration | Which differences can be trusted as biological signal. |
| Annotation and object definition | Which biological object later conclusions refer to. |
| Statistical unit and confounding control | Whether the comparison is interpretable at patient, sample, study, or cell level. |
| Downstream modules | Which vulnerability in the main claim is tested. |
| Validation hierarchy | How far the claim can travel beyond the discovery dataset. |
| Minimum sufficient route | Which modules are essential, optional, or just an analysis full stack. |

## What This Skill Produces / 产物

| Artifact | Purpose |
|---|---|
| Literature Corpus Protocol | Search, screening, enrichment, inclusion, exclusion, and saturation rules for building the paper corpus. |
| Paper Decision Audit | One-paper audit focused on why authors made data, QC, integration, annotation, downstream, validation, and statistical-design choices. |
| Decision Matrix | CSV where each row captures reusable decision-node logic from one evidence-eligible paper. |
| Cross-Paper Evidence Synthesis | Higher-order synthesis that extracts research-design rules across audited papers. |
| Research Action Guide | Final project-level guide with dataset criteria, inclusion/exclusion rules, QC/integration/annotation strategy, statistical design, downstream modules, validation logic, risks, literature support, and technical roadmap. |
| Supervision Report | PASS / REVISE / HOLD quality-control judgment for audits, synthesis, and final guides. |

## Current Workflow / 当前工作流

1. Capture the final biological question as a synthesis lens.
2. Build or update the literature corpus.
3. Audit evidence-eligible papers with `Paper Decision Audit`.
4. Run the supervision subagent before accepting each audit.
5. Add passing audits to the `Decision Matrix`.
6. Run cross-paper evidence synthesis.
7. Supervise the synthesis.
8. Generate the final `Research Action Guide`.
9. Supervise the final guide and run validators.

The final guide is not ready unless evidence-eligible papers have audits, audits pass supervision or have explicit HOLD gaps, the matrix captures decision-node logic, synthesis identifies what the corpus can and cannot support, the final guide is actionable, and validators pass.

## Bioinformatics Best-Practice Guards

The skill explicitly checks:

- decision node clarity,
- direct evidence vs inference,
- data boundary and data credibility,
- object identity,
- statistical unit,
- patient-level variation,
- confounding factor risks,
- validation hierarchy,
- minimum sufficient route,
- analysis full stack risk,
- actionability,
- life-science academic Chinese / 生命科学学术性.

Chinese output should read like disciplined life-science research reasoning. It should name the biological object, evidence bottleneck, claim strength, inference boundary, and validation requirement. It should avoid slogans, loose praise, decorative language, and machine-translated syntax.

## Supervision Subagent

The supervision subagent is a scientific reasoning auditor, not a copy editor.

It returns:

- `PASS`: the artifact can guide the next research decision.
- `REVISE`: the artifact is descriptive, generic, unsupported, statistically unsafe, weak in evidence architecture, or not actionable.
- `HOLD`: source evidence is insufficient, such as abstract-only evidence, missing methods, missing supplement, missing code, or missing dataset metadata.

Supervision checks are defined in:

- `references/supervision_subagent.md`
- `references/supervision_rubric.md`
- `references/quality_standards.md`

## Development Protocol / Skill 工程协议

Research Action Guide uses a `science-superpowers`-inspired engineering protocol for its own development.

The protocol is stored in:

- `references/skill_engineering_protocol.md`

The rule is:

```text
observed baseline failure -> RED -> GREEN -> REFACTOR -> forward-test -> supervision -> release
```

In practice, this means every meaningful skill change should be tied to an observed or testable agent failure, such as:

- turning a Paper Decision Audit into a paper summary,
- producing a tool catalog instead of decision-node logic,
- auditing abstract-only evidence,
- ignoring statistical unit or patient-level variation,
- flattening validation hierarchy,
- producing fluent but non-academic Chinese.

Before release, changes should be protected by at least one of:

- a failing unit test,
- a weak/golden example,
- a validator script,
- a supervision condition,
- a forward-test on realistic paper evidence.

Supervision is tiered:

| Level | Trigger | Required check |
|---|---|---|
| Level 0 | Non-behavioral edits such as typos or formatting. | Mechanical tests only. |
| Level 1 | Structural changes such as schema, examples, or validator scripts. | Tests plus relevant validators. |
| Level 2 | Agent behavior changes such as prompts, supervision criteria, or domain modules. | Tests, validators, and skill-engineering supervisor review. |
| Level 3 | Core philosophy, workflow order, completion rules, or release-level changes. | Tests, validators, forward-test, red-team review, and multi-role supervision when useful. |

## Domain Modules / 生信场景模块

The skill includes lightweight modules for common bioinformatics settings:

| Module | File |
|---|---|
| Single-cell / single-nucleus RNA-seq | `references/modules/single_cell_rna.md` |
| Spatial transcriptomics and tissue niche analysis | `references/modules/spatial_transcriptomics.md` |
| Bulk RNA-seq and pan-cancer public-data analysis | `references/modules/bulk_pan_cancer.md` |
| Clinical, response, biomarker, and survival analysis | `references/modules/clinical_survival.md` |

These modules do not replace paper-specific reasoning. They help the agent ask the right decision-node questions for each analysis setting.

## Repository Structure

```text
Research-Action-Guide/
|-- SKILL.md
|-- README.md
|-- agents/
|-- examples/
|-- references/
|   |-- bioinformatics_evidence_architecture.md
|   |-- bioinformatics_decision_ontology.md
|   |-- supervision_subagent.md
|   |-- supervision_rubric.md
|   |-- modules/
|   `-- ...
|-- scripts/
`-- tests/
```

## Installation

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/baishuai001/Research-Action-Guide.git ~/.codex/skills/research-action-guide
```

On Windows, the target folder is usually:

```text
C:\Users\<your-user-name>\.codex\skills\research-action-guide
```

## Validation

Run the full test suite:

```bash
python -m unittest discover -s tests
```

Initialize and validate a project:

```bash
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
python scripts/check_corpus.py --file ./research_action_guide/literature_corpus.csv
python scripts/check_matrix.py --file ./research_action_guide/decision_matrix.csv
python scripts/check_evidence_links.py --project-root ./research_action_guide
```

Check generated artifacts:

```bash
python scripts/check_audit.py --file ./research_action_guide/paper_decision_audits/P0001.md
python scripts/check_supervision_report.py --file ./research_action_guide/supervision/P0001_supervision.md
python scripts/check_research_action_guide.py --file ./research_action_guide/action_guides/research_action_guide.md
```

Check bundled examples:

```bash
python scripts/check_audit.py --file examples/golden_paper_decision_audit.md
python scripts/check_supervision_report.py --file examples/golden_supervision_report.md
python scripts/check_research_action_guide.py --file examples/golden_research_action_guide.md
```

## Typical Request

```text
我要筛选一批单细胞 / 泛癌 / 肿瘤免疫 / 空间转录组文献，
总结不同生物学问题对应的研究设计原则，
并最终形成一个课题行动指南。

我的生物学问题是：
mregDC 空间生态位是否决定肿瘤免疫治疗响应，
并在肿瘤进展中发生功能性重塑？
```

The skill should then build a literature corpus, audit evidence-eligible papers, supervise outputs, synthesize cross-paper rules, and generate an actionable Research Action Guide.
