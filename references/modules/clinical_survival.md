# Clinical And Survival Module

Use this module when auditing or planning prognosis, therapy response, biomarker, immunotherapy, or clinical translation analyses.

| Decision node | Clinical best-practice pressure |
|---|---|
| data_boundary | Capture endpoint definition, treatment timing, baseline/on-treatment status, follow-up, censoring, response criteria, and cohort eligibility. |
| data_credibility | Check endpoint completeness, label consistency, missingness, cohort imbalance, and measurement timing. |
| object_identity | Ensure the biomarker, cell state, signature, or niche is stable enough to support clinical interpretation. |
| statistical_unit | Patient is the inference unit; repeated samples need paired or hierarchical handling. |
| confounding_factor | Control treatment, stage, cancer type, line of therapy, sampling time, performance status if available, and cohort source. |
| downstream_evidence_role | Use survival, response association, stratification, calibration, or decision-curve logic only when clinically interpretable. |
| validation_hierarchy | Clinical endpoint support is stronger than internal association; external cohort validation is usually required for translation. |
| minimum_sufficient_route | Prefer a small clinically interpretable route over a broad analysis full stack. |

Red flag: a biomarker is called clinically useful without external cohort validation, endpoint clarity, or confounding control.
