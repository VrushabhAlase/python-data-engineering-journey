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

"""
Step 2: List Operations
  Why this matters

  In Data Engineering you:

add records
remove bad data
update values
"""

numbers = [10, 20, 30,50,60,70,80]

numbers.append(40)

print(numbers)

numbers.append(100)

print(numbers)

numbers.insert(1, 15)

print(numbers)

numbers.insert(5, 90)

print(numbers)

numbers.remove(90)

print(numbers)

numbers.remove(40)

print(numbers)

numbers.insert(4, 40)

print(numbers)

numbers.insert(9, 90)

print(numbers)

numbers.pop(1)

print(numbers)

numbers.pop(3)

print(numbers)

