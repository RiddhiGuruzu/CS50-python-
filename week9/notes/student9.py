# Defines class for a student
# classes allow to invent programmer's own data types


class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    # calling the function class
    student = Student()

    # attributes or instance variables
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
