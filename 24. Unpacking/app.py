# Defining a tuple
coordinates = (1, 2, 3)
# Imagine these are the coordinates for x, y and z
# Lets say we want to get these values and use them in a few epressions, a few complex expressions in our prgrm.
# Maybe we want to include them as part of a large complex formula
# So together we will have to write code like this
# coordinates[0] * coordinates[1] * coordinates[2]
# Like this our code is getting a little bit long
# A better approach is to get these values and store them in separate variables
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# Now instead of repeating coordinates word multiple times, we can simply work with these x, y, z variables
# x * y * z
# This is better

# But in Python we have a powerful feature called unpacking and with that we can achieve the same result with far less code.
# So we can define our variables x, y, z and set them to our tuple
x, y, z = coordinates
# This line 19 is exactly identical to what we have on line 10, 11, 12
# So this is shorthand to achieve the same result

# When python interpreter sees this statement, it will get the first item in the tuple and assign it to x variable
# Then it will get the second item in the tuple and assign it to second variable ans similarly third item to third variable
# So we are unpacking this tuple into 3 variables
print(x)  # 1
print(y)  # 2
print(z)  # 3

# WE can use this feature for lists as well
numbers = [1, 2, 3]
a, b, c = numbers
print(a)  # 1
print(b)  # 2
print(c)  # 3


