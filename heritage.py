import math

class A:
    def f1(self):
        print("This is F1")
    def f2(self):
        print("This is F2")

class B:
    def f3(self):
        print("This is F3")
    def f4(self):
        print("This is F4")

class C(A,B):
    def f5(self):
        print("This is F5")
    def f6(self):
        print("This is F6")


a1 = A()
a1.f1()
b1 = B()
b1.f4()
c1 = C()
c1.f1()

class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I make a sound!"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
mydog = Dog("Buddy")

print(f"{mydog} says: {mydog.speak()}")
print(f"{mydog} says: {mydog.speak()}")

class shape():
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
mycircle = circle(5)
myrectangle = rectangle(4, 5)

print(f"Circle area: {mycircle.area()}")
print(f"Rectangle area: {myrectangle.area()}")

class electronics():
    def __init__(self, brand):
        self.brand = brand
    def poweron(self):
        return (f"{self.brand} is turning on")
    
class Mobile(electronics):
    def makecall(self):
        return "Making a call. . ."
    
    
class Smartphone(Mobile):
    def browse(self):
        return "Browsing the internet. . ."

    
smartphone = Smartphone("Samsung")

print(smartphone.poweron())
print(smartphone.browse())
print(smartphone.makecall())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getdetails(self):
        print(f"Employee name: {self.name} - Salary: {self.salary}")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def develop(self):
        print(f"{self.name} is writing code.")

class TechLead(Employee):
    def lead(self):
        print(f"{self.name} is leading the project.")

employee = Employee("Alice", 50000)
employee.getdetails()

manager = Manager("Bob", 75000)
manager.getdetails()
manager.manage()

developer = Developer("Jake", 125000)
developer.getdetails()
developer.develop()

techlead = TechLead("Sheldon", 150000)
techlead.getdetails()
techlead.lead()



