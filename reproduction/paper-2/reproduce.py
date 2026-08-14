"""Reconstruct Paper 2 same-denominator viability readouts."""
import csv
import json
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

def rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

cells = rows("mp_elastic_null_comparable_cells.csv")
summary = {r["target"]: r for r in rows("mp_elastic_viability_summary.csv")}
admission = {r["measure"]: int(r["value"]) for r in rows("mp_admission_and_replay_summary.csv")}
beats_null = [r for r in cells if float(r["r2_minus_null"]) > 0]
positive_r2 = [r for r in cells if float(r["baseline_r2"]) > 0]
both = [r for r in cells if float(r["baseline_r2"]) > 0 and float(r["r2_minus_null"]) > 0]
result = {
    "eligible_cells": len(cells),
    "beats_null": len(beats_null),
    "beats_null_fraction": len(beats_null) / len(cells),
    "positive_r2": len(positive_r2),
    "positive_r2_fraction": len(positive_r2) / len(cells),
    "passes_both": len(both),
    "passes_both_fraction": len(both) / len(cells),
    "all_both_passes_bulk": all(r["target"] == "bulk_modulus" for r in both),
    "null_comparable_median_r2": median(float(r["baseline_r2"]) for r in cells),
    "route_wide_positive_r2_cells": round(float(summary["combined_elastic"]["positive_baseline_r2_fraction"]) * int(summary["combined_elastic"]["baseline_cells"])),
    "route_wide_cells": int(summary["combined_elastic"]["baseline_cells"]),
    "route_wide_median_r2": float(summary["combined_elastic"]["median_baseline_r2"]),
    "bulk_median_r2": float(summary["bulk_modulus"]["median_baseline_r2"]),
    "shear_median_r2": float(summary["shear_modulus"]["median_baseline_r2"]),
    "admission_and_replay": admission,
}
assert result["eligible_cells"] == 288
assert result["beats_null"] == 211
assert result["positive_r2"] == 13
assert result["passes_both"] == 13
assert result["all_both_passes_bulk"]
assert result["route_wide_positive_r2_cells"] == 20
assert result["route_wide_cells"] == 1152
print(json.dumps(result, indent=2, sort_keys=True))
