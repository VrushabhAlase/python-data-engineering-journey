# =========================================
# Pandas - Day 1: Reading Data & Merging
# =========================================

# -----------------------------------------
# THEORY: What is Pandas?
# -----------------------------------------
# Pandas is a Python library used to work with tabular data
# Think of it like working with Excel or SQL tables in Python
#
# Core object = DataFrame
# A DataFrame is a table with rows and columns — just like Excel
#
# Install: pip install pandas
# Import:  import pandas as pd  ← 'pd' is standard shortcut everyone uses


import pandas as pd


# =========================================
# SECTION 1: Reading a CSV File
# =========================================

# pd.read_csv() → reads a CSV file and converts it into a DataFrame
# Make sure the file path is correct on your machine

df = pd.read_csv("D:/DATA_ENG/Self Study/Python/python-data-engineering-journey/06_file_handling/data1.csv")

print("\n--- Full Data ---")
print(df)   # prints the entire table


# =========================================
# SECTION 2: What is Merge?
# =========================================

# -----------------------------------------
# THEORY: Merge (JOIN in SQL)
# -----------------------------------------
# merge() combines two DataFrames based on a common column
# Exactly like SQL JOINs
#
# how="inner"  → only matching rows from both tables  (SQL: INNER JOIN)
# how="left"   → all rows from left + matching from right (SQL: LEFT JOIN)
# how="right"  → all rows from right + matching from left (SQL: RIGHT JOIN)
# how="outer"  → all rows from both tables              (SQL: FULL OUTER JOIN)


# -----------------------------------------
# Sample Data: Employees & Salary tables
# -----------------------------------------

# Creating employees table manually
df_emp = pd.DataFrame({
    "id":   [1, 2, 3, 4],               # employee IDs
    "name": ["Vrushabh", "Akshay", "Ravi", "Sneha"]  # employee names
})

# Creating salary table manually
# Note: employee 4 (Sneha) has no salary record
df_sal = pd.DataFrame({
    "id":     [1, 2, 3],                # only 3 employees have salary
    "salary": [30000, 60000, 70000]     # salary amounts
})

print("\n--- Employees Table ---")
print(df_emp)

print("\n--- Salary Table ---")
print(df_sal)


# =========================================
# SECTION 3: Types of Joins / Merges
# =========================================

# -----------------------------------------
# INNER JOIN
# -----------------------------------------
# Returns only rows that have a match in BOTH tables
# Employee 4 (Sneha) is excluded because she has no salary record

inner_join = pd.merge(df_emp, df_sal, on="id", how="inner")

print("\n--- INNER JOIN (only matching rows) ---")
print(inner_join)
# Output: Employees 1, 2, 3 only (Sneha excluded)


# -----------------------------------------
# LEFT JOIN
# -----------------------------------------
# Returns ALL rows from the LEFT table (df_emp)
# If no match in right table → fills with NaN (null)
# Sneha will appear but salary will be NaN

left_join = pd.merge(df_emp, df_sal, on="id", how="left")

print("\n--- LEFT JOIN (all employees, salary if available) ---")
print(left_join)
# Output: All 4 employees, Sneha's salary = NaN


# -----------------------------------------
# RIGHT JOIN
# -----------------------------------------
# Returns ALL rows from the RIGHT table (df_sal)
# If no match in left table → fills with NaN
# Useful when you want all salary records regardless of employee match

right_join = pd.merge(df_emp, df_sal, on="id", how="right")

print("\n--- RIGHT JOIN (all salary records, employee if available) ---")
print(right_join)


# -----------------------------------------
# OUTER JOIN (FULL JOIN)
# -----------------------------------------
# Returns ALL rows from BOTH tables
# Fills NaN wherever there is no match
# Most inclusive join — nothing is excluded

outer_join = pd.merge(df_emp, df_sal, on="id", how="outer")

print("\n--- OUTER JOIN (all rows from both tables) ---")
print(outer_join)


# =========================================
# SECTION 4: Working with Merged Data
# =========================================

# -----------------------------------------
# Find Employees with No Salary
# -----------------------------------------
# After LEFT JOIN, employees with no salary record have NaN in salary column
# isna() → returns True where value is NaN (missing/null)

no_salary = left_join[left_join["salary"].isna()]

print("\n--- Employees Without Salary ---")
print(no_salary)
# Output: Sneha — she has no salary record


# -----------------------------------------
# Fill Missing Salary with 0
# -----------------------------------------
# fillna(0) → replaces all NaN values with 0
# This is a common data cleaning step in real pipelines

left_join["salary"] = left_join["salary"].fillna(0)

print("\n--- After Filling Missing Salary with 0 ---")
print(left_join)
# Output: Sneha's salary is now 0 instead of NaN


# -----------------------------------------
# Calculate Total Salary
# -----------------------------------------
# sum() → adds up all values in the salary column
# Used in pipelines for aggregation and reporting

total_salary = left_join["salary"].sum()

print("\n--- Total Salary of All Employees ---")
print("Total Salary:", total_salary)


# =========================================
# SECTION 5: Rename Columns
# =========================================

# rename() → changes column names
# columns={"old_name": "new_name"}
# inplace=True → modifies the original DataFrame directly
#                without inplace=True, it returns a new copy

df_emp.rename(columns={"name": "employee_name"}, inplace=True)

print("\n--- After Renaming 'name' to 'employee_name' ---")
print(df_emp)


# =========================================
# QUICK REFERENCE — Merge / JOIN Summary
# =========================================

# pd.merge(df1, df2, on="column", how="inner")  → matching rows only
# pd.merge(df1, df2, on="column", how="left")   → all from df1
# pd.merge(df1, df2, on="column", how="right")  → all from df2
# pd.merge(df1, df2, on="column", how="outer")  → all from both

# df["col"].isna()       → find missing values
# df["col"].fillna(0)    → fill missing values with 0
# df["col"].sum()        → total of a column
# df.rename(columns={})  → rename columns