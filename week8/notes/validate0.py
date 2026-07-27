# Validates email address by checking for @
# regexes- pattern or regular expression

# removing trailing and leading whitespace
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
