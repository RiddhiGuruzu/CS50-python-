# Validates email address by checking for @ with regex
# re library
import re

email = input("What's your email? ").strip()

# re.search(pattern,string, flags=0)
if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
