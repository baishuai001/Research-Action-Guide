# Research Action Guide Prompt

## Purpose

Produce the final project-level action guide. This is not a literature review, not a summary, and not a method catalog. It must tell the project what to do next.

Write the guide as a bioinformatics evidence architecture for the user's concrete biological question. Use literature details to extract research laws, then translate those laws into local decisions: what to include, exclude, clean, integrate, annotate, compare, validate, and do next.

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
   - falsifiable biological judgment the route is built around
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

9. Statistical design and confounding-control plan:
   - statistical unit for each major comparison
   - biological replicate or patient-level unit
   - patient-level variation
   - comparison groups and covariates
   - main confounding factor risks
   - study, platform, cancer-type, treatment, sampling, and metadata bias
   - pseudoreplication or leakage risks
   - diagnostics and sensitivity analyses
10. Minimum sufficient route:
   - essential modules that directly protect the main biological judgment
   - optional modules that may be useful but are not decision-critical
   - modules to avoid because they add complexity without changing inference
   - analysis full stack risks to avoid
11. Validation hierarchy:
   - internal consistency needed before interpretation
   - external cohort or cross-platform validation needed before generalization
   - spatial, perturbational, functional validation, or clinical endpoint evidence needed before mechanism or translation claims
12. Decision rationale matrix:

| Project choice | Scientific rationale | Direct evidence | Inference | Assumption | Risk if wrong | Next action |
|---|---|---|---|---|---|---|

13. Literature support ledger:

| Recommendation | Supporting paper/audit | Evidence location | Direct evidence or inference |
|---|---|---|---|

14. Technical roadmap:
   - include a Mermaid diagram from dataset screening to validation and decision-ready output.
15. Immediate action list:
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
- Do not recommend a module unless its decision node, evidence role, and failure mode are explicit.
- Do not confuse parameter detail with philosophical or methodological understanding.
- If the evidence base is pilot-level, label the guide provisional.
