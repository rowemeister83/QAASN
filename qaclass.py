class Dog:
    energy = "high"

    def speak(self):
        print("woof")

Scud = Dog()

LHobo = Dog()

Blondi = Dog()

Pickles = Dog()


Pickles.speak()
LHobo.speak()
Blondi.energy = "cyanide"
print(Scud.energy)
print(Pickles.energy)