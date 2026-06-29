#loops

#while- allows to ask a q multiple times
#click control C to cancel running when loops are too long 

#option A: counting down
i=3
while i != 0:
    print("meow")
    #i = i - 1
    i -= 1

#option B: couting up
i1 = 0
while i1 < 3:
    print("meow")
    #i = i + 1
    i1 += 1


#list- storing multiple values into one
#for- iterates over list of items

# Option 1: manually listing
for i in [0,1,2]:
    print("meow")

# Option 2: setting a range
# underscore used when a variable has no use except counting
for _ in range(3):
    print("meow")

# using multiplication to concatenate strings
print("meow\n"*3, end="")


# taking user input for number of iterations and looping
while True:
    # loops until a positive number is given
    n = int(input("What's n?"))
    if n>0:
        break

for _ in range(n):
    print("meow")


