# list of 3 strings
students = ["Hermione", "Harry", "Ron"]

# Option A
# manually indexing in lists
print(students[0])
print(students[1])
print(students[2])

# Option B
# using for loop to print each student
# no need to intialize variable "student"
for student in students:
    print(student)

# Option C
# using index positions in for loop to print each student
# len calculates number of items in lists
for i in range(len(students)):
    print(students[i])

# Option D
# ranking students with same index positions
for i in range(len(students)):
    print(i+1, students[i])


