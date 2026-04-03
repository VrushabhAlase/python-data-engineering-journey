# =========================================
# Day 2 - Operators (Arithmetic + Comparison + Logical)
# =========================================

# -----------------------------------------
# THEORY
# -----------------------------------------
# Arithmetic Operators:
# +  → addition
# -  → subtraction
# *  → multiplication
# /  → division
# %  → remainder (used to check even/odd)
# ** → power

# Comparison Operators:
# == → equal to
# != → not equal
# >  → greater than
# <  → less than
# >= → greater than or equal
# <= → less than or equal

# Logical Operators:
# and → both conditions must be True
# or  → at least one condition must be True
# not → reverses True/False

# -----------------------------------------
# Logical Operators Examples
# -----------------------------------------

age = 25
print("\n--- AND Example ---")
print("Eligible for job?", age > 18 and age < 60)


salary = 20000
print("\n--- OR Example ---")
print("Eligible for loan?", salary > 50000 or salary > 15000)


is_student = False
print("\n--- NOT Example ---")
print("Is not student?", not is_student)


# -----------------------------------------
# Practice Examples
# -----------------------------------------

age = 20
print("\n--- Age Check ---")
print("Eligible for job?", age > 18 and age < 60)


marks = 35
print("\n--- Pass Check ---")
print("Passed?", marks >= 40)


salary = 40000
print("\n--- Salary Range ---")
print("Within salary range?", salary > 30000 and salary < 100000)


num = 10
print("\n--- Even & Greater than 5 ---")
print("Is even and greater than 5?", num % 2 == 0 and num > 5)


# -----------------------------------------
# Real-World Scenarios
# -----------------------------------------

# Login System
is_logged_in = True
is_verified = True
print("\n--- Login Check ---")
print("Can access system?", is_logged_in and is_verified)


# Discount Eligibility
price = 1200
print("\n--- Discount Check ---")
print("Eligible for discount?", price > 1000)


# Distinction Check
marks = 75
print("\n--- Distinction Check ---")
print("Passed with distinction?", marks > 70)


# Valid Number Check
num = 20
print("\n--- Number Validation ---")
print("Valid number?", num % 2 == 0 and num % 5 == 0)


# Salary Range Check
salary = 50000
print("\n--- Expected Salary Range ---")
print("Within expected range?", salary > 30000 and salary < 70000)