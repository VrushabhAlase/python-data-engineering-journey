"""
What is a Dictionary?
A dictionary stores data as key-value pairs. Instead of accessing data by index number like a list, you access it by a name (key).
Think of it like a real dictionary — you look up a word (key) to get its meaning (value).
"""

# List — access by index (position)
employee = ["Vrushabh", "Pune", "Data Engineer"]
print(employee[0])   # Vrushabh — you need to remember index 0 = name

# Dictionary — access by key (name)
employee = {
    "name": "Vrushabh",
    "city": "Pune",
    "role": "Data Engineer"
}
print(employee["name"])   # Vrushabh — clear and readable

#Section 1 — Creating a Dictionary

# Basic dictionary
employee = {
    "name"  : "Vrushabh",
    "city"  : "Pune",
    "role"  : "Data Engineer",
    "exp"   : 2
}

print(employee)
print(type(employee))    # <class 'dict'>

# Empty dictionary — add data later
config = {}
config["env"]    = "prod"
config["bucket"] = "my-data-lake"
print(config)    # {'env': 'prod', 'bucket': 'my-data-lake'}

#Section 2 — Accessing Values

employee = {
    "name": "Vrushabh",
    "city": "Pune",
    "role": "Data Engineer",
    "exp" : 2
}

# Method 1 — direct key access
print(employee["name"])    # Vrushabh
print(employee["role"])    # Data Engineer

# Method 2 — get() — SAFER, returns None if key missing (no error)
print(employee.get("city"))       # Pune
print(employee.get("salary"))     # None  — no crash!
print(employee.get("salary", 0))  # 0     — default value if key missing

# Why get() matters in DE:
# Source data is often incomplete — missing fields crash your pipeline
# get() with a default value keeps your pipeline running safely

#Section 3 — Add, Update, Delete

employee = {"name": "Vrushabh", "city": "Pune"}

# Add new key
employee["role"] = "Data Engineer"
employee["exp"]  = 2
print(employee)

# Update existing key
employee["city"] = "Mumbai"    # overwrites Pune
employee["exp"]  = 3
print(employee)

# Delete a key — del
del employee["exp"]
print(employee)

# Delete and return value — pop()
city = employee.pop("city")
print("Removed city:", city)    # Mumbai
print(employee)

#Section 4 — Looping through a Dictionary

employee = {
    "name": "Vrushabh",
    "city": "Pune",
    "role": "Data Engineer",
    "exp" : 2
}

# Loop through keys only
print("--- Keys ---")
for key in employee:
    print(key)

# Loop through values only
print("--- Values ---")
for value in employee.values():
    print(value)

# Loop through BOTH key and value — most useful
print("--- Key + Value ---")
for key, value in employee.items():
    print(f"{key} : {value}")

#Section 5 — Dictionary Methods

employee = {"name": "Vrushabh", "city": "Pune", "role": "Data Engineer"}

# Get all keys
print(employee.keys())      # dict_keys(['name', 'city', 'role'])

# Get all values
print(employee.values())    # dict_values(['Vrushabh', 'Pune', 'Data Engineer'])

# Get all key-value pairs
print(employee.items())     # dict_items([('name', 'Vrushabh'), ...])

# Check if key exists
print("name" in employee)      # True
print("salary" in employee)    # False

# Length — number of keys
print(len(employee))           # 3

#Section 6 — List of Dictionaries

"""
This is the most important pattern in DE. Every row in a CSV, every record from an API, every row in a database table — they all become a list of dictionaries in Python.
"""
# Each dict = one row/record
employees = [
    {"id": "EMP001", "name": "Vrushabh", "city": "Pune",   "role": "DE"},
    {"id": "EMP002", "name": "Akshay",   "city": "Mumbai", "role": "DA"},
    {"id": "EMP003", "name": "Rohit",    "city": "Delhi",  "role": "DE"},
]

# Access one record
print(employees[0])                  # first record
print(employees[0]["name"])          # Vrushabh

# Loop through all records
for emp in employees:
    print(f"{emp['id']} | {emp['name']} | {emp['city']}")

# Filter — only Data Engineers
print("\n--- Data Engineers only ---")
for emp in employees:
    if emp["role"] == "DE":
        print(emp["name"])

#Section 7 — Nested Dictionary

# A dictionary inside a dictionary
pipeline = {
    "name"   : "sales_pipeline",
    "status" : "running",
    "config" : {
        "source" : "s3://raw/sales/",
        "target" : "s3://processed/sales/",
        "format" : "parquet"
    }
}

# Access nested values
print(pipeline["name"])                      # sales_pipeline
print(pipeline["config"]["source"])          # s3://raw/sales/
print(pipeline["config"]["format"])          # parquet

# Update nested value
pipeline["config"]["format"] = "csv"
print(pipeline["config"]["format"])          # csv

#Section 8 — DE Real-World Examples
# DE Example 1: Parse a single CSV row into a dict
# In real pipelines each row from a file becomes a dict

csv_row = "EMP001,Vrushabh,Pune,DataEngineer,85000"
fields  = csv_row.split(",")

record = {
    "id"    : fields[0],
    "name"  : fields[1],
    "city"  : fields[2],
    "role"  : fields[3],
    "salary": int(fields[4])
}
print(record)
print(f"Name: {record['name']} | Salary: {record['salary']:,}")


# DE Example 2: Pipeline config dictionary
# Real Glue/Airflow jobs use config dicts like this

config = {
    "env"        : "prod",
    "source"     : "s3://raw-bucket/sales/2024/",
    "target"     : "s3://processed-bucket/sales/2024/",
    "file_format": "parquet",
    "partition"  : "date"
}

print(f"\nRunning pipeline in {config['env']} env")
print(f"Reading from  : {config['source']}")
print(f"Writing to    : {config['target']}")
print(f"Output format : {config['file_format']}")


# DE Example 3: Count records per region (aggregation)
# This is what GROUP BY does in SQL — replicate it in Python

records = [
    {"region": "North", "sales": 1500},
    {"region": "South", "sales": 800},
    {"region": "North", "sales": 2000},
    {"region": "East",  "sales": 1200},
    {"region": "South", "sales": 900},
]

region_totals = {}

for record in records:
    region = record["region"]
    sales  = record["sales"]
    if region in region_totals:
        region_totals[region] += sales     # add to existing
    else:
        region_totals[region] = sales      # first time — create key

print("\n--- Sales by Region ---")
for region, total in region_totals.items():
    print(f"{region}: {total:,}")


# DE Example 4: Schema validation
# Check incoming data has all required fields before processing

required_fields = ["id", "name", "city", "role"]

incoming = {"id": "EMP004", "name": "Sneha", "role": "DE"}   # missing city!

missing = []
for field in required_fields:
    if field not in incoming:
        missing.append(field)

if missing:
    print(f"\nSchema error — missing fields: {missing}")
else:
    print("\nRecord is valid — proceed to pipeline")


data = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 90}
]

for std in data:
    if std["marks"] > 70:
        print(std["name"])