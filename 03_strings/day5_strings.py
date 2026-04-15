# =========================================
# Day 5 - Strings (Complete)
# =========================================

# -----------------------------------------
# Section 1 — What is a String?
# -----------------------------------------

name = "vrushabh"
city = "Pune"
job  = 'Data Engineer'

# Single / Double quotes — both are valid
first_name = "Akshay"
last_name  = 'Patil'

# Multi-line string — use triple quotes
about = """
I am learning Python.
My goal is AWS Data Engineer.
"""

# String vs Number — very different types!
emp_id = "EMP001"
print(type(emp_id))   # <class 'str'>

emp_id = 11
print(type(emp_id))   # <class 'int'>


# -----------------------------------------
# Section 2 — Length & Indexing
# -----------------------------------------
# String index works like a row of boxes:
# V  r  u  s  h  a  b  h
# 0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1  ← negative index from end

name = "Vrushabh"

print(len(name))    # 8 — total characters

print(name[0])      # V  — first character
print(name[1])      # r  — second character
print(name[-1])     # h  — last character
print(name[-2])     # b  — second from last
print(name[5])      # a  — index 5


# -----------------------------------------
# Section 3 — Looping through a String
# -----------------------------------------

print("\n--- Loop using index ---")
for i in range(len(name)):
    print(name[i])

print("\n--- Loop using slicing ---")
for ch in name[0:8]:
    print(ch)

print("\n--- Direct loop (Best Practice) ---")
for ch in name:
    print(ch)


# -----------------------------------------
# Section 4 — Slicing
# -----------------------------------------
# Syntax: string[start:stop]  → stop index is EXCLUDED

print(name[0:4])    # Vrus
print(name[2:6])    # usha
print(name[:4])     # Vrus  — start defaults to 0
print(name[4:])     # habh  — stop defaults to end
print(name[:])      # Vrushabh — full string copy


# -----------------------------------------
# Section 5 — String Methods
# -----------------------------------------

text = "  hello data engineer  "

# Case methods
print(text.upper())     # "  HELLO DATA ENGINEER  "
print(text.lower())     # "  hello data engineer  "
print(text.title())     # "  Hello Data Engineer  "

# Whitespace removal
print(text.strip())     # "hello data engineer"   — removes BOTH sides
print(text.lstrip())    # "hello data engineer  " — removes LEFT side only
print(text.rstrip())    # "  hello data engineer" — removes RIGHT side only

# Check start / end
print(text.strip().startswith("hello"))     # True
print(text.strip().endswith("engineer"))    # True

# Count & Find
sentence = "data engineer works with data"
print(sentence.count("data"))       # 2 — appears twice
print(sentence.find("engineer"))    # 5 — index where "engineer" starts


# -----------------------------------------
# Section 6 — Replace & Split
# -----------------------------------------

# replace(old, new)
filename = "sales_data_2024.CSV"
clean = filename.replace(".CSV", ".csv")
print(clean)    # sales_data_2024.csv

filename = "Data_engineering_students_2026.sql"
clean = filename.replace(".sql", ".SQL")
print(clean)    # Data_engineering_students_2026.SQL

# split(separator) — breaks string into a list
csv_row = "Vrushabh,Pune,DataEngineer,AWS"
fields  = csv_row.split(",")
print(fields)       # ['Vrushabh', 'Pune', 'DataEngineer', 'AWS']
print(fields[0])    # Vrushabh
print(fields[2])    # DataEngineer

# split by space (default — no separator needed)
sentence = "I love data engineering"
words = sentence.split()
print(words)    # ['I', 'love', 'data', 'engineering']


# -----------------------------------------
# Section 7 — f-Strings
# -----------------------------------------

name  = "Vrushabh"
day   = 5
topic = "Strings"

print(f"Day {day}: {topic}")
print(f"Hello {name}, today we are learning {topic}!")

records = 1500
print(f"Total records processed: {records:,}")      # adds comma → 1,500
print(f"Pipeline success rate: {95.678:.2f}%")      # 2 decimal places → 95.68%


# -----------------------------------------
# Section 8 — Real Data Engineering Examples
# -----------------------------------------

# DE use 1: Clean a messy column name from CSV header
raw_header = "  Customer Name  "
clean = raw_header.strip().lower().replace(" ", "_")
print(clean)    # customer_name

# DE use 2: Extract date from filename
filename = "sales_report_2024_04_14.csv"
parts    = filename.replace(".csv", "").split("_")
date_str = f"{parts[2]}-{parts[3]}-{parts[4]}"
print(date_str)     # 2024-04-14

# DE use 3: Build a dynamic S3 file path
bucket = "my-data-lake"
env    = "prod"
date   = "2024-04-14"
path   = f"s3://{bucket}/{env}/sales/{date}/data.parquet"
print(path)     # s3://my-data-lake/prod/sales/2024-04-14/data.parquet

