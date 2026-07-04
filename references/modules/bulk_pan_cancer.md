# Bulk And Pan-Cancer Module

Use this module when auditing or planning bulk RNA-seq, TCGA/GTEx/GEO integration, pan-cancer comparisons, signature scoring, or tumor microenvironment deconvolution.

| Decision node | Bulk/pan-cancer best-practice pressure |
|---|---|
| data_boundary | Capture cancer type, cohort source, normal controls, treatment status, stage, survival endpoint, platform, and duplicate samples. |
| data_credibility | Check normalization, batch, tumor purity, outliers, missing metadata, platform mixing, and study-level artifacts. |
| object_identity | Treat inferred cell states, immune infiltration, malignancy, and pathway scores as estimates requiring support. |
| statistical_unit | Patient/sample is usually the unit; gene, cell-type score, or tumor type is not an independent replicate. |
| confounding_factor | Control cancer type, stage, purity, treatment, age/sex if relevant, platform, center, and cohort source. |
| downstream_evidence_role | Use survival, differential expression, deconvolution, mutation, CNV, pathway, or drug association only when tied to a claim. |
| validation_hierarchy | External cohort and cross-platform validation are central before generalizing a bulk signature. |
| minimum_sufficient_route | Avoid piling on signatures unless each one resolves a distinct biological ambiguity. |

Red flag: a pan-cancer claim pools tumors without showing that cancer-type composition does not drive the result.
