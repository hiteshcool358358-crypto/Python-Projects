import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt
import seaborn as sns

bal = float(input("Enter your month's starting balance: "))
income = float(input("Enter your monthly income: "))

# Fix 1: Properly capture the appended array
final_categories_list = np.array([])
category = str(input("Enter the categories your expenses lie in: "))
if category != "0":
    final_categories_list = np.append(final_categories_list, category)

while category != "0":
    category = str(input("Enter the categories your expenses lie in: "))
    if category == "0":
        break
    else:
        # Fix 1: Properly capture the appended array
        final_categories_list = np.append(final_categories_list, category)

print("An estimated graph of costs and expenses due to a fluctuation in some of the expenses: ")
x = r.normal(loc = 2500, scale = 50, size = 12)
sns.displot(x, kind = "kde")
plt.show()

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

print(f"You can recieve a big shock in the {shock_month + 1}th month of the year.")