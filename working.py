import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)$"
    matches=re.search(pattern,s)

    if not matches:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = matches.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if p1 == "AM":
        h1 = 0 if h1 == 12 else h1
    elif p1 == "PM":
        h1 = 12 if h1 == 12 else h1 + 12

    if p2 == "AM":
        h2 = 0 if h2 == 12 else h2
    elif p2 == "PM":
        h2 = 12 if h2 == 12 else h2 + 12

    return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"

if __name__ == "__main__":
    main()