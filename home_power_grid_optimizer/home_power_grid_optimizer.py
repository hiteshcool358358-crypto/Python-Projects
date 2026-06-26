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

df1 = pd.read_csv(data1)
    

perm = input("Should we show the data table for all your appliances that have been registered so far (Y/N): ")
if perm.lower() == "y":
    print(df1.to_string())

data2 = r"C:\Python\home_power_grid_optimizer\weather_and_rates.csv"

df2 = pd.read_csv(data2)
temps = np.array(df2["Temperature(C)"])
time = np.array(df2["Hour/Time"])
cost = np.array(df2["Rate(₹)"])
apps = np.array(df1["Appliance"])
rates = np.array(df1["Power Rating (Watts)"]).astype(int)
behaves = np.array(df1["Behaviour"])

HourlyPowerConsumption = np.array([])
HourlyFinancialCost = np.array([])

for i in range(0, 24):
    hourly_watts = 0
    for x in range(len(apps)):
        if behaves[x] == "constant":
            hourly_watts += rates[x]
        elif behaves[x] == "variable":
            if temps[i] > 35:
                hourly_watts += rates[x]
            else:
                hourly_watts += 0
    hourly_bill = hourly_watts * cost[i]

    if hourly_watts > 3000:
        for z in range(len(apps)):
            if hourly_watts > 3000:
                if behaves[z] == "variable":
                    hourly_watts -= rates[z]
                    print(f"[{time[i]}] Alert: Peak load exceeded! Automatically shutting down {apps[z]} to save power.")
        hourly_bill = hourly_watts * cost[i]
        HourlyPowerConsumption = np.append(HourlyPowerConsumption, hourly_watts)
        HourlyFinancialCost = np.append(HourlyFinancialCost, hourly_bill)