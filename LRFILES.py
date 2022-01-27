openedfile = open("README.md")
textstuff = openedfile.read()
openedfile.close()

uppertext = textstuff.upper()

print(uppertext)
openedfile = open("README.md", "w")
openedfile.write(uppertext)
openedfile.close()
