# =========================================
# Day 3 - If / Else / Elif / Nested If
# =========================================

# -----------------------------------------
# THEORY:
# if → runs when condition is True
# else → runs when condition is False
# elif → used for multiple conditions
# nested if → if inside another if
# -----------------------------------------


# -----------------------------------------
# Basic If (Nested Example - Cleaned)
# -----------------------------------------

age = 20

if age > 18:
    print("You are an adult")

    if age == 20:
        print("You are a young man")

# Note:
# Removed unnecessary deep nesting (bad practice)


# -----------------------------------------
# If-Else Example
# -----------------------------------------

age = 20

if age > 18:
    print("Adult")
else:
    print("Not adult")


age = 10

if age > 18:
    print("Adult")
else:
    print("Not adult")


# -----------------------------------------
# Even or Odd
# -----------------------------------------

num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# -----------------------------------------
# Salary Check
# -----------------------------------------

salary = 30000

if salary > 40000:
    print("High Salary")
else:
    print("Low Salary")


# -----------------------------------------
# Marks Example (if-elif-else)
# -----------------------------------------

marks = 75

if marks > 80:
    print("Excellent")
elif marks > 60:
    print("Good")
else:
    print("Average")


# -----------------------------------------
# Salary Level (Fixed logic)
# -----------------------------------------

salary = 60000

if salary > 60000:
    print("High")
elif salary == 60000:
    print("Good")
else:
    print("Low")


# -----------------------------------------
# Grade System
# -----------------------------------------

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# -----------------------------------------
# Age Category (FIXED LOGIC)
# -----------------------------------------

age = 35

if age < 18:
    print("Minor")
elif age <= 60:
    print("Working")
else:
    print("Senior")

# FIX:
# Your condition was wrong earlier:
# age < 18 and age > 60 ❌ (impossible)


# -----------------------------------------
# Nested If (Loan Eligibility)
# -----------------------------------------

age = 25
salary = 40000

if age >= 18:
    if salary >= 30000:
        print("Eligible for loan")


# -----------------------------------------
# Nested If with Else
# -----------------------------------------

age = 16
salary = 40000

if age >= 18:
    if salary >= 30000:
        print("Eligible")
    else:
        print("Salary low")
else:
    print("Underage")


# -----------------------------------------
# Marks + Attendance (Nested If)
# -----------------------------------------

marks = 70
attendance = 80

if marks >= 50:
    if attendance >= 75:
        print("Pass")
    else:
        print("Low attendance")
else:
    print("Fail")


# -----------------------------------------
# Login System (Nested If)
# -----------------------------------------

is_logged_in = True
is_verified = False

if is_logged_in:
    if is_verified:
        print("Access granted")
    else:
        print("Verify account")
else:
    print("Login required")