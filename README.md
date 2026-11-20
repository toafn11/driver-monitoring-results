# Driver Monitoring Results and Team Demo

Final research models, a local webcam/video demonstration, verified DMD results, and report-writing materials for project **THS2026-77**.

**Purpose:** let team members clone one small repository, download the frozen model bundle, and demonstrate the system without accessing the private development repository or downloading the training dataset.

**Status:** the research snapshot was evaluated through **8 October 2026**. The visual webcam/video demo was added on **21 October 2026**. Webcam accuracy, end-to-end latency, and simultaneous three-branch performance in a deployment camera view have **not** been validated. This is a research demonstration, not a driving safety product.

## What the system does

| Component | Input | Output |
|---|---|---|
| Gaze | Face and eye crops, shared ResNet18 encoder | Nine gaze regions |
| Eye state and yawning | Face crop, ResNet18 with two heads | Closed/open eyes and three yawning classes |
| Driver actions | Full image showing torso and hands, ResNet18 | Eleven actions |
| Frozen hybrid policy v3 | Predictions and timestamps | Gaze-away, prolonged-eye-closure, and action alerts |

The system runs three separate checkpoints with a shared application-level decision pipeline. It is not one jointly trained neural network. Yawning is shown as supporting information, not an independent physiological drowsiness diagnosis.

## Quick start: Windows

Install Python **3.12** (64-bit). A CPU is sufficient to try the demo; actual speed depends on the computer. Close applications that are already using the camera.

```powershell
git clone https://github.com/toafn11/driver-monitoring-results.git
cd driver-monitoring-results
py -3.12 -m venv .venv
# If the next command says that python.exe is not recognized, rerun the
# venv command above from this repository directory.
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/download_models.py
.\.venv\Scripts\python.exe verify_setup.py --smoke
```

Alternatively, after installing Python 3.12, double-click **SETUP_WINDOWS.cmd**. It performs the steps above and stops on errors. Internet is needed for packages and the approximately 128 MB model archive. Inference is local after setup.

The downloader checks the archive and every file against the committed SHA256 values before installation. The `--smoke` check loads the models and processes synthetic blank images. It does not open a camera or measure model accuracy.

### Webcam demonstration

```powershell
.\.venv\Scripts\python.exe demo.py --camera 0
```

Or double-click **DEMO_WEBCAM.cmd**. Try `--camera 1` if index 0 is not the intended camera. Press **Q**, **Esc**, or close the window to stop.

By default, only face-related predictions are enabled. Keep one face clearly visible, use adequate lighting, and avoid a mirrored input feed. The program does not horizontally flip model inputs. Left/right labels follow the training convention and may not match a mirrored preview from another application.

To demonstrate driver-action recognition, position the camera so that the **upper body, hands, and relevant objects** are visible, then explicitly enable it:

```powershell
.\.venv\Scripts\python.exe demo.py --camera 0 --body-visible
```

`--body-visible` is your declaration, not an automatic visibility detector. A tight laptop face view is not sufficient to assess phone use or reaching behavior reliably. The original DMD branches used different camera views; using one webcam for all branches is exploratory.

Use seated, stationary demonstrations. Do not perform distracting actions while driving. The window displays predictions, active alerts, missing observations, and processing time. Footage is neither uploaded nor recorded.

### Audible demo and sustained-yawn alert (Windows)

After setup, double-click `DEMO_ALERTS.cmd` for webcam 0, or drag a local video onto that file. Equivalent commands:

```powershell
.\.venv\Scripts\python.exe demo.py --camera 0 --sound --yawn-alert --monitor-alerts
.\.venv\Scripts\python.exe demo.py --video "C:\videos\demo.mp4" --sound --yawn-alert --monitor-alerts
```

Add `--body-visible` only when the torso and hands are visible, or use `DEMO_BODY_ALERTS.cmd` (also accepts a dragged video). The action model runs on the full frame independently of face detection; a face-only view cannot support reliable body-action recognition. Check Windows volume and mute settings. A two-beep pattern loops continuously while any alert is active, including between inference calls. It stops when all alerts clear or the demo exits. Sound-enabled video playback is paced to its source timeline; slow inference can still make playback slower. This option generates warning tones, not the video's original audio track. The built-in sound backend currently supports Windows only.

By default, yawning is a prediction only. With `--yawn-alert`, the sum of `yawning_with_hand` and `yawning_without_hand` probabilities must remain at least 0.70 for 1.0 second to activate `ALERT: yawning`. Missing observations, negative predictions, or observation gaps exceeding 0.6 seconds reset the timer. A brief mouth opening may therefore remain a prediction without triggering an alert.

This optional rule is a **demo extension, not a validated drowsiness diagnosis**. It does not retrain or modify the models or frozen research policy. The published metrics do not evaluate this extension. Logs preserve the original policy output as `research_alerts` and record the extension configuration separately. Omit `--yawn-alert` to run the original alert rules; omit `--sound` for silent operation.

