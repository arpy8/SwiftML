@echo off
setlocal

REM Set the path to your Python executable
set PYTHON_EXE=python

REM Set the path where you want to create the virtual environment
set VENV_NAME=dababy

REM Create the virtual environment
%PYTHON_EXE% -m venv %VENV_NAME%

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate

REM Install required packages

echo Virtual environment created and activated.