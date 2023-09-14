# Handle Errors

# Lets start by writing a small prgrm asking user for age
age = int(input("Age: "))
print(age)

# Process finished with exit code 0
# exit code 0 means our prgrm terminated successfully, there were no errors

# What if we type abcd instead of a numerical value?
# ValueError: invalid literal for int() with base 10: 'abcd'
# We get a value error
# Process finished with exit code 1
# exit code 1 means that our exit code crashed

# 0 -> Success
# Anything except 0 -> Crash

# Now u dont want ur entire prgrm to crash if user enters wrong input
# U should handle the situation and print a proper error msg

# Look at the error, we are getting value error

# How we handle these errors?
# In python we have construct called try except. We use that to handle errors

try:
    age = int(input("Your Age: "))
    print(age)
except ValueError:
    print("Invalid Value")

# With try, we are saying that hey go ahead and try these 2 lines of code
# If u encounter an errror of type ValueError, then try this msg on terminal
# We refer to this kind of error as an exception
# Exception is kind of error that crashes our prgrm. With try except, it will catch error and prgrm will not crash


try:
    age = int(input("Enter Your Age: "))
    income = 2000
    risk = income / age
except ValueError:
    print("Invalid Value")

# If we enter 0, we get error -> ZeroDivisionError: division by zero
# Process finished with exit code 1
# So we are not catching this kind of exception with except block
# This except block is only catching exceptions of type value error
# So in situations like this, we should handle different kind of exceptions
# We can add another except statement for an exception of type 0

try:
    age = int(input("Hey Enter Your Age: "))
    income = 2000
    risk = income / age
except ZeroDivisionError:
    print("Age cant be zero")
except ValueError:
    print("Invalid Value")

# Age cant be zero.  We get this error msg and with successful execution of code -> Process finished with exit code 0
