# Adds \.edu

import re

email = input("What's your email? ").strip()

# ends in .edu
# the dot here is different so we use back slash and raw string (similar to f string)
# what if you type "my email address in malan@harvard.edu."- shows valid
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
