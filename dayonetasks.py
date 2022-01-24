print("Hello World")

# In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a,e,i,o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

num = int(input("Pick a number, any number: "))
 
if (num % 2) == 0:
   print("{0} is Even".format(num))
   
else:
   print("{0} is Odd".format(num))

# Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.


# Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.


# Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message.

shapes = int(input("enter the amount of sides for your shape"))

shapekernel = ["triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "enneagon", "decagon"]

if shapes < 3 or shapes > 10:
    print("Please run the python script with the playbutton - in the explorer window - THEN provide a number higher than 2, that's also lower than 11")

elif shapes == 3:
    print(shapekernel[0])

elif shapes == 4:
    print(shapekernel[1])

elif shapes == 5:
    print(shapekernel[2])

elif shapes == 6:
    print(shapekernel[3])

elif shapes == 7:
    print(shapekernel[4])

elif shapes == 8:
    print(shapekernel[5])

elif shapes == 9:
    print(shapekernel[6])

elif shapes == 10:
    print(shapekernel[7])

