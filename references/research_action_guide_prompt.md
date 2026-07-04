# Research Action Guide Prompt

## Purpose

Produce the final project-level action guide. This is not a literature review, not a summary, and not a method catalog. It must tell the project what to do next.

## Required Sections

1. Executive decision:
   - what the project can decide now
   - what remains unresolved
   - what evidence must be acquired next
2. Scientific premise:
   - current biological model
   - supported conclusions
   - hypotheses
   - boundaries of inference
3. Dataset screening criteria:

| Criterion | Required / preferred / exclusion | Scientific reason | Literature support | Risk if missing |
|---|---|---|---|---|

4. Inclusion, downgrade, hold, and exclusion standards:

| Decision | Standard | Reason | Example evidence role |
|---|---|---|---|

5. Data cleaning and QC plan:
   - sample-level QC
   - cell/spot-level QC
   - doublet or ambient RNA control
   - batch and platform checks
   - metadata completeness checks
   - study-level bias checks
6. Integration and batch strategy:
   - recommended strategy
   - what it protects
   - what it may erase
   - alternatives
   - diagnostics
   - literature support
7. Annotation and object-definition strategy:
   - target cell identity
   - state definition
   - malignant identity if relevant
   - spatial niche definition if relevant
   - response/progression labels if relevant
   - required validation
8. Downstream analysis module selection:

| Module | Evidence role | Why needed | Input requirement | Failure mode | Supporting papers |
|---|---|---|---|---|---|

9. Decision rationale matrix:

| Project choice | Scientific rationale | Direct evidence | Inference | Assumption | Risk if wrong | Next action |
|---|---|---|---|---|---|---|

10. Literature support ledger:

| Recommendation | Supporting paper/audit | Evidence location | Direct evidence or inference |
|---|---|---|---|

11. Technical roadmap:
   - include a Mermaid diagram from dataset screening to validation and decision-ready output.
12. Immediate action list:
   - next searches
   - datasets to prioritize
   - full texts or supplements to retrieve
   - analyses to prototype
   - decisions blocked by missing evidence

## Hard Rules

- Every major choice must be actionable.
- Every recommendation must have evidence support or be marked unresolved.
- Do not hide uncertainty.
- Do not use generic language as a substitute for decision criteria.
- If the evidence base is pilot-level, label the guide provisional.
