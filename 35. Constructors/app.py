# We have learned how to build new types using classes.

# class Point:
#     def move(self):
#         print("Move")
#     def draw(self):
#         print("Draw")

# There is a tiny prblm in this implementation.
# We can create a point object without x or y coordinates
# point1 = Point()
# print(point1.x)  # AttributeError: 'Point' object has no attribute 'x'
# We get the attribute error
# So point object has no attribute called x.
# This is prblm here
# It is possible to have a point object without an x or y coordinates.
# To solve this prblm, we use a constructor.

# A constructor is a function that gets called at the time of creating an object.
# When creating a point object, we need to pass values for x or y coordinates
# point = Point(10, 20)
# With this, the point object that we get will have its x and y coordinates initialized.
# How do we do this?
# We need to add special method in class called constructor.
# We add a function in class
# The name of function starts with __init__, init is short for initialized
# And this is the function or method that gets called when we create a new point object
# Right after self, we need to add two parameters for x and y
# And in the body we should use the values passed to intialize our object
# To initialize, we type our code like this: self.x = x

# self is reference to current object


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(20, 30)
# Now when we create a new object, self references that object in the memory, the same objet that we are referencing using this variable
# So using init method, we can initialize our objects and we refer to this method as a constructor
# This method is used to construct or create an object
print(point.x)  # 20
# We can also change these values
point.x = 11
print(point.x)  # 11
