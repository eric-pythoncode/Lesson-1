x = input("What item do you want to add to list?: ")

list = []

list.append(x)

print("The item added: ", x)

y = input("Add another item to the list: ")

list.append(y)

print("Item added: ", y)

z = input("What do you want to remove from the list?: ")

list.remove(z)

print("Item removed: ", z)