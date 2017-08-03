pushd bot

"%PYTHON%\\python.exe" bot.py

if %ERRORLEVEL% EQU 1 (
   echo Success
   exit /b 0
) else (
   echo Failure Reason Given is %errorlevel%
   exit /b %errorlevel%
)