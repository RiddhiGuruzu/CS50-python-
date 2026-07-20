# this code needs user to type the name everytime you run it.
# does not save the name
names=[]

for _ in range(3):
    name=input("What's your name? ")
    names.append(name)


for name in sorted(names):
    print(f"hello, {name}")