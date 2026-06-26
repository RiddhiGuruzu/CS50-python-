def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#option A
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Option B
#This can also be condesed to:
def is_even(n):
    return True if n % 2 == 0 else False


#Option C
#This can also be condesed to:
def is_even(n):
    return n % 2 == 0

main()
