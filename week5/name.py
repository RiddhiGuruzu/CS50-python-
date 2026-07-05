import sys

# sys.argv: is a list, getting no of elements in a list
# type in command line: "python name.py Riddhi"

# what is in sys.argv[0]: the name of the program

# Error Handling option A (vague)
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# Error Handling option B (detailed)

if len(sys.argv)<2:
    # sys.exit(): leaves the program
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


# how to print multiple names at once
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# no taken from zero to avoid printing name.py
for arg in sys.argv[1:]:
    print("hello, my name is", arg)