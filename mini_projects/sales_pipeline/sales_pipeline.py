import pandas as pd

# Step 1: Read file
df = pd.read_csv("D:\DATA_ENG\Self Study\Python\python-data-engineering-journey\mini_projects\sales_pipeline\input\sales.csv")

print(df)

import pandas as pd

df = pd.read_csv("input/sales.csv")

# Fill missing values
df["amount"] = df["amount"].fillna(0)

print(df)


import pandas as pd

df = pd.read_csv("input/sales.csv")

df["amount"] = df["amount"].fillna(0).astype(int)

# Add columns
df["tax"] = df["amount"] * 0.10
df["total"] = df["amount"] + df["tax"]

print(df)

import pandas as pd
import os

df = pd.read_csv("input/sales.csv")

df["amount"] = df["amount"].fillna(0).astype(int)

df["tax"] = df["amount"] * 0.10
df["total"] = df["amount"] + df["tax"]

# Create output folder
os.makedirs("output", exist_ok=True)

# Save file
df.to_csv("output/processed_sales.csv", index=False)

print("File saved")