# Packages are another way to organize our code
# Previously, we had three modules.
# But in real project there can be hundreds to thousands of modules.
# We dont want our proect to be floated with so many files.
# Better approach is to organize related modules inside of a package

# Package is a container for multiple modules
# In file system terms, a pckg is a directory or folder

# So in our projects, we can add dictionary
# In that dictionary, we can add all the directed modules

# Think of a mall
# When u go to a mall or a shopping center, there are different sections for men, women and kids clothing
# So that is like a pckg
# Now when u go to mens section, there are different areas for different kinds of products
# So we have section for shoes, t shirts, jackets and so on, so each of these is like a module

# How to create and use packages in python?
# Right click on ur project folder and add a new directory
# Lets call this directory e-commerce
# So we are going to create a package called e commerce
# In this pckg, we are going to have all the modules related for an ecommerce application
# For eg, we can have modules for sales, shipping, customer service and so on

# We have an empty directory
# In order to convert this into a package, we need to add a special file in it.
# So right click this directory and add a new python file
# Call the file double underscore init double underscore __init__
# This is a special convention in Python.
# When python interpreter sees a file with this name and name in directory, it treats that directory as a package

# We also have a short cut in pycharm
# Right click the project, and go to new then python package
# Pycharm automatically creates this file for us, so we dont have to manually create it.

# Now in this package, lets add a new module and lets call it shipping
# In this shipping module, i want a function for calculating the shipping costs.

# Now lets sat we want to import shipping module into our app module
# With this new structure, shipping module is part of ecommerce package.
# We can not import it directly
# You have to start from the ecommerce package.



# There are two ways to import this module
# We can import the entire module or we can import one of its functions or classes

# We are going to import the entire module
# We type import then name of our package, then dot then module in the package we want
import ecommerce.shipping
# We have to prefix it with the name of our package

# Now to access any of the functions or classes in this module, we have to type packagename.modulename.functioncall
ecommerce.shipping.calc_shipping()  # calc_shipping

# However with this approach, everytime u want to call one of the functions to this module, we will have to prefix it with ecommerce.shipping...
# This is very verbose


# So when working with packages, we often use the second approach using the from statement
from ecommerce.shipping import calc_shipping

# Now we dont need to prefix the function with ecommerce.shipping and we can call it multiple times in this module
# So our code is a little bit shorter
calc_shipping()  # calc_shipping
calc_shipping()  # calc_shipping
calc_shipping()  # calc_shipping

# What if we want to import multiple functions in shipping module?
# We can either import them here by coma like from ecommerce.shipping import calc_shipping, calc_tax
# Or we can import entire module and then access all the functions or classes in that module.

# Importing entire module
from ecommerce import shipping
# Now the shipping module is an object, so we can access all the functions and classes defined in it using dot operator

shipping.calc_shipping()  # calc_shipping

# With using from, we can either start from package and import a specific module or we can start from package.module and then import a specific function

# Packages are useful especially when u want to work with framework like django
# We use django for building web applications with python