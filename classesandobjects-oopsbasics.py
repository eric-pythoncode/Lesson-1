x = 10

print(type(x))

class car:
    color = "red"
    brand = "mercedes"

car1 = car()
car2 = car()

car2.color = "Black"
car2.brand = "Audi"

print(car1.brand)
print(car2.brand)

print(f"Car2 is an {car2.brand} in {car2.color}")

class CAR:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def display(self):
        print(f"This car is a {self.color} {self.model}")

car1 = CAR("Red", "BMW")
car2 = CAR("Black", "Audi")

car1.display()
car2.display()

class BOOK:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print(f"This book is called {self.title} and was made by {self.author}")

book1 = BOOK("The Outsiders", "S.E Hinton")
book2 = BOOK("Lord of the Rings", "J.R.R Token")

book1.display()
book2.display()

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(10, 20)

print(f"Rectangle 1 area: {rectangle1.area()}")
print(f"Rectangle 1 perimeter: {rectangle1.perimeter()}")

print(f"Rectangle 2 area: {rectangle1.area()}")
print(f"Rectangle 2 perimeter: {rectangle1.perimeter()}")

class Person:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def calculate_age(self, currentyear):
        age = currentyear - self.birthyear
        return age
    def displayinfo(self):
        print(f"{self.name} is {self.calculate_age(2024)} years old.")

person1 = Person("John", 1994)
person2 = Person("Jane", 1993)

person1.displayinfo()
person2.displayinfo()

class Employee:
    def __init__(self, name, job):
        self.name = name
        self.jpb = job
    def displayjob(self):
        print(f"{self.name} is a {self.jpb}")

Employee1 = Employee("John", "Manager")
Employee2 = Employee("Jane", "Employee")

person1.displayjob()
person2.displayjob()