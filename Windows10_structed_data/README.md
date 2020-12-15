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
    
 ## This tool nedds python 3.6 installed or embedded python interpreter 3.6 (no extra modules nedeed)
 ````
 C:\Users\user1\Desktop\Windows10_structed_data> python.exe get_windows_info.py --help
 usage: get_windows_info.py [-h] [-t {system,interfaces,programs,environment}]
                           [-r]

 optional arguments:
   -h, --help            show this help message and exit
   -t {system,interfaces,programs,environment}, --type {system,interfaces,programs,environment}
                        We will try to output: system info, interface info, or
                        installed programs. If 'type' is not set We will try
                        to output ALL
   -r
 ````
