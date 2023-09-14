# We need to break our code into maintainable, manageable chunks which we call functions
# So function is a container for a few lines of code that perform a specific task
# For eg, u learned about few of the built-in functions in python like print and input
# Each of these functions have a purpose. They know how to perform a specific task.
# So when we build large complex prgrms, we should break up our code into smaller reusable chunks which we call functions to better organize our code.

# Lets write a simple prgrm for printing a greeting msg.
print('Hi there!')
print('Welcome abroad')
# This is a simple prgrm with 2 lines of code.
# Lets say we are gonna need these 2 lines in other prgrms so we can put them in a function that we can reuse
# We start with def which is a reserved keyword in python short for define.
# When python interpreter sees this, it knows that we are defining a function
# Next we need to give our function a name lets say greet_user
# After that we add parenthesis followed by colon

# greet_user()  # We cant call a function before defining it
def greet_user():
    print("Hi there!")
    print("Welcome abroad")


print("Start")
# Calling function
greet_user()
print("Finish")
