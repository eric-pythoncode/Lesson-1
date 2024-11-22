class Vehicle:
    def __init__(self, name, basefare):
        self.name = name
        self.basefare = basefare

    def displayinfo(self):
        return f"Vehicle name: {self.name}, base fare: {self.basefare}"
    
class Bus(Vehicle):
    def __init__(self, name, basefare, numpassengers):
        super().__init__(name,basefare)
        self.numpassengers = numpassengers
    
    def calculatefare(self):
        return self.basefare * self.numpassengers
    
    def displayinfo(self):
        vehicleinfo = super().displayinfo()
        return f"{vehicleinfo}, Number of passengers: {self.numpassengers}, Total fare: {self.calculatefare}"
    
bus = Bus(name="City bus", basefare=10, numpassengers=50)

print(bus.displayinfo())