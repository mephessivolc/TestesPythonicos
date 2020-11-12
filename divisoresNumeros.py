
def list_divisores(a):
    lista_divisores = []
    for i in range(1, a+1):
        if a %i == 0:
            lista_divisores.append(i)

    return lista_divisores

a = int(input('Insira um numero inteiro '))
print(list_divisores(a))
