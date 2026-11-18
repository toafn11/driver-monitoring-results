# Team demonstration checklist

## Before running

1. Clone the repository and install dependencies in a virtual environment.
2. Download models, run `verify_setup.py --smoke`, and record whether it passes.
3. Select a stationary setting, one consenting participant, and adequate lighting.
4. Decide whether the camera supports face-only or face plus torso/hands. Do not enable the action branch on an unsuitable view.
5. Keep other applications from using the camera. A webcam demonstration opens a local preview; there is no hidden capture or background service.

## Suggested short demonstration

- For the optional audible/yawn demo on Windows, launch `DEMO_ALERTS.cmd` or use `--sound --yawn-alert`. Check system volume. Explain that this adds an unvalidated sustained-yawn rule to the frozen policy.
- Observe the distinction between a yawn prediction and `ALERT: yawning`: the latter requires combined yawn probability at least 0.70 for 1.0 second without missing observations or gaps over 0.6 seconds. Record missed and unexpected warnings too.
- Confirm the warning tone loops while an alert is active and stops after alerts clear or the demo exits. Record whether sound was actually audible; software checks alone cannot establish this.
- Both alert launchers now enable observation monitoring: look forward, press C, and stay still until posture calibration is ready. Test sustained head lowering, face occlusion over 2 seconds, and recovery. `driver_not_visible` means attention is unknown, not that distraction was recognized. Use `DEMO_BODY_ALERTS.cmd` only with torso/hands visible to exercise the independent action model.
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
