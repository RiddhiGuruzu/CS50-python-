def main():
    #get_number: asks user for input number of iterations
    number=get_number()

    #meow: prints meow
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            #returns n instead of break
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()