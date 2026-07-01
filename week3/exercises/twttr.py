text=input("Enter: ")

characters =["a","e","i","o","u"]
# no new line
print("Output: ", end="") 

for char in text:
    if char not in characters:
        print(char, end="")



        