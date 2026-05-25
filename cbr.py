#This program will accept a no. and find its cube root nearest to 4 decimal places
#Accepting the no. from the user
num=float(input("Enter a number to find its cube root= "))
cbr=round(num**(1/3), 4)
print(f"The cube root of {num} is {cbr}")