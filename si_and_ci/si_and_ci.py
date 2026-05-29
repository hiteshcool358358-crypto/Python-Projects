"""This program will accept the principal, rat and time period of investment and the calculate the si and amount and ci and amount
compunded yearly and half - yearly, both."""
#Accepting the principal, rate and time period from the user
p=int(input("Enter the pricipal or the sum of money= "))
r=float(input("Enter the rate percent= "))
t=float(input("Enter the time epriod of investment in years= "))
#Calculaing the si, ci and their amounts
si=(p*r*t)/100
a_si=si+p
ciYearly=p*(1+r/100)**t
ciHalfYearly=p*(1+r/100)**(t*2)
#Displaying the answers
print(f"The simple interest is {round(si, 2)} and the amount is {round(a_si,2)}")
print(f"The compound interest compounded yearly is {round(ciYearly-p, 2)} and the amount is {round(ciYearly, 2)}")
print(f"The compound interest compounded half yearly is {round(ciHalfYearly-p, 2)} and the amount is {round(ciHalfYearly, 2)}")