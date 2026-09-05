@echo off
setlocal
set /p interface="interface: "
echo 1 - Auto, 2 - Manually
set /p choice="Your choice: "
if "%choice%"=="1" goto auto
if "%choice%"=="2" goto manually
:auto
netsh interface ip set address name="%interface%" source=dhcp
netsh interface ip set dns name="%interface%" source=dhcp
goto end
:manually
set /p ip="ip: "
set /p mask="mask: "
set /p gateway="gateway: "
set /p dns="dns: "
netsh interface ip set address name="%interface%" static %ip% %mask% %gateway% 1
netsh interface ip set dns name="%interface%" static %dns% primary
goto end
:end
echo Done!
pause