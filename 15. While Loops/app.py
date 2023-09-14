# We write a while statement and right after that we type a condition followed by a colon
# As long as the condition is true, the quote that we write in the block will be repeatedly executed.

i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')
# If we wont increment i, i will be 1 forever and we will end up with an infinite loop

# With this expression '*' * i, we can repeat a string
# '*' * 1 -> *
# '*' * 2 -> **
# '*' * 3 -> ***
# '*' * 4 -> ****
# '*' * 5 -> *****

# We get a triangle type shape

j = 1
while j <= 5:
    print('*' * j)
    j = j + 1
print('Done')
