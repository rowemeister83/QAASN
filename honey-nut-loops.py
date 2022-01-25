countdown = 56

#print(countdown)
#countdown = countdown - 1
#print(countdown)
#countdown = countdown - 1
#print(countdown)
#countdown = countdown - 1
#print(countdown)
#countdown = countdown - 1
#print(countdown)
#countdown = countdown - 1

while countdown >40:
    print(countdown)
    countdown = countdown -1


for fish in ["cat", "dog", "lemur", "brazillian river snake", "Andelusian mountain llama"]:
    print(fish)

dictvar1 = {"cow":"moo" , "sheep":"baa" , "chicken":"cluck" , "dog":"bowow" }

print(dictvar1.keys())

for i in range(5):
    print("i love pies")

for i in "spoooooon":
    print(i)

my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:
    print(fruit.upper())

for word in "Hello world".split():
    print(word)

for key in {"key": "value"}:
    print(key)

for value in {"key": "value"}.values():
    print(value)

for key, value in {"key": "value"}.items():
    print(key, value)

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i * j)

for i in range(10, 21, 2):
    print(i)