# Creating functions that return values
def square(number):
    return number * number

# We can return values to caller of our functions
# square(3) just returns a value like input function
result = square(3)
print(result)  # 9

# We can also pass this function directly inside of print function without defining a variable
print(square(2))  # 4

# What happens if we dont use the return statement in our function?
# In last eg, we used print statement

def the_square(number):
    print(number * number)

print(the_square(5))

# With this we see two things on terminal, the number 25 and None
# When Python interpreter executes this code, first it will call the_square function where we calculate square and print it on terminal
# That is the reason we see 25 on terminal

# By default all the functions return a value none.
# So if u dont have a return statement, by default python returns none
# None is an object that represents the absence of a value. Its like nothing or null in c, c++, js.
# In this eg, we didnt had the return statement and by default python returned none from this function
# So after this the_square function is executed, the value none is returnned and passed as an argument to the print function.
# That is the reason we see none on the terminal in second line



# By default, all functions in Python return none.
# You can change that, so if u have a function that calculates something, u can return the result using the return statement
