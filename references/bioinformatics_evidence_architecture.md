# Bioinformatics Evidence Architecture

## Core Principle

A good bioinformatics workflow is not a catalog of common analyses. It is an evidence architecture built around a falsifiable biological judgment.

Do not reward a workflow for running many modules. Ask whether each choice protects a specific biological claim from a realistic failure mode.

## Author Choices As Evidence

Treat author choices as reusable research-design evidence:

| Author choice | What the choice actually decides |
|---|---|
| Data selection | Data selection defines the boundary of answerable questions. |
| QC and cleaning | Which differences can be trusted and which must be treated as technical noise. |
| Integration and batch strategy | Which cross-sample, cross-platform, or cross-study differences can be compared without erasing relevant biology. |
| Annotation and object definition | The object identity to which all later conclusions refer. |
| Statistical unit and confounding factor design | Whether the comparison unit, patient-level variation, covariates, and contrasts make the claimed difference interpretable. |
| Downstream modules | Which vulnerability in the main claim is being tested. |
| Validation hierarchy | How far the claim can travel beyond the discovery dataset. |
| Reporting and reproducibility | Whether another analyst can audit the decision chain and reproduce the claim. |

## Decision Node Lens

For every paper and every project recommendation, identify the decision node before naming tools:

| Decision node | Guiding question |
|---|---|
| Biological judgment | What specific claim would be falsified if the result is wrong? |
| Evidence bottleneck | What uncertainty would make the main conclusion fail? |
| Minimum sufficient data | What data are necessary to test the claim without unnecessary expansion? |
| Boundary of inference | What cannot be answered by the selected cohorts, platforms, labels, or time points? |
| Data credibility | What QC, metadata, replication, or diagnostics make the data trustworthy? |
| Object identity | How are cells, states, niches, malignant populations, clinical labels, or progression stages established? |
| Statistical unit | What is the real replicate: patient, sample, lesion, organoid, field, spot, or cell? |
| Confounding factor control | What patient-level variation, study-level, platform-level, cancer-type, treatment, sampling, or metadata bias must be controlled? |
| Downstream evidence role | What weakness in the claim does this module test? |
| Validation hierarchy | What level of validation is needed: internal consistency, external cohort, cross-platform, spatial, perturbational, clinical, functional validation, or clinical endpoint? |
| Failure mode | What false conclusion would appear if this decision were wrong? |
| Reusable rule | What general research-design principle can be transferred to the user's project? |

## Question Types And Route Pressure

"What question needs what route?" must grow from the evidence bottleneck, not from tool habit.

| Question pressure | Typical route implication |
|---|---|
| Reference or identity transfer | Needs reference mapping, marker/receptor evidence, and careful boundary statements. |
| Clinical translation | Needs state stability, patient-level statistics, external validation, and clinically meaningful labels. |
| Public-data synthesis | Needs metadata harmonization, duplicate control, platform comparability, and study-level bias checks. |
| Progression or temporal direction | Needs stage anchors, trajectory or longitudinal logic, and directionality validation. |
| Spatial niche or microenvironment | Needs spatial object definition, neighborhood controls, tissue-region context, and spatial validation. |
| Mechanism or causality | Needs perturbational, functional, regulon, ligand-receptor, or orthogonal evidence; association alone is insufficient. |
| Response or resistance | Needs treatment timing, response labels, baseline/on-treatment distinction, and independent response cohorts. |

## Minimum Sufficient Route

Prefer the minimum sufficient route: the smallest analysis design that can make the biological judgment credible while exposing its assumptions.

Do not add a module unless it changes at least one of these:

- the credibility of the data,
- the identity of the biological object,
- the strength of the main claim,
- the ability to rule out a realistic alternative explanation,
- the boundary of inference,
- the next project action.

If a module only decorates the workflow, mark it as non-essential.

The opposite failure mode is the analysis full stack: running common modules because they are customary rather than because they protect a claim. If a module cannot change claim credibility, rule out an alternative explanation, or guide the next action, it should not become main-line evidence.

## Statistical Unit And Confounding Factors

Many bioinformatics conclusions fail because the statistical unit is wrong, not because the tool is wrong.

Always ask:

- Are cells, spots, samples, patients, tumors, lesions, batches, or studies being treated as the independent unit?
- Is patient-level variation separated from cell-level abundance or expression?
- Could cancer type, treatment, stage, tissue site, platform, sequencing depth, sample processing, or study source explain the result?
- Is the comparison protected from pseudoreplication, data leakage, or cohort imbalance?
- Would the conclusion survive sensitivity analysis at the patient, sample, or study level?

## Validation Hierarchy

Validation levels are not interchangeable. Name the validation hierarchy required by the claim:

| Validation level | What it supports |
|---|---|
| Internal consistency | The signal is coherent inside the discovery dataset. |
| External cohort | The signal is not unique to one cohort or study. |
| Cross-platform validation | The signal survives different measurement technologies or preprocessing routes. |
| Spatial validation | The inferred object or interaction exists in tissue context. |
| Perturbational evidence | The proposed mechanism changes when the system is disturbed. |
| Functional validation | The biological object has the predicted function. |
| Clinical endpoint | The claim is connected to outcome, response, progression, or treatment relevance. |

## Detail Without Parameter Traps

Absorb details deeply, but do not become trapped by parameters.

Use parameters, thresholds, software names, and figure details to infer the underlying decision:

- What uncertainty was the author trying to reduce?
- What alternative explanation was being defended against?
- What biological signal might have been lost?
- What technical artifact might have been introduced?
- What conclusion depends on this choice?
- What would need to change if the user's biological question has a different evidence bottleneck?

Report concrete details when they affect a decision. Do not preserve detail just because it appears in the paper.

## Output Standard

Good output should move through this chain:

uncertainty -> author choice -> evidence role -> protected claim -> assumption -> failure mode -> reusable rule -> project action

Chinese output should preserve the same logic:

不把技术路线写成工具清单，而是写成围绕可证伪生物学判断组织起来的证据结构。文献细节用于理解作者为什么这样选择；跨文献综合用于提炼科研规律；最终指南必须把这些规律落到具体生物学问题中的数据筛选、质控、整合、注释、统计、下游分析、验证和下一步行动。
