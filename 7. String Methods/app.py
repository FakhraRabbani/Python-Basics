course = 'Python for beginners'

# Built-in Function : len -> Count no of characters in the string
print(len(course))  # 20
# This function is useful when u receive input from user.
# For eg, when you fill out a form online, each input field often has a limit
# For eg, u may have a limit of 50 characters for name
# So using len function, we can enforce a limit on number of characters in an input fields, if user types more than limit we can display an error
# len -> General purpose function
# len, print -> General purpose functions, They are not methods


# STRING METHODS

# Function for converting all strings character to upperCase or lower Case
# To access these functions, we use dot operator
print(course.upper())  # PYTHON FOR BEGINNERS
# If a function is specific to something, we call that function method, because this upper function is specific to strings, we can say it method
# This upper method doesnt change or modify our string, it creates a new string and returns it
print(course) # Python for beginners

# Converting string to lower case
print(course.lower())  # python for beginners


# Find characters or a sequence of characters in a string -> FIND METHOD
print(course.find('P'))  # 0
# In find method, we pass a character like P and it returns index of the first occurence of that character
print(course.find('o'))  # 4
# Find method -> Case Sensitive
print(course.find('O')) # -1
# We get -1 for upperCase O becayse we dont have uperCase O in our string

# We can also pass sequence of characters
print(course.find('beginners')) # 11
# We get 11 because the word beginner starts with index 11


# Replacing a character or a sequence of characters -> REPLACE METHOD
print(course.replace('beginners', 'Absolute Beginners')) #Python for Absolute Beginners
# This method is also Case Sensitive
print(course.replace('Beginners', 'Absolute Beginners')) #Python for beginners
# Now its not gonna replace because we dont have Beginners in our string, we have beginners

# We can also replace a single character
print(course.replace('P', 'J')) # Jython for beginners


# Check existence of a character or sequence of characters in ur string -> IN OPERATOR
# Lets check if Python is in our string
print('Python' in course)  # True
# This expression produces a boolean value
print('python' in course)  # False

# Find method -> Returns index of character or sequence of characters
# In operator -> Produce a boolean value, do we have this or not
