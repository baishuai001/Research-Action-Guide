---
name: research-action-guide
description: Use when the user wants literature evidence turned into an executable bioinformatics research plan, including paper screening, author-choice audits, evidence architecture, dataset criteria, QC/integration/annotation choices, downstream analysis selection, validation logic, and a technical roadmap.
---

# Research Action Guide

## Core Principle

The endpoint is always a **Research Action Guide / 课题行动指南**: an executable plan for what the project should do next and why each choice is scientifically justified.

Do not treat the task as literature management, paper notes, a method list, or a comparison table. Single-paper reading and cross-paper synthesis are only intermediate evidence-building layers.

## Bioinformatics Evidence Architecture

A good bioinformatics workflow is not a catalog of common analyses. It is an evidence architecture built around a falsifiable biological judgment.

Bioinformatics evidence architecture is the governing lens for this skill.

Use paper details to understand author choices, but do not become trapped by parameters. Infer the research logic behind data selection, QC, integration, annotation, statistical design, downstream modules, and validation. Then translate that logic into the user's concrete biological question: what philosophical stance, research rule, and local technical decision are required?

Default reasoning chain:

```text
uncertainty -> author choice -> evidence role -> protected claim -> assumption -> failure mode -> reusable rule -> project action
```

Bioinformatics-specific reasoning chain:

```text
biological judgment -> evidence bottleneck -> data boundary -> trusted difference -> object identity -> statistical unit and confounding factor -> downstream validation -> falsifiable conclusion
```

Before recommending any tool or module, identify the decision node it serves: question boundary, evidence bottleneck, data credibility, object identity, statistical unit, confounding factor, claim strength, validation hierarchy, or failure mode. Prefer the minimum sufficient route: each module must change what the project can believe, rule out, or do next. Reject the analysis full stack when modules do not change inference.

## Fixed Concepts

Use these names consistently:

| Name | Role |
|---|---|
| **Literature Corpus Protocol** | Search, screening, enrichment, inclusion, exclusion, and saturation rules for building the paper corpus. |
| **Paper Decision Audit** | One-paper analysis focused on why the authors chose specific data, QC, integration, annotation, downstream modules, validation, and technical route. |
| **Decision Matrix** | CSV where each row is one evidence-eligible paper and columns capture reusable decision logic. |
| **Cross-Paper Evidence Synthesis** | Higher-order synthesis that extracts patterns from many Paper Decision Audits. |
| **Research Action Guide / 课题行动指南** | Final project-level action plan: dataset screening criteria, inclusion/exclusion standards, cleaning/QC, integration, annotation, downstream modules, validation, risks, literature support, and technical roadmap. |

Forbidden legacy framing: do not make any reference manager, citation library, single-paper card, or matrix the center of the skill.

## Default Project

Default output path:

```text
./research_action_guide
```

Default structure:

