import time

t = int(input("qtos numeros? "))

inicio = time.time()
def fib():
    a, b = 0, 1

    for i in range(t):
        yield a
        a, b = b, a + b

print(list(fib()))

print("\nTempo: {}".format(time.time()-inicio))

inicio = time.time()
def listfib():
    a, b = 0, 1

    f = [a, b]
    for i in range(2, t):
        f.append(b)
        b = f[i-1] + f[i]
        
    return f

print("\n {}".format(listfib()))

print("\n2 Tempo: {}".format(time.time()-inicio))
