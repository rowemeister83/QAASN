class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))