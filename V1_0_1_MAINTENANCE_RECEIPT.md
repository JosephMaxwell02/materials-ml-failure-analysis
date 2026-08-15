# v1.0.1 repository maintenance receipt

## Scope

- Repository: `JosephMaxwell02/materials-ml-failure-analysis`
- Base tag and commit: `v1.0.0` / `9b1cd8d0df1e33d182103b48b03ea074a4b23b00`
- Historical sealed archive: `MATERIALS_ML_FAILURE_ANALYSIS_V1_0_0_20260814.zip`
- Historical archive SHA-256: `1154584044393459742122697a1852d66dacf801575f3b0ceccad50e699c85b1`

## Maintenance changes

- Declared canonical LF text and explicit binary handling in `.gitattributes`.
- Regenerated `MANIFEST.sha256` for the canonical v1.0.1 Git tree.
- Added clean-checkout manifest verification and the three existing public reconstruction routes to CI.
- Added a short quick-verification path to `README.md`.

The v1.0.0 clean-clone discrepancy was newline normalisation only. It did not affect
binary files, scientific values, reconstruction outputs or the integrity of the sealed
v1.0.0 ZIP.

## Verification

- Canonical Git-tree manifest: `120` files, PASS.
- Paper 1 reconstruction: PASS.
- Paper 2 reconstruction: PASS.
- Paper 3 public evidence-state inspection: PASS.
- Frozen scientific and publication files changed: `0`.
- Secret/private-path scan: PASS.
- Historical v1.0.0 archive SHA-256 recheck: PASS.

## Known documentation staleness

`KNOWN_DOCUMENTATION_STALENESS — DOI now assigned`: the frozen monograph says that
persistent identifiers will be inserted after archival deposit. This sentence is retained
for correction in the next substantive manuscript/preprint revision; the monograph and
archived PDF were not rebuilt for this maintenance patch.

## Claim boundary

No scientific claims or archived v1.0.0 scientific objects were changed.
