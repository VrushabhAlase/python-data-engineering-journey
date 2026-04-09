# =========================================
# Day 4 - Loops in Python
# =========================================

# -----------------------------------------
# THEORY: Loops
# -----------------------------------------
# Loops are used to repeat a block of code multiple times.
#
# Two types of loops in Python:
# 1. for loop  → used when you know how many times to repeat
# 2. while loop → used when you repeat until a condition becomes False
#
# range(start, stop, step):
#   start → where to begin (default 0)
#   stop  → where to stop (excluded)
#   step  → jump by how much (default 1)
#
# Example:
#   range(1, 6)  → 1, 2, 3, 4, 5
#   range(5)     → 0, 1, 2, 3, 4
#   range(0, 10, 2) → 0, 2, 4, 6, 8


# =========================================
# SECTION 1: Basic for Loop with range()
# =========================================

print("\n--- Example 1: Numbers 1 to 5 ---")
for i in range(1, 6):
    print(i)

print("\n--- Example 2: Numbers 1 to 8 ---")
for i in range(1, 9):
    print(i)

print("\n--- Example 3: Numbers 5 to 14 ---")
for i in range(5, 15):
    print(i)

print("\n--- Example 4: Numbers 0 to 4 (range with single value) ---")
# range(5) starts from 0 by default
for i in range(5):
    print(i)

print("\n--- Example 5: Numbers 1 to 3 ---")
for i in range(1, 4):
    print(i)

print("\n--- Example 6: Numbers 0 to 7 ---")
for i in range(8):
    print(i)

print("\n--- Example 7: Numbers 3 to 8 ---")
for i in range(3, 9):
    print(i)


# =========================================
# SECTION 2: for Loop with if Condition
# =========================================

# -----------------------------------------
# Even Numbers (1 to 10)
# -----------------------------------------
# A number is even if remainder after dividing by 2 is 0

print("\n--- Even Numbers (1 to 10) ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# -----------------------------------------
# Odd Numbers (1 to 10)
# -----------------------------------------
# A number is odd if remainder after dividing by 2 is not 0

print("\n--- Odd Numbers (1 to 10) ---")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)


# -----------------------------------------
# Numbers Greater Than 5 (1 to 10)
# -----------------------------------------

print("\n--- Numbers Greater Than 5 (1 to 10) ---")
for i in range(1, 11):
    if i > 5:
        print(i)


# -----------------------------------------
# Numbers Greater Than 8 (5 to 14)
# -----------------------------------------

print("\n--- Numbers Greater Than 8 (5 to 14) ---")
for i in range(5, 15):
    if i > 8:
        print(i)


# -----------------------------------------
# Numbers Divisible by 3 (1 to 19)
# -----------------------------------------
# A number is divisible by 3 if remainder is 0

print("\n--- Numbers Divisible by 3 (1 to 19) ---")
for i in range(1, 20):
    if i % 3 == 0:
        print(i)


# -----------------------------------------
# Numbers Between 10 and 20 (exclusive)
# -----------------------------------------
# Using and operator to combine two conditions

print("\n--- Numbers Between 10 and 20 (exclusive) ---")
for i in range(10, 20):
    if i > 10 and i < 20:
        print(i)


# -----------------------------------------
# Squares of Even Numbers (1 to 10)
# -----------------------------------------
# Square means number multiplied by itself
# Example: square of 4 = 4 * 4 = 16

print("\n--- Squares of Even Numbers (1 to 10) ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} x {i} = {i * i}")


# =========================================
# SECTION 3: Bonus for Loop Examples
# =========================================

# -----------------------------------------
# Multiplication Table (for DE interviews)
# -----------------------------------------

print("\n--- Multiplication Table of 5 ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# -----------------------------------------
# Skip a number using continue
# -----------------------------------------
# continue → skips current iteration and moves to next

print("\n--- Numbers 1 to 10, Skip 5 ---")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# -----------------------------------------
# Stop loop early using break
# -----------------------------------------
# break → exits the loop immediately

print("\n--- Stop loop when number reaches 6 ---")
for i in range(1, 11):
    if i == 6:
        break
    print(i)


# =========================================
# SECTION 4: while Loop
# =========================================

# -----------------------------------------
# THEORY: while Loop
# -----------------------------------------
# while loop keeps running as long as condition is True
# IMPORTANT: always update the variable inside loop
#            otherwise it runs forever (infinite loop)
#
# Syntax:
#   i = 1
#   while i <= 5:
#       print(i)
#       i += 1   ← this is critical!


# -----------------------------------------
# Basic while Loop (Count Up)
# -----------------------------------------

print("\n--- While Loop: Count 1 to 5 ---")
i = 1
while i <= 5:
    print(i)
    i += 1      # i = i + 1 (increment)


# -----------------------------------------
# Count Down using while
# -----------------------------------------

print("\n--- While Loop: Count Down 10 to 1 ---")
i = 10
while i >= 1:
    print(i)
    i -= 1      # i = i - 1 (decrement)


# -----------------------------------------
# Print Multiples of 3 using while (1 to 10)
# -----------------------------------------

print("\n--- While Loop: Multiples of 3 (1 to 10) ---")
i = 1
while i <= 10:
    if i % 3 == 0:
        print(i)
    i += 1


# =========================================
# SECTION 5: Sum Calculations (Real DE Use)
# =========================================

# -----------------------------------------
# Sum of Numbers 1 to 10
# -----------------------------------------
# This is a very common pattern in data pipelines
# Used to aggregate/total up values

print("\n--- Sum of Numbers 1 to 10 ---")
total = 0
for i in range(1, 11):
    total = total + i   # keep adding each number to total

print("Sum:", total)    # Expected: 55


# -----------------------------------------
# Running Total (shows sum after each step)
# -----------------------------------------
# This helps you see how the total builds up
# Very useful for understanding aggregation in DE

print("\n--- Running Total (1 to 5) ---")
total = 0
for i in range(1, 6):
    total = total + i
    print(f"After adding {i} → Total: {total}")


# =========================================
# SECTION 6: Real-World DE Mini Challenge
# =========================================

# -----------------------------------------
# Scenario: Validate a batch of records
# -----------------------------------------
# In real data pipelines, you loop through records
# and check each one for validity

print("\n--- DE Mini Challenge: Record Validator ---")

record_counts = [1500, 0, 800, 2500, 300]   # list of daily record counts

for count in record_counts:
    if count == 0:
        print(f"Count: {count} → ALERT: Empty batch!")
    elif count < 500:
        print(f"Count: {count} → WARNING: Low record count")
    elif count > 2000:
        print(f"Count: {count} → WARNING: Unusually high count")
    else:
        print(f"Count: {count} → OK")