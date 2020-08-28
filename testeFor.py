import random


total = 10

randomList = []
for i in range(total):
    randomList.append(random.randint(1,30))

print(randomList)
for i in range(total/2):
    if (randomList[i] < randomList[total/2]) and (randomList[total-1-i] < randomList[total/2]):
        teste = True
    else:
        teste = False
    print("i - {}...total/2 - {}.. total - i {} => [{},{}] {}".format(i, total/2, total-i, randomList[i], randomList[total-1-i], teste))
