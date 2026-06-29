# When using Multiple Lists if the order gets messed up, the students end up in the wrong houses!
example1 = ["Hermione", "Harry", "Ron", "Draco"]
example2 = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# THE SOLUTION: A dictionary (dict) allows you to associate a "key" with a "value".
# In this case, the student's name is the Key, and their house is the Value.

# i) One Dict 
students = {
    "Hermione": "Gryffindor",  
    "Harry": "Gryffindor",     
    "Ron": "Gryffindor",       
    "Draco": "Slytherin",      
}

# looking up the key(ex: hermione) to get value(ex: gryffindor)
for student in students:
    print(student, students[student], sep=", ")


# ii) Multiple Dicts (four) in a list
# 3 keys per Dict (ex: name, house, patronus)
# 3 values (ex: Hermione, Gryffindor, Otter)
students1 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    # "None" represents absence of value
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student1 in students1:
    print(student1["name"], student1["house"], student1["patronus"], sep=", ")



