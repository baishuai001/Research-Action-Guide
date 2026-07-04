---
name: research-action-guide
description: Use when the user wants literature evidence turned into an executable research plan, including paper screening, decision audits, cross-paper synthesis, dataset criteria, QC/integration/annotation choices, downstream analysis selection, validation logic, and a technical roadmap.
---

# Research Action Guide

## Core Principle

The endpoint is always a **Research Action Guide / 课题行动指南**: an executable plan for what the project should do next and why each choice is scientifically justified.

Do not treat the task as literature management, paper notes, a method list, or a comparison table. Single-paper reading and cross-paper synthesis are only intermediate evidence-building layers.

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
7. Update the Decision Matrix only after the audit passes supervision.
8. Run Cross-Paper Evidence Synthesis using `references/cross_paper_evidence_synthesis_prompt.md`.
9. Generate the Research Action Guide using `references/research_action_guide_prompt.md`.

## Quality Gates

- A Paper Decision Audit must explain author choices at decision-node depth. It is not enough to say which tools were used.
- For data selection, QC, integration, annotation, and downstream modules, state: choice, scientific rationale, realistic alternatives, assumptions, risks, conclusion affected, and reusable rule.
- Cross-Paper Evidence Synthesis must extract higher-order logic, not compare papers for comparison's sake.
- The Research Action Guide must be actionable. Every major recommendation needs evidence support, assumptions, risk if wrong, and next action if evidence is insufficient.
- Do not write project-specific advice inside a Paper Decision Audit. The project question belongs in synthesis and the final guide.
- Separate direct evidence from inference.
- Use natural life-science Chinese when writing Chinese output. Avoid stiff or decorative wording that obscures the biological logic.

## Required References

Read only the reference needed for the current task:

- Paper screening: `references/literature_corpus_protocol.md`
- Single-paper analysis: `references/paper_decision_audit_prompt.md`
- Cross-paper synthesis: `references/cross_paper_evidence_synthesis_prompt.md`
- Final guide: `references/research_action_guide_prompt.md`
- Style and supervision: `references/quality_standards.md`
- Matrix fields: `references/decision_matrix_schema.md`

## Scripts

Use scripts for deterministic project operations:

```bash
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
python scripts/check_research_action_guide.py --file ./research_action_guide/action_guides/research_action_guide.md
```

Script roles:

- `init_project.py`: create the default folder structure and empty CSV files.
- `validate_project.py`: check required folders/files and basic CSV headers.
- `check_research_action_guide.py`: reject reports that are not actionable guides.

## Completion Rule

Do not claim the final guide is ready unless:

1. evidence-eligible papers have Paper Decision Audits,
2. the Decision Matrix captures decision-node logic,
3. Cross-Paper Evidence Synthesis identifies what the corpus can and cannot support,
4. the Research Action Guide contains concrete project actions and literature support,
5. `check_research_action_guide.py` passes.
