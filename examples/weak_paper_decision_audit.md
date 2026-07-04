# Weak Paper Decision Audit Example

This is a compact anti-example.

## Problem

The paper used Seurat, UMAP, clustering, marker genes, CellChat, enrichment analysis, and survival analysis. These methods are common in single-cell cancer research.

## Why This Fails

Verdict: REVISE

Main failure mode: the audit is a method catalog.

Missing decision nodes:

- No evidence bottleneck.
- No data boundary or data credibility logic.
- No object identity reasoning.
- No statistical unit or patient-level variation check.
- No confounding factor discussion.
- No validation hierarchy.
- No minimum sufficient route.

Next action: reread methods, supplement, figures, and code to identify why the authors chose each dataset, QC step, annotation strategy, downstream module, and validation layer.
