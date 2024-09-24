def areacalculator():
    print("AREA CALCULATOR")
    print("-----------------")
    print("Enter the shape you want to calculate the area of:")
    print("1. Square \n2. Rectangle \n3. Triangle \n4. Circle")
    choice = int(input("Choose from 1 - 4: "))

    if choice == 1:
        side = float(input("Enter the size of the square: "))
        print("Area = " , side * side)
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area = " , length * width)
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area = " , 0.5 * (base * height))
    elif choice == 4:
        r = float(input("Enter the radius of the circle: "))
        pi = 3.14
        print("Area = " , pi * r * r)
    else:
        print("Invalid entry!")


#mainprogram
areacalculator()