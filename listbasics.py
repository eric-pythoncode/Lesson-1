import random

nums = [2, 4, 6, 7, 9, 9, 7, 5, 6, 4, 2, 9]

print (nums)


nums.insert(2,99)
print(nums)

nums.append(3)
print(nums)

nums.remove(8)
print(nums)

nums.pop(1)
print(nums)

nums.extend([99,100,1013,43214321,23423])

print("-----------------------------------------------------------")

print("Smallest number: ", min(nums))
print("Biggest number: ", max(nums))
print("Sum: ", sum(nums))

nums.sort()
print(nums)
print(nums(4))

nums.sort(reverse = True)
print(nums)

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