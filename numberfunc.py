def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x 
            #return does breaking and returning

        except ValueError:
            pass # do nothing and continue the loop

main()