def getnum():
    while True:
        try:
            num = int(input("Enter a number"))
            return num
        except ValueError:
            print("That is not a valid number")

value = getnum()
print("You entered: ", value)