# Decision Matrix Schema

One row equals one evidence-eligible paper.

Required columns:

| Column | Meaning |
|---|---|
| paper_id | Stable ID such as P0001. |
| title | Paper title. |
| year | Publication year. |
| doi_or_pmid | DOI, PMID, or other stable identifier. |
| evidence_depth | full-text-read, methods-reviewed, supplement-reviewed, code-reviewed, or insufficient. |
| biological_question_type | What kind of biological uncertainty the paper addresses. |
| evidence_bottleneck | The uncertainty that would make the main conclusion fail if unresolved. |
| data_selection_logic | Why authors included each major data source. |
| qc_integration_logic | How data credibility was established and what tradeoff was accepted. |
| annotation_logic | How the biological object was defined. |
| statistical_unit_logic | What was treated as the independent unit and whether patient-level variation was protected. |
| confounding_factor_logic | Which confounding factor risks were controlled or left unresolved. |
| downstream_selection_logic | Why downstream modules were chosen by evidence role. |
| validation_hierarchy | Which validation level was used, such as internal consistency, external cohort, cross-platform, spatial, perturbational, functional validation, or clinical endpoint. |
| minimum_sufficient_route | Which modules were essential, optional, or part of an analysis full stack. |
| validation_logic | What made the main claim more credible. |
| technical_tradeoff | What the chosen route gained and sacrificed. |
| reusable_rule | Transferable design rule extracted from the paper. |
| limitation | Main boundary of reuse. |
| audit_path | Path to the Paper Decision Audit. |

Metadata-only and abstract-only papers must not enter the Decision Matrix.
