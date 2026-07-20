# A: aren't sorted in alphabetical order
with open("names.txt","r") as file_1:
    for line in file_1:
        print("hello,",line.rstrip()) # reading names 

# B: sorted by appending to list
names=[]
# default at read
with open("names.txt") as file_2:
    for line in file_2:
        names.append(line.rstrip())
    
for name in sorted(names):
    print(f"hello, {name}")

# C: sorted in file itself in descending order
with open("names.txt") as file_2:
    for line in sorted(file_2,reverse=True):
        print("hello,", line.rstrip())