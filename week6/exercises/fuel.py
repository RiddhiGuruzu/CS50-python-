def main():
    fraction=input("fraction: ")
    print(convert(fraction))

    percentage=int(input("percentage: "))
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x<0 or x>y:
        raise ValueError
    
    return f"{x/y*100:.0f}%" # mintaske: returns string instead of int


def gauge(percentage):
    if percentage<=1:
        return f"E"
    elif percentage>=99:
        return f"F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


    





