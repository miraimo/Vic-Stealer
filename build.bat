@echo off
setlocal

cd /d "%~dp0"

set "UPX=%~dp0upx"
set "ICON="

for %%F in ("%~dp0icons\*.ico") do (
    set "ICON=%%~fF"
    goto :icon_found
)

:icon_found
if not defined ICON (
    echo [ERROR] No .ico file found in icons folder.
    pause
    exit /b 1
)

if not exist "%UPX%\upx.exe" (
    echo [ERROR] upx.exe not found in:
    echo %UPX%
    pause
    exit /b 1
)

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python was not found in PATH.
    pause
    exit /b 1
)

python -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PyInstaller is not installed.
    echo Run: python -m pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo ==============================
echo        BUILDING EXE
echo ==============================
echo.
echo Python:
python --version
echo Icon: %ICON%
echo UPX:  %UPX%
echo Main: %~dp0main.py
echo.

python -m PyInstaller ^
    --onefile ^
    --noconsole ^
    --clean ^
    --icon="%ICON%" ^
    --upx-dir="%UPX%" ^
    "%~dp0main.py" >nul 2>&1

if errorlevel 1 (
    echo.
    echo [ERROR] BUILD FAILED
    echo.
    pause
    exit /b 1
)

echo.
echo ==============================
echo       BUILD FINISHED
echo ==============================
echo.
echo EXE: %~dp0dist\main.exe
echo.

pause