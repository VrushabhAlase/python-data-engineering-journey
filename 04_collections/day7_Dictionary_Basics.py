# =========================================
# Day 6 - Dictionary (Complete Guide)
# =========================================

# -----------------------------------------
# What is a Dictionary?
# -----------------------------------------
# A dictionary stores data as key-value pairs
# Key → value mapping (like JSON / API response)

# List example (index-based)
employee_list = ["Vrushabh", "Pune", "Data Engineer"]
print(employee_list[0])   # need to remember index

# Dictionary example (key-based)
employee_dict = {
    "name": "Vrushabh",
    "city": "Pune",
    "role": "Data Engineer"
}
print(employee_dict["name"])   # clear & readable


# =========================================
# Section 1 — Creating Dictionary
# =========================================

employee = {
    "name": "Vrushabh",
    "city": "Pune",
    "role": "Data Engineer",
    "exp": 2
}

print("\n--- Basic Dictionary ---")
print(employee)
print(type(employee))

# Empty dictionary
config = {}
config["env"] = "prod"
config["bucket"] = "my-data-lake"
print("\n--- Config ---")
print(config)


# =========================================
# Section 2 — Accessing Values
# =========================================

print("\n--- Access Values ---")
print(employee["name"])
print(employee["role"])

# Safe access
print(employee.get("city"))
print(employee.get("salary"))       # None
print(employee.get("salary", 0))    # default value


# =========================================
# Section 3 — Add, Update, Delete
# =========================================

employee_update = {"name": "Vrushabh", "city": "Pune"}

# Add
employee_update["role"] = "Data Engineer"
employee_update["exp"] = 2
print("\nAfter Add:", employee_update)

# Update
employee_update["city"] = "Mumbai"
employee_update["exp"] = 3
print("After Update:", employee_update)

# Delete
del employee_update["exp"]
print("After Delete:", employee_update)

# Pop
city = employee_update.pop("city")
print("Removed city:", city)
print(employee_update)


# =========================================
# Section 4 — Looping Dictionary
# =========================================

print("\n--- Keys ---")
for key in employee:
    print(key)

print("\n--- Values ---")
for value in employee.values():
    print(value)

print("\n--- Key + Value ---")
for key, value in employee.items():
    print(f"{key} : {value}")


# =========================================
# Section 5 — Dictionary Methods
# =========================================

print("\n--- Methods ---")
print(employee.keys())
print(employee.values())
print(employee.items())

print("name" in employee)
print("salary" in employee)

print("Length:", len(employee))


# =========================================
# Section 6 — List of Dictionaries
# =========================================

employees = [
    {"id": "EMP001", "name": "Vrushabh", "city": "Pune", "role": "DE"},
    {"id": "EMP002", "name": "Akshay", "city": "Mumbai", "role": "DA"},
    {"id": "EMP003", "name": "Rohit", "city": "Delhi", "role": "DE"},
]

print("\n--- First Record ---")
print(employees[0])
print(employees[0]["name"])

print("\n--- All Employees ---")
for emp in employees:
    print(f"{emp['id']} | {emp['name']} | {emp['city']}")

print("\n--- Data Engineers Only ---")
for emp in employees:
    if emp["role"] == "DE":
        print(emp["name"])


# =========================================
# Section 7 — Nested Dictionary
# =========================================

pipeline = {
    "name": "sales_pipeline",
    "status": "running",
    "config": {
        "source": "s3://raw/sales/",
        "target": "s3://processed/sales/",
        "format": "parquet"
    }
}

print("\n--- Nested Dictionary ---")
print(pipeline["name"])
print(pipeline["config"]["source"])

pipeline["config"]["format"] = "csv"
print(pipeline["config"]["format"])


# =========================================
# Section 8 — Real Data Engineering Examples
# =========================================

# Example 1: CSV row → dictionary
csv_row = "EMP001,Vrushabh,Pune,DataEngineer,85000"
fields = csv_row.split(",")

record = {
    "id": fields[0],
    "name": fields[1],
    "city": fields[2],
    "role": fields[3],
    "salary": int(fields[4])
}

print("\n--- Parsed Record ---")
print(record)
print(f"Name: {record['name']} | Salary: {record['salary']:,}")


# Example 2: Pipeline config
config = {
    "env": "prod",
    "source": "s3://raw-bucket/sales/2024/",
    "target": "s3://processed-bucket/sales/2024/",
    "file_format": "parquet"
}

print("\n--- Pipeline Config ---")
print(f"Running in {config['env']}")
print(f"Source: {config['source']}")


# Example 3: Aggregation (GROUP BY)
records = [
    {"region": "North", "sales": 1500},
    {"region": "South", "sales": 800},
    {"region": "North", "sales": 2000},
]

region_totals = {}

for r in records:
    region = r["region"]
    sales = r["sales"]

    if region in region_totals:
        region_totals[region] += sales
    else:
        region_totals[region] = sales

print("\n--- Sales by Region ---")
for region, total in region_totals.items():
    print(f"{region}: {total}")


# Example 4: Schema validation
required_fields = ["id", "name", "city"]

incoming = {"id": "EMP004", "name": "Sneha"}

missing = []

for field in required_fields:
    if field not in incoming:
        missing.append(field)

print("\n--- Schema Check ---")
print("Missing fields:", missing)


# =========================================
# Practice
# =========================================

data = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 90}
]

print("\n--- Marks > 70 ---")
for std in data:
    if std["marks"] > 70:
        print(std["name"])


student = {
    "name": "Akshay",
    "marks": {
        "math": 80,
        "science": 75
    }
}

print("\n--- Nested Access ---")
print(student["marks"]["math"])
print(student["marks"]["science"])