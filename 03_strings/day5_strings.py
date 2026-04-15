# =========================================
# Day 5 - Strings (Complete)
# =========================================

# -----------------------------------------
# Section 1 — What is a String?
# -----------------------------------------

name = "vrushabh"
city = "Pune"
job = 'Data Engineer'

# Single / Double quotes
first_name = "Akshay"
last_name  = 'Patil'

# Multi-line string
about = """
I am learning Python.
My goal is AWS Data Engineer.
"""

# String vs Number
emp_id = "EMP001"
print(type(emp_id))   # str

emp_id = 11
print(type(emp_id))   # int


# -----------------------------------------
# Section 2 — Length & Indexing
# -----------------------------------------

name = "Vrushabh"

print(len(name))      # length

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
print(name[5])


# -----------------------------------------
# Section 3 — Looping through String
# -----------------------------------------

print("\n--- Loop using index ---")
for i in range(len(name)):
    print(name[i])

print("\n--- Loop using slicing ---")
for ch in name[0:8]:
    print(ch)

print("\n--- Direct loop (Best Practice) ---")
for ch in name:
    print(ch)


# -----------------------------------------
# Section 4 — Slicing
# -----------------------------------------

print(name[0:4])
print(name[2:6])
print(name[:4])
print(name[4:])
print(name[:])


# -----------------------------------------
# Section 5 — String Methods
# -----------------------------------------

text = "  hello data engineer  "

print(text.upper())
print(text.lower())
print(text.title())

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.strip().startswith("hello"))
print(text.strip().endswith("engineer"))

sentence = "data engineer works with data"
print(sentence.count("data"))
print(sentence.find("engineer"))


# -----------------------------------------
# Section 6 — Replace & Split
# -----------------------------------------

filename = "sales_data_2024.CSV"
clean = filename.replace(".CSV", ".csv")
print(clean)

filename = "Data_engineering_students_2026.sql"
clean = filename.replace(".sql", ".SQL")
print(clean)

csv_row = "Vrushabh,Pune,DataEngineer,AWS"
fields = csv_row.split(",")
print(fields)

print(fields[0])
print(fields[2])

sentence = "I love data engineering"
words = sentence.split()
print(words)


# -----------------------------------------
# Section 7 — f-Strings
# -----------------------------------------

name = "Vrushabh"
day = 5
topic = "Strings"

print(f"Day {day}: {topic}")
print(f"Hello {name}, today we are learning {topic}!")

records = 1500
print(f"Total records processed: {records:,}")
print(f"Pipeline success rate: {95.678:.2f}%")


# -----------------------------------------
# Section 8 — Real Data Engineering Examples
# -----------------------------------------

# Clean column name
raw_header = "  Customer Name  "
clean = raw_header.strip().lower().replace(" ", "_")
print(clean)

# Extract date from filename
filename = "sales_report_2024_04_14.csv"
parts = filename.replace(".csv", "").split("_")
date_str = f"{parts[2]}-{parts[3]}-{parts[4]}"
print(date_str)

# Build S3 path
bucket = "my-data-lake"
env = "prod"
date = "2024-04-14"
path = f"s3://{bucket}/{env}/sales/{date}/data.parquet"
print(path)

# File type check
file = "customers.csv"

if file.endswith(".csv"):
    print(f"Processing CSV: {file}")
elif file.endswith(".parquet"):
    print(f"Processing Parquet: {file}")
else:
    print(f"Unknown format: {file}")

    