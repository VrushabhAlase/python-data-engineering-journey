# =========================================
# Day 9 - Exception Handling (Complete Guide)
# =========================================

"""
📌 What is Exception Handling?

An exception is an error that occurs during program execution.

Without handling → program crashes ❌
With handling → program continues safely ✅

Used heavily in:
- File handling
- APIs
- Data pipelines
"""

# =========================================
# Section 1 — Basic Exception Handling
# =========================================

print("\n--- Basic Example ---")

try:
    num = int("abc")   # invalid conversion
except:
    print("Error occurred: invalid number")


# =========================================
# Section 2 — Specific Exception (Best Practice)
# =========================================

print("\n--- Specific Exception ---")

try:
    num = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to int")


# =========================================
# Section 3 — Multiple Exceptions
# =========================================

print("\n--- Multiple Exceptions ---")

try:
    x = int("abc")     # ValueError
    y = 10 / 0         # ZeroDivisionError
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# =========================================
# Section 4 — Finally Block
# =========================================

print("\n--- Finally Block ---")

try:
    print("Trying something...")
except:
    print("Error occurred")
finally:
    print("This always runs (cleanup/logging)")


# =========================================
# Section 5 — File Handling Example
# =========================================

print("\n--- File Handling ---")

try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")


# =========================================
# Section 6 — JSON Handling (Real DE Example)
# =========================================

import json

print("\n--- JSON Handling ---")

try:
    with open("data.json", "r") as file:
        data = json.load(file)

    print("Name:", data["name"])

    # This key may not exist
    print("Salary:", data["salary"])

except FileNotFoundError:
    print("JSON file not found")

except KeyError:
    print("Key not found in JSON")


# =========================================
# Section 7 — Generic Exception (Advanced)
# =========================================

print("\n--- Generic Exception ---")

try:
    x = int("abc")
except Exception as e:
    print("Error:", e)


# =========================================
# Section 8 — Real Data Engineering Style
# =========================================

print("\n--- Real ETL Example ---")

try:
    with open("data.json", "r") as file:
        data = json.load(file)

    # Safe access using .get()
    salary = data.get("salary", 0)

    print("Salary:", salary)

except FileNotFoundError:
    print("File missing")

except Exception as e:
    print("Unexpected error:", e)


# =========================================
# Section 9 — Practice Problems
# =========================================

print("\n--- Practice Section ---")

# Task 1: Handle invalid number
try:
    value = int("xyz")
except ValueError:
    print("Practice 1: Invalid number handled")


# Task 2: Handle division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Practice 2: Division by zero handled")


# Task 3: Handle missing file
try:
    with open("not_exists.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Practice 3: File not found handled")


# Task 4: JSON safe handling
try:
    with open("data.json", "r") as file:
        data = json.load(file)

    print("Practice 4 Name:", data.get("name", "NA"))
    print("Practice 4 Salary:", data.get("salary", "NA"))

except FileNotFoundError:
    print("Practice 4: JSON file missing")


# =========================================
# Key Learnings
# =========================================

"""
✔ try → risky code
✔ except → handle error
✔ specific exceptions → best practice
✔ finally → always executes
✔ Exception as e → debug errors
✔ .get() → safe dictionary access

👉 This is essential for:
- Data pipelines
- APIs
- Production systems
"""


print("\n--- Count Lines ---")

count = 0

with open("sample.txt", "r") as file:
    for line in file:
        count += 1

print("Total lines:", count)


print("\n--- Count Words ---")

word_count = 0

with open("sample.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print("Total words:", word_count)

print("\n--- File Copy ---")

with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as target:
    target.write(content)

print("File copied successfully")


print("\n--- Filter Lines ---")

with open("sample.txt", "r") as file:
    for line in file:
        if "Data" in line:
            print(line.strip())