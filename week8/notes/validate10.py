# Replaces character class with \w

import re
# we can do .lower()
email = input("What's your email? ").strip()

# \w is any word charcter
# (|) means or

# what if I type: MALAN@HARVARD.EDU- invalid

if re.search(r"^\w+@\w+\.(com|edu|gov)$", email):
    print("Valid")
else:
    print("Invalid")
