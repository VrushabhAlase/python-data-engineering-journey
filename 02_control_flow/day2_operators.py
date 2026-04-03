# =========================================
# Day 2 - Arithmetic Operators
# =========================================

# -----------------------------------------
# THEORY: Arithmetic Operators
# -----------------------------------------
# Arithmetic operators are used to perform mathematical operations.

# +  → Addition (adds two numbers)
# -  → Subtraction (difference between numbers)
# *  → Multiplication (product of numbers)
# /  → Division (gives decimal result)
# %  → Modulus (gives remainder)
# ** → Power (exponent)

# Example:
# 10 + 5 = 15
# 10 / 3 = 3.33
# 10 % 3 = 1  (remainder)


# -----------------------------------------
# Example 1
# -----------------------------------------

a = 10
b = 3

print("\n--- Example 1 ---")
print("Addition:", a + b)          # 10 + 3 = 13
print("Subtraction:", a - b)       # 10 - 3 = 7
print("Multiplication:", a * b)    # 10 * 3 = 30
print("Division:", a / b)          # 10 / 3 = 3.33 (float)
print("Modulus (remainder):", a % b)  # 10 % 3 = 1


# -----------------------------------------
# Example 2
# -----------------------------------------

a = 200
b = 35

print("\n--- Example 2 ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus (remainder):", a % b)


# -----------------------------------------
# Power Operations
# -----------------------------------------

num = 33

print("\n--- Power Operations ---")
print("Square (num^2):", num ** 2)   # 33 * 33
print("Cube (num^3):", num ** 3)     # 33 * 33 * 33
print("Double (num*2):", num * 2)


# -----------------------------------------
# Practice Example
# -----------------------------------------

num = 15

print("\n--- Practice Example ---")
print("Double:", num * 2)
print("Square:", num ** 2)


# -----------------------------------------
# Additional Examples
# -----------------------------------------

x = 20
y = 5

print("\n--- Additional Example ---")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)


# -----------------------------------------
# IMPORTANT CONCEPTS
# -----------------------------------------

# 1. Division always gives float
print("\n--- Division Behavior ---")
print(10 / 2)   # 5.0 (float)


# 2. Integer division (floor division)
# // removes decimal part
print("\n--- Floor Division ---")
print(10 // 3)  # 3 (not 3.33)


# 3. Modulus use case (even/odd check)
print("\n--- Even Check Example ---")
num = 10
print("Is even?", num % 2 == 0)


# 4. Real-life example (money split)
print("\n--- Real-Life Example ---")
money = 105
people = 10

print("Each person gets:", money // people)
print("Remaining money:", money % people)