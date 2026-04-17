# =========================================
# Day 6 - Lists (Complete)
# =========================================

# -----------------------------------------
# What is a List?
# -----------------------------------------
# A list is a collection of multiple values stored in order
# - Ordered     → items stay in the order you add them
# - Mutable     → you can change, add, remove items
# - Allows duplicates → [1, 1, 2, 3] is valid
# - Index starts from 0

numbers = [10, 20, 30, 40]
names   = ["Vrushabh", "Akshay", "Rohit"]
mixed   = [10, "Python", True]

print(numbers)
print(names)
print(mixed)


# -----------------------------------------
# Accessing Elements (Indexing)
# -----------------------------------------

print(numbers[0])    # 10  — first element
print(names[1])      # Akshay
print(numbers[-1])   # 40  — last element (negative = from end)


# -----------------------------------------
# Slicing a List (same as strings)
# -----------------------------------------
# Syntax: list[start:stop]  — stop is excluded

nums = [10, 20, 30, 40, 50]
print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]   — first 3
print(nums[2:])      # [30, 40, 50]   — from index 2 to end
print(nums[-2:])     # [40, 50]       — last 2 elements

# DE use: grab first 5 records from a batch for preview
batch = [101, 102, 103, 104, 105, 106, 107, 108]
preview = batch[:5]
print("Preview:", preview)    # [101, 102, 103, 104, 105]


# -----------------------------------------
# Looping through a List
# -----------------------------------------

print("\n--- Loop through numbers ---")
for num in numbers:
    print(num)

cities = ["Pune", "Mumbai", "Delhi"]

print("\n--- Loop through cities ---")
for city in cities:
    print(city)

# Loop with index using enumerate()
print("\n--- Loop with index ---")
for i, city in enumerate(cities):
    print(f"Index {i}: {city}")


# =========================================
# Section 2: List Operations
# =========================================

# In Data Engineering:
# - append()  → add a new record to a batch
# - remove()  → drop a bad/invalid record
# - pop()     → remove record at specific position
# - insert()  → add record at specific position

numbers = [10, 20, 30, 50, 60, 70, 80]

# -----------------------------------------
# append() — add to END of list
# -----------------------------------------
numbers.append(40)
numbers.append(100)
print("\nAfter append:", numbers)

# -----------------------------------------
# insert(index, value) — add at specific position
# -----------------------------------------
numbers.insert(1, 15)
numbers.insert(5, 90)
print("After insert:", numbers)

# -----------------------------------------
# remove(value) — remove FIRST occurrence of value
# -----------------------------------------
numbers.remove(90)
numbers.remove(40)
print("After remove:", numbers)

# -----------------------------------------
# insert again (practice)
# -----------------------------------------
numbers.insert(4, 40)
numbers.insert(9, 90)
print("After re-insert:", numbers)

# -----------------------------------------
# pop(index) — remove by INDEX, returns the removed value
# -----------------------------------------
removed = numbers.pop(1)    # removes index 1, returns it
print("Popped value:", removed)
numbers.pop(3)
print("After pop:", numbers)

# -----------------------------------------
# len() — length of list
# -----------------------------------------
print("Length:", len(numbers))

# -----------------------------------------
# in — check if value exists
# -----------------------------------------
print(10 in numbers)    # True
print(99 in numbers)    # False


# =========================================
# Sorting and Reversing
# =========================================

nums = [5, 2, 9, 1]

nums.sort()              # sort ascending — modifies original list
print("\nSorted:", nums)

nums.sort(reverse=True)  # sort descending
print("Sorted desc:", nums)

nums.reverse()           # reverse current order
print("Reversed:", nums)

# sorted() — returns NEW sorted list, does NOT modify original
original = [5, 2, 9, 1]
new_sorted = sorted(original)
print("Original:", original)      # unchanged
print("New sorted:", new_sorted)  # new list


# =========================================
# Practice Example
# =========================================

