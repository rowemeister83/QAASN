file = open("Teams.txt", "r")

print(file.readline())
file.readline()
print(file.readline())
file.seek(2)
print(file.readline())

file.close()