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