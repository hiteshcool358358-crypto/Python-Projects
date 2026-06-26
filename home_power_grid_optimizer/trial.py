import pandas as pd
import numpy as np

data1 = r"C:\Python\home_power_grid_optimizer\home_power_grid_optimizer.csv"

df1 = pd.read_csv(data1)

apps = np.array(df1["Appliance"])
rates = np.array(df1["Power Rating (Watts)"])
behavs = np.array(df1["Behaviour"])

print(apps)
print(rates)
print(behavs)