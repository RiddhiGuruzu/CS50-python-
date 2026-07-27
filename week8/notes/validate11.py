# Adds re.IGNORECASE
# treats case insensitively

import re

email = input("What's your email? ").strip()

# what if I type: malan@cs50.harvard.edu
# invalid due to dot after @

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
