# Define a new type called person
# This person object should have a name attribute as well as a talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Talk")
        print(f"Hi I am {self.name}!")


person1 = Person("Fakhra")
print(person1.name)  # Fakhra
person1.talk()  # Talk Hi I am Fakhra!
