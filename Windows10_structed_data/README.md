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
    
 ## This tool requires python 3.6 installed or embedded python interpreter 3.6 (no extra modules requirement). We did't test with previous or latests versions of python
 
 ### usage example
 ````
 C:\Users\user\Desktop\Windows10_structed_data> python-3.6.6-embed-amd64\python.exe get_windows_info.py --help
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
  ````
   C:\Users\user\Desktop\Windows10_structed_data> python-3.6.6-embed-amd64\python.exe get_windows_info.py --type system
   
   {
    "System_processor": "Intel64 Family 6 Model 61 Stepping 4, GenuineIntel",
    "HOST_NAME": "DAANME",
    "OS_NAME": "Microsoft Windows 10 Education",
    "OS_Version": "American Megatrends Inc. X5@@@@.@@, 4/16/2019",
    "OS_Configuration": "Standalone Workstation",
    "OS_Build_Type": "Multiprocessor Free",
    "Registered_Owner": "owner_",
    "Registered_Organization": "",
    "Product_ID": "@@@@@-00@@@-22542-A@@@",
    "Original_Install_Date": "12/14/2020, 4:31:31",
    "System_Manufacturer": "ASUSTeK COMPUTER INC.",
    "System_Model": "X5@@@@@@@",
    "System_Type": "x64-based PC",
    "BIOS_Version": "American Megatrends Inc. X555@@@@.@@, 4/16/2019",
    "Windows_Directory": "C:\\Windows",
    "System Directory": "C:\\Windows\\system32",
    "Boot_Device": "\\Device\\HarddiskVolume1",
    "System_Locale": "en-us;English (United States)",
    "Input_Locale": "pt;Portuguese (Portugal)",
    "Time_Zone": "(UTC+00",
    "Total Physical Memory": "12,191 MB",
    "Available_Physical_Memory": "6,933 MB",
    "Virtual Memory_MAX_Size": "14,623 MB",
    "Virtual_Memory_In_Use": "5,355 MB",
    "Page_File_Location(s)": "C:\\pagefile.sys",
    "Domain": "LOCALHOST",
    "Logon _Server": "\\\\DAANME",
    "Hotfix(s)": "7 Hotfix(s) Installed.",
    "Hotfix(s)_": 7,
    "HOTFIX_Instaled": [
        [
            "KB4586876",
            "KB4562830",
            "KB4570334",
            "KB4577266",
            "KB4580325",
            "KB4593175",
            "KB4579311"
        ]
    ],
    "Hyper-V Requirements": {
        "VM Monitor Mode Extensions": "Yes",
        "Virtualization Enabled In Firmware": "Yes",
        "Second Level Address Translation:": "Yes",
        "Data Execution Prevention Available:": "Yes"
    }
}
   
  ````
 
