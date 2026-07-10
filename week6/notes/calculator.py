def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# define a function called square that takes a number and returns the square of that number
def square(n):
    return n * n 
#or return n ** 2
#or pow(n, 2)

if __name__=="__main__":
    main()