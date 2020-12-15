import platform
import subprocess
from json import dumps, dump
import winreg
import argparse
from os import environ, system

"""
    - A bunch of functions that structure 'ipconfig /all' and 'systeminfo commands' output , so that can be easy to 
       extract data.
       
       ALL the values in the dictionary are strings. Some values will need an extra step to be Useful:
          . E.G 
          Assuming that data variable is the output result dictionary, to get access to the ipv4 ip on Ethernet interface we can: 
            data["INTERFACES_INFO"]["Ethernet adapter Ethernet"]["Physical Address"]
          
          As we can see below, this string could be useless, unless we extract the ip 
            " 192.168.1.72(Preferred)" 

    - There is also some functions that try to enumerate windows installed apps(the code is from GIT - psatler): 
          SOURCE: https://gist.github.com/psatler/010b26cd57e758278823d7027c40e2a6
            And the psatler solution is from: 
              - SOURCE: (https://stackoverflow.com/a/54825112) stackoverflow response.
              
    Some of the values: 
    System Directory": "C:\\Windows\\system32",
"""

def get_system_info():
    """
    Try to parse windows command 'systeminfo' output
    :return: <dictionary> parsed data
    """

    command = "systeminfo"
    output_dict = {}

    p = subprocess.run([command], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    #print(repr(p))

    lines =(p.split("\n")) 
    #print(lines)

    #print("=" * 80)
    #print("OUTPUT - We will run the command: {} and try to parse the output".format(command))
    #print("OUTPUT")



    for count,line in enumerate(lines):
        #print(count, repr(line))

        if "Host Name" in line:
            output_dict["HOST_NAME"] = line.split(":")[1].strip()
        if "OS Name" in line:
            output_dict["OS_NAME"] = line.split(":")[1].strip()
        if "OS Version" in line:
            output_dict["OS_Version"] = line.split(":")[1].strip()
        if "OS Configuration" in line:
            output_dict["OS_Configuration"] = line.split(":")[1].strip()
        if "OS Build Type" in line:
            output_dict["OS_Build_Type"] = line.split(":")[1].strip()
        if "Registered Owner" in line:
            output_dict["Registered_Owner"] = line.split(":")[1].strip()
        if "Registered Organization" in line:
            output_dict["Registered_Organization"] = line.split(":")[1].strip()
        if "Product ID" in line:
            output_dict["Product_ID"] = line.split(":")[1].strip()
        if "Original Install Date" in line:
            output_dict["Original_Install_Date"] = line.split(":")[1].strip() + ":" + line.split(":")[2] + ":" + line.split(":")[2]
        if "System Manufacturer" in line:
            output_dict["System_Manufacturer"] = line.split(":")[1].strip()
        if "System Model" in line:
            output_dict["System_Model"] = line.split(":")[1].strip()
        if "System Type" in line:
            output_dict["System_Type"] = line.split(":")[1].strip()
        
        if "BIOS Version" in line:
            output_dict["BIOS_Version"] = line.split(":")[1].strip()
        if "Windows Directory" in line:
            for l in line.split("  "):
                if l != "":
                    output_dict["Windows_Directory"] = l.strip()
        if "System Directory" in line:
            for l in line.split("  "):
                if l != "":
                    output_dict["System Directory"] = l.strip()
        if "Boot Device" in line:
            for l in line.split("  "):
                if l != "":
                    output_dict["Boot_Device"] = l.strip()
        if "System Locale" in line:
            output_dict["System_Locale"] = line.split(":")[1].strip()
        if "Input Locale" in line:
            output_dict["Input_Locale"] = line.split(":")[1].strip()
        if "Time Zone" in line:
            output_dict["Time_Zone"] = line.split(":")[1].strip()
        
        if "Total Physical Memory" in line:
            output_dict["Total Physical Memory"] = line.split(":")[1].strip()
        if "Available Physical Memory" in line:
            output_dict["Available_Physical_Memory"] = line.split(":")[1].strip()
        if "Virtual Memory: Max Size" in line:
            for l in line.split("  "):
                if l != "":
                    output_dict["Virtual Memory_MAX_Size"] = l.strip()
        if "Virtual Memory: In Use" in line:
            for l in line.split("  "):
                if l != "":
                    output_dict["Virtual_Memory_In_Use"] = l.strip()
    
        if "Page File Location(s)" in line:
                for l in line.split("  "):
                    if l != "":
                        output_dict["Page_File_Location(s)"] = l.strip()

        if "Domain" in line:
            output_dict["Domain"] = line.split(":")[1].strip()
        if "Logon Server" in line:
            output_dict["Logon _Server"] = line.split(":")[1].strip()

        # TODO: WE HAVE TO TEST THIS FOR HOST THAT DONT HAVE ANY HOT FIX INSTALLED:    
        if "Hotfix(s)" in line:
            """
            SOURCE: https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
            If you only want to extract only positive integers, try the following:
                >>> str = "h3110 23 cat 444.4 rabbit 11 2 dog"
                >>> [int(s) for s in str.split() if s.isdigit()]
                [23, 11, 2]

            for hotfixes number:
                run_lst = ["um","dois","tres",4,5,6,"sete","oito"]
                white = []
                white.append([run_lst[i-1] for i in range(1,8)])

            """
            output_dict["Hotfix(s)"] = line.split(":")[1].strip()
            number_of_hot_fixes = [int(s) for s in line.split(":")[1].strip().split() if s.isdigit()][0]
            output_dict["Hotfix(s)_"] = number_of_hot_fixes
            output_dict["HOTFIX_Instaled"] = []
            output_dict["HOTFIX_Instaled"].append([lines[count+x].split(":")[1].strip() for x in range(1,number_of_hot_fixes + 1)])


        
        if "Hyper-V Requirements" and "VM Monitor Mode Extensions" in line:
            output_dict["Hyper-V Requirements"] = {}
            #print("@@@@@")
            output_dict["Hyper-V Requirements"]["VM Monitor Mode Extensions"] = line.split(":")[2].strip() 

        if "Virtualization Enabled In Firmware" in line:
            output_dict["Hyper-V Requirements"]["Virtualization Enabled In Firmware"] = line.split(":")[1].strip() 

        if "Second Level Address Translation:" in line:
            output_dict["Hyper-V Requirements"]["Second Level Address Translation:"] = line.split(":")[1].strip() 

        if "Data Execution Prevention Available:" in line:
            output_dict["Hyper-V Requirements"]["Data Execution Prevention Available:"] = line.split(":")[1].strip() 

        output_dict["System_processor"] = platform.processor()

    return output_dict


def clean_string_dots(str_to_clean=None):
    """
    this function try to clean a string like "Media. . . . . . . . . . . "
    it will eliminate all the dots and blanck spaces
    :param str_to_clean: <string>
    :return: <string>
    """

    if str_to_clean is None:
        raise("Error, We need  a string")
    
    start_recording = False
    output_str = ""
    
    for i in range(len(str_to_clean) -1, -1, -1):
        if str_to_clean[i] != "." and  str_to_clean[i] != " ":
            start_recording = True
        if start_recording == True:
            output_str = output_str + str_to_clean[i]

    output_str =  output_str[::-1]
    return output_str

def get_interfaces():
    """
    Try to parse windows command 'ipconfig /all' output
    :return: <dictionary> parsed data
    """
    command = "ipconfig"
    parameter ="/all"
    output_dict = {}
    Windows_IP_Configuration = {}


    p = subprocess.run([command, parameter], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    #print(repr(p))

    lines =(p.split("\n")) 
    #print(lines)

    #print("=" * 79)
    #print("OUTPUT - We will run the command: {} {} and try to parse the output.".format(command, parameter))

    count_erres = 0 # count when first apear "\r"in line
    start_recording = False
    for count,line in enumerate(lines):
        #print(count, repr(line))
        #print(line.strip())
        #
        #    '\r'
        #    1 'Windows IP Configuration\r'
        #    2 '\r'
        #    3 '   Host Name . . . . . . . . . . . . : TACTILA\r'
        #    4 '   Primary Dns Suffix  . . . . . . . : \r'
        #    5 '   Node Type . . . . . . . . . . . . : Hybrid\r'
        #    6 '   IP Routing Enabled. . . . . . . . : No\r'
        #    7 '   WINS Proxy Enabled. . . . . . . . : No\r'
        #    8 '   DNS Suffix Search List. . . . . . : lan\r'
        #    9 '\r'
        #    ...
        #    ...
        if line == "\r" and (count_erres == 0):
            count_erres = count_erres + 1
            continue
        
        if line == "\r" and (count_erres == 1):
            count_erres = 0
            start_recording = True
            #print("--------------------------")
            #print(lines[count-1].strip().split(":")[0])
            dict_key_to_store_tempe_for_record = lines[count-1].strip().split(":")[0]
            output_dict[dict_key_to_store_tempe_for_record] = {}

        if start_recording is True and line != "\r":
            #print(len(line.strip().split(" . :")))
            try:
                #output_dict[dict_key_to_store_tempe_for_record][line.strip().split(". :")[0]] = line.strip().split(". :")[1]
                #output_dict[dict_key_to_store_tempe_for_record][lines[count].strip().split(" . :")[0]] = lines[count].strip().split(" . :")[1]
                #
                if len(line.strip().split(" . :")) == 1:
                    key = clean_string_dots(lines[count-1].strip().split(" . :")[0])
                    #output_dict[dict_key_to_store_tempe_for_record][lines[count-1].strip().split(" . :")[0]] = output_dict[dict_key_to_store_tempe_for_record][lines[count-1].strip().split(" . :")[0]] + ", " + lines[count].strip()
                    output_dict[dict_key_to_store_tempe_for_record][key] = output_dict[dict_key_to_store_tempe_for_record][key] + ", " + lines[count].strip()
                else:
                    key = clean_string_dots(lines[count].strip().split(" . :")[0])
                    output_dict[dict_key_to_store_tempe_for_record][key] = lines[count].strip().split(" . :")[1]
                    #output_dict[dict_key_to_store_tempe_for_record][lines[count].strip().split(" . :")[0]] = lines[count].strip().split(" . :")[1]
            except:
                pass


            if "Host Name" in line.strip():
                Windows_IP_Configuration["Host Name"] = line.split(":")[1].strip()
            if "Primary Dns Suffix" in line.strip():
                    Windows_IP_Configuration["Primary Dns Suffix"] = line.split(":")[1].strip()
            if "IP Routing Enabled" in line.strip():
                Windows_IP_Configuration["IP Routing Enabled"] = line.split(":")[1].strip()
            if "WINS Proxy Enabled" in line.strip():
                Windows_IP_Configuration["WINS Proxy Enabled"] = line.split(":")[1].strip()
            if "DNS Suffix Search List" in line.strip():
                Windows_IP_Configuration["DNS Suffix Search List"] = line.split(":")[1].strip()

        

        #if line == "\r" and count_erres = 2:
        #    count_erres = 0
        #    output_dict[line.strip()] = {}

    output_dict["Windows IP Configuration"] = Windows_IP_Configuration
    return output_dict


def get_os_environment():
    """
    this function gives OS environment data
    :return:<dictionary> with data from os environment
    """
    # CREATE A DICTINARY WIT DATA
    data_dict = {}
    for item in environ.items():
        print(item)
        data_dict[item[0]] = item[1]

    print(dumps(data_dict, indent=4, sort_keys=False))
    return data_dict


def foo(hive, flag):
    """
    This function can be found at : # SOURCE: https://gist.github.com/psatler/010b26cd57e758278823d7027c40e2a6
    :param hive:
    :param flag:
    :return:
    """
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list



def get_software_list():
    """

    This function can be found at : # SOURCE: https://gist.github.com/psatler/010b26cd57e758278823d7027c40e2a6
    :return:
    """
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)

    #for software in software_list:
    #    pass
    #    print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
    #print('Number of installed apps: %s' % len(software_list))

    #for software in software_list:
    #    print(dumps(software, indent =4 ,sort_keys= False))
    return software_list


def run_main():
    """
    This function parse the input parameters and runs our SCRIPTS...
    # WE will call this file like:
    python.exe get_windows_info.py -type [option]
        if option is: "system":
            - it will print the system dictionary
        if option is: "interfaces":
            - it will print the interfaces(ipconfig/all) dictionary
        if option is: "programs":
            -it will print the installed apps dictionary

    if not type parameter, it will print them all

    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", '--type', dest='type', choices=[ 'system', 'interfaces', 'programs', 'environment'],
                        help="We will try to output: system info, interface info, environment variables data or installed programs. \r If  "
                             "'type' is not set We will try to output ALL")
    # setting a variable True or False, have a look here (specifically store_true and store_false)
    parser.add_argument('-r', action='store_true' )
    args = parser.parse_args()

    WRITE_REPORT = False
    if args.r:
        WRITE_REPORT = args.r


    if args.type:
        #print("OUTPUT - WE WILL TRY TO GET '{}' information".format(args.type))
        if args.type == "system":
            sistema = get_system_info()
            print(dumps(sistema, indent=4,sort_keys=False))
            # WRITE json data on file
            if WRITE_REPORT is True:
                REPORT_FILE = "sistema_" + "report.txt"
                with open(REPORT_FILE, "w") as file:
                    dump(sistema, file)
  
        elif args.type == "interfaces":
            interfaces = get_interfaces()
            print(dumps(interfaces, indent=4,sort_keys=False))
            # WRITE json data on file
            if WRITE_REPORT is True:
                REPORT_FILE = "interfaces_" + "report.txt"
                with open(REPORT_FILE, "w") as file:
                    dump(interfaces, file)
        elif args.type == "environment":
            environ_info = get_os_environment()
            print(dumps(environ_info, indent=4, sort_keys=False))
            if WRITE_REPORT is True:
                REPORT_FILE = "system_environment_" + "report.txt"
                with open(REPORT_FILE, "w") as file:
                    dump(environ_info, file)
        elif args.type == "programs":
            software_lst =  get_software_list()
            output = {"software_list": software_lst,
                        "Number_of_instaled_apps": str(len(software_lst)) 
                        }
            print(dumps(output, indent =4 ,sort_keys= False))
            # WRITE json data on file
            if WRITE_REPORT is True:
                REPORT_FILE = "software_list_" + "report.txt"
                with open(REPORT_FILE, "w") as file:
                    dump(output, file)
    else:
        # do all
        sistema = get_system_info()
        interfaces = get_interfaces()
        environ_info = get_os_environment()
        #print(dumps(environ_info, indent=4, sort_keys=False))

        software_lst =  get_software_list()
        soft_output = {"software_list": software_lst,
                    "number_of_instaled_apps": str(len(software_lst))
                    }
        #print(dumps(soft_out, indent =4 ,sort_keys= False))
        output = {"SYSTEM_INFO": sistema,
                  "SYSTEM_ENVIRONMENT": environ_info,
                  "INTERFACES_INFO": interfaces,
                  "INSTALLED_APPS": soft_output
                  }
        #
        print(dumps(output, indent = 4 , sort_keys=False))


        # WRITE json data on file
        if WRITE_REPORT is True:
            REPORT_FILE = "report.txt"
            with open(REPORT_FILE, "w") as file:
                    dump(output, file)

if __name__ == '__main__':
    run_main()

    #
    





