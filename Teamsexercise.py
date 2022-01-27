file = open("Teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
print(file.readline())
file.seek(0)

file.close()