from subprocess import Popen, PIPE
from os import system, environ, path
from time import sleep
from datetime import datetime
from func_deposit import get_bios_info, get_system_info, get_os_environment, get_user_account
from json import dumps
from jinja2 import Template, Environment, FileSystemLoader

#command = Popen(["dir", "sdfsfp"], stdout=PIPE, stderr=PIPE, shell=False)
# out, err = command.communicate()
# result = command.wait()
# print(out)
#
#print(err)
#print(resultado)
################################################

# DEFINE VARIABLES
# CAPTURE SYSTEM DATE AND TIME
start_time = datetime.now()
print("OUTPUT - date_time: {}".format(start_time))

# COMPUTER NAME
NOME_PC = environ['COMPUTERNAME']
print("OUTPUT - NOME_PC: {}".format(NOME_PC))

# CONSTUCT FIRST COMAND (COMMAND1)
file_path = NOME_PC + "_" + "biosInfo.txt"
command_to_send = "WMIC BIOS Get /Format:list > " + file_path
print("0UTPUT - bios_info: (command to send: {} )".format(command_to_send))

# CONSTRUCT SECOND COMMAND (COMMAND2)
file_path_2 = NOME_PC + "_" + "system_info.txt"
command_to_send_2 = "systeminfo > " + file_path_2

# CONSTRUCT THIRD COMMAND (COMMAND3)
file_path_3 = NOME_PC + "_" + "userAccounts.txt"
# wmic useraccount get  /////   wmic useraccount get /format:list
command_to_send_3 = "wmic useraccount get /format:list > " + file_path_3




# END OF DEFINE VARIABLES

# SEND COMMANDS TO SYSTEM
system(command_to_send)
system(command_to_send_2)
system(command_to_send_3)

# CALL FUNCTIONS THAT READ DATA
data_bios_info = get_bios_info(file_path)
data_system_info = get_system_info(file_path_2)
data_env_info = get_os_environment()
data_user_Accounts = get_user_account(file_path_3)

#print(dumps(data_bios_info, indent=4 , sort_keys=True))
#print("OUTPUT - file_path: {}".format(file_path))
print(dumps(data_system_info, indent=4 , sort_keys=True))
print("OUTPUT - file_path: {}".format(file_path_2))




# BUILD HTML FILE REPORT USING JINJA2 TEMPLATE
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

my_template = env.get_template("template.j2")


output = my_template.render(data_bios_info=data_bios_info, time=start_time, data_system_info=data_system_info,
                            data_env_info=data_env_info, NOME_PC=NOME_PC, data_user_Accounts=data_user_Accounts)

# WRITE HTML TAGS TO FILE
with open("relatorio.html", "w", ) as file:
    for line in output:
        file.write(line)


