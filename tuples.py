# Simple Python program to demonstrate the use of lists

# 1. Creating a list

fruits = ["apple", "banana", "cherry", "date"]

# 2. Adding items to the list

fruits.append("elderberry") # Add to the end

fruits.insert(1, "blueberry") # Add at index 1

# 3. Removing items from the list

fruits.remove("banana") # Remove by value

removed_fruit = fruits.pop() # Remove the last item and get it

# 4. Accessing elements in the list

print("First fruit:", fruits[0]) # Access by index

print("Last fruit:", fruits[-1]) # Access the last element

# 5. Iterating through the list

print("Current fruits in the list:")

for fruit in fruits:    

    print(fruit)

# 6. Length of the list

print("Number of fruits:", len(fruits))

# 7. Checking if an item is in the list

if "cherry" in fruits:
    print("Cherry is in the list.")
else:

    print("Cherry is not in the list.")

# Final state of the list

print("Final list of fruits:", fruits)

print('-------------------------')
print("TUPLES")
print(fruits[3])
print(fruits[::-1])

print(fruits[2:5])
print(len(fruits))

for i in fruits:
    print(i)

del fruits

tup = (1, 3, 5, 3, 1)

tup1 = (72222, 5432, 354325324532, 1242423424233, 12423400, 235, 34214233, 6743214234)

def is_palindrome(tup):
    return tup == tup[::-1]

if is_palindrome(tup):
    print(tup, " is a palindrome.")
else:
    print(tup, " is not a palindrome. ")

if is_palindrome(tup1):
    print(tup1, " is a palindrome.")
else:
    print(tup1, " is not a palindrome. ")

print("-----------------------------")
print("SETS")

sets = {34, 56, 72, 100, 96, 100, 34, 64, 96, 72} # only puts first number in order - 34, 64, 34 -> 34, 64

print(sets)

print(sets[4]) # cannot put [4] it is not following sequence it randomly gives all number

#sets do not follow a particular sequence as it use hash(#) to fetch the values... it focuses on speed on execution rather than the sequesnce in which the data is stored
