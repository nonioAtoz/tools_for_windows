from json import dumps
def get_bios_info(file_to_open):
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
    return(dictio)


FILE_PATH = "DESKTOP-54QJNHS_biosInfo.txt"
data = get_bios_info(FILE_PATH)
print(dumps(data,indent=4))


