lista = []

for i in range(5):
    lista.append(i)

print(lista)
aux = lista.pop(0)
del lista[0]
print(lista)

lista.append(aux)

print(lista)
