# Team demonstration checklist

## Before running

1. Clone the repository and install dependencies in a virtual environment.
2. Download models, run `verify_setup.py --smoke`, and record whether it passes.
3. Select a stationary setting, one consenting participant, and adequate lighting.
4. Decide whether the camera supports face-only or face plus torso/hands. Do not enable the action branch on an unsuitable view.
5. Keep other applications from using the camera. A webcam demonstration opens a local preview; there is no hidden capture or background service.

## Suggested short demonstration

- Start with neutral forward gaze and observe whether the face is available.
- Briefly look to different regions while remaining seated. Explain that mirror checks are not automatically unsafe.
- Show short eye closure only in a stationary demonstration; explain the time rule.
- If the view supports it, demonstrate a visible action such as holding a phone. Treat the output as a prediction, not confirmed attention.
- Temporarily move out of frame and show that unknown is distinct from safe.
- Stop with Q/Esc. Camera capture is released when the program exits.

This checklist is a functional demonstration, not a quantitative evaluation protocol. It must not be used to manufacture favorable examples or replace the recorded missed/late cases.

## Record after each run

Copy these fields into the team's notes:

```text
Date / tester:
Repository commit / release:
OS / Python / CPU / GPU:
Camera model / index / resolution if known:
Command used:
Face-only or body-enabled:
Lighting / glasses / framing:
Approximate duration:
Setup verification result:
Observed unknown intervals / unexpected alerts:
Processing-time range displayed (not end-to-end FPS):
Errors and reproduction steps:
Screenshots/footage consent and storage location:
```

Optional `--log-dir outputs/run01` saves predictions locally. Do not upload private clips or identifying logs to public GitHub issues. The output folder is ignored by Git. Use separate newly labeled videos for actual performance measurement and preserve the locked configuration.

## What to say during the presentation

“This demonstration uses three trained visual models and a frozen temporal policy. Published results are from DMD recorded videos, not from this live camera. We are demonstrating functionality and documenting deployment limitations. Webcam performance evaluation is a separate next step.”
