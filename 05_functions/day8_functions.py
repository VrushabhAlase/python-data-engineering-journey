# =========================================
# Day 7 - Functions (Complete)
# =========================================

"""
What is a Function?

A function is a reusable block of code.
Define once → use multiple times.
"""

# =========================================
# Section 1 — Basic Functions
# =========================================

def greet():
    print("Hello, welcome to Python")

greet()


# -----------------------------------------
# Function with Parameters
# -----------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Vrushabh")
greet_user("Akshay")


# -----------------------------------------
# Function with Return
# -----------------------------------------

def add(a, b):
    return a + b

print("Sum:", add(10, 20))


# -----------------------------------------
# Function returning string
# -----------------------------------------

def get_full_name(first, last):
    return first + " " + last

print("Full Name:", get_full_name("Vrushabh", "Alase"))


# =========================================
# Section 2 — Practice Functions
# =========================================

# Even number check
def check_even_number(num):
    return num % 2 == 0

print("Is Even:", check_even_number(10))


# Square calculation
def calculate_square(num):
    return num * num

print("Square:", calculate_square(10))


# Maximum of two numbers
def max_of_two(a, b):
    return a if a > b else b

print("Maximum:", max_of_two(10, 20))


# =========================================
# Section 3 — Advanced Functions
# =========================================

# -----------------------------------------
# Default Parameters
# -----------------------------------------

def greet_default(name="Guest"):
    print("Hello", name)

greet_default("Vrushabh")
greet_default()


# -----------------------------------------
# Multiple Return Values
# -----------------------------------------

def calculate_operations(a, b):
    return a + b, a - b

sum_val, diff_val = calculate_operations(10, 5)

print("Sum:", sum_val)
print("Difference:", diff_val)


# -----------------------------------------
# Function inside loop
# -----------------------------------------

def is_even(num):
    return num % 2 == 0

nums = [10, 15, 20, 25]

print("\n--- Even Numbers ---")
for n in nums:
    if is_even(n):
        print(n)


# -----------------------------------------
# Function with Dictionary (Real DE)
# -----------------------------------------

def get_salary(record):
    return record.get("salary", 0)

def get_name(record):
    return record.get("name", "NA")

emp = {"name": "John", "salary": 50000}

print("Salary:", get_salary(emp))
print("Name:", get_name(emp))


# -----------------------------------------
# ETL Style Function
# -----------------------------------------

def clean_name(name):
    return name.strip().lower().replace(" ", "_")

print("Clean Name:", clean_name("  Data Engineer  "))


# =========================================
# Section 4 — Practice Tasks
# =========================================

# Task 1: High / Low
def check_value(num):
    return "High" if num > 50 else "Low"

print(check_value(70))
print(check_value(30))


# Task 2: Sum of list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("List Sum:", sum_list([1, 2, 3, 4]))


# Task 3: Dictionary details
def get_details(data):
    name = data.get("name", "NA")
    city = data.get("city", "NA")
    return f"{name} - {city}"

person = {"name": "Vrushabh", "city": "Pune"}
print("Details:", get_details(person))


# =========================================
# Key Learnings
# =========================================

# def → define function
# parameters → input values
# return → output result
# default params → optional inputs
# multiple return → tuple unpacking
# functions + loops → data processing
# functions + dict → real-world ETL logic