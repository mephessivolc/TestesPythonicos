class Fracao:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __call__(self):
        return self.__str__()

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def somar(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den

        return Fracao(num, den)

    def __add__(self, other):
        return self.somar(other)

    def subtracao(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den

        return Fracao(num, den)

    def __sub__(self    , other):
        return self.subtracao(other)

    def multiplicar(self, other):
        num = self.num * other.num
        den = self.den * other.den

        return Fracao(num, den)

    def __mul__(self, other):
        return self.multiplicar(other)

    def divisao(self, other):
        tmp = other.inverter()
        num = self.num * tmp.num
        den = self.den * tmp.den

        return Fracao(num, den)

    def __div__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        
        return Fracao(num, den)

    def inverter(self):
        return Fracao(self.den, self.num)
