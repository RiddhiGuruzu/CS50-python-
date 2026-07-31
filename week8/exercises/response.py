from validator_collection import is_email

email_id=input("What's your email address? ")
if is_email(email_id):
    print("Valid")
else:
    print("Invalid")