#What is a String?
#A string is simply text. Any time you wrap characters in quotes, Python treats it as a string.

name = "vrushabh"
city = "Pune"
job = 'Data Engineer'

# Single and double quotes — same thing
first_name = "Akshay"
last_name  = 'patil'

# Multi-line string — use triple quotes
about = """
I am learning Python.
My goal is AWS Data Engineer.
"""

# String with a number inside — still a string!
emp_id = "EMP001"
print(type(emp_id))   # <class 'str'>

emp_id = 11           
print(type(emp_id))   # <class 'int'>

#Section 2 — String Length & Indexing
#Think of a string as a row of boxes, each box holding one character, numbered from 0

#V  r  u  s  h  a  b  h
#0  1  2  3  4  5  6  7

name = "Vrushabh"

print(len(name))      # 8  → total characters

print(name[0])        # V  → first character
print(name[1])        # r  → second character
print(name[-1])       # h  → last character (negative = from end)
print(name[-2])       # b  → second from last
print(name[-5])
print(name[-7])
print(name[5])

print ("String with loop")
name = "vrushabh"

for i in range(0, 8):
    print(name[i])

for ch in name[0:8]:
    print(ch)

for ch in name:
    print(ch)

for zx in name[5:7]:
    print(zx)

# Syntax: string[start : stop]   (stop is excluded)

name = "Vrushabh"

print(name[0:4])    # Vrus  → index 0,1,2,3
print(name[2:6])    # ushab
print(name[0:3])    # Vru

# Shortcuts
print(name[:4])     # Vrus  → from beginning to index 4
print(name[4:])     # habh  → from index 4 to end
print(name[:])      # Vrushabh → full string

#Section 4 — String Methods (the real power)
#Methods are built-in actions you can perform on a string. You call them with a dot .

text = "  hello data engineer  "

# Case methods
print(text.upper())       # HELLO DATA ENGINEER
print(text.lower())       # hello data engineer
print(text.title())       # Hello Data Engineer

# Clean whitespace
print(text.strip())       # "hello data engineer"  → removes spaces from both ends
print(text.lstrip())      # removes left spaces only
print(text.rstrip())      # removes right spaces only

# Check content
print(text.strip().startswith("hello"))   # True
print(text.strip().endswith("engineer"))  # True

# Count and find
sentence = "data engineer works with data"
print(sentence.count("data"))     # 2  → how many times "data" appears
print(sentence.find("engineer"))  # 5  → index where "engineer" starts


#Section 5 — Replace & Split (most used in DE!)

# replace(old, new)
filename = "sales_data_2024.CSV"
clean = filename.replace(".CSV", ".csv")
print(clean)    # sales_data_2024.csv

filename = "Data_engineering_stundets_2026.sql"
clean = filename.replace(".sql",".SQL")
print(clean)

# split(separator) — breaks string into a LIST
csv_row = "Vrushabh,Pune,DataEngineer,AWS"
fields = csv_row.split(",")
print(fields)
# ['Vrushabh', 'Pune', 'DataEngineer', 'AWS']

print(fields[0])   # Vrushabh
print(fields[2])   # DataEngineer

# split by space (default)
sentence = "I love data engineering"
words = sentence.split()
print(words)   # ['I', 'love', 'data', 'engineering']


#Section 6 — f-strings (modern way to format strings)
#f-strings let you embed variables directly inside a string. Used everywhere — log messages, file paths, SQL queries.

name   = "Vrushabh"
day    = 4
topic  = "Strings"

# Old way (messy)
print("Day " + str(day) + ": " + topic)

# f-string way (clean and readable)
print(f"Day {day}: {topic}")
print(f"Hello {name}, today we are learning {topic}!")

# With expressions inside
records = 1500
print(f"Total records processed: {records:,}")    # 1,500
print(f"Pipeline success rate: {95.678:.2f}%")    # 95.68%
