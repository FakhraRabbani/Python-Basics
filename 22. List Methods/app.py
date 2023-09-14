numbers = [5, 2, 2,  1, 7, 4]

# We can add new items to list, remove existing items, check for existence of an item
# When we type (number.) we can see all the functions or more accurately the methods that are available in our list objects

# ADD NEW ITEM -> Append Method
numbers.append(20)
print(numbers)  # [5, 2, 1, 7, 4, 20]
# 20 is added to end of string

# What if u want to add a number in beginning or somewhere at middle
# INSERT METHOD
# This method takes 2 values
# First value we need to pass is index, so this is the index at which we want to insert the new item
# Lets say we want to add an item at beginning of list, so we pass index position of 0
# Then the second value is actual object we want to add to this list
numbers.insert(0, 10)
print(numbers)  # [10, 5, 2, 1, 7, 4, 20]

# REMOVE ITEM -> Remove Method
# We call remove and pass the item that we want to reemove
numbers.remove(5)
print(numbers)  # [10, 2, 1, 7, 4, 20]
# Now 5 is gone

# Pop Method
# With this, we can remove last item in a list
numbers.pop()
print(numbers)  # [10, 2, 1, 7, 4]

# Check Existence of an item -> Index Method
# This returns index of first occurrence of the item
print(numbers.index(2))  # 1
# What if we pass a number that doesnt exist?
# print(numbers.index(50))
# ValueError: 50 is not in list, We get value error

# There is also another way to check existence of an item
# In Opeartor
print(50 in numbers)  # False
# We get a boolean value
# Unlike index method, this expression doesnt generate an error. So it is safer to use

# Counting occurence of an item
# Count Method
print(numbers.count(2))  # 2
# It returns 2 because we have two 2's in our list

# Sort Method
# print(numbers.sort())  # None
# We got none
# None is an object in Python that represents the absence of a value
# So this sort method doesnt really return any value, it just simply sorts the list
# So instead of printing the return value, we simply call it to sort our list and then print our list
numbers.sort()
print(numbers)  # [1, 2, 2, 4, 7, 10]
# All items are sorted in ascending order

# We can also sort the items in descending order
# Reverse Method
numbers.reverse()
print(numbers)  # [10, 7, 4, 2, 2, 1]

# Copy Method
# With this method, u can get a copy of list
numbers2 = numbers.copy()
# If we make changes to our original list of numbers now, thats not gonna effect the copied numbers2list
print(numbers)  # [10, 7, 4, 2, 2, 1]
print(numbers2)  # [10, 7, 4, 2, 2, 1]
numbers.append(10)
print(numbers)  # [10, 7, 4, 2, 2, 1, 10]
print(numbers2)  # [10, 7, 4, 2, 2, 1]
# These both are 2 independent lists

# If u want to remove all the items in the list, u can call the clear method
# Clear Method
numbers.clear()
print(numbers)  # []


