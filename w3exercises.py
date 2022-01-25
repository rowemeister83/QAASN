#exercise one

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)

#exercise two

celsius = float(input("Enter celsius temp:"))
fahrenheit = (celsius * 1.8) + 32
print('%.0f celsius is %0.1f fahrenheit' %(celsius, fahrenheit))
fahrenheit = float(input("Enter fahrenheit temp:"))
celsius = (fahrenheit - 32) / 1.8
print('%.0f fahrenheit is %0.1f Celsius' %(fahrenheit, celsius))

#exercise three

#exercise four

for i in range(1, 10):
    if(i>5):
        i = 10 - i
    for j in range(i):
        print("*", end=" ")
    print()

#exercise five

st = input("Enter a random word: ")
rev = st[::-1]
print("your word, reversed, is: ", rev)


