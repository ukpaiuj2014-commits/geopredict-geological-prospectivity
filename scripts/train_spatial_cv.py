"""Train compact GeoPredict models with geographic GroupKFold.

Expected input:
A model-ready CSV containing:
- `grid_id`
- `gold_label_strict`
- `spatial_fold`
- all columns listed in data/derived/final_39_features.csv

This script intentionally does not ship raw government source data.
"""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from geopredict.evaluation import classification_metrics

ROOT = Path(__file__).resolve().parents[1]

def main(input_csv: str) -> None:
    df = pd.read_csv(input_csv)
    features = pd.read_csv(ROOT / "data/derived/final_39_features.csv")["feature"].tolist()
    y = df["gold_label_strict"].astype(int).to_numpy()
    groups = df["spatial_fold"].astype(int).to_numpy()

    models = {
        "Random Forest": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("model", RandomForestClassifier(
                n_estimators=180,
                max_depth=6,
                min_samples_leaf=3,
                class_weight="balanced_subsample",
                random_state=42,
                n_jobs=-1,
            )),
        ]),
        "XGBoost": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("model", XGBClassifier(
                n_estimators=150,
                max_depth=3,
                learning_rate=0.04,
                subsample=0.8,
                colsample_bytree=0.7,
                reg_lambda=2,
                reg_alpha=0.2,
                objective="binary:logistic",
                eval_metric="logloss",
                random_state=42,
                n_jobs=2,
            )),
        ]),
    }

    rows = []
    for name, model in models.items():
        for fold, (train_idx, test_idx) in enumerate(
            GroupKFold(5).split(df[features], y, groups)
        ):
            model.fit(df.iloc[train_idx][features], y[train_idx])
            score = model.predict_proba(df.iloc[test_idx][features])[:, 1]
            metrics = classification_metrics(y[test_idx], score)
            rows.append({"model": name, "fold": fold, **metrics})

    print(pd.DataFrame(rows).groupby("model").agg(["mean", "std"]))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv")
    args = parser.parse_args()
    main(args.input_csv)