names = ["A", "B", "C"]

names.append("D")
names.insert(1, "X")
names.remove("B")

print("\nFinal names list:", names)

names.sort()
print("Sorted:", names)

names.reverse()
print("Reversed:", names)


# =========================================
# Find Maximum Value (Manual Logic)
# =========================================
# This teaches you the logic behind max()
# Very common in DE interview questions

nums = [10, 50, 20, 80, 30]

max_num = nums[0]    # assume first value is max

for num in nums:
    if num > max_num:
        max_num = num

print("\nMaximum (manual):", max_num)       # 80

# Python built-in shortcuts
print("max():", max(nums))                  # 80
print("min():", min(nums))                  # 10
print("sum():", sum(nums))                  # 190
print("Type of max_num:", type(max_num))    # <class 'int'>


# =========================================
# Section 3 — List of Lists (2D List)
# =========================================
# In DE this is how you represent tabular data
# before loading into Pandas or a database

# Each inner list = one row of data
records = [
    ["EMP001", "Vrushabh", "Pune",   "Data Engineer"],
    ["EMP002", "Akshay",   "Mumbai", "Data Analyst"],
    ["EMP003", "Rohit",    "Delhi",  "DE Lead"],
]

# Access one row
print("\nFirst row:", records[0])           # ['EMP001', 'Vrushabh', ...]

# Access specific field — row 1, column 2
print("City of Akshay:", records[1][2])    # Mumbai

# Loop through all records
print("\n--- All Employees ---")
for row in records:
    print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]} | Role: {row[3]}")


# =========================================
# Section 4 — DE Real-World Scenarios
# =========================================

# --- Scenario 1: Filter valid records from a batch ---
# In real pipelines you remove empty/invalid records before processing

record_counts = [1500, 0, 800, 0, 2500, 300]
valid_records = []

for count in record_counts:
    if count > 0:
        valid_records.append(count)

print("\nValid records:", valid_records)
print("Total valid batches:", len(valid_records))
print("Total records:", sum(valid_records))


# --- Scenario 2: Collect only .csv files from a file list ---
# Common in Glue/Lambda when scanning an S3 folder

files = [
    "sales_2024.csv",
    "config.json",
    "orders_2024.csv",
    "notes.txt",
    "customers_2024.csv"
]

csv_files = []
for file in files:
    if file.endswith(".csv"):
        csv_files.append(file)

print("\nCSV files to process:", csv_files)


# --- Scenario 3: Extract unique regions from records ---
# Deduplication — common in data pipelines

regions = ["North", "South", "North", "East", "South", "West", "East"]
unique_regions = []

for region in regions:
    if region not in unique_regions:
        unique_regions.append(region)

print("\nUnique regions:", unique_regions)
# Note: a cleaner way is using set() — covered in Sets topic


# --- Scenario 4: Build a batch summary ---
# Simulates generating a pipeline run report

batches = [
    ["batch_001", 1500],
    ["batch_002", 0],
    ["batch_003", 800],
    ["batch_004", 2500],
]

print("\n--- Batch Summary ---")
for batch in batches:
    name  = batch[0]
    count = batch[1]
    if count == 0:
        status = "EMPTY — ALERT"
    elif count < 500:
        status = "LOW"
    else:
        status = "OK"
    print(f"{name} | Records: {count} | Status: {status}")


# =========================================
# KEY LEARNINGS
# =========================================

# List           = ordered, mutable collection
# list[i]        = access by index
# list[a:b]      = slice (get a portion)
# append()       = add to end
# insert(i, v)   = add at position i
# remove(v)      = remove first occurrence of v
# pop(i)         = remove and return item at index i
# len()          = count items
# sort()         = sort in place (modifies original)
# sorted()       = returns new sorted list (safe)
# reverse()      = reverse in place
# max/min/sum()  = built-in aggregations
# in             = check if value exists
# 2D list        = list of lists = tabular data
# enumerate()    = loop with index + value together
