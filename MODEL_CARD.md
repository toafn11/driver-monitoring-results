# Frozen research model card

Research snapshot: 2026-10-08. Demo packaging: 2026-10-21.

## Intended use

Academic investigation and stationary team demonstrations of visual driver-state cues. Outputs are not physiological diagnoses, validated road-risk estimates, or certified safety warnings. Camera and audio end-to-end validation is unfinished. The optional Windows audio backend and sustained-yawn alert added on 2026-11-18 are demo features; the yawn alert is not included in the frozen policy or reported evaluation metrics. See the README for activation, thresholds, and limitations.

The extended demo also provides missing-face warnings and operator-calibrated lowered-head geometry rules. These are unvalidated monitoring heuristics, not additional trained classes or proof of distraction. An active posture warning persists through missing observations and clears on observed recovery. Continuous warning tones indicate an active alert, not independently confirmed danger. The frozen research output is retained separately in demo logs.

## Model identities

| Model | Architecture | Seed / epoch | SHA256 |
|---|---|---|---|
| Gaze | Shared ResNet18 face/eye encoder, 9 classes | 43 / 7 | `9c6e90e7a50ad7dd5bafe2c7021b75bf4c3cc1be5ec27087b86b1568a9505717` |
| Eye/yawn | ResNet18, 2 eye and 3 yawn classes | 43 / 6 | `01eb9e1288444b74bc9957fa9d4a40d13402ffddd4e0bf11fd0887471ca0b83f` |
| Action | ResNet18, 11 classes | 43 / 8 | `bab541c67d87b904fc15cb04e5042fe389e1d976a37d0f622b26ad4c264ec3fc` |

The policy identity is recorded in [the final lock](config/final_lock.json). Its historical `status` string is preserved for exact identity; the separate final test evidence documents the subsequent evaluation. Do not alter fields in a frozen policy merely to rename the status.

## Data and training

DMD RGB data prepared separately by task. Train IDs: 1, 6, 9, 10, 14, 28, 33, 37 (28 absent in the available drowsiness part). Validation: 5, 13, 29. Test: 7, 23, 36. Image datasets contain 2,435 gaze, 29,583 eye/yawn, and 23,558 action samples. Stable-eye evaluation masks opening/closing labels, retaining valid yawn supervision. Action excludes change_gear and standstill_or_waiting; they are not recoded as safe.

ImageNet-initialized backbones; AdamW; three seeds; selection on validation macro-F1 (mean over heads for eyes/yawn). No test-threshold tuning is claimed. The release is a results/inference package, not the complete training environment or dataset. Full retraining requires the private development workflow and authorized source data.

## Inputs and missing information

RGB without mirrored inference. Face crop and eye band are letterboxed to 224 pixels; gaze uses their paired representation. Face preprocessing includes the training JPEG90 convention. Runtime missing face/eyes may suppress predictions and reset evidence. Body inference needs an appropriate wide view; visibility is operator-declared.

## Final temporal policy

Gaze-away: 1-P(front), threshold 0.9, 0.8-second window, time-weighted positive fraction 0.6. Closed eyes: threshold 0.4 with the same window/fraction. Action groups: phone 0.6, other 0.5, talk 0.9; evidence duration 1.2 seconds except talk at 3 seconds. Hysteresis margin 0.1, cooldown 1 second, bridge 0.2 seconds, maximum observation gap 0.6 seconds. Missing observations are not safe observations.

## Evidence and limitations

See [verified temporal metrics](reports/temporal_final_verified.json) and [summary table](reports/summary.csv). Event recalls are 10/10 gaze, 21/22 eye closure, 91/98 actions. False starts: 1, 7, 2; negative occupancy: 4.19%, 0.83%, 0.33%. Unknown-region starts: 25, 36, 5. Maximum action delay is 38.98 seconds after the reference onset. At least one overlapping sample counts as a hit; matching is not one-to-one.

Only three test subjects, correlated frames, unequal per-person contribution, sparse gaze negatives, repeated development on validation, and previous image-test exposure limit generalization claims. DMD camera views differ from a laptop webcam. No independent Vietnamese cohort, completed NTHU benchmark, quantization/pruning study, or validated full-system webcam FPS is included. Keep model quality, temporal-policy quality, and demo usability separate in the report.

