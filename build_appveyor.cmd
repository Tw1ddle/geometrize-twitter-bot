"%PYTHON%\\python.exe"

if %ERRORLEVEL% EQU 1 (
   echo Success
   exit /b 0
) else (
   echo Failure Reason Given is %errorlevel%
   exit /b %errorlevel%
)