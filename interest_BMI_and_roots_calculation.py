"""This program will accept a choice from the user depending on which it will perform operations to calculate and print the 
interest, body mass index or square and cube roots."""
#Accepting the choice from the user
print("Enter a choice:") 
print("1. Interest")
print("2. BMI")
print("3. Square and cube roots")
choice=int(input("Enter your choice= "))
#Evaluating choices
if choice==1:
    #Acceping the values and calculating the interests
    p=int(input("Enter the princial or sum= "))
    r=float(input("Enter the rate of interest= "))
    t=float(input("Enter the time period of investment= "))
    si=(p*r*t)/100
    amtSi=si+p
    AmtYearly=p*(1+r/100)**t
    AmtHalfYearly=p*(1+r/200)**(t*2)
    print(f"The simple interest on ₹{p} at {r}% p.a for {t} is ₹{round(si, 2)} and the amount gained is ₹{round(amtSi, 2)}")
    print(f"The compound interest on ₹{p} at {r}% p.a for {t} compounded yearly is ₹{round(AmtYearly-p, 2)} and the amount gained is ₹{round(AmtYearly, 2)}")
    print(f"The compound interest on ₹{p} at {r}% p.a for {t} compounded half yearly is ₹{round(AmtHalfYearly-p, 2)} and the amount gained is ₹{round(AmtHalfYearly, 2)}")
elif choice==2:
    #Accepting the weight in kgs and height in metres and calculating and then displaying the BMI
    weight=float(input("Enter your weight in kgs= "))
    height=float(input("Enter your height in metres= "))
    print(f"Your BMI is {round(weight/(height**2), 2)}")
elif choice==3:
    #Accepting the number whose square root and cube root has to be displayed and then calculating it and displaying it on the screen rounded to 4 places
    num=float(input("Enter the no. whose square root and cube root have to be found= "))
    print(f"The square root and cube root of {num} are {round(num**0.5, 4)} and {round(num**(1/3),4)} respectively.")
else:
    #Displaying a relevating message to tell the user to enter the correct choise if any one other unsupported choice is entered
    print("Please enter a valid choice.")