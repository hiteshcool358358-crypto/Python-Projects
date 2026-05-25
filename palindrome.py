#This program will check that whether the no. entered by the user is a palindrome or not
#Accepting a number
num=int(input("Enter a number to be checked= "))
#Creating a copy of the variable 'num' because its value will be changed if used further and then comparison or checking will not be possible
NumCopy=num
#Reversing the no.
RevNum=0
while NumCopy>0:
    digit=NumCopy%10
    RevNum=(RevNum*10)+digit
    NumCopy//=10
#Checking
if RevNum==num:
    print(f"{num} is a palindrome no.")
else:
    print(f"{num} is not a palindrome no.")