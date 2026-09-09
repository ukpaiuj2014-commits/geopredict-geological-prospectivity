"""Feature-building entry point.

The complete research pipeline used government geoscience datasets too large to
redistribute in this portfolio repository. This module documents the expected
feature families and provides validation hooks for a reproduced feature table.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def validate_feature_table(path: str) -> None:
    df = pd.read_csv(path)
    features = pd.read_csv(ROOT / "data/derived/final_39_features.csv")["feature"].tolist()
    missing = [c for c in features if c not in df.columns]
    if missing:
        raise ValueError(f"Missing {len(missing)} final features: {missing[:10]}")
    print(f"Validated {len(df):,} rows with all {len(features)} compact features.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("feature_csv")
    args = parser.parse_args()
    validate_feature_table(args.feature_csv)
