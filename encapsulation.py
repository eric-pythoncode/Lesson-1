class Bank:
    def __init__(self,owner,balance = 0):
        self.__balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount deposited: {amount}")

    def withdraw(self, amount):
        if 0 <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn S{amount}")
        else:
            return "Insufficient funds!"
        
    def getbalance(self):
        return self.__balance
    

accout = Bank("Alice", 1000)
accout.deposit(350)
print(F"Current balance: {accout.getbalance()}")
accout.withdraw(450)
print(F"Current balance: {accout.getbalance()}")

print(f"Account holder: {accout.owner}")
"""print(f"Account balance: {accout.__balance}")""" #account.__balance cannot be accessed - it is a private attribute

print("-----------------------------------------------------------------------------------------------------------------")

class Car:
    def __init__(self,make,model,speed = 0):
        self.make = make
        self.model = model
        self.__speed = speed

    def acc(self , increment):
        if increment > 0:
            self.__speed += increment
            print(f"Speed: {self.__speed} km/h")
        else:
            print("The increment value should be positive")
    
    def brake(self , decrement):
        if decrement > 0 and self.__speed - decrement >= 0:
            print(f"Speed: {self.__speed} km/h")
        else:
            print("The decrement value should be positive")
    
    def getspeed(self):
        return self.__speed
    
car = Car("Toyota" , "Corolla")
car.acc(120)
car.brake(40)
print(f"Car's speed: {car.getspeed()} km/h")

print("---------------------------------------------------------------------------------------------------------------")

class shoppingCart:

    def __init__(self):

        self.items = []

    def add_item(self, item, price):

# Append as a tuple (item, price)

        self.items.append((item, price))

        print(f"Added {item} to the cart")

    def final_bill(self):

# Calculate the total sum by summing the price part of each tuple

        return sum(price for item, price in self.items)


    def view_cart(self):

# Return a list of tuples (item, price)

        return self.items


# Test the shoppingCart class

cart = shoppingCart()

cart.add_item("Gift", 450)

cart.add_item("Toy", 340)

cart.add_item("Stationary", 450)

cart.add_item("Apples", 250)

print(f"\nCart Items: {cart.view_cart()}")

print(f"Total Price: {cart.final_bill()}")

