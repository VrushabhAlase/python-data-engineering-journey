# =========================================
# Day 1 - Variables and Data Types
# =========================================

# -----------------------------------------
# THEORY: Variables
# -----------------------------------------
# A variable is a container used to store data.
# Example:
# a = 10 → 'a' stores value 10

# Rules:
# - Variable names should be lowercase (best practice)
# - Use snake_case (e.g., total_salary)
# - No spaces allowed
# - Should not start with numbers


# -----------------------------------------
# THEORY: Data Types
# -----------------------------------------
# Python has different types of data:

# int    → Whole numbers (10, 20)
# float  → Decimal numbers (10.5, 99.99)
# str    → Text ("Hello", "Python")
# bool   → True or False


# -----------------------------------------
# Basic Variables
# -----------------------------------------

a = 10
b = 20

name = "Vrushabh"
is_learning = True

print("\n--- Basic Variables ---")
print("Sum:", a + b)
print("Name:", name)
print("Is Learning:", is_learning)

# type() function is used to check data type
print("Type of a:", type(a))
print("Type of name:", type(name))


# -----------------------------------------
# More Variable Examples
# -----------------------------------------

# Integer (whole numbers)
age = 25
vay = 26

# Float (decimal numbers)
salary = 50000.75
pagar = 44000.50

# String (text)
city = "Pune"
gaw = "Kolhapur"
gender = "Male"

# Boolean (True/False)
is_working = True
kam_suru_ahe = True


# -----------------------------------------
# Printing Values
# -----------------------------------------

print("\n--- Variable Values ---")
print("Age:", age)
print("Salary:", salary)
print("City:", city)
print("Is Working:", is_working)

print("Vay:", vay)
print("Pagar:", pagar)
print("Gaw:", gaw)
print("Kam Suru Ahe:", kam_suru_ahe)
print("Gender:", gender)


# -----------------------------------------
# Checking Data Types
# -----------------------------------------

print("\n--- Variable Types ---")
print(type(age))        # int
print(type(salary))     # float
print(type(city))       # string
print(type(is_working)) # boolean

print(type(vay))
print(type(pagar))
print(type(gaw))
print(type(kam_suru_ahe))


# =========================================
# Homework Section
# =========================================

# -----------------------------------------
# Task 1: Person Profile
# -----------------------------------------
# Creating variables to store personal details

person_name = "Akshay Patil"
person_age = 30
person_city = "Kolhapur"
person_is_working = True
person_salary = 1000001.1

print("\n--- Person Details ---")
print("Person Name:", person_name)
print("Person Age:", person_age)
print("Person City:", person_city)
print("Person Is Working:", person_is_working)
print("Person Salary:", person_salary)


# -----------------------------------------
# Task 2: Salary Calculation
# -----------------------------------------
# Performing arithmetic operation using variables

salary = 44000
bonus = 10000

print("\n--- Salary Calculation ---")
print("Total Salary:", salary + bonus)


# -----------------------------------------
# Task 3: Boolean Example
# -----------------------------------------
# Boolean values are used for decision making

is_student = False
is_employee = True

print("\n--- Boolean Check ---")
print("Am I Earning:", is_employee)
print("Am I Studying:", is_student)