"""Reproducible synthetic churn dataset and a single pysubgroup run.

The generator intentionally keeps the hidden interaction out of the table: it is
only encoded in the Bernoulli probability used to sample churn.  Discovery and
holdout are independent windows with the same deterministic recipe.
"""
from __future__ import annotations

import json
import math
import platform
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np
import pandas as pd
import pysubgroup as ps

SEED = 20260826
N = 11_000
OUT = Path(__file__).resolve().parents[1] / "data"


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def make_window(seed: int, n: int = N) -> tuple[pd.DataFrame, dict[str, float]]:
    rng = np.random.default_rng(seed)
    contract = rng.choice(["month-to-month", "one-year", "two-year"], n, p=[0.52, 0.28, 0.20])
    plan = rng.choice(["basic", "plus", "premium"], n, p=[0.42, 0.38, 0.20])
    tenure = np.clip(rng.gamma(2.1, 15.0, n).round().astype(int), 1, 72)
    autopay = rng.choice(["yes", "no"], n, p=[0.63, 0.37])
    monthly = np.clip(rng.normal(62, 17, n), 25, 135).round(2)

    # Service events are related but not duplicates: a noisy service-pressure
    # term makes complaints more likely after outages, without a risk_niche col.
    outages = rng.poisson(1.35 + 0.18 * (plan == "basic"), n)
    complaint_rate = 0.42 + 0.22 * (outages >= 1) + 0.10 * (contract == "month-to-month")
    complaints = rng.poisson(complaint_rate, n)
    noise = rng.normal(0, 0.50, n)
    interaction = (
        (contract == "month-to-month")
        & (tenure >= 3)
        & (tenure <= 12)
        & (outages >= 2)
        & (complaints >= 2)
    )

    # Calibrate the intercept on expected probabilities so the realized global
    # churn stays close to the brief's 4% baseline in both windows.
    base = (
        0.22 * (contract == "month-to-month")
        + 0.18 * ((tenure >= 3) & (tenure <= 12))
        + 0.05 * outages
        + 0.10 * complaints
        - 0.22 * (autopay == "yes")
        + 0.06 * (plan == "basic")
        + 1.55 * interaction
        + noise
    )
    lo, hi = -7.0, -1.0
    for _ in range(50):
        mid = (lo + hi) / 2
        if float(sigmoid(mid + base).mean()) > 0.04:
            hi = mid
        else:
            lo = mid
    intercept = (lo + hi) / 2
    probability = sigmoid(intercept + base)
    churn = rng.binomial(1, probability)
    frame = pd.DataFrame(
        {
            "churn": churn.astype(bool),
            "complaints_90d": complaints.astype(int),
            "outages_90d": outages.astype(int),
            "tenure_months": tenure.astype(int),
            "contract_type": contract,
            "plan_type": plan,
            "autopay": autopay,
            "monthly_charge": monthly,
        }
    )
    return frame, {"intercept": float(intercept), "interaction_expected_rate": float(probability[interaction].mean())}


def describe_rule(sg: object) -> str:
    # pysubgroup's description is intentionally the canonical API rendering.
    return str(sg)


