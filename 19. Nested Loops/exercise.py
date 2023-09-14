# Using nested loop, print F shape like this
# *****
# **
# *****
# **
# **

# HINT: First of all we have this list called numbers
numbers = [5, 2, 5, 2, 2]
# These values in list determine no of x's we have in each line

# TIP: USing a for...loop u need to iterate over this list
# In each iteration u get one number, this number determines the number of x's to be displayed on that particular line
# If we multiply 'x' by 5, we get 5 x's
# I dont want u to do this
# I want u to use an inner loop here to generate a string that contains 5 x's

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)