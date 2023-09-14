# Built-in modules in Python
# Where we can find the standard library?
# Search for python 3, module index on google
# We can see documentation for all the modules built into python
# For eg we have modules for working with date and time, we have modules for sending emails, for encoding values, and many

# Built in module for generating random values
# First we import the random module
import random

# It is stored in external libraries, then expand python 3, and then in python 3 library folder we have all built in modules in python

# Now we have this object random as we have imported the module
# We can use dot operator to access its methods.
# It has a random method
# Everytime we call it, it generates a random value between 0 and 1
# So here we can do a for...loop
# Range function is used to create a range object
# With the following loop, we can execute the code 3 times
for i in range(3):
    print(random.random())

# 0.9748768065972797
# 0.4535689022738678
# 0.1771621156615658

# In each iteration we get a new random value between 0 and 1

# What if we want a random value for a particular age?
# Lets say we want a random value between 10 and 20
# There is another method in this module randint
# We pass 2 arguments in it to specify our range
for i in range(3):
    print(random.randint(10, 20))

# 12
# 10
# 13

# We get different values everytime we run our prgrm

members = ['Fakhra', 'Aishwariya', 'Sairah', 'Sunaina']
# We can call random.choice and pass the list
# This method randomly picks a member from the list and returns it
leader = random.choice(members)
print(leader)


