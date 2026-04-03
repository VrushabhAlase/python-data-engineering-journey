# =========================================
# Day 2 - Comparison Operators Practice
# =========================================

# -----------------------------------------
# THEORY: Comparison Operators
# -----------------------------------------
# Comparison operators are used to compare two values.
# The result is always Boolean: True or False

# ==  → equal to
# !=  → not equal
# >   → greater than
# <   → less than
# >=  → greater than or equal
# <=  → less than or equal

# Example:
# 10 > 5 → True
# 10 == 5 → False


# -----------------------------------------
# Basic Comparison
# -----------------------------------------

a = 10
b = 5

print("\n--- Basic Comparison ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# -----------------------------------------
# Equal Values Example
# -----------------------------------------

x = 20
y = 20

print("\n--- Equal Values ---")
print("x == y:", x == y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


# -----------------------------------------
# Age Comparison (Real-world Example)
# -----------------------------------------

vrushabh_age = 30
akshay_age = 33

print("\n--- Age Comparison ---")
print("Is Akshay older than Vrushabh?", akshay_age > vrushabh_age)
print("Is Akshay younger than Vrushabh?", akshay_age < vrushabh_age)


# -----------------------------------------
# Modulus Operator (%) - Even / Odd
# -----------------------------------------
# % gives remainder after division

# If remainder is 0 → number is even
# If remainder is not 0 → number is odd

num = 10
print("\n--- Even Check ---")
print("Is number even?", num % 2 == 0)

num = 17
print("\n--- Odd Check ---")
print("Is number odd?", num % 2 != 0)


# -----------------------------------------
# Greater Number Check
# -----------------------------------------

a = 50
b = 20

print("\n--- Greater Number ---")
print("Is A greater than B?", a > b)

