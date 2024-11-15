#using inheritance-------------------------------------------------------

class dog:
    def sound(self):
        return "woof"
    
class cat:
    def sound(self):
        return "meow"
    
class cow:
    def sound(self):
        return "moo"
    
animals = [dog(), cat(), cow()]

for i in animals:
    print(i.sound())

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

class Square:
    def area(self, side):
        return side * side

class Rectangle:
    def area(self, width, height):
        return width * height
    
shapes = [Circle(), Square(), Rectangle()]

print(f"Circle area: {shapes[0].area(5)}")
print(f"Square area: {shapes[1].area(4)}")
print(f"Rectangle area: {shapes[2].area(3, 6)}")

class Lion:
    def habitat(self):
        return "Savanna"
    
class Penguin:
    def habitat(self):
        return "Antarctica"
    
class Frog:
    def habitat(self):
        return "Wetlands"
    
animals2 = [Lion(), Penguin(), Frog()]

for animal in animals2:
    print(f"The {animal.__class__.__name__} lives in {animal.habitat()}.")

# Base class

class Transportation:

    def travel_speed(self):

        pass

# Subclass for Car

class Car(Transportation):

    def travel_speed(self):

        return "The car travels at 100 km/h."

# Subclass for Bicycle

class Bicycle(Transportation):

    def travel_speed(self):

            return "The bicycle travels at 15 km/h."

# Subclass for Airplane

class Airplane(Transportation):

    def travel_speed(self):

        return "The airplane travels at 800 km/h."

# List of transportation modes

transport_modes = [Car(), Bicycle(), Airplane()]

# Displaying the travel speeds for each transportation mode

for mode in transport_modes:

    print(mode.travel_speed())


class PaymentMethod:
    def processpayment(self, amount):
        raise NotImplementedError("Subclass must implement this method")
    
class CreditCard(PaymentMethod):
    def processpayment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPal(PaymentMethod):
    def processpayment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransfer(PaymentMethod):
    def processpayment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

def makepayment(paymentmethod, amount):
    paymentmethod.processpayment(amount)

creditcard = CreditCard()
paypal = PayPal()
banktransfer = BankTransfer()

makepayment(creditcard, 100)
makepayment(paypal, 100)
makepayment(banktransfer, 100)

