"""Target ranking helpers."""
from __future__ import annotations

import pandas as pd

def ensemble_scores(frame: pd.DataFrame, rf_col: str, xgb_col: str) -> pd.DataFrame:
    out = frame.copy()
    out["final_ensemble_score"] = (out[rf_col] + out[xgb_col]) / 2.0
    out["model_disagreement"] = (out[rf_col] - out[xgb_col]).abs()
    return out

def rank_background(
    frame: pd.DataFrame,
    label_col: str = "gold_label_strict",
) -> pd.DataFrame:
    out = frame.loc[frame[label_col].eq(0)].copy()
    out = out.sort_values(
        ["final_ensemble_score", "model_disagreement"],
        ascending=[False, True],
    ).reset_index(drop=True)
    out["final_rank"] = out.index + 1
    return out