### Missing face and lowered-head monitoring

Posture calibration is **session-only**, never loaded from a previous run. Click the video preview (not the CMD terminal) before pressing keys. `C` starts calibration or replaces a locked reference; `R` clears it and disables the lowered-head comparison until calibration completes again. The display shows `NOT SET`, `COLLECTING` with progress/reason, or green `LOCKED` with a reference number. A terminal confirmation is printed on each successful lock. Recalibration clears stale lowered-head warnings but leaves independent visibility and model alerts intact. Optional summary logs contain the reference for auditing only; they are not settings files. Holding C while collecting no longer resets the collection timer.

`DEMO_ALERTS.cmd` and `DEMO_BODY_ALERTS.cmd` enable `--monitor-alerts`. This adds two separate demo warnings:

- `driver_not_visible`: face detection is unavailable continuously for 2 seconds. This is an observation warning, **not proof of distraction**. Occlusion, leaving the frame, low light, or a lowered head can all cause it. It works before posture calibration.
- `head_lowered`: relative face geometry indicates a sustained change from the operator's forward-looking posture for 1 second. Look forward, press **C** in the preview, and hold still for at least 2 seconds until `Posture: LOCKED`. Recalibrate after moving the camera or changing seat position. For a video/headless run that starts with a known forward-looking pose, use `--calibrate-at-start`; do not calibrate on an already lowered head.

Both warnings require 0.5 seconds of observed recovery to clear. Losing face landmarks does not clear an already active lowered-head warning. Observation gaps over 1 second reset pending activation/recovery timers rather than counting unobserved time. Without calibration, lowered-head detection remains unknown; missing-face warnings still operate.

The posture rule uses image-space nose/eye/chin geometry and downward movement, not a trained nod detector or measured pitch angle. Relative thresholds are 0.12 for nose position along the eye-to-chin axis or 0.12 image height for eye-center descent; face scale must remain between 0.7 and 1.4 times the baseline. Camera movement, facial movement, off-angle views, and calibration errors can cause misses or false alerts. These engineering defaults have not been calibrated on labeled validation clips. No new accuracy claim is made. Disable both `--monitor-alerts` and `--yawn-alert` to reproduce the original frozen alert rules.

Suggested acceptance sequence while stationary: forward gaze, brief head movement, sustained head lowering, hide the face for over 2 seconds, then return to the calibrated forward pose. Check that warning text remains visible and beeps continue during a sustained alert, and that both stop after recovery. Document failures as well as successes.

### Video demonstration

Use a local video you are authorized to use. No sample DMD footage is distributed.

```powershell
.\.venv\Scripts\python.exe demo.py --video "C:\videos\demo.mp4" --body-visible
```

For an offline run with optional local prediction logs:

```powershell
.\.venv\Scripts\python.exe demo.py --video "C:\videos\demo.mp4" --body-visible --headless --log-dir outputs\video01
```

Use a new log directory for each run. Logs contain predictions, timestamps, and a run summary, not video frames. Video processing is not paced to real-time playback. `--max-samples 100` runs a limited smoke check; do not describe it as a full-video evaluation.

### Linux/macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/download_models.py
python verify_setup.py --smoke
python demo.py --camera 0
```

The release was locally checked on Windows/Python 3.12 CPU. Linux, macOS, CUDA, and actual camera devices still require platform-specific validation. CUDA users should install the appropriate PyTorch build and then pass `--device cuda`; CPU is the default.

### Windows troubleshooting

If PowerShell reports that `.\.venv\Scripts\python.exe` is not recognized, the virtual environment has not been created at the current location. Run these commands from the cloned repository directory:

```powershell
py -3.12 -m venv .venv
Test-Path .\.venv\Scripts\python.exe
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

The `Test-Path` command must return `True`. If `py -3.12` is not recognized, install the 64-bit Python 3.12 launcher, reopen PowerShell, and run the commands again. Do not run the `.venv` command from the parent directory or another PowerShell working directory.

## Reading the demo correctly

- **ALERT** means the frozen temporal rule is active, not that real-world danger has been confirmed.
- **No alert** does not guarantee attention or safety.
- **Unknown** means a branch is missing usable observations. A disabled action branch is unknown, not safe.
- Scores are softmax outputs, not calibrated probabilities of danger.
- `Inference: ... ms` excludes capture, display, and some I/O. It is not end-to-end latency or verified webcam FPS.
- Slow processing or missing observations can reset temporal evidence. The gap limit is 0.6 seconds. Do not change locked thresholds just to obtain a favorable demo.
- Gaze includes mirror regions. Looking at a mirror can be appropriate driving behavior; road context is not modeled.

## Verified research results

### Prepared image test set

| Task | Samples | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| Gaze (9 classes) | 607 | 84.84% | 84.22% |
| Stable eye state (2 classes) | 5,355 | 98.67% | 96.95% |
| Yawning (3 classes) | 7,629 | 92.78% | 84.28% |
| Driver actions (11 classes) | 6,321 | 83.31% | 77.96% |

