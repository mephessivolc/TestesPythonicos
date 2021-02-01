"""
    Toma todos os nomes dos arquitos .csv e insere em um dicionario
    com:
    key = primeira letra maiuscula;
    value = (nome do arquivo, nome do arquivo.csv)

    caso exista um key ja cadastrado, ira criar uma nova key diferenciando-as
    por insercao de contagem numerica
"""
import os

def take_csv():
    arr = os.listdir()
    dic_file = {}

    for file in arr:
        file_name, file_ext = os.path.splitext(file)
        first_letter = file_name[0].upper()
        cont = 1

        if file_ext == ".csv":
            while first_letter in dic_file:
                first_letter = f"{first_letter[0]}{cont}"
                cont += 1
            dic_file[first_letter] = (file_name.upper(), file)

    return dic_file
