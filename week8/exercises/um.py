import re

def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum|\bUm",s))

if __name__ == "__main__":
    main()