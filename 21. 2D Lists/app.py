# In Math, we have a concept called matrix, which is like a rectangular array of numbers
# [
#    1 2 3
#    4 5 6
#    7 8 9
#]
# So we have a rectangluar array of numbers
# You have rows and columns. So this is 3 by 3 matrix
# Now we can model this in python using a 2 dimensional list
# A 2dLIST is a list where ach item in that list is another list
# We can define matrix like this, each item in list will be a list and each item list will represent a row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# We have 2d list now
# This is how we can implement a matrix in Python
# Now we can access an individual item in our matrix
# How do we access 1 ?
# First we neeed to go and get the first item -> [1, 2, 3]
# So by matrix[0], we get this list -> [1, 2, 3]
# This expression matrix[0] returns another list which is inner list
# In the inner list [1, 2, 3], lets say we want to access second item
# matrix[0][1], 1 is index in inner list of 2
print(matrix[0][1])  # 2
# So using two square brackets, we can access individual items in our matrix
# We can also modify these values
matrix[0][1] = 20
print(matrix[0][1])  # 20
# We can also use nested loops here to iterate over all the items in this matrix
# for row in matrix:
# With this loop, we will iterate over our matrix lits. In each iteration row will contain 1 list(1 item)
# Here we need to use an inner loop. We need to loop over row ehich is a list of items
# for item in row:
for row in matrix:
    for item in row:
        print(item)
# 1 20 3 4 5 6 7 8 9
# We get all the items