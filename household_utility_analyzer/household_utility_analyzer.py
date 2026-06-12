import numpy as np
import matplotlib.pyplot as plt

print("\nWelcome to the electricity bill calculator exclusively by JBVNL\n")

print("Billing Criteria:\nFirst 100 units = ₹5 per unit\nNext 100 units (101 to 200) = ₹7 per unit\nMore than 200 units = ₹10 per unit")

cont = "yes"
while cont.lower() == "yes":
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

    file_path = r"C:\Python\household_utility_analyzer\bills.txt"
    with open(file_path, "a") as f:
        f.write(str(bill - (0.05 * bill)) + "\n")
    print("\nBill added to the report!")
    cont = input("\nDo you want to enter more bills (YES/NO)? ")

graph_permission = input("\nDo you want a visualization of your past bills (YES/NO)? ")
if graph_permission.lower() == "yes":
    print("\nWhat kind of graph do you want: \n1. Line Graph\n2. Bar Graph")

    wrong = True
    while wrong == True:
        graph_type = input("Enter the kind of graph you want the data to be visualized in: ")
        if graph_type.lower() == "line graph":
            y = np.loadtxt(file_path)

            plt.plot(y, marker = "o")

            plt.show()

            break
        elif graph_type.lower() == "bar graph":
            x = np.array([])
            y = np.loadtxt(file_path)
            y = np.atleast_1d(y)

            for i in range(len(y)):
                element = f"Entry {i + 1}"
                x = np.append(x, element)

            plt.bar(x, y)

            plt.show()

            break
        else:
            print("\nWrong kind entered!")
            wrong = True

print("\nGraph plotting successful!")