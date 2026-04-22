import os

print("\n--- OS MODULE ---")

# Current working directory
print("Current Path:", os.getcwd())

# List files in directory
print("Files:", os.listdir())

# Create a folder
os.makedirs("test_folder", exist_ok=True)
print("Folder created")

# Check if file exists
if os.path.exists("sample.txt"):
    print("sample.txt exists")

# Get file size
if os.path.exists("sample.txt"):
    print("File size:", os.path.getsize("sample.txt"), "bytes")

from datetime import datetime

print("\n--- DATETIME MODULE ---")

# Current date & time
now = datetime.now()
print("Now:", now)

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Extract parts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


import random

print("\n--- RANDOM MODULE ---")

# Random number
print("Random int:", random.randint(1, 100))

# Random choice
cities = ["Pune", "Mumbai", "Delhi"]
print("Random city:", random.choice(cities))

# Shuffle list
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffled:", nums)


import os
from datetime import datetime

print("\n--- REAL USE CASE ---")

# Dynamic file path
date = datetime.now().strftime("%Y-%m-%d")

folder_path = f"data/{date}"
os.makedirs(folder_path, exist_ok=True)

file_path = f"{folder_path}/output.txt"

with open(file_path, "w") as file:
    file.write("Pipeline output")

print("File created at:", file_path)


# =========================================
# Practice Solutions - Modules
# =========================================

import os
from datetime import datetime
import random

# -----------------------------------------
# Task 1: Print current folder files
# -----------------------------------------

print("\n--- Task 1: List Files ---")

files = os.listdir()
print("Files in current directory:")
for f in files:
    print(f)


# -----------------------------------------
# Task 2: Create folder "logs"
# -----------------------------------------

print("\n--- Task 2: Create Folder ---")

os.makedirs("logs", exist_ok=True)
print("Folder 'logs' created (or already exists)")


# -----------------------------------------
# Task 3: Print current date YYYY-MM-DD
# -----------------------------------------

print("\n--- Task 3: Current Date ---")

today = datetime.now().strftime("%Y-%m-%d")
print("Today:", today)


# -----------------------------------------
# Task 4: Random number between 50-100
# -----------------------------------------

print("\n--- Task 4: Random Number ---")

rand_num = random.randint(50, 100)
print("Random Number:", rand_num)


# -----------------------------------------
# Task 5: Create file with today's date
# -----------------------------------------

print("\n--- Task 5: Create Dated File ---")

file_name = f"report_{today}.txt"

with open(file_name, "w") as file:
    file.write("Daily report generated\n")
    file.write(f"Date: {today}")

print("File created:", file_name)