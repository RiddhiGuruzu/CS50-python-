def main():
    text=input("Enter: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    characters =["a","e","i","o","u"] # mistake. doesn't work for capital letters.
    result=""

    for char in word:
        if char not in characters:
            result+=char
    return result

if __name__ == "__main__":
    main()