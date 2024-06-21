@echo off
%~d0
set path1=%~dp0
cd %path1%
echo %path1%
python app.py
