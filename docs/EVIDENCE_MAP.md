# Evidence map

The Vietnamese report preserves the 8 October research snapshot. Some paths in that historical text refer to the private development layout. Use the mapping below in this public results repository.

| Claim/material | File here |
|---|---|
| Gaze face-only versus face/eye validation | `reports/gaze_v3_verified_results.json` |
| Gaze image test | `reports/gaze_final_test_verified.json` |
| Stable-eye/yawn validation | `reports/drowsiness_v3_verified_results.json` |
| Stable-eye/yawn image test | `reports/drowsiness_v3_test_verified.json` |
| Action validation | `reports/distraction11_verified_results.json` |
| Action image test; historical four-eye-class development | `reports/results_6_7_verified.json` (distinct sections/tasks) |
| Dataset counts | `reports/drowsiness_face_ready.json`, `reports/distraction11_ready.json`, `reports/gaze_v3_dataset_verification.json` |
| Final checkpoint/policy identities | `config/final_lock.json` |
| Verified 21-video metrics | `reports/temporal_final_verified.json` |
| Event summary | `reports/summary.csv` |
| All reference events | `reports/all_events.csv` |
| Missed/late-event review | `reports/review_missed_or_late.csv` |
| Negative/unknown alerts | `reports/negative_and_unknown_alerts.csv` |
| Former `exports/driver_system_candidate_v3.zip` | Release model ZIP + this repo's `driver_system/` + frozen policy |

The included CSVs are analysis outputs, not a redistributable copy of DMD annotations or footage. Internal session IDs and pseudonymous participant IDs support interpretation; no participant images are included. The dataset, full training workflow, and historical exploratory outputs are not part of this inference release. Do not claim this small repo alone can reproduce the entire training process or rerun labeled DMD evaluation without the authorized source data.

`reports/temporal_final_lock.json` and `config/final_lock.json` preserve the same original lock. `config/candidate_policy.json` contains its policy for compatibility with the original runner. The supported demo verifies and loads the final lock automatically.
