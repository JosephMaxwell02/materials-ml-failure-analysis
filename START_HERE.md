# What can a successful rerun tell us?

This materials-ML study asks when an apparently encouraging computational result is
enough to support the next scientific claim. It examines three disagreements: a feature
can look important yet be replaceable after retraining; a model can beat a shuffled-target
comparator yet predict poorly; and an exact rerun can preserve a result that still fails a
declared scientific criterion.

The papers report bounded computational studies by Joseph Maxwell. They do not establish
physical validation, independent replication, production readiness or engineering
permission.

## One worked example

In a frozen 256-material structural study, the acceptance rule required a shear-related
feature addition to improve R² by at least 0.02 in each of two evaluation views. The
reported improvements were 0.0123 in the continuity view and 0.0453 in the
chemical-system-separated view. The first view failed that rule. Exact same-environment
replay preserved the numbers and the conditional conclusion.

The practical lesson is to record both the computational comparison and the scientific
criterion. Agreement with a previous execution does not make a failed scientific
criterion pass.

See the worked example in the [technical companion](papers/technical-companion/EVIDENCE_STATE_RUNTIME_PUBLIC_TECHNICAL_INDUSTRIAL_COMPANION_V1_5_A4.pdf)
and the [accepted spatial evidence](evidence/spatial-v0.6.1/). Those are the reported
historical results. The smaller public fitting route described below does not rerun this
entire comparison.

## Choose what you want to inspect

| Question | Read first | Result and limitation |
|---|---|---|
| Does fitted feature importance predict the consequence of removing a feature and retraining? | [Paper 1](papers/paper-1/PAPER_1_IMPORTANCE_IS_NOT_NECESSITY_FINAL.pdf) | Mean rank agreement 0.0394 across the declared Matbench comparisons. This is not causal necessity or a universal feature ranking. |
| Does beating a permutation comparator imply useful prediction? | [Paper 2](papers/paper-2/PAPER_2_BETTER_THAN_NULL_IS_NOT_YET_USEFUL_FINAL.pdf) | On the same 288 cells, 211 beat their mean paired null and 13 had positive held-out R². Positive R² is only a minimal reference boundary. |
| What does a successful replay establish? | [Paper 3](papers/paper-3/PAPER_3_AVAILABLE_EVIDENCE_IS_NOT_ENGINEERING_AUTHORITY_FINAL.pdf) | Different routes compare numerical, semantic and byte agreement. Agreement does not settle source suitability, scientific adequacy or human engineering decisions. |

The [current corrected monograph](papers/monograph/GEATOMICA_FLAGSHIP_MONOGRAPH_V1_0_1_20261020.pdf)
contains the wider research history and experimental context. It is optional background
for a first encounter. The deposited v1.0.0 monograph remains available through the
[archive DOI](https://doi.org/10.5281/zenodo.21919563).

## What you can execute

**Reconstruct the reported readouts.** This repository's three
[reproduction scripts](reproduction/README.md) read accepted derived tables. They require
no external dataset and fit no models. This checks how the reported summaries follow from
the supplied evidence; it does not independently regenerate that evidence.

**Run a smaller fresh calculation.** The separate
[scientific verification rerunner](https://github.com/JosephMaxwell02/materials-ml-scientific-verification-rerunner)
fits selected models from source data and then compares the computed receipt with accepted
reference values. Its documented defaults are:

- Matbench: one official fold, a baseline and one retrained feature removal using the
  generated cache. It does not regenerate the full ranking result.
- Materials Project: one Ridge comparison cell and 30 target-permutation fits. The exact
  historical input files are not redistributed; current API data are not the same
  historical experiment.
- Spatial/JARVIS: one bulk-modulus configuration and split view, with four folds and paired
  null fits. It does not reproduce the full geometry/sham or shear acceptance comparisons.

The rerunner's smoke checks use small synthetic examples. Its full-campaign command
explicitly refuses because the complete historical campaigns are not bound into that
public implementation. Use a disposable clone and isolated environment, and read its input
and licence instructions before running it.

## What remains open

The reported repeats were local computations, not independent-group replication. Physical
measurements, external validation and general superiority over other methods have not been
established. The historical Materials Project input restriction prevents a wholly
self-service exact rerun of that route. The public code excludes the private runtime and
recovery controller.

The compendium has no open-source code licence; the separate rerunner permits execution of
unmodified copies for non-commercial scientific verification under its stated licence.
Public access does not imply unrestricted modification, redistribution or reuse.

Maintained repositories: [research compendium](https://github.com/JosephMaxwell02/materials-ml-failure-analysis)
and [verification rerunner](https://github.com/JosephMaxwell02/materials-ml-scientific-verification-rerunner).
Archives: [research compendium DOI](https://doi.org/10.5281/zenodo.21919563) and
[verification rerunner DOI](https://doi.org/10.5281/zenodo.21939447). See the
[claim boundaries](boundaries/CLAIM_BOUNDARY.md) for the programme's explicit limits.
