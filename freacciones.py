import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

class FractionOperator:
    def operate(self, fraction1, fraction2):
        raise NotImplementedError

class FractionAdder(FractionOperator):
    def operate(self, fraction1, fraction2):
        if fraction1.denominator == fraction2.denominator:
            sum_num = fraction1.numerator + fraction2.numerator
            return self.reducer(sum_num, fraction2.denominator)
        else:
            mc = fraction2.denominator * fraction1.denominator
            resolution1 = (mc // fraction1.denominator) * fraction1.numerator
            resolution2 = (mc // fraction2.denominator) * fraction2.numerator
            sum_fraction = resolution1 + resolution2
            return self.reducer(sum_fraction, mc)
        
    def reducer(self, a, b):
        minim = min([a, b])
        for x in range(2, int(math.sqrt(minim) + 1)):
            while a % x == 0 and b % x == 0:
                a = a // x
                b = b // x
        return Fraction(a, b)

class FractionSubstracter(FractionOperator):
    def operate(self, fraction1, fraction2):
        if fraction1.denominator == fraction2.denominator:
            sus_num = fraction1.numerator - fraction2.numerator
            return self.reducer(sus_num, fraction2.denominator)
        else:
            mc = fraction2.denominator * fraction1.denominator
            resolution1 = (mc // fraction1.denominator) * fraction1.numerator
            resolution2 = (mc // fraction2.denominator) * fraction2.numerator
            sus_fraction = resolution1 - resolution2
            return self.reducer(sus_fraction, mc)

    def reducer(self, a, b):
        minim = min([a, b])
        for x in range(2, int(math.sqrt(abs(minim)) + 1)):
            while a % x == 0 and b % x == 0:
                a = a // x
                b = b // x
        return Fraction(a, b)

"""def fracsum(a, b, c, d):
    if b == d:
        sum_enu = a + c
        return sum_enu, b
    if b != d:
        mcm = b * d
        resolution1 = (mcm // b) * a
        resolution2 = (mcm // d) * c
        sum_fraction = resolution1 + resolution2
        return reducer(sum_fraction, mcm)

def reducer(a, b):
    minim = min([a, b])
    for x in range(2, int(math.sqrt(minim) + 1)):
        while a % x == 0 and b % x == 0:
            a = a // x
            b = b // x
    return a, b"""


A = Fraction(-1, 2)
B = Fraction(4, 4)
C = 1
D = 6   

print(FractionSubstracter().operate(A, B))
