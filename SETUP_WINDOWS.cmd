@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" py -3.12 -m venv .venv
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m pip install torch --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto fail
".venv\Scripts\python.exe" scripts\download_models.py
if errorlevel 1 goto fail
".venv\Scripts\python.exe" verify_setup.py --smoke
if errorlevel 1 goto fail
echo Setup completed. Run DEMO_WEBCAM.cmd to start the local preview.
pause
exit /b 0
:fail
echo Setup failed. Read the error above and the README troubleshooting section.
pause
exit /b 1

