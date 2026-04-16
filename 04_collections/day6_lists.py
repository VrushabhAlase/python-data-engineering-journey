# =========================================
# Day 6 - Lists (Complete)
# =========================================

# -----------------------------------------
# What is a List?
# -----------------------------------------
# A list is a collection of multiple values
# It can store numbers, strings, or mixed data

numbers = [10, 20, 30, 40]
names = ["Vrushabh", "Akshay", "Rohit"]
mixed = [10, "Python", True]

print(numbers)
print(names)
print(mixed)

# -----------------------------------------
# Accessing Elements (Indexing)
# -----------------------------------------
# Index starts from 0

print(numbers[0])   # 10 (first element)
print(names[1])     # Akshay
print(numbers[-1])  # 40 (last element)

# -----------------------------------------
# Looping through list
# -----------------------------------------

print("\n--- Loop through numbers ---")
for num in numbers:
    print(num)

cities = ["Pune", "Mumbai", "Delhi"]

print("\n--- Loop through cities ---")
for city in cities:
    print(city)


# =========================================
# Section 2: List Operations
# =========================================

# In Data Engineering:
# - Add records
# - Remove bad data
# - Update values

numbers = [10, 20, 30, 50, 60, 70, 80]

# -----------------------------------------
# Add elements → append()
# -----------------------------------------
numbers.append(40)     # adds at end
numbers.append(100)
print("\nAfter append:", numbers)

# -----------------------------------------
# Insert at specific position → insert(index, value)
# -----------------------------------------
numbers.insert(1, 15)
numbers.insert(5, 90)
print("After insert:", numbers)

# -----------------------------------------
# Remove element by value → remove()
# -----------------------------------------
numbers.remove(90)
numbers.remove(40)
print("After remove:", numbers)

# -----------------------------------------
# Insert again (practice)
# -----------------------------------------
numbers.insert(4, 40)
numbers.insert(9, 90)
print("After re-insert:", numbers)

# -----------------------------------------
# Remove using index → pop()
# -----------------------------------------
numbers.pop(1)   # removes index 1
numbers.pop(3)   # removes index 3
print("After pop:", numbers)

# -----------------------------------------
# Length of list
# -----------------------------------------
print("Length:", len(numbers))

# -----------------------------------------
# Check existence
# -----------------------------------------
print(10 in numbers)   # True
print(99 in numbers)   # False


# =========================================
# Sorting and Reversing
# =========================================

nums = [5, 2, 9, 1]

nums.sort()       # ascending
print("\nSorted:", nums)

nums.reverse()    # reverse order
print("Reversed:", nums)


# =========================================
# Practice Example
# =========================================

names = ["A", "B", "C"]

# Add "D"
names.append("D")

# Insert "X" at index 1
names.insert(1, "X")

# Remove "B"
names.remove("B")

print("\nFinal names list:", names)

# Optional: sort + reverse
names.sort()
print("Sorted:", names)

names.reverse()
print("Reversed:", names)


# =========================================
# Find Maximum Value (Important Logic)
# =========================================

nums = [10, 50, 20, 80, 30]

# Assume first value is max
max_num = nums[0]

# Compare each value
for num in nums:
    if num > max_num:
        max_num = num

print("\nMaximum:", max_num)

# Check type
print("Type of max_num:", type(max_num))


# =========================================
# KEY LEARNINGS
# =========================================

# List = collection of values
# Indexing = access elements
# append() = add element
# insert() = add at position
# remove() = remove by value
# pop() = remove by index
# sort() = arrange values
# reverse() = reverse list
# Loop + condition = logic building (important)