# Spatial Transcriptomics Module

Use this module when auditing or planning spatial transcriptomics, imaging-based spatial omics, tissue neighborhood, or niche analysis.

| Decision node | Spatial best-practice pressure |
|---|---|
| data_boundary | Capture tissue region, sampling site, section quality, spatial resolution, paired single-cell data, and clinical labels. |
| data_credibility | Check tissue damage, spot/cell quality, segmentation or deconvolution uncertainty, slide/batch effects, and region imbalance. |
| object_identity | Define spatial niches, neighborhoods, tumor/stroma/immune compartments, and cell states with orthogonal or reference support. |
| statistical_unit | Distinguish spot, cell, region, section, sample, and patient as inference units. |
| confounding_factor | Control tissue region, tumor purity, section depth, platform, sample handling, and patient-level variation. |
| downstream_evidence_role | Use neighborhood, colocalization, ligand-receptor, spatial domain, or gradient analysis only when it tests a claim vulnerability. |
| validation_hierarchy | Spatial validation can support location claims, but mechanism still needs perturbational or functional validation. |
| minimum_sufficient_route | Do not add spatial modules unless they sharpen object identity, niche definition, or mechanistic inference. |

Red flag: a niche is named from proximity alone without object identity, tissue-region controls, or patient-level robustness.
