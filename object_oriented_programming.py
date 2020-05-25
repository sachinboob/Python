class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("My name is {0} and age is {1}".format(Person("John", 36).name, Person("Sachin", 30).age))
