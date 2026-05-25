#Inventory Management System
#Creating the lists
item_name = ["Maggi", "Pazzta", "Exo dishwashing soap", "Cream bun", "Cream roll", "Atta", "Dairy milk"]
item_price = [15.00, 35.00, 10.00, 12.00, 20.00, 534.00, 20.00]
item_stock = [40, 30, 80, 13, 23, 3, 4]
#Asking the name of the item the user wants to buy
item = input("Enter the name of the item you want to buy: ")
index_no = 0
#Finding the index no. of the item in the list
for i in range(0, len(item_name)):
    if item_name[index_no] == item:
        status = "found"
        break
    else:
        status = "not found"
    index_no += 1
#Checking if the item is available in the inventory of the store or not
#Informing about the avaialabilty of the item and asking the user how many items they want to buy and calculating the bill amount
if status == "found":
    quan = int(input(f"How many {item} do you want to buy= "))
    if item_stock[index_no] >= quan:
        bill = quan * item_price[index_no]
        item_stock[index_no] -= quan
        print(f"Net payable= ₹{bill}")
    else:
        print(f"Sorry, we only have {item_stock[index_no]} {item} in stock.")
        ans = input(f"Do you want us to pack the remaining {item_stock[index_no]} {item} for you? (yes/no)")
        if ans == "yes":
            bill = item_stock[index_no] * item_price[index_no]
            item_stock[index_no] = 0
        elif ans == "no":
            ans = int(input("How many should we pack instead= "))
            if ans == 0:
                print("Okay, we won't pack any items for you.")
            elif ans>0:
                if ans <= item_stock[index_no]:
                    bill = ans * item_price[index_no]
                    item_stock[index_no] -= ans
                    print(f"Net payable= ₹{bill}")
                else:
                    print(f"Sorry, we only have {item_stock[index_no]} {item} in stock.")
                    print(f"Net payable= ₹0")
elif status == "not found":
    print("Item not found in the inventory. Sorry for the inconvenience.")
ans = input("Do you want to buy another item? (yes/no)")
while ans == "yes":
    item = input("Enter the name of the item you want to buy: ")
    index_no = 0
    #Finding the index no. of the item in the list
    for i in range(0, len(item_name)):
        if item_name[index_no] == item:
            status = "found"
            break
        else:
            status = "not found"
        index_no += 1
    #Checking if the item is available in the inventory of the store or not
    #Informing about the avaialabilty of the item and asking the user how many items they want to buy and calculating the bill amount
    if status == "found":
        quan = int(input(f"How many {item} do you want to buy= "))
        if item_stock[index_no] >= quan:
            bill = quan * item_price[index_no]
            item_stock[index_no] -= quan
            print(f"Net payable= ₹{bill}")
        else:
            print(f"Sorry, we only have {item_stock[index_no]} {item} in stock.")
            pack_remainder = input(f"Do you want us to pack the remaining {item_stock[index_no]} {item} for you? (yes/no)")
            if pack_remainder == "yes":
                bill = item_stock[index_no] * item_price[index_no]
                item_stock[index_no] = 0
            elif pack_remainder == "no":
                ans = int(input("How many should we pack instead= "))
                if ans == 0:
                    print("Okay, we won't pack any items for you.")
                elif ans>0:
                    if ans <= item_stock[index_no]:
                        bill = ans * item_price[index_no]
                        item_stock[index_no] -= ans
                        print(f"Net payable= ₹{bill}")
                    else:
                        print(f"Sorry, we only have {item_stock[index_no]} {item} in stock.")
                        print(f"Net payable= ₹0")
    elif status == "not found":
        print("Item not found in the inventory. Sorry for the inconvenience.")
    ans = input("Do you want to buy another item? (yes/no)")