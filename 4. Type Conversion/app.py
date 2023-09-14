# Write a prgrm that will ask the year that we wre born in, and then it will calculate our age and print it on terminal

# Input function
birth_year = input('Birth Year: ')
# Caclulating age
# age = 2023 - birth_year -> Type error: unsupported operand type(s) for -: 'int' and 'str'
# Here we are subtracting a string from an integer and python doesnt know what to do

# The birth_year is treated as a string. Whatever we type in terminal is treated as a string, even if u type a no on terminal
# When we run this prgrm, the birth_yaer variable will set to a string of 4 characters like '2004'
# This string '2004' and number 2004 are differnet

# To fix this prblm, we need to convert the input '2004' into an integer 2004, then we will be able to subtract it from 2023

# BUILT-IN FUNCTIONS FOR TYPE CONVERSION
# int() -> converts a string into integer
# float() -> converts a string to float
# bool() -> converts a string into boolean value

# We need to pass birth_year variable to int function like this int(birth_year), it will convert it into integer
age = 2023 - int(birth_year)

# Print
print(age)

# Function for getting type of variables -> type()
print(type((birth_year)))
print(type((age)))

# Whenever we use input function, we always get a string
# If u are expecting a numerical value, u should always convert that string into integer or a float

