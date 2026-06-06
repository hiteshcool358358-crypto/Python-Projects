import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

bal = float(input("Enter your month's starting balance: ₹"))
income = float(input("Enter your monthly income: ₹"))

final_categories_list = np.array([])
category = str(input("Enter the categories your expenses lie in: "))
if category != "0":
    final_categories_list = np.append(final_categories_list, category)

while category != "0":
    category = str(input("Enter the categories your expenses lie in: "))
    if category == "0":
        break
    else:
        final_categories_list = np.append(final_categories_list, category)

print(" ")
print("An estimated graph of costs and expenses due to a fluctuation in some of the expenses: ")
x = r.normal(loc = 2500, scale = 50, size = 12)
sns.displot(x, kind = "kde")
plt.show()

print(" ")
q1 = int(input("How often do you buy an expensive electronic per 100 times: "))
q2 = int(input("How often do you go out for a luxury dinner per 100 times: "))

p1 = q1 / 100
p2 = q2 / 100
p3 = 1.0 - (p1 + p2)

probab = np.array([p1, p2, p3])

unexpShoppingProbab = r.choice(["Purchase of an expensive electronic", "Luxury dinner", "No unexpected expense"], p = probab, size = 12)
graph = r.binomial(n = 12, p = 1/12, size = 1000)
sns.displot(graph)

plt.show()

big_shock = r.randint(29999, 49999)
shock_month = r.randint(0, 11)

print(" ")
print(f"You can recieve a big shock in the {shock_month + 1}th month of the year.")

ElecCost = 35000
DinnerCost = 5000

final_balances = np.array([])

for i in range(1000):
    YearExpense = 0
    shock_month = r.randint(0, 12)
    big_shock = r.randint(29999, 49999)
    
    for m in range(12):
        monthly_base = r.normal(loc = 2500, scale = 50)
        YearExpense += monthly_base
        
        event = r.choice(["Purchase of an expensive electronic", "Luxury dinner", "No unexpected expense"], p = probab)
        
        if event == "Purchase of an expensive electronic":
            YearExpense += ElecCost
        elif event == "Luxury dinner":
            YearExpense += DinnerCost
            
        if m == shock_month:
            YearExpense += big_shock
            
    FinalYearBalance = bal + (12 * income) - YearExpense
    final_balances = np.append(final_balances, FinalYearBalance)

avg_save = np.mean(final_balances)
max_save = np.max(final_balances)
min_save = np.min(final_balances)

file_path = r"C:\Python\personal_finance_and_expense_simulation_tool\Finance and Expense Track Summary.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("==================================================\n")
    f.write("      FINANCIAL SIMULATION REPORT             \n")
    f.write("==================================================\n")
    f.write("\n")
    f.write(f"Initial Starting Balance: ₹{bal:.2f}\n")
    f.write(f"Fixed Monthly Income: ₹{income:.2f}\n")
    f.write("\n")
    f.write("--------------------------------------------------\n")
    f.write("  1,000-YEAR LIFETIME SIMULATION RESULTS          \n")
    f.write("--------------------------------------------------\n")
    f.write("\n")
    f.write(f"Average Expected Ending Balance: ₹{avg_save:.2f}\n")
    f.write(f"Best-Case Scenario Ending Balance: ₹{max_save:.2f}\n")
    f.write(f"Worst-Case Scenario Ending Balance: ₹{min_save:.2f}\n")
    f.write("\n")
    f.write("--------------------------------------------------\n")
    f.write("Report generated successfully.")

print(" ")
print(f"A new file Finace and Expense Track Summary in the same folder as this file's.")