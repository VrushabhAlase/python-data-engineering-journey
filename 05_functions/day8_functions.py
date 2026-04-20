# =========================================
# Day 7 - Functions (Basics)
# =========================================

"""
What is a Function?

A function is a reusable block of code.
Instead of writing the same code again and again,
you define it once and use it multiple times.
"""

# -----------------------------------------
# Basic Function
# -----------------------------------------

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
# Function with Return (IMPORTANT)
# -----------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# -----------------------------------------
# Function returning string
# -----------------------------------------

def get_full_name(first, last):
    return first + " " + last

full_name = get_full_name("Vrushabh", "Alase")
print("Full Name:", full_name)


# =========================================
# Practice Functions
# =========================================

# -----------------------------------------
# 1. Check Even Number
# -----------------------------------------

def check_even_number(num):
    return num % 2 == 0

print("Is Even:", check_even_number(10))


# -----------------------------------------
# 2. Calculate Square
# -----------------------------------------

def calculate_square(num):
    return num * num

print("Square:", calculate_square(10))


# -----------------------------------------
# 3. Maximum of Two Numbers
# -----------------------------------------

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", max_of_two(10, 20))


# =========================================
# Key Learnings
# =========================================

# def → define function
# parameters → input to function
# return → gives result back
# functions help in code reusability


#Step 2: Advanced Functions
#🧠 1. Default Parameters

#👉 You can give default values

def greet(name="Guest"):
    print("Hello", name)

greet("Vrushabh")
greet()

#🧠 2. Multiple Return Values

#👉 Function can return more than one value

def calculate(a, b):
    return a + b, a - b

sum_val, diff_val = calculate(10, 5)

print("Sum:", sum_val)
print("Difference:", diff_val)



#🧠 3. Function Inside Loop (VERY IMPORTANT)

def check_even(num):
    return num % 2 == 0

nums = [10, 15, 20, 25]

for n in nums:
    if check_even(n):
        print(n, "is even")

#🧠 4. Function with Dictionary (Real DE)

def get_salary(record):
    return record.get("salary", 0)

emp = {"name": "John", "salary": 50000}

print(get_salary(emp))

def get_salaried_person_name(record):
    return record.get("name", 0)

emp = {"name": "John", "salary": 50000}

print(get_salaried_person_name(emp))

#🧠 5. Real ETL Style Function 🔥

def clean_name(name):
    return name.strip().lower().replace(" ", "_")

print(clean_name("  Data Engineer  "))