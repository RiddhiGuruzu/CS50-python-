name=input("What's your name? ")

#Option A: to use if statements to check for multiple conditions
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#Option B: to use match
match name:
    #vertical bar is used to check for multiple conditions in one case
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    #underscore is used as a catch-all for any other input
    case _:
        print("Who?")
