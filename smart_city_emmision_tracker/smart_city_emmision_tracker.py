import pandas as pd

file_path = r"C:\Python\smart_city_emmision_tracker\emmision_data.json"
df = pd.read_json(file_path)

x = df["Vehicle_Count"].mean()
df.fillna({"Vehicle_Count" : x}, inplace=True)

print(df.to_string())