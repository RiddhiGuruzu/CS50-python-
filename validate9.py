# Adds character class

import re

email = input("What's your email? ").strip()

# set of characters []: every character that can be included
# complementing the set [^]: any character except the one in it
# ex: r"^[^@]+@[^@]+\.edu$"
# what if i type ".edu@something.edu"- valid


# solution:
# can also takes space
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
