"""Feature-reduction helpers."""
from __future__ import annotations

import pandas as pd

def prune_correlated(
    frame: pd.DataFrame,
    features: list[str],
    importance: dict[str, float],
    threshold: float = 0.90,
) -> tuple[list[str], list[tuple[str, str, float]]]:
    """Greedily prune correlated features, retaining the higher-priority member."""
    corr = frame[features].corr(method="spearman").abs()
    ordered = sorted(features, key=lambda c: importance.get(c, 0.0), reverse=True)
    kept: list[str] = []
    dropped: list[tuple[str, str, float]] = []

    for feature in ordered:
        conflicts = [k for k in kept if corr.loc[feature, k] > threshold]
        if conflicts:
            retained = max(conflicts, key=lambda k: corr.loc[feature, k])
            dropped.append((feature, retained, float(corr.loc[feature, retained])))
        else:
            kept.append(feature)
    return kept, dropped
