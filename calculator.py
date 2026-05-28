'''This progam is going to take 2 numbers from the user and and operator answill calculate and print the answer unless the user doesn't stop
the program.'''
#Import math module for performing operations with a vast variation of operators.
import math as m
ans = "YES"
#Running the program in a loop so that that the program continues till the user say "YES" or "yes".
while ans == "YES":
    TypeOper = input("What kind of calcculation are you going to perform (Scientific / Arithematical)?")
    if TypeOper.lower() == "arithematical":
        print("The arithematial operators that are supported for now:")
        print("+ - for addition")
        print("- - for subtraction")
        print("* - for multiplication")
        print("/ - for division")
        print("^ - for exponents")
        print("sqrt - for square root")
        print("cbrt - for cube root")
        print("fact - for factorial")
    elif TypeOper.lower() == "scientific":
        print("The scientific operators that are supported for now:")
        print("sin - for sine")
        print("cos - for cosine")
        print("tan - for tangent")
        print("cosec - for cosecant")
        print("sec - for secant")
        print("cot - for cotangent")
    operator = input("Enter the operator: ")
    if operator == "+":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The answer is {num1 + num2}.")
    elif operator == "-":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The answer is {num1 - num2}.")
    elif operator == "*":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The answer is {num1 * num2}.")
    elif operator == "/":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0.0:
            print("Can't divide by zero.")
        else:
            print(f"The answer is {num1 / num2}.")
            print(f"The answer of floor division is {num1 // num2}")
    elif operator == "^":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The answer is {pow(num1, num2)}")
    elif operator.lower() == "sqrt":
        num1 = float(input("Enter the number: "))
        print(f"The answer is {m.sqrt(num1)}")
    elif operator.lower() == "cbrt":
        num1 = float(input("Enter the number: "))
        print(f"The answer is {m.cbrt(num1)}")
    elif operator.lower() == "fact":
        num1 = float(input("Enter the number: "))
        print(f"The answer is {m.factorial(int(num1))}")
    elif operator.lower() == "sin":
        num1 = float(input("Enter the angle in degrees: "))
        print(f"The sine of {num1}° is {m.sin(m.radians(num1))}")
    elif operator.lower() == "cos":
        num1 = float(input("Enter the angle in degrees: "))
        print(f"The cosine of {num1}° is {m.cos(m.radians(num1))}")
    elif operator.lower() == "tan":
        num1 = float(input("Enter the angle in degrees: "))
        print(f"The tangent of {num1}° is {m.tan(m.radians(num1))}")
    elif operator.lower() == "cosec":
        num1 = float(input("Enter the angle in degrees: "))
        try:
            print(f"The cosecant of {num1}° is {1 / m.sin(m.radians(num1))}")
        except ZeroDivisionError:
            print("Undefined value (Division by Zero).")
    elif operator.lower() == "sec":
        num1 = float(input("Enter the angle in degrees: "))
        try:
            print(f"The secant of {num1}° is {1 / m.cos(m.radians(num1))}")
        except ZeroDivisionError:
            print("Undefined value (Division by Zero).")
    elif operator.lower() == "cot":
        num1 = float(input("Enter the angle in degrees: "))
        try:
            print(f"The cotangent of {num1}° is {1 / m.tan(m.radians(num1))}")
        except ZeroDivisionError:
            print("Undefined value (Division by Zero).")
    else:
        print("Sorry. We cannot do calculation with that operator.")
    ans = input("Would you like to do more calculations? (YES/NO): ").upper()
print("Thank you for using our calculator,\nWe are still working on logarithms, exponents, number theoretic functions and many more.\nUpdate coming soon.\nStay tuned!")