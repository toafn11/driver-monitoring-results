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

Use seated, stationary demonstrations. Do not perform distracting actions while driving. There is no audio alarm in this release. The new window displays predictions, active alerts, missing observations, and processing time. Footage is neither uploaded nor recorded.

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

