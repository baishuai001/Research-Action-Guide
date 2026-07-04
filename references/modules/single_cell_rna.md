# Single-Cell RNA-Seq Module

Use this module when auditing or planning scRNA-seq, snRNA-seq, CITE-seq, or atlas-style single-cell work.

| Decision node | Single-cell best-practice pressure |
|---|---|
| data_boundary | Require patient/sample metadata, tissue source, treatment status, disease stage, and platform details. |
| data_credibility | Check low-quality cells/nuclei, mitochondrial/ribosomal signal, library complexity, doublets, ambient RNA, and sample-level outliers. |
| object_identity | Support annotation with markers, references, malignant inference if relevant, sample distribution, and biological plausibility. |
| statistical_unit | Do not treat cells as independent biological replicates when patient or sample is the real unit. |
| confounding_factor | Separate cell abundance, patient-level variation, cancer type, treatment, batch, and tissue-site effects. |
| downstream_evidence_role | Use DE, pathway, trajectory, communication, regulon, CNV, or clinical association only when each module protects a claim. |
| validation_hierarchy | Prefer external cohort, cross-platform, spatial, flow/IHC, perturbational, or functional validation according to claim strength. |
| minimum_sufficient_route | Avoid an analysis full stack; include only modules that change identity, credibility, mechanism, or actionability. |

Red flag: a paper reports many clusters and pathways but never proves object identity or patient-level robustness.
