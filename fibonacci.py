import math

def fibonacci(n):
    auxL = 1
    auxP = 0
    print(auxP)
    print(auxL)
    for i in range(n):
        aux = auxL
        auxL = auxL + auxP
        auxP = aux
        print(auxL)

    cont = math.pow((1+math.sqrt(5))/2, n)
    cont = cont - math.pow((1-math.sqrt(5))/2, n)
    cont = cont/math.sqrt(5)
    print(cont)

if __name__ == '__main__':
    n = int(input('Repeticoes: '))
    fibonacci(n)
