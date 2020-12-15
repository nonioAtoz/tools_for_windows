from json import dumps
from os import environ


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

def get_bios_info(file_to_open):
    # OPEN THE FILE WHERE THE DATA IS
    with open(file_to_open, "r", encoding="utf-16") as file:
        linhas = file.readlines()
    print("OUTPUT - linhas: {}".format(linhas))
    # elminar os \n
    lista = []
    dictio = {}
    for line in linhas:
        if line != "\n":
            lista.append(line)

    nova_lista = []
    for linha in lista:
        eliminar_enes = linha.split("\n")
        nova_lista.append(eliminar_enes)


    final_list = []
    for lista in nova_lista:
        for linha in lista:
            if linha != "":
                final_list.append(linha)
    #print(lista)
    #print(nova_lista)
    print("OUTPUT: final_list: {}".format(final_list))

    # AT THIS POINT WE HAVE A NICE LIST (final_list) READY FOR OUR NEEDS!
    # LETS SEARCH FOR SPeCIFIC SUBSTRINGS IN strings list, and store the result in a dictionary (dictio)
    for linha in final_list:
        if "BiosCharacteristics" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "BIOSVersion" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "Description" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "Manufacturer" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "Name" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "SerialNumber" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "SMBIOSMajorVersion" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "Version" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
        if "ReleaseDate" in linha:
            para_guardar = linha.split("=")
            dictio[para_guardar[0]] = para_guardar[1]
    return dictio


def get_system_info(file_to_open):

    print("=" * 79)
    print("OUTPUT - START FUCNTION : get_system_info")
    print("=" * 79)
    # OPEN THE FILE WHERE THE DATA IS

    with open(file_to_open, "r") as file:
        linhas = file.readlines()
    print("OUTPUT - linhas: {}".format(linhas))
    # elminar os \n
    lista = []
    dictio = {}
    for line in linhas:
        if line != "\n":
            lista.append(line)
    print("OUTPUT - lista: {}".format(lista))

    # ELIMINAR ENES
    nova_lista = []
    for linha in lista:
        eliminar_enes = linha.split("\n")
        nova_lista.append(eliminar_enes)
    print("OUTPUT - nova_lista: {}".format(nova_lista))

    for line in nova_lista:
        print(repr(line))

    intermedium_list = []
    for lista in nova_lista:
        for linha in lista:
            if linha != "":
                intermedium_list.append(linha)
    print("OUTPUT - intermedium_list: {}".format(intermedium_list))
    intermedium_list_2 = []


    #for line in intermedium_list:
    #    new_line = line.split(":")
    #    intermedium_list_2.append(new_line)
    #print("OUTUT - intermedium_list_2: {}".format(intermedium_list_2))
    #print("=" * 79)
    #for line in intermedium_list_2:
    #    print(line)
    #print("=" * 79)


    #final_list = []
    #for line in intermedium_list_2:
    #    new_subline_list = []
    #    for sub_line in line:
    #        new_subline= sub_line.lstrip()
    #        new_subline_list.append(new_subline)
    #    final_list.append(new_subline_list)


    # OUR FINAL _LIST IS READY TO WORK WITH
    #print(final_list)
    #print("OUTUT - final_list: {}".format(final_list))
    #for line in final_list:
    #    print(line)
    # CREATE A EMPTY DICTION TO STORE VALUES and later send to output



    #data_dictionary= {}
    #for line in final_list:
    #    if "Host Name" in line[0]:
    #        data_dictionary[line[0]] = line[1]

    #print(dumps(data_dictionary, indent=4, sort_keys= False))

    for line in intermedium_list:
        print(line)
    data_dictionary = {}
    for line in intermedium_list:
        if "Host Name" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "OS Version" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "OS Manufacturer" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "OS Configuration" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "OS Build Type" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Registered Owner" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Registered Organization" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Product ID" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Original Install Date" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Boot Time" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Manufacturer" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Model" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Type" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "BIOS Version" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Windows Directory" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Directory" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Boot Device" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "System Locale" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Input Locale" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Time Zone" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Total Physical Memory" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Available Physical Memory" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Page File Location(s" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Domain" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Logon Server" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
        if "Hyper-V Requirements" in line:
            breaked_line = line.split(":")
            breaked_line[1] = breaked_line[1].lstrip()
            data_dictionary[breaked_line[0]] = breaked_line[1]
    #print(dumps(data_dictionary, indent=4, sort_keys= False))
    return data_dictionary
##get_system_info("DESKTOP-54QJNHS_system_info.txt")


def get_user_account(file_to_open):
    """
    this function gives OS environment data
    :return:<dictionary> with data from os environment
    """

    with open(file_to_open, "r", encoding="utf-16") as file:
        linhas = file.readlines()
    print("OUTPUT - linhas: {}".format(linhas))

    # definicao de variaveis
    temp_list = []
    data_dict = {}
    temp_dict = {}
    i = 0
    contador_de_duas_posicoes = 0
    contador_tempo_de_gravacao = 18
    gravacao = False
    contador_de_contas = 1
    while i < (len(linhas)):
        print("#" *79)
        print("OUTPUT - inicio de CICLO")
        print("OUTPUT: conteudo da linha: {}".format(linhas[i]))
        print("OUTPUT - tamanho da lista: {}".format(len(linhas)))
        print("OUTPUT - i: {}".format(i))

        # comeca a gravar:
        # 1 linha nao conta
        # grava + 16
        # nao grava + 2  LINHA 17 e 18
        # grava + 16     LINHA 19
        # nao grava + 2  LINHA 35 e 36
        # grava + +16    LINHA 37
        # nao grava               LINHA 52 e 54

        # Comecar a gravar na primeira linha
        if i == 2:

            contador_tempo_de_gravacao = 1
            # colocar em modo gravacao
            gravacao = True
            print("fisrt if: contador_tempo_de_gravacao take value {}".format(contador_tempo_de_gravacao))
            print("fisrt if: gravacao take value {}".format(gravacao))
            print("END OF FISRT IIF")
        if contador_tempo_de_gravacao < 17 and gravacao is True:

             print("Second if: i take value \t{}".format(i))
             print("Second if: contador_tempo_de_gravacao take value \t  {}".format(contador_tempo_de_gravacao))
             print("Second if: gravacao take value \t {}".format(gravacao))
             print("grava aqui")
             print(linhas[i])
             print("=" * 79)
             # FAZ COISAS
             # tratar a linha 1. eliminar o barra ene e retirar o =
             # "Caption=DESKTOP-54QJNHS\\WDAGUtilityAccount\n",
             temp_line = linhas[i].split("\n")
             # EXEMPLO DE temp_line[0] ="Name=Administrador",
             nova_line = temp_line[0].split("=")
             temp_dict[nova_line[0]] = nova_line[1]
             #temp_list.append(duas srings)
             contador_tempo_de_gravacao = contador_tempo_de_gravacao +1
             if contador_tempo_de_gravacao == 16:
                 data_dict["Conta" +str(contador_de_contas)] = temp_dict
                 contador_de_contas = contador_de_contas + 1
        else:
            # reset ao contador tempo gravacoa
            print("# ---------------reset ao contador tempo gravacoa--------------------------------------")

            temp_dict = {}
            contador_tempo_de_gravacao = 1
            gravacao = False
            contador_de_duas_posicoes = contador_de_duas_posicoes + 1
            if contador_de_duas_posicoes == 2:
                gravacao = True
                contador_de_duas_posicoes = 0

        i = i + 1

    print("break")
    print(dumps(data_dict, indent=4,sort_keys=False))

    return data_dict