
"""def weight(m, g):
   print("Mass: " m * g)

weight(55, 9)"""

def sum():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    sum = x + y
    print(f"Sum of {x} and {y} = {sum}")

def difference():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    diff = x - y
    print(f"Difference of {x} and {y} = {diff}")

def product():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    prod = x * y
    print(f"Product of {x} and {y} = {prod}")

def quotient():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    quot = x / y
    print(f"Quotient of {x} and {y} = {quot}")

def sqrt():
    x = int(input("Enter a number: "))
    sq = x ** 2
    print(f"Square of {x} is {sq}")

#main program

print("CALCULATOR")
print("What operation do you want to perform?")
print("1. Additiom \n2. Subtraction \n3. Multiplication \n4. Division \n5. Square of a number")
choice = int(input("Choose from [1 - 5] : "))

if choice == 1:
    sum()
elif choice == 2:
    difference()

elif choice == 3:
    product()

elif choice == 4:
    quotient()

elif choice == 5:
    sqrt()

else:
    print("Invalid number!")