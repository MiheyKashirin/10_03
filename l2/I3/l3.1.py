import math
def calculator():
    number1=float(input("Type number1:"))
    operation=input("Type + - * /:")
    number2=float(input("Type + - * /:"))
    if operation == "/":
        if number2 == 0:
            print("Error")
            return
    if operation == "+":
        result=number1+number2
    elif operation=="-":
        result=number1-number2
    elif operation=="*":
        result=number1*number2
    elif operation=="/":
        result=number1/number2
    else:
        print("Error")
        return
    print(f"{result}")
calculator()



