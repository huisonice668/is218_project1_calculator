import math

class Calculator:

    def _init_(self):
        pass

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            raise ValueError("Can not divide by zero")
        return x / y

    def square(x):
        return x * x

    def squareRoot(x):
        return math.sqrt(x)