# Golden Supervision Report Example

Verdict: REVISE

Artifact reviewed: Paper Decision Audit P0004

Main failure mode: the audit captures useful methods details but has not yet converted them into decision node logic.

Decision nodes checked: data boundary, data credibility, object identity, statistical unit, confounding factor, validation hierarchy, minimum sufficient route.

Evidence architecture judgment: the audit identifies QC, integration, annotation, and external validation, but the chain from uncertainty to author choice to protected claim is incomplete.

Direct evidence vs inference: direct evidence from methods and figures is partially separated from inference; however, the claim that the state predicts response is not clearly marked as patient-level inference.

Statistical unit and confounding: the patient is the correct statistical unit for response association. The current audit must add patient-level variation, treatment timing, cohort source, platform, and cancer-type composition as possible confounding factor risks.

Validation hierarchy: internal consistency and external cohort support are named, but spatial and functional validation are not distinguished. Mechanistic claims should be downgraded unless perturbational or functional validation is available.

Minimum sufficient route: annotation, patient-level association, and external cohort validation are essential. The pathway and communication modules should be marked optional unless they test a specific failure mode. Avoid turning the paper into an analysis full stack.

Chinese academic quality: the Chinese is mostly clear, but several sentences are too generic. Revise toward life-science academic Chinese / 生命科学学术性 by naming the biological object, evidence bottleneck, inference boundary, and validation level.

Required revisions:

1. Add a decision-node table for data choice, QC/integration, annotation, statistical unit, validation hierarchy, and downstream modules.
2. Separate direct evidence, inference, assumption, risk if wrong, and next action.
3. Replace generic phrases such as "结果比较可靠" with claim-specific language.

Next action: revise the audit before adding this paper to the Decision Matrix.
