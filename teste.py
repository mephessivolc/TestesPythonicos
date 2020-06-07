import sys

mytuple = tuple()
mylist = list()
if __name__ == "__main__":
    n = 20
    for i in range(20):
        sizeList = len(mylist)
        sizeTuple = len(mytuple)
        sizeMemoryTuple = sys.getsizeof(mytuple)
        sizeMemoryList = sys.getsizeof(mylist)
        print("Tupla: Length {} SizeMemory: {}".format(sizeTuple, sizeMemoryTuple))
        print("Lista: Length {} SizeMemory: {}".format(sizeList, sizeMemoryList))
        print("\n")
        mylist.append(None)

    print(mylist)
