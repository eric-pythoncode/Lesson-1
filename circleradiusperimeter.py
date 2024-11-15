import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return math.pi * 2 * self.radius
    

radius = int(input("Enter the radius of the cirle:"))
c1 = circle(radius)

print(f"The radius of the circle is: {c1.area():.2f}")
print(f"The perimeter of the circle is: {c1.perimeter():.2f}")

