import emoji

user_input=input("Input: ")
# doing emoji.emojize(language='alias') enables both the full list and aliases.
print("Output:",emoji.emojize(user_input,language='alias'))