### Additional temporal evaluation: 21 videos, subjects 7, 23, 36

| Branch | Detected/reference events | Recall | False starts on labeled negative intervals | Maximum delay after reference onset |
|---|---:|---:|---:|---:|
| Gaze-away | 10/10 | 100.00% | 1 | 5.98 s |
| Prolonged eye closure | 21/22 | 95.45% | 7 | 0.00 s |
| Driver actions | 91/98 | 92.86% | 2 | 38.98 s |

Reference events start after 1.5 seconds of annotated closed eyes or 2 seconds of annotated gaze-away/action. A hit requires temporal overlap, not one-to-one event matching. Zero reference-relative delay is not instantaneous detection from behavior onset. These subjects had already been used for image-level testing; the temporal experiment is not a completely unseen population. Read [the model card](MODEL_CARD.md) and [detailed result discussion](docs/RESULTS_DISCUSSION_VI.md) before citing these values.

The main remaining weakness is not only recall: some alerts are late, and gaze has just 10 reference events and about 57 seconds of labeled negative data. Do not combine the branches into a single overall accuracy figure.

## Report collaboration

- [Shared report drafting Google Doc](https://docs.google.com/document/d/1tW-ffErO15po9oFcCIh8oE8n61blfpx9Y3yu3EEIfos/edit?usp=sharing). Access is controlled by the document owner; repository publication does not change Google Docs permissions.
- [Detailed project breakdown and research journey (Vietnamese)](docs/PROJECT_BREAKDOWN_AND_REPORT_GUIDE_VI.md).
- [Current full report (Vietnamese)](docs/FINAL_REPORT_VI.md) and [plain text](docs/FINAL_REPORT_VI.txt).
- [Evidence map](docs/EVIDENCE_MAP.md).
- [Team demo checklist](docs/TEAM_DEMO_CHECKLIST.md).

The current report is a research draft based on the 8 October snapshot. Its statements that the final webcam experiment is unfinished remain valid: adding a demo application is not a completed webcam evaluation.

## Repository layout

```text
demo.py                   Visible webcam/video demo, always uses the frozen v3 policy
verify_setup.py           Asset and policy checks; optional synthetic smoke run
driver_system/            Selected inference and temporal-policy implementation
config/                   Final lock, policy copy, release asset checksums
models/                   Downloaded locally; binaries are release assets, not Git history
scripts/download_models.py
reports/                  Selected verified metrics and event-analysis tables
docs/                     Research report, journey, evidence map, testing instructions
tests/                    Temporal-policy and release-integrity tests
```

The historical bundle manifest retains its original v1 metadata for identity checks. The supported `demo.py` entry point explicitly loads `config/final_lock.json`, so it runs **hybrid policy v3**. Do not call a legacy runner without supplying the final policy and then compare its output to the reported v3 results.

## Troubleshooting

| Symptom | Action |
|---|---|
| Missing models | Run `python scripts/download_models.py`; confirm all five assets exist in `models/`. |
| Download unavailable | Download the ZIP from [Releases](https://github.com/toafn11/driver-monitoring-results/releases/tag/v1.0.0), then use `python scripts/download_models.py --archive PATH_TO_ZIP`. |
| Checksum mismatch | Do not bypass verification. Re-download into an empty destination and check the release version. |
| Camera cannot open | Close competing apps, grant OS camera access, try another index. |
| OpenCV window error | Use desktop `opencv-python`, not a headless-only OpenCV package; use `--headless` only for video. |
| CUDA unavailable | Use CPU or install a compatible CUDA PyTorch build. |
| Timestamp error | The video contains missing/non-increasing timestamps. Audit/repair a copy before running it; no silent timestamp substitution is performed. |
| No action predictions | Action inference is disabled unless `--body-visible` is set. |
| Repeated unknown/no alerts | Check framing, lighting, eye visibility, and processing gaps. This does not prove that behavior is safe. |
| Existing log folder | Choose another output directory; previous runs are not overwritten. |

## Verification and contribution workflow

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

See [release verification](docs/RELEASE_VERIFICATION.md) for what was actually checked. The tests do not establish webcam accuracy. Members can submit an issue with OS, Python version, command, expected/observed behavior, and a redacted log. Do not post faces, private footage, credentials, or dataset download links in public issues. Proposed model/policy changes need a separate version and new validation; preserve this frozen release for report reproducibility.

## Data and third-party components

No DMD video, extracted face images, private dataset links, or training caches are included. Obtain research data from [Vicomtech](https://dmd.vicomtech.org/) under its terms. The public release contains the team's selected trained checkpoints and the referenced pretrained landmarker asset; this is not a grant of unrestricted rights to the source dataset or third-party components. See [third-party notices and usage scope](THIRD_PARTY_NOTICES.md).
