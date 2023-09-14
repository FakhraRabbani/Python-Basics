# Tuples are similar to lists. So we can use them to store a list of items
# But unlike lists, we can not modify them, we cant add new items, we cant remove existing items
# Tuples are immutable
# We can not mutate or change them.

# Defining a list of numbers
number = [1, 2, 3, 4]
# We use square brackets to deine a list

# We use parenthesis to define tuples
numbers = (1, 2, 3, 4)
# Now we hae=ve tuple
# If we type numbers. we can see we dont have append or insert methods, so we cant add new items to this tuple
# We also dont have remove, clear, pop. So we cant remove any of these items
# We only have 2 methods, count and index
# Count Method -> Count number of occurrences in an item
# Index Method -> To find index of the first occurrence of an item
# WE only get information about tuple. We cant change it

# Accessing individual items
print(numbers[0])  # 1

# Try changing an item -> Error
# numbers[0] = 5
# TypeError: 'tuple' object does not support item assignment


