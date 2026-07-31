# Returns student as tuple, unpacking it


def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # returning multiple values or a single tuple
    return name, house


if __name__ == "__main__":
    main()
