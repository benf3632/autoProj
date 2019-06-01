@ECHO off
auto.py %1 %2 %3
if %ERRORLEVEL% == "15" (
    exit /B
) else (
    cd %HOMEPATH%/Documents/Programming/%1
    code .
)
