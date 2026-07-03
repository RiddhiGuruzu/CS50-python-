while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)

        if 1 >= x/y >= 0.99:
            print("F")
            break

        elif 0 <= x/y <= 0.01:
            print("E")
            break

        elif x<0 or x>y:
            raise ValueError
        
        else:
            print(f"{x/y*100:.0f}%")
            break

    except (ValueError, ZeroDivisionError):
        continue
    





