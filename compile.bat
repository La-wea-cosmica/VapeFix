@echo off
python -m nuitka --output-filename=vfix --onefile --windows-uac-admin --windows-icon-from-ico=a.ico main.py
PAUSE
EXIT