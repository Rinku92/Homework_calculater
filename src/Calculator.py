import math
from decimal import Decimal, getcontext

def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = b -a
    return c

def multiplication(a,b):
    c= a * b
    return  c

def division(a,b):
    c= b/a
    return round(c,9)

def square(a):
    c=a*a
    return c

def squareroot(a):
    getcontext().prec = 10
    c = math.sqrt(Decimal(a))
    return +Decimal(c)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        return addition(a, b)

    def sub(self, a, b):
        return subtraction(a, b)

    def mul(self, a, b):
        return multiplication(a, b)

    def div(self,a,b):
        return division(a, b)

    def squ(self, a):
        return square(a)

    def sqr(self,a):
        return squareroot(a)

