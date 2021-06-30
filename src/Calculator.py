class Calculator:
    result = 0

    def _init_(self):
        x = 2 + 2
        self.result = x

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            print("divendend can not be 0")
        return x / y

