"""Inspect the public evidence-state examples; this is not an authority engine."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

def rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

states = rows("evidence_state_examples.csv")
replay = rows("programme_replay_ledger.csv")
cases = rows("bounded_engineering_case_summary.csv")
result = {
    "state_examples": states,
    "replay_routes": len(replay),
    "spatial_v0_6_1": next(r for r in replay if r["route"] == "Spatial V0.6.1"),
    "historical_engineering_cases": [r["case"] for r in cases],
    "authority_rule": "No state is promoted by this reference analysis.",
}
assert result["spatial_v0_6_1"]["numeric_cells"] == "927361"
assert all(r["present_architecture_retroactive"] == "no" for r in cases)
print(json.dumps(result, indent=2, sort_keys=True))
