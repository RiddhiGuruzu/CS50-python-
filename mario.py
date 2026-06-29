# Option A
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()


# Option B(most compact):
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        #  Print brick
        print("#"*size)


main()

# Option C:
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()