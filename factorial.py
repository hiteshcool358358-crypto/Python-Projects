#This program would accept a no. from the user and then print its factorial
#Accepting the no.
num=int(input("Enter a no.= "))
#Calculating the factorial
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
#Displaying the result
print(f"The factorial of {num} is {fact}")