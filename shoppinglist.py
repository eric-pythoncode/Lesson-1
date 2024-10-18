shoppinglist = []

while True:
    print("Shopping list menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Exit")
    decision = int(input("Choose an option (1 - 4): "))
    if  decision == 1:
        add = input("Input your item here: ")
        shoppinglist.append(add)
        print("Added item: ", add)
    elif decision == 2:
        remove = input("Enter the item that you want to remove: ")
        if remove in shoppinglist:
            shoppinglist.remove(remove)
            print("Removed item: ", remove)
        else:
            print("Item not in shopping list.")
    elif decision == 3:
        print("Shopping list:")
        for index, item in enumerate(shoppinglist):
            print(f"{index + 1}. {item}")
    elif decision == 4:
        print("Goodbye")
        break
    else:
        print("Wrong input! ")