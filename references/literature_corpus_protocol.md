# Literature Corpus Protocol

## Purpose

Build a paper corpus that can support a Research Action Guide. The goal is not to collect every related paper; it is to collect enough evidence roles to make justified project decisions.

## Inputs

Accept rough clues:

- title
- DOI or PMID
- article URL
- local PDF path
- pasted abstract, methods, results, or full text
- RIS, CSV, TSV, Markdown list
- folder of PDFs
- citation trail from already included papers

The user should provide the smallest clue they have. The agent enriches the rest.

## Screening Logic

Screen by evidence role, not by keyword match alone.

| Evidence role | What it contributes |
|---|---|
| Identity precedent | How a paper establishes cell identity, state identity, malignant identity, spatial object, clinical label, or progression state. |
| Data strategy precedent | How authors choose cohorts, platforms, metadata, validation sets, and public datasets. |
| Technical route precedent | How authors choose QC, integration, annotation, modeling, spatial, trajectory, communication, clinical, perturbation, or external validation layers. |
| Contrast case | A useful paper that solves a similar problem differently. |
| Failure boundary | A paper that reveals what cannot be concluded from a weaker design. |
| Validation precedent | A paper that shows what type of validation makes a claim credible. |

## Candidate Status

| Status | Meaning |
|---|---|
| candidate | Identified but not yet screened. |
| title-abstract-screened | Metadata and abstract reviewed. |
| needs-full-text | Promising but insufficient methods/results evidence. |
| ready-for-audit | Enough evidence exists for a Paper Decision Audit. |
| audited | Paper Decision Audit completed and supervised. |
| matrix-ready | Decision Matrix row completed. |
| excluded | Not useful for the current evidence corpus. |
| hold | Potentially useful but blocked by missing evidence or unclear relevance. |
| duplicate | Same paper already represented. |

## Phase Gates

| Phase | Practical threshold | Required judgment |
|---|---|---|
| Pilot | 10-20 candidates and 3-5 audited papers | Identify obvious missing evidence roles and decide the next search direction. |
| First phase | about 50 candidates and 10-15 audited papers | Major evidence roles should have representative examples and contrast cases. |
| Guide-ready | about 20 high-quality audited papers, unless the topic is narrow | The corpus can support concrete project actions, and new papers add little new decision logic. |

## Stop Rule

Stop broad screening only when both are true:

1. the practical threshold for the current phase is met,
2. the evidence-role saturation requirement is credible.

If counts are met but important evidence roles are missing, continue targeted gap filling.
