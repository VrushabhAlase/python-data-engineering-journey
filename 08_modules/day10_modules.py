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