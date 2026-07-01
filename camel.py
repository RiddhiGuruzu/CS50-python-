# Prompt the user for input
camel_case = input("camelCase: ")

print("snake_case: ", end="") # no new line

# Loop through each character in the string
for char in camel_case:
    # If the character is uppercase, print an underscore and the lowercase letter
    if char.isupper():
        print("_" + char.lower(), end="")
    # Otherwise, just print the lowercase character
    else:
        print(char, end="")

# Print a final newline
print()