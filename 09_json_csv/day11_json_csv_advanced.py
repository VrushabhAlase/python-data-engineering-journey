# =========================================
# Day 11 - CSV & JSON Advanced (Real Usage)
# =========================================

import csv
import json

print("\n--- CSV ADVANCED ---")

# -----------------------------------------
# 1. Read CSV → Clean + Transform
# -----------------------------------------

clean_data = []

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Clean & transform
        record = {
            "id": int(row["id"]),
            "name": row["name"].upper(),
            "city": row["city"].lower(),
            "salary": int(row["salary"])
        }

        clean_data.append(record)

print("Cleaned Data:", clean_data)


# -----------------------------------------
# 2. Write Clean Data to New CSV
# -----------------------------------------

with open("cleaned_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "city", "salary"])

    writer.writeheader()
    writer.writerows(clean_data)

print("Clean CSV created")


# -----------------------------------------
# 3. Convert CSV → JSON
# -----------------------------------------

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("CSV converted to JSON")


# =========================================
# JSON ADVANCED
# =========================================

print("\n--- JSON ADVANCED ---")

# -----------------------------------------
# 4. Read JSON & Process
# -----------------------------------------

with open("data.json", "r") as file:
    data = json.load(file)

for record in data:
    print(record["name"], record["salary"])


# -----------------------------------------
# 5. Filter JSON Data
# -----------------------------------------

high_salary = []

for record in data:
    if int(record["salary"]) > 50000:
        high_salary.append(record)

print("\nHigh Salary Records:", high_salary)


# -----------------------------------------
# 6. Write Filtered JSON
# -----------------------------------------

with open("high_salary.json", "w") as file:
    json.dump(high_salary, file, indent=4)

print("Filtered JSON created")

