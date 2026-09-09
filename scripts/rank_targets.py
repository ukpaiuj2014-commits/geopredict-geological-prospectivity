"""Rank background cells from compact-model OOF predictions."""
import pandas as pd
from geopredict.targeting import ensemble_scores, rank_background

def main(prediction_csv: str, output_csv: str) -> None:
    df = pd.read_csv(prediction_csv)
    df = ensemble_scores(df, "Random Forest", "XGBoost")
    ranked = rank_background(df)
    ranked.to_csv(output_csv, index=False)
    print(ranked.head(20).to_string(index=False))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("prediction_csv")
    parser.add_argument("output_csv")
    args = parser.parse_args()
    main(args.prediction_csv, args.output_csv)
