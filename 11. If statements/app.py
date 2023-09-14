# Rules for our prgrm
# If its hot -> Its a hot day .... Drink plenty of water
# Otherwise If its cold -> Its a cold day .... Wear warm clothes
# Otherwise -> Its a lovely day

# its_hot = True
its_hot = False

# if its_hot:
#    print("Its a hot day")
#   print("Drink plenty of water")
#print("Enjoy your day")

# If condition is false, only 3rd print statement will be executed.
# If condition is true, first and second will also be excuted and also 3rd

if its_hot:
    print("Its a hot day")
    print("Drink plenty of water")
else:
    print("Its a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

# The else block having 2 print statements will be executed if the if condition is false

# We can also add another condition
# its_cold = True
its_cold = False

# elif -> short for else if

if its_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif its_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")