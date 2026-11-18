@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run SETUP_WINDOWS.cmd first.
  pause
  exit /b 1
)
echo Body demo: camera must show the driver's torso and hands.
echo Look forward and press C in the preview to calibrate posture.
if "%~1"=="" (
  ".venv\Scripts\python.exe" demo.py --camera 0 --sound --yawn-alert --monitor-alerts --body-visible
) else (
  ".venv\Scripts\python.exe" demo.py --video "%~1" --sound --yawn-alert --monitor-alerts --body-visible
)
if errorlevel 1 pause
