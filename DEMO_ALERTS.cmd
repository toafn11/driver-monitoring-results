@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run SETUP_WINDOWS.cmd first.
  pause
  exit /b 1
)
if "%~1"=="" (
  ".venv\Scripts\python.exe" demo.py --camera 0 --sound --yawn-alert --monitor-alerts
) else (
  ".venv\Scripts\python.exe" demo.py --video "%~1" --sound --yawn-alert --monitor-alerts
)
if errorlevel 1 pause
