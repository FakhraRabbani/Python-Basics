# Nested loop basically means adding one loop inside of another loop

# With this, we can easily generate a list of coordinates.
# So a coordinate as u know is a combination of x and y
# (x, y) -> (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
# We can easily generate these coordinates using nested loops

# With this loop we can generate values for x coordinate
for x in range(4):
    print(x)
# We get values -> 0, 1, 2, 3

# Now for each x like zero, we should generate a few y values.
# So this is where we use a nested loop

# So inside of loop, we are going to add another loop
# So instead of just printing x, first we want to add another loop for y in range lets say 3
# Now we can print x and y together
# We use formatted string to display like coordinates
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
# (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) (2, 1) (2, 2) (3, 0) (3, 1) (3, 2)
# So we have these coordinates
# In first iteration of our outer loop, x is zero. Now we are on line 2 here we a new loop which we call an inner loop
# In this inner loop, in first iteration y is going to be zero so we ptint 0, 0 on terminal
# Now control goes back to line 2 or our inner loop. In second iteration of inner loop, y will se to 1 but we are still in first iteration of outer looop
# So x is still 0 and y is incremented to 1
# Once again in third iteration of inner loop, x is 0 y is 2
# After inner loop completes, control goes back to outer loop or line 2
# At this point we are going to be in second iteration of outer loop. So x will be 1
# Then control will go to inner loop and it will execute from y = 0 to y = 2, 3 times (range(3)) and x will be 1 in whole inner loop
