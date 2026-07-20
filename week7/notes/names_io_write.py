name=input("What's your name? ")

# automatically closes
with open("names.txt","a") as file:
    file.write(f"{name}\n") # writes names



