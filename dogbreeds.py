class Dog:
    species = "Canine"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    def display(self):
        print(f"Dog name: {self.name}")
        print(f"Dog breed: {self.breed}")
        print(f"Dog species: {self.species}")
        print("\n")

d1 = Dog("Golden retriever", "Buddy")
d2 = Dog("Bulldog", "Tiger")

print("Details of first dog")
print("------------------------------------------")
d1.display()


print("Details of second dog")
print("------------------------------------------")
d2.display()



