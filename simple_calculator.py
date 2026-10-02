"""Simple Calculator

Perform addition, subtraction, multiplication, and division.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Choose operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(add(num1, num2))
    elif operator == "-":
        print(subtract(num1, num2))
    elif operator == "*":
        print(multiply(num1, num2))
    elif operator == "/":
        print(divide(num1, num2))
    else:
        print("Invalid operator.")
