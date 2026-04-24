# =========================================
# Sales Data Pipeline (Basic Version)
# =========================================

"""
Goal:
Read → Clean → Transform → Save
"""

import pandas as pd
import os

print("\n--- STEP 1: READ DATA ---")

# Read input file
df = pd.read_csv("input/sales.csv")
print(df)


# -----------------------------------------
# STEP 2: CLEAN DATA
# -----------------------------------------

print("\n--- STEP 2: CLEAN DATA ---")

# Fill missing values with 0
df["amount"] = df["amount"].fillna(0).astype(int)

print(df)


# -----------------------------------------
# STEP 3: TRANSFORM DATA
# -----------------------------------------

print("\n--- STEP 3: TRANSFORM DATA ---")

# Add new columns
df["tax"] = df["amount"] * 0.10
df["total"] = df["amount"] + df["tax"]

print(df)


# -----------------------------------------
# STEP 4: SAVE OUTPUT
# -----------------------------------------

print("\n--- STEP 4: SAVE OUTPUT ---")

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Save processed file
df.to_csv("output/processed_sales.csv", index=False)

print("File saved successfully at: output/processed_sales.csv")


# =========================================
# PIPELINE COMPLETE
# =========================================