```text
research_action_guide/
|-- config.yaml
|-- literature_corpus.csv
|-- decision_matrix.csv
|-- translation_manifest.csv
|-- paper_decision_audits/
|-- synthesis/
|-- action_guides/
`-- supervision/
```

Always report absolute paths written. Paths can be changed through `config.yaml` or script arguments.

## When Starting A Project

1. Capture the final biological question as a **synthesis lens**.
2. Build or update the Literature Corpus Protocol using `references/literature_corpus_protocol.md`.
3. Accept rough paper clues from the user: title, DOI, PMID, URL, local PDF path, pasted text, RIS/CSV/Markdown list, or a folder of PDFs. The user should not have to pre-organize metadata.
4. Enrich candidates from available sources: DOI/PMID, article URL, publisher page, PubMed, PMC, local PDFs, pasted methods/results, references, supplements, code links, or web search when needed.
5. If only title/abstract/metadata are available, keep the paper as a candidate. Do not create a Paper Decision Audit.
6. If methods/results/supplement/code or sufficient full-text evidence is available, create a Paper Decision Audit using `references/paper_decision_audit_prompt.md`.
7. Run a supervision subagent using `references/supervision_subagent.md` before accepting the audit.
8. Update the Decision Matrix only after the audit passes supervision.
9. Run Cross-Paper Evidence Synthesis using `references/cross_paper_evidence_synthesis_prompt.md`, then supervise the synthesis.
10. Generate the Research Action Guide using `references/research_action_guide_prompt.md`, then supervise the final guide.

## Quality Gates

- A Paper Decision Audit must explain author choices at decision-node depth. It is not enough to say which tools were used.
- For data selection, QC, integration, annotation, and downstream modules, state: choice, scientific rationale, realistic alternatives, assumptions, risks, conclusion affected, and reusable rule.
- Cross-Paper Evidence Synthesis must extract higher-order logic, not compare papers for comparison's sake.
- The Research Action Guide must be actionable. Every major recommendation needs evidence support, assumptions, risk if wrong, and next action if evidence is insufficient.
- Do not write project-specific advice inside a Paper Decision Audit. The project question belongs in synthesis and the final guide.
- Separate direct evidence from inference.
- Do not let parameters, thresholds, software names, or figure details replace the underlying author-choice logic.
- Use the supervision subagent to reject artifacts that are descriptive, generic, unsupported, statistically unsafe, or not actionable.
- Use natural life-science Chinese when writing Chinese output. Avoid stiff or decorative wording that obscures the biological logic.

## Required References

Read only the reference needed for the current task:

- Paper screening: `references/literature_corpus_protocol.md`
- Single-paper analysis: `references/paper_decision_audit_prompt.md`
- Cross-paper synthesis: `references/cross_paper_evidence_synthesis_prompt.md`
- Final guide: `references/research_action_guide_prompt.md`
- Bioinformatics reasoning philosophy: `references/bioinformatics_evidence_architecture.md`
- Decision-node ontology: `references/bioinformatics_decision_ontology.md`
- Single-cell module: `references/modules/single_cell_rna.md`
- Spatial transcriptomics module: `references/modules/spatial_transcriptomics.md`
- Bulk and pan-cancer module: `references/modules/bulk_pan_cancer.md`
- Clinical and survival module: `references/modules/clinical_survival.md`
- Supervision rubric: `references/supervision_rubric.md`
- Supervision subagent: `references/supervision_subagent.md`
- Golden audit example: `examples/golden_paper_decision_audit.md`
- Weak audit anti-example: `examples/weak_paper_decision_audit.md`
- Golden final guide example: `examples/golden_research_action_guide.md`
- Golden supervision report example: `examples/golden_supervision_report.md`
- Style and supervision: `references/quality_standards.md`
- Matrix fields: `references/decision_matrix_schema.md`

## Scripts

Use scripts for deterministic project operations:

```bash
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
python scripts/check_corpus.py --file ./research_action_guide/literature_corpus.csv
python scripts/check_matrix.py --file ./research_action_guide/decision_matrix.csv
python scripts/check_evidence_links.py --project-root ./research_action_guide
python scripts/check_audit.py --file ./research_action_guide/paper_decision_audits/P0001.md
python scripts/check_supervision_report.py --file ./research_action_guide/supervision/P0001_supervision.md
python scripts/check_research_action_guide.py --file ./research_action_guide/action_guides/research_action_guide.md
```

Script roles:

- `init_project.py`: create the default folder structure and empty CSV files.
- `validate_project.py`: check required folders/files and basic CSV headers.
- `check_corpus.py`: check literature corpus columns and candidate statuses.
- `check_matrix.py`: check Decision Matrix fields and reject metadata-only or abstract-only rows.
- `check_evidence_links.py`: check matrix `audit_path` links resolve inside the project.
- `check_audit.py`: check Paper Decision Audit decision-node completeness.
- `check_supervision_report.py`: check supervision report completeness.
- `check_research_action_guide.py`: reject reports that are not actionable guides.

## Completion Rule

Do not claim the final guide is ready unless:

1. evidence-eligible papers have Paper Decision Audits,
2. Paper Decision Audits have supervision reports with `PASS` verdicts or explicit `HOLD` evidence gaps,
3. the Decision Matrix captures decision-node logic,
4. Cross-Paper Evidence Synthesis identifies what the corpus can and cannot support and has passed supervision,
5. the Research Action Guide contains concrete project actions and literature support,
6. the final guide has passed supervision,
7. `check_research_action_guide.py` passes.
