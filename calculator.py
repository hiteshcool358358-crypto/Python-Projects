'''This progam is going to take 2 numbers from the user and and operator answill calculate and print the answer unless the user doesn't stop
the program.'''
#Import math module for performing operations with a vast variation of operators.
import math
ans = "YES"
#Running the program in a loop so that that the program continues till the user say "YES" or "yes".
while ans == "YES":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    #Telling the user about the operators with which operations can be performed for now.
    print("Operators that are compatible for now:")
    print("+ - for addition")
    print("- - for subtraction")
    print("* - for multiplication")
    print("/ - for division")
    print("^ - for exponents")
    operator = input("Enter the operator: ")
    if operator == "+":
        print(f"The answer is {num1 + num2}.")
    elif operator == "-":
        print(f"The answer is {num1 - num2}.")
    elif operator == "*":
        print(f"The answer is {num1 * num2}.")
    elif operator == "/":
        if num2 == 0.0:
            print("Can't divide by zero.")
        else:
            print(f"The answer is {num1 / num2}.")
    elif operator == "^":
        print(f"The answer is {pow(num1, num2)}")
    else:
        print("Sorry. We cannot do calculation with that operator.")
    ans = input("Would you like to do more calculations? (YES/NO): ").upper()