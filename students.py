# csv: comma seperated values
# sorted
import csv

# writing CSV
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


# reading CSV
students = []

with open("students.csv") as file:
    reader = csv.Dictreader(file)
    for row in reader:
        students.append(row)


# key tells how to sort students
# lambda used instead of a function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

