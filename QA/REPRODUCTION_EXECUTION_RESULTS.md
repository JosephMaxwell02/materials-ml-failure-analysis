# Reproduction Execution Results

## `reproduction/paper-1/reproduce.py`

Exit code: `0`

```json
{
  "baseline_mean_r2": {
    "matbench_log_gvrh": 0.7503567800221302,
    "matbench_log_kvrh": 0.764881224187688,
    "matbench_mp_e_form": 0.9484262289869541,
    "matbench_mp_gap": 0.8082986019735781
  },
  "fresh_units": 3440,
  "group_spearman": {
    "matbench_log_gvrh": -0.2615763546798029,
    "matbench_log_kvrh": -0.1886699507389162,
    "matbench_mp_e_form": 0.46847290640394085,
    "matbench_mp_gap": 0.36896551724137927
  },
  "individual_removal_counts": {
    "improved_mae": 1781,
    "worsened_mae": 1059
  },
  "mean_spearman": 0.03940371884633198,
  "mean_top10_overlap": 0.1,
  "positive_group_means": {
    "matbench_log_gvrh": 6,
    "matbench_log_kvrh": 0,
    "matbench_mp_e_form": 20,
    "matbench_mp_gap": 20
  },
  "random_top10_expectation": 0.07042253521126761,
  "repeat_max_abs_difference": 0.0,
  "repeat_numeric_cells": 65740,
  "repeat_units": 3440,
  "spearman_range": [
    -0.28150363271729767,
    0.21394577852474167
  ],
  "top10_one_sided_probability": 0.06592675697420823
}
```

## `reproduction/paper-2/reproduce.py`

Exit code: `0`

```json
{
  "admission_and_replay": {
    "anomalous_or_unresolved": 2165,
    "conditional": 23891,
    "elastic_record_target_pairs": 26056,
    "fresh_units": 64,
    "replay_numeric_cells": 37924,
    "replay_units": 64,
    "strict_tolerance_exceedances": 916,
    "strongest_stable": 0
  },
  "all_both_passes_bulk": true,
  "beats_null": 211,
  "beats_null_fraction": 0.7326388888888888,
  "bulk_median_r2": -4.8657436927447755,
  "eligible_cells": 288,
  "null_comparable_median_r2": -0.4204734714793343,
  "passes_both": 13,
  "passes_both_fraction": 0.04513888888888889,
  "positive_r2": 13,
  "positive_r2_fraction": 0.04513888888888889,
  "route_wide_cells": 1152,
  "route_wide_median_r2": -2.248117060566412,
  "route_wide_positive_r2_cells": 20,
  "shear_median_r2": -0.6881161778769966
}
```

## `reproduction/paper-3/reproduce.py`

Exit code: `0`

```json
{
  "authority_rule": "No state is promoted by this reference analysis.",
  "historical_engineering_cases": [
    "Furnace",
    "Dual tank",
    "Heat shield"
  ],
  "replay_routes": 5,
  "spatial_v0_6_1": {
    "fresh_units": "576",
    "max_abs_delta": "0",
    "numeric_cells": "927361",
    "replay_units": "576",
    "route": "Spatial V0.6.1",
    "state": "EXACT_BYTE_METADATA_NUMERIC_REPLAY"
  },
  "state_examples": [
    {
      "admitted": "0",
      "available": "1",
      "bounded_disposition_recorded": "1",
      "case": "MP admission",
      "disposition": "HOLD",
      "replayed": "1",
      "viable": "NA"
    },
    {
      "admitted": "CONDITIONAL",
      "available": "1",
      "bounded_disposition_recorded": "1",
      "case": "MP elastic viability",
      "disposition": "HOLD",
      "replayed": "0",
      "viable": "0"
    },
    {
      "admitted": "1",
      "available": "1",
      "bounded_disposition_recorded": "1",
      "case": "Spatial bulk geometry",
      "disposition": "BOUNDED_PASS",
      "replayed": "1",
      "viable": "1"
    },
    {
      "admitted": "1",
      "available": "1",
      "bounded_disposition_recorded": "1",
      "case": "Spatial shear polarity",
      "disposition": "CONDITIONAL",
      "replayed": "1",
      "viable": "MIXED"
    }
  ]
}
```
