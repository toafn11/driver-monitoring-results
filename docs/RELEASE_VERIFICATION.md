# Release verification, 21 October 2026

This document describes software checks for the demo package, not new model-accuracy results.

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
