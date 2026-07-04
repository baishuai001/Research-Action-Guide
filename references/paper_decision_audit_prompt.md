# Paper Decision Audit Prompt

## Boundary

Analyze one paper only. Do not advise the user's project inside this audit. The goal is to understand how the authors organized evidence and why they made each choice.

Use the paper as a bioinformatics evidence architecture. Absorb concrete details, but translate them into decision node logic: what uncertainty forced this choice, what claim it protected, what assumption it introduced, what failure mode it avoided, and what reusable rule can be transferred.

## Output Structure

1. Bibliographic information and evidence depth.
2. Core scientific question.
3. Main conclusion the authors want to establish.
4. Evidence foundations:
   - What establishes data credibility?
   - What establishes cell/object identity?
   - What establishes the main conclusion?
   - Which evidence bottleneck would make the conclusion fail if unresolved?
5. Main technical route type.
6. Data choice logic:
   - What data were included?
   - Why were these data necessary?
   - What evidence role did each dataset, cohort, platform, metadata type, or validation layer play?
   - What bias or ambiguity did each data choice control?
7. QC, cleaning, and integration logic:
   - What was filtered or normalized?
   - What batch, sample, platform, or study-level bias was controlled?
   - What biological signal might be erased by overcorrection?
   - What artifact might appear if correction is too weak?
8. Annotation and object-definition logic:
   - How were cell types, states, malignant cells, spatial niches, clinical labels, or progression states established?
   - Which marker, reference, model, trajectory, regulon, modality, or validation evidence supported identity?
   - What conclusion would fail if annotation were wrong?
9. Statistical unit and confounding factor logic:
   - What was treated as the independent unit: patient, sample, tumor, lesion, batch, study, spot, or cell?
   - How did the authors handle patient-level variation?
   - Which confounding factor could explain the result: cancer type, treatment, stage, tissue site, platform, sequencing depth, sample processing, or study source?
   - What false conclusion would appear if cells or spots were treated as independent when the real replicate was patient or sample?
10. Validation hierarchy:
   - Which validation level was used: internal consistency, external cohort, cross-platform, spatial, perturbational, functional validation, or clinical endpoint?
   - Why was that level sufficient or insufficient for the claim?
   - What stronger validation would be needed for clinical translation or mechanism?
11. Evidence organization:
   - Show sequential, parallel, branching, and convergent evidence logic.
   - Include a Mermaid diagram when useful.
   - The diagram should be claim-centered, not method-centered.
12. Downstream module selection:
   - Which downstream analyses were used?
   - Which specific weakness in the evidence chain did each module address?
   - What realistic alternative could have been used?
   - Did the paper avoid an analysis full stack, or did it run modules that did not change inference?
13. Key technical choices:
   - choice
   - alternative
   - why this choice fits this paper
   - assumptions
   - risk if wrong
   - impact on the main conclusion
   - decision node served by this choice
14. Why this technical route was necessary.
15. What would be lost or biased if the authors used another route.
16. Reusable decision logic:
   - biological question type
   - evidence bottleneck
   - minimum sufficient route
   - transferable design pattern
   - data-selection rule
   - QC/integration rule
   - annotation rule
   - statistical-unit rule
   - confounding-control rule
   - downstream-module rule
   - validation hierarchy rule
   - boundary of reuse
17. Decision-node table:

| Decision node | Paper-specific choice | Scientific pressure behind the choice | Alternative | Failure mode | Reusable rule |
|---|---|---|---|---|---|

## Hard Rules

- Do not stop at method names.
- Do not let parameters, thresholds, software names, or figure details replace evidence architecture reasoning.
- Do not write generic statements such as "different questions need different analyses" unless grounded in paper-specific details.
- If details are unavailable, mark the audit as needing full text, supplement, or code review.
- Keep the user's final biological question out of this single-paper audit.
