# Skill Engineering Protocol

## Purpose

Use this protocol whenever Research-Action-Guide is created, edited, reviewed, or released.

This file makes `science-superpowers` continuously participate in the construction of Research-Action-Guide as an engineering discipline, not as a runtime dependency. The goal is to keep skill development empirical: observe how agents fail, write the smallest rule or validator that prevents the failure, then verify that the behavior changes.

## Governing Principle

Treat skill development as a scientific intervention on agent behavior.

Do not add principles because they sound right. Add them because an observed baseline failure shows that future agents need the constraint.

## Required Cycle

Every nontrivial skill change must follow this loop:

| Phase | Required action | Research-Action-Guide artifact |
|---|---|---|
| RED | Capture an observed baseline failure or define a failing test that represents it. | Unit test, weak example, supervision failure, or validator failure. |
| GREEN | Add the smallest protocol, prompt, schema, example, or script change that addresses the failure. | `SKILL.md`, `references/`, `examples/`, or `scripts/`. |
| REFACTOR | Remove duplication, close loopholes, and keep the skill discoverable through progressive disclosure. | Updated navigation, cleaner references, stronger tests. |

If there is no RED signal, the change is probably speculation. Either run a forward-test first or record why the change is urgent and how it will be tested later.

## Baseline Failure Log

Before adding or changing rules, write down the failure being targeted:

```text
Observed baseline failure:
Artifact affected:
What the agent did:
Why this is scientifically unsafe:
Which Research-Action-Guide layer should prevent it:
Minimal test or example to lock the fix:
```

Common baseline failures:

| Failure | Why it matters | Preferred fix |
|---|---|---|
| The audit becomes a paper summary. | It cannot support reusable design rules. | Add/strengthen decision-node and evidence-architecture checks. |
| The audit becomes a tool catalog. | It rewards analysis full stack behavior. | Add minimum sufficient route and downstream evidence-role checks. |
| Abstract-only evidence is audited. | It fabricates author-choice logic. | Enforce candidate/HOLD status and reject matrix entry. |
| Statistical unit is missing. | Cell-level or spot-level pseudoreplication can inflate claims. | Add statistical-unit fields, supervision checks, or examples. |
| Confounding factor risks are ignored. | The biological claim may be explained by cohort, platform, treatment, or sampling. | Add confounding-control rules or module-specific checks. |
| Validation hierarchy is flattened. | Internal consistency, external cohort, spatial, functional, and clinical endpoint evidence are not equivalent. | Add validation hierarchy requirements. |
| Chinese output is fluent but vague. | It lacks life-science academic Chinese / 生命科学学术性. | Add concrete rewrite standard and supervision criterion. |

## Rationalization Guard

Close the loophole explicitly whenever a new rationalization appears.

| Rationalization | Reality |
|---|---|
| "This is just documentation." | A skill is process code for agents; untested documentation changes behavior unpredictably. |
| "The principle is obvious." | Obvious to the author is not obvious to a future agent under task pressure. |
| "The model will understand from context." | Context is unstable; important constraints belong in the skill or a validator. |
| "A good example is enough." | Examples guide behavior, but validators and supervision prevent drift. |
| "We can test later." | Untested skill changes become hidden workflow debt. |
| "This paper used many analyses, so the workflow is strong." | Many analyses may be an analysis full stack; each module needs a decision node. |

## Forward-Test Requirement

Use forward-test when a change affects judgment, not just file structure.

Good forward-test prompts look like real use:

```text
Use Research-Action-Guide at <path> to produce a Paper Decision Audit for this paper. Use only the evidence provided. Do not create project-specific advice.
```

Bad forward-test prompts leak the intended answer:

```text
Test whether the skill avoids tool catalogs and includes statistical unit, confounding, and validation hierarchy.
```

Forward-test inputs should be raw artifacts: title/abstract, methods excerpt, full text, supplement snippet, code link, or a generated weak audit. The reviewer should not receive your diagnosis unless the test is specifically about supervision.

## Change Placement Rules

Put each change at the right layer:

| Change type | Preferred location |
|---|---|
| Governing philosophy | `references/bioinformatics_evidence_architecture.md` |
| Decision vocabulary or schema logic | `references/bioinformatics_decision_ontology.md` and `references/decision_matrix_schema.md` |
| Domain-specific best practice | `references/modules/` |
| Prompt behavior | audit, synthesis, guide, or supervision prompt files |
| Quality scoring | `references/supervision_rubric.md` |
| Chinese academic standard | `references/quality_standards.md` and `references/supervision_subagent.md` |
| Golden or weak behavior | `examples/` |
| Mechanical enforcement | `scripts/` and `tests/` |
| Development discipline | `references/skill_engineering_protocol.md` |

Do not duplicate a principle in many files. Put the full principle in one owner file and cross-reference it elsewhere.

## Required Validation Before Release

Run these before claiming a Research-Action-Guide skill change is ready:

```bash
python -m unittest discover -s tests
python -m py_compile scripts/init_project.py scripts/validate_project.py scripts/check_research_action_guide.py scripts/check_audit.py scripts/check_matrix.py scripts/check_corpus.py scripts/check_evidence_links.py scripts/check_supervision_report.py
python scripts/check_audit.py --file examples/golden_paper_decision_audit.md
python scripts/check_supervision_report.py --file examples/golden_supervision_report.md
python scripts/check_research_action_guide.py --file examples/golden_research_action_guide.md
```

For schema or project-structure changes, also run:

```bash
python scripts/init_project.py --project-root ./research_action_guide
python scripts/validate_project.py --project-root ./research_action_guide
python scripts/check_corpus.py --file ./research_action_guide/literature_corpus.csv
python scripts/check_matrix.py --file ./research_action_guide/decision_matrix.csv
python scripts/check_evidence_links.py --project-root ./research_action_guide
```

## Release Checklist

Before pushing:

1. State the observed baseline failure or reason for the change.
2. Add or update a failing test, weak example, golden example, or validator.
3. Implement the smallest sufficient change.
4. Run validators.
5. Update README only if user-facing behavior changed.
6. Confirm no generated files such as `__pycache__` are committed.
7. Commit with a message that names the behavior change, not just the file edited.

## Bottom Line

`science-superpowers` should guide Research-Action-Guide development as a discipline:

observed baseline failure -> RED -> GREEN -> REFACTOR -> forward-test -> supervision -> release.

If a proposed change cannot be tied to this chain, pause before adding it.
