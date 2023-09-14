# A module in python is basically a file with some python code.
# We use modules to organize our codes into files just like sections in a super market.
# When u go to super market, there are different sections for fruits, vegetables, cleaning products, and so on.
# We dont have one section with all products in super market.
# We have same concept in programming.
# So instead of writing all our code, all functions and classes in app.py, we want to break up our code into multiple files.
# We refer to each file as a module.
# With this our code gets better and organized. We also have the ability to reuse our code.

# I have defined two functions to convert weight from pounds to kgs and vice versa
# def lbs_to_kg(weight):
#    return weight * 0.45


# def kgs_to_lbs(weight):
#    return weight / 0.45


# Now we can take these two functions and put them in a separate module called converters
# Then we can import the module into any prgrm that needs these converter functions.
# Lets add a new fil and call it converters .py
# Cut all the above code and paste in converters.py
# With this, we cleaned our app module. It is not bloated with different functions
# As we write more functions, we put them in their corresponding module.
# A module should contain all the related functions and classes

# Now we want to import converters module into our app module
import converters

# This converter is an object, so we can use dot operator to access its members
# Currently we have defined two functions in module.
print(converters.kgs_to_lbs(70))  # 155.55555555555554

# There is also another syntax for importing modules.
# Instead of importing the entire module, we can import specific functions from that module.
# We type from. Then we add the name of our modules, so converters and then import
# If u press control and space u can see all functions defined in this module.
# So we can grab one of those functions
# With this we can also directly call the function  just like if the function defined in this file

from converters import kgs_to_lbs
print(kgs_to_lbs(100))  # 222.22222222222223

# Compare what we have on line 42 with line 32
# On line 32, we have to prefix the function with name of an object converters. So we have to type converters. and then we will be able to access the function
# In contrast, when we import a specific function from our module, then we can easily call that function without prefixing it with the module name.


# We use modules to better organize our code. Instead of writing all the code, instead of writing all the functions in one file, u break up our code across multiple files.
# each file is called a module and it should contain all the related functions and classes
# Then we can import a module into another module
# In this case, we are importing the converters module into our app module
# and as u saw there are 2 ways to import module
