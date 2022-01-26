class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

dog1 = Dog("Ross Barkley", "Jack Russel", "High")

print(dog1.name, "is a", dog1.breed, "and his energy level is very", dog1.energy)

