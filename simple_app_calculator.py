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

#Display Menu
def show_menu():
    print("\n==============================")
    print("      MAANGAS CALCULATOR")
    print("==============================")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("==============================")

# Main Program
def main():

    while True:

        try:
            show_menu()

            choice = input("Choose operation (1-4): ")

            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid operation selected!")

            # Input numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Object Creation
            if choice == '1':
                operation = Addition(num1, num2)
                operation_name = "Addition"

            elif choice == '2':
                operation = Subtraction(num1, num2)
                operation_name = "Subtraction"

            elif choice == '3':
                operation = Multiplication(num1, num2)
                operation_name = "Multiplication"

            elif choice == '4':
                operation = Division(num1, num2)
                operation_name = "Division"