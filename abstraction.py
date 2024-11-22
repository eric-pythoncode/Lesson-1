from abc import ABC, abstractmethod
from typing import Any

class Vehicle(ABC):
    @abstractmethod
    def numwheels(self):
        pass

class Bike(Vehicle):
    @property
    def numwheels(self):
        return 2
    
class Car(Vehicle):
    @property
    def numwheels(self):
        return 4

bike = Bike()
car = Car()

print(f"A bike has {bike.numwheels} wheels.")
print(f"A car has {car.numwheels} wheels.")

print("---------------------------------------------------------------------------")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
c1= Circle(5)

r1 = Rectangle(4,6)

print(f"Area of Circle = {c1.area()}")

print(f"Area of Rectangle = {r1.area()}")
    
"""shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes():
    print(f"Area: {shape.area()}")"""

print("--------------------------------------------------------------------")

class Vehicle(ABC):
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def showDetails(self):
                return f"Brand: {self.brand}, number of wheels: {self.wheels}"
    
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, fuelCapacity):
        super().__init__(brand, 4)
        self.fuelCapacity = fuelCapacity

    def start(self):
        return f"{self.brand} car is starting with {self.fuelCapacity} liters of fuel."
    def stop(self):
        return f"{self.brand} is stopping"
    
    def honk(self):
        return "Car goes Beep Beep!"
    
class Bicycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)

    def start(self):
        return f"{self.brand} car is starting by pedaling."
    def stop(self):
        return f"{self.brand} is stopping by applying brakes"
    
    def honk(self):
        return "Bicycle goes Ring Ring!"
    
class Bus   (Vehicle):
    def __init__(self, brand, seatingCapacity):
        super().__init__(brand, 4)
        self.seatingCapacity = seatingCapacity

    def start(self):
        return f"{self.brand} car is starting with a seating capacity of {self.seatingCapacity} passengers."
    def stop(self):
        return f"{self.brand} bus is stopping"
    
    def honk(self):
        return "Car goes Beep Beep!"
    
    def openDoors(self):
        return "Bus doors are opening"
    
car = Car(brand="Toyota", fuelCapacity=50)
bicycle = Bicycle(brand="Giant")
bus = Bus(brand="Volvo", seatingCapacity=40)

vehicles = [car, bicycle, bus]

for vehicle in vehicles:
    print(vehicle.showDetails())
    print(vehicle.start())
    print(vehicle.stop())
    if isinstance(vehicle, Car):
        print(vehicle.honk())
    elif isinstance(vehicle, Bicycle):
        print(vehicle.honk())
    elif isinstance(vehicle, Bus):
        print(vehicle.openDoors())
    print("-" * 40)