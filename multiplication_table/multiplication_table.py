#This program would print the multiplication table of a number entered by the user.
#Accepting the number whose multiplication table is to be printed and the no. of multiples he wants
num=int(input("Enter the number whose multiplication table is to be printed= "))
no_mult=int(input(f"Enter the number of multiples you want for the number {num}= "))
#Printing the multiplication table of the number
for i in range(1,no_mult+1):
    print(f"{num} x {i} = {num*i}")