# Data Dictionary

## Final ranking fields

| Field | Meaning |
|---|---|
| `grid_id` | Stable modelling-grid identifier |
| `longitude`, `latitude` | Grid-cell centre |
| `final_rank` | Rank among strict-background cells |
| `Random Forest` | Compact RF out-of-fold score |
| `XGBoost` | Compact XGBoost out-of-fold score |
| `final_ensemble_score` | Mean RF/XGBoost OOF score |
| `model_disagreement` | Absolute difference between RF and XGBoost scores |
| `final_tier` | Internal screening tier |
| `distance_to_nearest_deposit_km` | Distance to nearest strict deposit |
| `distance_to_nearest_broad_gold_site_km` | Distance to nearest broader MINEDEX gold site |

## Important note

`final_ensemble_score` is a ranking score. It is not a calibrated probability of a mineral discovery.
