# =========================================
# Day 10 - Python Modules (os, datetime, random)
# =========================================

"""
📌 Purpose of this file:

Learn and use important Python modules:
1. os       → File & directory operations
2. datetime → Date & time handling
3. random   → Random data generation

These are widely used in Data Engineering pipelines.
"""

# =========================================
# Section 1 — OS MODULE (File System Operations)
# =========================================

import os

print("\n--- OS MODULE ---")

# Get current working directory (where script is running)
current_path = os.getcwd()
print("Current Path:", current_path)

# List all files and folders in current directory
files = os.listdir()
print("\nFiles in current directory:")
for f in files:
    print(f)

# Create a folder (if it does not exist)
os.makedirs("test_folder", exist_ok=True)
print("\n'test_folder' created (or already exists)")

# Check if a file exists
if os.path.exists("sample.txt"):
    print("\n'sample.txt' exists")

# Get file size (in bytes)
if os.path.exists("sample.txt"):
    size = os.path.getsize("sample.txt")
    print("File size:", size, "bytes")


# =========================================
# Section 2 — DATETIME MODULE (Date & Time)
# =========================================

from datetime import datetime

print("\n--- DATETIME MODULE ---")

# Get current date and time
now = datetime.now()
print("Current DateTime:", now)

# Format date (commonly used in pipelines/logs)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Extract individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


# =========================================
# Section 3 — RANDOM MODULE (Test Data)
# =========================================

import random

print("\n--- RANDOM MODULE ---")

# Generate random number between 1 and 100
rand_num = random.randint(1, 100)
print("Random Number:", rand_num)

# Select random item from list
cities = ["Pune", "Mumbai", "Delhi"]
random_city = random.choice(cities)
print("Random City:", random_city)

# Shuffle list randomly
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffled List:", nums)


# =========================================
# Section 4 — Real Data Engineering Use Case
# =========================================

print("\n--- REAL USE CASE ---")

# Create dynamic folder based on today's date
date = datetime.now().strftime("%Y-%m-%d")

folder_path = f"data/{date}"

# Create folder structure (like partitioned data)
os.makedirs(folder_path, exist_ok=True)

# Create file inside that folder
file_path = f"{folder_path}/output.txt"

with open(file_path, "w") as file:
    file.write("Pipeline output")

print("File created at:", file_path)


# =========================================
# Section 5 — Practice Tasks (Solutions)
# =========================================

print("\n--- PRACTICE TASKS ---")

# -----------------------------------------
# Task 1: List all files
# -----------------------------------------

print("\nTask 1: Files in current directory")
for f in os.listdir():
    print(f)


# -----------------------------------------
# Task 2: Create "logs" folder
# -----------------------------------------

os.makedirs("logs", exist_ok=True)
print("\nTask 2: 'logs' folder created")


# -----------------------------------------
# Task 3: Print current date (YYYY-MM-DD)
# -----------------------------------------

today = datetime.now().strftime("%Y-%m-%d")
print("\nTask 3: Today's Date:", today)


# -----------------------------------------
# Task 4: Generate random number (50-100)
# -----------------------------------------

rand_num = random.randint(50, 100)
print("\nTask 4: Random Number (50-100):", rand_num)


# -----------------------------------------
# Task 5: Create file with today's date
# -----------------------------------------

file_name = f"report_{today}.txt"

with open(file_name, "w") as file:
    file.write("Daily Report\n")
    file.write(f"Date: {today}")

print("\nTask 5: File created →", file_name)


# =========================================
# Key Learnings
# =========================================

"""
✔ os module → file and directory handling
✔ datetime → date formatting and extraction
✔ random → test data and sampling

👉 These are used in:
- ETL pipelines
- Logging systems
- Data partitioning
- Automation scripts
"""

