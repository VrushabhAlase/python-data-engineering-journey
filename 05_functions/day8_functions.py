"""
What is a Function?

👉 A function is a reusable block of code

👉 Instead of writing same code again & again
👉 You define once → use many times
"""
def greet():
    print("Hello, welcome to Python")

greet()

"""
def      → define function  
greet    → function name  
()       → parameters (empty for now)  
:        → start of block  

"""

#Function with Parameters

#👉 Now pass values

def greet(name):
    print("Hello", name)

greet("Vrushabh")
greet("Akshay")


#🔹 Function with Return (VERY IMPORTANT)

#👉 Return gives result back

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def get_full_name(first, last):
    return first + " " + last

name = get_full_name("Vrushabh", "Alase")
print(name)

# 1. Function to check even number
# input: number
# output: True/False

# 2. Function to calculate square

# 3. Function to return max of two numbers

def check_even_number (num):
    return num%2== 0
result = check_even_number(10)
print (result)

def calculate_square (num):
    return num*num
result = calculate_square(10)
print (result)

def max_of_two(a, b):
    if  a>b :
      return a
    else:
      return b

result = max_of_two(10, 20)
print(result)





    
