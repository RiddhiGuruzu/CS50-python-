def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i+1))


if __name__ == "__main__":
    main()


# How to fix bugs:
# use print to debug and check the output of each step

# use breakpoints to pause the program and inspect variables
# step over codes that python inventors introduced
# step into codes that you wrote to see how they work
# continue to run the program after inspecting variables

