#This program will accept the weight and height of a person and calculate the BMI and display the category also
#Accepting the weight and hight in kgs and ms respectively
weight=float(input("Enter you weight in kgs= "))
height=float(input("Ener the height in ms= "))
#Calculating the bmi and printing it
bmi=round(weight/(height**2), 2)
print(f"Your BMI is {bmi}")
if bmi<18.5:
    print("You are underweight.")
elif bmi>=18.5 and bmi<25:
    print("You are normal weight.")
elif bmi>=25 and bmi<30:
    print("You are overweight.")
else:
    print("You are obese.")