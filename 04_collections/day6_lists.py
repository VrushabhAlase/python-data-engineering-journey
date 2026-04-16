#What is a List?

# A list is a collection of values

# =========================================
# Day 6 - Lists Basics
# =========================================

# Creating a list
numbers = [10, 20, 30, 40]

names = ["Vrushabh", "Akshay", "Rohit"]

mixed = [10, "Python", True]

print(numbers)
print(names)
print(mixed)

print(numbers[0])   # 10
print(names[1])     # Akshay
print(numbers[-1])  # 40

for num in numbers:
    print(num)

cities = ["Pune", "Mumbai", "Delhi"]

for city in cities:
    print(city)