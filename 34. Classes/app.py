# Classes in Python
# We use classes to define new types

# We have learned about basic types of python such as numbers, strings and booleans
# These are basic or simple types in python
# You also learn about a couple of complex types like lists and dictionaries
# While these types are useful, they cant always be used to model complex concepts, for eg think about the concept of a point, or a shopping cart.
# A shopping cart is not a boolean, its not a list, its not a dictionary. Its a different kind of thing.
# So we use classes to define new types to model real concepts.

# How to define a new type called point?
# And this new type is going to have methods for working with points

# We start by defining a class using class keyword and right after that we give our class a name.
# We use pascal notation here. We dont use underscore to separate multiple words. We capitalize first letter of every word.
# Like Point, EmailClient
# class Point
# After that we add colon and in the block we can define all the functions or methods that belong to points

class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


# The self parameter is automatically added by pycharm
# With this class, we define a new type. With this new type, we can create obejcts
# Object is an instance of class.
# A class simply defines the blueprint for creating objects
# And objects are actual instance based on that blue print.
# So we can have tens of hunderds of points on the screen. These are the objects or instances.

# To create an object, we type out the name of our class and then call it like a function. Point().
# This creates a new object and returns it. So then we can store that object in a variable.

point1 = Point()

# Now when we use the dot operator point1.  We have these 2 methods that we have defined draw and move
# We also have a bunch of other methods that start with two underscores. These are called magic methods.

# Calling draw method
point1.draw()  # Draw

# Apart from the methods, these objects can also have attributes
# These attributes are like variables that belong to a particular object.
point1.x = 10
point1.y = 20
print(point1.x)  # 10

# We can create another object
point2 = Point()
# This point2 is completely different from point1.
# print(point2.x)  # AttributeError: 'Point' object has no attribute 'x'
# We get error because this point object doesnt have x attribute

# So each object is different instance of our points class
point2.x = 50
print(point2.x)  # 50
# Now it has


# Use classes to define new types.
# These types can have methods that we define in body of the class and they can also have attributes that we can set anywhere in our prgrm.

