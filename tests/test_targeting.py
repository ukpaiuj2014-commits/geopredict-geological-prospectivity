import pandas as pd
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
