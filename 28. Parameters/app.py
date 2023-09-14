def greet_user():
    print("Hi there!")
    print("Welcome abroad")

print("Start")
greet_user()
print("Finish")

# What is the difference between print function and the greet_user function?
# The difference is that print function takes some information,its the msg that we want to print
# But our greet function doesnt take any information
# Wouldnt it be nicer if we could pass the user name and instead of Hi there, we can print user name

# Inside of parenthesis, we add parameters
# Parameters -> Place holders for receiving information

def greet_the_user(name):
    print(f"Hi {name}!")
    print("Welcome abroad")


print("Start")
greet_the_user("Fakhra")
print("Finish")

# When we pass this value, name paramter will be set to Fakhra
# So it will act like a local variable that we defined inside of the function
# With parameters, we can receive information in our functions

# We can reuse our function and pass it a different value
greet_the_user("Aisha")

# Imagine if we didnt have this function, you would have to repeat the line twice, once for Hi Fakhra, once for Hi Aisha

# When our function has a parameter, we are obligated to pass a value for that parameter
# If we wont, we will get type error
# greet_the_user()  # TypeError: greet_the_user() missing 1 required positional argument: 'name'

# Argument in programming is the value that we supply to a function
# Fakhra and Aisha are the arguments that we pass to the name parameter

# Parameters are placeholders that we define in our function for receiving information
# Arguments are the actual pieces of information that we supply to these functions.

# We can also define multiple parameters

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome abroad")

greet("Fakhra", "Rabbani")