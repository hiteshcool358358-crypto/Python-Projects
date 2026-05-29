#This program would print the multiplication table of a number entered by the user.
#Accepting the number whose multiplication table is to be printed
num=int(input("Enter the number whose multiplication table is to be printed= "))
#Printing the multiplication table of the number
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")