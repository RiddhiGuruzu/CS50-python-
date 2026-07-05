def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# to make use of sayings.py in ownsay.py
if __name__ == "__main__":
    main()