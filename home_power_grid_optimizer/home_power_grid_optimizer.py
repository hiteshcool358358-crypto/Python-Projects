import pandas as pd
import numpy as np

data1 = r"C:\Python\home_power_grid_optimizer\home_power_grid_optimizer.csv"

app = ""
rate = ""
behav = ""

ans = input("Do you want to register a new appliaction of yours (Y/N): ")
while ans.lower() == "y":
    app = input("Enter the name of your appliance: ")
    rate = input("Enter the power rating of your appliance in watts: ")
    behav = input("What is its its behaviour (constant/variable): ")
    with open(data1, "a") as f:
        f.write(app + "," + rate + "," + behav + "\n")
    ans = input("Do you want to register a new appliaction of yours (Y/N): ")

perm = input("Should we show the data table for all your appliances that have been registered so far (Y/N): ")
if perm.lower() == "y":
    try:
        df1 = pd.read_csv(data1)
        print(df1)
    except pd.errors.EmptyDataError:
        print("Error!\nPlease register an appliance first.")
        app = ""
        while app == "" or app == " ":
            app = input("Enter the name of your appliance: ")
            rate = input("Enter the power rating of your appliance in watts: ")
            behav = input("What is its its behaviour (constant/variable): ")
    with open(data1, "a") as f:
        f.write(app + "," + rate + "," + behav + "\n")
    df1 = pd.read_csv(data1)
    print(df1)

data2 = r"C:\Python\home_power_grid_optimizer\weather_and_rates.csv"

df2 = pd.read_csv(data2)
temps = np.array(df2["Temperature(C)"])
time = np.array(df2["Hour/Time"])