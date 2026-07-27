# Adds .*

import re

email = input("What's your email? ").strip()

# * 0 or more repetitions
# . any character except new line
if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")
