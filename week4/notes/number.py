# run-time errors
# errors that occur while the program is running
x = int(input("What's x?"))
print(f"x is {x}")

# ValueError: the program will crash with if the user inputs a non-integer value
# invalid literal: refers to a value that cannot be converted to an integer
# base 10: refers to the decimal system (default)

# solution:
# Option A: add a print instruction statement
# But user might not pay attention 

# Option B: use a try/except block to handle the error 
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")



# NameError: the program will crash if you try to use a variable that has not been defined
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}") 
# x is not defined 

# solution A: using else 
# breaks out of loop if not integer
try:
    x = int(input("What's x?")) 
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# solution B: use a while loop to keep prompting the user until they enter a valid integer
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")