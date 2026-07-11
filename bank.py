def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    if greeting.lower().startswith("hello"):
        return f"$100" # mistake
    elif greeting.lower().startswith("h"):
        return f"$20"   
    else:
        return f"$0" # mistake

if __name__ == "__main__":
    main()


