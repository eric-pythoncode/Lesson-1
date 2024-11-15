class Employee:
    def calculatesalary(self):
        raise NotImplementedError("This method is not overridden in subclasses.")

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculatesalary(self):
        return f"{self.name}'s salary is ${self.salary}."
    
class FullTimeEmployee(Employee):
    def __init__(self, name, hourlyrate, hoursworked):
        self.name = name
        self.hourlyrate = hourlyrate
        self.hoursworked = hoursworked
    def calculatesalary(self):
        return f"{self.name}'s salary is ${self.salary}."
    
