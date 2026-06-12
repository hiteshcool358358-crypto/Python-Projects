import numpy as np
import matplotlib.pyplot as plt

print("\nWelcome to the electricity bill calculator exclusively by JBVNL\n")

print("Billing Criteria:\nFirst 100 units = ₹5 per unit\nNext 100 units (101 to 200) = ₹7 per unit\nMore than 200 units = ₹10 per unit")

units = input("\nEnter the no. of units consumed by your household this month: ")

try:
    units = int(units)
except ValueError:
    units = False
    while units == False:
        print("\nAlphabetical or special characters were entered instead of number. Plese enter the asked info again below.")
        units = input("Enter the no. of units consumed by your household this month: ")
        try:
            units = int(units)
        except ValueError:
            units = False

if units == 0:
    bill = 0
elif units > 0 and units <= 100:
    bill = units * 5
elif units > 100 and units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(f"\nNet demand: ₹{bill:.2f}")
print(f"Your bill after applying a discount of 5%: ₹{bill - (0.05 * bill):.2f}")

bills = np.array([])
bills = np.append(bills, bill)

file_path = r"C:\Python\household_utility_analyzer\bills.txt"
with open(file_path, "a") as f:
    f.write(str(bill))
