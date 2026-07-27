# Adds optional subdomain

import re

email = input("What's your email? ").strip()


# adds another word character and dot optionally by using ()?
# ? is 0 or 1 repetitions. 
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
