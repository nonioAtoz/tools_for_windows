# get_windows_info.py

---
### Description : A bunch  of scripts that try to extract/parse some windows commands.
- the script/tool will print out a dictionary or generate a json file with structured data.
    ````



    data_output = {"SYSTEM_INFO": sistema,
                  "SYSTEM_ENVIRONMENT": environ_info,
                  "INTERFACES_INFO": interfaces,
                  "INSTALLED_APPS": soft_output
                  }
    ````
    1. SYSTEM_INFO - is a structured dict with the output of windows command 'systeminfo'
    2. SYSTEM_ENVIRONMENT - Windows environment variables
    3. INTERFACES_INFO - a structured dictionary with the output of windows command 'ipconfig /all'
    3. INSTALLED_APPS - a structured dict with installed apps (THIS CODE IS FROM GIT -  psatler solutionS https://gist.github.com/psatler/010b26cd57e758278823d7027c40e2a6)