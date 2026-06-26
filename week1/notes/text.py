#code hello.py : creates file named hello.py

#print hello world
#print is a function
print("hello, world")

#python hello.py : runs the file hello.py

# ask user for name
# input function only returns strings
# "name" variable stores the return value of input function
name=input("what's your name? ")

#print name option 1
print("hello,")
print(name)

#alternative way to print name option 2
#no space between "hello," and name
print("hello, " + name)

#the best way to print name option 3
#automatically adds space between "hello," and name
print("hello,", name)

#how to add comments in python
# hash symbol is used for single line comments
'''multi line comments are done using triple quotes.'''

#print function documentation
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#astrisk before objects means that it can take any number of arguments.
#sep is used to separate the objects with a string. default is space.
#\n is used to add a new line at the end of the print statement. default is \n.

#way to alter end of print statement. 
print("hello, ", end="")
print(name)

#way to alter separator of print statement.
print("hello", name, sep="???")

#escape characters(quotation inside a string)
#option 1: using single quotes inside double quotes and vice versa 
print("hello, 'friend'")
#option 2: using backslash to escape the quotation mark
print("hello, \"friend\"")

#latest or most elegant way to print name option 4
#formatting strings using f-strings. f before the string indicates that it is an f-string.
print(f"hello {name}")

#manipulating strings in python
#documentation: https://docs.python.org/3/library/stdtypes.html
#option A
#removes whitespace from the beginning and end of the string
name=name.strip() 
#capitalizes the first letter of the string
name=name.capitalize() 
#capitalizes the first letter of each word in the string
name=name.title() 
#splits users name into first and last name. New variables are created for first and last name.
first, last=name.split(" ")
print(f"hello {first}")

#Option B: chaining the string methods
name=name.strip().title()

#Option C: chaining the variable at input itself
name=input("what's your name? ").strip().title()



