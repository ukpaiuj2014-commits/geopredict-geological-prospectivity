# Model Card — GeoPredict AI

## Intended use

Regional gold-prospectivity screening and research demonstration.

## Not intended for

- economic resource estimation;
- reserve classification;
- drill-site authorization;
- environmental or regulatory decision-making;
- claims of mineral discovery without field verification.

## Inputs

The final model uses 39 predictors selected from:

- surface/unspecified-media geochemistry;
- mapped structural geology;
- RTP/1VD magnetic context;
- Bouguer gravity context.

## Outputs

A relative prospectivity ranking score for regional grid cells.

The score is not calibrated as a probability of an economic deposit.

## Validation

Five geographic spatial folds are used. The final compact model reaches approximately:

- Random Forest ROC-AUC: 0.960 ± 0.038
- XGBoost ROC-AUC: 0.960 ± 0.037
- Ensemble ROC-AUC: ~0.962
- Ensemble PR-AUC: ~0.904

## Known risks

### Spatial autocorrelation
Neighbouring geological systems are not statistically independent.

### Pseudo-absence uncertainty
Background cells may contain undiscovered or unrecorded mineralization.

### Exploration-history bias
Drilling is concentrated in historically favourable areas. This bias was explicitly diagnosed, and drill-density features were excluded from the final scientific model.

### Dataset provenance
Government geoscience datasets combine surveys of different vintages, scales, and acquisition methods.

### Internal model selection
Feature selection used the same spatial folds used for internal performance reporting. External geographic validation is still required for a stronger generalization claim.

## Interpretation

Feature importance is associative, not causal. Prospectivity rankings should be reviewed by geoscientists alongside local geology, geophysics, tenure, accessibility, and field evidence.
