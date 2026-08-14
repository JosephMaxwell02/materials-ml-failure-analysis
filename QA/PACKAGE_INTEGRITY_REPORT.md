# Package Integrity Report

- Release files including manifest: 116
- Manifest entries excluding self: 115
- Release total bytes: recorded in the detached adjacent build receipt
- Manifest verification: PASS
- ZIP bytes: recorded in the detached adjacent build receipt
- ZIP SHA-256: recorded in `reports/PACKAGE_BUILD_RESULT.json` outside the ZIP
- Duplicate groups: 7
- Duplicate review: six intentional PDF pairs appear in both their paper-specific folders
  and `papers/all-pdfs/`; one intentional Matbench repeat-adjudication JSON pair appears
  under `evidence/` and Paper 1 `reproduction/data/`. All paired hashes are identical.
- Unused assets: none detected by the allowlist build
- Missing manuscript figures: 0
- Malformed metadata findings: 0

The deterministic ZIP uses sorted paths, fixed archive timestamps and normalised file
permissions. `MANIFEST.sha256` excludes itself to avoid a recursive hash. Final archive
bytes and SHA-256 are necessarily detached: embedding either final value inside that
archive would change the archive and invalidate the recorded value.
