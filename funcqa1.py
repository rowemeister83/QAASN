def greet(firstname, lastname):
    return f"Hello {firstname} {lastname}"

print(greet("Steve", "Rogers"))

def greet():
    name = input("What is your name? ")
    print(f"Hello {name}")

greet()

def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
print(greet(name))


def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Steve"))  
print(greet("Bill", "Hola"))

def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Ollie", greeting="Hey"))


def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)

