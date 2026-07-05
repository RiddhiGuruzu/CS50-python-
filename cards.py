import random

cards = ["jack", "queen", "king"]


def main():
    print(
        "random.choice:", random.choice(cards)
    )  # Selects exactly ONE random element from the list as a single string
    # weights: probability of occurance, which add upto a 100%
    random.seed(1)  # takes position numbe and only prints elements till that
    print(
        "random.choices:", random.choices(cards, weights=[20, 20, 60], k=2)
    )  # Selects multiple random elements WITH replacement (duplicates allowed)
    print(
        "random.sample:", random.sample(cards, k=2)
    )  # Selects multiple unique elements WITHOUT replacement (no duplicates)


main()