def run_search(frame: pd.DataFrame) -> tuple[dict[str, object], object]:
    # Keep the search space bounded and legible: these are the supplied service,
    # tenure, contract and plan fields that a presenter can defend.  Autopay and
    # charge remain in the synthetic table as context/noise, but are not allowed
    # to win merely because a wider selector universe is available.
    search_columns = [
        "churn",
        "complaints_90d",
        "outages_90d",
        "tenure_months",
        "contract_type",
        "plan_type",
    ]
    search_space = ps.create_selectors(frame[search_columns], ignore=["churn"], nbins=5)
    target = ps.BinaryTarget("churn", True)
    quality = ps.StandardQF(1)
    task = ps.SubgroupDiscoveryTask(
        data=frame,
        target=target,
        search_space=search_space,
        qf=quality,
        result_set_size=20,
        depth=3,
        constraints=[ps.MinSupportConstraint(0.02)],
    )
    result = ps.BeamSearch(beam_width=50).execute(task)
    rows = result.to_dataframe()
    # Prefer a legible 2–5% niche when the search returns one; this keeps the
    # visual comparison honest about support instead of selecting the broadest
    # positive rule.  Search result rows are sorted by quality.
    baseline = float(frame["churn"].mean())
    candidates: list[tuple[float, object, int, float]] = []
    for _, row in rows.iterrows():
        subgroup = row["subgroup"]
        try:
            mask = subgroup.covers(frame)
        except AttributeError:
            continue
        count = int(mask.sum())
        rate = float(frame.loc[mask, "churn"].mean()) if count else 0.0
        if 0.02 <= count / len(frame) <= 0.05 and rate > baseline:
            candidates.append((float(row["quality"]), subgroup, count, rate))
    if candidates:
        _, subgroup, count, rate = max(candidates, key=lambda item: item[0])
        metrics = {
                "description": describe_rule(subgroup),
                "n": count,
                "support": count / len(frame),
                "rate": rate,
                "baseline": baseline,
                "lift": rate / baseline if baseline else None,
                "difference": rate - baseline,
                "quality": float(row["quality"]),
        }
        return metrics, subgroup
    # If no compact candidate exists, keep the best positive rule as a truthful
    # fallback; the displayed support remains the observed value.
    for _, row in rows.iterrows():
        subgroup = row["subgroup"]
        mask = subgroup.covers(frame)
        count = int(mask.sum())
        rate = float(frame.loc[mask, "churn"].mean()) if count else 0.0
        if count / len(frame) >= 0.02 and rate > baseline:
            return {
                "description": describe_rule(subgroup),
                "n": count,
                "support": count / len(frame),
                "rate": rate,
                "baseline": baseline,
                "lift": rate / baseline if baseline else None,
                "difference": rate - baseline,
                "quality": float(row["quality"]),
            }, subgroup
    raise RuntimeError("No stable-direction subgroup survived the 2% support constraint")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    discovery, dmeta = make_window(SEED)
    holdout, hmeta = make_window(SEED + 1)
    metrics, subgroup = run_search(discovery)
    hold_mask = subgroup.covers(holdout)
    hold_n = int(hold_mask.sum())
    hold_rate = float(holdout.loc[hold_mask, "churn"].mean()) if hold_n else 0.0
    hold_baseline = float(holdout["churn"].mean())
    metrics.update(
        {
            "holdout_n": hold_n,
            "holdout_support": hold_n / len(holdout),
            "holdout_rate": hold_rate,
            "holdout_baseline": hold_baseline,
            "holdout_lift": hold_rate / hold_baseline if hold_baseline else None,
            "holdout_difference": hold_rate - hold_baseline,
            "holdout_direction_retained": hold_rate > hold_baseline,
        }
    )
    discovery.to_csv(OUT / "discovery.csv", index=False)
    holdout.to_csv(OUT / "holdout.csv", index=False)
    summary = {
        "seed": SEED,
        "n_per_window": N,
        "columns": list(discovery.columns),
        "discovery": metrics,
        "windows": {
            "discovery": {"seed": SEED, "churn_rate": float(discovery["churn"].mean()), **dmeta},
            "holdout": {"seed": SEED + 1, "churn_rate": float(holdout["churn"].mean()), **hmeta},
        },
        "environment": {
            "python": platform.python_version(),
            "executable": sys.executable,
            "pysubgroup": version("pysubgroup"),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": version("scikit-learn"),
            "scipy": version("scipy"),
            "matplotlib": version("matplotlib"),
            "statsmodels": version("statsmodels"),
        },
        "api": {
            "target": "BinaryTarget('churn', True)",
            "quality": "StandardQF(1)",
            "search": "BeamSearch(beam_width=50)",
            "depth": 3,
            "min_support": 0.02,
        },
    }
    (OUT / "demo-result.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
