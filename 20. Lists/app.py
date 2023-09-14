# Defining list of names
names = ['Fakhra', 'Maria', 'Sarah', 'Alisha', 'Sonia']
print(names)
# ['Fakhra', 'Maria', 'Sarah', 'Alisha', 'Sonia']
# We get exact thing on terminal what we defined

# We can also access individual element using an index just like how we can access an individual character in a string using an index
print(names[0])  # Fakhra
print(names[2])  # Sarah

# We can also pass a negative index here, so -1 refers to last item in the list
print(names[-1])  # Sonia
print(names[-2])  # Alisha

# We can also use a colon to select a range of items
# For eg, if u pass 2 colon 2:, this will get all items from index 2 all the way to end of list
print(names[2:])  # ['Sarah', 'Alisha', 'Sonia']

# We can also specify an end index lets say 4, so it will give all items up to index 4 but excluding item at this index
print(names[2:4])  # ['Sarah', 'Alisha']

# We also have default values here
# If we dont write end index like [2:], this is going to return all items from index of 2 to end of list

# If we also leave out start index [:], it will return all items from 0 as default index from beginning to end of list

# Just like strings, these square brackets here dont modify our original list
# They simply return a new list
print(names)  # ['Fakhra', 'Maria', 'Sarah', 'Alisha', 'Sonia']
# Our original list of names is not affected


# We can also modify any of the items in the list
names[1] = 'Mairah'
print(names)  # ['Fakhra', 'Mairah', 'Sarah', 'Alisha', 'Sonia']


