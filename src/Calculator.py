def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = b -a
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        return addition(a, b)

    def sub(self, a, b):
        return subtraction(a, b)
