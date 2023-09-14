# Inheritance is a mechanism for using code

# Lets say we have this dog class with a simple walk method
# class Dog:
#    def walk(self):
#        print("Walk")

# What if in the future, we want to define another class
# Lets say cat and we want to add this walk method there as well
#class Cat:
#    def walk(self):
#        print("Walk")

# We need to define this method again here
# This is bad because we have repeated the code.
# In programming there is concept of dry -> dont repeat yourself

# Lets say in future we discover a prblm with our walk method
# If u have repeated or duplicated this method in many other places, then we have to fix that prblm in every single place
# Thats why in programming, you should not define something twice.

# How can we solve this prblm?
# One approach is inheritance
# We define a new class called mammal and move the walk method there. Then we will have the dog and cat classes inherit that method from their parent.

class Mammal:
    def walk(self):
        print("walk")


# Now we want dog class to inherit this method from mammal classs
# So right after the class name, we add parenthesis and then type out the name of parent class
# class Dog(Mammal):
# This is all we have to do. With this the dog class will inherit all methods defined in mammal class.
# Python doesnt like any class empty. So we can add methods in Dog class or we can add pass
# pass means nothing.
# We are telling python interpreter, hey pass this line, dont worry about it.

# We can also add specific method to Dog in dog class
class Dog(Mammal):
     def bark(self):
         print("bark")

class Cat(Mammal):
    pass


dog1 = Dog()
# If we type dog. we can see walk method here.
dog1.walk()  # walk
cat1 = Cat()
cat1.walk()  # walk
dog1.bark()  # bark

# So both dog and cat classes are inheriting method defined in their parent class.
# We can also add be_annoying method to Cat class