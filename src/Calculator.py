import math

class Calculator:
    result = 0
    def _init_(self):
        pass

    def add(self, x, y):
        x = int(x)
        y = int(y)
        result = x + y
        return result

    def minus(self, x, y):
        result = x - y
        return result

    def multiply(self, x, y):
        result = x * y
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Can not divide by zero")
        result = x / y
        return result

    def square(self, x):
        result = x * x
        return result

    def squareRoot(self, x):
        result = math.sqrt(x)
        return result