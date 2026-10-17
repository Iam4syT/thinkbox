@echo off
setlocal
set "TARGET=%ProgramData%\WorkplaceLab\SupportNote"
if exist "%TARGET%\note.txt" del /q "%TARGET%\note.txt"
if exist "%TARGET%\note.txt" exit /b 1
if exist "%TARGET%\version.txt" del /q "%TARGET%\version.txt"
if exist "%TARGET%\version.txt" exit /b 1
if exist "%TARGET%" rmdir "%TARGET%" 2>nul
exit /b 0
