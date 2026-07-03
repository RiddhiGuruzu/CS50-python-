grocery_list = {}

while True:
    try:
        # Prompt the user for an item and strip whitespace
        item = input().strip().lower()
            
        # Skip empty inputs if any, otherwise count the item
        if item:
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

    except EOFError:
        # Print a newline to clear the line after Control-Z-enter
        print()

        # Sort the items alphabetically
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item.upper()}")

        break



