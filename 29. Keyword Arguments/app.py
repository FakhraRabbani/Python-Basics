# Whenever we define parameters for our functions, we should always supply values otherwise we will get an error
# We refer to arguments as positional arguments, they are positioned or order matters
# First argument is for first parameter, second argument is for second parameter and so on

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

greet_user("Smith", "John") # Hi Smith John

# But in Python, we also have keyword arguments and with those the position doesnt matter
# Keyword argument is the combination of having the parameter name, followed by its value like first_name="John"
greet_user(last_name="Smith", first_name="John")  # Hi John Smith

# These keywords arguments are useful when we supply numerical values, when we get confused which value is for which

# cal_cost(50 , 5, 0.1)
# Someone reading this code, may not be sure what these 3 values represent
# In this case, we can improve the reusablity of code by using keyword arguments
# cal_cost(total=50 , shipping=5, discount=0.1)
# Now if u give this code to someone else, they can immediately tell what these values represent


# For the most part, use positional arguments
# But if u are dealing with functions that take numerical values, see if u can improve the readability of ur code by using keyword arguments
# U simply prefix the arguments that u pass with the name of parameters and this will increase the readability of ur code

# These keyword arguments should always come after positional arguments
# greet_user(first_name="Fakhra", "Rabbani")  # SyntaxError: positional argument follows keyword argument
# We get error
# You should always use positional arguments first and then keyword arguments
greet_user("Fakhra", last_name="Rabbani")  # Hi Fakhra Rabbani
