"""Reconstruct Paper 1 headline readouts from accepted public tables."""
import csv
import json
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

def rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

tasks = rows("task_summary.csv")
correlations = rows("importance_removal_correlations.csv")
topk = [r for r in rows("topk_overlap.csv") if int(r["k"]) == 10]
groups = rows("group_level_correlation_readout.csv")
chance = rows("top10_chance_reference.csv")[0]
counts = rows("individual_removal_outcome_counts.csv")
repeat = json.loads((DATA / "fresh_repeat_adjudication_summary.json").read_text())

result = {
    "baseline_mean_r2": {r["task"]: float(r["mean_r2"]) for r in tasks},
    "mean_spearman": mean(float(r["permutation_vs_removal_spearman"]) for r in correlations),
    "spearman_range": [
        min(float(r["permutation_vs_removal_spearman"]) for r in correlations),
        max(float(r["permutation_vs_removal_spearman"]) for r in correlations),
    ],
    "mean_top10_overlap": mean(float(r["overlap_fraction"]) for r in topk),
    "random_top10_expectation": float(chance["random_ranking_expected_overlap_fraction"]),
    "top10_one_sided_probability": float(chance["one_sided_probability_total_at_least_observed"]),
    "individual_removal_counts": {r["outcome"]: int(r["count"]) for r in counts},
    "positive_group_means": {r["task"]: int(r["positive_mean_group_removal_count"]) for r in groups},
    "group_spearman": {r["task"]: float(r["spearman_aggregated_fitted_vs_group_removal"]) for r in groups},
    "fresh_units": int(repeat["units_compared"]),
    "repeat_units": int(repeat["units_compared"]),
    "repeat_numeric_cells": int(repeat["numeric_cells_compared"]),
    "repeat_max_abs_difference": float(repeat["maximum_absolute_difference"]),
}

expected = {
    "mean_spearman": 0.039404,
    "mean_top10_overlap": 0.1,
    "fresh_units": 3440,
    "repeat_numeric_cells": 65740,
    "repeat_max_abs_difference": 0.0,
}
assert abs(result["mean_spearman"] - expected["mean_spearman"]) < 5e-7
assert result["mean_top10_overlap"] == expected["mean_top10_overlap"]
assert result["fresh_units"] == expected["fresh_units"]
assert result["repeat_numeric_cells"] == expected["repeat_numeric_cells"]
assert result["repeat_max_abs_difference"] == expected["repeat_max_abs_difference"]
print(json.dumps(result, indent=2, sort_keys=True))
