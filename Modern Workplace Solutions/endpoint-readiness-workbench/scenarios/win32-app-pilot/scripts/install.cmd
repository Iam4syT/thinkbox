@echo off
setlocal
set "TARGET=%ProgramData%\WorkplaceLab\SupportNote"
if not exist "%TARGET%" mkdir "%TARGET%"
if errorlevel 1 exit /b 1
copy /y "%~dp0note.txt" "%TARGET%\note.txt" >nul
if errorlevel 1 exit /b 1
copy /y "%~dp0version.txt" "%TARGET%\version.txt" >nul
if errorlevel 1 exit /b 1
exit /b 0
