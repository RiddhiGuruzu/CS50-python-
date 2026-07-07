import random

while True:
    try:
        level=int(input("Level: "))
        if level<=0:
            continue
        else:
            break
        
    except ValueError:
        continue

number=list(range(1,level+1))
comp_number=random.choice(number)

while True:
    try:
        guess=int(input("Guess: "))

        if guess>0 and guess<comp_number:
            print("Too small!")
            continue
        elif guess>0 and guess>comp_number:
            print("Too large!")
            continue
        elif guess>0 and guess==comp_number:
            print("Just right!")
            break
        else:
            continue

    except ValueError:
        continue



        



