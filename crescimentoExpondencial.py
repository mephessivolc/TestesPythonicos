import random
# a = int(input("Entre com um numero de dias "))

ci = 1000
t = 0.01
total = []
cres = []
per = []
tmp = 0
i = 0

while tmp < 2*ci:
# while i < 12*20:
    # t = random.random()/100
    per.append(round(t, 4))
    tmp = ci*((1+t)**i)
    i += 1
    total.append(tmp)
    cres.append(tmp/ci - 1)

def sum(per):
    soma = 0
    for i in per:
        soma += i

    return soma

media = sum(per)/len(per)
print(f"Per aplicados {per}\n Media {media:.4f} \nQuantidade de dias {len(total)}\nValor final {total[-1]:.2f}\nCresc per {cres[-1]:.2f}")
