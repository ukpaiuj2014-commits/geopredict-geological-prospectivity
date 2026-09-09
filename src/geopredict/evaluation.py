"""Spatial evaluation helpers."""
from __future__ import annotations

import pandas as pd
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    balanced_accuracy_score,
    f1_score,
)

def classification_metrics(y_true, score, threshold: float = 0.5) -> dict:
    pred = (score >= threshold).astype(int)
    return {
        "roc_auc": roc_auc_score(y_true, score),
        "pr_auc": average_precision_score(y_true, score),
        "balanced_accuracy": balanced_accuracy_score(y_true, pred),
        "f1": f1_score(y_true, pred, zero_division=0),
    }

def summarize_folds(metrics: pd.DataFrame) -> pd.DataFrame:
    cols = ["roc_auc", "pr_auc", "balanced_accuracy", "f1"]
    return metrics[cols].agg(["mean", "std"]).T
