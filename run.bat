@echo off
title DivineConnect - Smart Temple Booking & Devotional Services
echo ========================================================
echo   DivineConnect - Smart Temple Pilgrimage Platform
echo   South Indian Sacred Temples, Darshan, Poojas & Prasad
echo ========================================================
echo.
echo Checking Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH. Please install Python 3.9+.
    pause
    exit /b
)

echo Installing / Checking dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo Starting DivineConnect Application Server...
echo Devotee Website : http://localhost:5000
echo Admin Portal    : http://localhost:5000/admin
echo Admin Login     : admin@divineconnect.com / admin123
echo Devotee Login   : devotee@divineconnect.com / devotee123
echo.
python app.py
pause
