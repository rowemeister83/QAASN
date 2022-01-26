class Dog:
    energy = "high"

    def speak(self):
        print("woof")


bilbo_waggins = Dog()

print(bilbo_waggins.energy)
bilbo_waggins.speak()

chewbarka = Dog()
chewbarka.energy = "low"

print(chewbarka.energy)
chewbarka.speak()