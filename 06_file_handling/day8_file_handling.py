#📅 Day 8 — File Handling (Step 1: Basics)
#🧠 Why File Handling?

#👉 In Data Engineering:

#Read data from files
#Process it
#Write cleaned data

#👉 Example:

#input.csv → process → output.csv

#💻 1. Writing to File
# write mode (w)
file = open("sample.txt", "w")

file.write("Hello Data Engineering\n")
file.write("Learning file handling")

file.close()

import os

print(os.getcwd())


with open("data.csv", "r") as file:
    for line in file:
        print(line.strip())

with open("data1.csv", "w") as file:
    file.write("id,name,city,salary\n")
    file.write("1,A,Pune,30000\n")
    file.write("2,B,Mumbai,60000\n")
    file.write("3,C,Delhi,70000\n")

with open("data.csv", "r") as file:
    for line in file:
        print(line.strip())

with open("data1.csv", "w") as file:
    file.write("id,name,city,salary\n")
    file.write("1,A,Pune,30000\n")
    file.write("2,B,Mumbai,60000\n")
    file.write("3,C,Delhi,70000\n")

print("File created successfully")

import os
print(os.getcwd())

import csv

with open("data1.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

import csv

with open("data1.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # skip header

    for row in reader:
        print(row)

import csv

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


import csv

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["salary"]) > 50000:
            print(row["name"], row["salary"])

import csv

total = 0

with open("data1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["salary"])

print("Total Salary:", total)

import csv

data = [
    ["id", "name", "city"],
    ["1", "Vrushabh", "Pune"],
    ["2", "Akshay", "Mumbai"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file written successfully")

data = {
    "id": 101,
    "name": "Vrushabh",
    "city": "Pune"
}

import json

with open("data.json", "w") as file:
    json.dump(data, file)

print("CSV file written successfully")

data = {
    "id": 101,
    "name": "Vrushabh",
    "city": "Pune"
}

import json

with open("data.json", "w") as file:
    json.dump(data, file)

import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])