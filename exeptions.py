x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

try:
    result = x / y
except ZeroDivisionError:
    print("ERROR: Number cannot be divided by zero")
else:
    print("Result = ", result)