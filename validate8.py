# Adds ^ and $ to regex

import re

email = input("What's your email? ").strip()

# ^ start of string
# $ end of string
# back slash for specifically a dot
# if we add more than one @ it is still valid

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
