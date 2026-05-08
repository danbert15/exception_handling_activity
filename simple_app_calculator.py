class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calculate(self):
        pass

class Addition(Calculator):
    def calculate(self):
        return self.num1 + self.num2


class Subtraction(Calculator):
    def calculate(self):
        return self.num1 - self.num2


class Multiplication(Calculator):
    def calculate(self):
        return self.num1 * self.num2


class Division(Calculator):
    def calculate(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.num1 / self.num2