# importing the function directly when the library name does not conflict with variable names
import random
# or "from random import choice"

# seq = ["heads", "tails"], which is a list
# random.choice() is a method that randomly selects an item from a sequence
coin = random.choice(["heads", "tails"])
print(coin)

# random.randint() randomly generates numbers between two ranges
number = random.randint(1,10)
print(number)

# random.shuffle(x): randomizes variables
cards =["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
