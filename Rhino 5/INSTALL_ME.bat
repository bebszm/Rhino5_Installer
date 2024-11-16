@echo off

:: Minimize the Command Prompt window to the taskbar
powershell.exe -WindowStyle Minimized -Command "Write-Host 'Minimizing Command Prompt...'"

:: Minimize the File Explorer window
powershell.exe -WindowStyle Hidden -Command "$shell = New-Object -ComObject Shell.Application; $shell.MinimizeAll()"

:: Check if running with admin privileges
NET SESSION >nul 2>&1
if %errorLevel% == 0 (
    echo Running with admin privileges.
) else (
    echo Running without admin privileges. Restarting with admin privileges...
    set "VBS=%temp%\runasadmin.vbs"
    echo Set UAC = CreateObject^("Shell.Application"^) > "%VBS%"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%VBS%"
    "%temp%\runasadmin.vbs"
    del "%temp%\runasadmin.vbs"
    exit /b
)

:: Run your PowerShell script here
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\temp\Rhino 5\src\install.ps1"
