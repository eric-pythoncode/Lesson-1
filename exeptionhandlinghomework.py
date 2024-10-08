def checkage():
    try:
        age = int(input("Please enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if age %2 == 0:
            print("Your age is ", age, " which is even")
        else:
            print("Youra age is ", age, " which is an odd number")
        
    except ValueError as e:
        print("Error: ", e)
    except Exception as e:
        print("An unexpeted error occured: ", e)

checkage()