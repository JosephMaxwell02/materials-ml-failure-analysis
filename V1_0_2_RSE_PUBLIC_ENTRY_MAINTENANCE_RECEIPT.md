# v1.0.2 RSE public-entry maintenance receipt

Date: 20 October 2026

State: local QA candidate; not pushed, deposited, published or submitted to RSE

Repository: `JosephMaxwell02/materials-ml-failure-analysis`

Base commit: `5e0068bcdbf50a680162bc734c30c80ec5ddba13`

## Classification

This pass contains one adjudicated scientific-documentation correction and bounded
navigation/editorial maintenance. It introduces no new experiment, architecture,
numerical result, model fit or scientific claim.

## Scientific-documentation changes

- Created the versioned monograph successor
  `papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_V1_0_1_20261020.pdf` and its TeX source.
- Corrected Appendix D to state the adjudicated common fold-local preprocessing used by
  Ridge, Random Forest, Extra Trees and HistGradientBoosting.
- Corrected Figure 4.4's caption to match the target-specific grouped-split ordering.
- Distinguished the historical raw-elasticity 88.0% population from Paper 2's
  same-denominator 211/288 (73.3%) and 13/288 (4.51%) results.
- Preserved the accepted 288-cell table and all reported values; no numerical
  re-execution was required or performed.

The bound identities, receipt hashes and runner hash are recorded in
`QA/GEATOMICA_MONOGRAPH_V1_0_1_CORRECTION_RECORD_20261020.md`.

## Navigation and editorial changes

- Added the browser-readable `START_HERE.md` entrance.
- Reworked the root README entrance and reproduction guide around the reader's question.
- Added prominent reciprocal routing to the separate scientific-verification rerunner.
- Distinguished accepted-table reconstruction from selected fresh fitting.
- Stated exact command scopes, archive-versus-maintenance status and the retained-rights
  boundary.
- Added canonical navigation for the corrected and archived monograph PDFs.
- Replaced pre-deposit placeholders in the successor with current repository and DOI
  destinations.

## Successor identities

- Corrected PDF SHA-256:
  `4206d7123139d92bd07bba088a86e0b87e847b4f19bc596adc4feaa232459c8d`
- Corrected TeX SHA-256:
  `cf5f19b54c9ed2e4bd84c9ed5b08da88139775aaf15b5c6d6d5fa2d5574195f6`
- PDF format: A4, 149 pages.

## Preserved archive identities

- Deposited v1.0.0 monograph PDF SHA-256:
  `b8ed98ecd47ae86464e3523df2f83faff07923e62355ee091f2d94bd91a192c5`
- Deposited v1.0.0 monograph TeX SHA-256:
  `9b6680000742849a015ebf3c8cca39d7a4e622e59653f0bd35002ea7c6cdc3c0`
- Sealed v1.0.0 compendium ZIP SHA-256:
  `1154584044393459742122697a1852d66dacf801575f3b0ceccad50e699c85b1`

The deposited Zenodo v1.0.0 object and its archived local files were not overwritten.

## Verification

- Paper 1 accepted-table reconstruction: PASS.
- Paper 2 accepted-table reconstruction: PASS; 211/288 and 13/288 retained.
- Paper 3 public evidence-state reconstruction: PASS.
- Relative Markdown destinations: PASS.
- Four maintained repository/DOI destinations: HTTP 200 after redirects.
- Corrected PDF link annotations: PASS.
- Corrected PDF visual QA: all 149 pages inspected as contact sheets; six changed or
  governance-critical pages inspected individually; no clipping or malformed layout.
- Canonical-tree manifest: regenerated and verified from a clean local checkout.

## External-action boundary

Public GitHub updated: **NO**.

Zenodo or other archived release updated: **NO**.

RSE submission or contact performed: **NO**.

Canonical RSE-newsletter URL after QA and publication approval:
`https://github.com/JosephMaxwell02/materials-ml-failure-analysis`
