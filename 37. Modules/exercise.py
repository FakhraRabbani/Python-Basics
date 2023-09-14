# You had an exercise before for finding the largest number in the list.
numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# This code currently has no organization.
# We dont have any functionss, we dont have any modules
# We wrote all the code in app.py   Thats okay for small prgrms
# But as your prgrm grows, u need to properly organize your code into functions, classes and modules

# So in this exercise, write a function call it find_max
# This function should take a list, and return the largest number in the list
# After this, put this function in a separate module called utils
# In this module, we are going to have bunch of utility functions
# Then import the utils module into current module and call this function find_max
# Get result and print it on terminal

from utils import find_max

number = [10, 3, 11, 2]
maximum = find_max(number)
print(maximum) # 11

# We have built-in max function already. We are over-writing it. Thats why we are getting a warning
# So we wont use max. Rename it



