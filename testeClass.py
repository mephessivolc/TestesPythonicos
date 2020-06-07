class Ponto:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def sum(self):
        return self.a+self.b

class Area:
    def __init__(self, c=45):
        self.c = c

class Reta(Ponto, Area):

    def reta(self):
        return "reta entre {} e {}".format(self.a, self.b)

    def area(self):
        return self.a + self.b + self.c

p1 = Ponto(2, 3)
p2 = p1

p2.b = 4

r = Reta(2, 3)

print(p2.b)
print(p1.b)

print(r.reta())
print(r.area())
