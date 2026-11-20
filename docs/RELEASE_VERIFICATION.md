# Release verification, 21 October 2026

This document describes software checks for the demo package, not new model-accuracy results.

## Posture calibration correction, 20 November 2026

All 30 unit tests passed; Python compilation passed. New tests verify replacement of a locked baseline, removal of stale posture warnings without clearing independent visibility alerts, key-repeat handling, progress and missing-face feedback, explicit reset, and fresh state in a new session. A synthetic overlay was visually inspected for the green LOCKED confirmation and C/R instructions. No webcam session was used for this verification. References remain in memory only; summary logs are not reloaded as settings.

## Demo extension verification, 18 November 2026

### Follow-up: visibility, posture and looping sound

- All 28 unit tests passed. Added checks cover explicit stable calibration, relative geometry, sustained head lowering, face-loss warning/recovery, retention of a posture warning during missing observations, observation gaps, preservation of frozen outputs, and looping-audio start/stop/restart behavior.
- Actual model inference completed 100 samples from the same 10-second SUST clip with the observation extension enabled; a baseline was collected. Runtime was 23.47 seconds. This checks integration, not labeled head-lowering accuracy.
- A 3.5-second generated blank video completed 35 samples with body inference and looping sound enabled. `driver_not_visible` activated at 2.0 seconds and remained active through EOF. All 35 samples retained action predictions despite missing faces, and original research alerts remained separate. Blank-frame predictions are not meaningful action classifications.
- The Windows audio backend remained ready without errors; playback is stopped during normal cleanup. A synthetic portrait overlay was visually checked: warning and calibration instructions fit without stretching the input image.
- Actual speaker audibility and live head-lowering detection still require operator acceptance testing. Thresholds are unvalidated demo defaults. No checkpoints or frozen policy configuration were changed.

### Earlier yawn extension

- All 20 unit tests passed, including sustained-yawn activation, reset on missing observations/gaps, preservation of original research alerts, audio throttling, and backend failure handling. Python compilation and Git whitespace checks passed.
- A local 10-second SUST-DDD `d_1.mp4` clip ran through the actual models with `--headless --sound --yawn-alert`: 100 samples completed; yawning alerts started at source times 6.6 and 9.3 seconds. Audio status remained `ready-windows` without a playback exception. Total measured demo runtime was 31.31 seconds, so this CPU run does not establish real-time speed.
- The clip is a functional smoke test, not a labeled accuracy evaluation. The operator must still verify audible output, speaker volume, webcam behavior, and false alerts on their machine.
- Model weights, final-lock policy and reported research metrics are unchanged. The optional demo yawn rule is not validation-calibrated and must not be represented as part of the frozen evaluation.

## Checked locally

- Frozen Gaze, Drowsiness and Distraction checkpoint hashes matched the final research lock.
- The bundle manifest and MediaPipe asset matched the release checksum manifest.
- The policy loaded by the supported demo is exactly the policy in the final lock.
- Fourteen unit tests cover temporal rules, observation gaps, group handling, corruption rejection, policy/model identity and demo input defaults.
- Synthetic smoke inference exercises every model and missing-face handling on CPU.
- A short generated blank video exercises decoding, timestamp handling, logging, a sample limit and cleanup through the new headless demo entry point.
- A generated overlay image was inspected for layout; it is not participant footage.

## Environment

Windows, Python 3.12.14; torch 2.14.0+cpu; NumPy 2.5.3; OpenCV 5.0.0.93; MediaPipe 1.0.1; Pillow 12.3.0. This was the existing local verification environment, not a fresh installation on every supported platform. `requirements-tested.txt` records these versions; `requirements.txt` permits compatible releases.

## Not established by these checks

- Actual webcam hardware compatibility, live face-recognition accuracy, audio behavior, or user experience on every member's computer.
- A clean installation on Linux/macOS or a CUDA environment.
- Real-world safety, physiological drowsiness detection, or end-to-end real-time performance.
- Independent accuracy of model predictions on synthetic inputs. Blank-frame forward passes only test that the software loads and runs.

Team members should complete `TEAM_DEMO_CHECKLIST.md` and add a separate, dated validation record. Do not edit the historical DMD metrics to represent new webcam runs.
