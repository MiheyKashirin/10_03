import math
number1 = float(input("Type number1: "))
operation = input("Type + - * /: ")
number2 = float(input("Type number2: "))
if operation == "/":
    if number2 == 0:
        print("Error: Division by zero!")
        exit()
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    print("Error: Invalid operation!")
    exit()
print(f"Result: {result}")





