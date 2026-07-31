# Adds __init__

# everytime we call a class, we create an object
class Student:
    # instance methods
    # adding instance variables to objects
    # self gives access to current object that was just created
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # constructor call -> passing arguments to the class
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
