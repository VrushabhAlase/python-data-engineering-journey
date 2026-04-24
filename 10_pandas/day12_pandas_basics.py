"""
🧠 What is Pandas?

👉 A library to work with tabular data (like Excel / SQL tables)
👉 Core object = DataFrame
"""

#Step 1: Read CSV
import pandas as pd

# Read CSV file
df = pd.read_csv("D:/DATA_ENG/Self Study/Python/python-data-engineering-journey/06_file_handling/data1.csv")

print("\n--- Full Data ---")
print(df)

df1 = pd.read_csv("employees.csv")
df2 = pd.read_csv("salary.csv")

merged = pd.merge(df1, df2, on="id")

print(merged)


#🧠 What is Merge?

#👉 Combine data from multiple tables (like SQL JOIN)

import pandas as pd

# Employees table
df_emp = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["A", "B", "C", "D"]
})

# Salary table
df_sal = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [30000, 60000, 70000]
})

print("\n--- Employees ---")
print(df_emp)

print("\n--- Salary ---")
print(df_sal)

merged = pd.merge(df_emp, df_sal, on="id", how="inner")

print("\n--- INNER JOIN ---")
print(merged)

left_join = pd.merge(df_emp, df_sal, on="id", how="left")

print("\n--- LEFT JOIN ---")
print(left_join)

left_join = pd.merge(df1, df2, on="id", how="left")

print("\n--- LEFT JOIN ---")
print(left_join)

# RIGHT JOIN
right_join = pd.merge(df_emp, df_sal, on="id", how="right")
print("\n--- RIGHT JOIN ---")
print(right_join)

# OUTER JOIN
outer_join = pd.merge(df_emp, df_sal, on="id", how="outer")
print("\n--- OUTER JOIN ---")
print(outer_join)

# Employees without salary
no_salary = left_join[left_join["salary"].isna()]

print("\n--- Employees without Salary ---")
print(no_salary)

left_join["salary"] = left_join["salary"].fillna(0)

print("\n--- After Filling Missing Salary ---")
print(left_join)

total_salary = left_join["salary"].sum()

print("\nTotal Salary:", total_salary)

df_emp.rename(columns={"name": "employee_name"}, inplace=True)

print("\n--- Renamed Columns ---")
print(df_emp)