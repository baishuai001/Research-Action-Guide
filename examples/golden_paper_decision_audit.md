# Golden Paper Decision Audit Example

This is a compact shape example, not a real paper audit.

## Core Claim

The paper argues that a therapy-associated myeloid state predicts poor response.

## Evidence Architecture

The evidence bottleneck is object identity: the claim fails if the state is a batch-specific cluster or a generic inflammatory program.

| Decision node | Paper-specific choice | Scientific pressure | Failure mode | Reusable rule |
|---|---|---|---|---|
| data_boundary | Discovery and validation cohorts with response labels. | Response claims need labels beyond one cohort. | Cohort-specific association. | Clinical translation requires external cohort support. |
| data_credibility | Sample QC, doublet control, and patient-level aggregation. | Cell-level signal must survive sample-level checks. | Pseudoreplication. | Treat patient as statistical unit for response claims. |
| object_identity | Markers, reference mapping, and spatial confirmation. | The state must be the claimed cell object. | Wrong target object. | Annotation must protect the conclusion, not just name a cluster. |
| validation_hierarchy | External cohort plus spatial validation. | Generalization and tissue context are both needed. | Internal-only pattern. | Validation level should match claim strength. |
| minimum_sufficient_route | Annotation, response association, spatial check, external validation. | Each module protects a different claim weakness. | Analysis full stack. | Keep only modules that change inference. |

## Data Choice

The data choice combines a discovery cohort, an external cohort, response metadata, and spatial evidence because the claim requires both clinical association and tissue-context support.

## QC, Annotation, And Confounding Factor Logic

QC protects trusted differences by removing low-quality cells and checking patient-level robustness. Annotation protects object identity by combining markers, reference mapping, and spatial confirmation. The main confounding factor risks are treatment timing, sample source, batch, and patient-level variation.

## Validation Hierarchy

The validation hierarchy is: internal consistency -> external cohort -> spatial validation. Functional validation would be needed before claiming mechanism.

## Minimum Sufficient Route

The minimum sufficient route is discovery annotation, patient-level response association, external cohort validation, and spatial confirmation. Other modules are optional unless they rule out a specific alternative explanation.

## Supervision Verdict

PASS. The audit explains author choices as decision node logic and separates reusable rules from paper-specific parameters.
