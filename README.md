# Materials ML Failure Analysis

**What remains scientifically usable when data, models, explanations or reruns disagree?**

This public research compendium examines three distinctions: fitted feature importance
versus retrained removal, relative versus absolute predictive performance, and exact
replay versus scientific acceptance.

**New readers: [start with the question, worked example and execution map](START_HERE.md).**

> **Maintained public entry:** this GitHub repository.
> **Archived scientific release:** [Zenodo v1.0.0, DOI 10.5281/zenodo.21919563](https://doi.org/10.5281/zenodo.21919563).

The repository contains three papers, a programme monograph, a public technical
companion, selected evidence, replay receipts and small publication-specific scripts
that reconstruct the principal reported readouts.

> **This is a research compendium, not the production Systemica/Geatomica runtime.**
> Reusable orchestration, authority control, memory, progression, recovery and deployment
> implementations are intentionally excluded.

## Two different executable routes

1. **Accepted-table reconstruction in this repository** reads accepted derived tables,
   performs no model fitting and requires no external dataset.
2. **Selected fresh fitting in the separate
   [scientific verification rerunner](https://github.com/JosephMaxwell02/materials-ml-scientific-verification-rerunner)**
   performs bounded calculations from source data. Its documented defaults cover
   individual configurations, not the complete published campaigns.

Neither route is external replication, peer review or physical validation.

## Quick reconstruction

```bash
git clone https://github.com/JosephMaxwell02/materials-ml-failure-analysis.git
cd materials-ml-failure-analysis
python tools/verify_manifest.py
python reproduction/paper-1/reproduce.py
python reproduction/paper-2/reproduce.py
python reproduction/paper-3/reproduce.py
```

### Windows checkout path

On Windows, cloning beneath a deeply nested parent directory can fail before any
reconstruction runs because checkout paths exceed Git's default long-path handling. Use a
short, writable destination and enable long paths for the clone command itself. For example,
in Windows PowerShell:

```powershell
Set-Location C:\
git -c core.longpaths=true clone https://github.com/JosephMaxwell02/materials-ml-failure-analysis.git C:\SYSTEMICA_RSE_COMPENDIUM_20261021
Set-Location C:\SYSTEMICA_RSE_COMPENDIUM_20261021
python tools/verify_manifest.py
python reproduction/paper-1/reproduce.py
python reproduction/paper-2/reproduce.py
python reproduction/paper-3/reproduce.py
```

Choose another short writable path if that destination is unavailable. The command-scoped
Git setting changes checkout handling only; it does not weaken manifest verification.

These commands verify the maintained Git tree and reconstruct public readouts from
accepted tables. See [reproduction/README.md](reproduction/README.md) for exact scope.

## Three measured disagreements

| **0.0394** | **73.3% -> 4.51%** | **927,361; max delta = 0** |
|---|---|---|
| **Paper 1: fitted use vs retrained dependence** | **Paper 2: non-null signal vs absolute viability** | **Paper 3: exact replay vs bounded authority** |
| Mean rank agreement was close to zero under the frozen Matbench protocol. | Many MP elastic cells beat their paired null while very few cleared the minimal absolute boundary. | Exact Spatial V0.6.1 replay preserved both the bulk PASS and the conditional shear conclusion. |

These are bounded measurements, not claims of causal necessity, universal thresholds or
automatic engineering permission.

## Read the publications

- [Browser-readable guide](START_HERE.md)
- [Visual four-page guide from archived v1.0.0](START_HERE.pdf)
- [Paper 1 - Importance Is Not Necessity](papers/paper-1/PAPER_1_IMPORTANCE_IS_NOT_NECESSITY_FINAL.pdf)
- [Paper 2 - Better Than Null Is Not Yet Useful](papers/paper-2/PAPER_2_BETTER_THAN_NULL_IS_NOT_YET_USEFUL_FINAL.pdf)
- [Paper 3 - Available Evidence Is Not Engineering Authority](papers/paper-3/PAPER_3_AVAILABLE_EVIDENCE_IS_NOT_ENGINEERING_AUTHORITY_FINAL.pdf)
- [Current corrected Geatomica monograph v1.0.1](papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_V1_0_1_20261020.pdf)
- [Archived Geatomica monograph v1.0.0](papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_FINAL.pdf)
- [Public Technical & Industrial Companion V1.5](papers/technical-companion/EVIDENCE_STATE_RUNTIME_PUBLIC_TECHNICAL_INDUSTRIAL_COMPANION_V1_5_A4.pdf)
- [Six-page public explainer](papers/explainer/MATERIALS_ML_FAILURE_ANALYSIS_WHAT_IT_IS_V2.pdf)
- [Archived v1.0.0 PDF distribution copies](papers/all-pdfs/)

The [monograph navigation note](papers/monograph/README.md) identifies the canonical
maintained PDF and the preserved deposited version.

## Inspect the evidence

| Route | Purpose |
|---|---|
| [Reproduce](reproduction/README.md) | Reconstruct headline readouts from accepted public tables; no model fitting. |
| [Fresh fitting](https://github.com/JosephMaxwell02/materials-ml-scientific-verification-rerunner) | Run selected bounded model fits under a separate licence and scope. |
| [Evidence](evidence/) | Inspect bounded result and replay summaries. |
| [Protocols](protocols/) | Read the public experimental and replay contracts. |
| [Claim boundaries](boundaries/CLAIM_BOUNDARY.md) | See what the evidence does and does not support. |
| [Release audit](QA/PUBLIC_RELEASE_AUDIT.md) | Inspect disclosure, integrity, rights and release verification. |

## Evidence state

- **Matbench:** 3,440 fresh + 3,440 repeat units; 65,740 numeric cells; exact same-environment repeat.
- **Materials Project:** admission and elastic viability remain held/conditional; adverse replay findings are retained.
- **JARVIS:** local numerical replay passed at frozen tolerance; raw-byte divergence remains disclosed.
- **Spatial V0.6.1:** 576 fresh + 576 replay units; 927,361 cells exact; bulk metric geometry passed both views; shear polarity remained conditional.

Local replay is not external replication, peer review, physical qualification or
engineering deployment authority.

## Archive, maintenance and rights

The immutable archived scientific release is **Materials ML Failure Analysis - Public
Research Compendium v1.0.0** at [DOI 10.5281/zenodo.21919563](https://doi.org/10.5281/zenodo.21919563).
The maintained GitHub tree contains later integrity, navigation and documented correction
work. Those changes do not rewrite the deposited archive; see the versioned maintenance
receipts in this repository.

The papers are preprints. This repository does not claim peer review, journal publication,
external validation or engineering qualification.

Citation metadata for the archived release is in `CITATION.cff` and `.zenodo.json`.
Publication content and reference code remain copyright Joseph Maxwell; no open-source
licence is granted for this compendium unless an individual file explicitly says
otherwise. Public availability permits reading, citation and scholarly inspection under
applicable law, not unrestricted modification or reuse. Third-party source data are not
relicensed here; see [LICENSES](LICENSES/README.md).
