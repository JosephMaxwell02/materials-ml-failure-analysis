# Minimal Reproduction

These are publication-specific reference analyses. They reconstruct reported readouts
from sanitised accepted-result tables with the Python standard library. They do not fit
models and do not contain the production scientific runtime, recovery controller,
authority engine, memory system, orchestration, worker routing, or generic adapters.

Run each script from the repository root:

```text
python reproduction/paper-1/reproduce.py
python reproduction/paper-2/reproduce.py
python reproduction/paper-3/reproduce.py
```

Each command reads the accepted table packaged for one paper and prints a bounded summary.
The default scope is the complete packaged table for that paper; it performs zero new
estimator fits and writes no scientific receipt.

For the scientific questions and scope map, see [START_HERE](../START_HERE.md). For
selected fresh fits, use the separate
[scientific verification rerunner](https://github.com/JosephMaxwell02/materials-ml-scientific-verification-rerunner).
These reconstruction scripts do not regenerate the model fits or replace that smaller
fresh-computation route.
