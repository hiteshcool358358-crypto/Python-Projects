#This program will accept a no. and find its square root nearest to 4 decimal places
#Accepting the no. from the user
num=float(input("Enter a number to find its square root= "))
sqr=round(num**0.5, 4)
print(f"The square root of {num} is {sqr}")