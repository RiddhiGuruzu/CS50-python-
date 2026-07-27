# Uses re.search

import re

name = input("What's your name? ").strip()
# () for grouping
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")
