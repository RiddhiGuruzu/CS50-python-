# Changes * to +

import re

email = input("What's your email? ").strip()

# + 1 or more repetition
# plus is same as dot dot
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
