@echo off
echo Starting Flask...
start cmd /k "cd C:\Users\AASRITHA\currency_project && venv\Scripts\activate.bat && python app.py"
timeout /t 20
echo Starting Cloudflared...
start cmd /k "cd C:\Users\AASRITHA\currency_project && cloudflared.exe tunnel --url 127.0.0.1:5000"
echo Done! Check cloudflared window for URL!
pause