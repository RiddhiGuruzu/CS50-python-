# Stores student as dict


def main():
    student = get_student()
    # calling out a key. be aware of single and double quotes
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
