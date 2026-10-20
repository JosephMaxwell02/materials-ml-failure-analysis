# Geatomica monograph v1.0.1 correction record

Date: 20 October 2026

State: QA candidate; not deposited

Predecessor: `papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_FINAL.pdf` from archived compendium v1.0.0

Successor: `papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_V1_0_1_20261020.pdf`

## Classification

The Appendix D preprocessing change is a **documentation-only correction** established
from sealed campaign identity receipts and the exact campaign-bound runner. No numerical
re-execution was required or performed. The accepted 288-cell table, 211/288 and 13/288
headline counts, protocols and historical archives are unchanged.

## Exact scientific correction

The v1.0.0 Appendix D row said that only Ridge received `StandardScaler` and tree models
used unscaled imputed values. That wording is contradicted by the bound execution. The
v1.0.1 row states:

> Preprocessing — All four model families used the same fold-local preprocessing: numeric
> coercion and median imputation followed by StandardScaler; categorical crystal-system
> values received most-frequent imputation and dense one-hot encoding with unknown
> categories ignored. All transformers were fitted on the training partition only.

## Bound execution identity

- Fresh execution: `exec-geatomica-mp-four-target-v0_1-20260801T003237Z-fresh`
- Fresh identity receipt: `Internal Documents (Classified)/Codex/external_validation/runs/exec-geatomica-mp-four-target-v0_1-20260801T003237Z-fresh_IDENTITY_RECEIPT.json`
- Fresh identity receipt SHA-256: `9b83a1ba11a807cfba44df2daaac8f3b7c4c3f06baf635dd984c59961ddd26ed`
- Replay execution: `exec-geatomica-mp-four-target-v0_1-20260802T125758Z-replay`
- Replay identity receipt: `Internal Documents (Classified)/Codex/external_validation/runs/exec-geatomica-mp-four-target-v0_1-20260802T125758Z-replay_IDENTITY_RECEIPT.json`
- Replay identity receipt SHA-256: `ef8de9e53a7411cfa333d0d68312c045a49f90aa9a3af98bf52177702f0b4964`
- Bound runner: `Internal Documents (Classified)/Codex/external_validation/geatomica_v1/run_unit.py`
- Bound runner SHA-256: `615c9969ec227c59934e4b206b747bd26002aae13c72982ab079737ac0b3d674`
- Accepted 288-cell table SHA-256: `f38ed6a843c03ce92cb44e0e972a2bf92eb12e9b13ab8196c06a09d245b4c7c8`

The private paths above are provenance identifiers in this governed correction record;
they are not public implementation disclosures and are not embedded in the monograph.

## Other maintenance-safe edits in the successor

- Figure 4.4 caption now matches the plotted ordering: chemical-system separation is
  hardest for formation energy and band gap; reduced-composition grouping is slightly
  harder for bulk and shear.
- The historical 88.0% raw-elasticity figure is explicitly distinguished from Paper 2's
  211/288 (73.3%) same-denominator result and 13/288 (4.51%) positive-R² result.
- The pre-deposit placeholder is replaced by the maintained repository and both archival
  DOI destinations, with reconstruction and selected-fitting scopes distinguished.
- Rights wording states the retained-copyright/no-open-source-grant position without
  implying that public access authorises modification or redistribution.
- The title and status pages identify this file as v1.0.1, a corrected successor to the
  preserved v1.0.0 manuscript.

## Exclusions

No data, experimental protocol, accepted result, historical receipt or archived Zenodo
object was edited. No patentability, ownership, external-validation or publication-status
conclusion was added.
