def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum()):
        return False

    number = False
    for c in s:
        if c.isdigit():
            if not number:
                if c == "0":
                    return False
                number = True
        elif number:
            return False

    return True


main()