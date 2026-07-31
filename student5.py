# Stores student as (mutable) list


def main():
    student = get_student()
    # indexing uses square brackets
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # lists are mutable
    return [name, house]


if __name__ == "__main__":
    main()
