# Cross-Paper Evidence Synthesis Prompt

## Purpose

Turn many Paper Decision Audits into higher-order research-design knowledge. The synthesis is not the final product; it prepares the Research Action Guide.

Synthesize the corpus as a bioinformatics evidence architecture. The goal is to learn research laws from author choices: which decision node recurs, which evidence bottleneck determines the route, which details are transferable, and which details are paper-specific parameters.

## Required Output

1. Corpus statement:
   - number of candidates
   - number of audited papers
   - evidence roles represented
   - major gaps
2. Integrated scientific answer:
   - what the corpus can support
   - what it cannot support
   - what evidence is still needed
3. Evidence support for the synthesis lens, grouped by biological subquestion rather than paper order.
4. Claim strength matrix:

| Claim | Support level | Supporting papers | Strongest evidence | Weakest point | Next evidence needed |
|---|---|---|---|---|---|

5. Author choice pressure table:

| Paper | Choice | Scientific pressure | Vulnerability defended | Tradeoff | Transferable insight |
|---|---|---|---|---|---|

6. Data-selection logic:
   - what data authors chose
   - why those data were needed
   - what bias they controlled
   - what a weaker dataset would lose
7. QC/integration principles.
8. Annotation/object-definition principles.
9. Statistical and confounding-control principles:
   - statistical unit used for inference
   - biological replicate or patient-level unit
   - patient-level variation
   - common confounding factor patterns
   - study, platform, cancer-type, treatment, sampling, and metadata bias
   - comparison design and covariates
10. Downstream module principles, grouped by evidence role:
   - identity support
   - spatial context
   - progression direction
   - clinical association
   - mechanism
   - external replication
   - bias control
11. Minimum sufficient route:
    - which modules are essential for the biological judgment
    - which modules are optional, redundant, or decorative
    - which papers fell into an analysis full stack pattern
    - what each essential module changes about claim credibility
12. Validation hierarchy across the corpus:
    - internal consistency
    - external cohort
    - cross-platform
    - spatial
    - perturbational
    - functional validation
    - clinical endpoint
13. Biological working model:
    - clearly separate supported conclusions from hypotheses.
14. Screening rubric for the next evidence batch:
    - core inclusion
    - auxiliary inclusion
    - downgrade
    - exclusion
15. Evidence acquisition plan:
    - next searches as evidence roles, not only query strings.
16. Readiness judgment:
    - ready for Research Action Guide
    - or which Paper Decision Audits / evidence roles must be added first.

## Writing Standard

Start with the integrated answer, then use tables as evidence support. Tables must have interpretive text before and after them.

Do not produce fragmented lists that force the reader to assemble the conclusion.

Do not flatten the synthesis into a tool catalog. Every cross-paper rule should connect a decision node to a biological judgment, evidence role, failure mode, and practical screening or analysis action.
