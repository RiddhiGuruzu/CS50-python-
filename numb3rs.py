import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    parts = ip.split(".")
    # (?:)- Non-Capturing Group
    # | - OR operator
    # Option A: 0
    # Option B: [1-9]- starts with non zero number and \d* -allows zero or more digits to follow
    if re.search(r"^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)$", ip):
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        else:
            return True
    return False


if __name__ == "__main__":
    main()