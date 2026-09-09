# GeoPredict AI — Technical Case Study

## Problem

Mineral exploration decisions are made from sparse, heterogeneous evidence: geochemical samples, mapped geology, structural interpretations, geophysics, and historical exploration. A machine-learning model can appear highly accurate while merely learning where previous exploration activity was concentrated.

GeoPredict AI was developed as a regional gold-prospectivity workflow that explicitly tests that failure mode.

## Study design

The project uses a regional Eastern Goldfields study window and a coarse screening grid. MINEDEX gold deposits form the strict positive label. Cells sufficiently far from strict deposits are treated as pseudo-absence background, while a buffer is excluded from training to avoid ambiguous near-deposit negatives.

Broader MINEDEX categories—prospects, occurrences, and mines—are retained for post-model plausibility checks rather than included in the strict training label.

## Geochemical preprocessing

WACHEM geochemistry contains analytical missing-value and below-detection-limit conventions. Negative non-missing concentrations were verified against batch detection limits and treated as left-censored measurements rather than physical negative values.

Repeated analytical records were aggregated to sample level. Sample media were kept separate to avoid mixing drill-core, outcrop, regolith, and unspecified populations indiscriminately.

## Exploration-bias experiment

Drill-core information improved model scores strongly. Controlled ablation showed that drill-data density/availability alone reproduced most of the improvement. That indicated historical exploration footprint leakage.

Decision: retain drill-core information for diagnostic/operational analysis, but exclude drill-density features from the final scientific prospectivity model.

## Independent geology

Mapped bedrock geology and structures were added independently of WACHEM samples. Fault/shear intensity and distances to contacts/folds provided consistent uplift under the same spatial folds.

A reduced four-feature structural augmentation captured much of the benefit of the larger geological stack.

## Magnetics

A single RTP sample produced only modest improvement. A native 1VD raster was therefore converted into neighbourhood texture features at 5, 10, and 25 km.

Local 1VD medians, variability, and gradient statistics materially improved spatially held-out discrimination. This also changed the candidate ranking, downgrading several earlier geochemistry/structure favourites.

## Gravity

A Bouguer gravity raster was processed in the same way. Gradient and local-range features improved the model again. The scalar gravity value itself was much weaker, reinforcing the importance of spatial context over single-point intensity.

## Model reduction

The gravity-aware stack contained 206 predictors.

Two reduction stages were applied:

1. Prune strongly correlated geophysical variables using absolute Spearman correlation > 0.90.
2. Retain predictors showing stable Random Forest importance across the five geographic folds.

The result was a 39-feature compact model.

## Final performance

The compact Random Forest and XGBoost models each achieved approximately 0.960 mean spatial-CV ROC-AUC. Their out-of-fold ensemble reached approximately 0.962 mean ROC-AUC and 0.904 PR-AUC.

These metrics are internal spatial-CV estimates, not external validation.

## Target interpretation

The raw highest-scoring cells include both exploration candidates and known-area validation hits.

The final workflow therefore distinguishes:

- **integrated targets** — supported across multiple evidence families;
- **high-novelty candidates** — farther from broader known gold activity and without drill-core support;
- **validation hits** — high scores near known prospects/mines that were excluded from the strict deposit label.

Grid 33 is the strongest integrated candidate. Grid 149 is the strongest high-novelty geophysics-led candidate in the current study.

## What I would do next

The scientifically strongest next step is not another feature family. It is external geographic validation: hold out an entire district or transfer the workflow to a second goldfield and measure how well the trained prospectivity logic generalizes.
