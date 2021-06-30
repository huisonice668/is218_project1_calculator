import math
def addition(x, y):
    return x + y

def subtraction(x, y):
    x = int(x)
    y = int(y)
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero")
    return x / y

def squaring(x):
    return x * x

def squareRoots(x):
    return math.sqrt(x)


class Calculator:

    def _init_(self):
        pass

    def add(x, y):
        return addition(x, y)

    def minus(x, y):
        return subtraction(x, y)

    def multiply(x, y):
        return multiplication(x, y)

    def divide(x, y):
        return division(x, y)

    def square(x):
        return squaring(x)

    def squareRoot(x):
        return squareRoots(x)
