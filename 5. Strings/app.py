course = 'Python for beginners'

# course = 'Python's Course for beginners' -> Wrong Way

course = "Python's Course for beginners"

print(course)

# course = "Python for "beginners""  -> Wrong Way
course = 'Python for "beginners"'
print(course)

# String of multiple lines like email -> Use three starting and ending single or double quotes
course = '''
Hi Fakhra,

Here is our first email to you.

Thank you,
The support team

'''

print(course)

course = 'Python for beginners'
# [] Square brackets to get a character at a given index in string
print(course[0]) # P
# We can also use negative index
# With negative index, we can get characters starting from the end
# 0 is index of first character, -1 is the index of last character
print(course[-1]) #s

# We can also extract few characters instead of one character
# [0:3] -> Python interpreter will return all the characters starting from 0 index to index 2, it doesnt return the character at index 3
print(course[0:3]) #Pyt

# We also have default values for start and end index, If we dont supply end index, it will return all characters to the end of string
print(course[0:]) # Python for beginners

# If we change start index to 1, this will exclude the first character
print(course[1:]) # ython for beginners

# Similarly, we have default value for starting index
# If we dont supply start index but add an end index like 5, python interpreter will assume 0 as the start index
print(course[:5]) #Pytho

# What if we leave both the start and end index?
# In this case, 0 will be assumed as start index, and length of the string will assume as end index
print(course[:])  # Python for beginners
# So with this syntax [:], u can basically copy or clone a string
another = course[:]
print(another) # Python for beginners