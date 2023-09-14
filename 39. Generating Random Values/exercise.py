# Write a prgrm to roll a dice
# Everytime we run this prgrm, we get a different value.

# Define a class called Dice
# In this class, we are going to have a roll method
# Everytime we call this role method, we get a tuple
# Tuple is a list of values but values cant be changed, added or removed.
# Its like a read only list
# Everytime we call roll method, we should get tuple of two random values

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second= random.randint(1, 6)
        return first, second


# In python when u need to return a tuple from function, u dont need to add parenthesis around. Python will automatically interpret it as a tuple

# Creating object of Dice type
dice = Dice()
print(dice.roll())


