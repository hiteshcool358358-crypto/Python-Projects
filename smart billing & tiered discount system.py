'''This program is a Smart Billing & Tiered Discount System. It will calculate the bill and give discount on certain criteria as well and 
also calculate the loyalty points earned by the customer.'''
#Creating lists to sore the prices of the items purchased by the user.
prices = []
price = float(input("Enter the price of the item purchased= "))
prices.append(price)
#Creating a list of the prices of all the items purchased by the user.
while price > 0:
    price = float(input("Enter the price of the item purchased= "))
    if price > 0:
        prices.append(price)
    else:
        break
#Defining functions for calculating value and returning the output with a relevant message and in a formatted output.
def bill_calculator():
    s = 0
    for i in prices:
        s += i
    print(f"Original Total: Rs. {s}")
def discount_calculator():
    s = 0
    for i in prices:
        s += i
    if s >= 500:
        d = 0.1 * s
    else:
        d = 0
    print(f"Discount Applied: Rs. {d}")
def discounted_amt():
    s = 0
    for i in prices:
        s += i
    if s >= 500:
        s -= (0.1 * s)
    else:
        s = s
    print(f"Final Amount to Pay: Rs. {s}")
def loyalty_points_calculator():
    s = 0
    for i in prices:
        s += i
    if s >= 500:
        dt = s - (0.1 * s)  
    else:
        dt = s
    print(f"Loyalty Points Earned: {dt // 10} points")
#Printing the output in a formatted manner like a reciept.
print("--- FINAL RECEIPT ---")
c = 1
for x in prices:
    print(f"Item {c}: Rs. {x}")
    c += 1
print("---------------------")
print(f"Items processed: {len(prices)}")
bill_calculator()
discount_calculator()
discounted_amt()
loyalty_points_calculator()
print("---------------------")