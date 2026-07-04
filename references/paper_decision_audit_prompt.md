# Paper Decision Audit Prompt

## Boundary

Analyze one paper only. Do not advise the user's project inside this audit. The goal is to understand how the authors organized evidence and why they made each choice.

## Output Structure

1. Bibliographic information and evidence depth.
2. Core scientific question.
3. Main conclusion the authors want to establish.
4. Evidence foundations:
   - What establishes data credibility?
   - What establishes cell/object identity?
   - What establishes the main conclusion?
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
9. Evidence organization:
   - Show sequential, parallel, branching, and convergent evidence logic.
   - Include a Mermaid diagram when useful.
   - The diagram should be claim-centered, not method-centered.
10. Downstream module selection:
   - Which downstream analyses were used?
   - Which specific weakness in the evidence chain did each module address?
   - What realistic alternative could have been used?
11. Key technical choices:
   - choice
   - alternative
   - why this choice fits this paper
   - assumptions
   - risk if wrong
   - impact on the main conclusion
12. Why this technical route was necessary.
13. What would be lost or biased if the authors used another route.
14. Reusable decision logic:
   - biological question type
   - evidence bottleneck
   - transferable design pattern
   - data-selection rule
   - QC/integration rule
   - annotation rule
   - downstream-module rule
   - validation rule
   - boundary of reuse
15. Decision-node table:

| Decision node | Paper-specific choice | Scientific pressure behind the choice | Alternative | Failure mode | Reusable rule |
|---|---|---|---|---|---|

## Hard Rules

- Do not stop at method names.
- Do not write generic statements such as "different questions need different analyses" unless grounded in paper-specific details.
- If details are unavailable, mark the audit as needing full text, supplement, or code review.
- Keep the user's final biological question out of this single-paper audit.
