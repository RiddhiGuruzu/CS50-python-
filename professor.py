import random

def main():
    level = get_level()

    q_no = 0
    score = 0

    while q_no < 10:
        q_no += 1
        error_no = 0

        x = generate_integer(level)
        y = generate_integer(level)

        while error_no < 3:
            print(x, "+", y, "= ", end="")

            try:
                ans = int(input())

                if ans == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    error_no += 1

            except ValueError:
                print("EEE")
                error_no += 1

        if error_no == 3:
            print(x, "+", y, "=", x + y)

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)
    else:
        raise ValueError


if __name__ == "__main__":
    main()