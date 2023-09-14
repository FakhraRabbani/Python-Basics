
# We use for loop to iterate over items of a collection, such as a string.
# The variable we define in for loop is called loop variable

# With this for loop, we can iterate over a string and in each iteration, the item variable will hold one character at a time
# In the first iteration, it will se to P, then in second iteration it will set to y and so on

for item in 'Python':
    print(item)
# With this each character is printed on a new line

# In python, we define LISTS using square brackets
# A LIST is simply a list of items, a list of numbers, a list of customers, a list of emails, whatever

for item in ['Fakhra', 'Hajra', 'Sarah']:
    print(item)
# In each iteration, we get one name and print it on a new line

# We can also loop over list of numbers
for item in [1, 2, 3, 4]:
    print(item)
# We get each number on new line

# What if we want a list of numbers?
# We dont want to explicitly type out a list with lets say 100 or 1000 numbers, we dont want to type, 5, 6, 7 all the way to 100
# That is when we use the range function

# Built-in Function -> RANGE
# range function is used for creating a range of numbers.
# So we give it a number like 10
for item in range(10):
    print(item)
# We get numbers from 0 to 9. So 10 is not included

# When we call the range function, this range creates an object, its not a list
# Its a special kind of object we can iterate over, in each iteration this object will spit out a new number.

# We can also work with a range of numbers here
# Lets say u want to start from 5 and go all the way to 10
for item in range(5, 10):
    print(item)
# Now we have numbers 5, 6, 7, 8, 9

# Also this range function can optionally take a step, so we can pass two as a step to this function
for item in range(5, 10, 2):
    print(item)
# 5, 7, 9
# Our first number is 5 and then we go 2 steps further to 7 and then 2 steps further to 9