# DE use 4: Check file format before processing
file = "customers.csv"
if file.endswith(".csv"):
    print(f"Processing CSV: {file}")
elif file.endswith(".parquet"):
    print(f"Processing Parquet: {file}")
else:
    print(f"Unknown format: {file}")


# =========================================
# Practice Problems
# =========================================

# -----------------------------------------
# Problem 1 — strip + case methods
# -----------------------------------------

text   = "  DATA_ENGINEER  "
result = text.strip().lower()
print(result)   # data_engineer

# rstrip removes RIGHT side spaces only — dash on LEFT stays
text   = "-  abscdefghijklmnopqrstuvwxyz  "
result = text.rstrip().upper()
print(result)   # "-  ABSCDEFGHIJKLMNOPQRSTUVWXYZ"  ← dash + left spaces remain

# lstrip removes LEFT side spaces only — right spaces stay
text   = "  abscdefghijklmnopqrstuvwxyz  "
result = text.lstrip().upper()
print(result)   # "ABSCDEFGHIJKLMNOPQRSTUVWXYZ  "  ← trailing spaces remain

# strip removes BOTH sides
text   = "  abscdefghijklmnopqrstuvwxyz  "
result = text.strip().upper()
print(result)   # "ABSCDEFGHIJKLMNOPQRSTUVWXYZ"


# -----------------------------------------
# Problem 2 — Parse filename, extract date
# -----------------------------------------

# Basic: extract date from employee report filename
file  = "employee_report_2024_03_15.csv"
parts = file.replace(".csv", "").split("_")
# parts → ['employee', 'report', '2024', '03', '15']
#           0            1         2       3     4
date  = f"{parts[2]}-{parts[3]}-{parts[4]}"
print(date)     # 2024-03-15

# Extended: extract file_type and date (reversed: DD-MM-YYYY)
file  = "orders_online_2025_11_30.json"
parts = file.replace(".json", "").split("_")
# parts → ['orders', 'online', '2025', '11', '30']
#           0          1         2       3     4
# BUG FIX: avoid using 'type' as variable name — it shadows Python built-in
file_type = parts[1]
date      = f"{parts[4]}-{parts[3]}-{parts[2]}"    # DD-MM-YYYY
print(file_type)    # online
print(date)         # 30-11-2025

# Task 2: Extract region + FULL date from filename
file  = "sales_US_west_2024_07_25.csv"
parts = file.replace(".csv", "").split("_")
# parts → ['sales', 'US', 'west', '2024', '07', '25']
#           0        1     2        3       4     5
region = f"{parts[1]}-{parts[2]}"
# BUG FIX: parts[4] gives only the MONTH (07), not the full date
# Correct: combine parts[3]-parts[4]-parts[5] for full date
date   = f"{parts[3]}-{parts[4]}-{parts[5]}"
print(region)   # US-west
print(date)     # 2024-07-25  ← was printing only "07" before the fix


# -----------------------------------------
# Problem 3 — Split CSV row, print each field
# -----------------------------------------

data   = "Mumbai,Maharashtra,India,400001"
fields = data.split(",")
for item in fields:
    print(item)
# Mumbai
# Maharashtra
# India
# 400001


# -----------------------------------------
# Problem 4 — f-string formatting
# -----------------------------------------

pipeline = "sales"
date     = "2024-04-14"
records  = 5000
print(f"Pipeline: {pipeline} | Date: {date} | Records: {records:,}")
# Pipeline: sales | Date: 2024-04-14 | Records: 5,000


# =========================================
# Section 9 — Extra String Methods
# (Important for DE — not covered above)
# =========================================

# join() — opposite of split(), builds a string from a list
# Very common in DE for rebuilding paths, headers, queries

parts = ["2024", "04", "14"]
date  = "-".join(parts)
print(date)     # 2024-04-14

columns = ["customer_id", "name", "region", "revenue"]
header  = ", ".join(columns)
print(header)   # customer_id, name, region, revenue

# in operator — check if substring exists inside string
filename = "sales_2024_04_14.csv"
print("2024" in filename)       # True
print("parquet" in filename)    # False

# DE use: check if filename belongs to correct folder/table
if "sales" in filename:
    print("This is a sales file — route to sales pipeline")

# isdigit() — check if string contains only numbers
# Useful for validating IDs, zip codes, numeric columns
print("400001".isdigit())   # True
print("EMP001".isdigit())   # False

# zfill() — pad a number string with leading zeros
# Common in DE for generating batch IDs or sequence numbers
batch_id = "7"
print(batch_id.zfill(4))    # 0007

for i in range(1, 6):
    print(f"BATCH_{str(i).zfill(4)}")
# BATCH_0001
# BATCH_0002 ... etc