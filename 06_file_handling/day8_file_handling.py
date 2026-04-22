# =========================================
# Day 8 - File Handling + CSV + JSON
# =========================================

"""
📌 Why File Handling?

In Data Engineering:
- Read data from files
- Process/transform data
- Write cleaned data

Example:
input.csv → process → output.csv
"""

import os
import csv
import json

# =========================================
# Section 1 — File Basics
# =========================================

# Print current working directory (VERY IMPORTANT)
print("Current Path:", os.getcwd())

# -----------------------------------------
# Writing to File (overwrite mode 'w')
# -----------------------------------------

with open("sample.txt", "w") as file:
    file.write("Hello Data Engineering\n")
    file.write("Learning file handling")

print("sample.txt created")

# -----------------------------------------
# Reading File (line by line)
# -----------------------------------------

print("\n--- Reading sample.txt ---")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())


# =========================================
# Section 2 — CSV (Manual Way)
# =========================================

# Create CSV file manually
with open("data1.csv", "w") as file:
    file.write("id,name,city,salary\n")
    file.write("1,A,Pune,30000\n")
    file.write("2,B,Mumbai,60000\n")
    file.write("3,C,Delhi,70000\n")

print("\ndata1.csv created")

# Read CSV manually
print("\n--- Manual CSV Read ---")
with open("data1.csv", "r") as file:
    for line in file:
        print(line.strip())


# =========================================
# Section 3 — CSV Module (Professional Way)
# =========================================

# Read CSV using csv.reader
print("\n--- csv.reader ---")
with open("data1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Skip header
print("\n--- Skip Header ---")
with open("data1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        print(row)


# -----------------------------------------
# DictReader (MOST IMPORTANT)
# -----------------------------------------

print("\n--- DictReader ---")
with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


# -----------------------------------------
# Filter Data (salary > 50000)
# -----------------------------------------

print("\n--- Salary > 50000 ---")
with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["salary"]) > 50000:
            print(row["name"], row["salary"])


# -----------------------------------------
# Aggregation (Total Salary)
# -----------------------------------------

total = 0

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["salary"])

print("\nTotal Salary:", total)


# -----------------------------------------
# Write CSV using csv module
# -----------------------------------------

data = [
    ["id", "name", "city"],
    ["1", "Vrushabh", "Pune"],
    ["2", "Akshay", "Mumbai"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("\noutput.csv created")


# =========================================
# Section 4 — JSON Handling
# =========================================

# Create JSON
data = {
    "id": 101,
    "name": "Vrushabh",
    "city": "Pune"
}

with open("data.json", "w") as file:
    json.dump(data, file)

print("\ndata.json created")


# -----------------------------------------
# Read JSON
# -----------------------------------------

with open("data.json", "r") as file:
    data = json.load(file)

print("\n--- JSON Data ---")
print(data)
print("Name:", data["name"])


# =========================================
# Section 5 — Extra Examples (Important)
# =========================================

# Append mode example
with open("sample.txt", "a") as file:
    file.write("\nNew line added")

print("\nData appended to sample.txt")


# Read full file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFull content:\n", content)


# Safe JSON access (best practice)
print("\nSafe access example:")
print(data.get("salary", "Not Available"))