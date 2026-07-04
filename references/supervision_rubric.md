# Supervision Rubric

Use this rubric when deciding whether a Paper Decision Audit, Decision Matrix row, Cross-Paper Evidence Synthesis, or Research Action Guide passes supervision.

Score each criterion 0-2:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| decision node clarity | Mostly method names or summary. | Some choices mapped to decision nodes. | Every major choice has a clear decision node. |
| detail-to-logic conversion | Preserves details without interpretation. | Explains some details as author choices. | Converts details into evidence role, assumption, failure mode, and reusable rule. |
| data and object credibility | Counts samples/clusters only. | Mentions QC or annotation evidence. | Explains data credibility and object identity as foundations of the claim. |
| statistical unit and confounding | Missing or generic. | Notes patient/study/batch issues. | Explicitly handles statistical unit, patient-level variation, and confounding factor risks. |
| validation hierarchy | Treats validation as one category. | Names validation type. | Judges whether internal, external cohort, cross-platform, spatial, perturbational, functional validation, or clinical endpoint evidence fits the claim. |
| minimum sufficient route | Runs or praises many modules. | Separates some essential and optional modules. | Identifies essential modules and rejects analysis full stack behavior. |
| direct evidence vs inference | Blended. | Sometimes separated. | Clearly separates direct evidence, inference, assumption, and unresolved gap. |
| actionability | Descriptive. | Has partial next steps. | Guides inclusion, exclusion, QC, integration, annotation, analysis, validation, or next search. |
| life-science academic Chinese | Colloquial, decorative, machine-translated, or vague. | Mostly clear but sometimes generic. | Uses precise life-science academic Chinese with biological objects, evidence boundaries, and claim strength clearly named. |

Verdict:

- `PASS`: no criterion scored 0, and actionability, decision node clarity, and life-science academic Chinese all score 2 when Chinese output is present.
- `REVISE`: any criterion scores 0, or the artifact is mostly descriptive.
- `HOLD`: evidence is insufficient because full text, supplement, code, or metadata is missing.

Supervision note format:

```text
Verdict: PASS | REVISE | HOLD
Main failure mode:
Decision node needing revision:
Evidence needed:
Next action:
```
