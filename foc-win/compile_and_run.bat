@echo off
cd /d %~dp0
echo %CD%
python setup.py py2exe
dist\foc-win.exe || notepad dist\foc-win.exe.log && del dist\foc-win.exe.log
