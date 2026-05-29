"""Here we will make an arithmetic solver or calculator that will accept two nos. from the user and will then print the
 sum, difference, product, quotient, remainder, floor division and power."""
ans = "YES"
while ans == "YES":
    #Accepting nos. from the user
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    #Printing the answers
    print(f"The sum of {num1} and {num2} is {num1+num2}")
    print(f"The difference of {num1} and {num2} is {num1-num2}")
    print(f"The product of {num1} and {num2} is {num1*num2}")
    print(f"The quotient of {num1} and {num2} is {num1/num2}")
    print(f"The remainder of {num1} and {num2} is {num1%num2}")
    print(f"The floor division of {num1} and {num2} is {num1//num2}")
    print(f"The power of {num1} to the power of {num2} is {num1**num2}")
    ans = input("Do you want to continue? (YES/NO): ")