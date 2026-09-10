import pandas as pd
import pytest
from geopredict.targeting import ensemble_scores, rank_background

def test_rank_background_orders_scores():
    df = pd.DataFrame({
        "grid_id": [1, 2, 3],
        "gold_label_strict": [0, 0, 1],
        "Random Forest": [0.3, 0.8, 0.9],
        "XGBoost": [0.5, 0.7, 0.9],
    })
    scored = ensemble_scores(df, "Random Forest", "XGBoost")
    ranked = rank_background(scored)
    assert ranked["grid_id"].tolist() == [2, 1]
    assert ranked["final_rank"].tolist() == [1, 2]

def test_ensemble_scores_calculates_average_and_disagreement():
    df = pd.DataFrame(
        {
            "Random Forest": [0.2, 0.8],
            "XGBoost": [0.4, 0.6],
        }
    )

    scored = ensemble_scores(df, "Random Forest", "XGBoost")

    assert scored["final_ensemble_score"].tolist() == pytest.approx([0.3, 0.7]) 
    assert scored["model_disagreement"].tolist() == pytest.approx([0.2, 0.2])
