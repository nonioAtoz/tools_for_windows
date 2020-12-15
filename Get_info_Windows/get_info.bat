REM DATE: 20191016
REM AUTHOR: nuno.moura@outlook.pt
REM AUTHOR: POWERED BY MICROSOFT COMMUNITY

REM some usefull info:
REM https://helpdeskgeek.com/how-to/generate-a-list-of-installed-programs-in-windows/
REM https://www.robvanderwoude.com/wmic.php
REM https://stackoverflow.com/questions/32061169/wmic-batch-file


@ECHO OFF
SETLOCAL enableextensions

md "C:\%computername%_Software_Baseline" 2>NUL

pushd "C:\%computername%_Software_Baseline"
wmic /output:"Installed_Software.txt" product get name,version
popd


WMIC BIOS Get /Format:list >> "C:\%computername%_Software_Baseline\BiosInfo.txt"
WMIC OS Get /Format:list >> "C:\%computername%_Software_Baseline\OS_info.txt"
WMIC cpu Get /Format:list >> "C:\%computername%_Software_Baseline\CPU_info.txt"
WMIC diskdrive Get /Format:list >> "C:\%computername%_Software_Baseline\DiskDrive_info.txt"
WMIC computersystem Get /Format:list >> "C:\%computername%_Software_Baseline\ComputerSystem_info.txt"
WMIC path win32_networkadapter get /format:list >> "C:\%computername%_Software_Baseline\networkAdapter_info.txt"
WMIC printer get /format:list >> "C:\%computername%_Software_Baseline\printer_info.txt"

systeminfo >> "C:\%computername%_Software_Baseline\systemInfo_info.txt"
NET ACCOUNTS >> "C:\%computername%_Software_Baseline\passwordPolicy_info.txt"
net user >> "C:\%computername%_Software_Baseline\UsersAccounts_info.txt"
ipconfig /all >> "C:\%computername%_Software_Baseline\ipconfig_all_info.txt"
