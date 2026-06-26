#conditionals- > >= < <= == !=
#using if- condition 1

x=int(input("What's x?"))
y=int(input("What's y?"))

#boolean expressions
#Three conditions to check
if  x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
if x==y:
    print("x is equal to y")


#using elif- condition 2
x1=int(input("What's x1?"))
y1=int(input("What's y1?"))

#faster processing
if  x1<y1:
    print("x1 is less than y1")
elif x1>y1:
    print("x1 is greater than y1")
elif x1==y1:
    print("x1 is equal to y1")


#using else- condition 3
x2=int(input("What's x2?"))
y2=int(input("What's y2?"))

#logically if not greater than and not less than then it must be equal to
if  x2<y2:
    print("x2 is less than y2")
elif x2>y2:
    print("x2 is greater than y2")  
else:
    print("x2 is equal to y2")

#using or-condition 4
x3=int(input("What's x3?"))
y3=int(input("What's y3?"))
if x3<y3 or x3>y3:
    print("x3 is not equal to y3")
else:
    print("x3 is equal to y3")

#using not equal to- condition 5
x4=int(input("What's x4?"))
y4=int(input("What's y4?")) 
if x4!=y4:
    print("x4 is not equal to y4")  
else:
    print("x4 is equal to y4")

#using equal to- condition 6
x5=int(input("What's x5?")) 
y5=int(input("What's y5?"))
if x5==y5:
    print("x5 is equal to y5")  
else:
    print("x5 is not equal to y5")
