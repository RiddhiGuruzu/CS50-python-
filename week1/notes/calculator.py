#operations in python: + - * / %

#printing the result of an operation
x1 = 1
y1 = 2
z1 = x1 + y1
print(z1)

#printing result of an operation with user input                                 
x2 = input("What's x? ")
y2 = input("What's y? ")
#converting the input values to integers before performing the addition operation
z2 = int(x2) + int(y2)
print(z2)

#printing result of an operation with user input without z
#nested function calls: input() returns a string, int() converts the string to an integer, and then the addition operation is performed.
x3 = int(input("What's x? "))
y3 = int(input("What's y? "))
print(x3 + y3)

#floating point numbers: numbers with decimal points
#printing result of an operation with floating point numbers
x4 = float(input("What's x? "))
y4 = float(input("What's y? "))
print(x4 + y4)

# rounding numbers in python
# Documentation: round(number, ndigits=None)
z4 = round(x4 + y4)

# Print the result in f string format
print(f"{z4}") 

#formatting the number with commas as thousands separators
print(f"{z4:,}") 


#trying division operation with user input
#rounding to 2 decimal places with round() function 
z5=round(x4/y4, 2)
print(z5)

#rounding to 2 decimal places with f string formatting
#point 2f is how many decimal places you want to round to, in this case 2 decimal places
print(f"{z5:.2f}") 
