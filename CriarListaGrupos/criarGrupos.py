"""
    Divide uma lista de nomes de uma sala em grupo aleatórios com
    ecolha de quantidade de participantes em tempo de execução.
"""

import random
import csv

from all_files import take_csv

dic_file = take_csv()

print("Arquivo")

for key in dic_file:
    print(f"\t{key}: {dic_file[key][0]}")

choice_file = input("\nEscolha a lista ")


list_parter = []
with open(dic_file[choice_file][1], 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_file:
        if "*" not in line:
            list_parter.append(line.replace("\n", ''))

print(f"Quantidade total: {len(list_parter)}")

qtd = int(input("\nDigite qtd de componentes ")) # quantidade de alunos por grupo
list_group = []
while qtd < len(list_parter):
    tmp = []
    while len(tmp) < qtd:
        name = random.choice(list_parter)
        list_parter.remove(name)
        tmp.append(name)

    list_group.append(tmp)
else:
    list_group.append(list_parter)

count = 1
for group in list_group:
    print(count)
    for parter in sorted(group):
        print(f"\t{parter}")

    count = count + 1
