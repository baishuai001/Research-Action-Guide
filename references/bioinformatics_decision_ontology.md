# Bioinformatics Decision Ontology

## Purpose

Use this file when a task needs operational decision fields rather than the philosophy in `bioinformatics_evidence_architecture.md`.

The ontology defines the reusable decision node vocabulary for Paper Decision Audits, Decision Matrix rows, Cross-Paper Evidence Synthesis, and Research Action Guides.

## Core Decision Nodes

| Decision node | Required capture | Failure mode |
|---|---|---|
| biological_judgment | The falsifiable claim the route protects. | The workflow becomes descriptive and cannot decide anything. |
| evidence_bottleneck | The uncertainty that would make the conclusion fail. | The route answers an easier or different question. |
| data_boundary | Cohorts, platforms, labels, time points, and metadata included or excluded. | The analysis overclaims beyond the data. |
| data_credibility | QC, sample quality, platform diagnostics, metadata completeness, and replication checks. | Technical noise is interpreted as biology. |
| object_identity | Cell type, state, malignant identity, spatial niche, clinical label, or progression stage. | Downstream conclusions point to the wrong biological object. |
| statistical_unit | The true independent unit: patient, sample, lesion, tumor, study, spot, or cell. | Pseudoreplication inflates confidence. |
| confounding_factor | Patient-level variation, cancer type, treatment, stage, tissue site, platform, batch, sampling, or study source. | A hidden variable explains the signal. |
| downstream_evidence_role | The specific vulnerability tested by a downstream module. | The workflow becomes an analysis full stack. |
| validation_hierarchy | Internal, external cohort, cross-platform, spatial, perturbational, functional validation, or clinical endpoint support. | Validation strength is overstated. |
| minimum_sufficient_route | Essential, optional, and non-essential modules. | Complexity replaces inference. |
| inference_boundary | What the current evidence cannot support. | The final guide hides uncertainty. |
| project_action | The next dataset, audit, analysis, validation, or decision. | The output cannot guide work. |

## Matrix Field Mapping

| Decision Matrix column | Decision node represented |
|---|---|
| evidence_bottleneck | evidence_bottleneck |
| data_selection_logic | data_boundary |
| qc_integration_logic | data_credibility |
| annotation_logic | object_identity |
| statistical_unit_logic | statistical_unit |
| confounding_factor_logic | confounding_factor |
| downstream_selection_logic | downstream_evidence_role |
| validation_hierarchy | validation_hierarchy |
| minimum_sufficient_route | minimum_sufficient_route |
| validation_logic | protected claim and validation credibility |
| technical_tradeoff | assumption, sacrifice, and failure mode |
| reusable_rule | transferable research-design law |
| limitation | inference_boundary |

## Rule

Do not invent a new category when one of these decision nodes is sufficient. If a paper exposes a new recurring decision pattern, add it here and then update the schema, rubric, examples, and validators together.
